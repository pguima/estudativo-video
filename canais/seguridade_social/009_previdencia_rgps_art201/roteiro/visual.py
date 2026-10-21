"""Visual do vídeo Seguridade 009 — Previdência Social e RGPS (CF, art. 201). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_009_previdencia_rgps_art201.mp4"
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
    pill(c, "CONCURSO INSS · AULA 9", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    pil = [("SAÚDE", SAUDE, "entra de graça"), ("ASSISTÊNCIA", ASSIST, "entra de graça")]
    for k, (n, col, sub) in enumerate(pil):
        a = ep(t, B["start"] + 0.4 + 1.6 * k, 0.5)
        x = 560 + k * 800
        rrect(c, x - 220, 270, 440, 90, 22, col, a, shadow=True)
        text_mid(c, n, x, 315, 38, "black", "#FFFFFF", a)
        text(c, sub, x, 410, 32, "bold", GRAY, a)
    aa, dy = rise(t, C["01.a"])
    if aa > 0:
        rrect(c, W / 2 - 300, 470 + dy, 600, 110, 24, PREST, aa, shadow=True)
        text_mid(c, "PREVIDÊNCIA", W / 2, 525 + dy, 56, "black", "#FFFFFF", aa)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "ninguém entra de GRAÇA", W / 2, 660, 50, "black", INK, ab)
    ac = ep(t, C["01.c"], 0.5)
    text(c, "ninguém ESCOLHE não entrar", W / 2, 730, 50, "black", PREST, ac)
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "CF, art. 201  ·  fim da temporada 1", W / 2, 820, GRAY, size=28, a=ad, anchor="center")


def b_seguro(c, t, C, B):
    head(c, t, B["start"], "PREVIDÊNCIA", "UM SEGURO DIFERENTE", PREST)
    aa, dya = rise(t, C["02.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 700, 340, aa)
        text(c, "SEGURO PRIVADO", 550, 260 + dya, 32, "black", GRAY, aa)
        text(c, "entra SE QUISER", 550, 380 + dya, 52, "black", INK, aa)
        text(c, "contrato", 550, 460 + dya, 34, "bold", GRAY, aa)
    ab, dyb = rise(t, C["02.b"])
    if ab > 0:
        card(c, 1020, 190 + dyb, 700, 340, ab)
        text(c, "PREVIDÊNCIA SOCIAL", 1370, 260 + dyb, 32, "black", PREST, ab)
        text(c, "entra POR LEI", 1370, 380 + dyb, 52, "black", PREST, ab)
        text(c, "filiação obrigatória", 1370, 460 + dyb, 34, "bold", GRAY, ab)
    ac = ep(t, C["02.c"], 0.5)
    pill(c, "SOLIDÁRIA", W / 2, 610, ASSIST, size=36, a=ac, anchor="center")
    ad = ep(t, C["02.d"], 0.5)
    if ad > 0:
        text(c, "quem trabalha HOJE", 720, 730, 42, "black", INK, ad, align="right")
        arrow(c, 750, 716, 870, 716, INK, ad, 5, 18, progress=ep(t, C["02.d"] + 0.4, 0.5))
        text(c, "paga quem está aposentado HOJE", 900, 730, 42, "black", PREST, ep(t, C["02.d"] + 0.8, 0.4), align="left")


def b_cfe(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 201 · CAPUT", "OS TRÊS PILARES", PREST)
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    pill(c, "RGPS · Regime Geral de Previdência Social", W / 2, 220, PREST, size=32, a=aa, anchor="center")
    items = [("03.l1", "C", "aráter contributivo", "só recebe quem contribui"),
             ("03.l2", "F", "iliação obrigatória", "não depende de vontade"),
             ("03.l3", "E", "quilíbrio financeiro e atuarial", "receitas sustentam despesas")]
    for k, (cue, l, rest, sub) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 360 + k * 120 + dy
        text(c, l, 330, y + 18, 96, "black", PREST, a, align="right")
        w = text(c, rest, 336, y + 18, 50, "black", INK, a, align="left")
        text(c, sub, 360 + w, y + 18, 30, "bold", GRAY, a, align="left")
    pill(c, "C · F · E  =  contribui, filia, equilibra", W / 2, 760, ASSIST, size=34, a=ep(t, C["03.m"], 0.5), anchor="center")


def b_fin_atu(c, t, C, B):
    head(c, t, B["start"], "A BANCA ADORA", "FINANCEIRO × ATUARIAL", GEST)
    aa, dya = rise(t, C["04.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 700, 360, aa)
        text(c, "FINANCEIRO", 550, 280 + dya, 52, "black", PREST, aa)
        text(c, "CURTO prazo", 550, 380 + dya, 44, "black", INK, aa)
        text(c, "o que entra × o que sai hoje", 550, 450 + dya, 32, "bold", GRAY, aa)
    ab, dyb = rise(t, C["04.b"])
    if ab > 0:
        card(c, 1020, 190 + dyb, 700, 360, ab)
        text(c, "ATUARIAL", 1370, 280 + dyb, 52, "black", GEST, ab)
        text(c, "LONGO prazo", 1370, 380 + dyb, 44, "black", INK, ab)
        text(c, "projeção · expectativa de vida", 1370, 450 + dyb, 32, "bold", GRAY, ab)
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        text(c, "C · F · E são EXCLUSIVOS da previdência", W / 2, 650, 42, "black", INK, ac)
        ok_x(c, "saúde ou assistência com C-F-E", W / 2 - 30, 740, False, ep(t, C["04.c"] + 2.0, 0.4), 32)


def b_riscos(c, t, C, B):
    head(c, t, B["start"], "CF, ART. 201, I A V", "OS RISCOS COBERTOS", PREST)
    card(c, 200, 170, 1520, 690)
    rows = [("05.r1", "I", "I", "ncapacidade (temporária ou permanente) e idade avançada"),
            ("05.r2", "II", "M", "aternidade, especialmente a gestante"),
            ("05.r3", "III", "D", "esemprego involuntário"),
            ("05.r4", "IV", "S", "alário-família e auxílio-reclusão"),
            ("05.r5", "V", "M", "orte: pensão por morte")]
    for k, (cue, rom, l, rest) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 100 + dy
        tag(c, rom, 250, y - 14, PREST, a, 30)
        text(c, l, 420, y + 6, 60, "black", ASSIST, a, align="left")
        text(c, rest, 420 + text_w(l, "black", 60) + 4, y, 36, "bold", INK, a, align="left")
    pill(c, "I · M · D · S · M", W / 2, 790, ASSIST, size=38, a=ep(t, C["05.m"], 0.5), anchor="center")


def b_armadilhas(c, t, C, B):
    head(c, t, B["start"], "DUAS ARMADILHAS", "DOS INCISOS", RED)
    aa, dya = rise(t, C["06.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 700, 520, aa)
        tag(c, "inciso III", 240, 250 + dya, PREST, aa, 30)
        text(c, "seguro-desemprego", 550, 370 + dya, 46, "black", INK, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            ok_x(c, "pago pelo INSS", 530, 470 + dya, False, ab, 34)
            text(c, "vem do FAT", 550, 590 + dya, 56, "black", ASSIST, ep(t, C["06.b"] + 1.5, 0.4))
            text(c, "Fundo de Amparo ao Trabalhador", 550, 640 + dya, 26, "bold", GRAY, ep(t, C["06.b"] + 1.5, 0.4))
    ac, dyc = rise(t, C["06.c"])
    if ac > 0:
        card(c, 1020, 190 + dyc, 700, 520, ac)
        tag(c, "inciso IV", 1060, 250 + dyc, PREST, ac, 30)
        text(c, "salário-família e", 1370, 350 + dyc, 38, "bold", INK, ac)
        text(c, "auxílio-reclusão", 1370, 400 + dyc, 38, "bold", INK, ac)
        text(c, "aos DEPENDENTES", 1370, 490 + dyc, 46, "black", PREST, ac)
        ad = ep(t, C["06.d"], 0.5)
        text(c, "de segurados de BAIXA RENDA", 1370, 560 + dyc, 36, "black", ASSIST, ad)
    ae = ep(t, C["06.e"], 0.5)
    pill(c, "a banca troca DEPENDENTES por SEGURADOS ou apaga a BAIXA RENDA", W / 2, 790, RED, size=28, a=ae, anchor="center")


def b_p1(c, t, C, B):
    head(c, t, B["start"], "ART. 201, §1º", "CRITÉRIOS DIFERENCIADOS", PREST)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.5, 0.5)
    text(c, "regra: VEDADOS", W / 2, 250, 50, "black", RED, a0)
    aa = ep(t, C["07.a"], 0.5)
    pill(c, "2 exceções · só por LEI COMPLEMENTAR", W / 2, 330, ASSIST, size=32, a=aa, anchor="center")
    for k, (cue, big, sub) in enumerate((("07.b", "COM DEFICIÊNCIA", "avaliação biopsicossocial"),
                                         ("07.c", "EFETIVA EXPOSIÇÃO", "a agentes nocivos à saúde"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 400 + dy, 680, 170, 24, PREST if k == 0 else GEST, a, shadow=True)
        text_mid(c, big, x, 460 + dy, 42, "black", "#FFFFFF", a)
        text_mid(c, sub, x, 520 + dy, 30, "bold", "#FFFFFF", a)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        ok_x(c, "enquadrar por CATEGORIA PROFISSIONAL", W / 2 - 30, 660, False, ad, 32)
        text(c, "tem que PROVAR a exposição", W / 2, 760, 40, "black", INK, ep(t, C["07.d"] + 2.0, 0.4))


def b_p2(c, t, C, B):
    head(c, t, B["start"], "ART. 201, §2º", "O PISO DE 1 SALÁRIO MÍNIMO", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    text(c, "nenhum benefício que", W / 2, 260, 42, "bold", INK, aa)
    text(c, "SUBSTITUA", W / 2, 350, 84, "black", ASSIST, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        w = text_w("SUBSTITUA", "black", 84)
        line(c, W / 2 - w / 2, 372, W / 2 + w / 2, 372, ASSIST, ab, 8)
    text(c, "o salário terá valor inferior ao salário mínimo", W / 2, 430, 38, "bold", INK, aa)
    ac = ep(t, C["08.c"], 0.5)
    text(c, "NÃO substitui → pode ser MENOR", W / 2, 540, 42, "black", INK, ac)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        pill(c, "salário-família", 760, 630, GEST, size=34, a=ad, anchor="center")
        pill(c, "auxílio-acidente", 1160, 630, GEST, size=34, a=ep(t, C["08.d"] + 0.8, 0.4), anchor="center")
    ae = ep(t, C["08.e"], 0.5)
    if ae > 0:
        ok_x(c, "NENHUM benefício abaixo do mínimo", W / 2 - 30, 760, False, ae, 32)


def b_p4p6(c, t, C, B):
    head(c, t, B["start"], "ART. 201, §§4º E 6º", "VALOR REAL E 13º", PREST)
    aa, dya = rise(t, C["09.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 700, 300, aa)
        tag(c, "201, §4º", 240, 250 + dya, PREST, aa, 30)
        text(c, "valor REAL", 550, 380 + dya, 64, "black", PREST, aa)
        text(c, "reajuste · RGPS", 550, 440 + dya, 32, "bold", GRAY, aa)
    ab, dyb = rise(t, C["09.b"])
    if ab > 0:
        card(c, 1020, 190 + dyb, 700, 300, ab)
        tag(c, "194, IV", 1060, 250 + dyb, GEST, ab, 30)
        text(c, "valor NOMINAL", 1370, 380 + dyb, 64, "black", GEST, ab)
        text(c, "irredutibilidade · seguridade", 1370, 440 + dyb, 32, "bold", GRAY, ab)
    ac, dyc = rise(t, C["09.c"])
    if ac > 0:
        card(c, 200, 550 + dyc, 1520, 200, ac)
        tag(c, "201, §6º", 240, 610 + dyc, ASSIST, ac, 30)
        text(c, "13º de aposentados e pensionistas: base em", 860, 690 + dyc, 38, "bold", INK, ac)
        result_box(c, "DEZEMBRO", 1470, 676 + dyc, 44, ac, ASSIST)


def b_p5(c, t, C, B):
    head(c, t, B["start"], "ART. 201, §5º", "A MELHOR PEGADINHA", RED)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        text(c, "participante de REGIME PRÓPRIO", W / 2, 260, 46, "black", INK, aa)
        text(c, "(servidor efetivo)", W / 2, 315, 32, "bold", GRAY, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        ok_x(c, "RGPS como FACULTATIVO", W / 2 - 30, 410, False, ab, 40)
    ac = ep(t, C["10.c"], 0.5)
    text(c, "mas, se tiver OUTRA ATIVIDADE abrangida pelo RGPS...", W / 2, 520, 36, "bold", INK, ac)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        ok_x(c, "RGPS como OBRIGATÓRIO", W / 2 - 30, 610, True, ad, 40)
    ae = ep(t, C["10.e"], 0.5)
    text(c, "não ESCOLHE entrar · se a atividade OBRIGA, entra", W / 2, 750, 40, "black", PREST, ae)


def b_p7(c, t, C, B):
    head(c, t, B["start"], "ART. 201, §7º (EC 103/2019)", "AS IDADES DA APOSENTADORIA", PREST)
    for k, (cue, tit, h, m, col, sub) in enumerate((("11.a", "REGRA GERAL", "65", "62", PREST, "+ tempo mínimo de contribuição"),
                                                   ("11.b", "RURAL", "60", "55", ASSIST, "e regime de economia familiar"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 820
        card(c, x, 190 + dy, 700, 460, a)
        text(c, tit, x + 350, 260 + dy, 36, "black", col, a)
        for j, (lab, n) in enumerate((("HOMEM", h), ("MULHER", m))):
            cx = x + 190 + j * 320
            text(c, n, cx, 450 + dy, 150, "black", col, a)
            text(c, lab, cx, 520 + dy, 30, "black", GRAY, a)
        text(c, sub, x + 350, 600 + dy, 28, "bold", GRAY, a)
    ac = ep(t, C["11.c"], 0.5)
    pill(c, "5 anos a menos = EQUIVALÊNCIA na prática", W / 2, 750, GREEN, size=34, a=ac, anchor="center")


def b_p9(c, t, C, B):
    head(c, t, B["start"], "ART. 201, §9º", "CONTAGEM RECÍPROCA", GEST)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 300, 420, 160, 26, PREST, aa, shadow=True)
        text_mid(c, "RGPS", 510, 380, 64, "black", "#FFFFFF", aa)
        rrect(c, 1200, 300, 420, 160, 26, GEST, aa, shadow=True)
        text_mid(c, "RPPS", 1410, 380, 64, "black", "#FFFFFF", aa)
        pr = ep(t, C["12.a"] + 0.6, 1.0)
        arrow(c, 760, 350, 1160, 350, INK, aa, 5, 18, progress=pr)
        arrow(c, 1160, 410, 760, 410, INK, aa, 5, 18, progress=pr)
        text(c, "o TEMPO viaja", W / 2, 300, 36, "black", INK, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        result_box(c, "COMPENSAÇÃO FINANCEIRA", W / 2, 590, 50, ab, GEST)
        text(c, "os regimes acertam as contas entre si", W / 2, 700, 34, "bold", GRAY, ab)


def b_regimes(c, t, C, B):
    head(c, t, B["start"], "OS REGIMES", "ONDE O RGPS SE ENCAIXA", PREST)
    cols = [("13.a", "RGPS", "CF, art. 201", "trabalhadores em geral", "gestor: INSS", PREST),
            ("13.b", "RPPS", "CF, art. 40", "servidores efetivos", "gestor: o ente", GEST),
            ("13.d", "COMPLEMENTAR", "CF, art. 202", "PRIVADA", "FACULTATIVA", ASSIST)]
    for k, (cue, n, base, l1, l2, col) in enumerate(cols):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 520
        card(c, x, 190 + dy, 480, 460, a)
        rrect(c, x + 30, 220 + dy, 420, 100, 20, col, a)
        text_mid(c, n, x + 240, 270 + dy, 44 if k < 2 else 36, "black", "#FFFFFF", a)
        text(c, base, x + 240, 380 + dy, 32, "black", GRAY, a)
        text(c, l1, x + 240, 470 + dy, 36, "black", INK, a)
        text(c, l2, x + 240, 530 + dy, 36, "black" if k == 2 else "bold", INK if k == 2 else GRAY, a)
    ac = ep(t, C["13.c"], 0.5)
    pill(c, "RGPS e RPPS: PÚBLICOS e OBRIGATÓRIOS", 720, 730, PREST, size=32, a=ac, anchor="center")


def b_servicos(c, t, C, B):
    head(c, t, B["start"], "DERRUBA MUITA GENTE", "BENEFÍCIOS × SERVIÇOS", RED)
    aa, dya = rise(t, C["14.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 600, 460, aa)
        text(c, "BENEFÍCIOS", 500, 280 + dya, 44, "black", PREST, aa)
        text(c, "em DINHEIRO", 500, 350 + dya, 34, "bold", GRAY, aa)
        for k, s in enumerate(("aposentadorias", "pensão por morte", "auxílios · salários")):
            text(c, s, 500, 450 + k * 60 + dya, 32, "bold", INK, aa)
    ab, dyb = rise(t, C["14.b"])
    if ab > 0:
        card(c, 880, 190 + dyb, 840, 460, ab)
        text(c, "SERVIÇOS", 1300, 280 + dyb, 44, "black", ASSIST, ab)
        text(c, "SÓ DOIS", 1300, 350 + dyb, 34, "black", RED, ab)
    for k, (cue, s) in enumerate((("14.c", "SERVIÇO SOCIAL"), ("14.d", "REABILITAÇÃO PROFISSIONAL"))):
        a = ep(t, C[cue], 0.5)
        if a > 0:
            badge_num(c, k + 1, 960, 450 + k * 110, a, 26, bg=ASSIST)
            text(c, s, 1010, 462 + k * 110, 40, "black", INK, a, align="left")
    ae = ep(t, C["14.e"], 0.5)
    if ae > 0:
        ok_x(c, "perícia médica como 3º serviço", W / 2 - 30, 760, False, ae, 32)


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("15.p1", "15.r1", "a previdência tem caráter contributivo e filiação FACULTATIVA", False, "a filiação é OBRIGATÓRIA"),
             ("15.p2", "15.r2", "aposentadoria: 65 anos para o homem e 60 para a MULHER", False, "são 62 anos (§7º, I)"),
             ("15.p3", "15.r3", "o §4º assegura a preservação do valor REAL dos benefícios", True, "art. 201, §4º (nominal é o 194, IV)")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_piso(c, t, C, B):
    ce(c, t, C, "16.e", "16.r", "16.x",
       ["Nenhum benefício previdenciário terá valor", "mensal INFERIOR AO SALÁRIO MÍNIMO."],
       "ERRADO", False, "o piso vale só para benefício que SUBSTITUI a renda (§2º)", "O PISO DO §2º", size=46)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("17.a", "caput: C · F · E (contributivo, filiação obrigatória, equilíbrio)"),
            ("17.b", "riscos: I · M · D · S · M"),
            ("17.c", "piso de 1 SM só para benefício SUBSTITUTIVO"),
            ("17.d", "quem tem regime próprio NÃO vira facultativo"),
            ("17.e", "idades: 65 H · 62 M  ·  rural: 60 H · 55 M"),
            ("17.f", "serviços do RGPS: só DOIS")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["18.like"] - 0.3)
    if a > 0:
        pill(c, "FIM DA TEMPORADA 1", W / 2, 260, GREEN, size=30, a=a, anchor="center")
        pill(c, "PRÓXIMA AULA · TEMPORADA 2", W / 2, 360, BLUE, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a, anchor="center")
        text(c, "Segurados e dependentes", W / 2, 480, 64, "black", INK, ep(t, B["start"] + 1.5, 0.4) * a)
        pill(c, "o RGPS por dentro", W / 2, 580, PREST, size=30, a=ep(t, B["start"] + 2.5, 0.4) * a, anchor="center")
    cta(c, t, C["18.like"], C["18.sub"], C["18.bell"], C["18.com"], C["18.bye"], "Sabia que o INSS não paga o seguro-desemprego?")


BLOCKS = dict(hook=b_hook, seguro=b_seguro, cfe=b_cfe, fin_atu=b_fin_atu, riscos=b_riscos, armadilhas=b_armadilhas,
              p1=b_p1, p2=b_p2, p4p6=b_p4p6, p5=b_p5, p7=b_p7, p9=b_p9, regimes=b_regimes, servicos=b_servicos,
              pegadinhas=b_pegadinhas, q_piso=b_q_piso, resumo=b_resumo, cta=b_cta)
