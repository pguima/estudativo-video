"""Visual do vídeo Seguridade 008 — BPC e auxílio-inclusão (LOAS arts. 20, 21, 21-A e 26-A). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_008_bpc_auxilio_inclusao.mp4"
CARD_R = (140, 150, 1640, 690)

SAUDE = "#E5484D"
PREST = "#0F766E"
ASSIST = "#E8A317"
GEST = "#4F46E5"


def tag(c, s, x, y, col, a, size=40):
    w = text_w(s, "black", size) + 40
    rrect(c, x, y - size * 0.75, w, size * 1.5, 14, col, a)
    text_mid(c, s, x + w / 2, y, size, "black", "#FFFFFF", a)
    return w


def ce(c, t, C, cue_e, cue_r, cue_x, frase_lines, resp, ok, expl, head_l2, size=40):
    head(c, t, C[cue_e] - 1.2, "QUESTÃO DE PROVA", head_l2)
    card(c, 200, 180, 1520, 560)
    pill(c, "C / E", 240, 230, BLUE, size=26, bounds=(0, 1920))
    for k, ln in enumerate(frase_lines):
        text(c, ln, 280, 330 + k * (size + 24), size, "semibold", INK, ep(t, C[cue_e] + 0.7 * k, 0.4), align="left")
    ar = ep(t, C[cue_r], 0.4)
    result_box(c, resp, 1480, 590, 50, ar, GREEN if ok else RED)
    ax = ep(t, C[cue_x], 0.5)
    pill(c, expl, 960, 690, GREEN if ok else RED, size=30, a=ax, anchor="center")


def ok_x(c, s, x, cy, ok, a, size=30):
    """pílula com ✓/✗ ao lado, sem encostar"""
    x1 = pill(c, s, x, cy, GREEN if ok else RED, size=size, a=a, anchor="center")[1]
    check_icon(c, x1 + 34, cy, 22, a, GREEN if ok else RED, "check" if ok else "x")


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 8", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    for k, (s, col) in enumerate((("pago pelo INSS", PREST), ("1 salário mínimo", PREST))):
        ok_x(c, s, 640 + k * 640, 300, True, ep(t, B["start"] + 0.6 + 1.6 * k, 0.4), 34)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        text(c, "mas NÃO é", W / 2, 430, 50, "black", INK, aa)
        text(c, "PREVIDÊNCIA", W / 2, 520, 84, "black", RED, aa)
    ab, dy = rise(t, C["01.b"])
    if ab > 0:
        result_box(c, "BPC", W / 2, 650 + dy, 84, ab, ASSIST)
    ac = ep(t, C["01.c"], 0.5)
    pill(c, "LOAS, art. 20  ·  auxílio-inclusão  ·  BPC × previdência", W / 2, 790, PREST, size=30, a=ac, anchor="center")


def b_conceito(c, t, C, B):
    head(c, t, B["start"], "LOAS · ART. 20", "O QUE É O BPC", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["02.a"], 0.5)
    if aa > 0:
        text(c, "garantia de", W / 2, 260, 40, "bold", GRAY, aa)
        result_box(c, "1 SALÁRIO MÍNIMO mensal", W / 2, 330, 54, aa, ASSIST)
    for k, (cue, s, col) in enumerate((("02.b", "PESSOA COM DEFICIÊNCIA", GEST), ("02.c", "IDOSO com 65 anos ou mais", PREST))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 430 + dy, 680, 110, 22, col, a, shadow=True)
        text_mid(c, s, x, 485 + dy, 38, "black", "#FFFFFF", a)
    text(c, "ou", W / 2, 498, 40, "black", GRAY, ep(t, C["02.c"], 0.4))
    ad = ep(t, C["02.d"], 0.5)
    text(c, "sem meios de se manter", W / 2, 640, 46, "black", INK, ad)
    text(c, "nem de ser mantido pela família", W / 2, 700, 38, "bold", GRAY, ep(t, C["02.d"] + 1.2, 0.4))


def b_natureza(c, t, C, B):
    head(c, t, B["start"], "PONTO DE OURO", "A NATUREZA DO BPC", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        ok_x(c, "ASSISTENCIAL", 640, 270, True, aa, 40)
        ok_x(c, "previdenciário", 1240, 270, False, ep(t, C["03.a"] + 1.0, 0.4), 40)
    ab, dyb = rise(t, C["03.b"])
    if ab > 0:
        card(c, 260, 360 + dyb, 640, 200, ab)
        text(c, "QUEM OPERA", 580, 420 + dyb, 30, "black", GRAY, ab)
        text(c, "INSS", 580, 510 + dyb, 76, "black", PREST, ab)
    ac, dyc = rise(t, C["03.c"])
    if ac > 0:
        card(c, 1020, 360 + dyc, 640, 200, ac)
        text(c, "DE ONDE VEM O DINHEIRO", 1340, 420 + dyc, 30, "black", GRAY, ac)
        text(c, "ASSISTÊNCIA", 1340, 500 + dyc, 60, "black", ASSIST, ac)
        text(c, "não o fundo do RGPS", 1340, 540 + dyc, 26, "bold", RED, ac)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        text(c, "quem PAGA é o INSS,", 700, 700, 46, "black", PREST, ad)
        text(c, "quem MANDA é a LOAS", 1260, 700, 46, "black", ASSIST, ep(t, C["03.d"] + 1.2, 0.4))


def b_idade(c, t, C, B):
    head(c, t, B["start"], "REQUISITO 1", "A IDADE", PREST)
    aa, dya = rise(t, C["04.a"])
    if aa > 0:
        card(c, 200, 200 + dya, 700, 480, aa)
        text(c, "ESTATUTO DO IDOSO", 550, 280 + dya, 32, "black", GRAY, aa)
        text(c, "60", 550, 480 + dya, 200, "black", GRAY, aa)
        text(c, "anos", 550, 570 + dya, 44, "bold", GRAY, aa)
    ab, dyb = rise(t, C["04.b"])
    if ab > 0:
        card(c, 1020, 200 + dyb, 700, 480, ab)
        text(c, "BPC", 1370, 280 + dyb, 36, "black", PREST, ab)
        text(c, "65", 1370, 480 + dyb, 200, "black", PREST, ab)
        text(c, "anos · homem E mulher", 1370, 570 + dyb, 40, "bold", INK, ab)
        if aa > 0:
            strike(c, 380, 330 + dya, 720, 600 + dya, ab, RED, ep(t, C["04.b"] + 0.8, 0.5))
    ac = ep(t, C["04.c"], 0.5)
    pill(c, "a banca troca 60 por 65 o tempo todo", W / 2, 770, RED, size=32, a=ac, anchor="center")


def b_deficiencia(c, t, C, B):
    head(c, t, B["start"], "REQUISITO 2", "A DEFICIÊNCIA (ART. 20, §2º)", GEST)
    card(c, *CARD_R)
    steps = [("05.a", "IMPEDIMENTO", "físico · mental · intelectual · sensorial", GEST),
             ("05.b", "BARREIRAS", "em interação com uma ou mais", ASSIST),
             ("05.c", "PARTICIPAÇÃO", "plena e efetiva obstruída", RED)]
    for k, (cue, big, sub, col) in enumerate(steps):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 230, 230 + dy, 460, 120, 22, col, a, shadow=True)
        text_mid(c, big, x, 290 + dy, 40, "black", "#FFFFFF", a)
        text(c, sub, x, 400 + dy, 26, "bold", GRAY, a)
        if k > 0:
            text_mid(c, "+" if k == 1 else "→", x - 280, 290, 56, "black", INK, a)
    ad = ep(t, C["05.d"], 0.5)
    text(c, "modelo BIOPSICOSSOCIAL", W / 2, 540, 60, "black", GEST, ad)
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        ok_x(c, "deficiência = só a doença", W / 2 - 30, 680, False, ae, 34)


def b_longoprazo(c, t, C, B):
    head(c, t, B["start"], "LONGO PRAZO", "ART. 20, §10", GEST)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text(c, "efeitos por no mínimo", W / 2, 280, 42, "bold", GRAY, aa)
        text(c, "2 ANOS", W / 2, 420, 150, "black", GEST, aa)
    ab = ep(t, C["06.b"], 0.5)
    text(c, "AVALIAÇÃO DUPLA", W / 2, 540, 34, "black", GRAY, ab)
    ac = ep(t, C["06.c"], 0.5)
    if ac > 0:
        pill(c, "MÉDICA · médico perito", 660, 640, PREST, size=34, a=ac, anchor="center")
        pill(c, "SOCIAL · assistente social", 1260, 640, ASSIST, size=34, a=ep(t, C["06.c"] + 0.6, 0.4), anchor="center")


def b_renda(c, t, C, B):
    head(c, t, B["start"], "REQUISITO 3", "A RENDA (ART. 20, §3º)", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        text(c, "renda familiar mensal POR PESSOA", W / 2, 260, 40, "black", INK, aa)
        text(c, "≤", 720, 420, 110, "black", GRAY, aa)
        frac(c, "1", "4", 870, 385, 90, ASSIST, aa, "black")
        text(c, "do salário mínimo", 1200, 405, 48, "black", INK, aa, align="center")
    ab = ep(t, C["07.b"], 0.5)
    pill(c, "REGRA GERAL", W / 2, 545, GREEN, size=30, a=ab, anchor="center")
    ac = ep(t, C["07.c"], 0.5)
    if ac > 0:
        text(c, "pode AMPLIAR até", 720, 655, 40, "bold", INK, ac)
        frac(c, "1", "2", 990, 640, 54, PREST, ac, "black")
        text(c, "salário mínimo", 1200, 655, 40, "bold", INK, ac)
    ad = ep(t, C["07.d"], 0.5)
    text(c, "grau da deficiência · gastos com tratamento · na forma do regulamento", W / 2, 775, 28, "bold", GRAY, ad)


def b_familia(c, t, C, B):
    head(c, t, B["start"], "GRUPO FAMILIAR", "ROL FECHADO (ART. 20, §1º)", PREST)
    card(c, 200, 170, 1520, 680)
    rows = [("08.f1", "o REQUERENTE"), ("08.f2", "cônjuge ou companheiro"),
            ("08.f3", "pais (na falta de um: madrasta ou padrasto)"), ("08.f4", "irmãos SOLTEIROS"),
            ("08.f5", "filhos e enteados SOLTEIROS"), ("08.f6", "menores tutelados")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 80 + dy
        badge_num(c, k + 1, 290, y - 12, a, 24, bg=PREST)
        text(c, s, 340, y, 38, "bold", INK, a, align="left")
    ag = ep(t, C["08.g"], 0.5)
    if ag > 0:
        rrect(c, 260, 720, 1400, 90, 20, ASSIST, 0.16 * ag)
        text(c, "TODOS: desde que vivam SOB O MESMO TETO", W / 2, 780, 42, "black", ASSIST, ag)


def b_detalhes(c, t, C, B):
    head(c, t, B["start"], "3 DETALHES", "QUE DECIDEM A QUESTÃO", RED)
    items = [("09.a", "SOLTEIROS", "casado não entra"), ("09.b", "MESMO TETO", "outra casa não entra"),
             ("09.c", "ROL FECHADO", "só quem está na lista")]
    for k, (cue, big, sub) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 520
        card(c, x, 200 + dy, 480, 300, a)
        badge_num(c, k + 1, x + 60, 260 + dy, a, 28, bg=RED)
        text(c, big, x + 240, 380 + dy, 46, "black", INK, a)
        text(c, sub, x + 240, 440 + dy, 32, "bold", GRAY, a)
    ad = ep(t, C["09.d"], 0.5)
    for k, s in enumerate(("avós", "netos", "tios", "sogros", "cunhados")):
        a = ep(t, C["09.d"] + 0.35 * k, 0.4)
        if a > 0:
            ok_x(c, s, 340 + k * 300, 620, False, a, 34)
    text(c, "não entram, mesmo na mesma casa", W / 2, 740, 36, "black", RED, ad)


def b_naos(c, t, C, B):
    head(c, t, B["start"], "DECORE EM BLOCO", "OS CINCO NÃOS DO BPC", RED)
    card(c, 200, 170, 1520, 680)
    rows = [("10.n1", "exige contribuição"), ("10.n2", "exige carência"), ("10.n3", "tem 13º (abono anual)"),
            ("10.n4", "gera pensão por morte · é personalíssimo"), ("10.n5", "pode ser acumulado")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 112 + dy
        w = tag(c, "NÃO", 300, y - 14, RED, a, 40)
        text(c, s, 300 + w + 30, y, 44, "black", INK, a, align="left")


def b_acumulacao(c, t, C, B):
    head(c, t, B["start"], "ACUMULAÇÃO", "AS DUAS EXCEÇÕES (ART. 20, §4º)", PREST)
    card(c, *CARD_R)
    for k, (cue, s) in enumerate((("11.a", "ASSISTÊNCIA MÉDICA"), ("11.b", "PENSÃO ESPECIAL indenizatória"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 360, 260 + dy, 720, 200, 26, GREEN, a, shadow=True)
        text_mid(c, "BPC +", x, 320 + dy, 34, "black", "#FFFFFF", a)
        text_mid(c, s, x, 390 + dy, 40, "black", "#FFFFFF", a)
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        text(c, "SÓ ESSAS DUAS", W / 2, 580, 64, "black", INK, ac)
        ok_x(c, "qualquer outra hipótese", W / 2 - 30, 690, False, ep(t, C["11.c"] + 1.0, 0.4), 34)


def b_revisao(c, t, C, B):
    head(c, t, B["start"], "NÃO É VITALÍCIO", "REVISÃO, CESSAÇÃO E SUSPENSÃO", PREST)
    aa, dya = rise(t, C["12.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 480, 330, aa)
        text(c, "REVISÃO", 440, 260 + dya, 32, "black", GRAY, aa)
        text(c, "2 anos", 440, 380 + dya, 90, "black", PREST, aa)
        text(c, "LOAS, art. 21", 440, 470 + dya, 28, "bold", GRAY, aa)
    ac, dyc = rise(t, C["12.c"])
    if ac > 0:
        card(c, 720, 190 + dyc, 480, 330, ac)
        text(c, "CESSA", 960, 260 + dyc, 32, "black", GRAY, ac)
        text(c, "condições superadas", 960, 370 + dyc, 34, "black", INK, ac)
        text(c, "ou MORTE", 960, 430 + dyc, 40, "black", RED, ac)
    ae, dye = rise(t, C["12.e"])
    if ae > 0:
        card(c, 1240, 190 + dye, 480, 330, ae)
        text(c, "PcD PASSA A TRABALHAR", 1480, 260 + dye, 28, "black", GRAY, ae)
        text(c, "SUSPENSO", 1480, 380 + dye, 62, "black", ASSIST, ae)
        text(c, "não cancelado · art. 21-A", 1480, 470 + dye, 28, "bold", GRAY, ae)
    ab = ep(t, C["12.b"], 0.5)
    pill(c, "2 anos de impedimento ≠ 2 anos de revisão", 700, 610, ASSIST, size=30, a=ab * (1 - ep(t, C["12.c"], 0.4)),
         anchor="center")
    ad = ep(t, C["12.d"], 0.5)
    pill(c, "e se a PcD começar a trabalhar?", W / 2, 620, GEST, size=32, a=ad * (1 - ep(t, C["12.e"] + 2.5, 0.4)),
         anchor="center")
    ae2 = ep(t, C["12.e"] + 2.5, 0.5)
    text(c, "a lei NÃO quer punir quem tenta trabalhar", W / 2, 640, 40, "black", GREEN, ae2)


def b_inclusao(c, t, C, B):
    head(c, t, B["start"], "AUXÍLIO-INCLUSÃO", "LOAS, ART. 26-A (2021)", GEST)
    card(c, 140, 150, 900, 690)
    rows = [("13.a", "PcD MODERADA ou GRAVE que recebia o BPC"), ("13.b", "PASSOU A TRABALHAR"),
            ("13.b", "remuneração até 2 SALÁRIOS MÍNIMOS"), ("13.d", "NÃO acumula com o BPC")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue] + (0.9 if k == 2 else 0))
        if a <= 0:
            continue
        y = 250 + k * 120 + dy
        if k == 3:
            check_icon(c, 210, y - 12, 24, a, RED, "x")
        else:
            check_icon(c, 210, y - 12, 24, a, GREEN)
        text(c, s, 255, y, 32, "bold", INK, a, align="left")
    ac, dyc = rise(t, C["13.c"])
    if ac > 0:
        card(c, 1100, 150 + dyc, 680, 450, ac)
        text(c, "VALOR", 1440, 230 + dyc, 32, "black", GRAY, ac)
        text(c, "50%", 1440, 400 + dyc, 170, "black", GEST, ac)
        text(c, "do BPC · metade", 1440, 490 + dyc, 40, "bold", INK, ac)
    am = ep(t, C["13.m"], 0.5)
    pill(c, "metade do BPC para quem passou a trabalhar", 1440, 700, ASSIST, size=26, a=am, anchor="center",
         bounds=(1060, 1900))


def b_comparacao(c, t, C, B):
    head(c, t, B["start"], "A QUE MAIS CAI", "BPC × APOSENTADORIA", ASSIST)
    card(c, 160, 160, 1600, 700)
    ah = ep(t, B["start"] + 0.4, 0.5)
    text(c, "BPC (assistencial)", 1130, 240, 34, "black", ASSIST, ah)
    text(c, "aposentadoria", 1530, 240, 34, "black", PREST, ah)
    line(c, 200, 275, 1720, 275, LIGHT, ah, 3)
    rows = [("14.r1", "contribuição · carência · qualidade de segurado", False, True),
            ("14.r2", "teste de renda (¼ SM por pessoa)", True, False),
            ("14.r3", "13º salário e pensão por morte", False, True)]
    for k, (cue, s, bpc, apos) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 350 + k * 120 + dy
        text(c, s, 220, y, 34, "bold", INK, a, align="left")
        check_icon(c, 1130, y - 12, 30, a, GREEN if bpc else RED, "check" if bpc else "x")
        check_icon(c, 1530, y - 12, 30, a, GREEN if apos else RED, "check" if apos else "x")
    a4, dy4 = rise(t, C["14.r4"])
    if a4 > 0:
        y = 710 + dy4
        text(c, "base constitucional", 220, y, 34, "bold", INK, a4, align="left")
        pill(c, "CF, art. 203, V", 1130, y - 12, ASSIST, size=28, a=a4, anchor="center")
        pill(c, "CF, art. 201", 1530, y - 12, PREST, size=28, a=a4, anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("15.p1", "15.r1", "faz jus ao BPC o idoso com 60 ANOS ou mais", False, "são 65 anos (60 é o Estatuto)"),
             ("15.p2", "15.r2", "integram o grupo familiar os AVÓS sob o mesmo teto", False, "rol FECHADO: avós não entram"),
             ("15.p3", "15.r3", "o auxílio-inclusão corresponde a 100% do BPC", False, "é METADE: 50%")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_pensao(c, t, C, B):
    ce(c, t, C, "16.e", "16.r", "16.x",
       ["O BPC corresponde a um salário mínimo, ACRESCIDO", "DO ABONO ANUAL, e, falecendo o titular,",
        "CONVERTE-SE EM PENSÃO POR MORTE aos dependentes."],
       "ERRADO", False, "dupla armadilha: o BPC não tem 13º e não gera pensão", "13º E PENSÃO NO BPC", size=40)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("17.a", "ASSISTENCIAL: quem paga é o INSS, quem manda é a LOAS"),
            ("17.b", "1 SM · idoso 65+ ou PcD de longo prazo (2 anos)"),
            ("17.c", "renda por pessoa ≤ ¼ SM · grupo familiar FECHADO"),
            ("17.d", "os 5 NÃOS · só 2 exceções na acumulação"),
            ("17.e", "revisão a cada 2 anos · trabalho SUSPENDE"),
            ("17.f", "auxílio-inclusão = METADE do BPC")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["18.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Previdência Social e RGPS", W / 2, 430, 64, "black", INK, a)
        pill(c, "CF, art. 201 · fim da temporada 1", W / 2, 540, PREST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a,
             anchor="center")
    cta(c, t, C["18.like"], C["18.sub"], C["18.bell"], C["18.com"], C["18.bye"], "Sabia que o BPC não tem 13º?")


BLOCKS = dict(hook=b_hook, conceito=b_conceito, natureza=b_natureza, idade=b_idade, deficiencia=b_deficiencia,
              longoprazo=b_longoprazo, renda=b_renda, familia=b_familia, detalhes=b_detalhes, naos=b_naos,
              acumulacao=b_acumulacao, revisao=b_revisao, inclusao=b_inclusao, comparacao=b_comparacao,
              pegadinhas=b_pegadinhas, q_pensao=b_q_pensao, resumo=b_resumo, cta=b_cta)
