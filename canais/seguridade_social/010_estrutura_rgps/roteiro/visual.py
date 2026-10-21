"""Visual do vídeo Seguridade 010 — A estrutura do RGPS (Lei 8.213, arts. 10, 11, 13 e 18). Tema 'seguridade'."""
import math
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "seguridade_010_estrutura_rgps.mp4"
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


def lista(c, t, C, rows, x, y0, dy, size=40, col=INK, bullet=PREST):
    for k, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = y0 + k * dy + d
        badge_num(c, k + 1, x, y - 12, a, 24, bg=bullet)
        text(c, s, x + 50, y, size, "black", col, a, align="left")


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 10 · TEMPORADA 2", W / 2, 200, BLUE, size=30, a=a0, anchor="center")
    aa = ep(t, C["01.a"], 0.5)
    text(c, "no RGPS só existem DOIS tipos de gente", W / 2, 320, 50, "black", INK, aa)
    for k, (cue, big, sub, col) in enumerate((("01.b", "SEGURADO", "quem contribui", PREST),
                                              ("01.c", "DEPENDENTE", "quem depende de quem contribui", ASSIST))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 320, 400 + dy, 640, 200, 26, col, a, shadow=True)
        text_mid(c, big, x, 470 + dy, 60, "black", "#FFFFFF", a)
        text_mid(c, sub, x, 540 + dy, 30, "bold", "#FFFFFF", a)
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "o MAPA do RGPS · Lei 8.213/1991", W / 2, 720, PREST, size=32, a=ad, anchor="center")


def b_rgps(c, t, C, B):
    head(c, t, B["start"], "O QUE É O RGPS", "REGIME GERAL DE PREVIDÊNCIA SOCIAL", PREST)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.6, 0.5)
    text(c, "iniciativa privada + quem NÃO tem regime próprio", W / 2, 240, 38, "bold", GRAY, a0)
    items = [("02.a", "GESTOR", "INSS", PREST), ("02.b", "FILIAÇÃO", "OBRIGATÓRIA", GEST),
             ("02.c", "CUSTEIO", "CONTRIBUTIVO", ASSIST), ("02.d", "REGIME", "REPARTIÇÃO", RED)]
    for k, (cue, lab, val, col) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 340 + k * 413
        rrect(c, x - 180, 320 + dy, 360, 200, 24, col, a, shadow=True)
        text_mid(c, lab, x, 380 + dy, 28, "black", "#FFFFFF", a)
        text_mid(c, val, x, 450 + dy, 40 if len(val) < 12 else 34, "black", "#FFFFFF", a)
    ad = ep(t, C["02.d"] + 1.6, 0.5)
    text(c, "quem trabalha HOJE paga quem está aposentado HOJE", W / 2, 640, 40, "black", INK, ad)
    text(c, "não existe poupança individual", W / 2, 700, 32, "bold", GRAY, ad)


def b_normas(c, t, C, B):
    head(c, t, B["start"], "A BANCA ADORA TROCAR", "8.212 × 8.213", ASSIST)
    for k, (cue, lei, nome, sub, col) in enumerate((("03.a", "8.212", "CUSTEIO", "dinheiro ENTRANDO", PREST),
                                                   ("03.b", "8.213", "BENEFÍCIOS", "dinheiro SAINDO", ASSIST))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 820
        card(c, x, 190 + dy, 700, 380, a)
        text(c, "LEI", x + 350, 260 + dy, 30, "black", GRAY, a)
        text(c, lei, x + 350, 380 + dy, 110, "black", col, a)
        text(c, nome, x + 350, 460 + dy, 46, "black", INK, a)
        text(c, sub, x + 350, 520 + dy, 32, "bold", GRAY, a)
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        text(c, "o 2 vem antes: primeiro se PAGA", 560, 650, 36, "black", PREST, ac)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        text(c, "o 3 vem depois: depois se RECEBE", 1370, 650, 36, "black", ASSIST, ad)
    ae = ep(t, C["03.e"], 0.5)
    pill(c, "Decreto 3.048/1999 regulamenta as duas", W / 2, 750, GRAY, size=30, a=ae, anchor="center")


def b_binaria(c, t, C, B):
    head(c, t, B["start"], "LEI 8.213 · ART. 10", "OS BENEFICIÁRIOS", PREST)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 260, 210, 520, 100, 24, INK, aa, shadow=True)
        text_mid(c, "BENEFICIÁRIOS", W / 2, 260, 44, "black", "#FFFFFF", aa)
    for k, (cue, s, col) in enumerate((("04.b", "SEGURADOS", PREST), ("04.c", "DEPENDENTES", ASSIST))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 600 + k * 720
        line(c, W / 2, 310, x, 420, LIGHT, a, 5)
        rrect(c, x - 250, 420 + dy, 500, 120, 24, col, a, shadow=True)
        text_mid(c, s, x, 480 + dy, 50, "black", "#FFFFFF", a)
    ad = ep(t, C["04.d"], 0.5)
    text(c, "divisão BINÁRIA · não existe terceira categoria", W / 2, 680, 42, "black", INK, ad)


def b_pensionista(c, t, C, B):
    head(c, t, B["start"], "PRIMEIRA PEGADINHA", "E O PENSIONISTA?", RED)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "“beneficiários: segurados, dependentes", W / 2, 280, 44, "semibold", INK, aa)
        text(c, "E OS PENSIONISTAS”", W / 2, 350, 52, "black", RED, aa)
    ar = ep(t, C["05.r"], 0.4)
    result_box(c, "ERRADO", W / 2, 460, 56, ar, RED)
    ab = ep(t, C["05.b"], 0.5)
    text(c, "pensionista = DEPENDENTE que já recebe pensão", W / 2, 600, 40, "black", INK, ab)
    ac = ep(t, C["05.c"], 0.5)
    pill(c, "pensionista e aposentado são SITUAÇÕES, não categorias", W / 2, 700, ASSIST, size=30, a=ac, anchor="center")


def b_obrigatorios(c, t, C, B):
    head(c, t, B["start"], "LEI 8.213 · ART. 11", "OS 5 SEGURADOS OBRIGATÓRIOS", PREST)
    card(c, 200, 170, 1520, 680)
    rows = [("06.s1", "I", "E", "mpregado"), ("06.s2", "II", "E", "mpregado doméstico"),
            ("06.s3", "V", "C", "ontribuinte individual"), ("06.s4", "VI", "T", "rabalhador avulso"),
            ("06.s5", "VII", "S", "egurado especial")]
    for k, (cue, rom, l, rest) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 100 + dy
        tag(c, rom, 260, y - 14, PREST, a, 30)
        text(c, l, 520, y + 14, 80, "black", ASSIST, a, align="right")
        text(c, rest, 524, y + 14, 50, "black", INK, a, align="left")
    pill(c, "E · E · C · T · S", W / 2, 790, ASSIST, size=40, a=ep(t, C["06.m"], 0.5), anchor="center")


def b_revogados(c, t, C, B):
    head(c, t, B["start"], "REPARE NOS INCISOS", "CADÊ O III E O IV?", ASSIST)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    roms = ["I", "II", "III", "IV", "V", "VI", "VII"]
    ab = ep(t, C["07.b"], 0.5)
    for k, r in enumerate(roms):
        x = 330 + k * 210
        miss = r in ("III", "IV")
        a = ab if miss else aa
        if a <= 0:
            continue
        rrect(c, x - 85, 210, 170, 110, 20, RED if miss else PREST, a, shadow=not miss)
        text_mid(c, r, x, 265, 52, "black", "#FFFFFF", a)
    ac = ep(t, C["07.c"], 0.5)
    pill(c, "REVOGADOS em 1999 (Lei 9.876)", W / 2, 390, RED, size=32, a=ac, anchor="center")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        pill(c, "empresário (III)", 640, 500, INK, size=36, a=ad, anchor="center")
        pill(c, "autônomo (IV)", 1280, 500, INK, size=36, a=ad, anchor="center")
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        arrow(c, 760, 540, 900, 600, INK, ae, 5, 16)
        arrow(c, 1160, 540, 1020, 600, INK, ae, 5, 16)
        result_box(c, "CONTRIBUINTE INDIVIDUAL", W / 2, 650, 44, ae, GEST)
    af = ep(t, C["07.f"], 0.5)
    if af > 0:
        ok_x(c, "empresário ou autônomo como categoria", W / 2 - 30, 770, False, af, 30)


def b_facultativo(c, t, C, B):
    head(c, t, B["start"], "LEI 8.213 · ART. 13", "O SEXTO SEGURADO", GEST)
    aa, dya = rise(t, C["08.a"])
    if aa > 0:
        card(c, 200, 190 + dya, 760, 420, aa)
        text(c, "FACULTATIVO", 580, 300 + dya, 64, "black", GEST, aa)
        ab = ep(t, C["08.b"], 0.5)
        text(c, "não está no art. 11", 580, 400 + dya, 38, "bold", GRAY, ab)
        text(c, "entra PORQUE QUER", 580, 480 + dya, 50, "black", INK, ab)
    ac = ep(t, C["08.c"], 0.5)
    text(c, "quantas categorias?", 1340, 260, 40, "black", GRAY, ac)
    ad, dyd = rise(t, C["08.d"])
    if ad > 0:
        text(c, "6", 1340, 470 + dyd, 220, "black", PREST, ad)
        text(c, "5 obrigatórios + 1 facultativo", 1340, 560 + dyd, 34, "black", INK, ad)


def b_art18(c, t, C, B):
    head(c, t, B["start"], "LEI 8.213 · ART. 18", "AS PRESTAÇÕES", PREST)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 230, 210, 460, 100, 24, INK, aa, shadow=True)
        text_mid(c, "PRESTAÇÕES", W / 2, 260, 44, "black", "#FFFFFF", aa)
        line(c, W / 2, 310, 600, 400, LIGHT, aa, 5)
        rrect(c, 380, 400, 440, 140, 24, PREST, aa, shadow=True)
        text_mid(c, "BENEFÍCIOS", 600, 450, 44, "black", "#FFFFFF", aa)
        text_mid(c, "em DINHEIRO", 600, 505, 28, "bold", "#FFFFFF", aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        line(c, W / 2, 310, 1320, 400, LIGHT, ab, 5)
        rrect(c, 1100, 400, 440, 140, 24, ASSIST, ab, shadow=True)
        text_mid(c, "SERVIÇOS", 1320, 450, 44, "black", "#FFFFFF", ab)
        text_mid(c, "não pecuniários", 1320, 505, 28, "bold", "#FFFFFF", ab)
    ac = ep(t, C["09.c"], 0.5)
    text(c, "“inclusive em razão de ACIDENTE DO TRABALHO”", W / 2, 680, 44, "black", GREEN, ac)


def b_segurado(c, t, C, B):
    head(c, t, B["start"], "PRESTAÇÕES", "SÓ DO SEGURADO", PREST)
    card(c, 200, 170, 1520, 680)
    lista(c, t, C, [("10.a", "aposentadorias"), ("10.b", "auxílio por incapacidade temporária"),
                    ("10.c", "salário-família"), ("10.d", "salário-maternidade"), ("10.e", "auxílio-acidente")],
          320, 290, 110, 46, INK, PREST)


def b_dependente(c, t, C, B):
    head(c, t, B["start"], "PRESTAÇÕES", "SÓ DO DEPENDENTE", ASSIST)
    card(c, *CARD_R)
    for k, (cue, l, rest) in enumerate((("11.a", "P", "ensão por morte"), ("11.b", "A", "uxílio-reclusão"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 130 + dy
        text(c, l, 700, y + 30, 120, "black", ASSIST, a, align="right")
        text(c, rest, 706, y + 30, 64, "black", INK, a, align="left")
    pill(c, "P · A", 1500, 360, ASSIST, size=44, a=ep(t, C["11.m"], 0.5), anchor="center")
    ax = ep(t, C["11.x"], 0.5)
    if ax > 0:
        ok_x(c, "auxílio-reclusão ao SEGURADO PRESO", W / 2 - 30, 620, False, ax, 34)
    ar = ep(t, C["11.r"], 0.5)
    text(c, "é devido aos DEPENDENTES dele", W / 2, 740, 46, "black", GREEN, ar)


def b_servicos(c, t, C, B):
    head(c, t, B["start"], "PRESTAÇÕES", "SERVIÇOS: SEGURADO E DEPENDENTE", GEST)
    card(c, *CARD_R)
    a0 = ep(t, B["start"] + 0.6, 0.5)
    text(c, "só DOIS", W / 2, 270, 70, "black", GEST, a0)
    for k, (cue, s) in enumerate((("12.a", "SERVIÇO SOCIAL"), ("12.b", "REABILITAÇÃO PROFISSIONAL"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 360 + dy, 680, 150, 24, GEST, a, shadow=True)
        text_mid(c, s, x, 435 + dy, 40, "black", "#FFFFFF", a)
    ac = ep(t, C["12.c"], 0.5)
    if ac > 0:
        ok_x(c, "perícia médica", W / 2 - 30, 640, False, ac, 40)


def b_nomes(c, t, C, B):
    head(c, t, B["start"], "REFORMA DE 2019", "OS NOMES MUDARAM", ASSIST)
    card(c, 200, 170, 1520, 680)
    rows = [("13.a", "auxílio-doença", "auxílio por incapacidade TEMPORÁRIA"),
            ("13.b", "aposentadoria por invalidez", "aposentadoria por incapacidade PERMANENTE")]
    for k, (cue, old, new) in enumerate(rows):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 150 + dy
        text(c, old, 260, y, 36, "bold", GRAY, a, align="left")
        line(c, 260, y - 12, 260 + text_w(old, "bold", 36), y - 12, GRAY, a, 3)
        text(c, "→ " + new, 300, y + 60, 40, "black", PREST, a, align="left")
    ac, dyc = rise(t, C["13.c"])
    if ac > 0:
        y = 600 + dyc
        text(c, "aposentadoria por TEMPO DE CONTRIBUIÇÃO:", 260, y, 36, "black", INK, ac, align="left")
        text(c, "só na transição e no direito adquirido", 260, y + 55, 34, "bold", RED, ac, align="left")
    ad = ep(t, C["13.d"], 0.5)
    pill(c, "a banca usa o nome ANTIGO ou o NOVO", W / 2, 810, ASSIST, size=30, a=ad, anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("14.p1", "14.r1", "o RGPS possui CINCO categorias de segurado", False, "são SEIS (com o facultativo)"),
             ("14.p2", "14.r2", "a pensão por morte é devida ao SEGURADO", False, "é dos DEPENDENTES"),
             ("14.p3", "14.r3", "prestações devidas INCLUSIVE por acidente do trabalho", True, "Lei 8.213, art. 18")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_lei(c, t, C, B):
    ce(c, t, C, "15.e", "15.r", "15.x",
       ["A Lei 8.212/1991 dispõe sobre os PLANOS DE", "BENEFÍCIOS da Previdência Social."],
       "ERRADO", False, "8.212 = custeio · os benefícios estão na 8.213", "8.212 OU 8.213?", size=46)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("16.a", "RGPS: INSS · obrigatório · contributivo · repartição"),
            ("16.b", "8.212 = custeio · 8.213 = benefícios"),
            ("16.c", "beneficiários: só SEGURADOS e DEPENDENTES"),
            ("16.d", "obrigatórios E · E · C · T · S + facultativo = 6"),
            ("16.e", "só do dependente: P · A"),
            ("16.f", "serviços: só DOIS")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 260 + k * 100 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def pdf_card(c, a, dy=0.0):
    """cartão 'PDF completo · link na descrição' (reaproveitável nos próximos vídeos)"""
    card(c, 460, 230 + dy, 1000, 420, a)
    x0, y0 = 560, 300 + dy
    rrect(c, x0, y0, 220, 280, 18, RED, a, shadow=True)
    text_mid(c, "PDF", x0 + 110, y0 + 140, 70, "black", "#FFFFFF", a)
    text(c, "PDF COMPLETO", 1150, 360 + dy, 56, "black", INK, a)
    text(c, "Seguridade Social para o INSS", 1150, 420 + dy, 32, "bold", GRAY, a)
    text(c, "módulos · pegadinhas · simulados", 1150, 470 + dy, 30, "bold", GRAY, a)
    pill(c, "link na DESCRIÇÃO ↓", 1150, 550 + dy, PREST, size=34, a=a, anchor="center")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["17.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Empregado, doméstico e avulso", W / 2, 430, 64, "black", INK, a)
        pill(c, "os segurados obrigatórios por dentro", W / 2, 540, PREST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a,
             anchor="center")
    ap = fw(t, C["17.pdf"], C["17.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["17.pdf"], 0.5)) * 20)
    cta(c, t, C["17.like"], C["17.sub"], C["17.bell"], C["17.com"], C["17.bye"], "Sabia que os incisos III e IV foram revogados?")


BLOCKS = dict(hook=b_hook, rgps=b_rgps, normas=b_normas, binaria=b_binaria, pensionista=b_pensionista,
              obrigatorios=b_obrigatorios, revogados=b_revogados, facultativo=b_facultativo, art18=b_art18,
              segurado=b_segurado, dependente=b_dependente, servicos=b_servicos, nomes=b_nomes,
              pegadinhas=b_pegadinhas, q_lei=b_q_lei, resumo=b_resumo, cta=b_cta)
