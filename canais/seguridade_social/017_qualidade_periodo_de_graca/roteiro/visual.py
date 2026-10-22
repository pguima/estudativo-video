"""Visual do vídeo Seguridade 017 — Qualidade de segurado e período de graça (Lei 8.213, art. 15 e §§; art. 27-A;
Lei 10.666/2003, art. 3º). Tema 'seguridade'.
Cores: lei / prazo-regra (12 meses) = verde-petróleo · macete = âmbar · militar e facultativo = roxo · perda = vermelho ·
manter / certo = verde. Reaproveita do 013/012 (rowbox, numero), do 011 (chip, frame, lei_card) e do 010 (ce, tag, ok_x, pdf_card)."""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "012_contribuinte_individual" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v012", _p)
V12 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V12)
motor.set_theme("seguridade")
chip, frame, ce, tag, ok_x, pdf_card, rowbox = V12.chip, V12.frame, V12.ce, V12.tag, V12.ok_x, V12.pdf_card, V12.rowbox
lei_card = V12.V11.lei_card

MARCA = ""
ARQUIVO_FINAL = "seguridade_017_qualidade_periodo_de_graca.mp4"
CARD_R = (140, 150, 1640, 690)

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
REGRA, CURTO, PERDA, MANT = PREST, GEST, RED, "#16A36A"


def numero(c, n, sub, cx, cy, a, col=REGRA, w=230, h=230, size=96):
    """quadrado colorido com um número grande e a legenda embaixo (como no 013)"""
    if a <= 0:
        return
    sc = 0.85 + 0.15 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(sc, sc)
    rrect(c, -w / 2, -h / 2, w, h, 26, col, a, shadow=True)
    text_mid(c, n, 0, -18, size, "black", "#FFFFFF", a)
    text_mid(c, sub, 0, h / 2 - 40, 24, "bold", "#FFFFFF", a)
    c.restore()


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 17 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    fatos = [("01.a", "15 anos", "como empregado", REGRA),
             ("01.b", "180", "contribuições sem interrupção", MANT),
             ("01.c", "demitido", "registrado como desempregado", ASSIST)]
    for k, (cue, s1, s2, col) in enumerate(fatos):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 150 + k * 550
        y = 260 + d
        rrect(c, x, y, 520, 170, 24, "#FFFFFF", a, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 14, 170), paint(col, a))
        text(c, s1, x + 50, y + 80, 56, "black", col, a, align="left")
        text(c, s2, x + 50, y + 132, 27, "bold", GRAY, a, align="left")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "POR QUANTO TEMPO ELE CONTINUA PROTEGIDO?", W / 2, 540, REGRA, ad, 42, 1300)
    for k, s in enumerate(("12 meses?", "24 meses?", "ou mais?")):
        ae = ep(t, C["01.e"] + 0.5 * k, 0.4)
        if ae > 0:
            x = W / 2 + (k - 1) * 360
            rrect(c, x - 150, 620, 300, 90, 20, "#F7F7F5", ae, shadow=True)
            text_mid(c, s, x, 665, 40, "black", INK, ae)
    pill(c, "resolvemos juntos no fim da aula", W / 2, 790, ASSIST, size=30, a=ep(t, C["01.f"], 0.5), anchor="center")


def b_base(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213/1991 · ART. 15", "QUALIDADE E PERÍODO DE GRAÇA", REGRA)
    a0 = ep(t, C["02.t"], 0.4)
    text(c, "AULA DE", W / 2 - 20, 300, 60, "black", INK, a0, align="right")
    if a0 > 0:
        tag(c, "NÚMEROS", W / 2 + 10, 280, ASSIST, a0, 60)
    aa, da = rise(t, C["02.a"])
    if aa > 0:
        rrect(c, 560, 360 + da, 800, 110, 24, PREST, aa, shadow=True)
        text_mid(c, "LEI 8.213/1991 · ART. 15", W / 2, 415 + da, 46, "black", "#FFFFFF", aa)
    for k, (cue, s1, s2, col) in enumerate((("02.b", "o PRAZO", "de cada inciso", REGRA),
                                             ("02.c", "as PRORROGAÇÕES", "§§ 1º e 2º", ASSIST),
                                             ("02.d", "a DATA EXATA", "da perda · §4º", PERDA))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 215 + k * 505
        rrect(c, x, 540 + d, 480, 200, 24, mix("#FFFFFF", col, 0.08), a)
        c.drawRect(skia.Rect.MakeXYWH(x, 540 + d, 14, 200), paint(col, a))
        badge_num(c, k + 1, x + 70, 600 + d, a, 26, bg=col)
        text(c, s1, x + 115, 615 + d, 34, "black", col, a, align="left")
        text(c, s2, x + 115, 680 + d, 30, "bold", GRAY, a, align="left")


def b_conceito(c, t, C, B):
    frame(c, t, B["start"], "O CONCEITO", "QUALIDADE DE SEGURADO", REGRA)
    a1 = fw(t, B["start"], C["03.e"] - 0.3)
    if a1 > 0:
        text(c, "a condição de quem está COBERTO: a vigência do seguro", W / 2, 260, 38, "black", INK, a1)
        rows = [("03.a", "FILIAÇÃO", "o INGRESSO no sistema", "Aula 16", GRAY),
                ("03.b", "QUALIDADE", "a MANUTENÇÃO da cobertura", "esta aula", REGRA),
                ("03.c", "CARÊNCIA", "o TEMPO MÍNIMO de contribuição", "Aula 18", GRAY)]
        for k, (cue, s1, s2, quando, col) in enumerate(rows):
            a, d = rise(t, C[cue])
            a *= a1
            if a <= 0:
                continue
            y = 380 + k * 105 + d
            rrect(c, 260, y - 46, 1400, 92, 18, mix("#FFFFFF", REGRA, 0.10) if k == 1 else "#F7F7F5", a)
            text(c, s1, 300, y + 14, 42, "black", REGRA if k == 1 else INK, a, align="left")
            text(c, s2, 680, y + 14, 36, "bold", INK, a, align="left")
            pill(c, quando, 1630, y, col, size=24, a=a, anchor="right", bounds=(0, 1920))
        pill(c, "em regra: SEM QUALIDADE, NÃO HÁ BENEFÍCIO", W / 2, 760, PERDA, size=32, a=ep(t, C["03.d"], 0.4) * a1,
             anchor="center")
    a2 = ep(t, C["03.e"], 0.5)
    if a2 > 0:
        chip(c, "PERÍODO DE GRAÇA", W / 2, 270, MANT, a2, 46, 760)
        text(c, "o segurado continua protegido MESMO SEM CONTRIBUIR", W / 2, 390, 38, "black", INK, a2)
        lei_card(c, t, [(C["03.g"], "“Mantém a qualidade de segurado,", False),
                        (C["03.g"] + 1.0, "INDEPENDENTEMENTE DE CONTRIBUIÇÕES”", True)],
                 x=360, y=440, w=1200, size=40, col=PREST, src="ART. 15, CAPUT")
        ah = ep(t, C["03.h"], 0.5)
        if ah > 0:
            pill(c, "§3º: conserva TODOS OS SEUS DIREITOS perante a previdência", W / 2, 775, MANT, size=30, a=ah,
                 anchor="center")


INCISOS = [("04.a", "I", "em gozo de benefício", "", "SEM LIMITE", MANT),
           ("04.b", "II", "deixou de exercer atividade remunerada", "ou suspenso / licenciado sem remuneração", "12 MESES", REGRA),
           ("04.c", "III", "doença de segregação compulsória", "após cessar a segregação", "12 MESES", REGRA),
           ("04.d", "IV", "preso (retido ou recluso)", "após o LIVRAMENTO", "12 MESES", REGRA),
           ("04.e", "V", "serviço militar", "após o LICENCIAMENTO", "3 MESES", CURTO),
           ("04.f", "VI", "segurado facultativo", "após cessar as contribuições", "6 MESES", CURTO)]


def b_incisos(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213/1991 · ART. 15", "OS SEIS INCISOS", REGRA)
    for k, (cue, rom, s1, s2, prazo, col) in enumerate(INCISOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 225 + k * 102 + d
        rrect(c, 200, y - 44, 1520, 92, 18, "#F7F7F5", a)
        tag(c, rom, 225, y + 2, col, a, 34)
        if s2:
            text(c, s1, 360, y - 2, 34, "black", INK, a, align="left")
            text(c, s2, 360, y + 34, 26, "bold", GRAY, a, align="left")
        else:
            text(c, s1, 360, y + 14, 34, "black", INK, a, align="left")
        pill(c, prazo, 1695, y + 2, col, size=32, a=ep(t, C[cue] + 0.6, 0.4), anchor="right", bounds=(0, 1920))


FRASE = [("05.a", "3", "militar · o mais curto", CURTO), ("05.b", "6", "facultativo", CURTO),
         ("05.c", "12", "todo o resto", REGRA), ("05.d", "∞", "quem já recebe", MANT)]


def b_frase(c, t, C, B):
    frame(c, t, B["start"], "GUARDE ESTA FRASE", "3 · 6 · 12 · ∞", ASSIST)
    for k, (cue, n, sub, col) in enumerate(FRASE):
        numero(c, n, sub, 420 + k * 360, 310, ep(t, C[cue], 0.45), col, 300, 200, 92)
    pill(c, "TERMOS INICIAIS: a banca adora trocar", W / 2, 480, ASSIST, size=30, a=ep(t, C["05.e"], 0.4),
         anchor="center", fg=INK)
    for k, (cue, cno, s, errado) in enumerate((("05.f", "05.g", "PRESO: 12 meses depois de SOLTO", "não da prisão"),
                                               ("05.h", "05.i", "MILITAR: 3 meses depois do LICENCIAMENTO",
                                                "não da incorporação"))):
        y = 590 + k * 120
        rowbox(c, s, y, ep(t, C[cue], 0.4), None, x=220, w=1480, size=38)
        an = ep(t, C[cno], 0.4)
        if an > 0:
            text(c, errado, 1640, y + 12, 32, "bold", RED, an, align="right")
            tw = text_w(errado, "bold", 32)
            strike(c, 1640 - tw - 6, y + 1, 1646, y + 1, an, RED, an)


def b_acidente(c, t, C, B):
    frame(c, t, B["start"], "ART. 15, I · A EXCEÇÃO", "SEM LIMITE... EXCETO", PERDA)
    aa = ep(t, C["06.a"], 0.4)
    ok_x(c, "em gozo de benefício: SEM LIMITE de prazo", W / 2 - 30, 260, True, aa, 32)
    ab, db = rise(t, C["06.b"])
    if ab > 0:
        rrect(c, 460, 330 + db, 1000, 120, 24, PERDA, ab, shadow=True)
        text_mid(c, "EXCETO O AUXÍLIO-ACIDENTE", W / 2, 390 + db, 52, "black", "#FFFFFF", ab)
    text(c, "POR QUÊ?", W / 2, 530, 40, "black", GRAY, ep(t, C["06.c"], 0.4), tracking=2)
    for k, (cue, s1, s2, col) in enumerate((("06.d", "INDENIZATÓRIO", "não substitui a renda", GEST),
                                             ("06.e", "JUNTO COM O SALÁRIO", "quem recebe continua trabalhando", ASSIST))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 730
        rrect(c, x, 570 + d, 690, 140, 22, mix("#FFFFFF", col, 0.10), a)
        c.drawRect(skia.Rect.MakeXYWH(x, 570 + d, 12, 140), paint(col, a))
        text(c, s1, x + 50, 630 + d, 42, "black", col if col != ASSIST else INK, a, align="left")
        text(c, s2, x + 50, 680 + d, 28, "bold", GRAY, a, align="left")
    pill(c, "ressalva incluída depois por alteração da lei: confira o texto compilado", W / 2, 790, INK2, size=26,
         a=ep(t, C["06.f"], 0.5), anchor="center")


def b_prorrog(c, t, C, B):
    frame(c, t, B["start"], "ART. 15, §§ 1º E 2º", "AS DUAS PRORROGAÇÕES", ASSIST)
    # §1º
    aa, da = rise(t, C["07.a"])
    if aa > 0:
        card(c, 200, 200 + da, 740, 600, aa)
        tag(c, "§1º", 240, 260 + da, PREST, aa, 40)
        text(c, "inciso II", 390, 275 + da, 32, "bold", GRAY, aa, align="left")
        text(c, "12 → 24 meses", 570, 400 + da, 70, "black", PREST, aa)
        ab = ep(t, C["07.b"], 0.4)
        text(c, "MAIS DE 120 contribuições", 570, 490 + da, 40, "black", INK, ab)
        text(c, "sem interrupção que acarrete", 570, 545 + da, 30, "bold", GRAY, ab)
        text(c, "a perda da qualidade", 570, 585 + da, 30, "bold", GRAY, ab)
        acc = ep(t, C["07.c"], 0.4)
        if acc > 0:
            rrect(c, 250, 650 + da, 640, 100, 20, mix("#FFFFFF", RED, 0.12), acc)
            text_mid(c, "120 exatas NÃO bastam: 121+", 570, 700 + da, 36, "black", RED, acc)
    # §2º
    ad, dd = rise(t, C["07.d"])
    if ad > 0:
        card(c, 980, 200 + dd, 740, 600, ad)
        tag(c, "§2º", 1020, 260 + dd, ASSIST, ad, 40)
        text(c, "inciso II ou §1º", 1170, 275 + dd, 32, "bold", GRAY, ad, align="left")
        text(c, "+ 12 meses", 1350, 400 + dd, 70, "black", ASSIST, ad)
        text(c, "DESEMPREGADO", 1350, 490 + dd, 40, "black", INK, ad)
        ae = ep(t, C["07.e"], 0.4)
        text(c, "comprovado pelo REGISTRO no", 1350, 545 + dd, 30, "bold", GRAY, ae)
        text(c, "órgão próprio do Min. do Trabalho", 1350, 585 + dd, 30, "bold", GRAY, ae)
        af = ep(t, C["07.f"], 0.4)
        if af > 0:
            rrect(c, 1030, 650 + dd, 640, 100, 20, mix("#FFFFFF", ASSIST, 0.18), af)
            text_mid(c, "pediu a lei? é o REGISTRO", 1350, 700 + dd, 36, "black", INK, af)


DEGRAUS = [("08.b", "12", "a REGRA", "inciso II", REGRA),
           ("08.c", "24", "+120 contribuições", "OU desemprego", ASSIST),
           ("08.d", "36", "as DUAS", "coisas juntas", MANT)]


def b_escada(c, t, C, B):
    frame(c, t, B["start"], "PONTO DE OURO", "A ESCADA DOS PRAZOS", ASSIST)
    base_y = 620
    for k, (cue, n, s1, s2, col) in enumerate(DEGRAUS):
        if ep(t, C["08.a"] + 0.6 * k, 0.45) <= 0:
            continue
        h = 150 + k * 110
        x = 280 + k * 430
        ah = ep(t, C["08.a"] + 0.6 * k, 0.5)
        hh = h * ah
        rrect(c, x, base_y - hh, 400, hh, 22, col, ah, shadow=True)
        text_mid(c, n, x + 200, base_y - hh + 70, 84, "black", "#FFFFFF", ah)
        text(c, "meses", x + 200, base_y - hh + 135, 28, "bold", "#FFFFFF", ah)
        hl = ep(t, C[cue], 0.4)
        if hl > 0:
            text(c, s1, x + 200, base_y + 50, 32, "black", INK, hl)
            text(c, s2, x + 200, base_y + 88, 26, "bold", GRAY, hl)
    chip(c, "MÁXIMO: 36 MESES", 520, 280, PERDA, ep(t, C["08.e"], 0.5), 40, 560)
    af = ep(t, C["08.f"], 0.4)
    pill(c, "prorrogações: SÓ o inciso II", 620, 780, PREST, size=30, a=af, anchor="center")
    ag = ep(t, C["08.g"], 0.4)
    if ag > 0:
        ok_x(c, "militar (3) e facultativo (6) não sobem", 1300, 780, False, ag, 28)


TL = [("09.c", "FIM", "do período de graça", INK2), ("09.d", "MÊS SEGUINTE", "o imediatamente posterior", ASSIST),
      ("09.e", "VENCIMENTO", "da contribuição desse mês", GEST), ("09.f", "PERDA", "no DIA SEGUINTE", PERDA)]


def b_perda(c, t, C, B):
    frame(c, t, B["start"], "ART. 15, §4º", "A DATA EXATA DA PERDA", PERDA)
    aa = ep(t, C["09.a"], 0.4)
    if aa > 0:
        pill(c, "NÃO é no dia seguinte ao fim do prazo!", W / 2, 240, RED, size=32, a=aa, anchor="center")
    lei_card(c, t, [(C["09.b"], "perda no dia seguinte ao término do prazo para recolher a contribuição", False),
                    (C["09.b"] + 2.5, "referente ao MÊS IMEDIATAMENTE POSTERIOR ao fim dos prazos", True)],
             x=220, y=290, w=1480, size=33, col=PREST, src="ART. 15, §4º")
    x0, x1, y = 340, 1580, 610
    ac = ep(t, C["09.c"], 0.4)
    if ac > 0:
        prog_l = max(ep(t, C[cue], 0.6) * k / 3 for k, (cue, *_r) in enumerate(TL))
        line(c, x0, y, x0 + (x1 - x0) * prog_l, y, LIGHT, ac, 8)
    for k, (cue, s1, s2, col) in enumerate(TL):
        a = ep(t, C[cue], 0.4)
        if a <= 0:
            continue
        x = x0 + k * (x1 - x0) / 3
        badge_num(c, k + 1, x, y, a, 30, bg=col)
        text(c, s1, x, y + 80, 34, "black", col, a)
        text(c, s2, x, y + 120, 25, "bold", GRAY, a)
    pill(c, "o dia exato depende da categoria: guarde a MECÂNICA, não o dia", W / 2, 800, ASSIST, size=27,
         a=ep(t, C["09.g"], 0.5), anchor="center", fg=INK)


ART27 = [("10.b", "incapacidade temporária e permanente", "12", "6"),
         ("10.c", "salário-maternidade", "10", "5"),
         ("10.d", "auxílio-reclusão", "24", "12")]


def b_art27a(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213/1991 · ART. 27-A", "PERDEU E VOLTOU?", PREST)
    aa = ep(t, C["10.a"], 0.4)
    text(c, "METADE da carência, a partir da NOVA FILIAÇÃO", W / 2, 250, 42, "black", INK, aa)
    for k, (cue, s, cheio, meia) in enumerate(ART27):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 340 + k * 100 + d
        rrect(c, 220, y - 44, 1480, 88, 18, "#F7F7F5", a)
        text(c, s, 260, y + 13, 36, "black", INK, a, align="left")
        text(c, cheio, 1300, y + 15, 44, "black", GRAY, a)
        ar = ep(t, C[cue] + 1.0, 0.4)
        strike(c, 1265, y, 1335, y, ar, RED, ar)
        arrow(c, 1370, y, 1450, y, GRAY, ar, 4, 14)
        text(c, meia, 1560, y + 17, 54, "black", MANT, ar)
    ae = ep(t, C["10.e"], 0.4)
    rowbox(c, "aposentadoria POR IDADE", 650, ae, "FICA DE FORA", RED, ae, 36)
    pill(c, "a perda NÃO apaga o tempo de contribuição já cumprido", W / 2, 785, MANT, size=30,
         a=ep(t, C["10.f"], 0.5), anchor="center")


def b_lei10666(c, t, C, B):
    frame(c, t, B["start"], "LEI 10.666/2003 · ART. 3º", "QUANDO A PERDA NEM IMPORTA", MANT)
    aa = ep(t, C["11.a"], 0.4)
    text(c, "a perda da qualidade NÃO É CONSIDERADA para a aposentadoria:", W / 2, 250, 38, "black", INK, aa)
    rows = [("11.b", "por TEMPO DE CONTRIBUIÇÃO", "NÃO IMPORTA"),
            ("11.c", "ESPECIAL", "NÃO IMPORTA"),
            ("11.d", "POR IDADE · §1º", "se já tem a CARÊNCIA")]
    for k, (cue, s, res) in enumerate(rows):
        a = ep(t, C[cue], 0.4)
        rowbox(c, s, 360 + k * 120, a, res, MANT if k < 2 else ASSIST, ep(t, C[cue] + 0.8, 0.4), 40)
    ae, de = rise(t, C["11.e"])
    if ae > 0:
        rrect(c, 220, 700 + de, 1480, 110, 20, mix("#FFFFFF", ASSIST, 0.18), ae)
        text_mid(c, "tempo de contribuição: extinta pela EC 103/2019", W / 2, 735 + de, 32, "black", INK, ae)
        text_mid(c, "sobrevive na TRANSIÇÃO e no DIREITO ADQUIRIDO", W / 2, 778 + de, 28, "bold", INK2, ae)


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 160, 1520, 700)
    items = [("12.p1", "12.r1", "o facultativo mantém a qualidade por 12 meses", False, "são 6 meses"),
             ("12.p2", "12.r2", "o período de graça é de, no máximo, 24 meses", False, "pode chegar a 36"),
             ("12.p3", "12.r3", "QUALQUER benefício mantém a qualidade sem limite", False, "exceto o auxílio-acidente"),
             ("12.p4", "12.r4", "a perda não é considerada para a aposentadoria especial", True, "Lei 10.666/2003, art. 3º")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 250 + k * 150 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 50, GREEN if ok else RED, size=28, a=ar, anchor="right",
             bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 60, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_ce(c, t, C, B):
    ce(c, t, C, "13.e", "13.r", "13.x",
       ["O prazo do inciso II será prorrogado para até 24 meses", "se o segurado já tiver pago 120 contribuições mensais,",
        "sem interrupção que acarrete a perda da qualidade."],
       "ERRADO", False, "a lei exige MAIS DE 120: no mínimo, 121", "§1º DO ART. 15", size=40)


CASO = [("14.a", "prazo básico do inciso II", "12"),
        ("14.b", "180 contribuições: mais de 120 (§1º)", "24"),
        ("14.c", "registrado como desempregado (§2º)", "36")]


def b_caso(c, t, C, B):
    head(c, t, B["start"], "O CASO DO CARLOS", "DEGRAU POR DEGRAU", REGRA)
    card(c, 200, 160, 1520, 700)
    for k, (cue, s, tot) in enumerate(CASO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 115 + d
        badge_num(c, str(k + 1), 280, y - 12, a, 26, bg=INK)
        text(c, s, 330, y, 38, "black", INK, a, align="left")
        ar = ep(t, C[cue] + 1.2, 0.4)
        if k:
            text(c, "+12", 1300, y, 36, "black", ASSIST, ar, align="right")
        pill(c, f"{tot} meses", 1660, y - 12, DEGRAUS[k][4], size=32, a=ar, anchor="right", bounds=(0, 1920))
    ad = ep(t, C["14.d"], 0.5)
    chip(c, "TOTAL: 36 MESES", W / 2, 640, MANT, ad, 50, 760)
    pill(c, "com só 100 contribuições: 12 + 12 = 24 meses", W / 2, 780, ASSIST, size=30, a=ep(t, C["14.e"], 0.5),
         anchor="center", fg=INK)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("15.a", "art. 15: ∞ · 12 · 12 · 12 · 3 · 6 (incisos I a VI)"),
            ("15.b", "inciso I: exceto o AUXÍLIO-ACIDENTE"),
            ("15.c", "preso: após o LIVRAMENTO · militar: após o LICENCIAMENTO · facultativo: 6"),
            ("15.d", "escada 12 → 24 → 36, só no inciso II"),
            ("15.e", "perda: dia seguinte ao vencimento da contribuição do mês seguinte"),
            ("15.f", "perdeu e voltou: METADE da carência (menos na aposentadoria por idade)")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 255 + k * 100 + dy
        check_icon(c, 270, y - 12, 24, a, GREEN)
        text(c, s, 315, y, 33, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["16.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Carência", W / 2, 430, 72, "black", INK, a)
        text(c, "quantas contribuições cada benefício exige", W / 2, 500, 36, "bold", GRAY,
             ep(t, B["start"] + 1.2, 0.4) * a)
        pill(c, "fecha a Temporada 2", W / 2, 590, GEST, size=30, a=ep(t, B["start"] + 3.5, 0.4) * a, anchor="center")
    ap = fw(t, C["16.pdf"], C["16.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["16.pdf"], 0.5)) * 20)
    cta(c, t, C["16.like"], C["16.sub"], C["16.bell"], C["16.com"], C["16.bye"],
        "Você chegou aos 36 meses do Carlos?", canal="no Estudativo")


BLOCKS = dict(hook=b_hook, base=b_base, conceito=b_conceito, incisos=b_incisos, frase=b_frase, acidente=b_acidente,
              prorrog=b_prorrog, escada=b_escada, perda=b_perda, art27a=b_art27a, lei10666=b_lei10666,
              pegadinhas=b_pegadinhas, q_ce=b_q_ce, caso=b_caso, resumo=b_resumo, cta=b_cta)
