"""Visual do vídeo Seguridade 016 — Filiação × inscrição (Lei 8.213, art. 17 e art. 27, II; Decreto 3.048, arts. 18 e 20).
Tema 'seguridade'. Cores: filiação = verde-petróleo (#0F766E) · inscrição = roxo (#4F46E5) · facultativo = âmbar ·
dependente = cinza-escuro. Reaproveita do 012/011/010 (chip, frame, ce, tag, ok_x, pdf_card, rowbox, lei_card)."""
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
ARQUIVO_FINAL = "seguridade_016_filiacao_inscricao.mp4"
CARD_R = (140, 150, 1640, 690)

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
FIL, INS, FAC, DEP, CI = PREST, GEST, ASSIST, "#3A3A3C", "#3A3A3C"


def col_card(c, x, y, w, h, col, a, d=0.0):
    """cartão claro com faixa colorida à esquerda"""
    rrect(c, x, y + d, w, h, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y + d, 14, h), paint(col, a))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 16 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    fatos = [("01.a", "vendedor AUTÔNOMO", "há 3 anos · atende pessoas físicas", PREST, None),
             ("01.b", "nunca se INSCREVEU", "no INSS", GEST, "x"),
             ("01.c", "nunca RECOLHEU", "nem um centavo", ASSIST, "x")]
    for k, (cue, s1, s2, col, ic) in enumerate(fatos):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 140 + k * 560
        rrect(c, x, 270 + d, 520, 170, 24, "#FFFFFF", a, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x, 270 + d, 14, 170), paint(col, a))
        text(c, s1, x + 50, 340 + d, 38, "black", INK, a, align="left")
        text(c, s2, x + 50, 395 + d, 26, "bold", GRAY, a, align="left")
        if ic:
            check_icon(c, x + 470, 386 + d, 22, a, RED, "x")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "O LUCAS ESTÁ FILIADO AO RGPS?", W / 2, 560, FIL, ad, 46, 1040)
    ae = ep(t, C["01.e"], 0.5) * (1 - ep(t, C["01.f"] + 1.0, 0.4))
    pill(c, "muita gente responde: NÃO (nunca se cadastrou nem pagou)", W / 2, 690, GRAY, size=30, a=ae, anchor="center")
    pill(c, "resolvemos juntos no fim da aula", W / 2, 690, ASSIST, size=30, a=ep(t, C["01.f"] + 1.0, 0.4),
         anchor="center")


def b_base(c, t, C, B):
    frame(c, t, B["start"], "CAMPEÃO DE PEGADINHAS", "FILIAÇÃO × INSCRIÇÃO", FIL)
    aa = ep(t, C["02.a"], 0.5)
    if aa > 0:
        # na cue b as duas palavras trocam de lugar e voltam
        tb = clamp((t - C["02.b"]) / 1.6) if t > C["02.b"] else 0.0
        sw = ease_io(clamp(tb * 2)) - ease_io(clamp(tb * 2 - 1))
        x1, x2 = 560 + 800 * sw, 1360 - 800 * sw
        lift = 60 * (1 - (2 * sw - 1) ** 2) if 0 < sw < 1 else 0
        chip(c, "FILIAÇÃO", x1, 290 - lift, FIL, aa, 50, 520)
        chip(c, "INSCRIÇÃO", x2, 290 + lift, INS, aa, 50, 520)
        text_mid(c, "×", W / 2, 290, 70, "black", GRAY, aa * (1 - min(1, 4 * sw * (1 - sw))))
    pill(c, "a banca TROCA uma pela outra", W / 2, 410, RED, size=30, a=ep(t, C["02.b"], 0.4), anchor="center")
    for k, (cue, s, sub) in enumerate((("02.c", "LEI 8.213/1991 · ART. 17", "a lei"),
                                       ("02.d", "DECRETO 3.048/1999 · ARTS. 18 E 20", "as definições"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 760
        rrect(c, x, 480 + d, 720, 130, 22, PREST, a, shadow=True)
        text_mid(c, s, x + 360, 530 + d, 34, "black", "#FFFFFF", a)
        text_mid(c, sub, x + 360, 580 + d, 26, "bold", "#FFFFFF", a)
    pill(c, "conceitos estáveis · a NUMERAÇÃO do Decreto já mudou: confira no texto compilado", W / 2, 730, RED,
         size=26, a=ep(t, C["02.e"], 0.5), anchor="center")


def b_academia(c, t, C, B):
    frame(c, t, B["start"], "PENSE NUMA ACADEMIA", "VÍNCULO × CADASTRO", FIL)
    for k, (cue, top, big, l1, l2, col) in enumerate((
            ("03.a", "FILIAÇÃO", "o VÍNCULO", "começou a treinar: está dentro", "é o FATO → direitos e obrigações", FIL),
            ("03.b", "INSCRIÇÃO", "o CADASTRO", "ficha · documentos · sistema", "é um ATO FORMAL", INS))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 800
        col_card(c, x, 210, 720, 360, col, a, d)
        pill(c, top, x + 60, 270 + d, col, size=30, a=a, bounds=(0, 1920))
        text(c, big, x + 60, 380 + d, 60, "black", col, a, align="left")
        text(c, l1, x + 60, 460 + d, 32, "bold", INK, a, align="left")
        text(c, l2, x + 60, 520 + d, 32, "black", INK2, a, align="left")
    ac = ep(t, C["03.c"], 0.5)
    chip(c, "FILIADO sem estar INSCRITO", W / 2, 680, ASSIST, ac, 46, 900)
    pill(c, "acontece com MILHÕES de trabalhadores", W / 2, 800, INK, size=28, a=ep(t, C["03.d"], 0.4), anchor="center")


def b_definicoes(c, t, C, B):
    head(c, t, B["start"], "DECRETO 3.048/1999", "AS DEFINIÇÕES", FIL)
    rf = [(C["04.a"], "“Filiação é o VÍNCULO que se", True), (C["04.a"] + 0.9, "estabelece entre pessoas que", False),
          (C["04.a"] + 1.8, "contribuem para a previdência", False), (C["04.a"] + 2.7, "social e esta, do qual decorrem", False),
          (C["04.b"], "DIREITOS E OBRIGAÇÕES.”", True)]
    lei_card(c, t, rf, 160, 180, 780, 32, FIL, "DECRETO 3.048/1999 · ART. 20")
    ri = [(C["04.c"], "“Inscrição é o ATO pelo qual o", True), (C["04.c"] + 0.9, "segurado é CADASTRADO no RGPS,", True),
          (C["04.d"], "mediante comprovação dos dados", False), (C["04.d"] + 0.9, "pessoais e de outros elementos", False),
          (C["04.d"] + 1.8, "necessários à sua caracterização.”", False)]
    lei_card(c, t, ri, 980, 180, 780, 32, INS, "DECRETO 3.048/1999 · ART. 18")
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        rrect(c, 260, 630, 1400, 110, 24, "#FFFFFF", ae, shadow=True)
        parts = [("FILIAÇÃO = o ", INK), ("FATO", FIL), ("   ·   INSCRIÇÃO = a ", INK), ("FICHA", INS)]
        x = W / 2 - sum(text_w(s, "black", 52) for s, _ in parts) / 2
        for s, col in parts:
            text(c, s, x, 704, 52, "black", col, ae, align="left")
            x += text_w(s, "black", 52)
    pill(c, "filia-se TRABALHANDO · inscreve-se CADASTRANDO", W / 2, 810, ASSIST, size=30, a=ep(t, C["04.f"], 0.4),
         anchor="center")


def b_quando(c, t, C, B):
    frame(c, t, B["start"], "QUANDO OCORRE", "A FILIAÇÃO", FIL)
    aa, da = rise(t, C["05.a"])
    if aa > 0:
        col_card(c, 190, 200, 900, 470, FIL, aa, da)
        pill(c, "OS 5 OBRIGATÓRIOS", 250, 255 + da, FIL, size=28, a=aa, bounds=(0, 1920))
        text(c, "filiação AUTOMÁTICA", 250, 355 + da, 50, "black", FIL, aa, align="left")
        text(c, "pelo exercício da atividade remunerada", 250, 405 + da, 30, "bold", INK2, aa, align="left")
    for k, (cue, s) in enumerate((("05.b", "INSCRIÇÃO"), ("05.c", "PAGAMENTO"), ("05.d", "VONTADE do segurado"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 480 + k * 62 + d
        check_icon(c, 275, y - 12, 20, a, FIL)
        text(c, "independe de ", 310, y, 34, "bold", INK, a, align="left")
        text(c, s, 310 + text_w("independe de ", "bold", 34), y, 34, "black", INK, a, align="left")
    ae = ep(t, C["05.e"], 0.4)
    pill(c, "trabalhou com remuneração = FILIADO", 640, 760, FIL, size=30, a=ae, anchor="center")
    af, df = rise(t, C["05.f"])
    if af > 0:
        col_card(c, 1130, 200, 600, 470, FAC, af, df)
        pill(c, "FACULTATIVO", 1190, 255 + df, FAC, size=28, a=af, bounds=(0, 1920))
        text(c, "não exerce atividade", 1190, 340 + df, 32, "bold", INK2, af, align="left")
        text(c, "obrigatória", 1190, 380 + df, 32, "bold", INK2, af, align="left")
        ag = ep(t, C["05.g"], 0.5)
        if ag > 0:
            rrect(c, 1180, 430 + df, 500, 90, 18, INS, ag)
            text_mid(c, "INSCRIÇÃO", 1430, 475 + df, 40, "black", "#FFFFFF", ag)
            text_mid(c, "+", 1430, 548 + df, 46, "black", INK, ag)
            ag2 = ep(t, C["05.g"] + 1.4, 0.4)
            rrect(c, 1180, 576 + df, 500, 70, 18, FAC, ag2)
            text_mid(c, "1ª CONTRIBUIÇÃO", 1430, 611 + df, 36, "black", INK, ag2)


def b_natureza(c, t, C, B):
    frame(c, t, B["start"], "PONTO DE OURO", "A NATUREZA DA INSCRIÇÃO", ASSIST)
    for k, (cue, who, nat, sub, col) in enumerate((
            ("06.a", "OBRIGATÓRIO", "DECLARATÓRIA", "só DOCUMENTA um vínculo que já existe", FIL),
            ("06.b", "FACULTATIVO", "CONSTITUTIVA", "sem ela, NÃO HÁ vínculo nenhum", FAC))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 780
        col_card(c, x, 190, 740, 250, col, a, d)
        text(c, who, x + 60, 250 + d, 30, "black", GRAY, a, align="left", tracking=1.5)
        text(c, nat, x + 60, 340 + d, 64, "black", col, a, align="left")
        text(c, sub, x + 60, 405 + d, 30, "bold", INK, a, align="left")
    text(c, "as 2 frases que a banca adora são FALSAS", W / 2, 520, 38, "black", RED, ep(t, C["06.c"], 0.4))
    rowbox(c, "“a filiação decorre SEMPRE do exercício de atividade”", 620, ep(t, C["06.d"], 0.4),
           "ERRADO · facultativo", RED, ep(t, C["06.e"], 0.4), 32)
    rowbox(c, "“a filiação depende de PRÉVIA INSCRIÇÃO”", 750, ep(t, C["06.f"], 0.4),
           "ERRADO · obrigatórios", RED, ep(t, C["06.g"], 0.4), 32)


QUEM = [("07.a", 0.0, "EMPREGADO", "o EMPREGADOR, na admissão", PREST),
        ("07.b", 0.0, "EMPREGADO DOMÉSTICO", "o EMPREGADOR DOMÉSTICO", GEST),
        ("07.c", 0.0, "TRABALHADOR AVULSO", "o SINDICATO ou o OGMO", ASSIST),
        ("07.d", 0.0, "CONTRIBUINTE INDIVIDUAL", "o PRÓPRIO segurado", CI),
        ("07.d", 0.8, "SEGURADO ESPECIAL", "o PRÓPRIO segurado *", "#16A36A"),
        ("07.d", 1.6, "FACULTATIVO", "o PRÓPRIO segurado", FAC)]


def b_quem(c, t, C, B):
    frame(c, t, B["start"], "QUEM FAZ", "A INSCRIÇÃO", INS)
    for k, (cue, dt, who, por, col) in enumerate(QUEM):
        a, d = rise(t, C[cue] + dt)
        if a <= 0:
            continue
        y = 230 + k * 84 + d
        rrect(c, 220, y - 36, 1480, 72, 16, "#F7F7F5", a)
        c.drawRect(skia.Rect.MakeXYWH(220, y - 36, 12, 72), paint(col, a))
        text(c, who, 270, y + 12, 34, "black", INK, a, align="left")
        arrow(c, 880, y, 960, y, GRAY, a, 4, 14)
        text(c, por, 1000, y + 12, 34, "bold" if "PRÓPRIO" in por else "black", INS if "PRÓPRIO" not in por else INK2,
             a, align="left")
    pill(c, "* segurado especial: sistemática PRÓPRIA de cadastro", W / 2, 780, "#16A36A", size=28,
         a=ep(t, C["07.e"], 0.4), anchor="center")


def b_dependente(c, t, C, B):
    frame(c, t, B["start"], "ATENÇÃO", "E O DEPENDENTE?", DEP)
    aa, da = rise(t, C["08.a"])
    if aa > 0:
        col_card(c, 220, 190, 700, 250, FIL, aa, da)
        text(c, "SEGURADO", 280, 255 + da, 40, "black", FIL, aa, align="left")
        for k, s in enumerate(("FILIA-SE", "INSCREVE-SE")):
            check_icon(c, 300, 320 + k * 60 + da, 20, aa, GREEN)
            text(c, s, 340, 332 + k * 60 + da, 34, "black", INK, aa, align="left")
    ab, db = rise(t, C["08.b"])
    if ab > 0:
        col_card(c, 1000, 190, 700, 250, DEP, ab, db)
        text(c, "DEPENDENTE", 1060, 255 + db, 40, "black", DEP, ab, align="left")
        check_icon(c, 1080, 320 + db, 20, ab, RED, "x")
        text(c, "NÃO se filia", 1120, 332 + db, 34, "black", RED, ab, align="left")
        ad = ep(t, C["08.d"], 0.4)
        check_icon(c, 1080, 380 + db, 20, ad, GREEN)
        text(c, "apenas SE INSCREVE", 1120, 392 + db, 34, "black", INK, ad, align="left")
    pill(c, "relação DERIVADA", 1350, 470, DEP, size=26, a=ep(t, C["08.c"], 0.4), anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        text(c, "inscrição do dependente: em regra no REQUERIMENTO DO BENEFÍCIO, não antes", W / 2, 560, 34, "black",
             INK, ad)
    ae = ep(t, C["08.e"], 0.5)
    chip(c, "não precisa de cadastro em vida do segurado para a PENSÃO", W / 2, 660, GREEN, ae, 34, 1300)
    pill(c, "confira o art. 17 da Lei 8.213 · alterado em 2019 (Lei 13.846/2019)", W / 2, 790, RED, size=26,
         a=ep(t, C["08.f"], 0.4), anchor="center")


def b_derrubam(c, t, C, B):
    frame(c, t, B["start"], "PONTOS QUE DERRUBAM", "INDEPENDE DE RECOLHIMENTO", RED)
    aa = ep(t, C["09.a"], 0.5)
    chip(c, "filiação do obrigatório INDEPENDE DE RECOLHIMENTO", W / 2, 250, FIL, aa, 38, 1300)
    ab, db = rise(t, C["09.b"])
    if ab > 0:
        card(c, 260, 330 + db, 560, 150, ab)
        text(c, "EMPRESA", 540, 390 + db, 38, "black", INK, ab)
        text(c, "nunca recolheu", 540, 440 + db, 30, "bold", RED, ab)
        check_icon(c, 780, 365 + db, 20, ab, RED, "x")
        arrow(c, 850, 405 + db, 1070, 405 + db, GRAY, ab, 5, 18)
        card(c, 1100, 330 + db, 560, 150, ab)
        text(c, "EMPREGADO", 1380, 390 + db, 38, "black", INK, ab)
        text(c, "continua FILIADO", 1380, 440 + db, 30, "black", GREEN, ab)
        check_icon(c, 1620, 365 + db, 20, ab, GREEN)
    pill(c, "recolher é obrigação DA EMPRESA · a omissão NÃO prejudica o empregado", W / 2, 540, PREST, size=28,
         a=ep(t, C["09.c"], 0.4), anchor="center")
    ad = ep(t, C["09.d"], 0.4)
    text(c, "inscrição NÃO CRIA atividade", W / 2, 640, 40, "black", INS, ad)
    rowbox(c, "inscrever-se SEM TRABALHAR", 740, ep(t, C["09.e"], 0.4), "NÃO GERA FILIAÇÃO OBRIGATÓRIA", RED,
           ep(t, C["09.e"] + 1.0, 0.4), 36)


TRES = [("10.a", "FILIAÇÃO", "o INGRESSO", "no sistema", "esta aula", FIL),
        ("10.b", "QUALIDADE DE SEGURADO", "a MANUTENÇÃO", "do vínculo", "Aula 17", GEST),
        ("10.c", "CARÊNCIA", "o nº MÍNIMO", "de contribuições", "Aula 18", ASSIST)]


def b_tres(c, t, C, B):
    frame(c, t, B["start"], "NÃO CONFUNDA", "TRÊS COISAS DIFERENTES", INK)
    for k, (cue, top, big, sub, aula, col) in enumerate(TRES):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 520
        col_card(c, x, 190, 480, 240, col, a, d)
        text(c, top, x + 250, 240 + d, 26, "black", col, a, tracking=1.0)
        text(c, big, x + 250, 320 + d, 46, "black", INK, a)
        text(c, sub, x + 250, 365 + d, 28, "bold", INK2, a)
        pill(c, aula, x + 250, 410 + d, col, size=22, a=a, anchor="center")
    ad = ep(t, C["10.d"], 0.4)
    if ad > 0:
        text(c, "perder a QUALIDADE de segurado:", 300, 520, 34, "black", INK, ad, align="left")
        ok_x(c, "NÃO desfaz a filiação", 1080, 508, False, ad, 28)
        ok_x(c, "NÃO apaga o tempo de contribuição", 1080, 578, False, ep(t, C["10.e"], 0.4), 28)
    af = ep(t, C["10.f"], 0.4)
    if af > 0:
        etapas = [("FILIAÇÃO", FIL), ("QUALIDADE", GEST), ("CARÊNCIA", ASSIST), ("BENEFÍCIO", GREEN)]
        for k, (s, col) in enumerate(etapas):
            ak = ep(t, C["10.f"] + 0.6 * k, 0.35)
            cx = 360 + k * 400
            chip(c, s, cx, 720, col, ak, 34, 320)
            if k:
                arrow(c, cx - 240, 720, cx - 168, 720, INK, ak, 5, 16)
        pill(c, "a linha do tempo do segurado", W / 2, 810, INK, size=24, a=ep(t, C["10.f"] + 2.6, 0.4), anchor="center")


def b_retroativo(c, t, C, B):
    frame(c, t, B["start"], "FACULTATIVO", "PODE COMPRAR O PASSADO?", FAC)
    a0 = ep(t, C["11.t"], 0.4)
    text(c, "recolher período ANTERIOR à inscrição?", W / 2, 240, 40, "black", INK, a0)
    if a0 > 0:
        x0, xm, x1, y = 300, 960, 1620, 380
        ab = ep(t, C["11.b"], 0.6)
        ac = ep(t, C["11.c"], 0.4)
        line(c, x0, y, xm, y, mix(LIGHT, RED, 0.6 * ac), a0, 10)
        line(c, xm, y, xm + (x1 - xm) * ab, y, FIL, ab, 10)
        line(c, xm + (x1 - xm) * ab, y, x1, y, LIGHT, a0, 10)
        arrow(c, x1, y, x1 + 60, y, INK, a0, 4, 14)
        c.drawCircle(xm, y, 22, paint(FAC, a0))
        text(c, "INSCRIÇÃO + 1º PAGAMENTO", xm, y - 45, 28, "black", FAC, a0)
        text(c, "o vínculo NASCE aqui →", (xm + x1) / 2 + 20, y + 60, 30, "black", FIL, ab)
        text(c, "sem vínculo anterior", (x0 + xm) / 2, y + 60, 30, "black", RED, ac)
        if ac > 0:
            check_icon(c, (x0 + xm) / 2, y, 22, ac, RED, "x")
    aa = ep(t, C["11.a"], 0.5)
    chip(c, "EM REGRA, NÃO", 520, 540, RED, aa, 40, 520)
    pill(c, "nada a amparar recolhimento RETROATIVO", 1260, 540, RED, size=26, a=ep(t, C["11.c"] + 1.2, 0.4),
         anchor="center")
    ad, dd = rise(t, C["11.d"])
    if ad > 0:
        rrect(c, 240, 620 + dd, 1440, 100, 22, PREST, ad, shadow=True)
        text_mid(c, "LEI 8.213 · ART. 27, II · carência: a partir do 1º PAGAMENTO SEM ATRASO", W / 2, 670 + dd, 34,
                 "black", "#FFFFFF", ad)
    pill(c, "há EXCEÇÕES no regulamento: confira antes de afirmar", W / 2, 790, RED, size=26,
         a=ep(t, C["11.e"], 0.4), anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 160, 1520, 700)
    items = [("12.p1", "12.r1", "INSCRIÇÃO é o vínculo entre o segurado e a previdência", False,
              "esse é o conceito de FILIAÇÃO"),
             ("12.p2", "12.r2", "o dependente se FILIA ao RGPS na mesma data do segurado", False,
              "dependente não se filia, só se INSCREVE"),
             ("12.p3", "12.r3", "o dependente deve se inscrever PREVIAMENTE, sob pena de perder a pensão", False,
              "em regra, no REQUERIMENTO DO BENEFÍCIO"),
             ("12.p4", "12.r4", "para o facultativo, a inscrição tem natureza CONSTITUTIVA", True, "sem ela, não há vínculo")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 250 + k * 150 + dy
        text(c, "“" + frase + "”", 260, y, 32, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 50, GREEN if ok else RED, size=28, a=ar, anchor="right",
             bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 60, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_ce(c, t, C, B):
    ce(c, t, C, "13.e", "13.r", "13.x",
       ["O empregado cuja empresa deixa de recolher as", "contribuições previdenciárias não se considera",
        "filiado ao RGPS naquele período."],
       "ERRADO", False, "a filiação independe do recolhimento, que é responsabilidade da EMPRESA", "FILIAÇÃO", size=42)


def b_caso(c, t, C, B):
    head(c, t, B["start"], "O CASO DO LUCAS", "RESOLVIDO", FIL)
    card(c, 200, 160, 1520, 700)
    aa = ep(t, C["14.a"], 0.4)
    text(c, "trabalha por CONTA PRÓPRIA, com remuneração", 260, 250, 36, "black", INK, aa, align="left")
    ab, db = rise(t, C["14.b"])
    if ab > 0:
        chip(c, "CONTRIBUINTE INDIVIDUAL · OBRIGATÓRIO", 760, 370 + db, CI, ab, 34, 900)
    ac = ep(t, C["14.c"], 0.4)
    if ac > 0:
        check_icon(c, 280, 466, 22, ac, GREEN)
        text(c, "FILIADO desde o 1º dia da atividade", 320, 480, 36, "black", GREEN, ac, align="left")
        text(c, "mesmo sem inscrição e sem recolhimento", 1000, 480, 28, "bold", GRAY, ep(t, C["14.c"] + 1.6, 0.4),
             align="left")
    ad = ep(t, C["14.d"], 0.4)
    if ad > 0:
        check_icon(c, 280, 546, 22, ad, RED, "x")
        text(c, "facultativo? NÃO pode: exerce atividade obrigatória", 320, 560, 34, "black", INK, ad, align="left")
    ae, de = rise(t, C["14.e"])
    if ae > 0:
        rrect(c, 260, 610 + de, 1400, 80, 18, mix("#FFFFFF", RED, 0.12), ae)
        text_mid(c, "mas: filiado ≠ direito imediato a benefício", W / 2, 650 + de, 36, "black", RED, ae)
    for k, s in enumerate(("comprovar a atividade", "recolher o que deve", "qualidade + carência")):
        ak = ep(t, C["14.f"] + 1.1 * k, 0.4)
        pill(c, s, 470 + k * 490, 770, (PREST, ASSIST, GEST)[k], size=28, a=ak, anchor="center")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("15.a", "FILIAÇÃO = vínculo (direitos e obrigações) · INSCRIÇÃO = cadastro"),
            ("15.b", "obrigatórios: filiação AUTOMÁTICA · inscrição DECLARATÓRIA"),
            ("15.c", "facultativo: INSCRIÇÃO + 1ª CONTRIBUIÇÃO · inscrição CONSTITUTIVA"),
            ("15.d", "só o segurado se filia · dependente só se INSCREVE (no requerimento)"),
            ("15.e", "a filiação é o FATO · a inscrição é a FICHA")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 270 + k * 112 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 34, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["16.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Qualidade de segurado", W / 2, 430, 64, "black", INK, a)
        pill(c, "e período de graça", W / 2, 540, GEST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a, anchor="center")
    ap = fw(t, C["16.pdf"], C["16.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["16.pdf"], 0.5)) * 20)
    cta(c, t, C["16.like"], C["16.sub"], C["16.bell"], C["16.com"], C["16.bye"],
        "Você achava que o Lucas não estava filiado?", canal="no Estudativo")


BLOCKS = dict(hook=b_hook, base=b_base, academia=b_academia, definicoes=b_definicoes, quando=b_quando,
              natureza=b_natureza, quem=b_quem, dependente=b_dependente, derrubam=b_derrubam, tres=b_tres,
              retroativo=b_retroativo, pegadinhas=b_pegadinhas, q_ce=b_q_ce, caso=b_caso, resumo=b_resumo, cta=b_cta)
