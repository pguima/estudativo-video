"""Visual do vídeo Seguridade 005 — Contrapartida, noventena, imunidade e orçamento (§§ do art. 195). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_005_contrapartida_orcamento.mp4"
CARD_R = (140, 150, 1640, 690)

SAUDE = "#E5484D"
PREST = "#0F766E"
CUST = "#E8A317"
GEST = "#4F46E5"


def par_tag(c, s, x, y, col, a, size=40):
    """etiqueta do parágrafo (§5º etc.) em caixa colorida"""
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


def calendario(c, x, y, mes, dia, col, a, w=300, h=300):
    card(c, x, y, w, h, a)
    rrect(c, x, y, w, 80, 28, col, a)
    rrect(c, x, y + 40, w, 40, 0, col, a)
    text_mid(c, mes, x + w / 2, y + 40, 34, "black", "#FFFFFF", a)
    text_mid(c, str(dia), x + w / 2, y + 80 + (h - 80) / 2, 120, "black", INK, a)


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 5", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    aa = ep(t, C["01.a"], 0.5)
    text(c, "OS PARÁGRAFOS DO", W / 2, 380, 84, "black", INK, aa)
    result_box(c, "CF, art. 195", W / 2, 490, 60, aa, PREST)
    ab = ep(t, C["01.b"], 0.5)
    pill(c, "onde a banca derruba muita gente", W / 2, 630, RED, size=34, a=ab, anchor="center")
    for k, s in enumerate(("total", "estendido", "90 dias", "isentas", "60 meses")):
        a, dy = rise(t, C["01.c"] + 0.35 * k)
        pill(c, s, 470 + k * 245, 760 + dy, CUST, fg=INK, size=30, a=a, anchor="center")


def b_mapa(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO", "DE HOJE")
    card(c, *CARD_R)
    rows = [("02.a", "§5º", "regra da CONTRAPARTIDA", PREST), ("02.b", "§4º", "NOVAS FONTES de custeio", GEST),
            ("02.c", "§6º", "NOVENTENA", CUST), ("02.d", "§7º", "IMUNIDADE das beneficentes", SAUDE),
            ("02.e", "LOA", "o ORÇAMENTO da seguridade", BLUE)]
    for k, (cue, tag, s, col) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 108 + dy
        par_tag(c, tag, 420, y, col, a, 36)
        text(c, s, 600, y + 14, 44, "black", INK, a, align="left")


def b_contra(c, t, C, B):
    head(c, t, B["start"], "§5º · A FRASE MAIS COBRADA", "REGRA DA CONTRAPARTIDA", PREST)
    card(c, *CARD_R)
    par_tag(c, "CF, art. 195, §5º", 220, 230, PREST, ep(t, B["start"] + 0.3, 0.4), 30)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "“Nenhum benefício ou serviço da seguridade social", W / 2, 350, 42, "semibold", INK, aa)
    text(c, "poderá ser CRIADO, MAJORADO ou ESTENDIDO", W / 2, 420, 46, "black", PREST, ep(t, C["03.a"] + 1.2, 0.5))
    ab = ep(t, C["03.b"], 0.5)
    text(c, "sem a correspondente fonte de CUSTEIO TOTAL.”", W / 2, 490, 46, "black", INK, ab)
    if ab > 0:
        x0 = W / 2 + text_w("sem a correspondente fonte de ", "black", 46) / 2 - text_w("CUSTEIO TOTAL.”", "black", 46) / 2
        hline(c, x0 - 10, x0 + text_w("CUSTEIO TOTAL", "black", 46) + 10, 508, CUST, ab, 6, progress=ep(t, C["03.b"] + 0.6, 0.6))
    ac = ep(t, C["03.c"], 0.5)
    pill(c, "contrapartida = preexistência do custeio", W / 2, 640, PREST, size=32, a=ac, anchor="center")


def b_verbos(c, t, C, B):
    head(c, t, B["start"], "§5º", "OS TRÊS VERBOS", PREST)
    cw, gap = 460, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    verbos = [("04.a", "CRIADO", "benefício novo", "+"), ("04.b", "MAJORADO", "aumento de valor", "↑"),
              ("04.c", "ESTENDIDO", "mais gente recebe", "→")]
    ax = ep(t, C["04.x"], 0.5)
    for k, (cue, v, sub, sym) in enumerate(verbos):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 190 + dy, cw, 380, a)
        c.drawCircle(x + cw / 2, 300 + dy, 62, paint(PREST, a * 0.15))
        text_mid(c, sym, x + cw / 2, 300 + dy, 64, "black", PREST, a)
        text(c, v, x + cw / 2, 440 + dy, 52, "black", INK, a)
        text(c, sub, x + cw / 2, 500 + dy, 32, "semibold", GRAY, a)
        if k == 2 and ax > 0:
            strike(c, x + 70, 425 + dy, x + cw - 70, 425 + dy, ax, RED, ep(t, C["04.x"] + 0.4, 0.5))
            pill(c, "a banca tira este", x + cw / 2, 610, RED, size=26, a=ax, anchor="center")
    ay = ep(t, C["04.y"], 0.5)
    if ay > 0:
        text(c, "custeio", 720, 720, 44, "black", INK, ay)
        pill(c, "TOTAL", 900, 706, GREEN, size=34, a=ay, anchor="center")
        check_icon(c, 1010, 706, 22, ay, GREEN)
        pill(c, "PARCIAL", 1240, 706, RED, size=34, a=ay, anchor="center")
        check_icon(c, 1370, 706, 22, ay, RED, "x")


def b_residual(c, t, C, B):
    head(c, t, B["start"], "§4º · COMPETÊNCIA RESIDUAL", "NOVAS FONTES DE CUSTEIO", GEST)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.4, 0.5)
    text(c, "a lei pode criar OUTRAS FONTES", W / 2, 260, 46, "black", INK, a0)
    text(c, "para MANTER ou EXPANDIR a seguridade", W / 2, 320, 36, "bold", GRAY, a0)
    aa = ep(t, C["05.a"], 0.5)
    pill(c, "segue o art. 154, I", W / 2, 400, GEST, size=32, a=aa, anchor="center")
    cw, gap = 440, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    req = [("05.r1", "LEI", "COMPLEMENTAR"), ("05.r2", "NÃO", "CUMULATIVA"), ("05.r3", "FATO GERADOR E BASE", "DIFERENTES")]
    for k, (cue, l1, l2) in enumerate(req):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 470 + dy, cw, 190, a)
        badge_num(c, str(k + 1), x + 50, 520 + dy, a, 24, bg=GEST)
        text(c, l1, x + cw / 2, 570 + dy, 34, "black", INK, a)
        text(c, l2, x + cw / 2, 620 + dy, 34, "black", GEST, a)


def b_ouro_lei(c, t, C, B):
    q = C["06.q"]
    if t < q - 0.2:
        head(c, t, B["start"], "PONTO DE OURO", "QUAL LEI?", CUST, t_out=q - 0.6)
        card(c, *CARD_R)
        aa, dya = rise(t, C["06.a"])
        if aa > 0:
            card(c, 260, 240 + dya, 620, 400, aa)
            text(c, "fonte JÁ PREVISTA", 570, 330 + dya, 44, "black", INK, aa)
            text(c, "no art. 195", 570, 385 + dya, 34, "bold", GRAY, aa)
            result_box(c, "LEI ORDINÁRIA", 570, 520 + dya, 46, aa, PREST)
        ab, dyb = rise(t, C["06.b"])
        if ab > 0:
            card(c, 1040, 240 + dyb, 620, 400, ab)
            text(c, "fonte NOVA", 1350, 330 + dyb, 44, "black", INK, ab)
            text(c, "residual (§4º)", 1350, 385 + dyb, 34, "bold", GRAY, ab)
            result_box(c, "LEI COMPLEMENTAR", 1350, 520 + dyb, 46, ab, GEST)
    else:
        ce(c, t, C, "06.q", "06.r", "06.x", ["Nova fonte de custeio para expandir a seguridade", "pode ser criada por LEI ORDINÁRIA."],
           "ERRADO", False, "fonte residual exige LEI COMPLEMENTAR (art. 195, §4º)", "§4º · FONTE RESIDUAL", size=42)


def b_noventena(c, t, C, B):
    head(c, t, B["start"], "§6º · ANTERIORIDADE NONAGESIMAL", "A NOVENTENA", CUST)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    text(c, "contribuições sociais só podem ser exigidas", W / 2, 260, 40, "semibold", INK, aa)
    text(c, "após", 640, 360, 46, "black", INK, aa)
    result_box(c, "90 DIAS", 860, 350, 60, aa, CUST)
    text(c, "da publicação da lei", 1250, 360, 40, "bold", INK, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        card(c, 300, 470, 620, 190, ab)
        text(c, "NOVENTENA (90 dias)", 610, 545, 38, "black", INK, ab)
        pill(c, "APLICA", 610, 610, GREEN, size=28, a=ab, anchor="center")
        ab2 = ep(t, C["07.b"] + 1.0, 0.5)
        card(c, 1000, 470, 620, 190, ab2)
        text(c, "anterioridade DE EXERCÍCIO", 1310, 545, 36, "black", INK, ab2)
        pill(c, "NÃO APLICA (art. 150, III, b)", 1310, 610, RED, size=26, a=ab2, anchor="center")


def b_calendario(c, t, C, B):
    head(c, t, B["start"], "NOVENTENA", "NA PRÁTICA", CUST)
    card(c, *CARD_R)
    aa, dya = rise(t, C["08.a"])
    calendario(c, 300, 240 + dya, "DEZEMBRO", 1, PREST, aa)
    text(c, "lei publicada", 450, 600, 32, "bold", GRAY, aa)
    ab, dyb = rise(t, C["08.b"])
    if ab > 0:
        arrow(c, 660, 390, 1220, 390, CUST, ab, 6, 22, progress=ep(t, C["08.b"], 0.8))
        pill(c, "+ 90 dias", 940, 340, CUST, fg=INK, size=30, a=ab, anchor="center")
    calendario(c, 1260, 240 + dyb, "MARÇO", 1, GREEN, ab)
    text(c, "já pode cobrar", 1410, 600, 32, "bold", GREEN, ab)
    ac = ep(t, C["08.c"], 0.5)
    pill(c, "não espera o exercício seguinte", 940, 470, INK, size=26, a=ac, anchor="center")
    ax = ep(t, C["08.x"], 0.5)
    if ax > 0:
        for k, (s, ok) in enumerate((("60 dias", False), ("120 dias", False), ("90 dias", True))):
            a = ep(t, C["08.x"] + 0.5 * k, 0.4)
            x = 620 + k * 340
            pill(c, s, x, 690, GREEN if ok else RED, size=32, a=a, anchor="center")
            check_icon(c, x + 110, 690, 20, a, GREEN if ok else RED, "check" if ok else "x")


def b_imune(c, t, C, B):
    head(c, t, B["start"], "§7º · ENTIDADES BENEFICENTES", "A PEGADINHA MAIS ELEGANTE", SAUDE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    par_tag(c, "CF, art. 195, §7º", 220, 230, SAUDE, aa, 30)
    text(c, "“São ISENTAS de contribuição para a seguridade social", W / 2, 340, 40, "semibold", INK, aa)
    text(c, "as entidades BENEFICENTES de assistência social", W / 2, 400, 40, "semibold", INK, ep(t, C["09.a"] + 1.0, 0.5))
    text(c, "que atendam às exigências estabelecidas em lei.”", W / 2, 460, 40, "semibold", INK, ep(t, C["09.a"] + 2.0, 0.5))
    ab = ep(t, C["09.b"], 0.5)
    pill(c, "regra está NA CONSTITUIÇÃO", 620, 600, PREST, size=30, a=ab, anchor="center")
    if ab > 0:
        arrow(c, 860, 600, 1060, 600, INK, ab, 5, 18, progress=ep(t, C["09.b"] + 0.5, 0.6))
    ac = ep(t, C["09.c"], 0.5)
    result_box(c, "IMUNIDADE", 1300, 600, 50, ac, SAUDE)


def b_isen_imun(c, t, C, B):
    head(c, t, B["start"], "ISENÇÃO × IMUNIDADE", "LEIA O COMANDO DA QUESTÃO", SAUDE)
    aa, dya = rise(t, C["10.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 720, 300, aa)
        text(c, "ISENÇÃO", 560, 280 + dya, 54, "black", GRAY, aa)
        text(c, "dispensa dada por LEI", 560, 360 + dya, 38, "bold", INK, aa)
    ab, dyb = rise(t, C["10.b"])
    if ab > 0:
        card(c, 1000, 190 + dyb, 720, 300, ab)
        text(c, "IMUNIDADE", 1360, 280 + dyb, 54, "black", SAUDE, ab)
        text(c, "proibição dada pela", 1360, 360 + dyb, 38, "bold", INK, ab)
        text(c, "CONSTITUIÇÃO", 1360, 415 + dyb, 38, "black", INK, ab)
    ac = ep(t, C["10.c"], 0.5)
    if ac > 0:
        card(c, 200, 560, 720, 200, ac)
        text(c, "pede a LITERALIDADE?", 560, 640, 36, "black", INK, ac)
        pill(c, "“isentas”", 560, 705, PREST, size=32, a=ac, anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        card(c, 1000, 560, 720, 200, ad)
        text(c, "pede a NATUREZA JURÍDICA?", 1360, 640, 36, "black", INK, ad)
        pill(c, "IMUNIDADE", 1360, 705, SAUDE, size=32, a=ad, anchor="center")


def b_ampc(c, t, C, B):
    head(c, t, B["start"], "§9º · ALÍQUOTAS DIFERENCIADAS", "OS 4 CRITÉRIOS", CUST)
    cw, gap = 380, 30
    x0 = W / 2 - (4 * cw + 3 * gap) / 2
    crit = [("11.l1", "A", "ATIVIDADE", "econômica"), ("11.l2", "M", "MÃO DE OBRA", "intensiva"),
            ("11.l3", "P", "PORTE", "da empresa"), ("11.l4", "C", "CONDIÇÃO", "do mercado de trabalho")]
    am = ep(t, C["11.m"], 0.5)
    for k, (cue, l, nome, sub) in enumerate(crit):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 190 + dy, cw, 400, a)
        text(c, l, x + cw / 2, 360 + dy, 140, "black", mix(LIGHT, CUST, am), a)
        text(c, nome, x + cw / 2, 470 + dy, 38, "black", INK, a)
        text(c, sub, x + cw / 2, 520 + dy, 28, "semibold", GRAY, a)
    pill(c, "A · M · P · C", W / 2, 640, CUST, fg=INK, size=40, a=am, anchor="center")
    ax = ep(t, C["11.x"], 0.5)
    if ax > 0:
        text(c, "BASE DE CÁLCULO diferenciada:", 560, 770, 34, "black", INK, ax)
        for k, (s, ok) in enumerate((("receita", True), ("lucro", True), ("folha", False))):
            x = 1000 + k * 230
            pill(c, s, x, 758, GREEN if ok else RED, size=30, a=ax, anchor="center")
            check_icon(c, x + 90, 758, 18, ax, GREEN if ok else RED, "check" if ok else "x")


def b_sessenta(c, t, C, B):
    head(c, t, B["start"], "§11 · MORATÓRIA E PARCELAMENTO", "O LIMITE DE 60 MESES", RED)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.4, 0.5)
    text(c, "VEDADOS moratória e parcelamento acima de", 700, 280, 40, "black", INK, a0)
    result_box(c, "60 MESES", 1440, 268, 56, a0, RED)
    aa = ep(t, C["12.a"], 0.5)
    pill(c, "remissão e anistia: só na forma de LEI COMPLEMENTAR", W / 2, 390, GEST, size=30, a=aa, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    text(c, "vale APENAS para:", W / 2, 500, 40, "black", RED, ab)
    for k, (cue, tag, s) in enumerate((("12.c", "I, a", "FOLHA de salários"), ("12.d", "II", "TRABALHADOR"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 660
        card(c, x, 550 + dy, 600, 130, a)
        par_tag(c, tag, x + 30, 615 + dy, PREST, a, 32)
        text(c, s, x + 360, 630 + dy, 40, "black", INK, a)
    pill(c, "as contribuições PREVIDENCIÁRIAS", W / 2, 790, PREST, size=28, a=ep(t, C["12.d"] + 1.2, 0.5), anchor="center")


def b_loa(c, t, C, B):
    head(c, t, B["start"], "O ORÇAMENTO · CF, ART. 165, §5º", "A LOA TEM 3 ORÇAMENTOS", BLUE)
    aa = ep(t, C["13.a"], 0.5)
    rrect(c, W / 2 - 360, 180, 720, 100, 22, BLUE, aa, shadow=True)
    text_mid(c, "LEI ORÇAMENTÁRIA ANUAL", W / 2, 230, 42, "black", "#FFFFFF", aa)
    am = ep(t, C["13.m"], 0.5)
    orc = [("13.o1", "F", "FISCAL", ""), ("13.o2", "I", "INVESTIMENTO", "das estatais"), ("13.o3", "S", "SEGURIDADE", "social")]
    cw, gap = 460, 50
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, l, nome, sub) in enumerate(orc):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        line(c, W / 2, 280, x + cw / 2, 360, LIGHT, a, 4)
        hi = k == 2
        card(c, x, 360 + dy, cw, 330, a)
        if hi:
            rrect(c, x, 360 + dy, cw, 330, 28, PREST, 0.10 * a)
        text(c, l, x + cw / 2, 500 + dy, 110, "black", mix(LIGHT, PREST if hi else BLUE, am), a)
        text(c, nome, x + cw / 2, 590 + dy, 42, "black", PREST if hi else INK, a)
        text(c, sub, x + cw / 2, 640 + dy, 30, "semibold", GRAY, a)
    pill(c, "F · I · S", 700, 770, BLUE, size=38, a=am, anchor="center")
    pill(c, "seguridade = orçamento PRÓPRIO", 1220, 770, PREST, size=30, a=ep(t, C["13.x"], 0.5), anchor="center")


def b_integrada(c, t, C, B):
    head(c, t, B["start"], "§2º · A PROPOSTA DE ORÇAMENTO", "ELABORAÇÃO CONJUNTA, GESTÃO SEPARADA", PREST)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    pil = [("SAÚDE", SAUDE), ("PREVIDÊNCIA", PREST), ("ASSISTÊNCIA", CUST)]
    for k, (s, col) in enumerate(pil):
        x = 420 + k * 540
        rrect(c, x - 220, 220, 440, 90, 20, col, aa)
        text_mid(c, s, x, 265, 36, "black", "#FFFFFF", aa)
    if aa > 0:
        for k in range(3):
            line(c, 420 + k * 540, 310, W / 2, 380, LIGHT, aa, 4)
        pill(c, "de forma INTEGRADA · metas da LDO", W / 2, 410, PREST, size=30, a=aa, anchor="center")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "assegurada a CADA ÁREA a gestão de seus recursos", W / 2, 510, 38, "black", INK, ab)
        for k, (s, col) in enumerate(pil):
            c.drawCircle(420 + k * 540, 580, 24, paint(col, ab))
    ac = ep(t, C["14.c"], 0.5)
    pill(c, "elaboração CONJUNTA · gestão SEPARADA", W / 2, 650, INK, size=28, a=ac, anchor="center")
    ad = ep(t, C["14.d"], 0.5)
    pill(c, "§1º: receitas de Estados, DF e Municípios NÃO integram o orçamento da União", W / 2, 760, BLUE, size=26, a=ad, anchor="center")


def b_vinculo(c, t, C, B):
    head(c, t, B["start"], "A BANCA ADORA · CF, ART. 167, XI", "DINHEIRO CARIMBADO", RED)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    for k, (tag, s) in enumerate((("I, a", "contribuição sobre a FOLHA"), ("II", "contribuição do TRABALHADOR"))):
        a = ep(t, C["15.a"] + 0.6 * k, 0.5)
        y = 270 + k * 110
        par_tag(c, tag, 240, y, PREST, a, 32)
        text(c, s, 400, y + 14, 40, "black", INK, a, align="left")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        arrow(c, 1080, 320, 1260, 320, INK, ab, 5, 18, progress=ep(t, C["15.b"], 0.6))
        rrect(c, 1290, 250, 400, 140, 20, GREEN, ab, shadow=True)
        text_mid(c, "SÓ benefícios", 1490, 300, 34, "black", "#FFFFFF", ab)
        text_mid(c, "do RGPS", 1490, 345, 30, "bold", "#FFFFFF", ab)
    ac = ep(t, C["15.c"], 0.5)
    for k, (s, col) in enumerate((("SAÚDE", SAUDE), ("ASSISTÊNCIA", CUST))):
        a = ep(t, C["15.c"] + 0.6 * k, 0.4)
        x = 640 + k * 640
        card(c, x - 250, 490, 500, 130, a)
        text_mid(c, s, x - 20, 555, 40, "black", col, a)
        check_icon(c, x + 190, 555, 24, a, RED, "x")
    pill(c, "a integração da seguridade NÃO derruba a vinculação", W / 2, 720, RED, size=28, a=ep(t, C["15.x"], 0.5), anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("16.p1", "16.r1", "contribuições sociais respeitam a anterioridade DE EXERCÍCIO", False, "só a NOVENTENA (90 dias)"),
             ("16.p2", "16.r2", "o limite de 60 meses alcança TODAS as contribuições", False, "só a da FOLHA e a do TRABALHADOR"),
             ("16.p3", "16.r3", "a CF chama de ISENTAS as entidades beneficentes", True, "é a literalidade (natureza: imunidade)")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_contra(c, t, C, B):
    ce(c, t, C, "17.e", "17.r", "17.x",
       ["Nenhum benefício ou serviço da seguridade social", "poderá ser criado ou majorado sem a",
        "correspondente fonte de custeio total."],
       "ERRADO", False, "faltou o verbo ESTENDIDO (art. 195, §5º)", "LEI SECA · §5º", size=40)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("18.a", "§5º: criado, majorado ou estendido só com custeio TOTAL"), ("18.b", "§4º: fonte nova = LEI COMPLEMENTAR"),
            ("18.c", "§6º: NOVENTA DIAS, sem anterioridade de exercício"), ("18.d", "§7º: o texto diz ISENTAS; a natureza é IMUNIDADE"),
            ("18.e", "§11: parcelamento de no máximo 60 MESES"), ("18.f", "LOA: três orçamentos, F · I · S")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["19.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "A Saúde na Constituição", W / 2, 430, 64, "black", INK, a)
        for k, s in enumerate(("SUS", "diretrizes", "o que mais cai")):
            pill(c, s, 660 + k * 300, 540, SAUDE, size=28, a=ep(t, B["start"] + 1.5 + 0.5 * k, 0.4) * a, anchor="center")
    cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"], "Já caiu na pegadinha da isenção?")


BLOCKS = dict(hook=b_hook, mapa=b_mapa, contra=b_contra, verbos=b_verbos, residual=b_residual, ouro_lei=b_ouro_lei,
              noventena=b_noventena, calendario=b_calendario, imune=b_imune, isen_imun=b_isen_imun, ampc=b_ampc,
              sessenta=b_sessenta, loa=b_loa, integrada=b_integrada, vinculo=b_vinculo, pegadinhas=b_pegadinhas,
              q_contra=b_q_contra, resumo=b_resumo, cta=b_cta)
