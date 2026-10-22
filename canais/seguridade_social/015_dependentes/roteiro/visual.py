"""Visual do vídeo Seguridade 015 — Dependentes, as 3 classes (Lei 8.213, art. 16 e §§; Decreto 3.048, art. 17). Tema 'seguridade'.
Cores: classe I = verde-petróleo · classe II = roxo · classe III = âmbar · presumida = verde · comprovada = âmbar ·
exclusão / perda = vermelho. Reaproveita do 013/012 (chip, frame, ce, tag, ok_x, pdf_card, rowbox)."""
import importlib.util
from pathlib import Path
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "012_contribuinte_individual" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v012", _p)
V12 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V12)
motor.set_theme("seguridade")
chip, frame, ce, tag, ok_x, pdf_card, rowbox = V12.chip, V12.frame, V12.ce, V12.tag, V12.ok_x, V12.pdf_card, V12.rowbox

MARCA = ""
ARQUIVO_FINAL = "seguridade_015_dependentes.mp4"
CARD_R = (140, 150, 1640, 690)

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
C1, C2, C3 = PREST, GEST, ASSIST
PRES, COMP = "#16A36A", "#E8A317"


def pessoa(c, cx, cy, col, a, s=1.0):
    """bonequinho simples: cabeça + tronco (cy = centro do tronco)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - 58 * s, 30 * s, paint(col, a))
    rrect(c, cx - 44 * s, cy - 20 * s, 88 * s, 76 * s, 34 * s, col, a)


def classe_box(c, rom, x, y, w, h, col, a, l1, l2=None, size=44):
    """faixa de uma classe: tag com o romano + texto"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 22, mix("#FFFFFF", col, 0.08), a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, 14, h), paint(col, a))
    rrect(c, x + 44, y + h / 2 - 44, 150, 88, 16, col, a)
    text_mid(c, rom, x + 119, y + h / 2, 44, "black", "#FFFFFF", a)
    if l2:
        text(c, l1, x + 230, y + h / 2 - 8, size, "black", INK, a, align="left")
        text(c, l2, x + 230, y + h / 2 + 42, 28, "bold", GRAY, a, align="left")
    else:
        text_mid(c, l1, x + 230 + text_w(l1, "black", size) / 2, y + h / 2, size, "black", INK, a)


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 15 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    text(c, "o Antônio, segurado do INSS, faleceu e deixou:", W / 2, 285, 40, "black", INK2, ep(t, C["01.a"], 0.5))
    fam = [("01.b", "a esposa", "", PREST),
           ("01.c", "filho de 23 anos", "saudável", GRAY),
           ("01.d", "filho de 16 anos", "", PREST),
           ("01.e", "a mãe", "dependia dele economicamente", GEST)]
    for k, (cue, s1, s2, col) in enumerate(fam):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 140 + (k % 2) * 830
        y = 330 + (k // 2) * 160 + d
        rrect(c, x, y, 780, 135, 24, "#FFFFFF", a, shadow=True)
        pessoa(c, x + 80, y + 78, col, a, 0.62)
        text(c, s1, x + 150, y + (62 if s2 else 82), 40, "black", INK, a, align="left")
        if s2:
            text(c, s2, x + 150, y + 108, 28, "bold", GRAY, a, align="left")
    af = ep(t, C["01.f"], 0.5)
    chip(c, "QUEM RECEBE A PENSÃO POR MORTE?", W / 2, 720, RED, af, 44, 1080)
    pill(c, "resolvemos juntos no fim da aula", W / 2, 830, ASSIST, size=30, a=ep(t, C["01.g"], 0.5), anchor="center")


def b_base(c, t, C, B):
    frame(c, t, B["start"], "AULA 15", "DEPENDENTES", PREST)
    ok_x(c, "decorar a LISTA", 560, 280, False, ep(t, C["02.a"], 0.4), 34)
    ok_x(c, "resolver o CASO: quem recebe?", 1270, 280, True, ep(t, C["02.b"], 0.4), 34)
    for k, (cue, top, s1, s2, col) in enumerate((
            ("02.c", "LEI 8.213/1991 · ART. 16", "as três classes", "quem é dependente", PREST),
            ("02.d", "DECRETO 3.048/1999 · ART. 17", "a perda da condição", "quando deixa de ser", GEST))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        rrect(c, x - 350, 400 + d, 700, 300, 26, col, a, shadow=True)
        text(c, top, x, 470 + d, 30, "black", "#FFFFFF", a, tracking=1.5)
        text(c, s1, x, 570 + d, 52, "black", "#FFFFFF", a)
        text(c, s2, x, 635 + d, 30, "bold", mix("#FFFFFF", col, 0.25), a)


def b_conceito(c, t, C, B):
    frame(c, t, B["start"], "PRIMEIRO, O CONCEITO", "QUEM É DEPENDENTE", PREST)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "recebe prestações em NOME PRÓPRIO", W / 2, 260, 44, "black", INK, aa)
    text(c, "quando o segurado MORRE ou é PRESO", W / 2, 320, 36, "bold", INK2, ep(t, C["03.a"] + 1.5, 0.5))
    pill(c, "BENEFÍCIOS EXCLUSIVOS: 2", W / 2, 400, INK, size=26, a=ep(t, C["03.b"], 0.4), anchor="center")
    for k, (cue, s1, s2, col) in enumerate((("03.c", "PENSÃO POR MORTE", "o segurado falece", PREST),
                                            ("03.d", "AUXÍLIO-RECLUSÃO", "o segurado é preso", GEST))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 330, 450 + d, 660, 160, 24, col, a, shadow=True)
        text_mid(c, s1, x, 510 + d, 48, "black", "#FFFFFF", a)
        text_mid(c, s2, x, 568 + d, 28, "bold", "#FFFFFF", a)
    ok_x(c, "NÃO contribui · vínculo DERIVADO do segurado", W / 2 - 30, 690, False, ep(t, C["03.e"], 0.4), 30)
    pill(c, "sem segurado, não há dependente", W / 2, 790, ASSIST, size=30, a=ep(t, C["03.f"], 0.5), anchor="center")


def b_classes(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 16, I A III", "AS TRÊS CLASSES", PREST)
    a1, d1 = rise(t, C["04.a"])
    if a1 > 0:
        classe_box(c, "I", 220, 200 + d1, 1480, 230, C1, a1, "")
        text(c, "cônjuge · companheira · companheiro · filho", 450, 270 + d1, 42, "black", INK, a1, align="left")
        sub = ep(t, C["04.a"] + 3.5, 0.5)
        text(c, "filho: não emancipado, de qualquer condição,", 450, 335 + d1, 30, "bold", INK2, sub, align="left")
        text(c, "menor de 21 OU inválido OU com deficiência intelectual, mental ou grave", 450, 385 + d1, 30, "bold",
             INK2, sub, align="left")
    a2, d2 = rise(t, C["04.b"])
    classe_box(c, "II", 220, 450 + d2, 1480, 120, C2, a2, "os PAIS", size=46)
    a3, d3 = rise(t, C["04.c"])
    classe_box(c, "III", 220, 590 + d3, 1480, 120, C3, a3, "o IRMÃO", "com os mesmos requisitos do filho", size=46)
    pill(c, "família nuclear  →  pais  →  irmãos", W / 2, 790, INK, size=34, a=ep(t, C["04.d"], 0.5), anchor="center")


def b_exclusao(c, t, C, B):
    frame(c, t, B["start"], "PONTO DE OURO · ART. 16, §1º", "A REGRA DA EXCLUSÃO", RED)
    a1 = fw(t, C["05.a"], C["05.e"] - 0.2)
    if a1 > 0:
        rrect(c, 220, 200, 1480, 190, 24, mix("#FFFFFF", PREST, 0.06), a1, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(220, 200, 12, 190), paint(PREST, a1))
        text(c, "LEI 8.213/1991 · ART. 16, §1º", 270, 250, 24, "black", PREST, a1, align="left", tracking=1.5)
        text(c, "“a existência de dependente de QUALQUER classe EXCLUI do", 270, 310, 38, "semibold", INK, a1, align="left")
        text(c, "direito às prestações os das classes SEGUINTES”", 270, 360, 38, "semibold", INK, a1, align="left")
        ab = ep(t, C["05.b"], 0.4) * a1
        if ab > 0:
            sc = 0.8 + 0.2 * ease_back(clamp(ab))
            c.save(); c.translate(W / 2, 480); c.scale(sc, sc)
            chip(c, "EXCLUI!", 0, 0, RED, ab, 56, 420)
            c.restore()
        acc = ep(t, C["05.c"], 0.4) * a1
        for k, s in enumerate(("preferência", "prioridade no pagamento")):
            x0, x1 = pill(c, s, 640 + k * 560, 610, LIGHT, INK2, size=32, a=acc, anchor="center")
            strike(c, x0 + 10, 610, x1 - 10, 610, acc, RED, ep(t, C["05.c"] + 0.6 + 0.8 * k, 0.4))
        chip(c, "EXCLUSÃO TOTAL", W / 2, 740, RED, ep(t, C["05.d"], 0.4) * a1, 44, 640)
    a2 = ep(t, C["05.e"], 0.4)
    if a2 > 0:
        for k, (rom, col) in enumerate((("I", C1), ("II", C2), ("III", C3))):
            y = 210 + k * 150
            off = k > 0
            ao = ep(t, C["05.e"] + 0.8, 0.5) if off else 0
            cc = mix(col, LIGHT, ao) if off else col
            rrect(c, 220, y, 700, 128, 22, mix("#FFFFFF", cc, 0.10), a2)
            rrect(c, 250, y + 22, 120, 84, 16, cc, a2)
            text_mid(c, rom, 310, y + 64, 40, "black", "#FFFFFF", a2)
            if not off:
                pessoa(c, 470, y + 78, C1, a2, 0.6)
                text(c, "basta UM", 540, y + 78, 36, "black", INK, a2, align="left")
            else:
                text(c, "ZERO", 470, y + 78, 44, "black", RED, ao, align="left")
                strike(c, 400, y + 64, 890, y + 64, ao, RED, ao)
        af = ep(t, C["05.f"], 0.5)
        if af > 0:
            card(c, 1000, 210, 700, 430, af)
            text(c, "DENTRO DA MESMA CLASSE", 1350, 270, 28, "black", GRAY, af, tracking=1.5)
            for k, (s, col) in enumerate((("cônjuge", C1), ("filho", C1))):
                x = 1210 + k * 280
                pessoa(c, x, 400, col, af, 0.9)
                text(c, s, x, 500, 32, "black", INK, af)
                text(c, "50%", x, 570, 50, "black", PREST, ep(t, C["05.f"] + 1.2, 0.4))
            line(c, 1350, 330, 1350, 590, LINE, af, 3)
        pill(c, "partes IGUAIS · o cônjuge NÃO prefere ao filho", W / 2, 750, INK, size=32,
             a=ep(t, C["05.g"], 0.5), anchor="center")


def b_presuncao(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 16, §4º", "PRESUMIDA × COMPROVADA", PREST)
    a1 = fw(t, C["06.a"], C["06.d"] - 0.2)
    if a1 > 0:
        rows = [("06.a", "CLASSE I · cônjuge, companheiro, filho", "PRESUMIDA", PRES),
                ("06.b", "CLASSE II · os pais", "COMPROVADA", COMP),
                ("06.b", "CLASSE III · o irmão", "COMPROVADA", COMP)]
        for k, (cue, s, res, col) in enumerate(rows):
            ak = ep(t, C[cue] + (0.5 if k == 2 else 0), 0.4) * a1
            rowbox(c, s, 260 + k * 125, ak, res, col, ep(t, C[cue] + 1.0 + (0.5 if k == 2 else 0), 0.4) * a1, 38)
        ac = ep(t, C["06.c"], 0.5) * a1
        if ac > 0:
            chip(c, "CLASSE I NÃO PROVA · II E III PROVAM", W / 2, 690, ASSIST, ac, 44, 1200)
    a2 = ep(t, C["06.d"], 0.4)
    if a2 > 0:
        chip(c, "presunção RELATIVA", W / 2, 290, PRES, a2, 48, 760)
        text(c, "admite prova em contrário", W / 2, 400, 38, "bold", INK2, a2)
        for k, s in enumerate(("filho de 19 anos que começa a trabalhar", "cônjuge que passa a ter renda própria")):
            ak = ep(t, C["06.e"] + 1.6 * k, 0.4)
            rowbox(c, s, 530 + k * 125, ak, "NÃO PERDE", PRES, ep(t, C["06.f"], 0.4), 36)


def b_filho(c, t, C, B):
    frame(c, t, B["start"], "FILHO E IRMÃO", "OS REQUISITOS", C1)
    aa, da = rise(t, C["07.a"])
    if aa > 0:
        rrect(c, 220, 220 + da, 520, 270, 24, C1, aa, shadow=True)
        text_mid(c, "NÃO", 480, 310 + da, 52, "black", "#FFFFFF", aa)
        text_mid(c, "EMANCIPADO", 480, 380 + da, 52, "black", "#FFFFFF", aa)
    ab = ep(t, C["07.b"], 0.4)
    if ab > 0:
        text_mid(c, "+", 800, 355, 90, "black", INK, ab)
        text(c, "basta UMA:", 880, 240, 30, "black", GRAY, ab, align="left")
        for k, s in enumerate(("menor de 21 anos", "inválido", "deficiência intelectual, mental ou grave")):
            ak = ep(t, C["07.b"] + 1.0 + 0.6 * k, 0.4)
            check_icon(c, 900, 300 + k * 72, 20, ak, C1)
            text(c, s, 940, 312 + k * 72, 36, "black", INK, ak, align="left")
    ac = ep(t, C["07.c"], 0.4)
    if ac > 0:
        text(c, "“de qualquer condição”:", 220, 600, 34, "black", GRAY, ac, align="left")
        x = 690
        for k, s in enumerate(("biológico", "adotivo", "havido ou não do casamento")):
            x = pill(c, s, x, 590, PREST, size=30, a=ep(t, C["07.c"] + 0.8 + 0.5 * k, 0.4), bounds=(0, 1920))[1] + 24
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 220, 680, 1480, 110, 22, mix("#FFFFFF", C1, 0.10), ad)
        text_mid(c, "filho INVÁLIDO: sem limite de idade", 720, 735, 40, "black", INK, ad)
        pill(c, "aos 45 anos? continua dependente", 1670, 735, C1, size=28, a=ep(t, C["07.e"], 0.4), anchor="right",
             bounds=(0, 1920))


def b_equiparados(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 16, §2º", "EQUIPARADOS A FILHO", C1)
    a1 = fw(t, C["08.a"], C["08.f"] - 0.2)
    if a1 > 0:
        for k, s in enumerate(("ENTEADO", "MENOR TUTELADO")):
            ak = ep(t, C["08.a"] + 0.9 * k, 0.4) * a1
            x = 620 + k * 680
            pessoa(c, x - 150 - (40 if k else 0), 280, C1, ak, 0.7)
            text(c, s, x - 90 - (40 if k else 0), 292, 44, "black", INK, ak, align="left")
        pill(c, "DOIS REQUISITOS JUNTOS", W / 2, 390, INK, size=28, a=ep(t, C["08.b"], 0.4) * a1, anchor="center")
        for k, (cue, s1, s2) in enumerate((("08.c", "DECLARAÇÃO", "do segurado"),
                                           ("08.d", "COMPROVAÇÃO", "da dependência econômica"))):
            a, d = rise(t, C[cue])
            a *= a1
            if a <= 0:
                continue
            x = 590 + k * 740
            rrect(c, x - 320, 450 + d, 640, 160, 24, C1 if k == 0 else COMP, a, shadow=True)
            text_mid(c, s1, x, 510 + d, 48, "black", "#FFFFFF", a)
            text_mid(c, s2, x, 568 + d, 28, "bold", "#FFFFFF", a)
        text_mid(c, "+", W / 2, 530, 70, "black", INK, ep(t, C["08.d"], 0.4) * a1)
        pill(c, "classe I, mas a dependência NÃO é presumida!", W / 2, 720, RED, size=32,
             a=ep(t, C["08.e"], 0.5) * a1, anchor="center")
    a2 = ep(t, C["08.f"], 0.4)
    if a2 > 0:
        text(c, "E o menor sob GUARDA?", W / 2, 270, 52, "black", INK, a2)
        for k, (cue, top, s1, s2, col, ok) in enumerate((
                ("08.g", "TEXTO DA LEI", "NÃO consta do §2º", "retirado em 1997 (Lei 9.528/1997)", RED, False),
                ("08.h", "TRIBUNAIS", "direito reconhecido", "entendimento jurisprudencial", PRES, True))):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            x = 570 + k * 780
            card(c, x - 350, 340 + d, 700, 280, a)
            text(c, top, x, 400 + d, 30, "black", col, a, tracking=1.5)
            text(c, s1, x, 490 + d, 46, "black", INK, a)
            text(c, s2, x, 560 + d, 28, "bold", GRAY, a)
            check_icon(c, x + 300, 390 + d, 24, a, col, "check" if ok else "x")
        pill(c, "leia o COMANDO: texto da lei ou entendimento dos tribunais?", W / 2, 740, ASSIST, size=30,
             a=ep(t, C["08.i"], 0.5), anchor="center")


def b_prova(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 16, §5º", "A PROVA", PREST)
    text(c, "união estável e dependência econômica", W / 2, 245, 34, "bold", GRAY, ep(t, B["start"] + 0.3, 0.5))
    aa = ep(t, C["09.a"], 0.4)
    if aa > 0:
        rrect(c, 220, 280, 1480, 100, 22, mix("#FFFFFF", PREST, 0.08), aa)
        check_icon(c, 280, 330, 24, aa, PREST)
        text_mid(c, "início de PROVA MATERIAL contemporânea dos fatos", 980, 330, 40, "black", INK, aa)
    ab = ep(t, C["09.b"], 0.6)
    if ab > 0:
        x0, x1, y = 360, 1420, 480
        rrect(c, x0, y - 26, (x1 - x0) * ab, 52, 14, PREST, ab)
        text_mid(c, "até 24 MESES", (x0 + x1) / 2, y, 34, "black", "#FFFFFF", ep(t, C["09.b"] + 0.4, 0.4))
        line(c, x1 + 20, y - 50, x1 + 20, y + 50, RED, ab, 6)
        text(c, "óbito / prisão", x1 + 40, y + 12, 34, "black", RED, ab, align="left")
    ac = ep(t, C["09.c"], 0.4)
    ok_x(c, "prova EXCLUSIVAMENTE testemunhal", 640, 610, False, ac, 32)
    pill(c, "salvo força maior ou caso fortuito", 1300, 610, INK, size=28, a=ep(t, C["09.d"], 0.4), anchor="center")
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        ok_x(c, "testemunha PODE", 620, 740, True, ae, 32)
        ok_x(c, "SÓ testemunha NÃO", 1260, 740, False, ep(t, C["09.e"] + 1.0, 0.4), 32)


def b_perda(c, t, C, B):
    frame(c, t, B["start"], "DECRETO 3.048 · ART. 17", "A PERDA DA CONDIÇÃO", RED)
    rows = [("10.a", "filho e irmão: aos 21 ANOS", "salvo inválido / deficiência", C1, None),
            ("10.b", "prorrogação por FACULDADE?", "NÃO EXISTE", RED, None),
            ("10.d", "cônjuge: SEPARAÇÃO ou DIVÓRCIO", "salvo pensão alimentícia", C2, "10.e"),
            ("10.f", "todos: cessação da invalidez ou falecimento", "", INK, None)]
    for k, (cue, s, res, col, cr) in enumerate(rows):
        a = ep(t, C[cue], 0.4)
        ra = ep(t, C[cr] if cr else C[cue] + (0.3 if k == 1 else 1.4), 0.4)
        rowbox(c, s, 250 + k * 132, a, res or None, col, ra, 36)
    pill(c, "“até os 24, se universitário” é regra do IMPOSTO DE RENDA, não do INSS", W / 2, 790, ASSIST, size=28,
         a=ep(t, C["10.c"], 0.5), anchor="center")


def b_emancipacao(c, t, C, B):
    frame(c, t, B["start"], "PEGADINHA DE OURO", "A EMANCIPAÇÃO", RED)
    aa = ep(t, C["11.a"], 0.4)
    if aa > 0:
        text(c, "EMANCIPOU?", 600, 290, 64, "black", INK, aa)
        chip(c, "PERDE", 1080, 270, RED, ep(t, C["11.a"] + 0.6, 0.4), 50, 300)
        pill(c, "AINDA QUE INVÁLIDO", 1290, 270, INK, size=32, a=ep(t, C["11.b"], 0.4), bounds=(0, 1920))
    ac, dc = rise(t, C["11.c"])
    if ac > 0:
        rrect(c, 220, 370 + dc, 1480, 100, 22, "#F7F7F5", ac)
        text(c, "o CASAMENTO emancipa: filho de 20 anos que casou", 260, 434 + dc, 38, "black", INK, ac, align="left")
        pill(c, "PERDEU", 1670, 420 + dc, RED, size=30, a=ac, anchor="right", bounds=(0, 1920))
    ad, dd = rise(t, C["11.d"])
    if ad > 0:
        rrect(c, 220, 500 + dd, 1480, 170, 24, mix("#FFFFFF", PRES, 0.10), ad, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(220, 500 + dd, 14, 170), paint(PRES, ad))
        text(c, "EXCEÇÃO NO DECRETO", 270, 550 + dd, 28, "black", PRES, ad, align="left", tracking=1.5)
        ae = ep(t, C["11.e"], 0.4)
        text(c, "emancipação por COLAÇÃO DE GRAU em curso superior", 270, 620 + dd, 38, "black", INK, ae, align="left")
        pill(c, "NÃO PERDE", 1670, 585 + dd, PRES, size=30, a=ep(t, C["11.e"] + 2.0, 0.4), anchor="right",
             bounds=(0, 1920))
    pill(c, "confira no texto atualizado do Decreto 3.048, art. 17 · ela CAI", W / 2, 770, ASSIST, size=28,
         a=ep(t, C["11.f"], 0.5), anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 160, 1520, 700)
    items = [("12.p1", "12.r1", "havendo cônjuge e pais, o benefício é rateado entre todos", False,
              "classes excludentes: os pais não recebem nada"),
             ("12.p2", "12.r2", "a dependência econômica dos pais é presumida", False, "é COMPROVADA"),
             ("12.p3", "12.r3", "o filho universitário é dependente até os 24 anos", False, "não há prorrogação por estudo"),
             ("12.p4", "12.r4", "o ex-cônjuge que recebia pensão alimentícia mantém a condição", True,
              "a pensão alimentícia mantém o vínculo")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 250 + k * 150 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 50, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 60, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_ce(c, t, C, B):
    ce(c, t, C, "13.e", "13.r", "13.x",
       ["O enteado e o menor tutelado equiparam-se a filho", "mediante declaração do segurado, sendo sua",
        "dependência econômica presumida por integrarem", "a primeira classe."],
       "ERRADO", False, "exige declaração E comprovação da dependência econômica", "ART. 16, §2º", size=40)


CASO = [("14.a", "14.a2", "filho de 23 anos, capaz", "perdeu aos 21", "FORA", RED),
        ("14.b", "14.b2", "a mãe (classe II)", "há classe I", "EXCLUÍDA", RED),
        ("14.c", "14.c2", "esposa + filho de 16 (classe I)", "partes iguais", "50% CADA", PRES)]


def b_caso(c, t, C, B):
    head(c, t, B["start"], "O CASO DO ANTÔNIO", "PELO MÉTODO", PREST)
    card(c, 200, 160, 1520, 700)
    x = 330
    for k, s in enumerate(("1 · CLASSE", "2 · EXCLUSÃO", "3 · PARTES IGUAIS")):
        ak = ep(t, C["14.m"] + 1.0 * k, 0.4)
        x0, x1 = pill(c, s, x, 250, (C1, RED, PRES)[k], size=30, a=ak, bounds=(0, 1920))
        if k < 2:
            arrow(c, x1 + 18, 250, x1 + 78, 250, GRAY, ak, 4, 12)
        x = x1 + 100
    for k, (cue, cr, s, why, res, col) in enumerate(CASO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 380 + k * 115 + d
        rrect(c, 260, y - 46, 1400, 92, 18, "#F7F7F5", a)
        text(c, s, 300, y + 14, 38, "black", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        text(c, why, 1330, y + 12, 28, "bold", GRAY, ar, align="right")
        pill(c, res, 1640, y, col, size=30, a=ar, anchor="right", bounds=(0, 1920))
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 720, 1320, 100, 22, mix("#FFFFFF", ASSIST, 0.16), ad)
        text_mid(c, "e se o de 23 fosse INVÁLIDO?", 700, 770, 36, "black", INK, ad)
        pill(c, "entraria: 3 partes iguais", 1580, 770, ASSIST, INK, size=30, a=ep(t, C["14.d2"], 0.4), anchor="right",
             bounds=(0, 1920))


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("15.a", "3 classes EXCLUDENTES (art. 16, §1º)"),
            ("15.b", "classe I: cônjuge, companheiro e filho · PRESUMIDA"),
            ("15.c", "classe II: pais · classe III: irmão · COMPROVADA"),
            ("15.d", "dentro da classe: PARTES IGUAIS"),
            ("15.e", "enteado e tutelado: declaração + comprovação"),
            ("15.f", "prova material de até 24 meses · nunca SÓ testemunhal"),
            ("15.g", "21 anos · sem prorrogação por faculdade"),
            ("15.h", "emancipação faz perder, ainda que inválido")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 240 + k * 79 + dy
        check_icon(c, 280, y - 12, 22, a, GREEN)
        text(c, s, 330, y, 34, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["16.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Filiação × inscrição", W / 2, 430, 64, "black", INK, a)
        pill(c, "a diferença que a banca adora cobrar", W / 2, 540, GEST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a,
             anchor="center")
    ap = fw(t, C["16.pdf"], C["16.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["16.pdf"], 0.5)) * 20)
    cta(c, t, C["16.like"], C["16.sub"], C["16.bell"], C["16.com"], C["16.bye"],
        "Você acertou quem recebe a pensão do Antônio?", canal="no Estudativo")


BLOCKS = dict(hook=b_hook, base=b_base, conceito=b_conceito, classes=b_classes, exclusao=b_exclusao,
              presuncao=b_presuncao, filho=b_filho, equiparados=b_equiparados, prova=b_prova, perda=b_perda,
              emancipacao=b_emancipacao, pegadinhas=b_pegadinhas, q_ce=b_q_ce, caso=b_caso, resumo=b_resumo, cta=b_cta)
