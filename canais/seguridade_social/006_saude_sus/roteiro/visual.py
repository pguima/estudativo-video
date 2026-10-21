"""Visual do vídeo Seguridade 006 — Saúde e SUS na Constituição (arts. 196 a 200). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_006_saude_sus.mp4"
CARD_R = (140, 150, 1640, 690)

SAUDE = "#E5484D"
PREST = "#0F766E"
CUST = "#E8A317"
GEST = "#4F46E5"


def art_tag(c, s, x, y, col, a, size=40):
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
    result_box(c, resp, 1480, 560, 50, ar, GREEN if ok else RED)
    ax = ep(t, C[cue_x], 0.5)
    pill(c, expl, 960, 680, GREEN if ok else RED, size=30, a=ax, anchor="center")


def cruz(c, cx, cy, s, col, a):
    """cruz da saúde"""
    if a <= 0:
        return
    k = s / 3
    rrect(c, cx - k / 2, cy - s / 2, k, s, k * 0.25, col, a)
    rrect(c, cx - s / 2, cy - k / 2, s, k, k * 0.25, col, a)


def pessoa(c, cx, cy, s, col, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.55, s * 0.28, paint(col, a))
    p = skia.Path()
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.42, cy - s * 0.2, s * 0.84, s * 0.75), s * 0.3, s * 0.3))
    c.drawPath(p, paint(col, a))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 6", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    text(c, "Precisa ter CONTRIBUÍDO", W / 2, 360, 76, "black", INK, ep(t, B["start"] + 0.6, 0.5))
    text(c, "para ser atendido no SUS?", W / 2, 450, 66, "black", INK, ep(t, B["start"] + 1.4, 0.5))
    aa = ep(t, C["01.a"], 0.4)
    result_box(c, "NÃO", W / 2, 590, 72, aa, SAUDE)
    ac = ep(t, C["01.c"], 0.5)
    pill(c, "CF, arts. 196 a 200", W / 2, 750, PREST, size=34, a=ac, anchor="center")


def b_aberto(c, t, C, B):
    head(c, t, B["start"], "SAÚDE", "O PILAR MAIS ABERTO", SAUDE)
    card(c, *CARD_R)
    rows = [("02.a", "Você contribuiu?"), ("02.b", "Você é pobre?"), ("02.c", "Você é filiado a algum regime?")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 270 + k * 110 + dy
        text(c, s, 260, y, 44, "bold", INK, a, align="left")
        pill(c, "NÃO PERGUNTA", 1100, y - 14, GRAY, size=26, a=a, anchor="center")
    ad = ep(t, C["02.d"], 0.5)
    if ad > 0:
        pessoa(c, 1440, 420, 150, SAUDE, ad)
        cruz(c, 1440, 395, 46, "#FFFFFF", ad)
        result_box(c, "BASTA SER PESSOA", 960, 680, 50, ad, SAUDE)


def b_art196(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 196", "O MAIS COBRADO DO MÓDULO", SAUDE)
    card(c, *CARD_R)
    art_tag(c, "art. 196", 220, 220, SAUDE, ep(t, B["start"] + 0.3, 0.4), 30)
    lines = [("03.a", [("A saúde é ", INK), ("DIREITO DE TODOS", SAUDE), (" e ", INK), ("DEVER DO ESTADO,", SAUDE)]),
             ("03.b", [("garantido mediante políticas ", INK), ("SOCIAIS E ECONÔMICAS", PREST)]),
             ("03.c", [("que visem à ", INK), ("REDUÇÃO", CUST), (" do risco de doença e de outros agravos", INK)]),
             ("03.d", [("e ao acesso ", INK), ("UNIVERSAL E IGUALITÁRIO", PREST), (" às ações e serviços", INK)]),
             ("03.e", [("para sua ", INK), ("PROMOÇÃO, PROTEÇÃO E RECUPERAÇÃO.", SAUDE)])]
    for k, (cue, segs) in enumerate(lines):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        tot = sum(text_w(s, "bold", 38) for s, _ in segs)
        x = W / 2 - tot / 2
        for s, col in segs:
            x += text(c, s, x, 330 + k * 92 + dy, 38, "black" if col != INK else "semibold", col, a, align="left")


def b_desmonte(c, t, C, B):
    head(c, t, B["start"], "A BANCA TROCA", "CADA PEDAÇO DO ART. 196", RED)
    card(c, *CARD_R)
    rows = [("04.a", "direito de TODOS", "direito dos contribuintes"), ("04.b", "dever do ESTADO", "dever da família / da sociedade"),
            ("04.c", "REDUÇÃO do risco", "ELIMINAÇÃO do risco")]
    for k, (cue, ok, bad) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 130 + dy
        hi = k == 2
        if hi:
            rrect(c, 220, y - 62, 1480, 112, 18, CUST, 0.12 * a)
        check_icon(c, 270, y - 14, 24, a, GREEN)
        text(c, ok, 315, y, 42, "black", INK, a, align="left")
        arrow(c, 820, y - 14, 940, y - 14, GRAY, a, 4, 14)
        check_icon(c, 990, y - 14, 24, a, RED, "x")
        text(c, bad, 1035, y, 38, "bold", RED, a, align="left")
        if a > 0.3:
            strike(c, 1035, y - 14, 1035 + text_w(bad, "bold", 38), y - 14, a, RED, ep(t, C[cue] + 0.6, 0.4))
    ad = ep(t, C["04.d"], 0.5)
    pill(c, "o texto diz REDUÇÃO — nunca eliminação", W / 2, 720, CUST, size=32, a=ad, anchor="center")


def b_ppr(c, t, C, B):
    head(c, t, B["start"], "ART. 196", "MAIS DOIS DETALHES", SAUDE)
    aa, dya = rise(t, C["05.a"])
    if aa > 0:
        card(c, 200, 200 + dya, 700, 300, aa)
        text(c, "acesso", 550, 290 + dya, 38, "bold", GRAY, aa)
        text(c, "UNIVERSAL E", 550, 370 + dya, 50, "black", PREST, aa)
        text(c, "IGUALITÁRIO", 550, 430 + dya, 50, "black", PREST, aa)
        check_icon(c, 820, 260 + dya, 24, aa, GREEN)
    ab, dyb = rise(t, C["05.b"])
    if ab > 0:
        card(c, 1020, 200 + dyb, 700, 300, ab)
        text(c, "“gratuito”", 1370, 380 + dyb, 64, "black", RED, ab)
        strike(c, 1200, 360 + dyb, 1540, 360 + dyb, ab, RED, ep(t, C["05.b"] + 0.5, 0.4))
        text(c, "NÃO está no texto", 1370, 450 + dyb, 34, "bold", INK, ab)
    am = ep(t, C["05.m"], 0.5)
    for k, (cue_d, l, rest) in enumerate(((0.0, "P", "romoção"), (0.6, "P", "roteção"), (1.2, "R", "ecuperação"))):
        a = ep(t, C["05.c"] + cue_d, 0.4)
        x = 380 + k * 460
        text(c, l, x, 690, 120, "black", mix(LIGHT, SAUDE, am) if am > 0 else SAUDE, a, align="right")
        text(c, rest, x + 4, 690, 52, "black", INK, a, align="left")
    pill(c, "P · P · R", W / 2, 790, SAUDE, size=36, a=am, anchor="center")


def b_art197(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 197", "RELEVÂNCIA PÚBLICA", PREST)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.4, 0.5)
    text(c, "ações e serviços de saúde são de RELEVÂNCIA PÚBLICA", W / 2, 260, 42, "black", INK, a0)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text(c, "PODER PÚBLICO", 560, 350, 34, "black", PREST, aa)
        for k, (l, rest) in enumerate((("R", "egulamentação"), ("F", "iscalização"), ("C", "ontrole"))):
            a = ep(t, C["06.a"] + 0.6 * k, 0.4)
            y = 440 + k * 90
            text(c, l, 360, y + 20, 80, "black", PREST, a, align="right")
            text(c, rest, 366, y + 20, 44, "black", INK, a, align="left")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        line(c, 960, 340, 960, 720, LINE, ab, 3)
        text(c, "EXECUÇÃO", 1340, 350, 34, "black", CUST, ab)
        for k, s in enumerate(("diretamente", "por terceiros", "por pessoa física ou", "jurídica de direito privado")):
            a = ep(t, C["06.b"] + 0.5 * min(k, 2), 0.4)
            text(c, s, 1340, 440 + k * 70, 38, "bold", INK, a)


def b_art198(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 198", "O SISTEMA ÚNICO DE SAÚDE", SAUDE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        # rede hierarquizada
        nodes = [(560, 260, 1)] + [(380 + k * 180, 380, 2) for k in range(3)] + [(290 + k * 90, 490, 3) for k in range(7)]
        for x, y, lv in nodes[1:]:
            px, py = (560, 260) if lv == 2 else (380 + 180 * min(2, round((x - 290) / 90 / 2.4)), 380)
            line(c, px, py, x, y, LIGHT, aa, 3)
        for x, y, lv in nodes:
            c.drawCircle(x, y, 26 - lv * 4, paint(SAUDE if lv == 1 else PREST, aa))
        text(c, "regionalizada e hierarquizada", 560, 580, 32, "bold", INK, aa)
    ab = ep(t, C["07.b"], 0.5)
    result_box(c, "SISTEMA ÚNICO = SUS", 560, 670, 40, ab, SAUDE)
    ac = ep(t, C["07.c"], 0.5)
    text(c, "3 DIRETRIZES", 1340, 250, 34, "black", PREST, ac)
    for k, (cue, l, rest) in enumerate((("07.d1", "D", "escentralização"), ("07.d2", "A", "tendimento integral"),
                                        ("07.d3", "P", "articipação da comunidade"))):
        a, dy = rise(t, C[cue])
        y = 360 + k * 110 + dy
        text(c, l, 1080, y + 20, 84, "black", PREST, a, align="right")
        text(c, rest, 1086, y + 20, 38, "black", INK, a, align="left")
    pill(c, "D · A · P", 1340, 700, PREST, size=36, a=ep(t, C["07.m"], 0.5), anchor="center")


def b_dap(c, t, C, B):
    head(c, t, B["start"], "CADA DIRETRIZ TEM", "UM COMPLEMENTO QUE CAI", PREST)
    rows = [("08.a", "D", "DESCENTRALIZAÇÃO", "direção ÚNICA em CADA ESFERA de governo"),
            ("08.b", "A", "ATENDIMENTO INTEGRAL", "prioridade às PREVENTIVAS, sem prejuízo das assistenciais"),
            ("08.c", "P", "PARTICIPAÇÃO DA COMUNIDADE", "os conselhos de saúde")]
    for k, (cue, l, nome, comp) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 200 + k * 190 + dy
        card(c, 200, y, 1520, 160, a)
        rrect(c, 230, y + 25, 110, 110, 20, PREST, a)
        text_mid(c, l, 285, y + 80, 70, "black", "#FFFFFF", a)
        text(c, nome, 380, y + 65, 40, "black", INK, a, align="left")
        text(c, comp, 380, y + 120, 34, "bold", PREST, a, align="left")


def b_q_dir(c, t, C, B):
    ce(c, t, C, "09.e", "09.r", "09.x", ["O SUS tem como diretriz a descentralização,", "com direção única em ÂMBITO FEDERAL."],
       "ERRADO", False, "direção única EM CADA ESFERA de governo (art. 198, I)", "ART. 198 · DIRETRIZES", size=44)


def b_art199(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 199", "A INICIATIVA PRIVADA", CUST)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    text(c, "assistência à saúde é", 560, 280, 38, "bold", INK, aa)
    result_box(c, "LIVRE à iniciativa privada", 560, 370, 40, aa, CUST)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        c.drawCircle(1340, 400, 150, paint(SAUDE, ab * 0.12))
        c.drawCircle(1340, 400, 150, paint(SAUDE, ab, stroke=5))
        text_mid(c, "SUS", 1340, 400, 64, "black", SAUDE, ab)
        c.drawCircle(1520, 520, 70, paint(CUST, ab * 0.18))
        c.drawCircle(1520, 520, 70, paint(CUST, ab, stroke=4))
        text_mid(c, "privada", 1520, 520, 26, "black", INK, ab)
        text(c, "COMPLEMENTAR · contrato ou convênio", 560, 500, 34, "black", PREST, ab)
    ac = ep(t, C["10.c"], 0.5)
    pill(c, "preferência: FILANTRÓPICAS e SEM FINS LUCRATIVOS", 560, 590, GREEN, size=26, a=ac, anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        x1 = pill(c, "COMPLEMENTAR", 760, 710, GREEN, size=32, a=ad, anchor="center")[1]
        check_icon(c, x1 + 34, 710, 22, ad, GREEN)
        x1 = pill(c, "SUPLEMENTAR", 1160, 710, RED, size=32, a=ad, anchor="center")[1]
        check_icon(c, x1 + 34, 710, 22, ad, RED, "x")


def b_vedacoes(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 199 · §§ 2º A 4º", "AS TRÊS VEDAÇÕES", RED)
    rows = [("11.a", "RECURSO PÚBLICO", "para privada COM FINS LUCRATIVOS", "VEDADO", RED),
            ("11.b", "CAPITAL ESTRANGEIRO", "na assistência à saúde", "VEDADO, SALVO LEI", CUST),
            ("11.c", "COMERCIALIZAÇÃO", "de órgãos, tecidos e sangue", "VEDADA SEM RESSALVA", RED)]
    for k, (cue, nome, sub, res, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 200 + k * 190 + dy
        card(c, 200, y, 1520, 160, a)
        text(c, nome, 250, y + 70, 42, "black", INK, a, align="left")
        text(c, sub, 250, y + 120, 32, "bold", GRAY, a, align="left")
        pill(c, res, 1680, y + 80, col, size=30, a=a, anchor="right", bounds=(0, 1920))


def b_art200(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 200", "AS COMPETÊNCIAS DO SUS", SAUDE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    text(c, "“compete ao SUS, ALÉM DE OUTRAS ATRIBUIÇÕES, nos termos da lei”", W / 2, 260, 36, "semibold", INK, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        x1 = pill(c, "rol EXEMPLIFICATIVO", 760, 350, GREEN, size=32, a=ab, anchor="center")[1]
        check_icon(c, x1 + 34, 350, 22, ab, GREEN)
        x1 = pill(c, "taxativo", 1200, 350, RED, size=32, a=ab, anchor="center")[1]
        check_icon(c, x1 + 34, 350, 22, ab, RED, "x")
    rows = [("12.c", "SAÚDE DO TRABALHADOR", "EXECUTA", SAUDE), ("12.d", "SANEAMENTO BÁSICO", "PARTICIPA", CUST),
            ("12.e", "MEIO AMBIENTE", "COLABORA", PREST)]
    for k, (cue, s, verbo, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 260 + k * 480
        card(c, x, 440 + dy, 440, 220, a)
        text(c, s, x + 220, 530 + dy, 32, "black", INK, a)
        pill(c, verbo, x + 220, 600 + dy, col, size=30, a=a, anchor="center")


def b_caso(c, t, C, B):
    head(c, t, B["start"], "CASO PRÁTICO", "ROBERTO E O PLANO DE SAÚDE", PREST)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        pessoa(c, 400, 380, 170, INK, aa)
        text(c, "Roberto", 400, 560, 40, "black", INK, aa)
        for k, s in enumerate(("renda alta", "plano particular")):
            pill(c, s, 400, 620 + k * 60, CUST, size=26, a=ep(t, C["13.a"] + 0.6 * (k + 1), 0.4), anchor="center")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 640, 260, 300, 220, 20, SAUDE, ab * 0.12)
        cruz(c, 790, 370, 110, SAUDE, ab)
        text(c, "emergência pública", 790, 530, 30, "bold", INK, ab)
    for k, (cue, q) in enumerate((("13.c", "Recusar por causa do plano?"), ("13.d", "Cobrar por causa da renda?"))):
        a, dy = rise(t, C[cue])
        y = 320 + k * 150 + dy
        text(c, q, 1040, y, 38, "bold", INK, a, align="left")
        pill(c, "NÃO", 1040, y + 50, RED, size=30, a=ep(t, C[cue] + 1.2, 0.4))
    ae = ep(t, C["13.e"], 0.5)
    pill(c, "direito de TODOS · acesso universal e igualitário", 1290, 690, GREEN, size=28, a=ae, anchor="center")


def b_tripe(c, t, C, B):
    head(c, t, B["start"], "COMPARE OS PILARES", "QUEM TEM DIREITO?", PREST)
    cols = [("14.a", "SAÚDE", SAUDE, "TODOS", "sem contribuição · sem renda"),
            ("14.b", "ASSISTÊNCIA", CUST, "QUEM DELA NECESSITAR", "sem contribuição"),
            ("14.c", "PREVIDÊNCIA", PREST, "FILIADO QUE CONTRIBUI", "caráter contributivo")]
    cw, gap = 480, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, nome, col, quem, sub) in enumerate(cols):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 210 + dy, cw, 460, a)
        rrect(c, x, 210 + dy, cw, 100, 28, col, a)
        rrect(c, x, 270 + dy, cw, 40, 0, col, a)
        text_mid(c, nome, x + cw / 2, 260 + dy, 42, "black", "#FFFFFF", a)
        for j, ln in enumerate(quem.split(" ", 1) if len(quem) > 14 else [quem]):
            text(c, ln, x + cw / 2, 440 + dy + j * 60, 46, "black", col, a)
        text(c, sub, x + cw / 2, 600 + dy, 26, "semibold", GRAY, a)


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("15.p1", "15.r1", "o art. 196 garante acesso universal e GRATUITO", False, "universal e IGUALITÁRIO"),
             ("15.p2", "15.r2", "privadas participam do SUS de forma SUPLEMENTAR", False, "de forma COMPLEMENTAR"),
             ("15.p3", "15.r3", "compete ao SUS executar ações de SAÚDE DO TRABALHADOR", True, "art. 200, II")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_rol(c, t, C, B):
    ce(c, t, C, "16.e", "16.r", "16.x", ["O rol de competências do SUS, no art. 200, é", "TAXATIVO, não admitindo ampliação por lei."],
       "ERRADO", False, "“além de outras atribuições”: rol EXEMPLIFICATIVO", "LEI SECA · ART. 200", size=44)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("17.a", "direito de TODOS e dever do ESTADO (art. 196)"), ("17.b", "REDUÇÃO do risco, nunca eliminação"),
            ("17.c", "acesso UNIVERSAL E IGUALITÁRIO · P-P-R"), ("17.d", "SUS: D-A-P, direção única EM CADA ESFERA"),
            ("17.e", "privados no SUS: COMPLEMENTAR"), ("17.f", "rol do art. 200: EXEMPLIFICATIVO")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["18.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Assistência Social e LOAS", W / 2, 430, 64, "black", INK, a)
        for k, s in enumerate(("para quem é", "objetivos", "diretrizes")):
            pill(c, s, 660 + k * 300, 540, CUST, size=28, a=ep(t, B["start"] + 1.5 + 0.5 * k, 0.4) * a, anchor="center")
    cta(c, t, C["18.like"], C["18.sub"], C["18.bell"], C["18.com"], C["18.bye"], "Já caiu na pegadinha da eliminação?")


BLOCKS = dict(hook=b_hook, aberto=b_aberto, art196=b_art196, desmonte=b_desmonte, ppr=b_ppr, art197=b_art197,
              art198=b_art198, dap=b_dap, q_dir=b_q_dir, art199=b_art199, vedacoes=b_vedacoes, art200=b_art200,
              caso=b_caso, tripe=b_tripe, pegadinhas=b_pegadinhas, q_rol=b_q_rol, resumo=b_resumo, cta=b_cta)
