"""Visual do vídeo Seguridade 002 — Princípios parte 1 (incisos I–III). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_002_principios_parte1.mp4"
CARD_R = (140, 150, 1640, 690)

PREST = "#0F766E"   # prestação
CUST = "#E8A317"    # custeio
GEST = "#4F46E5"    # gestão
INC = [("I", "Universalidade", PREST), ("II", "Uniformidade e equivalência", PREST),
       ("III", "Seletividade e distributividade", PREST), ("IV", "Irredutibilidade", PREST),
       ("V", "Equidade no custeio", CUST), ("VI", "Diversidade da base de financiamento", CUST),
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
    pill(c, expl, 960, 660, RED if not ok else GREEN, size=30, a=ax, anchor="center")


def twin(c, t, a_left, a_right, left, right, y=200, h=520):
    """dois cartões lado a lado: (titulo, cor, linhas[(txt,size,peso,cor)])"""
    for k, ((tit, col, lines), a) in enumerate(((left, a_left), (right, a_right))):
        if a <= 0:
            continue
        x = 200 + k * 780
        dy = (1 - a) * 18
        card(c, x, y + dy, 740, h, a)
        rrect(c, x, y + dy, 740, 14, 7, col, a)
        text(c, tit, x + 370, y + 110 + dy, 56, "black", col, a)
        for j, (s, size, peso, cc) in enumerate(lines):
            text(c, s, x + 370, y + 210 + dy + j * (size + 26), size, peso, cc or INK, a)


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 2", W / 2, 220, BLUE, size=30, a=a0, anchor="center")
    text(c, "OS 7 PRINCÍPIOS", W / 2, 360, 96, "black", INK, a0)
    text(c, "da Seguridade Social · art. 194", W / 2, 430, 40, "semibold", GRAY, a0)
    ab = ep(t, C["01.c"], 0.5)
    for k, (l, r) in enumerate((("COBERTURA", "ATENDIMENTO"), ("IGUALDADE", "EQUIVALÊNCIA"))):
        a = ep(t, C["01.c"] + 1.3 * k, 0.5)
        y = 560 + k * 110
        pill(c, l, W / 2 - 60, y, RED, size=34, a=a, anchor="right", bounds=(0, 1920))
        text(c, "×", W / 2, y + 14, 46, "black", INK, a)
        pill(c, r, W / 2 + 60, y, RED, size=34, a=a, bounds=(0, 1920))
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "HOJE: incisos I, II e III", W / 2, 820, BLUE, size=32, a=ad, anchor="center")


def b_lista(c, t, C, B):
    head(c, t, B["start"], "ART. 194, PARÁGRAFO ÚNICO", "OS 7 OBJETIVOS")
    card(c, 300, 170, 1320, 680)
    for k, (rom, nome, col) in enumerate(INC):
        a, dy = rise(t, C[f"02.i{k + 1}"])
        y = 250 + k * 86 + dy
        inciso_tag(c, rom, 360, y, col, a, 34)
        text(c, nome, 520, y + 14, 40, "bold", INK, a, align="left")


def b_mnemonico(c, t, C, B):
    head(c, t, B["start"], "MEMORIZE A ORDEM", "UM UNIVERSO SELETO...", GREEN)
    card(c, *CARD_R)
    words = ["Um", "Universo", "Seleto", "Irredutível", "Equilibra", "Diversas", "Comunidades"]
    princ = ["Universalidade", "Uniformidade", "Seletividade", "Irredutibilidade", "Equidade", "Diversidade", "Caráter dem."]
    fs, gap = 58, 30
    while sum(text_w(wd, "black", fs) for wd in words) + gap * 6 > 1520:
        fs -= 2
    total = sum(text_w(wd, "black", fs) for wd in words) + gap * 6
    x = W / 2 - total / 2
    for k, (wd, pr) in enumerate(zip(words, princ)):
        a = ep(t, C["03.f"] + 0.45 * k, 0.4)
        ww = text_w(wd, "black", fs)
        col = INC[k][2]
        text(c, wd[0], x, 420, fs, "black", col, a, align="left")
        text(c, wd[1:], x + text_w(wd[0], "black", fs), 420, fs, "black", INK, a, align="left")
        al = ep(t, C["03.l"], 0.4)
        text(c, INC[k][0], x + ww / 2, 520, 34, "black", col, al * a)
        text(c, pr, x + ww / 2, 570 + 34 * (k % 2), 22, "bold", GRAY, al * a)
        x += ww + gap


def b_nome(c, t, C, B):
    head(c, t, B["start"], "NOMENCLATURA", "OBJETIVOS OU PRINCÍPIOS?")
    twin(c, t, ep(t, C["04.cf"], 0.5), ep(t, C["04.lei"], 0.5),
         ("CONSTITUIÇÃO", BLUE, [("art. 194, parágrafo único", 32, "semibold", GRAY), ("“OBJETIVOS”", 60, "black", INK)]),
         ("LEI 8.212/1991", GEST, [("art. 1º, parágrafo único", 32, "semibold", GRAY), ("“PRINCÍPIOS E", 52, "black", INK), ("DIRETRIZES”", 52, "black", INK)]))
    pill(c, "os dois nomes estão CERTOS", W / 2, 800, GREEN, size=32, a=ep(t, C["04.x"], 0.5), anchor="center")


def b_corte(c, t, C, B):
    head(c, t, B["start"], "O CORTE QUE RESOLVE", "METADE DAS QUESTÕES", AMBER)
    groups = [("04b.p", "PRESTAÇÃO", "o que a pessoa RECEBE", "I · II · III · IV", PREST),
              ("04b.c", "CUSTEIO", "de onde vem o DINHEIRO", "V · VI", CUST),
              ("04b.g", "GESTÃO", "quem MANDA", "VII", GEST)]
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, tit, sub, incs, col) in enumerate(groups):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 200 + dy, cw, 470, a)
        rrect(c, x, 200 + dy, cw, 14, 7, col, a)
        text(c, tit, x + cw / 2, 310 + dy, 52, "black", col, a)
        text(c, sub, x + cw / 2, 370 + dy, 30, "semibold", GRAY, a)
        text(c, incs, x + cw / 2, 520 + dy, 64, "black", INK, a)
    ax = ep(t, C["04b.x"], 0.5)
    pill(c, "dinheiro ENTRANDO? só pode ser V ou VI", W / 2, 760, CUST, size=32, a=ax, anchor="center")


def b_univ(c, t, C, B):
    head(c, t, B["start"], "INCISO I", "UNIVERSALIDADE DA COBERTURA E DO ATENDIMENTO")
    s6 = C["06"]
    am = ep(t, C["06.m"], 0.5)
    twin(c, t, ep(t, C["05.c"], 0.5), ep(t, C["05.a"], 0.5),
         ("COBERTURA", BLUE, [("os RISCOS", 44, "black", INK), ("doença · velhice", 32, "semibold", GRAY),
                              ("morte · maternidade", 32, "semibold", GRAY)]),
         ("ATENDIMENTO", GEST, [("as PESSOAS", 44, "black", INK), ("urbano · rural", 32, "semibold", GRAY),
                                ("doméstico · autônomo", 32, "semibold", GRAY)]), y=190, h=480)
    if am > 0:
        pill(c, "cobertura = COISA", 570, 740, BLUE, size=34, a=am, anchor="center")
        pill(c, "atendimento = ALGUÉM", 1350, 740, GEST, size=34, a=am, anchor="center")
        pill(c, "OBJETIVA", 570, 820, BLUE, size=26, a=ep(t, C["06.o"], 0.4), anchor="center")
        pill(c, "SUBJETIVA", 1350, 820, GEST, size=26, a=ep(t, C["06.s"], 0.4), anchor="center")


def b_absoluta(c, t, C, B):
    head(c, t, B["start"], "ATENÇÃO", "A UNIVERSALIDADE NÃO É ABSOLUTA", RED)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    text(c, "é um OBJETIVO a ser perseguido", W / 2, 300, 50, "black", INK, aa)
    pill(c, "convive com o caráter CONTRIBUTIVO da Previdência", W / 2, 390, PREST, size=30, a=aa, anchor="center")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 480, 1320, 180, 24, RED, 0.08 * ab)
        text(c, "“pela universalidade, qualquer pessoa recebe", W / 2, 560, 38, "semibold", INK, ab)
        text(c, "benefício previdenciário sem contribuir”", W / 2, 615, 38, "semibold", INK, ab)
    result_box(c, "ERRADO", W / 2, 760, 50, ep(t, C["07.c"], 0.4), RED)


def b_contra(c, t, C, B):
    head(c, t, B["start"], "COMO SERIA UMA VIOLAÇÃO?", "CONTRAEXEMPLO", RED)
    card(c, *CARD_R)
    aa = ep(t, C["07b.a"], 0.5)
    rrect(c, 300, 260, 1320, 140, 24, INK, 0.06 * aa)
    text(c, "Lei: “os trabalhadores RURAIS ficam fora da proteção na velhice”", W / 2, 345, 36, "bold", INK, aa)
    ab = ep(t, C["07b.b"], 0.5)
    for k in range(8):
        x = 520 + k * 120
        col = RED if k >= 5 else GEST
        c.drawCircle(x, 520, 26, paint(col, ab))
        rrect(c, x - 24, 550, 48, 80, 16, col, ab)
    check_icon(c, 1340, 470, 28, ab, RED, "x")
    pill(c, "fere a universalidade do ATENDIMENTO (pessoas)", W / 2, 720, RED, size=30, a=ab, anchor="center")


def b_q_univ(c, t, C, B):
    ce(c, t, C, "08.e", "08.r", "08.x",
       ["A universalidade da COBERTURA diz respeito às PESSOAS", "alcançadas pela proteção, e a do ATENDIMENTO",
        "se refere aos RISCOS protegidos."], "ERRADO", False, "INVERTEU: cobertura = risco · atendimento = pessoa", "UNIVERSALIDADE")


def b_unif(c, t, C, B):
    head(c, t, B["start"], "INCISO II", "UNIFORMIDADE E EQUIVALÊNCIA · URBANO E RURAL")
    twin(c, t, ep(t, C["09.u"], 0.5), ep(t, C["09.e"], 0.5),
         ("UNIFORMIDADE", BLUE, [("MESMOS TIPOS de benefício", 38, "black", INK), ("aspecto QUALITATIVO", 32, "semibold", GRAY)]),
         ("EQUIVALÊNCIA", AMBER, [("VALORES equivalentes", 38, "black", INK), ("aspecto QUANTITATIVO", 32, "semibold", GRAY)]),
         y=190, h=420)
    am = ep(t, C["10.m"], 0.5)
    if am > 0:
        pill(c, "uniforme = ROUPA IGUAL (o tipo)", 570, 700, BLUE, size=30, a=am, anchor="center")
        pill(c, "equivalência = TROCO (o valor)", 1350, 700, AMBER, size=30, a=ep(t, C["10.e"], 0.4), anchor="center")


def b_equiv(c, t, C, B):
    head(c, t, B["start"], "O PONTO QUE DECIDE", "EQUIVALÊNCIA ≠ IGUALDADE", RED)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    text(c, "EQUIVALÊNCIA", 620, 320, 56, "black", AMBER, aa)
    text(c, "≠", W / 2, 325, 70, "black", INK, aa)
    text(c, "IGUALDADE", 1300, 320, 56, "black", GRAY, aa)
    pill(c, "admite diferença JUSTIFICADA", W / 2, 400, INK, size=28, a=ep(t, C["11.b"], 0.5), anchor="center")
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        for k, (lab, h_, m_, col) in enumerate((("URBANO", 65, 62, GRAY), ("RURAL", 60, 55, PREST))):
            x = 520 + k * 520
            text(c, lab, x, 520, 40, "black", col, ac)
            ad = ep(t, C["11.d"], 0.5) if k == 1 else ac
            text(c, f"homem {h_} · mulher {m_}", x, 590, 36, "bold", INK, ad)
        pill(c, "−5 anos (CF, art. 201, §7º, II)", 1560, 560, PREST, size=26, a=ep(t, C["11.d"], 0.4), anchor="center")
    pill(c, "com IGUALDADE absoluta, seria inconstitucional", W / 2, 740, RED, size=28, a=ep(t, C["11.e"], 0.5), anchor="center")


def b_q_unif(c, t, C, B):
    ce(c, t, C, "12.e", "12.r", "12.x",
       ["Em razão da uniformidade e equivalência, é VEDADO", "à Constituição estabelecer idade reduzida",
        "para a aposentadoria do trabalhador rural."], "ERRADO", False, "a própria CF fixa a idade reduzida", "UNIFORMIDADE E EQUIVALÊNCIA")


def b_sel(c, t, C, B):
    head(c, t, B["start"], "INCISO III", "SELETIVIDADE E DISTRIBUTIVIDADE")
    twin(c, t, ep(t, C["13.s"], 0.5), ep(t, C["13.d"], 0.5),
         ("SELETIVIDADE", BLUE, [("escolhe O QUÊ", 44, "black", INK), ("quais prestações existem", 32, "semibold", GRAY)]),
         ("DISTRIBUTIVIDADE", GEST, [("escolhe PARA QUEM", 44, "black", INK), ("quem mais precisa primeiro", 32, "semibold", GRAY)]),
         y=190, h=420)
    pill(c, "SELECIONA o quê · DISTRIBUI para quem", W / 2, 720, INK, size=34, a=ep(t, C["13.m"], 0.5), anchor="center")


def b_sel_ex(c, t, C, B):
    head(c, t, B["start"], "NA PRÁTICA", "EXEMPLOS QUE CAEM")
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    for k, s in enumerate(("salário-família", "auxílio-reclusão")):
        pill(c, s, 400 + k * 330, 300, PREST, size=34, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "só para dependentes de segurado de BAIXA RENDA", 560, 400, 32, "bold", INK, aa)
    pill(c, "SELETIVIDADE", 560, 470, BLUE, size=30, a=aa, anchor="center")
    ab = ep(t, C["14.b"], 0.5)
    pill(c, "BPC", 1350, 300, AMBER, size=40, a=ab, anchor="center")
    text(c, "idosos e pessoas com deficiência na miséria", 1350, 400, 32, "bold", INK, ab)
    pill(c, "DISTRIBUTIVIDADE", 1350, 470, GEST, size=30, a=ab, anchor="center")
    ac = ep(t, C["14.c"], 0.5)
    if ac > 0:
        arrow(c, 760, 680, 1160, 680, GEST, ac, 7, 24, progress=ac)
        text(c, "quem tem mais", 620, 690, 30, "bold", GRAY, ac)
        text(c, "quem precisa mais", 1320, 690, 30, "bold", GRAY, ac)
        pill(c, "caráter REDISTRIBUTIVO de renda", W / 2, 780, GEST, size=28, a=ac, anchor="center")


def b_tensao(c, t, C, B):
    head(c, t, B["start"], "SÃO INCOMPATÍVEIS?", "UNIVERSALIDADE × SELETIVIDADE", AMBER)
    card(c, *CARD_R)
    au = ep(t, C["15.u"], 0.5)
    text(c, "UNIVERSALIDADE", 560, 330, 50, "black", BLUE, au)
    text(c, "o IDEAL", 560, 400, 40, "bold", INK, au)
    text(c, "proteger todos, contra tudo", 560, 450, 30, "semibold", GRAY, au)
    as_ = ep(t, C["15.s"], 0.5)
    text(c, "SELETIVIDADE", 1360, 330, 50, "black", GEST, as_)
    text(c, "o LIMITE REALISTA", 1360, 400, 40, "bold", INK, as_)
    text(c, "os recursos são finitos", 1360, 450, 30, "semibold", GRAY, as_)
    ar = ep(t, C["15.r"], 0.5)
    result_box(c, "NÃO se contradizem: se COMPATIBILIZAM", W / 2, 640, 40, ar, GREEN)
    pill(c, "a seletividade torna a universalidade VIÁVEL", W / 2, 770, INK, size=28, a=ep(t, C["15.r"] + 2.0, 0.5),
         anchor="center")


def b_q_sel(c, t, C, B):
    head(c, t, C["16.e"] - 1.2, "QUESTÃO DE PROVA", "MÚLTIPLA ESCOLHA")
    stmt_card(c, t, [(C["16.e"], "A restrição do\nsalário-família aos\ndependentes de\nsegurados de baixa\nrenda é manifestação\nde qual objetivo?")],
              size=34)
    alts = ["a) Universalidade", "b) Uniformidade e equivalência", "c) Seletividade e distributividade",
            "d) Irredutibilidade", "e) Diversidade da base"]
    card(c, 880, 150, 900, 690)
    ar = ep(t, C["16.r"], 0.4)
    for k, s in enumerate(alts):
        a = ep(t, C["16.e"] + 1.5 + 0.3 * k, 0.4)
        y = 260 + k * 100
        if k == 2 and ar > 0:
            rrect(c, 910, y - 50, 840, 80, 16, GREEN, 0.15 * ar)
            check_icon(c, 1710, y - 10, 24, ar, GREEN)
        text(c, s, 940, y, 36, "black" if k == 2 and ar > 0 else "semibold", INK if not (k == 2 and ar > 0) else GREEN,
             a * (1 - 0.5 * ar if k != 2 else 1), align="left")
    pill(c, "selecionou a prestação e distribuiu a quem precisa", 1330, 790, GREEN, size=24, a=ep(t, C["16.x"], 0.5),
         anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("16b.p1", "16b.r1", "a SELETIVIDADE define A QUEM serão prestados os benefícios", False, "isso é DISTRIBUTIVIDADE"),
             ("16b.p2", "16b.r2", "o princípio impõe IGUALDADE de valores entre urbanos e rurais", False, "é EQUIVALÊNCIA"),
             ("16b.p3", "16b.r3", "a universalidade do ATENDIMENTO tem caráter SUBJETIVO", True, "alcança as PESSOAS")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 32, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "INCISOS I, II E III", GREEN)
    rows = [("17.a", "I", "UNIVERSALIDADE", "cobertura = RISCO · atendimento = PESSOA · não é absoluta"),
            ("17.b", "II", "UNIFORMIDADE E EQUIVALÊNCIA", "uniformidade = TIPO · equivalência = VALOR (≠ igualdade)"),
            ("17.c", "III", "SELETIVIDADE E DISTRIBUTIVIDADE", "seleciona O QUÊ · distribui PARA QUEM")]
    card(c, 200, 180, 1520, 640)
    for k, (cue, rom, nome, desc) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 300 + k * 180 + dy
        inciso_tag(c, rom, 260, y, PREST, a, 40)
        text(c, nome, 420, y + 14, 42, "black", INK, a, align="left")
        text(c, desc, 420, y + 70, 30, "semibold", GRAY, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["18.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Princípios — parte 2", W / 2, 430, 64, "black", INK, a)
        for k, (rom, nome, col) in enumerate(INC[3:]):
            pill(c, f"{rom} · {nome}", W / 2, 540 + k * 70, col, size=26, a=ep(t, B["start"] + 1 + 0.6 * k, 0.4) * a,
                 anchor="center")
    cta(c, t, C["18.like"], C["18.sub"], C["18.bell"], C["18.com"], C["18.bye"], "Qual desses você mais confunde?")


BLOCKS = dict(hook=b_hook, lista=b_lista, mnemonico=b_mnemonico, nome=b_nome, corte=b_corte, univ=b_univ,
              absoluta=b_absoluta, contra=b_contra, q_univ=b_q_univ, unif=b_unif, equiv=b_equiv, q_unif=b_q_unif,
              sel=b_sel, sel_ex=b_sel_ex, tensao=b_tensao, q_sel=b_q_sel, pegadinhas=b_pegadinhas, resumo=b_resumo,
              cta=b_cta)
