"""Visual — Estudativo · Questão de Matemática 022 (aula horizontal 1920x1080): ENEM 2025, questão 143, o recorde de
Usain Bolt (10,00 − 9,58). Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = os números do enunciado (10,00 e 9,58), ciano = os empréstimos (a ferramenta), menta = o
resultado certo e a conferência, coral = o "não dá" e os resultados das armadilhas (0,52 e 1,42).
Figura principal: a conta armada (conta()), com os algarismos alinhados pela vírgula, os empréstimos escritos em cima
(o algarismo antigo riscado) e o resultado aparecendo da direita para a esquerda."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_022_matematica_recorde_bolt.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "shimmer", "02.b": "data", "02.c": "confirm", "03.b": "deny", "03.c": "data", "03.d": "confirm",
        "04.b": "lock", "05.b": "deny", "05.c": "data", "05.e": "impact", "06.c": "confirm", "06.d": "lock",
        "07.b": "deny", "07.c": "deny", "07.d": "alert", "08.c": "whoosh", "08.d": "alert", "10.a": "shimmer", "10.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 022", "QUESTÃO DE MATEMÁTICA · 022"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_dec=("TOOL 1 · WHAT EACH DIGIT IS WORTH", "FERRAMENTA 1 · O QUE CADA ALGARISMO VALE"),
    s_emp=("TOOL 2 · BORROWING", "FERRAMENTA 2 · SUBTRAÇÃO COM EMPRÉSTIMO"),
    s_armar=("STEP 1 · SET UP THE SUBTRACTION", "PASSO 1 · ARMAR A CONTA"),
    s_conta=("STEP 2 · RIGHT TO LEFT", "PASSO 2 · DA DIREITA PARA A ESQUERDA"), s_conf=("STEP 3 · CHECK", "PASSO 3 · CONFERIR"),
    s_peg=("THE TRAPS", "AS ARMADILHAS"), s_gen=("ON THE TRACK · AND A CHALLENGE", "NA PISTA · E UM DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 143", "ENEM 2025 · questão 143"), rasos=("100 m sprint", "100 metros rasos"),
    ref=("benchmark: ", "referência: "), bolt=("Bolt, 2009: ", "Bolt, 2009: "), dif=("difference = ", "diferença = "),
    p_sub=("DECIMAL SUBTRACTION", "SUBTRAÇÃO COM DECIMAIS"), p_arm=("2 TRAPS", "2 ARMADILHAS"),
    inteiros=("ones", "inteiros"), decimos=("tenths", "décimos"), centesimos=("hundredths", "centésimos"),
    v9=("9 ones", "9 inteiros"), v5=("5 tenths = 0.5", "5 décimos = 0,5"), v8=("8 hundredths = 0.08", "8 centésimos = 0,08"),
    zeros=("zeros on the right don't change it", "zeros à direita não mudam o número"),
    naoda=("2 − 7: can't", "2 − 7: não dá"), pede=("borrow 1 ten: 12", "pede 1 dezena: 12"),
    regra=("DECIMAL POINT UNDER DECIMAL POINT", "VÍRGULA EMBAIXO DE VÍRGULA"),
    maior=("on top: the larger number", "em cima: o maior"),
    naoda2=("0 − 8: can't, and the neighbor is 0", "0 − 8: não dá, e o vizinho é 0"),
    vira=("10 = 9 + 0.9 + 0.10", "10 = 9 + 0,9 + 0,10"), vem=("the borrow comes from the 10", "o empréstimo vem do 10"),
    soma=("difference + Bolt = benchmark", "diferença + Bolt = referência"),
    peg_c=("C · 0.52: forgot it in the tenths", "C · 0,52: esqueceu nos décimos"),
    peg_e=("E · 1.42: forgot it in the ones", "E · 1,42: esqueceu nos inteiros"),
    vel=("100 m in 10 s → 10 m per second", "100 m em 10 s → 10 m por segundo"), const=("(same speed the whole time)", "(mesma velocidade o tempo todo)"),
    atras=("behind", "atrás"), desafio=("an athlete ran 9.87 s", "um atleta fez 9,87 s"),
    lento=("how much slower than Bolt?", "quanto mais lento que o Bolt?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["fill with zeros, point under point", "right to left, borrowing", "take each borrow off its neighbor",
             "check with addition"],
            ["complete com zeros, vírgula embaixo de vírgula", "da direita para a esquerda, com empréstimo",
             "desconte cada empréstimo na vizinha", "confira pela soma"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Decimal", "numbers"), ("Adding and subtracting", "decimals"), ("Average", "speed")],
           [("Números", "decimais"), ("Adição e subtração", "de decimais"), ("Velocidade", "média")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("dois mil e nove", "2009"),
    ("nove vírgula cinquenta e oito", "9,58"), ("dez vírgula zero zero", "10,00"), ("zero vírgula quarenta e dois", "0,42"),
    ("zero vírgula cinquenta e dois", "0,52"), ("um vírgula quarenta e dois", "1,42"), ("dez vírgula um", "10,1"),
    ("noventa e cinco vírgula oito", "95,8"), ("quatro vírgula dois", "4,2"), ("nove vírgula oitenta e sete", "9,87"),
    ("passo um", "Passo 1"), ("passo dois", "Passo 2"), ("passo três", "Passo 3"), ("letra c", "letra C"), ("letra e", "letra E")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("dez", "menos"), ("vai", "dez")}
n_ = lambda s: s.replace(",", ".") if EN else s   # noqa: E731  vírgula decimal → ponto no inglês


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- a conta armada
CW = 100   # largura de uma coluna (algarismo)


def _xs(s, cx):
    """x de cada caractere de s, alinhado pela vírgula em cx (sem vírgula: as unidades terminam em cx)"""
    ref = s.index(",") if "," in s else len(s)
    out = []
    for i in range(len(s)):
        if i < ref:
            out.append(cx - 0.3 * CW - (ref - i - 0.5) * CW)
        elif i == ref:
            out.append(cx)
        else:
            out.append(cx + 0.3 * CW + (i - ref - 0.5) * CW)
    return out


def conta(c, a, t, cx, y0, top, bot, sinal="−", res=None, res_vis=None, res_col=MNT, novos=None, riscos=(), hl=(),
          hl_col=AMB, cores_res=None, size=104, bot_a=1.0, linha_a=1.0):
    """conta armada: top e bot com o mesmo comprimento (' ' = vazio); res = resultado (mesmo alinhamento),
    res_vis = índices já escritos; novos = {índice: texto do empréstimo em cima}; riscos = índices riscados em top;
    hl = colunas em destaque; cores_res = {índice: cor} (ex.: o algarismo errado em coral)"""
    if a <= 0:
        return
    xs = _xs(top, cx)
    y1, y2, yr = y0, y0 + 140, y0 + 300
    for i in hl:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[i] - CW * 0.46, y1 - 120, CW * 0.92, (yr if res else y2) - y1 + 170), 18, 18)
        c.drawRRect(r, blur_paint(hl_col, 0.35 * a, 14))
        c.drawRRect(r, paint(hl_col, 0.12 * a))
        c.drawRRect(r, paint(hl_col, 0.8 * a, stroke=3))
    for i, ch in enumerate(top):
        if ch.strip():
            text_mid(c, ch, xs[i], y1, size, "black", AMB if ch != "," else WHITE, a * (0.45 if i in riscos else 1))
            if i in riscos:
                c.drawLine(xs[i] - 30, y1 + 34, xs[i] + 30, y1 - 34, paint(RED, a, stroke=7, cap_round=True))
    for i, s in (novos or {}).items():
        if s:
            text_mid(c, s, xs[i], y1 - 92, size * 0.5, "black", CYA, a)
    kb = a * bot_a
    for i, ch in enumerate(bot):
        if ch.strip():
            text_mid(c, ch, xs[i], y2, size, "black", AMB if ch != "," else WHITE, kb)
    text_mid(c, sinal, min(xs) - CW * 0.95, y2, size, "black", WHITE, kb)
    kl = a * linha_a
    if kl > 0:
        c.drawLine(min(xs) - CW * 1.4, y2 + 80, max(xs) + CW * 0.5, y2 + 80, paint(WHITE, kl, stroke=6, cap_round=True))
    if res:
        vis = range(len(res)) if res_vis is None else res_vis
        for i in vis:
            ch = res[i]
            if ch.strip():
                col = (cores_res or {}).get(i, res_col if ch != "," else WHITE)
                text_mid(c, ch, xs[i], yr, size, "black", col, a)


def _card_enunciado(c, a):
    img = _img_enunciado()
    w = 760
    h = img.height() * w / img.width()
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


OPS = [("A", "0,02"), ("B", "0,42"), ("C", "0,52"), ("D", "1,02"), ("E", "1,42")]


def opcoes(c, a, t, t0, certa="B", erradas=(), y=800):
    """linha A..E com os valores, a certa em caixa menta e as erradas riscadas"""
    for j, (le, v) in enumerate(OPS):
        x = BX0 + 130 + j * 160
        k = a * ep(t, t0 + j * 0.08, 0.2)
        col = MNT if le == certa else (RED if le in erradas else INK2)
        text_mid(c, le, x, y - 22, 44, "black", col, k)
        text_mid(c, n_(v), x, y + 30, 30, "bold", col if col != INK2 else WHITE, k)
        if le in erradas:
            cross(c, x + 40, y - 40, 20, k * ep(t, t0 + 0.6, 0.2))
    kk = a * ep(t, t0 + 0.6, 0.3)
    if kk > 0 and certa:
        j = "ABCDE".index(certa)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 130 + j * 160 - 66, y - 78, 132, 140), 18, 18)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["rasos"], RX, 340, a, 50, WHITE, "black")
    eq(c, [(L["ref"], INK2), (n_("10,00 s"), AMB)], 450, a * ep(t, ta + 3.0, 0.3), 54)
    eq(c, [(L["bolt"], INK2), (n_("9,58 s"), AMB)], 550, a * ep(t, tb + 1.2, 0.3), 54)
    eq(c, [(L["dif"], WHITE), ("?", CYA)], 690, a * ep(t, tc, 0.3), 58, box=CYA)
    kd = a * ep(t, td, 0.3)
    popill(c, L["p_sub"], RX - 160, 840, 26, CYA, BG0, kd, t, td + 0.2)
    popill(c, L["p_arm"], RX + 250, 840, 26, RED, BG0, kd, t, td + 1.6)


def b_decimais(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_dec"], a)
    kc = ep(t, tc, 0.4)
    k1 = a * (1 - kc)
    if k1 > 0:   # 9,58 com o valor de cada algarismo
        s = "9,58"
        xs = _xs(s, LX)
        cols = (AMB, WHITE, CYA, MNT)
        nomes = (L["inteiros"], "", L["decimos"], L["centesimos"])
        for i, ch in enumerate(s):
            kk = k1 * (ep(t, tb + 0.4 + 1.6 * [0, 0, 1, 2][i], 0.3) if t >= tb else 0.6)
            text_mid(c, ch, xs[i], 460, 200, "black", cols[i] if t >= tb else WHITE, max(k1 * 0.6, kk) if ch != "," else k1)
            if nomes[i]:
                label(c, nomes[i], xs[i], 620, kk if t >= tb else 0, 34, cols[i], "black")
    if kc > 0:   # 10 → 10,00: os zeros entram à direita, o 10 desliza para a esquerda
        kz = ep(t, tc + 1.8, 0.4)
        w10, wz = text_w("10", "black", 200), text_w(n_(",00"), "black", 200)
        x0 = LX - (w10 + wz * kz) / 2
        text(c, "10", x0, 470 + 72, 200, "black", AMB, a * kc, align="left")
        text(c, n_(",00"), x0 + w10, 470 + 72, 200, "black", MNT, a * kc * kz, align="left")
        label(c, L["zeros"], LX, 680, a * ep(t, tc + 3.0, 0.3), 34, INK2, "bold")
    board(c, a)
    for j, (key, col, tt) in enumerate((("v9", AMB, tb + 0.4), ("v5", CYA, tb + 2.0), ("v8", MNT, tb + 3.6))):
        label(c, n_(L[key]), RX, 290 + j * 90, a * ep(t, tt, 0.3), 46, col, "black")
    eq(c, [(n_("10 = 10,00"), MNT)], 610, a * ep(t, tc + 2.4, 0.3), 58, box=MNT)
    popill(c, L["zeros"], RX, 780, 30, AMB, BG0, a * ep(t, td, 0.3), t, td)


def b_emprestimo(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_emp"], a)
    kc = t >= tc + 0.8
    vis = [i for i, t0 in ((1, td + 0.4), (0, td + 2.4)) if t >= t0]
    conta(c, a * ep(t, tb, 0.3), t, LX + 60, 330, "52", "17", res="35", res_vis=vis,
          novos={0: "4", 1: "12"} if kc else None, riscos=(0, 1) if kc else (),
          hl=(1,) if tb + 1.6 <= t < td + 2.4 else ((0,) if t >= td + 2.4 and t < td + 4.0 else ()),
          hl_col=RED if t < tc else CYA)
    board(c, a)
    eq(c, [(L["naoda"], RED)], 300, a * ep(t, tb + 1.6, 0.3), 50)
    eq(c, [(L["pede"], CYA)], 430, a * ep(t, tc + 0.6, 0.3), 50, box=CYA)
    eq(c, [("12 − 7 = ", WHITE), ("5", MNT)], 570, a * ep(t, td + 0.4, 0.3), 54)
    eq(c, [("4 − 1 = ", WHITE), ("3", MNT)], 670, a * ep(t, td + 2.4, 0.3), 54)
    eq(c, [("52 − 17 = ", WHITE), ("35", MNT)], 800, a * ep(t, td + 4.0, 0.3), 56, box=MNT)


def b_armar(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_armar"], a)
    kb = ep(t, tb + 0.6, 0.4)
    conta(c, a, t, LX + 30, 360, "10,00", " 9,58", bot_a=ep(t, tc + 2.0, 0.3) if t >= tc else 0.0,
          linha_a=ep(t, tc + 2.0, 0.3) if t >= tc else 0.0, hl=(2,) if kb > 0 else ())
    if kb > 0:   # as colunas: inteiros, décimos, centésimos
        xs = _xs("10,00", LX + 30)
        for i, nome, col in ((1, L["inteiros"], AMB), (3, L["decimos"], CYA), (4, L["centesimos"], MNT)):
            kk = a * ep(t, tb + 2.0 + 0.9 * (i // 2), 0.3)
            pd = paint(col, 0.6 * kk, stroke=3)
            pd.setPathEffect(skia.DashPathEffect.Make([10, 10], 0))
            c.drawLine(xs[i], 230, xs[i], 760, pd)
            c.save(); c.translate(xs[i], 810); c.rotate(-30)
            text_mid(c, nome, 0, 0, 30, "black", col, kk, align="right")
            c.restore()
    board(c, a)
    eq(c, [(L["regra"], CYA)], 320, a * ep(t, tb, 0.3), 40, box=CYA)
    label(c, L["inteiros"] + " · " + L["decimos"] + " · " + L["centesimos"], RX, 460, a * ep(t, tb + 2.0, 0.3), 36, WHITE, "bold")
    label(c, L["maior"], RX, 600, a * ep(t, tc, 0.3), 44, AMB, "black")
    eq(c, [(n_("10,00 − 9,58"), AMB)], 730, a * ep(t, tc + 2.0, 0.3), 58)


def b_conta(c, t, C, B):
    ta, tb, tc, td, te = (C[f"05.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conta"], a)
    dur = te - td
    t2, t4, t0 = td + 0.15 * dur, td + 0.45 * dur, td + 0.75 * dur   # 10 − 8 · 9 − 5 · 9 − 9
    emp = t >= tc + 0.3
    vis = [i for i, tt in ((4, t2), (3, t4), (2, t0), (1, t0)) if t >= tt]
    if t < tc:
        hl, hc = ((4, 3) if t >= tb else ()), RED
    elif t < td:
        hl, hc = (0, 1, 3, 4), CYA
    else:
        hl, hc = ((4,) if t < t4 else (3,) if t < t0 else (1,) if t < te else ()), AMB
    conta(c, a, t, LX + 30, 340, "10,00", " 9,58", res=" 0,42", res_vis=vis,
          novos={1: "9", 3: "9", 4: "10"} if emp else None, riscos=(0, 1, 3, 4) if emp else (), hl=hl, hl_col=hc)
    board(c, a)
    k1 = a * (1 - ep(t, td, 0.3))
    eq(c, [(n_(L["naoda2"]), RED)], 290, k1 * ep(t, tb + 0.4, 0.3), 40)
    label(c, L["vem"], RX, 400, k1 * ep(t, tb + 3.0, 0.3), 40, CYA, "black")
    eq(c, [(n_(L["vira"]), CYA)], 540, k1 * ep(t, tc + 0.6, 0.3), 54, box=CYA)
    k2 = a * ep(t, td, 0.3)
    for j, (s, r, tt) in enumerate((("10 − 8 = ", "2", t2), ("9 − 5 = ", "4", t4), ("9 − 9 = ", "0", t0))):
        eq(c, [(s, WHITE), (r, MNT)], 300 + j * 110, k2 * ep(t, tt, 0.3), 54)
    eq(c, [("= ", WHITE), (n_("0,42 s"), MNT)], 690, a * ep(t, te, 0.3), 68, box=MNT)


def b_conferir(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conf"], a)
    dur = 2.4
    vis = [i for i, tt in ((4, 0.0), (3, 0.5), (2, 1.0), (1, 1.0), (0, 1.5)) if t >= tc + tt]
    conta(c, a * ep(t, tb, 0.3), t, LX + 30, 340, " 9,58", " 0,42", sinal="+", res="10,00", res_vis=vis,
          novos={3: "1", 1: "1", 0: ""} if t >= tc else None)
    if t >= tc + 2.0:
        check(c, LX + 30 + 300, 640, 34, a * ep(t, tc + 2.0, 0.3))
    board(c, a)
    label(c, L["soma"], RX, 300, a * ep(t, tb, 0.3), 42, WHITE, "black")
    eq(c, [(n_("9,58 + 0,42 = "), WHITE), (n_("10,00"), MNT)], 460, a * ep(t, tc + 0.6, 0.3), 56, box=MNT)
    opcoes(c, a, t, td, "B", y=700)


def b_pegadinhas(c, t, C, B):
    tb, tc, td = (C[f"07.{k}"] for k in "bcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    if t < tc:
        res, cr, nv, hl = " 0,52", {3: RED}, {1: "9", 3: "10", 4: "10"}, (3,)
    else:
        res, cr, nv, hl = " 1,42", {1: RED}, {1: "10", 3: "9", 4: "10"}, (1,)
    k0 = a * ep(t, tb, 0.3)
    conta(c, k0, t, LX + 30, 340, "10,00", " 9,58", res=res, res_col=WHITE, cores_res=cr, novos=nv, riscos=(0, 1, 3, 4),
          hl=hl, hl_col=RED)
    board(c, a)
    for j, (key, val, soma, tt) in enumerate((("peg_c", "0,52", "10,10", tb), ("peg_e", "1,42", "11,00", tc))):
        k = a * ep(t, tt, 0.3)
        y = 290 + j * 260
        label(c, n_(L[key]), RX, y, k, 40, RED, "black")
        eq(c, [(n_(f"9,58 + {val} = "), WHITE), (n_(soma), RED)], y + 100, a * ep(t, td + 1.0 + 4.0 * j, 0.3), 48)
        if t >= td + 2.0 + 4.0 * j:
            cross(c, BX1 - 70, y + 100, 26, a * ep(t, td + 2.0 + 4.0 * j, 0.2))
    opcoes(c, a * ep(t, td + 8.0, 0.3), t, td + 8.0, "B", ("C", "E"), y=820)


def pista(c, a, t, t0, x0=110, x1=900, y0=330):
    """duas raias: o Bolt (menta, 9,58 s) e um corredor de 10,00 s (âmbar), na mesma velocidade o tempo todo"""
    if a <= 0:
        return 0
    for j in range(3):
        c.drawLine(x0, y0 + j * 150, x1, y0 + j * 150, paint(WHITE, 0.35 * a, stroke=3))
    pd = paint(WHITE, a, stroke=8)
    c.drawLine(x1, y0 - 20, x1, y0 + 320, pd)
    text_mid(c, "100 m", x1, y0 - 50, 32, "black", WHITE, a)
    u = clamp((t - t0) / 3.0)       # a corrida dura 3 s na tela: o Bolt chega no fim
    xb = x0 + (x1 - x0) * ease_out(u) if u < 1 else x1
    xo = x0 + (x1 - x0) * 0.958 * (ease_out(u) if u < 1 else 1)
    for y, x, col, nome in ((y0 + 75, xb, MNT, "Bolt · " + n_("9,58 s")), (y0 + 225, xo, AMB, n_("10,00 s"))):
        c.drawCircle(x, y, 34, blur_paint(col, 0.6 * a, 14))
        c.drawCircle(x, y, 26, paint(col, a))
        text_mid(c, nome, x0 + 10, y - 50, 28, "black", col, a, align="left")
    return xo


def b_generaliza(c, t, C, B):
    ta, tb, tc, td = (C[f"08.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    kp = a * (1 - ep(t, td, 0.4))
    xo = pista(c, kp, t, tb + 2.6)
    kc = kp * ep(t, tc, 0.3)
    if kc > 0:   # a distância que falta: 4,2 m
        y = 650
        c.drawLine(xo, y, 900, y, paint(CYA, kc, stroke=6, cap_round=True))
        for x in (xo, 900):
            c.drawLine(x, y - 20, x, y + 20, paint(CYA, kc, stroke=6, cap_round=True))
        text_mid(c, n_("4,2 m"), (xo + 900) / 2 - 40, y + 60, 50, "black", CYA, kc)
        text_mid(c, L["atras"], (xo + 900) / 2 - 40, y + 112, 30, "bold", INK2, kc)
    kd = a * ep(t, td, 0.4)
    if kd > 0:
        conta(c, kd, t, LX + 30, 360, " 9,87", " 9,58", res=" 0,??", res_col=AMB)
    board(c, a)
    k1 = a * (1 - ep(t, td, 0.3))
    label(c, L["vel"], RX, 280, k1 * ep(t, tb, 0.3), 38, WHITE, "black")
    label(c, L["const"], RX, 340, k1 * ep(t, tb + 2.6, 0.3), 30, INK2, "bold")
    eq(c, [(n_("10 × 9,58 = "), WHITE), (n_("95,8 m"), AMB)], 470, k1 * ep(t, tb + 4.4, 0.3), 54)
    eq(c, [(n_("100 − 95,8 = "), WHITE), (n_("4,2 m"), CYA)], 620, k1 * ep(t, tc, 0.3), 56, box=CYA)
    label(c, L["desafio"], RX, 330, kd * ep(t, td + 0.8, 0.3), 46, AMB, "black")
    label(c, L["lento"], RX, 470, kd * ep(t, td + 3.0, 0.3), 46, WHITE, "black")
    label(c, L["comenta"], RX, 640, kd * ep(t, td + 5.0, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"09.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 280 + i * 160
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 260
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 48, "black", WHITE, ki, align="left")
        check(c, 1700, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: 0,58 com as casas · uma conta armada · um corredor com m/s"""
    if i == 0:
        text_mid(c, n_("9,58"), cx, cy, 110, "black", CYA, a)
    elif i == 1:
        text_mid(c, n_("10,00"), cx + 20, cy - 50, 56, "black", AMB, a)
        text_mid(c, n_("− 9,58"), cx + 20, cy + 14, 56, "black", AMB, a)
        c.drawLine(cx - 100, cy + 52, cx + 110, cy + 52, paint(WHITE, a, stroke=5))
    else:
        c.drawLine(cx - 120, cy + 40, cx + 120, cy + 40, paint(INK2, a, stroke=4))
        c.drawCircle(cx + 40, cy + 10, 26, paint(MNT, a))
        for j in range(3):
            c.drawLine(cx - 110 + j * 30, cy - 10 + j * 14, cx - 40 + j * 30, cy - 10 + j * 14, paint(MNT, a * 0.6, stroke=5, cap_round=True))
        text_mid(c, "m/s", cx, cy - 60, 50, "black", WHITE, a)


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
            bolinha(c, 960 - 280 + j * 140, 790, v, kl, MNT if v == "B" else INK2, glow=1.0 if v == "B" else 0, k=0.9)


BLOCKS = dict(gancho=b_gancho, decimais=b_decimais, emprestimo=b_emprestimo, armar=b_armar, conta=b_conta,
              conferir=b_conferir, pegadinhas=b_pegadinhas, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
