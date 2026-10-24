"""Visual — Frações, Decimais e Dízimas, Episódio 8: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (pizza, expr com frações empilhadas, alternativas, pause_timer, selo...).
Índice visual da revisão: os 7 ícones dos episódios (icone()).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum018", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr, expr, expr_w, pizza = K.fr, K.expr, K.expr_w, K.pizza
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep8_revisao.mp4"
CARD_R = K.CARD_R
TEAL = "#1FA39A"
OURO = "#E8B53A"


# ======================================================================
# os 7 ícones da série (índice da revisão)
# ======================================================================

def moeda(c, cx, cy, r, a, s="R$"):
    c.drawCircle(cx, cy, r, paint("#C98F1E", a))
    c.drawCircle(cx, cy, r * 0.84, paint(OURO, a))
    text_mid(c, s, cx, cy, r * 0.62, "black", "#8A5A12", a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    if a <= 0:
        return
    if k == 0:      # ep1 pizza
        pizza(c, cx, cy, 62 * s, 4, 3, a, pull=0.4)
    elif k == 1:    # ep2 pizzas inteiras + pedaço
        pizza(c, cx - 66 * s, cy, 32 * s, 4, 4, a)
        pizza(c, cx, cy, 32 * s, 4, 4, a)
        pizza(c, cx + 62 * s, cy, 32 * s, 4, 1, a, gone={1, 2, 3}, sombra=False)
    elif k == 2:    # ep3 sinais
        for j, (g, col) in enumerate((("+", BLUE), ("−", RED), ("×", PURPLE), ("÷", GREEN))):
            x = cx + (-34 if j % 2 == 0 else 34) * s
            y = cy + (-34 if j < 2 else 34) * s
            rrect(c, x - 30 * s, y - 30 * s, 60 * s, 60 * s, 14 * s, col, a)
            fmid(c, g, x, y, 44 * s, "black", "#FFFFFF", a)
    elif k == 3:    # ep4 pizza que encolhe
        pizza(c, cx, cy, 62 * s, 3, {1}, a, sel_col=TEAL, gone={0})
    elif k == 4:    # ep5 moedas
        for j in range(3):
            moeda(c, cx - 40 * s + j * 40 * s, cy + (8 - j * 8) * s, 34 * s, a)
    elif k == 5:    # ep6 fita infinita
        w, h = 170 * s, 58 * s
        rrect(c, cx - w / 2, cy - h / 2, w, h, 12 * s, mix("#FFFFFF", PURPLE, 0.14), a)
        for j in range(5):
            x = cx - w / 2 + 22 * s + j * 30 * s
            text_mid(c, "7", x, cy, 34 * s, "black", PURPLE, a * (1 - 0.17 * j))
        text_mid(c, "…", cx + w / 2 - 14 * s, cy, 30 * s, "black", PURPLE, a * 0.5)
        text_mid(c, "∞", cx, cy + 58 * s, 40 * s, "black", PURPLE, a)
    elif k == 6:    # ep7 três cartas
        for j, s_ in enumerate(("3/4", "0,75", "75%")):
            c.save(); c.translate(cx + (j - 1) * 52 * s, cy); c.rotate((j - 1) * 9)
            rrect(c, -30 * s, -44 * s, 60 * s, 88 * s, 10 * s, "#FFFFFF", a, shadow=True)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-30 * s, -44 * s, 60 * s, 88 * s), 10 * s, 10 * s),
                        paint([BLUE, GREEN, AMBER][j], a, stroke=3))
            if "/" in s_:
                fr(c, "3", "4", 0, -4 * s, 26 * s, BLUE, a)
            else:
                fmid(c, s_, 0, 0, 18 * s, "black", [BLUE, GREEN, AMBER][j], a)
            c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 190, 1000, 120, AMBER, aa, 0.10)
        text_mid(c, "o assunto MAIS SUBESTIMADO do ENEM", W / 2, 250, 44, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "questões com o nome dele: quase nenhuma", W / 2, 380, 34, "bold", INK2, ab)
    for k in range(7):
        a = ep(t, C["01.c"] + 0.2 * k, 0.4)
        icone(c, k, 300 + k * 220, 530, 0.8, a)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 PEGADINHAS", 720, 730, AMBER, ad, 40)
    chip(c, "5 QUESTÕES", 1200, 730, GREEN, ep(t, C["01.d"] + 0.6, 0.4), 40)


def b_onde(c, t, C, B):
    head_seq(c, t, C, [("02", "ONDE A FRAÇÃO SE ESCONDE", "DENTRO DE OUTROS ASSUNTOS", BLUE),
                       ("03", "QUANDO A QUESTÃO É DE FRAÇÃO", "O PROBLEMA EM DUAS ETAPAS", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["02", "03"])
    if sid == "02":
        temas = [("02.a", "probabilidade", "sempre uma fração"), ("02.b", "porcentagem", "converter é o atalho"),
                 ("02.c", "estatística", "média e setores"), ("02.d", "razão e proporção", "escala e velocidade"),
                 ("02.e", "Física e Química", "quase toda fórmula")]
        for k, (cue, s, sub) in enumerate(temas):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            x = 300 + k * 330
            rrect(c, x - 150, 230 + d, 300, 460, 22, "#F7F7F5", a)
            y = 400 + d
            if k == 0:
                fr(c, "1", "6", x, y, 80, PURPLE, a)
            elif k == 1:
                expr(c, "3/4 = 75%", x, y + 30, 46, a, cores={2: GREEN})
            elif k == 2:
                pizza(c, x, y, 80, 5, {0, 1}, a, sel_col=BLUE, sombra=False)
            elif k == 3:
                fr(c, "km", "h", x, y, 70, PURPLE, a)
            else:
                expr(c, "v = d/t", x, y + 30, 56, a, cores={2: PURPLE})
            text(c, s, x, 560 + d, 30, "black", INK, a)
            text(c, sub, x, 610 + d, 24, "bold", GRAY, a)
        pill(c, "a fração é o PASSO do meio", W / 2, 770, BLUE, size=30, a=ep(t, C["02.e"] + 1.4, 0.5), anchor="center")
        return
    # 03 duas etapas (a pizza que encolhe, em barra)
    x0, wbar, y = 300, 1320, 330
    a0 = ep(t, C["03"], 0.5)
    rrect(c, x0, y, wbar, 90, 14, "#EFE7D6", a0)
    text(c, "o TOTAL", x0 + wbar / 2, y - 26, 28, "black", INK2, a0)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, x0, y, wbar / 3 * aa, 90, 14, "#E8743B", aa)
        text_mid(c, "ETAPA 1: gasta uma fração", x0 + wbar / 6, y + 45, 26, "black", "#FFFFFF", aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        x1 = x0 + wbar / 3
        line(c, x1, y + 100, x1, y + 170, INK2, ab, 3, dash=[8, 8])
        line(c, x0 + wbar, y + 100, x0 + wbar, y + 170, INK2, ab, 3, dash=[8, 8])
        rrect(c, x1, y + 170, wbar * 2 / 3, 90, 14, "#EFE7D6", ab)
        rrect(c, x1, y + 170, wbar * 2 / 3 / 4 * ab, 90, 14, TEAL, ab)
        text_mid(c, "ETAPA 2: fração do que SOBROU", x1 + wbar * 0.4, y + 215, 28, "black", INK, ab)
    selo(c, W / 2, 700, ep(t, C["03.c"], 0.4), "DERRUBA MUITA GENTE", AMBER, -4, 34)


INDICE = [("EP. 1", "fatias de pizza · “de” é vezes"), ("EP. 2", "pizzas inteiras + um pedaço"),
          ("EP. 3", "o mesmo tamanho de fatia"), ("EP. 4", "a pizza que encolhe"),
          ("EP. 5", "decimal é dinheiro"), ("EP. 6", "o 10 só aceita 2 e 5"), ("EP. 7", "três idiomas")]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    cues = ["04.a", "04.b", "04.c", "04.d", "05.a", "05.b", "05.c"]
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[cues[k]], 0.5)
        if a <= 0:
            continue
        # ilumina o episódio que está sendo lembrado
        nxt = C[cues[k + 1]] if k + 1 < len(cues) else C["05.end"]
        on_ = 1.0 if C[cues[k]] - 0.05 <= t < nxt else 0.0
        if k < 4:
            x, y = 380 + k * 385, 200
        else:
            x, y = 380 + (k - 4) * 385 + 192, 520
        rrect(c, x - 180, y, 360, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 180, y, 360, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=22, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 140, 0.85, a)
        para(c, s, x, y + 245, 26, "black", INK if on_ else INK2, a, 330, align="center")


def b_rendem(c, t, C, B):
    frame(c, t, B["start"], "SE TIVER TEMPO PARA DUAS", "AS QUE MAIS RENDEM", GREEN)
    aa, ab = ep(t, C["06.a"], 0.5), ep(t, C["06.b"], 0.5)
    for k, (a, tit, sub) in enumerate(((aa, "1 · A TABELA", "fração ↔ decimal ↔ %, de cor"),
                                       (ab, "2 · O “DO RESTANTE”", "fração do que SOBROU"))):
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 470, 24, "#F7F7F5", a)
        text(c, tit, x, 260, 38, "black", GREEN, a)
        text(c, sub, x, 310, 28, "bold", INK2, a)
        if k == 0:
            for j, (f_, d_, p_) in enumerate((("1/2", "0,5", "50%"), ("1/4", "0,25", "25%"), ("3/4", "0,75", "75%"))):
                y = 410 + j * 80
                expr(c, f_, x - 190, y, 46, a, cores={0: BLUE})
                fmid(c, d_, x, y, 40, "black", GREEN, a)
                fmid(c, p_, x + 190, y, 40, "black", AMBER, a)
        else:
            icone(c, 3, x, 490, 1.6, a)
    pill(c, "juntas valem mais que toda a teoria de dízimas", W / 2, 760, GREEN, size=30, a=ep(t, C["06.c"], 0.5),
         anchor="center")


JOGO = [("3/4", "PORCENTAGEM", "75%"), ("0,2", "FRAÇÃO", "1/5"), ("1/8", "PORCENTAGEM", "12,5%"),
        ("2/3", "DECIMAL", "0,666…"), ("5%", "FRAÇÃO", "1/20"), ("0,375", "FRAÇÃO", "3/8")]


def b_jogo(c, t, C, B):
    head_seq(c, t, C, [("07", "JOGO RÁPIDO", "6 CONVERSÕES", GREEN), ("08", "CONFERINDO", "6 CONVERSÕES", GREEN)])
    card(c, *CARD_R)
    for k, (q, para_, r) in enumerate(JOGO):
        a, d = rise(t, C["07." + "abcdef"[k]])
        if a <= 0:
            continue
        x = 450 + (k % 3) * 510
        y = 190 + (k // 3) * 270 + d
        rrect(c, x - 230, y, 460, 240, 20, "#F7F7F5", a)
        pill(c, "→ " + para_, x, y + 34, BLUE, size=20, a=a, anchor="center", bounds=(0, 1920))
        ar = ep(t, C["08." + "abcdef"[k]], 0.4) if t >= C["08"] else 0
        expr(c, q, x - 80 * ar, y + 140, 62, a)
        if ar > 0:
            expr(c, "= " + r, x + 30 + expr_w(q, 62) / 2 - 80 * ar + expr_w("= " + r, 56) / 2, y + 140, 56, ar,
                 cores={1: GREEN})
    pause_timer(c, t, C["07.end"] - 1.9, W / 2, 760)
    if t >= C["08"]:
        regra(c, "ATALHO: porcentagem → fração: ponha sobre 100 e simplifique", W / 2, 790, ep(t, C["08.g"], 0.5), 30, GREEN)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["09"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["09.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["09.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "algumas são pegadinhas · outras são verdade", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["09.b"], 0.5), anchor="center")


# (frase, conta mostrada, verdadeira?, por que engana, regra certa, conta corrigida, ícone)
VF = [
    ("1/3 e depois 1/4 DO RESTANTE é o mesmo que", "1/3 + 1/4", False, "as duas frações parecem do mesmo todo",
     "a pizza ENCOLHEU: o 1/4 é do que sobrou", "1/3 + 1/6", 3),
    ("um meio mais um terço dá dois quintos", "1/2 + 1/3 = 2/5", False, "na multiplicação é em cima com em cima",
     "na soma, recorte no mesmo tamanho de fatia", "3/6 + 2/6 = 5/6", 2),
    ("dois e meio vezes três dá seis e meio", "2|1/2 × 3 = 6|1/2", False, "parece natural multiplicar só o inteiro",
     "misto vira impróprio ANTES da conta", "5/2 × 3 = 15/2 = 7|1/2", 1),
    ("três sétimos é maior, porque 7 é maior que 5", "3/7 > 3/5", False, "número maior parece fração maior",
     "mesmo numerador: pizza para menos gente, fatia maior", "3/5 > 3/7", 1),
    ("zero vírgula três vezes zero vírgula zero quatro", "0,3 × 0,04 = 0,12", False, "3 × 4 = 12 mesmo",
     "some as casas: 1 + 2 = 3 casas", "0,3 × 0,04 = 0,012", 4),
    ("dividir 4,8 por 0,12 dá MAIS que 4,8", "4,8 ÷ 0,12 > 4,8", True, "a gente aprendeu que dividir diminui",
     "quantas moedas de 12 centavos cabem em R$ 4,80?", "4,8 ÷ 0,12 = 40", 4),
    ("toda dízima periódica é um número RACIONAL", "0,777…", True, "ela nunca termina",
     "repete com padrão → tem fração mãe (geratriz)", "0,777… = 7/9", 5),
    ("6/12 NÃO dá decimal exato (o 12 tem o fator 3)", "6/12", False, "o critério foi usado antes de simplificar",
     "simplifique primeiro; o 10 só aceita 2 e 5", "6/12 = 1/2 = 0,5", 5),
    ("0,999… (repetindo para sempre) é EXATAMENTE 1", "0,999… = 1", True, "soa como “quase 1”",
     "10x − x = 9 → 9x = 9 → x = 1", "0,999… = 1", 5),
]
VF_IDS = [f"{10 + k}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    frase, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 380, 0.85, a0)
    text(c, frase, 1000, 320, 34, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    expr(c, conta, 1000, 420, 70, a0)
    if ar > 0 and not ver:
        w = expr_w(conta, 70)
        strike(c, 1000 - w / 2 - 10, 425, 1000 + w / 2 + 10, 425, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 400)
    selo(c, 1580, 400, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 700, 32, "black", GREEN, ag, 700)
        expr(c, fix, 1330, 715, 56, ag, cores={len(fix.split()) - 1: GREEN})


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["19.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["19.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["19.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 640, GREEN, ab, 44)
    text(c, "no estilo do ENEM", W / 2, 750, 30, "bold", INK2, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("20", "21"), titulo="O CAMINHÃO-PIPA", ok="B", icone=3,
               enun=[("a", "Um caminhão-pipa sai com 6.000 litros de água."), ("b", "Na 1ª parada, entrega 1/5 da carga."),
                     ("c", "Na 2ª, entrega 2/3 do que restou."), ("d", "Quantos litros ficam no caminhão?")],
               alts=[("A", "800 L", "tirou 2/3 do TOTAL", RED), ("B", "1.600 L", "", GREEN),
                     ("C", "2.000 L", "esqueceu a 1ª parada", RED), ("D", "3.200 L", "é a 2ª entrega", RED),
                     ("E", "4.800 L", "parou na 1ª etapa", AMBER)],
               passos=[("t", "1/5 × 6.000 = 1.200", {}), ("a", "6.000 − 1.200 = 4.800", {4: BLUE}),
                       ("b", "2/3 × 4.800 = 3.200", {}), ("c", "4.800 − 3.200 = 1.600", {4: GREEN})],
               atalho="6.000 × 4/5 × 1/3 = 1.600"),
    "q2": dict(ids=("22", "23"), titulo="AS HORAS DE ESTUDO", ok="C", icone=2,
               enun=[("a", "Lucas dedicou 1/3 das horas de estudo da semana a Matemática"), ("b", "e 2/5 a Linguagens."),
                     ("c", "Que fração das horas foi para essas duas áreas juntas?")],
               alts=[("A", "= 3/8", "somou em cima e embaixo", RED), ("B", "= 2/15", "multiplicou", RED),
                     ("C", "= 11/15", "", GREEN), ("D", "= 4/15", "é o que sobrou", AMBER),
                     ("E", "= 3/15", "não ajustou os numeradores", RED)],
               passos=[("a", "MMC(3, 5) = 15", {}), ("b", "1/3 = 5/15", {2: BLUE}), ("b", "2/5 = 6/15", {2: BLUE}),
                       ("c", "5/15 + 6/15 = 11/15", {4: GREEN})],
               atalho=None),
    "q3": dict(ids=("24", "25"), titulo="A GINCANA", ok="E", icone=1,
               enun=[("a", "Numa gincana, três equipes completaram estas frações da trilha:"),
                     ("b", "Azul: 3/4 · Verde: 7/10 · Laranja: 9/11"),
                     ("c", "Qual é a ordem, da que andou mais para a que andou menos?")],
               alts=[("A", "Verde, Azul, Laranja", "ordem ao contrário", RED),
                     ("B", "Azul, Verde, Laranja", "mesmo numerador fora de lugar", AMBER),
                     ("C", "Laranja, Verde, Azul", "só os numeradores", RED),
                     ("D", "Azul, Laranja, Verde", "contou os pedaços que faltam", RED),
                     ("E", "Laranja, Azul, Verde", "", GREEN)],
               passos=[("a", "3/4 = 0,75", {2: BLUE}), ("b", "7/10 = 0,70", {2: GREEN}), ("c", "9/11 = 0,8181…", {2: OURO}),
                       ("d", "0,81… > 0,75 > 0,70", {})],
               atalho=None),
    "q4": dict(ids=("26", "27"), titulo="O CRÉDITO DE IMPRESSÃO", ok="D", icone=4,
               enun=[("a", "Uma estudante tem R$ 12,60 de crédito de impressão."), ("b", "Cada página custa R$ 0,35."),
                     ("c", "Quantas páginas ela consegue imprimir?")],
               alts=[("A", "3,6", "vírgula só no divisor", RED), ("B", "4,41", "multiplicou", RED),
                     ("C", "12,25", "subtraiu", RED), ("D", "36", "", GREEN), ("E", "360", "vírgula só no dividendo", RED)],
               passos=[("t", "12,60 ÷ 0,35", {}), ("a", "1.260 ÷ 35", {}), ("b", "= 36", {1: GREEN})],
               atalho=None),
    "q5": dict(ids=("28", "29"), titulo="A PESQUISA DA BICICLETA", ok="D", icone=6,
               enun=[("a", "Numa pesquisa em um bairro, 7 em cada 20 moradores vão ao trabalho de bicicleta."),
                     ("b", "Que porcentagem dos pesquisados usa bicicleta?")],
               alts=[("A", "0,35%", "parou no decimal", RED), ("B", "7%", "leu o 7 como %", RED),
                     ("C", "13%", "fez 20 − 7", RED), ("D", "35%", "", GREEN), ("E", "65%", "quem NÃO usa", AMBER)],
               passos=[("t", "7/20", {}), ("a", "7/20 = 35/100 = 35%", {4: GREEN})],
               atalho="20 × 5 = 100"),
}


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · ESTILO ENEM", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        # enunciado (some na resolução)
        sol = ep(t, C[s2], 0.5)
        y = 270
        for cue, s in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            last = cue == d["enun"][-1][0]
            h = para(c, s, 180, y, 30, "black" if last else "bold", BLUE if last else INK, a, 600, 40)
            y += h + 16
        icone(c, d["icone"], 470, 690, 0.8, a0 * (1 - sol) * ep(t, C[f"{s1}.{d['enun'][-1][0]}"], 0.4))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 680, 700)
        # alternativas
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        size = 34 if nome != "q3" else 30
        K.alternativas(c, t, C, d["alts"], 880, 250, 800, size, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=16)
        # resolução
        if sol > 0:
            yy = 280
            for cue, s, cores in d["passos"]:
                a = ep(t, C[f"{s2}.{cue}"], 0.4)
                expr(c, s, 470, yy, 42, a, cores=cores)
                yy += 84
            ag = ep(t, C[f"{s2}.g"], 0.4) if f"{s2}.g" in C else 0
            if d["atalho"] and ag > 0:
                boxed(c, 180, yy - 30, 580, 120, GREEN, ag, 0.08)
                text(c, "ATALHO", 470, yy + 4, 20, "black", GREEN, ag, tracking=2)
                expr(c, d["atalho"], 470, yy + 56, 40, ag, cores={len(d["atalho"].split()) - 1: GREEN})
            elif nome == "q4" and ag > 0:
                pill(c, "dividir por menos de 1 faz CRESCER", 470, yy + 20, GREEN, size=26, a=ag, anchor="center",
                     bounds=(0, 1920))
            result_box(c, f"Letra {d['ok']}", 470, 770, 40, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("30.b", "EP. 1", ["4 significados e “de” = vezes", "simplifico pelo MDC", "produto cruzado"]),
         ("30.c", "EP. 2", ["misto → impróprio e volto", "mesmo numerador", "ordeno em decimal"]),
         ("30.d", "EP. 3", ["as 4 operações e potências", "corte em cruz"]),
         ("31.a", "EP. 4", ["fração do restante"]),
         ("31.b", "EP. 5", ["× e ÷ com decimais"]),
         ("31.c", "EP. 6", ["prevejo o decimal exato", "acho a geratriz"]),
         ("31.d", "EP. 7", ["a tabela de cor"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["30.a"], 0.5) * (1 - ep(t, C["30.b"], 0.4))
    pill(c, "explicar para outra pessoa, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 3 else 1
        x = 200 if col_ == 0 else 1000
        y0 = 200 + sum(len(CHECK[j][2]) * 50 + 30 for j in range(0 if col_ == 0 else 3, k))
        pill(c, ep_, x, y0 + 20, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 20 + j * 50
            rrect(c, x + 110, yy - 16, 32, 32, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            text(c, it, x + 160, yy + 11, 30, "bold", INK, a, align="left")
    ae = ep(t, C["31.e"], 0.5)
    if ae > 0:
        boxed(c, 1000, 690, 640, 110, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1320, 745, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["32.a"], 0.5)
    ab = ep(t, C["32.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["32.a"] + 0.04 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 330 + k * 82, 260 + r_ * 92
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 330, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 430, 46, "black", GREEN, ab)
    ac = ep(t, C["32.c"], 0.5)
    if ac > 0:
        icone(c, 3, 520, 700, 0.75, ac)
        boxed(c, 650, 640, 1000, 120, AMBER, ac, 0.10)
        text_mid(c, "priorize as de duas etapas com “do restante”", 1150, 700, 34, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SEMANA 1 DE MATEMÁTICA", "FECHADA", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    for k in range(7):
        icone(c, k, 300 + k * 220, 300, 0.7, aa * ep(t, C["33.a"] + 0.12 * k, 0.3))
    check_icon(c, W / 2, 440, 36, ep(t, C["33.a"] + 1.4, 0.4), GREEN)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        text(c, "PRÓXIMO ASSUNTO", W / 2, 560, 28, "black", GRAY, ab, tracking=2)
        text(c, "Potenciação e radiciação", W / 2, 640, 60, "black", PURPLE, ab)
    ac = ep(t, C["33.c"], 0.5)
    if ac > 0:
        boxed(c, 560, 700, 800, 100, AMBER, ac, 0.10)
        fmid(c, "o expoente negativo: 2^{-1}", W / 2, 750, 40, "black", INK, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quantas das 5 questões você acertou?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, onde=b_onde, indice=b_indice, rendem=b_rendem, jogo=b_jogo, vf_intro=b_vf_intro, vf=b_vf,
              vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"), q3=faz_questao("q3"),
              q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
