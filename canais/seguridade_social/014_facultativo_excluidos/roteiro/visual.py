"""Visual do vídeo Seguridade 014 — Facultativo, excluídos e o "quem é quem" (Lei 8.213, arts. 12 e 13; Decreto 3.048, art. 11;
CF, art. 201, §5º). Tema 'seguridade'.
Cores: facultativo = azul (#0284C7) · empregado = verde-petróleo · doméstico = roxo · contribuinte individual = cinza-escuro ·
avulso = âmbar · segurado especial = verde · regime próprio / excluídos = cinza-azulado.
Reaproveita do 013 (numero), do 012 (rowbox), do 011 (chip, frame, lei_card) e do 010 (ce, tag, ok_x, pdf_card)."""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "013_segurado_especial" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v013", _p)
V13 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V13)
motor.set_theme("seguridade")
chip, frame, ce, tag, ok_x, pdf_card, rowbox, lei_card, numero = (V13.chip, V13.frame, V13.ce, V13.tag, V13.ok_x,
                                                                   V13.pdf_card, V13.rowbox, V13.lei_card, V13.numero)

MARCA = ""
ARQUIVO_FINAL = "seguridade_014_facultativo_excluidos.mp4"
CARD_R = (140, 150, 1640, 690)

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
EMP, DOM, AVU, CI, ESP = PREST, GEST, ASSIST, "#3A3A3C", "#16A36A"
FAC, RPPS = "#0284C7", "#64748B"


def caixa(c, x, y, w, h, col, a, top, l1, l2="", fill=0.08):
    """cartão com faixa colorida à esquerda, título colorido e 1-2 linhas"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, fill), a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, 14, h), paint(col, a))
    text(c, top, x + 50, y + 58, 28, "black", col, a, align="left", tracking=1.5)
    text(c, l1, x + 50, y + 118, 40, "black", INK, a, align="left")
    if l2:
        text(c, l2, x + 50, y + 168, 28, "bold", GRAY, a, align="left")


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 14 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    for k, (cue, mes, s1, s2, col) in enumerate((("01.a", "JANEIRO", "dona de casa", "contribui como FACULTATIVA", FAC),
                                                  ("01.b", "JULHO", "contratada por empresa", "CARTEIRA ASSINADA", EMP))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 860
        caixa(c, x, 270 + d, 700, 210, col, a, mes, s1, s2)
    aar = ep(t, C["01.b"] + 0.3, 0.5)
    if aar > 0:
        arrow(c, 900, 375, 1020, 375, INK, aar, 6, 20, progress=aar)
    for k, (cue, s) in enumerate((("01.c", "continua facultativa?"), ("01.d", "as DUAS filiações?"),
                                  ("01.e", "pode ESCOLHER?"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        cx = 420 + k * 540
        rrect(c, cx - 240, 560 + d, 480, 110, 22, "#FFFFFF", a, shadow=True)
        text_mid(c, s, cx, 615 + d, 36, "black", INK, a)
    pill(c, "resolvemos juntos no fim da aula", W / 2, 790, ASSIST, size=30, a=ep(t, C["01.f"], 0.5), anchor="center")


CATS = [("EMPREGADO", EMP), ("DOMÉSTICO", DOM), ("C. INDIVIDUAL", CI), ("AVULSO", AVU), ("ESPECIAL", ESP),
        ("FACULTATIVO", FAC)]


def b_base(c, t, C, B):
    frame(c, t, B["start"], "FECHANDO O BLOCO DE SEGURADOS", "QUEM ENTRA E QUEM FICA FORA", PREST)
    a0 = ep(t, C["02.t"], 0.5)
    aa = ep(t, C["02.a"], 0.4)
    for k, (s, col) in enumerate(CATS):
        cx = 330 + k * 252
        if k < 5:
            a = a0 * ep(t, C["02.t"] + 0.12 * k, 0.4)
            badge_num(c, k + 1, cx, 260, a, 30, bg=mix(col, "#FFFFFF", 0.35 * aa))
            text(c, s, cx, 330, 24, "black", mix(col, GRAY, 0.5 * aa), a)
        else:
            sc = 1 + 0.15 * ease_back(aa)
            badge_num(c, 6, cx, 260, aa, int(30 * sc), bg=FAC)
            text(c, s, cx, 330, 26, "black", FAC, aa)
    ab = ep(t, C["02.b"], 0.4)
    for k, (cue, top, l1, l2, col) in enumerate((
            ("02.a", "O 6º SEGURADO", "FACULTATIVO", "LEI 8.213 · ART. 13 · DECRETO 3.048 · ART. 11", FAC),
            ("02.b", "QUEM ESTÁ FORA", "EXCLUÍDOS DO RGPS", "LEI 8.213 · ART. 12", RPPS))):
        a, d = rise(t, C[cue])
        caixa(c, 200 + k * 780, 400 + d, 740, 210, col, a, top, l1, l2)
    pill(c, "e no fim: a tabela do QUEM É QUEM", W / 2, 750, GREEN, size=32, a=ep(t, C["02.c"], 0.5), anchor="center")


def b_conceito(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 13", "O CONCEITO", FAC)
    aa, da = rise(t, C["03.a"])
    if aa > 0:
        rrect(c, 220, 215 + da, 1480, 130, 24, mix("#FFFFFF", FAC, 0.07), aa, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(220, 215 + da, 12, 130), paint(FAC, aa))
        seq(c, [("filia-se ao RGPS ", INK), ("MEDIANTE CONTRIBUIÇÃO,", FAC)], 270, 270 + da, 40, aa, align="left", gap=0)
        seq(c, [("desde que ", INK), ("NÃO", RED), (" incluído no art. 11 (não é obrigatório)", INK)], 270, 322 + da, 34,
            aa, align="left", gap=0)
    ab = ep(t, C["03.b"], 0.4)
    text(c, "OS 3 REQUISITOS", W / 2, 410, 30, "black", GRAY, ab, tracking=2)
    for k, (cue, s1, s2) in enumerate((("03.r1", "IDADE", "mínima"), ("03.r2", "CONTRIBUIÇÃO", "filia-se pagando"),
                                       ("03.r3", "NÃO OBRIGATÓRIO", "sem atividade do art. 11"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        cx = 470 + k * 490
        rrect(c, cx - 220, 440 + d, 440, 170, 22, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, cx - 220 + 40, 440 + 40 + d, a, 24, bg=FAC)
        text(c, s1, cx + 10, 530 + d, 40 if k < 2 else 34, "black", FAC, a)
        text(c, s2, cx + 10, 580 + d, 28, "bold", GRAY, a)
    ac, ad = ep(t, C["03.c"], 0.4), ep(t, C["03.d"], 0.4)
    pill(c, "facultativo: quem PODE não estar", 950, 740, FAC, size=32, a=ac, anchor="right", bounds=(0, 1920))
    pill(c, "obrigatório: quem NÃO PODE escolher", 970, 740, INK, size=32, a=ad, anchor="left", bounds=(0, 1920))


def b_idade(c, t, C, B):
    frame(c, t, B["start"], "A PEGADINHA MAIS SOFISTICADA", "14 OU 16 ANOS?", RED)
    aa = ep(t, C["04.a"], 0.45)
    numero(c, "14", "anos", 420, 330, aa, RPPS, 210, 210, 96)
    text(c, "LEI 8.213 · ART. 13", 420, 475, 28, "black", INK, aa)
    text(c, "texto de 1991", 420, 515, 26, "bold", GRAY, aa)
    pill(c, "NUNCA ATUALIZADO", 560, 230, RED, size=24, a=ep(t, C["04.b"], 0.4), anchor="left", bounds=(0, 1920))
    ac, dc = rise(t, C["04.c"])
    if ac > 0:
        arrow(c, 600, 330, 1240, 330, LIGHT, ac, 6, 20, progress=ac)
        text(c, "EC 20/1998", W / 2, 300, 38, "black", PREST, ac)
        text(c, "trabalho a partir de 16 · 14 só aprendiz", W / 2, 380, 28, "bold", INK2, ac)
    ad = ep(t, C["04.d"], 0.45)
    numero(c, "16", "anos", 1500, 330, ad, FAC, 210, 210, 96)
    text(c, "DECRETO 3.048 · ART. 11", 1500, 475, 28, "black", INK, ad)
    text(c, "regra aplicável", 1500, 515, 26, "bold", GRAY, ad)
    ae = ep(t, C["04.e"], 0.4)
    text(c, "COMO RESPONDER", W / 2, 585, 28, "black", GRAY, ae, tracking=2)
    for k, (cue, s, n, col) in enumerate((("04.f", "literalidade da lei", "14", RPPS),
                                          ("04.g", "Decreto / aplicável", "16", FAC),
                                          ("04.h", "sem especificação", "16", FAC))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        cx = 470 + k * 490
        rrect(c, cx - 225, 615 + d, 450, 120, 20, mix("#FFFFFF", col, 0.10), a)
        text(c, s, cx - 195, 685 + d, 28, "bold", INK, a, align="left")
        text_mid(c, n, cx + 180, 675 + d, 56, "black", col, ep(t, C[cue] + (1.0 if k < 2 else 1.2), 0.4))
    pill(c, "ISSO CAI", 1650, 785, ASSIST, size=28, a=ep(t, C["04.i"], 0.4), anchor="right", bounds=(0, 1920))


def b_quem(c, t, C, B):
    frame(c, t, B["start"], "QUEM PODE E QUEM NÃO PODE", "SER FACULTATIVO", FAC)
    a0 = ep(t, C["05.t"], 0.4)
    pill(c, "PODE", 220, 225, GREEN, size=30, a=a0, bounds=(0, 1920))
    for k, (cue, s, sub) in enumerate((("05.a", "dona de casa", ""), ("05.b", "estudante maior de 16", ""),
                                       ("05.c", "desempregado", "que perdeu a qualidade de segurado"),
                                       ("05.d", "síndico NÃO remunerado", "sem remuneração, não é contribuinte individual"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 320 + k * 120 + d
        check_icon(c, 245, y - 14, 24, a, GREEN)
        text(c, s, 290, y, 38, "black", INK, a, align="left")
        if sub:
            text(c, sub, 290, y + 42, 24, "bold", GRAY, a, align="left")
    ae = ep(t, C["05.e"], 0.4)
    if ae > 0:
        line(c, 1050, 210, 1050, 800, LIGHT, ae, 3)
    pill(c, "NÃO PODE", 1100, 225, RED, size=30, a=ae, bounds=(0, 1920))
    for k, (cue, s, sub) in enumerate((("05.f", "quem exerce atividade", "que gera filiação OBRIGATÓRIA"),
                                       ("05.g", "participante de", "REGIME PRÓPRIO"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 200 + d
        rrect(c, 1100, y - 60, 620, 150, 20, mix("#FFFFFF", RED, 0.08), a)
        check_icon(c, 1140, y - 10, 22, a, RED, "x")
        text(c, s, 1180, y, 32, "bold", INK, a, align="left")
        text(c, sub, 1180, y + 50, 32, "black", RED, a, align="left")


def b_vedacao(c, t, C, B):
    frame(c, t, B["start"], "CF · ART. 201, §5º", "A VEDAÇÃO", RED)
    lei_card(c, t, [(C["06.a"], "é VEDADA a filiação ao regime geral,", True),
                    (C["06.b"], "na qualidade de segurado FACULTATIVO,", False),
                    (C["06.c"], "de pessoa participante de REGIME PRÓPRIO.", False)],
             y=210, size=40, col=RED, src="CONSTITUIÇÃO FEDERAL · ART. 201, §5º")
    ad = ep(t, C["06.d"], 0.4)
    pill(c, "a vedação é SÓ como facultativo", W / 2, 575, INK, size=28, a=ad, anchor="center")
    ok_x(c, "regime próprio + FACULTATIVO no RGPS", W / 2 - 20, 665, False, ad, 30)
    ok_x(c, "regime próprio + atividade privada = OBRIGATÓRIO no RGPS por ela", W / 2 - 20, 760, True,
         ep(t, C["06.e"], 0.4), 30)


def b_filiacao(c, t, C, B):
    frame(c, t, B["start"], "PONTO DE OURO", "A FILIAÇÃO", ASSIST)
    for k, (cue, top, big, s1, s2, col) in enumerate((
            ("07.a", "SEGURADOS OBRIGATÓRIOS", "AUTOMÁTICA", "pelo exercício da atividade remunerada",
             "independe de inscrição e de pagamento", PREST),
            ("07.b", "SEGURADO FACULTATIVO", "INSCRIÇÃO + 1ª CONTRIBUIÇÃO", "inscrição formalizada",
             "mais o pagamento da primeira contribuição", FAC))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        card(c, x - 350, 220 + d, 700, 360, a)
        text(c, top, x, 285 + d, 30, "black", GRAY, a, tracking=1.5)
        chip(c, big, x, 380 + d, col, a, 40 if k == 0 else 34, 620)
        text(c, s1, x, 490 + d, 28, "bold", INK, a)
        text(c, s2, x, 535 + d, 28, "bold", INK, a)
    pill(c, "a ÚNICA sem filiação automática", 1350, 610, RED, size=28, a=ep(t, C["07.c"], 0.4), anchor="center")
    ad, ae = ep(t, C["07.d"], 0.4), ep(t, C["07.e"], 0.4)
    if ad > 0:
        seq(c, [("só o facultativo ", INK), ("PAGA PARA ENTRAR", FAC)], W / 2, 720, 44, ad, gap=0)
    if ae > 0:
        seq(c, [("os outros entram ", INK), ("SÓ POR TRABALHAR", PREST)], W / 2, 790, 40, ae, gap=0)


def b_contribuicao(c, t, C, B):
    frame(c, t, B["start"], "CONTRIBUIÇÃO DO FACULTATIVO", "QUEM RECOLHE?", FAC)
    chip(c, "ELE MESMO", W / 2, 270, FAC, ep(t, C["08.a"], 0.4), 50, 560)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        x0, x1, y = 400, 1520, 450
        text(c, "salário de contribuição que ELE ESCOLHE", W / 2, 395, 34, "black", INK, ab)
        line(c, x0, y, x0 + (x1 - x0) * ab, y, FAC, ab, 10)
        for xf, s in ((0.0, "MÍNIMO"), (1.0, "TETO")):
            x = x0 + (x1 - x0) * xf
            c.drawCircle(x, y, 16, paint(FAC, ab))
            text(c, s, x, y + 60, 32, "black", FAC, ab)
        mv = ep(t, C["08.b"] + 1.0, 1.2)
        xm = x0 + (x1 - x0) * (0.15 + 0.5 * ease_io(mv))
        c.drawCircle(xm, y, 26, paint("#FFFFFF", ab))
        c.drawCircle(xm, y, 26, paint(INK, ab, stroke=5))
    pill(c, "o RISCO de não recolher é DELE", W / 2, 620, RED, size=32, a=ep(t, C["08.c"], 0.4), anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 700, 1320, 100, 20, mix("#FFFFFF", ASSIST, 0.15), ad)
        text_mid(c, "alíquotas (plano simplificado, baixa renda): CONFIRA O VALOR ATUALIZADO", W / 2, 750, 30, "black",
                 INK, ad)


def b_excluidos(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 12", "OS EXCLUÍDOS DO RGPS", RPPS)
    aa, da = rise(t, C["09.a"])
    if aa > 0:
        for k, s in enumerate(("SERVIDOR de CARGO EFETIVO", "MILITAR")):
            cx = 650 if k == 0 else 1330
            chip(c, s, cx, 250 + da, RPPS, ep(t, C["09.a"] + 0.9 * k, 0.4), 36, 760 if k == 0 else 420)
        text(c, "da União · dos Estados · do DF · dos Municípios", W / 2, 345 + da, 28, "bold", GRAY, aa)
    ab = ep(t, C["09.b"], 0.4)
    text(c, "são EXCLUÍDOS do RGPS", 760, 420, 44, "black", INK, ab)
    ac, dc = rise(t, C["09.c"])
    if ac > 0:
        rrect(c, 300, 450 + dc, 1320, 100, 22, ASSIST, ac, shadow=True)
        text_mid(c, "DESDE QUE AMPARADOS POR REGIME PRÓPRIO", W / 2, 500 + dc, 44, "black", INK, ac)
    pill(c, "a CHAVE: exclusão CONDICIONADA", 1110, 405, RED, size=26, a=ep(t, C["09.d"], 0.4), anchor="left",
         bounds=(0, 1920))
    rowbox(c, "município COM regime próprio", 640, ep(t, C["09.e"], 0.4), "EXCLUÍDO", RPPS, ep(t, C["09.e"], 0.4), 34)
    rowbox(c, "município SEM regime próprio", 760, ep(t, C["09.e"] + 0.8, 0.4), "OBRIGATÓRIO do RGPS", PREST,
           ep(t, C["09.f"] + 0.6, 0.4), 34)


def b_servidor(c, t, C, B):
    frame(c, t, B["start"], "ART. 12, PARÁGRAFO ÚNICO", "O SERVIDOR NO RGPS", PREST)
    aa = ep(t, C["10.a"], 0.4)
    rowbox(c, "servidor/militar + atividade do RGPS ao mesmo tempo", 270, aa, "OBRIGATÓRIO", PREST,
           ep(t, C["10.a"] + 6.0, 0.4), 34)
    text(c, "em relação a essa atividade", 260, 355, 26, "bold", GRAY, ep(t, C["10.a"] + 6.0, 0.4), align="left")
    pill(c, "+ 2 casos que a banca adora", W / 2, 420, ASSIST, size=28, a=ep(t, C["10.b"], 0.4), anchor="center")
    rowbox(c, "EXCLUSIVAMENTE cargo em comissão", 530, ep(t, C["10.c"], 0.4), "EMPREGADO do RGPS", EMP,
           ep(t, C["10.c"] + 1.6, 0.4), 34)
    rowbox(c, "empregado público CELETISTA (EP / SEM)", 660, ep(t, C["10.d"], 0.4), "EMPREGADO do RGPS", EMP,
           ep(t, C["10.d"] + 4.5, 0.4), 34)
    pill(c, "NÃO é excluído", W / 2, 790, RED, size=32, a=ep(t, C["10.e"], 0.4), anchor="center")


ROWS_T = [("FILIAÇÃO", ["automática"] * 5, "inscrição + 1ª contrib."),
          ("RECOLHE P/ SI?", ["não", "não", "SIM", "não", "adquirente"], "SIM"),
          ("PERÍODO DE GRAÇA", ["12 meses"] * 5, "6 meses")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "QUEM É QUEM NO RGPS", "AS 3 LINHAS QUE MAIS CAEM", GREEN)
    card(c, 160, 160, 1600, 700)
    a0 = ep(t, C["11.t"], 0.4)
    xs = [640 + k * 195 for k in range(6)]
    for k, (s, col) in enumerate(CATS):
        a = a0 * ep(t, C["11.t"] + 0.1 * k, 0.3)
        rrect(c, xs[k] - 94, 205, 188, 64, 16, col, a)
        text_mid(c, s if k != 2 else "C. INDIV.", xs[k], 237, 22 if k != 5 else 21, "black", "#FFFFFF", a)
    cues = [("11.a", "11.a2"), ("11.b", "11.b2"), ("11.c", "11.c3")]
    for r, ((lab, vals, fac), (c1, c2)) in enumerate(zip(ROWS_T, cues)):
        y = 300 + r * 180
        a, d = rise(t, C[c1])
        if a <= 0:
            continue
        rrect(c, 190, y + d, 1540, 160, 18, "#F7F7F5", a)
        text(c, lab, 220, y + 92 + d, 28, "black", INK, a, align="left")
        for k, v in enumerate(vals):
            if r == 0:
                ak = a * ep(t, C[c1] + 0.6 * k, 0.3)
            elif r == 1:
                ak = ep(t, C["11.b2"], 0.3) if k == 2 else (a if k != 4 else a * 0.8)
            else:
                ak = ep(t, C["11.c3"], 0.4)
            hl = (r == 1 and k == 2)
            col = CI if hl else (GRAY if (r == 1 and k == 4) else INK2)
            sz = 30 if r == 2 else (30 if v in ("SIM", "não") else 24)
            text_mid(c, v, xs[k], y + 80 + d, sz, "black", col, ak)
        if r == 1:
            af = ep(t, C["11.b2"], 0.4)
        elif r == 2:
            af = ep(t, C["11.c2"], 0.4)
        else:
            af = ep(t, C["11.a2"], 0.4)
        if af > 0:
            rrect(c, xs[5] - 98, y + 12 + d, 196, 136, 16, FAC, af, shadow=True)
            if r == 0:
                text_mid(c, "inscrição +", xs[5], y + 58 + d, 25, "black", "#FFFFFF", af)
                text_mid(c, "1ª contrib.", xs[5], y + 100 + d, 25, "black", "#FFFFFF", af)
            else:
                text_mid(c, fac, xs[5], y + 80 + d, 32 if r == 1 else 30, "black", "#FFFFFF", af)


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 160, 1520, 700)
    items = [("12.p1", "12.r1", "é facultativo o MAIOR DE 18 que se filiar mediante contribuição", False, "16 anos, pelo Decreto"),
             ("12.p2", "12.r2", "quem tem regime próprio pode ser facultativo no RGPS", False, "VEDADO pela CF (art. 201, §5º)"),
             ("12.p3", "12.r3", "a dona de casa é segurada OBRIGATÓRIA", False, "é FACULTATIVA, se quiser se filiar"),
             ("12.p4", "12.r4", "o síndico não remunerado pode ser facultativo", True, "sem remuneração, não é contribuinte individual")]
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
       ["A filiação ao Regime Geral de Previdência Social", "é SEMPRE automática, decorrendo do exercício",
        "de atividade remunerada."],
       "ERRADO", False, "automática só para os OBRIGATÓRIOS · facultativo: inscrição + 1ª contribuição", "A FILIAÇÃO",
       size=42)


def b_caso(c, t, C, B):
    head(c, t, B["start"], "O CASO DA RENATA", "FACULTATIVA OU EMPREGADA?", FAC)
    card(c, 200, 160, 1520, 700)
    aa = ep(t, C["14.a"], 0.4)
    if aa > 0:
        seq(c, [("art. 13: o facultativo ", INK), ("NÃO", RED), (" pode estar no art. 11, ", INK), ("o tempo todo", FAC)],
            W / 2, 255, 36, aa, gap=0)
    ab = ep(t, C["14.b"], 0.5)
    x0, xm, x1, y = 300, 960, 1620, 400
    a0 = ep(t, C["14.t"], 0.4)
    if a0 > 0:
        ac = ep(t, C["14.c"], 0.4)
        rrect(c, x0, y - 40, xm - x0 - 10, 80, 16, mix(FAC, "#D4D4D8", 0.7 * ac), a0)
        text_mid(c, "JAN · FACULTATIVA", (x0 + xm) / 2, y, 34, "black", "#FFFFFF", a0)
        if ac > 0:
            strike(c, x0 + 30, y, xm - 40, y, ac, RED, ac)
            pill(c, "a condição de facultativa ACABA", (x0 + xm) / 2, y + 90, RED, size=26, a=ac, anchor="center")
    if ab > 0:
        rrect(c, xm + 10, y - 40, (x1 - xm - 10) * ab, 80, 16, EMP, ab)
        text_mid(c, "JUL · EMPREGADA", (xm + x1) / 2, y, 34, "black", "#FFFFFF", ab)
        text(c, "filiação obrigatória e AUTOMÁTICA", (xm + x1) / 2, y + 100, 28, "bold", EMP, ab)
    ad = ep(t, C["14.d"], 0.4)
    ok_x(c, "opção", 520, 600, False, ad, 30)
    ok_x(c, "dupla filiação", 860, 600, False, ep(t, C["14.d"] + 0.8, 0.4), 30)
    chip(c, "O OBRIGATÓRIO PREVALECE", 1330, 600, EMP, ep(t, C["14.d"] + 2.0, 0.4), 34, 560)
    ae = ep(t, C["14.e"], 0.4)
    if ae > 0:
        rrect(c, 330, 690, 1260, 100, 20, mix("#FFFFFF", ASSIST, 0.15), ae)
        text_mid(c, "nova inscrição? NÃO: quem inscreve o empregado é o EMPREGADOR", W / 2, 740, 32, "black", INK, ae)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("15.a", "facultativo (art. 13): maior de 16 pelo Decreto · 14 na literalidade"),
            ("15.b", "mediante contribuição · SEM atividade obrigatória"),
            ("15.c", "filiação: INSCRIÇÃO + 1ª CONTRIBUIÇÃO (a única não automática)"),
            ("15.d", "período de graça: 6 MESES (os demais, 12)"),
            ("15.e", "regime próprio NÃO pode ser facultativo (CF, art. 201, §5º)"),
            ("15.f", "excluídos (art. 12): efetivo e militar SÓ SE amparados por RPPS")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 255 + k * 100 + dy
        check_icon(c, 270, y - 12, 24, a, GREEN)
        text(c, s, 320, y, 34, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["16.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Os dependentes", W / 2, 430, 64, "black", INK, a)
        pill(c, "e as suas três classes", W / 2, 540, GEST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a,
             anchor="center")
    ap = fw(t, C["16.pdf"], C["16.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["16.pdf"], 0.5)) * 20)
    cta(c, t, C["16.like"], C["16.sub"], C["16.bell"], C["16.com"], C["16.bye"], "Você acertou o caso da Renata?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, base=b_base, conceito=b_conceito, idade=b_idade, quem=b_quem, vedacao=b_vedacao,
              filiacao=b_filiacao, contribuicao=b_contribuicao, excluidos=b_excluidos, servidor=b_servidor,
              tabela=b_tabela, pegadinhas=b_pegadinhas, q_ce=b_q_ce, caso=b_caso, resumo=b_resumo, cta=b_cta)
