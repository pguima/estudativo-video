"""Visual do vídeo Seguridade 004 — Financiamento: as fontes do art. 195. Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_004_financiamento_fontes.mp4"
CARD_R = (140, 150, 1640, 690)

PREST = "#0F766E"
CUST = "#E8A317"
GEST = "#4F46E5"
FONTES = [("I", "EMPREGADOR", "e empresa", "E"), ("II", "TRABALHADOR", "e demais segurados", "T"),
          ("III", "CONCURSOS", "de prognósticos", "C"), ("IV", "IMPORTADOR", "de bens ou serviços", "I")]


def inciso_tag(c, roman, x, y, col, a, size=40):
    w = text_w(roman, "black", size) + 40
    rrect(c, x, y - size * 0.75, w, size * 1.5, 14, col, a)
    text_mid(c, roman, x + w / 2, y, size, "black", "#FFFFFF", a)
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


def cofre(c, cx, cy, a, label="SEGURIDADE SOCIAL"):
    rrect(c, cx - 260, cy - 120, 520, 240, 26, PREST, a, shadow=True)
    c.drawCircle(cx + 195, cy, 34, paint("#FFFFFF", a * 0.25))
    c.drawCircle(cx + 195, cy, 34, paint("#FFFFFF", a, stroke=5))
    text_mid(c, label, cx - 45, cy, 32, "black", "#FFFFFF", a)


def coin_flow(c, t, x0, y0, x1, y1, a, col, n=4, speed=0.6):
    if a <= 0:
        return
    for k in range(n):
        u = ((t * speed + k / n) % 1.0)
        x, y = lerp(x0, x1, u), lerp(y0, y1, u)
        c.drawCircle(x, y, 16, paint(col, a * (0.4 + 0.6 * math.sin(math.pi * u))))
        text_mid(c, "$", x, y, 18, "black", "#FFFFFF", a * (0.4 + 0.6 * math.sin(math.pi * u)))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 4", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    for k, s in enumerate(("aposentadorias", "SUS", "BPC")):
        pill(c, s, 640 + k * 320, 320, INK, size=34, a=ep(t, B["start"] + 0.6 + 0.6 * k, 0.4), anchor="center")
    aa = ep(t, C["01.a"], 0.5)
    text(c, "DE ONDE VEM O DINHEIRO?", W / 2, 500, 90, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    result_box(c, "CF, art. 195", W / 2, 650, 56, ab, PREST)
    pill(c, "a base de todo o CUSTEIO do edital", W / 2, 790, CUST, size=30, a=ep(t, C["01.c"], 0.5), anchor="center")


def b_toda(c, t, C, B):
    head(c, t, B["start"], "FINANCIADA POR", "TODA A SOCIEDADE")
    card(c, *CARD_R)
    cofre(c, W / 2, 640, 1)
    ai = ep(t, C["02.i"], 0.5)
    if ai > 0:
        rrect(c, 220, 220, 620, 230, 22, BLUE, 0.08 * ai)
        text(c, "INDIRETA", 530, 290, 46, "black", BLUE, ai)
        text(c, "orçamentos públicos", 530, 350, 32, "bold", INK, ai)
        text(c, "União · Estados · DF · Municípios", 530, 400, 28, "semibold", GRAY, ai)
        coin_flow(c, t, 600, 460, 820, 580, ai, BLUE)
    ad = ep(t, C["02.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 220, 620, 230, 22, CUST, 0.1 * ad)
        text(c, "DIRETA", 1390, 290, 46, "black", CUST, ad)
        text(c, "contribuições sociais", 1390, 350, 32, "bold", INK, ad)
        text(c, "pagas especificamente para a seguridade", 1390, 400, 26, "semibold", GRAY, ad)
        coin_flow(c, t, 1320, 460, 1100, 580, ad, CUST)


def b_solid(c, t, C, B):
    head(c, t, B["start"], "SOLIDARIEDADE", "QUEM PAGA NÃO É QUEM RECEBE")
    card(c, *CARD_R)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "quem PAGA não é necessariamente quem RECEBE", W / 2, 290, 44, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    for k, s in enumerate(("União", "Estados", "Distrito Federal", "Municípios")):
        a = ep(t, C["03.b"] + 0.4 * k, 0.4)
        x = 380 + k * 390
        card(c, x - 170, 400, 340, 140, a)
        text_mid(c, s, x, 470, 36, "black", PREST if k < 3 else RED, a)
    ac = ep(t, C["03.c"], 0.5)
    pill(c, "a banca tira os MUNICÍPIOS ou diz “somente a União”", W / 2, 680, RED, size=28, a=ac, anchor="center")


def b_etci(c, t, C, B):
    head(c, t, B["start"], "AS CONTRIBUIÇÕES SOCIAIS", "4 FONTES · INCISOS I A IV", CUST)
    cw, gap = 380, 30
    x0 = W / 2 - (4 * cw + 3 * gap) / 2
    am = ep(t, C["04.m"], 0.5)
    for k, (rom, nome, sub, letra) in enumerate(FONTES):
        a, dy = rise(t, C[f"04.i{k + 1}"])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 200 + dy, cw, 470, a)
        inciso_tag(c, rom, x + 30, 260 + dy, CUST, a, 34)
        text(c, letra, x + cw / 2, 450 + dy, 150, "black", mix(LIGHT, CUST, am), a)
        text(c, nome, x + cw / 2, 560 + dy, 38, "black", INK, a)
        text(c, sub, x + cw / 2, 610 + dy, 28, "semibold", GRAY, a)
    pill(c, "E · T · C · I", W / 2, 760, CUST, size=40, a=am, anchor="center")


def b_emp(c, t, C, B):
    head(c, t, B["start"], "INCISO I", "EMPREGADOR E EMPRESA: 3 BASES", CUST)
    card(c, *CARD_R)
    bases = [("05.a", "F", "OLHA de salários", "contribuição patronal"), ("05.b", "R", "ECEITA ou faturamento", "COFINS"),
             ("05.c", "L", "UCRO", "CSLL")]
    ax = ep(t, C["05.x"], 0.5)
    for k, (cue, l, rest, trib) in enumerate(bases):
        a, dy = rise(t, C[cue])
        y = 300 + k * 140 + dy
        text(c, l, 330, y + 20, 100, "black", CUST, a)
        text(c, rest, 410, y + 10, 48, "black", INK, a, align="left")
        pill(c, trib, 1560, y - 14, PREST, size=30, a=ax * a, anchor="right", bounds=(0, 1920))
    am = ep(t, C["05.m"], 0.5)
    if am > 0:
        # farol
        bx, by = 1080, 650
        rrect(c, bx - 18, by, 36, 120, 6, RED, am)
        rrect(c, bx - 28, by - 26, 56, 30, 8, INK, am)
        for k in range(3):
            p = skia.Path(); p.moveTo(bx, by - 12); p.lineTo(bx + 160, by - 60 + k * 10); p.lineTo(bx + 160, by + 20 - k * 10); p.close()
            c.drawPath(p, paint(AMBER, am * 0.25))
        pill(c, "F · R · L = FAROL", bx + 380, by + 50, CUST, size=30, a=am, anchor="center")


def b_folha(c, t, C, B):
    head(c, t, B["start"], "PONTO DE OURO", "A FOLHA VAI ALÉM DOS EMPREGADOS", RED)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    text(c, "pagamento a PESSOA FÍSICA que presta serviço", W / 2, 280, 42, "black", INK, aa)
    text(c, "MESMO SEM VÍNCULO de emprego", W / 2, 340, 38, "bold", PREST, aa)
    ab = ep(t, C["06.b"], 0.5)
    for k, s in enumerate(("empregados", "autônomos", "avulsos")):
        a = ep(t, C["06.b"] + 0.5 * k, 0.4) if k else max(ab, aa)
        x = 450 + k * 300
        card(c, x - 130, 420, 260, 170, a)
        text_mid(c, s, x, 485, 32, "black", INK, a)
        check_icon(c, x, 550, 22, a, GREEN)
    ac = ep(t, C["06.c"], 0.5)
    card(c, 1300, 420, 300, 170, ac)
    text_mid(c, "pessoa JURÍDICA", 1450, 485, 30, "black", INK, ac)
    check_icon(c, 1450, 550, 22, ac, RED, "x")
    pill(c, "não incide sobre pagamento a PJ", W / 2, 720, RED, size=28, a=ac, anchor="center")


def b_q_folha(c, t, C, B):
    ce(c, t, C, "07.e", "07.r", "07.x", ["A contribuição patronal incide APENAS", "sobre a folha de salários dos EMPREGADOS."],
       "ERRADO", False, "alcança qualquer PESSOA FÍSICA que preste serviço, mesmo sem vínculo", "INCISO I", size=42)


def b_trab(c, t, C, B):
    head(c, t, B["start"], "INCISO II", "TRABALHADOR E DEMAIS SEGURADOS", CUST)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "1. ALÍQUOTAS PROGRESSIVAS", 560, 270, 38, "black", CUST, aa)
        for k in range(4):
            h = 60 + 45 * k
            rrect(c, 380 + k * 100, 520 - h, 70, h, 8, CUST, aa * (0.5 + 0.15 * k))
        text(c, "ganha mais → % maior", 560, 580, 30, "bold", INK, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "2. NÃO INCIDE", 1360, 270, 38, "black", PREST, ab)
        for k, s in enumerate(("aposentadoria", "pensão")):
            pill(c, s, 1220 + k * 280, 380, PREST, size=32, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "concedidas pelo RGPS", 1360, 470, 34, "bold", INK, ab)
        check_icon(c, 1360, 540, 26, ab, GREEN)
    ac = ep(t, C["09.c"], 0.5)
    if ac > 0:
        rrect(c, 960, 610, 800, 120, 20, RED, 0.08 * ac)
        text(c, "RPPS (servidores): NÃO se estende automaticamente", 1360, 665, 28, "black", RED, ac)
        text(c, "têm regras próprias", 1360, 705, 26, "semibold", GRAY, ep(t, C["09.d"], 0.4))
    pill(c, "EC 103/2019", W / 2, 790, INK, size=26, a=ep(t, B["start"] + 2.0, 0.5), anchor="center")


def b_loteria(c, t, C, B):
    head(c, t, B["start"], "INCISOS III E IV", "LOTERIAS E IMPORTADOR", CUST)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.3, 0.5)
    text(c, "CONCURSOS DE PROGNÓSTICOS", 560, 260, 34, "black", CUST, a0)
    for k, n in enumerate((7, 13, 22, 35, 41, 58)):
        x = 330 + (k % 3) * 160
        y = 340 + (k // 3) * 110
        c.drawCircle(x, y, 44, paint(CUST, a0 * 0.18))
        c.drawCircle(x, y, 44, paint(CUST, a0, stroke=4))
        text_mid(c, str(n), x, y, 36, "black", INK, a0)
    aa = ep(t, C["10.a"], 0.5)
    pill(c, "RECEITA do concurso", 420, 600, GREEN, size=30, a=aa, anchor="center")
    check_icon(c, 640, 600, 22, aa, GREEN)
    ab = ep(t, C["10.b"], 0.5)
    pill(c, "PRÊMIO do apostador", 420, 680, RED, size=30, a=ab, anchor="center")
    check_icon(c, 640, 680, 22, ab, RED, "x")
    ac = ep(t, C["10.c"], 0.5)
    if ac > 0:
        text(c, "IMPORTADOR", 1360, 300, 44, "black", CUST, ac)
        rrect(c, 1170, 380, 380, 200, 16, "#94A3B8", ac)
        for k in range(4):
            line(c, 1170 + 76 * (k + 1), 380, 1170 + 76 * (k + 1), 580, "#64748B", ac, 4)
        text(c, "bens ou serviços do exterior", 1360, 640, 30, "bold", INK, ac)


def b_lei11(c, t, C, B):
    head(c, t, B["start"], "LEI 8.212/1991 · ART. 11", "AS RECEITAS DA SEGURIDADE (ÂMBITO FEDERAL)", PREST)
    cw, gap = 480, 50
    x0 = W / 2 - (3 * cw + 2 * gap) / 2
    for k, (cue, s, col) in enumerate((("11.r1", "receitas da\nUNIÃO", BLUE), ("11.r2", "receitas das\nCONTRIBUIÇÕES\nSOCIAIS", CUST),
                                        ("11.r3", "receitas de\nOUTRAS FONTES", GEST))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = x0 + k * (cw + gap)
        card(c, x, 230 + dy, cw, 420, a)
        badge_num(c, ["I", "II", "III"][k], x + cw / 2, 320 + dy, a, 40, bg=col)
        for j, ln in enumerate(s.split("\n")):
            text(c, ln, x + cw / 2, 450 + dy + j * 54, 42, "black", INK, a)


def b_lei11b(c, t, C, B):
    head(c, t, B["start"], "AS 5 CONTRIBUIÇÕES SOCIAIS", "LEI 8.212, ART. 11, PARÁGRAFO ÚNICO", PREST)
    card(c, 260, 170, 1400, 680)
    rows = [("12.a1", "a", "das EMPRESAS, sobre a remuneração"), ("12.a2", "b", "dos EMPREGADORES DOMÉSTICOS"),
            ("12.a3", "c", "dos TRABALHADORES"), ("12.a4", "d", "das EMPRESAS, sobre faturamento e lucro"),
            ("12.a5", "e", "sobre CONCURSOS DE PROGNÓSTICOS")]
    ax = ep(t, C["12.x"], 0.5)
    for k, (cue, l, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 270 + k * 100 + dy
        if k == 1 and ax > 0:
            rrect(c, 300, y - 58, 1320, 90, 16, RED, 0.12 * ax)
            pill(c, "só na LEI (a CF não destaca)", 1600, y - 14, RED, size=24, a=ax, anchor="right", bounds=(0, 1920))
        badge_num(c, l, 360, y - 14, a, 28, bg=PREST)
        text(c, s, 420, y, 40, "bold", INK, a, align="left")


def b_uniao(c, t, C, B):
    head(c, t, B["start"], "O PAPEL DA UNIÃO", "A GARANTIDORA DO SISTEMA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    text(c, "recursos adicionais do Orçamento Fiscal", W / 2, 290, 42, "black", INK, aa)
    text(c, "fixados na LEI ORÇAMENTÁRIA ANUAL", W / 2, 350, 34, "bold", BLUE, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        # rede de proteção
        cofre(c, W / 2, 500, ab, "BENEFÍCIOS")
        p = skia.Path(); p.moveTo(500, 640); p.quadTo(W / 2, 760, 1420, 640)
        c.drawPath(p, paint(BLUE, ab, stroke=10, cap_round=True))
        text(c, "UNIÃO", W / 2, 790, 40, "black", BLUE, ab)
    ac = ep(t, C["13.c"], 0.5)
    pill(c, "faltou dinheiro? a UNIÃO cobre", 1500, 450, BLUE, size=28, a=ac, anchor="center")


def b_outras(c, t, C, B):
    head(c, t, B["start"], "OUTRAS FONTES", "LEI 8.212, ART. 27", GEST)
    card(c, 260, 170, 1400, 680)
    rows = [("14.a", "multas, juros e atualização monetária"), ("14.b", "receitas patrimoniais e financeiras"),
            ("14.c", "doações e legados"), ("14.d", "parte dos valores de bens apreendidos")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 300 + k * 130 + dy
        check_icon(c, 360, y - 12, 26, a, GEST)
        text(c, s, 420, y, 42, "bold", INK, a, align="left")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("15.p1", "15.r1", "financiada SOMENTE pelas contribuições sociais", False, "também pelos ORÇAMENTOS (forma indireta)"),
             ("15.p2", "15.r2", "a contribuição das loterias incide sobre o PRÊMIO", False, "incide sobre a RECEITA do concurso"),
             ("15.p3", "15.r3", "a empresa contribui também sobre o que paga a AUTÔNOMOS", True, "pessoa física, mesmo sem vínculo")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_caput(c, t, C, B):
    ce(c, t, C, "16.e", "16.r", "16.x",
       ["A seguridade será financiada por toda a sociedade, de forma", "direta e indireta, mediante recursos dos orçamentos da União,",
        "dos Estados, do Distrito Federal e dos Municípios,", "e das contribuições sociais."],
       "CERTO", True, "texto do art. 195, caput, com os QUATRO entes", "LEI SECA · ART. 195", size=36)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("17.a", "financiamento DIRETO e INDIRETO, por toda a sociedade"), ("17.b", "4 fontes: E · T · C · I"),
            ("17.c", "empresa: folha, receita e lucro (FAROL)"), ("17.d", "folha inclui pessoa física SEM vínculo"),
            ("17.e", "aposentadoria e pensão do RGPS: sem contribuição"), ("17.f", "a UNIÃO cobre as insuficiências")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["18.like"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Os parágrafos do art. 195", W / 2, 430, 64, "black", INK, a)
        for k, s in enumerate(("contrapartida", "noventena", "imunidade", "orçamento")):
            pill(c, s, 510 + k * 300, 540, PREST, size=28, a=ep(t, B["start"] + 1.5 + 0.5 * k, 0.4) * a, anchor="center")
    cta(c, t, C["18.like"], C["18.sub"], C["18.bell"], C["18.com"], C["18.bye"], "Já conhecia o macete do farol?")


BLOCKS = dict(hook=b_hook, toda=b_toda, solid=b_solid, etci=b_etci, emp=b_emp, folha=b_folha, q_folha=b_q_folha,
              trab=b_trab, loteria=b_loteria, lei11=b_lei11, lei11b=b_lei11b, uniao=b_uniao, outras=b_outras,
              pegadinhas=b_pegadinhas, q_caput=b_q_caput, resumo=b_resumo, cta=b_cta)
