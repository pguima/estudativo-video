"""Visual do vídeo Seguridade 003 — Princípios parte 2 (incisos IV–VII). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_003_principios_parte2.mp4"
CARD_R = (140, 150, 1640, 690)

PREST = "#0F766E"
CUST = "#E8A317"
GEST = "#4F46E5"
INC = [("I", "Universalidade", PREST), ("II", "Uniformidade e equivalência", PREST),
       ("III", "Seletividade e distributividade", PREST), ("IV", "Irredutibilidade", PREST),
       ("V", "Equidade no custeio", CUST), ("VI", "Diversidade da base", CUST),
       ("VII", "Caráter democrático e descentralizado", GEST)]


def inciso_tag(c, roman, x, y, col, a, size=40):
    w = text_w(roman, "black", size) + 40
    rrect(c, x, y - size * 0.75, w, size * 1.5, 14, col, a)
    text_mid(c, roman, x + w / 2, y, size, "black", "#FFFFFF", a)
    return w


def ce(c, t, C, cue_e, cue_r, cue_x, frase_lines, resp, ok, expl, head_l2):
    head(c, t, C[cue_e] - 1.2, "QUESTÃO DE PROVA", head_l2)
    card(c, 200, 180, 1520, 560)
    pill(c, "C / E", 240, 230, BLUE, size=26, bounds=(0, 1920))
    for k, ln in enumerate(frase_lines):
        text(c, ln, 280, 330 + k * 64, 40, "semibold", INK, ep(t, C[cue_e] + 0.7 * k, 0.4), align="left")
    ar = ep(t, C[cue_r], 0.4)
    result_box(c, resp, 1500, 800, 50, ar, GREEN if ok else RED)
    ax = ep(t, C[cue_x], 0.5)
    pill(c, expl, 960, 660, GREEN if ok else RED, size=30, a=ax, anchor="center")


def twin(c, a_left, a_right, left, right, y=200, h=520):
    for k, ((tit, col, lines), a) in enumerate(((left, a_left), (right, a_right))):
        if a <= 0:
            continue
        x = 200 + k * 780
        dy = (1 - a) * 18
        card(c, x, y + dy, 740, h, a)
        rrect(c, x, y + dy, 740, 14, 7, col, a)
        text(c, tit, x + 370, y + 110 + dy, 52, "black", col, a)
        for j, (s, size, peso, cc) in enumerate(lines):
            text(c, s, x + 370, y + 200 + dy + j * (size + 24), size, peso, cc or INK, a)


def money(c, x, y, s, a, col=None):
    col = GREEN if col is None else col
    rrect(c, x - 70 * s, y - 40 * s, 140 * s, 80 * s, 12 * s, col, a * 0.85)
    c.drawCircle(x, y, 22 * s, paint("#FFFFFF", a * 0.6))
    text_mid(c, "R$", x, y, 22 * s, "black", col, a)


def person(c, x, y, col, a, s=1.0):
    c.drawCircle(x, y - 70 * s, 24 * s, paint(col, a))
    rrect(c, x - 22 * s, y - 42 * s, 44 * s, 90 * s, 16 * s, col, a)


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 3", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    text(c, "OS 7 PRINCÍPIOS", W / 2, 320, 84, "black", INK, a0)
    text(c, "parte 2 · art. 194, parágrafo único", W / 2, 385, 38, "semibold", GRAY, a0)
    for k, (cue, (rom, nome, col)) in enumerate(zip(("01.b", "01.c", "01.d", "01.e"), INC[3:])):
        a, dy = rise(t, C[cue])
        x = 260 + k * 360
        card(c, x, 460 + dy, 330, 200, a)
        inciso_tag(c, rom, x + 165 - (text_w(rom, "black", 40) + 40) / 2, 520 + dy, col, a)
        nm = {"IV": "Irredutibilidade", "V": "Equidade", "VI": "Diversidade", "VII": "Gestão"}[rom]
        text(c, nm, x + 165, 620 + dy, 36, "black", INK, a)
    pill(c, "pegadinhas MUITO perigosas", W / 2, 780, RED, size=30, a=ep(t, C["01.f"], 0.5), anchor="center")


def b_lembrete(c, t, C, B):
    head(c, t, B["start"], "LEMBRETE", "PRESTAÇÃO · CUSTEIO · GESTÃO", AMBER)
    card(c, 300, 170, 1320, 680)
    groups = {"02.p": [3], "02.c": [4, 5], "02.g": [6]}
    for k, (rom, nome, col) in enumerate(INC):
        y = 250 + k * 86
        hl = 0.25
        for cue, ks in groups.items():
            if k in ks:
                hl = max(hl, ep(t, C[cue], 0.5))
        a = 0.35 if k < 3 else 1.0
        a = max(a * hl, 0.25)
        inciso_tag(c, rom, 360, y, col, a, 34)
        text(c, nome, 520, y + 14, 40, "bold", INK, a, align="left")
    for cue, lab, col, y in (("02.p", "PRESTAÇÃO", PREST, 250 + 3 * 86), ("02.c", "CUSTEIO", CUST, 250 + 4.5 * 86),
                             ("02.g", "GESTÃO", GEST, 250 + 6 * 86)):
        pill(c, lab, 1580, y, col, size=28, a=ep(t, C[cue], 0.5), anchor="right", bounds=(0, 1920))


def b_irred(c, t, C, B):
    head(c, t, B["start"], "INCISO IV", "IRREDUTIBILIDADE DO VALOR DOS BENEFÍCIOS")
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "depois de concedido, o valor NÃO PODE CAIR", W / 2, 300, 46, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "R$ 3.000", 700, 520, 80, "black", PREST, ab)
        arrow(c, 900, 495, 1080, 495, LIGHT, ab, 6, 22)
        text(c, "R$ 2.700", 1260, 520, 80, "black", RED, ab)
        strike(c, 1100, 495, 1420, 495, ep(t, C["03.b"] + 1.0, 0.4))
        mark(c, False, 1500, 560, ep(t, C["03.b"] + 1.0, 0.4), 30)
        text(c, "redução por ato da administração", W / 2, 650, 32, "semibold", GRAY, ab)


def b_nominal(c, t, C, B):
    head(c, t, B["start"], "O PONTO QUE DECIDE", "NOMINAL OU REAL?", RED)
    twin(c, ep(t, C["04.n"], 0.5), ep(t, C["04.r"], 0.5),
         ("VALOR NOMINAL", PREST, [("o NÚMERO não cai", 40, "black", INK), ("art. 194, IV", 34, "bold", PREST),
                                   ("TODA a seguridade", 32, "semibold", GRAY)]),
         ("VALOR REAL", CUST, [("o PODER DE COMPRA (reajuste)", 36, "black", INK), ("art. 201, §4º", 34, "bold", CUST),
                               ("só o RGPS", 32, "semibold", GRAY)]), y=180, h=440)
    ax = ep(t, C["05.x"], 0.5)
    if ax > 0:
        rrect(c, 300, 680, 1320, 100, 22, RED, 0.08 * ax)
        text_mid(c, "NÃO há direito adquirido a índice específico de reajuste", W / 2, 730, 32, "black", RED, ax)
    pill(c, "a LEI define os critérios", W / 2, 830, INK, size=26, a=ep(t, C["05.y"], 0.5), anchor="center")


def b_piso(c, t, C, B):
    head(c, t, B["start"], "A PEGADINHA DO PISO", "1 SALÁRIO MÍNIMO PARA QUEM?", RED)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    text(c, "nenhum benefício que", W / 2, 280, 40, "semibold", INK, aa)
    ab = ep(t, C["06.b"], 0.5)
    sw = text_w("SUBSTITUA", "black", 60)
    if ab > 0:
        rrect(c, W / 2 - sw / 2 - 20, 300, sw + 40, 80, 16, AMBER, 0.2 * ab)
    text(c, "SUBSTITUA", W / 2, 362, 60, "black", mix(INK, AMBER, ab), aa)
    text(c, "o salário pode ser menor que 1 salário mínimo", W / 2, 430, 40, "semibold", INK, aa)
    ac = ep(t, C["06.c"], 0.5)
    for k, s in enumerate(("salário-família", "auxílio-acidente")):
        pill(c, s, 650 + k * 620, 560, PREST, size=36, a=ac, anchor="center")
        text(c, "pode ser < 1 SM", 650 + k * 620, 640, 32, "bold", GREEN, ac)
    pill(c, "NÃO substituem a renda: são COMPLEMENTARES", W / 2, 760, INK, size=28, a=ep(t, C["06.d"], 0.5), anchor="center")


def b_q_piso(c, t, C, B):
    ce(c, t, C, "07.e", "07.r", "07.x",
       ["Por força da irredutibilidade, o auxílio-acidente", "não pode ser fixado em valor INFERIOR", "ao salário mínimo."],
       "ERRADO", False, "piso só para benefício SUBSTITUTIVO · auxílio-acidente é indenizatório", "IRREDUTIBILIDADE")


def b_equid(c, t, C, B):
    head(c, t, B["start"], "INCISO V", "EQUIDADE NA FORMA DE PARTICIPAÇÃO NO CUSTEIO", CUST)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    pill(c, "CAPACIDADE econômica", 620, 270, CUST, size=32, a=aa, anchor="center")
    pill(c, "RISCO que gera", 1300, 270, CUST, size=32, a=ep(t, C["08.b"], 0.5), anchor="center")
    ai = ep(t, C["08.i"], 0.5)
    if ai > 0:
        text(c, "IGUALDADE", 560, 400, 46, "black", GRAY, ai)
        for k in range(4):
            person(c, 380 + k * 120, 600, GRAY, ai, 1.0)
            money(c, 380 + k * 120, 680, 0.55, ai, GRAY)
        text(c, "todos pagam o mesmo", 560, 760, 30, "semibold", GRAY, ai)
    ae = ep(t, C["08.e"], 0.5)
    if ae > 0:
        text(c, "EQUIDADE", 1360, 400, 46, "black", CUST, ae)
        for k, s in enumerate((0.45, 0.65, 0.85, 1.05)):
            person(c, 1180 + k * 120, 600, CUST, ae, 1.0)
            money(c, 1180 + k * 120, 680, s * 0.75, ae, CUST)
        text(c, "cada um conforme pode", 1360, 760, 30, "semibold", CUST, ae)
    pill(c, "equidade ≠ igualdade", W / 2, 400, RED, size=28, a=ep(t, C["08.c"], 0.5), anchor="center")


def b_equid_ex(c, t, C, B):
    head(c, t, B["start"], "NA PRÁTICA", "DOIS CRITÉRIOS DA EQUIDADE", CUST)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    text(c, "CAPACIDADE", 560, 270, 40, "black", CUST, aa)
    text(c, "quem ganha mais → alíquota maior", 560, 330, 32, "bold", INK, aa)
    ab = ep(t, C["09.b"], 0.5)
    text(c, "RISCO", 1360, 270, 40, "black", CUST, ab)
    for k, (nome, pct, h) in enumerate((("mineradora", "alíquota maior", 220), ("escritório", "alíquota menor", 80))):
        x = 1220 + k * 280
        rrect(c, x - 60, 560 - h, 120, h, 10, RED if k == 0 else GREEN, ab)
        text(c, nome, x, 600, 28, "bold", INK, ab)
        text(c, pct, x, 640, 24, "semibold", GRAY, ab)
    ac = ep(t, C["09.c"], 0.5)
    if ac > 0:
        rrect(c, 220, 400, 700, 340, 20, CUST, 0.08 * ac)
        text(c, "alíquotas diferenciadas por:", 570, 450, 30, "bold", INK, ac)
        for k, s in enumerate(("atividade econômica", "uso intensivo de mão de obra", "PORTE da empresa", "condição do mercado de trabalho")):
            a = ep(t, C["09.c"] + 0.6 * k, 0.4)
            check_icon(c, 270, 510 + k * 56, 16, a, GREEN)
            text(c, s, 300, 522 + k * 56, 30, "bold", INK, a, align="left")


def b_q_equid(c, t, C, B):
    ce(c, t, C, "10.e", "10.r", "10.x",
       ["Alíquotas diferenciadas para a empresa", "em razão do seu PORTE afrontam", "a equidade no custeio."],
       "ERRADO", False, "elas CONCRETIZAM a equidade (autorizadas pela CF)", "EQUIDADE")


def b_divers(c, t, C, B):
    head(c, t, B["start"], "INCISO VI", "DIVERSIDADE DA BASE DE FINANCIAMENTO", CUST)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    text(c, "não depender de UMA ÚNICA fonte", W / 2, 290, 46, "black", INK, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        # um pilar só segurando o teto
        rrect(c, 700, 380, 520, 30, 8, PREST, ab)
        tilt = ep(t, C["11.c"], 0.8) * 12
        c.save(); c.translate(960, 640); c.rotate(tilt); c.translate(-960, -640)
        rrect(c, 930, 410, 60, 230, 8, CUST, ab)
        c.restore()
        text(c, "só a folha de salários", 960, 700, 30, "bold", INK, ab)
        pill(c, "crise de desemprego = sistema quebra", 960, 780, RED, size=28, a=ep(t, C["11.c"], 0.5), anchor="center")


def b_fontes(c, t, C, B):
    head(c, t, B["start"], "MUITAS FONTES", "AO MESMO TEMPO", CUST)
    card(c, *CARD_R)
    rrect(c, 360, 260, 1200, 40, 10, PREST)
    text(c, "SEGURIDADE SOCIAL", W / 2, 292, 30, "black", "#FFFFFF")
    fontes = [("12.f1", "folha"), ("12.f2", "faturamento\ne lucro"), ("12.f3", "trabalhadores"), ("12.f4", "loterias"),
              ("12.f5", "importação")]
    for k, (cue, s) in enumerate(fontes):
        a, dy = rise(t, C[cue])
        x = 440 + k * 260
        rrect(c, x - 40, 300 + dy, 80, 260, 8, CUST, a)
        for j, ln in enumerate(s.split("\n")):
            text(c, ln, x, 610 + dy + j * 36, 30, "black", INK, a)
    ao = ep(t, C["12.o"], 0.5)
    pill(c, "+ orçamentos da União, Estados, DF e Municípios", W / 2, 760, PREST, size=28, a=ao, anchor="center")


def b_ec103(c, t, C, B):
    head(c, t, B["start"], "EC 103/2019", "DUAS EXIGÊNCIAS NOVAS NO INCISO VI", RED)
    card(c, 200, 170, 1520, 680)
    for k, (cue, tit, sub) in enumerate((("13.a", "RUBRICAS CONTÁBEIS ESPECÍFICAS", "receitas e despesas de saúde, previdência e assistência separadas"),
                                         ("13.b", "PRESERVADO o caráter contributivo", "da previdência social"))):
        a, dy = rise(t, C[cue])
        y = 300 + k * 200 + dy
        badge_num(c, k + 1, 290, y - 12, a, 34, bg=CUST)
        text(c, tit, 360, y, 44, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 30, "semibold", GRAY, a, align="left")
    pill(c, "trecho NOVO: as questões recentes cobram exatamente ele", W / 2, 760, RED, size=28, a=ep(t, C["13.c"], 0.5),
         anchor="center")


def b_exclusiv(c, t, C, B):
    head(c, t, B["start"], "A FRASE QUE É", "SEMPRE ERRADA", RED)
    card(c, 200, 180, 1520, 640)
    ae = ep(t, C["14.e"], 0.5)
    text(c, "“a seguridade social é financiada", W / 2, 320, 44, "semibold", INK, ae)
    x0 = W / 2 - text_w("EXCLUSIVAMENTE pelas contribuições dos TRABALHADORES”", "black", 44) / 2
    text(c, "EXCLUSIVAMENTE", x0, 390, 44, "black", RED, ae, align="left")
    x1 = x0 + text_w("EXCLUSIVAMENTE ", "black", 44)
    text(c, "pelas contribuições dos", x1, 390, 44, "semibold", INK, ae, align="left")
    x2 = x1 + text_w("pelas contribuições dos ", "semibold", 44)
    text(c, "TRABALHADORES”", x2, 390, 44, "black", RED, ae, align="left")
    a1 = ep(t, C["14.x1"], 0.5)
    pill(c, "EXCLUSIVAMENTE → nega a diversidade", W / 2, 520, RED, size=30, a=a1, anchor="center")
    a2 = ep(t, C["14.x2"], 0.5)
    pill(c, "DOS TRABALHADORES → esquece empresas, loterias, importação e orçamentos", W / 2, 610, RED, size=26, a=a2,
         anchor="center")
    result_box(c, "ERRADO", W / 2, 730, 50, ep(t, C["14.x1"], 0.4), RED)


def b_gestao(c, t, C, B):
    head(c, t, B["start"], "INCISO VII", "CARÁTER DEMOCRÁTICO E DESCENTRALIZADO", GEST)
    twin(c, ep(t, C["15.d"], 0.5), ep(t, C["15.s"], 0.5),
         ("DEMOCRÁTICO", GEST, [("a sociedade PARTICIPA", 40, "black", INK), ("das decisões", 32, "semibold", GRAY)]),
         ("DESCENTRALIZADO", GEST, [("DISTRIBUÍDO entre", 40, "black", INK), ("entes e órgãos", 32, "semibold", GRAY)]),
         y=200, h=420)


def b_quadri(c, t, C, B):
    head(c, t, B["start"], "GESTÃO QUADRIPARTITE", "OS 4 ATORES", GEST)
    card(c, *CARD_R)
    atores = [("16.a1", "T", "TRABALHADORES"), ("16.a2", "E", "EMPREGADORES"), ("16.a3", "A", "APOSENTADOS"), ("16.a4", "G", "GOVERNO")]
    for k, (cue, l, nome) in enumerate(atores):
        a, dy = rise(t, C[cue])
        x = 360 + k * 400
        c.drawCircle(x, 430 + dy, 110, paint(GEST, 0.12 * a))
        text(c, l, x, 470 + dy, 130, "black", GEST, a)
        text(c, nome, x, 620 + dy, 34, "black", INK, a)
    am = ep(t, C["16.m"], 0.5)
    pill(c, "T · E · A · G — nos órgãos COLEGIADOS", W / 2, 760, GEST, size=32, a=am, anchor="center")


def b_falso(c, t, C, B):
    head(c, t, B["start"], "O QUINTO ATOR", "É SEMPRE FALSO", RED)
    card(c, *CARD_R)
    for k, cue in enumerate(("17.f1", "17.f2", "17.f3", "17.f4")):
        s = ("sindicatos", "Ministério Público", "usuários", "servidores do INSS")[k]
        a, dy = rise(t, C[cue])
        x = 380 + k * 390
        card(c, x - 170, 260 + dy, 340, 200, a)
        text(c, s, x, 370 + dy, 34, "black", INK, a)
        ax = ep(t, C["17.x"], 0.4)
        check_icon(c, x + 140, 280 + dy, 24, ax * a, RED, "x")
    ay = ep(t, C["17.y"], 0.5)
    if ay > 0:
        text(c, "TRIPARTITE", 760, 620, 52, "black", RED, ay)
        strike(c, 600, 602, 920, 602, ay)
        text(c, "faltaram os APOSENTADOS", 1240, 616, 36, "black", INK, ay)


def b_lei(c, t, C, B):
    head(c, t, B["start"], "DETALHE FINO", "LEI 8.212 × CONSTITUIÇÃO", GEST)
    twin(c, ep(t, C["18.t"], 0.5), ep(t, C["18.a"], 0.5),
         ("LEI 8.212", GRAY, [("trabalhadores", 36, "bold", INK), ("empresários", 36, "bold", INK), ("aposentados", 36, "bold", INK)]),
         ("CONSTITUIÇÃO", GEST, [("QUADRIPARTITE", 40, "black", GEST), ("trabalhadores · empregadores", 30, "bold", INK),
                                 ("aposentados · GOVERNO", 30, "bold", INK)]), y=180, h=480)
    pill(c, "“nos termos da Constituição” → os QUATRO", W / 2, 760, GEST, size=30, a=ep(t, C["18.b"], 0.5), anchor="center")


def b_q_quadri(c, t, C, B):
    head(c, t, C["19.e"] - 1.2, "QUESTÃO DE PROVA", "GESTÃO QUADRIPARTITE", GEST)
    card(c, 200, 180, 1520, 620)
    text(c, "Integram a gestão quadripartite, nos termos da Constituição:", W / 2, 270, 38, "bold", INK, ep(t, C["19.e"], 0.5))
    opts = [("19.a", "trabalhadores, empregadores, SERVIDORES PÚBLICOS e Governo", False),
            ("19.b", "trabalhadores, empregadores, APOSENTADOS e Governo", True)]
    ar = ep(t, C["19.r"], 0.4)
    for k, (cue, s, ok) in enumerate(opts):
        a, dy = rise(t, C[cue])
        y = 420 + k * 150 + dy
        if ar > 0:
            rrect(c, 260, y - 60, 1400, 100, 18, GREEN if ok else RED, 0.12 * ar)
            mark(c, ok, 1600, y - 12, ar, 26)
        text(c, s, 300, y, 38, "bold", INK, a, align="left")


def b_sintese(c, t, C, B):
    head(c, t, B["start"], "OS 7 PRINCÍPIOS", "NUM QUADRO SÓ", GREEN)
    card(c, 200, 160, 1520, 700)
    resumo = ["cobertura = risco · atendimento = pessoa", "uniformidade = tipo · equivalência = valor",
              "seletividade = o quê · distributividade = para quem", "o valor NOMINAL não cai",
              "cada um paga conforme pode", "várias fontes de dinheiro", "quadripartite: T · E · A · G"]
    for k, ((rom, nome, col), desc) in enumerate(zip(INC, resumo)):
        a, dy = rise(t, C[f"20.i{k + 1}"])
        y = 240 + k * 88 + dy
        inciso_tag(c, rom, 260, y, col, a, 32)
        text(c, nome, 400, y + 12, 34, "black", INK, a, align="left")
        text(c, desc, 1660, y + 12, 28, "semibold", GRAY, a, align="right")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["21.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 360, BLUE, size=30, a=a, anchor="center")
        text(c, "Financiamento da Seguridade", W / 2, 490, 64, "black", INK, a)
        text(c, "as fontes do art. 195", W / 2, 560, 38, "semibold", GRAY, a)
    cta(c, t, C["21.like"], C["21.sub"], C["21.bell"], C["21.com"], C["21.bye"], "Sabia do auxílio-acidente < 1 SM?")


BLOCKS = dict(hook=b_hook, lembrete=b_lembrete, irred=b_irred, nominal=b_nominal, piso=b_piso, q_piso=b_q_piso,
              equid=b_equid, equid_ex=b_equid_ex, q_equid=b_q_equid, divers=b_divers, fontes=b_fontes, ec103=b_ec103,
              exclusiv=b_exclusiv, gestao=b_gestao, quadri=b_quadri, falso=b_falso, lei=b_lei, q_quadri=b_q_quadri,
              sintese=b_sintese, cta=b_cta)
