"""Visual do vídeo Seguridade 001 — Conceito e tripé (tema 'seguridade': claro com destaque verde-petróleo)."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_001_conceito_e_tripe.mp4"
CARD_R = (140, 150, 1640, 690)

SAUDE = "#E5484D"
PREV = "#0F766E"
ASSIST = "#E8A317"
PILARES = [("SAÚDE", SAUDE, ""), ("PREVIDÊNCIA", PREV, ""), ("ASSISTÊNCIA", ASSIST, "")]


def pillar(c, x, y, w, h, nome, col, a, lines=(), sub=None, glyph=None):
    if a <= 0:
        return
    card(c, x, y, w, h, a)
    rrect(c, x, y, w, 14, 7, col, a)
    if glyph:
        icon(c, glyph, x + w / 2, y + 90, 70, col, a)
    text(c, nome, x + w / 2, y + (180 if glyph else 80), 40, "black", col, a)
    for k, (s, peso, cc) in enumerate(lines):
        text(c, s, x + w / 2, y + (250 if glyph else 150) + k * 52, 32, peso, cc or INK, a)


def umbrella(c, cx, cy, r, a, col=None):
    col = BLUE if col is None else col
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), 180, 180, False)
    n = 4
    for k in range(n, 0, -1):
        x1 = cx - r + 2 * r * k / n
        x0 = cx - r + 2 * r * (k - 1) / n
        p.quadTo((x0 + x1) / 2, cy - r * 0.12, x0, cy)
    p.close()
    c.drawPath(p, paint(col, a))
    line(c, cx, cy, cx, cy + r * 0.9, INK, a, 8)
    c.drawArc(skia.Rect.MakeLTRB(cx, cy + r * 0.8, cx + r * 0.24, cy + r * 1.04), 0, 180, False, paint(INK, a, stroke=8))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 1", W / 2, 230, BLUE, size=30, a=a0, anchor="center")
    text(c, "O que é", W / 2, 380, 70, "bold", INK2, a0)
    text(c, "SEGURIDADE SOCIAL?", W / 2, 480, 96, "black", INK, a0)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        y = 600
        s1 = "“...de iniciativa dos Poderes Públicos "
        w1 = text_w(s1, "semibold", 40); w2 = text_w("e da sociedade", "black", 40)
        x1 = W / 2 - (w1 + w2) / 2
        text(c, s1, x1, y + 30, 40, "semibold", INK, ab, align="left")
        tx = x1 + w1 + w2 / 2
        text(c, "e da sociedade", tx, y + 30, 40, "black", RED, ab)
        strike(c, tx - 145, y + 16, tx + 145, y + 16, ab, progress=ep(t, C["01.b"] + 1.2, 0.5))
        pill(c, "UMA palavra muda tudo", W / 2, y + 120, RED, size=28, a=ep(t, C["01.b"] + 1.6, 0.4), anchor="center")
    ac = ep(t, C["01.c"], 0.5)
    for k, s in enumerate(("conceito", "o tripé", "pegadinhas")):
        pill(c, s, W / 2 + (k - 1) * 300, 840, BLUE, size=28, a=ep(t, C["01.c"] + 0.5 * k, 0.4), anchor="center")


def b_riscos(c, t, C, B):
    head(c, t, B["start"], "TRÊS RISCOS", "QUE PODEM DERRUBAR UMA PESSOA")
    items = [("02.r1", "", "ADOECER", "cuidar da saúde", SAUDE), ("02.r2", "", "PERDER A RENDA", "doença, idade, morte", PREV),
             ("02.r3", "", "ESTAR NA MISÉRIA", "garantir o mínimo", ASSIST)]
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, g, tit, sub, col) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 220 + dy, cw, 480, a)
        badge_num(c, k + 1, x + 60, 280 + dy, a, 30, bg=col)
        icon(c, g, x + cw / 2, 380 + dy, 110, col, a)
        text(c, tit, x + cw / 2, 540 + dy, 42, "black", INK, a)
        text(c, sub, x + cw / 2, 600 + dy, 30, "semibold", GRAY, a)


def b_guarda(c, t, C, B):
    head(c, t, B["start"], "O GUARDA-CHUVA", "SEGURIDADE SOCIAL")
    ag = ep(t, C["03.g"], 0.6)
    umbrella(c, W / 2, 440, 280, ag)
    text(c, "SEGURIDADE SOCIAL", W / 2, 380, 42, "black", "#FFFFFF", ag)
    cw, gap = 420, 60
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, (nome, col, g)) in enumerate(zip(("03.s", "03.p", "03.a"), PILARES)):
        a, dy = rise(t, C[cue])
        y = 560 + dy if ag > 0 else 300 + dy
        pillar(c, x0 + k * (cw + gap), y, cw, 230, nome, col, a, glyph=g)
    af = ep(t, C["03.f"], 0.5)
    if af > 0:
        pill(c, "GÊNERO", W / 2 + 400, 330, BLUE, size=28, a=af, anchor="center")
        pill(c, "ESPÉCIES", W / 2 - 660, 530, INK, size=28, a=af, anchor="center", bounds=(0, 1920))


def b_conceito(c, t, C, B):
    head(c, t, B["start"], "O CONCEITO", "CF, ART. 194, CAPUT")
    card(c, 200, 190, 1520, 640)
    pill(c, "Art. 194", 240, 240, BLUE, size=26, bounds=(0, 1920))
    lines = [("04.l1", "A seguridade social compreende um", "conjunto integrado de ações", PURPLE),
             ("04.l2", "de iniciativa dos", "Poderes Públicos e da sociedade,", RED),
             ("04.l3", "destinadas a assegurar os direitos relativos à", "saúde, à previdência e à assistência social.", BLUE)]
    for k, (cue, plain, key, col) in enumerate(lines):
        a, dy = rise(t, C[cue])
        y = 360 + k * 150 + dy
        text(c, plain, 280, y, 38, "medium", INK2, a, align="left")
        text(c, key, 280, y + 58, 46, "black", col, a, align="left")


def b_nucleos(c, t, C, B):
    head(c, t, B["start"], "3 NÚCLEOS", "QUE A BANCA ATACA", RED)
    items = [("05.n1", "conjunto integrado\nde ações", "não é órgão\nnem o INSS", PURPLE),
             ("05.n2", "Poderes Públicos\nE da sociedade", "não é exclusivo\ndo Estado", RED),
             ("05.n3", "saúde, previdência\ne assistência", "educação e\nmoradia NÃO", BLUE)]
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, s1, s2, col) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 210 + dy, cw, 520, a)
        badge_num(c, k + 1, x + cw / 2, 290 + dy, a, 40, bg=col)
        for j, ln in enumerate(s1.split("\n")):
            text(c, ln, x + cw / 2, 410 + dy + j * 52, 40, "black", col, a)
        for j, ln in enumerate(s2.split("\n")):
            text(c, ln, x + cw / 2, 590 + dy + j * 44, 32, "bold", GRAY, a)


def b_lei(c, t, C, B):
    head(c, t, B["start"], "BÔNUS", "A LEI 8.212/1991 REPETE O CONCEITO")
    for k, (lab, ref, col) in enumerate((("Constituição", "art. 194, caput", BLUE), ("Lei 8.212/1991", "art. 1º, caput", PURPLE))):
        a, dy = rise(t, B["start"] + 0.5 + k * 1.2)
        x = 300 + k * 700
        card(c, x, 260 + dy, 620, 300, a)
        text(c, lab, x + 310, 380 + dy, 48, "black", col, a)
        text(c, ref, x + 310, 450 + dy, 34, "semibold", GRAY, a)
    text(c, "=", W / 2, 440, 90, "black", INK, ep(t, B["start"] + 2.0, 0.4))
    pill(c, "uma decoreba, DUAS fontes", W / 2, 690, GREEN, size=34, a=ep(t, C["06.a"], 0.5), anchor="center")


def b_organizar(c, t, C, B):
    head(c, t, B["start"], "QUEM FAZ O QUÊ", "ORGANIZAR × PARTICIPAR")
    card(c, *CARD_R)
    for k, (cue, verbo, quem, col) in enumerate((("07.f", "FINANCIA", "Poder Público + sociedade", GREEN),
                                                  ("07.p", "PARTICIPA da gestão", "Poder Público + sociedade", GREEN),
                                                  ("07.o", "ORGANIZA", "SÓ o Poder Público", RED))):
        a, dy = rise(t, C[cue])
        y = 300 + k * 130 + dy
        text(c, verbo, 300, y, 50, "black", col, a, align="left")
        pill(c, quem, 1620, y - 16, col, size=32, a=a, anchor="right", bounds=(0, 1920))
    afr = ep(t, C["07.fr"], 0.5)
    if afr > 0:
        rrect(c, 300, 690, 1320, 100, 22, BLUE, 0.1 * afr)
        text_mid(c, "O Poder Público ORGANIZA; a sociedade PARTICIPA e FINANCIA", W / 2, 740, 34, "black", BLUE, afr)


def b_topografia(c, t, C, B):
    head(c, t, B["start"], "ONDE ESTÁ", "NA CONSTITUIÇÃO")
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    rrect(c, 300, 250, 1320, 110, 18, BLUE, aa * 0.12)
    text_mid(c, "TÍTULO VIII — DA ORDEM SOCIAL", W / 2, 305, 48, "black", BLUE, aa)
    ab = ep(t, C["08.b"], 0.5)
    rrect(c, 400, 390, 1120, 90, 16, BLUE, ab * 0.08)
    text_mid(c, "Capítulo II — Da Seguridade Social · arts. 194 a 204", W / 2, 435, 36, "bold", INK, ab)
    secs = [("194–195", "disposições gerais", BLUE), ("196–200", "Saúde", SAUDE), ("201–202", "Previdência", PREV),
            ("203–204", "Assistência", ASSIST)]
    for k, (arts, nome, col) in enumerate(secs):
        a = ep(t, C["08.b"] + 0.4 + 0.3 * k, 0.4)
        x = 420 + k * 280
        rrect(c, x, 510, 250, 110, 14, col, a * 0.15)
        text(c, arts, x + 125, 555, 32, "black", col, a)
        text(c, nome, x + 125, 600, 26, "bold", INK, a)
    ax = ep(t, C["08.x"], 0.5)
    if ax > 0:
        text(c, "Ordem Econômica", W / 2 - 40, 730, 40, "bold", RED, ax)
        strike(c, W / 2 - 220, 716, W / 2 + 140, 716, ax)
        mark(c, False, W / 2 + 200, 716, ax, 26)


def b_tripe(c, t, C, B):
    head(c, t, B["start"], "O TRIPÉ", "QUEM TEM DIREITO A CADA UM")
    cw, gap = 500, 40
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    data = [("09.s", ("PARA TODOS", "black", None), ("não exige contribuição", "semibold", GRAY), ("SUS", "black", SAUDE)),
            ("09.p", ("QUEM CONTRIBUI", "black", None), ("contributiva e filiação\nobrigatória", "semibold", GRAY), ("INSS", "black", PREV)),
            ("09.a", ("QUEM NECESSITAR", "black", None), ("independe de\ncontribuição", "semibold", GRAY), ("LOAS / BPC", "black", ASSIST))]
    for k, ((nome, col, g), (cue, l1, l2, l3)) in enumerate(zip(PILARES, data)):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        y = 200 + dy
        card(c, x, y, cw, 600, a)
        rrect(c, x, y, cw, 14, 7, col, a)
        icon(c, g, x + cw / 2, y + 100, 80, col, a)
        text(c, nome, x + cw / 2, y + 210, 44, "black", col, a)
        text(c, l1[0], x + cw / 2, y + 300, 36, "black", INK, a)
        for j, ln in enumerate(l2[0].split("\n")):
            text(c, ln, x + cw / 2, y + 370 + j * 40, 30, "semibold", GRAY, a)
        pill(c, l3[0], x + cw / 2, y + 520, col, size=30, a=a, anchor="center", bounds=(0, 1920))


def b_spa(c, t, C, B):
    head(c, t, B["start"], "MEMORIZE", "A SEGURIDADE É UM SPA", GREEN)
    card(c, *CARD_R)
    for k, (cue, letra, nome, col) in enumerate((("10.s", "S", "aúde", SAUDE), ("10.p", "P", "revidência", PREV), ("10.a", "A", "ssistência", ASSIST))):
        a, dy = rise(t, C[cue])
        x = 380 + k * 450
        text(c, letra, x, 470 + dy, 220, "black", col, a)
        text(c, letra + nome, x, 560 + dy, 38, "bold", INK, a)
    ap = ep(t, C["10.pg"], 0.5)
    if ap > 0:
        pill(c, "R$ PAGO", 830, 250, PREV, size=34, a=ap, anchor="center")
        pill(c, "grátis", 380, 250, GRAY, size=30, a=ap, anchor="center")
        pill(c, "grátis", 1280, 250, GRAY, size=30, a=ap, anchor="center")
        pill(c, "só a PREVIDÊNCIA exige contribuição", W / 2, 720, PREV, size=32, a=ap, anchor="center")


def b_ovelha(c, t, C, B):
    head(c, t, B["start"], "A OVELHA DIFERENTE", "PREVIDÊNCIA")
    card(c, 260, 180, 1400, 640)
    cols_x = [900, 1150, 1400]
    for (nome, col, _), x in zip(PILARES, cols_x):
        text(c, nome, x, 270, 28, "black", col)
    rows = [("exige contribuição?", (False, True, False)), ("para todos / quem necessita?", (True, False, True)),
            ("exige filiação?", (False, True, False))]
    aa = ep(t, C["11.a"], 0.5)
    for j, (q, vals) in enumerate(rows):
        y = 380 + j * 120
        text(c, q, 320, y + 12, 36, "bold", INK, aa, align="left")
        for k, (v, x) in enumerate(zip(vals, cols_x)):
            a = aa if k != 1 else ep(t, C["11.b"], 0.4)
            check_icon(c, x, y, 26, a, GREEN if v else RED, "check" if v else "x")
    ab = ep(t, C["11.b"], 0.5)
    rrect(c, 1035, 300, 230, 380, 18, PREV, 0.1 * ab)
    pill(c, "duas contra uma", 1150, 720, PREV, size=28, a=ab, anchor="center")
    pill(c, "regra 'para toda a Seguridade'? TESTE NA PREVIDÊNCIA", W / 2, 790, RED, size=26, a=ep(t, C["11.c"], 0.5),
         anchor="center")


def b_genero(c, t, C, B):
    head(c, t, B["start"], "A CONFUSÃO Nº 1", "SEGURIDADE ≠ PREVIDÊNCIA", RED)
    card(c, *CARD_R)
    cx, cy = 700, 480
    aa = ep(t, C["12.a"], 0.5)
    c.drawCircle(cx, cy, 270, paint(BLUE, 0.1 * aa)); c.drawCircle(cx, cy, 270, paint(BLUE, aa, stroke=5))
    text(c, "SEGURIDADE", cx, cy - 180, 40, "black", BLUE, aa)
    c.drawCircle(cx + 40, cy + 50, 140, paint(PREV, 0.25 * aa)); c.drawCircle(cx + 40, cy + 50, 140, paint(PREV, aa, stroke=5))
    text(c, "PREVIDÊNCIA", cx + 40, cy + 64, 34, "black", PREV, aa)
    text(c, "sinônimos", 1300, 300, 46, "black", RED, aa)
    strike(c, 1180, 284, 1420, 284, aa)
    mark(c, False, 1470, 284, aa, 26)
    for k, (cue, s, ok) in enumerate((("12.b", "Toda Previdência é Seguridade", True), ("12.c", "Nem toda Seguridade é Previdência", True))):
        a, dy = rise(t, C[cue])
        y = 430 + k * 110 + dy
        mark(c, ok, 1060, y - 12, a, 24)
        text(c, s, 1100, y, 36, "bold", INK, a, align="left")
    pill(c, "a Previdência é só uma PARTE do todo", 1340, 700, PREV, size=26, a=ep(t, C["12.d"], 0.5), anchor="center")


def b_caso(c, t, C, B):
    head(c, t, B["start"], "CASO PRÁTICO", "O AMBULANTE MARCELO")
    card(c, 140, 150, 560, 690)
    am = ep(t, C["13.a"], 0.5)
    c.drawCircle(420, 330, 60, paint(INK2, am))
    rrect(c, 340, 400, 160, 220, 50, INK2, am)
    text(c, "Marcelo", 420, 680, 40, "black", INK, am)
    text(c, "nunca contribuiu", 420, 730, 30, "semibold", RED, am)
    ab = ep(t, C["13.b"], 0.5)
    pill(c, "quebrou o braço", 420, 790, INK, size=24, a=ab, anchor="center")
    rows = [("13.q1", "13.r1", "Atendimento no SUS?", "SIM", "saúde é universal", True, SAUDE),
            ("13.q2", "13.r2", "Auxílio do INSS?", "NÃO", "previdência é contributiva", False, PREV),
            ("14.q3", "14.r3", "BPC (se miserável e impedido)?", "PODE", "assistência independe de contribuição", True, ASSIST)]
    for k, (cq, cr, q, r, why, ok, col) in enumerate(rows):
        aq, dy = rise(t, C[cq])
        if aq <= 0:
            continue
        y = 170 + k * 210 + dy
        card(c, 740, y, 1040, 190, aq)
        rrect(c, 740, y, 12, 190, 6, col, aq)
        text(c, q, 790, y + 70, 36, "bold", INK, aq, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, r, 1740, y + 58, GREEN if ok else RED, size=34, a=ar, anchor="right", bounds=(0, 1920))
        text(c, why, 790, y + 135, 28, "semibold", GRAY, ar, align="left")
    af = ep(t, C["14.f"], 0.5)
    pill(c, "UM fato, TRÊS respostas", 420, 230, RED, size=28, a=af, anchor="center")


def _pegadinhas(c, t, C, items):
    card(c, 200, 170, 1520, 680)
    step = 600 / len(items)
    for k, (cp, cr, frase, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 270 + k * step + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "ERRADO", 1660, y - 12, RED, size=26, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 50, 30, "bold", GREEN, ar, align="left")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    _pegadinhas(c, t, C, [("15.p1", "15.r1", "...iniciativa EXCLUSIVA dos Poderes Públicos", "dos Poderes Públicos E da sociedade"),
                          ("15.p2", "15.r2", "compete ao Poder Público E À SOCIEDADE organizar", "organizar é SÓ do Poder Público")])


def b_pegadinhas2(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    _pegadinhas(c, t, C, [("16.p3", "16.r3", "saúde, previdência, assistência E EDUCAÇÃO", "educação não integra a Seguridade"),
                          ("16.p4", "16.r4", "a assistência exige contribuição prévia", "independe de contribuição"),
                          ("16.p5", "16.r5", "está no Título da Ordem ECONÔMICA", "está na ORDEM SOCIAL")])


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO DE PROVA", "CERTO OU ERRADO?", BLUE)
    card(c, 200, 180, 1520, 560)
    pill(c, "C / E", 240, 230, BLUE, size=26, bounds=(0, 1920))
    ae = ep(t, C["17.e"], 0.5)
    lines = ["A seguridade social compreende um conjunto integrado", "de ações de iniciativa dos Poderes Públicos, ___",
             "destinadas a assegurar os direitos relativos à saúde,", "à previdência e à assistência social."]
    for k, ln in enumerate(lines):
        text(c, ln, 280, 330 + k * 66, 40, "semibold", INK, ep(t, C["17.e"] + 0.8 * k, 0.4), align="left")
    ar = ep(t, C["17.r"], 0.4)
    result_box(c, "ERRADO", 1500, 800, 50, ar, RED)
    ax = ep(t, C["17.x"], 0.5)
    pill(c, "faltou: “e da sociedade”", 960, 640, RED, size=32, a=ax, anchor="center")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 170, 1520, 680)
    rows = [("18.a", "Seguridade = GÊNERO · saúde, previdência e assistência = ESPÉCIES"),
            ("18.b", "conjunto integrado de ações dos Poderes Públicos E da sociedade"),
            ("18.c", "ORGANIZAR: só o Poder Público"),
            ("18.d", "Título VIII (Ordem Social), arts. 194 a 204"),
            ("18.e", "só a PREVIDÊNCIA é contributiva")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 290 + k * 115 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 36, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["19.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 360, BLUE, size=30, a=a, anchor="center")
        text(c, "Os princípios da Seguridade Social", W / 2, 490, 60, "black", INK, a)
        text(c, "art. 194, parágrafo único", W / 2, 560, 36, "semibold", GRAY, a)
    cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"], "Qual pegadinha você já caiu?")


BLOCKS = dict(hook=b_hook, riscos=b_riscos, guarda=b_guarda, conceito=b_conceito, nucleos=b_nucleos, lei=b_lei,
              organizar=b_organizar, topografia=b_topografia, tripe=b_tripe, spa=b_spa, ovelha=b_ovelha, genero=b_genero,
              caso=b_caso, pegadinhas=b_pegadinhas, pegadinhas2=b_pegadinhas2, questao=b_questao, resumo=b_resumo, cta=b_cta)
