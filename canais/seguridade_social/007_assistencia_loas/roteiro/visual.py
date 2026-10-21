"""Visual do vídeo Seguridade 007 — Assistência Social e LOAS (arts. 203 e 204 + Lei 8.742). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_007_assistencia_loas.mp4"
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


def letras(c, t, C, cues, palavras, x0, y0, dy, col, size_l=84, size_r=40, am=0.0):
    for k, (cue, w) in enumerate(zip(cues, palavras)):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = y0 + k * dy + d
        text(c, w[0], x0, y + 20, size_l, "black", col, a, align="right")
        text(c, w[1:], x0 + 6, y + 20, size_r, "black", INK, a, align="left")


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 7", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    pil = [("SAÚDE", SAUDE, "para todos"), ("PREVIDÊNCIA", PREST, "quem contribui"), ("ASSISTÊNCIA", ASSIST, "?")]
    for k, (n, col, sub) in enumerate(pil):
        a = ep(t, B["start"] + 0.4 + 1.2 * k if k < 2 else C["01.a"], 0.5)
        x = 420 + k * 540
        rrect(c, x - 220, 280, 440, 100, 22, col, a, shadow=True)
        text_mid(c, n, x, 330, 40, "black", "#FFFFFF", a)
        text(c, sub, x, 440, 40 if k < 2 else 70, "bold" if k < 2 else "black", INK if k < 2 else ASSIST, a)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "VOCÊ PRECISA?", W / 2, 600, 96, "black", ASSIST, ab)
    ac = ep(t, C["01.c"], 0.5)
    pill(c, "CF, arts. 203 e 204  ·  LOAS (Lei 8.742/1993)", W / 2, 740, PREST, size=32, a=ac, anchor="center")


def b_art203(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 203", "A FRASE MAIS COBRADA DO PILAR", ASSIST)
    card(c, *CARD_R)
    tag(c, "art. 203", 220, 230, ASSIST, ep(t, B["start"] + 0.3, 0.4), 30)
    aa = ep(t, C["02.a"], 0.5)
    text(c, "“A assistência social será prestada", W / 2, 350, 44, "semibold", INK, aa)
    text(c, "A QUEM DELA NECESSITAR,", W / 2, 420, 50, "black", ASSIST, ep(t, C["02.a"] + 1.0, 0.5))
    ab = ep(t, C["02.b"], 0.5)
    text(c, "INDEPENDENTEMENTE DE CONTRIBUIÇÃO", W / 2, 490, 50, "black", PREST, ab)
    text(c, "à seguridade social”", W / 2, 550, 40, "semibold", INK, ab)
    ac = ep(t, C["02.c"], 0.5)
    if ac > 0:
        ok_x(c, "exige NECESSIDADE", 700, 670, True, ac, 32)
        ok_x(c, "exige CONTRIBUIÇÃO", 1240, 670, False, ep(t, C["02.c"] + 0.8, 0.4), 32)


def b_objetivos(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 203", "OS SEIS OBJETIVOS", ASSIST)
    objs = [("o1", "I", "proteção à FAMÍLIA, maternidade, infância, adolescência e velhice"),
            ("o2", "II", "amparo às crianças e adolescentes CARENTES"),
            ("o3", "III", "integração ao MERCADO DE TRABALHO"),
            ("o4", "IV", "HABILITAÇÃO e REABILITAÇÃO das pessoas com deficiência"),
            ("o5", "V", "UM SALÁRIO MÍNIMO ao idoso e à pessoa com deficiência"),
            ("o6", "VI", "redução da VULNERABILIDADE socioeconômica (EC 114/2021)")]
    card(c, 200, 170, 1520, 690)
    for k, (cue, rom, s) in enumerate(objs):
        a, dy = rise(t, C["03." + cue])
        if a <= 0:
            continue
        y = 260 + k * 98 + dy
        if k == 4:
            rrect(c, 230, y - 56, 1460, 86, 16, ASSIST, 0.14 * a)
        tag(c, rom, 250, y - 14, ASSIST if k == 4 else PREST, a, 30)
        text(c, s, 380, y, 34, "bold", INK, a, align="left")


def b_inciso5(c, t, C, B):
    head(c, t, B["start"], "PONTO DE OURO", "O INCISO V E O BPC", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        tag(c, "art. 203, V", 640, 300, ASSIST, aa, 40)
        arrow(c, 980, 300, 1150, 300, INK, aa, 5, 18, progress=ep(t, C["04.a"] + 0.3, 0.5))
        result_box(c, "BPC", 1300, 300, 64, aa, ASSIST)
    ab = ep(t, C["04.b"], 0.5)
    text(c, "“conforme dispuser a lei”", W / 2, 470, 58, "black", PREST, ab)
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        text(c, "quem fixa idade e renda é a", 820, 620, 40, "bold", INK, ac)
        pill(c, "LOAS", 1240, 606, PREST, size=40, a=ac, anchor="center")
        pill(c, "detalhes na AULA 8", W / 2, 720, GRAY, size=28, a=ep(t, C["04.c"] + 1.5, 0.4), anchor="center")


def b_art204(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 204", "FINANCIAMENTO E DIRETRIZES", PREST)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "DE ONDE VEM O DINHEIRO", 560, 260, 32, "black", GRAY, aa)
        rrect(c, 300, 300, 520, 140, 22, PREST, aa, shadow=True)
        text_mid(c, "orçamento da", 560, 345, 34, "bold", "#FFFFFF", aa)
        text_mid(c, "SEGURIDADE", 560, 395, 42, "black", "#FFFFFF", aa)
        pill(c, "+ outras fontes", 560, 500, ASSIST, size=30, a=ep(t, C["05.a"] + 1.0, 0.4), anchor="center")
    ab = ep(t, C["05.b"], 0.5)
    text(c, "2 DIRETRIZES (CF)", 1340, 260, 32, "black", GRAY, ab)
    for k, (cue, n, s, sub) in enumerate((("05.d1", "1", "DESCENTRALIZAÇÃO", "político-administrativa"),
                                          ("05.d2", "2", "PARTICIPAÇÃO DA POPULAÇÃO", "por organizações representativas"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 340 + k * 150 + dy
        card(c, 1000, y, 680, 120, a)
        badge_num(c, n, 1060, y + 60, a, 28, bg=PREST)
        text(c, s, 1110, y + 55, 34, "black", INK, a, align="left")
        text(c, sub, 1110, y + 95, 26, "bold", GRAY, a, align="left")


def b_competencias(c, t, C, B):
    head(c, t, B["start"], "DESCENTRALIZAÇÃO", "QUEM FAZ O QUÊ", PREST)
    aa, dya = rise(t, C["06.a"])
    if aa > 0:
        card(c, 200, 200 + dya, 700, 300, aa)
        tag(c, "UNIÃO", 240, 260 + dya, PREST, aa, 34)
        text(c, "coordenação e", 550, 380 + dya, 40, "bold", INK, aa)
        text(c, "NORMAS GERAIS", 550, 440 + dya, 48, "black", PREST, aa)
    ab, dyb = rise(t, C["06.b"])
    if ab > 0:
        card(c, 1020, 200 + dyb, 700, 300, ab)
        tag(c, "ESTADOS E MUNICÍPIOS", 1060, 260 + dyb, ASSIST, ab, 30)
        text(c, "coordenação e", 1370, 380 + dyb, 40, "bold", INK, ab)
        text(c, "EXECUÇÃO", 1370, 440 + dyb, 48, "black", ASSIST, ab)
    ac = ep(t, C["06.c"], 0.5)
    pill(c, "+ entidades beneficentes", 1370, 540, ASSIST, size=26, a=ac, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        card(c, 200, 600, 1520, 150, ad)
        text(c, "Estados e DF podem vincular até", 640, 690, 38, "bold", INK, ad)
        result_box(c, "0,5%", 1130, 676, 50, ad, PREST)
        text(c, "da receita tributária líquida", 1480, 690, 32, "bold", GRAY, ad)


def b_loas1(c, t, C, B):
    head(c, t, B["start"], "LOAS · ART. 1º", "OS QUATRO NÚCLEOS", PREST)
    nucs = [("07.n1", "DIREITO DO CIDADÃO", "e dever do Estado"), ("07.n2", "NÃO CONTRIBUTIVA", "política de seguridade"),
            ("07.n3", "MÍNIMOS SOCIAIS", "o que ela provê"), ("07.n4", "NECESSIDADES BÁSICAS", "o que ela garante")]
    for k, (cue, big, sub) in enumerate(nucs):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + (k % 2) * 780
        y = 210 + (k // 2) * 300 + dy
        card(c, x, y, 740, 250, a)
        badge_num(c, k + 1, x + 60, y + 60, a, 28, bg=PREST)
        text(c, big, x + 370, y + 145, 46, "black", INK, a)
        text(c, sub, x + 370, y + 200, 30, "bold", GRAY, a)


def b_pvd(c, t, C, B):
    head(c, t, B["start"], "LOAS · ART. 2º", "OS TRÊS OBJETIVOS", ASSIST)
    card(c, *CARD_R)
    letras(c, t, C, ["08.a", "08.b", "08.c"], ["Proteção social", "Vigilância socioassistencial", "Defesa de direitos"],
           620, 300, 140, ASSIST, 110, 50)
    pill(c, "P · V · D", W / 2, 740, ASSIST, size=40, a=ep(t, C["08.m"], 0.5), anchor="center")


def b_surid(c, t, C, B):
    head(c, t, B["start"], "LOAS · ART. 4º", "OS CINCO PRINCÍPIOS", PREST)
    card(c, *CARD_R)
    items = [("09.l1", "S", "upremacia", "das necessidades sociais sobre a rentabilidade"),
             ("09.l2", "U", "niversalização", "dos direitos sociais"),
             ("09.l3", "R", "espeito", "à dignidade do cidadão"),
             ("09.l4", "I", "gualdade", "de direitos no acesso"),
             ("09.l5", "D", "ivulgação", "ampla")]
    for k, (cue, l, rest, sub) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 100 + dy
        text(c, l, 330, y + 18, 84, "black", PREST, a, align="right")
        w = text(c, rest, 336, y + 18, 44, "black", INK, a, align="left")
        text(c, sub, 360 + w, y + 18, 32, "bold", GRAY, a, align="left")
    pill(c, "S · U · R · I · D", 1500, 740, PREST, size=36, a=ep(t, C["09.m"], 0.5), anchor="center")


def b_vexatoria(c, t, C, B):
    head(c, t, B["start"], "EXPRESSÃO DE OURO", "LOAS · ART. 4º, III", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    text(c, "“vedando-se qualquer", W / 2, 360, 64, "black", INK, aa)
    text(c, "COMPROVAÇÃO VEXATÓRIA", W / 2, 450, 70, "black", RED, ep(t, C["10.a"] + 0.8, 0.5))
    text(c, "de necessidade”", W / 2, 530, 64, "black", INK, ep(t, C["10.a"] + 1.4, 0.5))
    ab = ep(t, C["10.b"], 0.5)
    pill(c, "ninguém pode ser humilhado para provar que precisa", W / 2, 680, ASSIST, size=32, a=ab, anchor="center")


def b_dpp(c, t, C, B):
    head(c, t, B["start"], "LOAS · ART. 5º", "AS DIRETRIZES: CF × LOAS", PREST)
    ax = ep(t, C["11.x"], 0.5)
    ay = ep(t, C["11.y"], 0.5)
    rows = [("11.a", "D", "escentralização"), ("11.b", "P", "articipação da população"), ("11.c", "P", "rimazia do Estado")]
    card(c, 200, 190, 1000, 560)
    for k, (cue, l, rest) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 150 + dy
        if k == 2:
            rrect(c, 230, y - 70, 940, 120, 18, ASSIST, 0.15 * a)
        text(c, l, 360, y + 20, 90, "black", PREST if k < 2 else ASSIST, a, align="right")
        text(c, rest, 366, y + 20, 44, "black", INK, a, align="left")
    if ax > 0:
        card(c, 1260, 190, 460, 260, ax)
        text(c, "CONSTITUIÇÃO", 1490, 270, 34, "black", GRAY, ax)
        result_box(c, "2 diretrizes", 1490, 370, 44, ax, PREST)
    if ay > 0:
        card(c, 1260, 490, 460, 260, ay)
        text(c, "LOAS", 1490, 570, 34, "black", GRAY, ay)
        result_box(c, "3 diretrizes", 1490, 670, 44, ay, ASSIST)
        pill(c, "a PRIMAZIA só está na lei", 700, 800, ASSIST, size=28, a=ep(t, C["11.y"] + 1.2, 0.4), anchor="center")


def b_suas(c, t, C, B):
    head(c, t, B["start"], "SUAS", "SISTEMA ÚNICO DE ASSISTÊNCIA SOCIAL", ASSIST)
    aa, dya = rise(t, C["12.a"])
    if aa > 0:
        card(c, 200, 200 + dya, 700, 520, aa)
        text(c, "PROTEÇÃO SOCIAL BÁSICA", 550, 280 + dya, 32, "black", GRAY, aa)
        text(c, "CRAS", 550, 420 + dya, 120, "black", PREST, aa)
        text(c, "famílias vulneráveis", 550, 510 + dya, 36, "bold", INK, aa)
        pill(c, "ANTES da violação", 550, 620 + dya, GREEN, size=32, a=aa, anchor="center")
    ab, dyb = rise(t, C["12.b"])
    if ab > 0:
        card(c, 1020, 200 + dyb, 700, 520, ab)
        text(c, "PROTEÇÃO SOCIAL ESPECIAL", 1370, 280 + dyb, 32, "black", GRAY, ab)
        w = text_w("CREAS", "black", 120)
        x0 = 1370 - w / 2
        x = x0 + text(c, "CR", x0, 420 + dyb, 120, "black", RED, ab, align="left")
        x += text(c, "E", x, 420 + dyb, 120, "black", ASSIST, ab, align="left")
        text(c, "AS", x, 420 + dyb, 120, "black", RED, ab, align="left")
        text(c, "E de ESPECIALIZADO", 1370, 510 + dyb, 36, "bold", INK, ab)
    ac = ep(t, C["12.c"], 0.5)
    pill(c, "violação JÁ ACONTECEU", 1370, 620, RED, size=32, a=ac, anchor="center")


def b_eventuais(c, t, C, B):
    head(c, t, B["start"], "DERRUBA MUITA GENTE", "BENEFÍCIOS EVENTUAIS", RED)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    for k, s in enumerate(("auxílio-natalidade", "auxílio-funeral")):
        pill(c, s, 640 + k * 640, 280, INK, size=40, a=ep(t, C["13.a"] + 0.6 * k, 0.4), anchor="center")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        ok_x(c, "previdenciários", 640, 420, False, ab, 34)
    ac = ep(t, C["13.c"], 0.5)
    if ac > 0:
        ok_x(c, "EVENTUAIS da assistência", 1240, 420, True, ac, 34)
    ad = ep(t, C["13.d"], 0.5)
    for k, s in enumerate(("nascimento", "morte", "vulnerabilidade temporária", "calamidade pública")):
        pill(c, s, (470, 720, 1040, 1430)[k], 620, ASSIST, size=28, a=ep(t, C["13.d"] + 0.4 * k, 0.4), anchor="center")
    text(c, "LOAS, art. 22", W / 2, 740, 30, "bold", GRAY, ad)


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("14.p1", "14.r1", "prestada a quem necessitar, DESDE QUE tenha contribuído", False, "INDEPENDENTEMENTE de contribuição"),
             ("14.p2", "14.r2", "auxílio-funeral é benefício PREVIDENCIÁRIO", False, "benefício EVENTUAL da assistência"),
             ("14.p3", "14.r3", "é vedada qualquer comprovação vexatória de necessidade", True, "LOAS, art. 4º, III")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_dir(c, t, C, B):
    ce(c, t, C, "15.e", "15.r", "15.x",
       ["São diretrizes da assistência social, PREVISTAS NA", "CONSTITUIÇÃO, a descentralização, a participação",
        "da população e a primazia da responsabilidade do Estado."],
       "ERRADO", False, "a CF traz DUAS; a primazia do Estado é da LOAS (art. 5º, III)", "DIRETRIZES · CF × LOAS", size=40)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("16.a", "a quem dela necessitar, INDEPENDENTEMENTE de contribuição"),
            ("16.b", "6 objetivos na CF · o inciso V é a base do BPC"), ("16.c", "objetivos da LOAS: P · V · D"),
            ("16.d", "princípios: S · U · R · I · D"), ("16.e", "diretrizes: DUAS na CF, TRÊS na LOAS"),
            ("16.f", "CRAS previne · CREAS atua depois da violação")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["17.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "BPC e auxílio-inclusão", W / 2, 430, 64, "black", INK, a)
        pill(c, "o tema que MAIS CAI", W / 2, 540, ASSIST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a, anchor="center")
    cta(c, t, C["17.like"], C["17.sub"], C["17.bell"], C["17.com"], C["17.bye"], "Sabia que o auxílio-funeral saiu da previdência?")


BLOCKS = dict(hook=b_hook, art203=b_art203, objetivos=b_objetivos, inciso5=b_inciso5, art204=b_art204,
              competencias=b_competencias, loas1=b_loas1, pvd=b_pvd, surid=b_surid, vexatoria=b_vexatoria, dpp=b_dpp,
              suas=b_suas, eventuais=b_eventuais, pegadinhas=b_pegadinhas, q_dir=b_q_dir, resumo=b_resumo, cta=b_cta)
