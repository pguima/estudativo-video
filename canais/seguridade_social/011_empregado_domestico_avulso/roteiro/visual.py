"""Visual do vídeo Seguridade 011 — Empregado, empregado doméstico e avulso (Lei 8.213, art. 11, I, II e VI). Tema 'seguridade'.
Cores das categorias neste vídeo: empregado = verde-petróleo · doméstico = roxo · avulso = âmbar · contribuinte individual = cinza-escuro.
Reaproveita do 010: ce() (questão C/E), tag() (inciso), ok_x() e pdf_card()."""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "010_estrutura_rgps" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v010", _p)
V10 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V10)
motor.set_theme("seguridade")
tag, ce, ok_x, pdf_card = V10.tag, V10.ce, V10.ok_x, V10.pdf_card

MARCA = ""
ARQUIVO_FINAL = "seguridade_011_empregado_domestico_avulso.mp4"
CARD_R = (140, 150, 1640, 690)

PREST = "#0F766E"
ASSIST = "#E8A317"
GEST = "#4F46E5"
EMP, DOM, AVU, CI = PREST, GEST, ASSIST, "#3A3A3C"


def frame(c, t, t0, l1, l2, col):
    head(c, t, t0, l1, l2, col)
    card(c, *CARD_R)


def lei_card(c, t, rows, x=220, y=230, w=1480, size=40, col=EMP, src=""):
    """texto de lei: rows = [(cue, trecho, destaque?)] — cada trecho entra na sua vez; destaque em cor"""
    a0 = ep(t, rows[0][0], 0.4)
    if a0 <= 0:
        return
    rrect(c, x, y, w, 90 + len(rows) * (size + 26) + 20, 24, mix("#FFFFFF", col, 0.06), a0, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, 12, 90 + len(rows) * (size + 26) + 20), paint(col, a0))
    text(c, src, x + 50, y + 54, 24, "black", col, a0, align="left", tracking=1.5)
    for k, (tc, s, hl) in enumerate(rows):
        a, d = rise(t, tc)
        text(c, s, x + 50, y + 120 + k * (size + 26) + d, size, "black" if hl else "semibold", col if hl else INK, a, align="left")


def macete(c, letras, cy, a, col, size=110, gap=40):
    if a <= 0:
        return
    ws = [text_w(l, "black", size) for l in letras]
    tot = sum(ws) + gap * (len(letras) - 1)
    x = W / 2 - tot / 2
    for k, (l, w) in enumerate(zip(letras, ws)):
        ak = a * ep(k * 0.12, 0, 0.01)
        sc = 0.85 + 0.15 * ease_back(clamp(a * 1.4 - k * 0.08))
        c.save(); c.translate(x + w / 2, cy); c.scale(sc, sc)
        text_mid(c, l, 0, 0, size, "black", col, ak)
        c.restore()
        x += w + gap


def chip(c, s, cx, cy, col, a, size=40, w=None, sub=None):
    if a <= 0:
        return
    w = w or text_w(s, "black", size) + 80
    h = size * 1.9 + (40 if sub else 0)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, col, a, shadow=True)
    text_mid(c, s, cx, cy - (18 if sub else 0), size, "black", "#FFFFFF", a)
    if sub:
        text_mid(c, sub, cx, cy + size * 0.75, size * 0.6, "bold", "#FFFFFF", a)


def verdict(c, s, cx, cy, a, col):
    if a <= 0:
        return
    result_box(c, s, cx, cy, 44, a, col)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 11 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        card(c, 460, 260, 1000, 150, aa)
        text_mid(c, "“O gari é empregado?”", W / 2, 335, 56, "black", GRAY, aa)
        if t > C["01.b"]:
            strike(c, 640, 335, 1280, 335, 1, RED, ep(t, C["01.b"], 0.5))
    ab = ep(t, C["01.b"], 0.5)
    text(c, "a banca DESCREVE uma situação · você ENQUADRA", W / 2, 490, 42, "black", INK, ab)
    for k, (cue, s, col) in enumerate((("01.d", "EMPREGADO", EMP), ("01.d", "DOMÉSTICO", DOM), ("01.d", "AVULSO", AVU))):
        a, d = rise(t, C[cue] + 0.7 * k)
        chip(c, s, 520 + k * 440, 620 + d, col, a, 40, 380)
    ae = ep(t, C["01.e"], 0.5)
    pill(c, "1 pergunta para cada um", W / 2, 760, GREEN, size=32, a=ae, anchor="center")


def b_mapa(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 11", "TRÊS INCISOS", PREST)
    for k, (cue, rom, s, col) in enumerate((("02.a", "I", "EMPREGADO", EMP), ("02.b", "II", "EMPREGADO DOMÉSTICO", DOM),
                                           ("02.c", "VI", "TRABALHADOR AVULSO", AVU))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 125 + d
        tag(c, rom, 420, y, col, a, 46)
        text(c, s, 560, y + 18, 54, "black", INK, a, align="left")
    ad = ep(t, C["02.d"], 0.5)
    if ad > 0:
        check_icon(c, 560, 690, 26, ad, RED, "x")
        text(c, "decorar o NOME", 600, 704, 38, "black", RED, ad, align="left")
        check_icon(c, 1040, 690, 26, ad, GREEN)
        text(c, "decorar os ELEMENTOS", 1080, 704, 38, "black", GREEN, ad, align="left")


# ======================================================================
# empregado
# ======================================================================

def b_emp_conceito(c, t, C, B):
    head(c, t, B["start"], "INCISO I", "O EMPREGADO", EMP)
    rows = [(C["03.a"], "presta serviço urbano ou rural à EMPRESA,", True),
            (C["03.b"], "em caráter NÃO EVENTUAL,", True),
            (C["03.c"], "sob sua SUBORDINAÇÃO", True),
            (C["03.d"], "e mediante REMUNERAÇÃO,", True),
            (C["03.e"], "inclusive como DIRETOR EMPREGADO.", True)]
    lei_card(c, t, rows, 240, 190, 1440, 44, EMP, "LEI 8.213/1991 · ART. 11, I, “a”")


PPNSO = [("04.a", "P", "essoa física", "empresa nunca é empregado"), ("04.b", "P", "essoalidade", "ele mesmo trabalha"),
         ("04.c", "N", "ão eventualidade", "habitual"), ("04.d", "S", "ubordinação", "recebe ordens"),
         ("04.e", "O", "nerosidade", "é pago")]


def b_ppnso(c, t, C, B):
    head(c, t, B["start"], "EMPREGADO", "OS 5 ELEMENTOS", EMP)
    card(c, 200, 160, 1520, 700)
    am = ep(t, C["04.m"], 0.5)
    for k, (cue, l, rest, sub) in enumerate(PPNSO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 110 + d
        hl = (l == "S") and am > 0
        text(c, l, 420, y + 16, 90, "black", ASSIST, a, align="right")
        text(c, rest, 426, y + 16, 50, "black", INK, a, align="left")
        text(c, sub, 1640, y + 10, 32, "bold", GRAY, a, align="right")
    pill(c, "P · P · N · S · O", W / 2, 820, ASSIST, size=40, a=am, anchor="center")


def b_subordinacao(c, t, C, B):
    frame(c, t, B["start"], "PONTO DE OURO", "A SUBORDINAÇÃO DECIDE", ASSIST)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        sc = 1 + 0.04 * math.sin(t * 5) * ab
        c.save(); c.translate(W / 2, 290); c.scale(sc, sc)
        text_mid(c, "SUBORDINAÇÃO", 0, 0, 96, "black", ASSIST, ab)
        c.restore()
    text(c, "decide quase todas as questões", W / 2, 230, 34, "bold", GRAY, ep(t, C["05.a"], 0.5) * (1 - ab))
    ac, dc = rise(t, C["05.c"])
    if ac > 0:
        text(c, "TEM? →", 640, 520 + dc, 50, "black", INK, ac, align="right")
        chip(c, "EMPREGADO", 960, 504 + dc, EMP, ac, 46, 500)
    ad, dd = rise(t, C["05.d"])
    if ad > 0:
        text(c, "NÃO TEM? →", 640, 680 + dd, 50, "black", INK, ad, align="right")
        chip(c, "CONTRIBUINTE INDIVIDUAL", 1090, 664 + dd, CI, ad, 40, 760, "o autônomo")


def b_diretor(c, t, C, B):
    frame(c, t, B["start"], "QUEM MAIS É EMPREGADO", "O DIRETOR", EMP)
    ab, db = rise(t, C["06.b"])
    if ab > 0:
        card(c, 230, 260 + db, 680, 380, ab)
        text(c, "DIRETOR", 570, 360 + db, 50, "black", INK, ab)
        text(c, "EMPREGADO", 570, 430 + db, 50, "black", EMP, ab)
        chip(c, "EMPREGADO", 570, 550 + db, EMP, ab, 38, 480)
    ac, dc = rise(t, C["06.c"])
    if ac > 0:
        card(c, 1010, 260 + dc, 680, 380, ac)
        text(c, "DIRETOR", 1350, 360 + dc, 50, "black", INK, ac)
        text(c, "NÃO EMPREGADO", 1350, 430 + dc, 50, "black", RED, ac)
        chip(c, "CONTRIBUINTE INDIVIDUAL", 1350, 550 + dc, CI, ac, 32, 600)
    pill(c, "uma palavrinha muda tudo", W / 2, 770, ASSIST, size=34, a=ep(t, C["06.d"], 0.4), anchor="center")


def b_temporario(c, t, C, B):
    frame(c, t, B["start"], "QUEM MAIS É EMPREGADO", "O TEMPORÁRIO", EMP)
    aa = ep(t, C["07.a"], 0.5)
    person_x = 960
    if aa > 0:
        c.drawCircle(person_x, 300, 46, paint(EMP, aa))
        rrect(c, person_x - 66, 356, 132, 120, 50, EMP, aa)
        chip(c, "EMPREGADO", person_x, 540, EMP, aa, 34, 360)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 260, 500, 200, 24, "#FFFFFF", ab, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(230, 260, 500, 200), 24, 24), paint(GREEN, ab, stroke=5))
        text_mid(c, "EMPRESA DE", 480, 330, 34, "black", INK, ab)
        text_mid(c, "TRABALHO TEMPORÁRIO", 480, 380, 34, "black", INK, ab)
        line(c, 730, 360, 880, 360, GREEN, ab, 8, progress=ab)
        pill(c, "VÍNCULO", 805, 320, GREEN, size=24, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["07.c"], 0.5)
    if ac > 0:
        rrect(c, 1190, 260, 500, 200, 24, "#FFFFFF", ac * 0.7, shadow=True)
        text_mid(c, "EMPRESA ONDE", 1440, 330, 34, "black", GRAY, ac)
        text_mid(c, "PRESTA O SERVIÇO", 1440, 380, 34, "black", GRAY, ac)
        line(c, 1040, 360, 1190, 360, LIGHT, ac, 6, dash=(14, 10))
        check_icon(c, 1115, 360, 22, ac, RED, "x")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        ok_x(c, "temporário = avulso", W / 2 - 30, 700, False, ad, 34)


def b_comissao(c, t, C, B):
    frame(c, t, B["start"], "O CLÁSSICO", "O SERVIDOR PÚBLICO", EMP)
    rows = [("08.a", "efetivo COM regime próprio", "FORA DO RGPS", RED),
            ("08.b", "EXCLUSIVAMENTE cargo em comissão, SEM vínculo efetivo", "EMPREGADO", EMP)]
    for k, (cue, s, res, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 180 + d
        rrect(c, 220, y - 60, 1480, 140, 20, "#F7F7F5", a)
        text(c, s, 260, y + 22, 40 if k == 0 else 34, "black", INK, a, align="left")
        ar = a if k == 0 else ep(t, C["08.c"], 0.5)
        pill(c, res, 1670, y + 10, col, size=34, a=ar, anchor="right", bounds=(0, 1920))
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        ok_x(c, "todo servidor está excluído do RGPS", W / 2 - 30, 720, False, ad, 32)


def b_mandato(c, t, C, B):
    frame(c, t, B["start"], "QUEM MAIS É EMPREGADO", "O MANDATO ELETIVO", EMP)
    a0 = ep(t, C["09.t"], 0.5)
    for k, s in enumerate(("vereador", "prefeito", "deputado", "senador")):
        pill(c, s, 400 + k * 370, 240, INK2, size=32, a=a0 * ep(t, C["09.t"] + 0.4 * k, 0.3), anchor="center", bounds=(0, 1920))
    aa = ep(t, C["09.a"], 0.5)
    text(c, "SEM vínculo a regime próprio →", 900, 420, 48, "black", INK, aa, align="right")
    chip(c, "EMPREGADO", 1220, 400, EMP, ep(t, C["09.b"], 0.5), 44, 480)
    ac = ep(t, C["09.c"], 0.5)
    if ac > 0:
        ok_x(c, "contribuinte individual", W / 2 - 30, 560, False, ac, 34)
    selo = ep(t, C["09.d"], 0.5)
    pill(c, "parece estranho? por isso CAI", W / 2, 700, ASSIST, size=36, a=selo, anchor="center")


def b_emp_recolhe(c, t, C, B):
    frame(c, t, B["start"], "QUEM RECOLHE", "A CONTRIBUIÇÃO DO EMPREGADO", EMP)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        chip(c, "EMPRESA", 560, 330, EMP, aa, 44, 420)
        text(c, "desconta do salário e recolhe", 560, 440, 34, "bold", INK2, aa)
        arrow(c, 800, 330, 1100, 330, EMP, aa, 6, 20, progress=aa)
        rrect(c, 1120, 260, 420, 140, 24, INK, aa, shadow=True)
        text_mid(c, "INSS", 1330, 330, 60, "black", "#FFFFFF", aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0 and t < C["10.c"]:
        xmark_a = ab
        line(c, 920, 290, 980, 370, RED, xmark_a, 10)
        line(c, 980, 290, 920, 370, RED, xmark_a, 10)
    ac = ep(t, C["10.c"], 0.5)
    pill(c, "o risco é da EMPRESA", W / 2, 580, RED, size=40, a=ac, anchor="center")
    text(c, "o empregado NÃO perde o tempo de contribuição", W / 2, 700, 40, "black", GREEN, ep(t, C["10.c"] + 1.0, 0.5))


# ======================================================================
# doméstico
# ======================================================================

def b_dom_conceito(c, t, C, B):
    head(c, t, B["start"], "INCISO II", "O EMPREGADO DOMÉSTICO", DOM)
    rows = [(C["11.a"], "presta serviço CONTÍNUO, mediante remuneração,", True),
            (C["11.b"], "a PESSOA OU FAMÍLIA,", True),
            (C["11.c"], "no ÂMBITO RESIDENCIAL destas,", True),
            (C["11.d"], "em atividades SEM FINS LUCRATIVOS.", True)]
    lei_card(c, t, rows, 240, 200, 1440, 46, DOM, "LEI 8.213/1991 · ART. 11, II")


CPRS2 = [("12.a", "C", "ontínuo"), ("12.b", "P", "essoa ou família"), ("12.c", "R", "esidência"),
         ("12.d", "S", "em lucro"), ("12.e", "2", " dias: MAIS de 2 por semana")]


def b_cprs2(c, t, C, B):
    head(c, t, B["start"], "DOMÉSTICO", "OS 5 FILTROS", DOM)
    card(c, 200, 160, 1520, 700)
    for k, (cue, l, rest) in enumerate(CPRS2):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 110 + d
        text(c, l, 520, y + 16, 90, "black", ASSIST, a, align="right")
        text(c, rest, 526, y + 16, 50, "black", INK, a, align="left")
    pill(c, "C · P · R · S · 2", W / 2, 820, ASSIST, size=40, a=ep(t, C["12.m"], 0.5), anchor="center")


def b_dois_dias(c, t, C, B):
    frame(c, t, B["start"], "LC 150/2015", "A REGRA DOS 2 DIAS", DOM)
    dias = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
    ab = ep(t, C["13.b"], 0.5)
    acc = ep(t, C["13.c"], 0.5)
    for row, (aa, n, lab, col, sub) in enumerate(((ab, 2, "DIARISTA", CI, "contribuinte individual"),
                                                  (acc, 3, "DOMÉSTICA", DOM, "empregada doméstica"))):
        if aa <= 0:
            continue
        y = 260 + row * 230
        for k, d in enumerate(dias):
            on_ = k < n
            x = 240 + k * 120
            rrect(c, x, y, 100, 100, 16, col if on_ else "#F2F2EF", aa * ep(t, (C["13.b"] if row == 0 else C["13.c"]) + 0.15 * k, 0.3))
            text_mid(c, d, x + 50, y + 50, 26, "black", "#FFFFFF" if on_ else GRAY, aa)
        text(c, ("ATÉ " if row == 0 else "MAIS DE ") + "2 DIAS", 1100, y + 40, 34, "black", INK2, aa, align="left")
        chip(c, lab, 1530, y + 50, col, aa, 32, 300)
        text(c, sub, 1100, y + 92, 26, "bold", GRAY, aa, align="left")
    ad = ep(t, C["13.d"], 0.5)
    pill(c, "3× por semana: doméstica · 2×: diarista", W / 2, 770, ASSIST, size=34, a=ad, anchor="center")
    a2 = ep(t, C["13.t"], 0.5) * (1 - ab)
    text(c, "2", W / 2, 560, 300, "black", DOM, a2)
    text(c, "DIAS POR SEMANA", W / 2, 650, 50, "black", INK, a2)
    text(c, "Lei Complementar 150/2015", W / 2, 260, 34, "bold", GRAY, ep(t, C["13.a"], 0.4) * (1 - ab))


def b_idade(c, t, C, B):
    frame(c, t, B["start"], "IDADE MÍNIMA", "DOMÉSTICO É 18", DOM)
    items = [("14.a", "18", "DOMÉSTICO", DOM), ("14.b", "16", "REGRA GERAL", INK2), ("14.c", "14", "APRENDIZ", GRAY)]
    for k, (cue, n, lab, col) in enumerate(items):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 480 + k * 480
        sz = 200 if k == 0 else 150
        text(c, n, x, 470 + d, sz, "black", col, a)
        text(c, lab, x, 560 + d, 38, "black", INK, a)
    text(c, "LC 150/2015 proíbe contratar menor de 18 para o trabalho doméstico", W / 2, 680, 30, "bold", GRAY, ep(t, C["14.a"] + 1.0, 0.4))
    pill(c, "doméstico 18 · regra geral 16 · aprendiz 14", W / 2, 780, ASSIST, size=34, a=ep(t, C["14.m"], 0.5), anchor="center")


def b_lucro(c, t, C, B):
    frame(c, t, B["start"], "O FILTRO DO SEM LUCRO", "CASOS PRÁTICOS", DOM)
    rows = [("15.a", "cozinheira na casa da família", "DOMÉSTICA", DOM),
            ("15.b", "cozinheira no restaurante", "EMPREGADA", EMP),
            ("15.c", "caseiro do sítio de LAZER da família", "DOMÉSTICO", DOM),
            ("15.d", "caseiro do sítio que PRODUZ E VENDE", "EMPREGADO RURAL", EMP)]
    for k, (cue, s, res, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 135 + (30 if k >= 2 else 0) + d
        rrect(c, 220, y - 50, 1480, 110, 18, "#F7F7F5", a)
        text(c, s, 260, y + 16, 40, "black", INK, a, align="left")
        pill(c, res, 1670, y + 4, col, size=32, a=ep(t, C[cue] + 1.2, 0.4), anchor="right", bounds=(0, 1920))


# ======================================================================
# avulso
# ======================================================================

def empresas(c, cx, cy, a, n=3, col=None):
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * 200
        rrect(c, x - 70, cy - 60, 140, 120, 14, col or INK2, a, shadow=True)
        for j in range(2):
            rrect(c, x - 44 + j * 52, cy - 34, 36, 30, 4, "#FFFFFF", a * 0.8)
        rrect(c, x - 18, cy + 18, 36, 42, 4, "#FFFFFF", a * 0.8)


def b_avulso(c, t, C, B):
    frame(c, t, B["start"], "INCISO VI", "O TRABALHADOR AVULSO", AVU)
    aa = ep(t, C["16.a"], 0.5)
    empresas(c, W / 2, 280, aa)
    if aa > 0:
        c.drawCircle(W / 2, 520, 40, paint(AVU, aa))
        rrect(c, W / 2 - 56, 566, 112, 100, 44, AVU, aa)
        for k in range(3):
            x = W / 2 + (k - 1) * 200
            line(c, W / 2, 480, x, 345, AVU, aa, 4, progress=ep(t, C["16.a"] + 0.3 * k, 0.4))
    text(c, "DIVERSAS empresas", 420, 520, 40, "black", INK, aa)
    ab = ep(t, C["16.b"], 0.5)
    text(c, "SEM vínculo empregatício", 1500, 520, 40, "black", INK, ab)
    ac = ep(t, C["16.c"], 0.5) * (1 - ep(t, C["16.e"], 0.4))
    pill(c, "o autônomo também não faz isso?", W / 2, 760, CI, size=34, a=ac, anchor="center")
    ae = ep(t, C["16.e"], 0.5)
    pill(c, "o que separa os dois: INTERMEDIAÇÃO", W / 2, 760, ASSIST, size=38, a=ae, anchor="center")


def b_psi(c, t, C, B):
    head(c, t, B["start"], "AVULSO", "OS 3 ELEMENTOS", AVU)
    card(c, 200, 160, 1520, 700)
    rows = [("17.a", "P", "luralidade de tomadores"), ("17.b", "S", "em vínculo"), ("17.c", "I", "ntermediação obrigatória")]
    for k, (cue, l, rest) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 120 + d
        text(c, l, 520, y + 16, 96, "black", ASSIST, a, align="right")
        text(c, rest, 526, y + 16, 54, "black", INK, a, align="left")
    pill(c, "P · S · I", 500, 680, ASSIST, size=40, a=ep(t, C["17.m"], 0.5), anchor="center", bounds=(0, 1920))
    ax = ep(t, C["17.x"], 0.5)
    if ax > 0:
        rrect(c, 720, 630, 960, 110, 22, mix("#FFFFFF", GEST, 0.10), ax)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(720, 630, 960, 110), 22, 22), paint(GEST, ax, stroke=4))
        text_mid(c, "sem intermediação, não há avulso", 1200, 685, 40, "black", GEST, ax)


def b_ogmo(c, t, C, B):
    frame(c, t, B["start"], "QUEM INTERMEDEIA", "OGMO × SINDICATO", AVU)
    for k, (cue, tipo, quem, sub, col) in enumerate((("18.a", "PORTUÁRIO", "OGMO", "Órgão Gestor de Mão de Obra", PREST),
                                                    ("18.b", "NÃO PORTUÁRIO", "SINDICATO", "da categoria", GEST))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        card(c, x - 330, 220 + d, 660, 400, a)
        text(c, "avulso", x, 290 + d, 32, "bold", GRAY, a)
        text(c, tipo, x, 350 + d, 46, "black", INK, a)
        arrow(c, x, 380 + d, x, 440 + d, col, a, 5, 16)
        chip(c, quem, x, 500 + d, col, a, 50, 440)
        text(c, sub, x, 590 + d, 28, "bold", GRAY, a)
    ac = ep(t, C["18.c"], 0.5)
    if ac > 0:
        ok_x(c, "portuário pelo sindicato", W / 2 - 30, 740, False, ac, 34)


def b_cf7(c, t, C, B):
    frame(c, t, B["start"], "PONTO DE OURO", "CF, ART. 7º, XXXIV", PREST)
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 220, 1400, 180, 24, mix("#FFFFFF", PREST, 0.08), ab, shadow=True)
        text(c, "“igualdade de direitos entre o trabalhador com vínculo", W / 2, 295, 40, "semibold", INK, ab)
        text(c, "empregatício permanente e o trabalhador avulso”", W / 2, 350, 40, "semibold", INK, ab)
    text(c, "Constituição Federal · art. 7º, XXXIV", W / 2, 450, 28, "bold", GRAY, ep(t, C["19.a"], 0.4))
    ac = ep(t, C["19.c"], 0.5)
    if ac > 0:
        chip(c, "AVULSO", 640, 610, AVU, ac, 46, 360)
        text_mid(c, "=", W / 2, 610, 90, "black", INK, ac)
        chip(c, "EMPREGADO", 1280, 610, EMP, ac, 46, 440)
        text(c, "na previdência", W / 2, 760, 34, "bold", GRAY, ac)


# ======================================================================
# quem recolhe · perguntas
# ======================================================================

def b_recolhe(c, t, C, B):
    frame(c, t, B["start"], "A LINHA MAIS IMPORTANTE", "QUEM RECOLHE?", ASSIST)
    aa, da = rise(t, C["20.a"])
    if aa > 0:
        rrect(c, 220, 220 + da, 700, 400, 24, mix("#FFFFFF", EMP, 0.07), aa, shadow=True)
        text(c, "NÃO recolhem para si", 570, 290 + da, 34, "black", EMP, aa)
        for k, (s, col) in enumerate((("Empregado", EMP), ("Doméstico", DOM), ("Avulso", AVU))):
            pill(c, s, 570, 360 + k * 70 + da, col, size=32, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "quem recolhe: um TERCEIRO", 570, 590 + da, 30, "bold", INK2, aa)
    ab, db = rise(t, C["20.b"])
    if ab > 0:
        rrect(c, 1000, 220 + db, 700, 400, 24, mix("#FFFFFF", CI, 0.05), ab, shadow=True)
        text(c, "recolhem POR CONTA PRÓPRIA", 1350, 290 + db, 34, "black", CI, ab)
        for k, s in enumerate(("Contribuinte individual", "Facultativo")):
            pill(c, s, 1350, 380 + k * 80 + db, CI, size=32, a=ab, anchor="center", bounds=(0, 1920))
    pill(c, "E · E · A não recolhem   ·   C · F recolhem", W / 2, 760, ASSIST, size=38, a=ep(t, C["20.m"], 0.5), anchor="center")


def b_perguntas(c, t, C, B):
    frame(c, t, B["start"], "AS 3 PERGUNTAS", "QUE RESOLVEM A QUESTÃO", GREEN)
    rows = [("21.a", "Tem SUBORDINAÇÃO?", "EMPREGADO", EMP), ("21.b", "Tem RESIDÊNCIA SEM LUCRO?", "DOMÉSTICO", DOM),
            ("21.c", "Tem INTERMEDIAÇÃO?", "AVULSO", AVU)]
    for k, (cue, q, r, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 290 + k * 160 + d
        text(c, q, 300, y + 18, 52, "black", INK, a, align="left")
        arrow(c, 1180, y, 1260, y, GRAY, a, 5, 16)
        chip(c, r, 1480, y, col, ep(t, C[cue] + 0.8, 0.4), 40, 400)


# ======================================================================
# pegadinhas e questões
# ======================================================================

def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 170, 1520, 680)
    items = [("22.p1", "22.r1", "a diarista de 2 dias por semana é empregada doméstica", False, "até 2 dias: contribuinte individual"),
             ("22.p2", "22.r2", "o vereador sem regime próprio é contribuinte individual", False, "é EMPREGADO"),
             ("22.p3", "22.r3", "a CF assegura igualdade entre empregado permanente e avulso", True, "CF, art. 7º, XXXIV")]
    for k, (cp, cr, frase, ok, corr) in enumerate(items):
        a, dy = rise(t, C[cp])
        if a <= 0:
            continue
        y = 280 + k * 190 + dy
        text(c, "“" + frase + "”", 260, y, 34, "semibold", INK, a, align="left")
        ar = ep(t, C[cr], 0.4)
        pill(c, "CERTO" if ok else "ERRADO", 1660, y + 60, GREEN if ok else RED, size=28, a=ar, anchor="right", bounds=(0, 1920))
        text(c, "→ " + corr, 290, y + 70, 30, "bold", GREEN if ok else RED, ar, align="left")


def b_q_ce(c, t, C, B):
    ce(c, t, C, "23.e", "23.r", "23.x",
       ["Empregado com a contribuição descontada do salário,", "sem recolhimento pela empresa, NÃO pode contar",
        "esse período como tempo de contribuição."],
       "ERRADO", False, "a responsabilidade é da EMPRESA · o empregado não é prejudicado", "O RISCO É DE QUEM?", size=42)


def b_q_caso(c, t, C, B):
    head(c, t, B["start"], "CASO PRÁTICO", "O CASEIRO CARLOS", DOM)
    card(c, 200, 170, 1520, 680)
    aa = ep(t, C["24.a"], 0.4)
    text(c, "Carlos é caseiro da chácara de uma família, usada só para LAZER", 260, 260, 36, "semibold", INK, aa, align="left")
    ab = ep(t, C["24.b"], 0.4)
    text(c, "nos fins de semana. Trabalha de segunda a sexta e mora no local.", 260, 315, 36, "semibold", INK, ab, align="left")
    ar = ep(t, C["24.r"], 0.4)
    opts = [("empregado rural", EMP, False), ("empregado doméstico", DOM, True), ("contribuinte individual", CI, False)]
    for k, (s, col, ok) in enumerate(opts):
        a = ep(t, C["24.c"] + 0.5 * k, 0.4)
        x = 470 + k * 490
        al = a * (1 - 0.6 * ar if not ok else 1)
        rrect(c, x - 220, 400, 440, 100, 20, col if (ok and ar > 0.5) else "#F2F2EF", al, shadow=ok and ar > 0.5)
        text_mid(c, s, x, 450, 32, "black", "#FFFFFF" if (ok and ar > 0.5) else INK, al)
    ax = ep(t, C["24.x"], 0.5)
    for k, s in enumerate(("família", "residência", "sem lucro", "+ de 2 dias")):
        a = ax * ep(t, C["24.x"] + 0.4 * k, 0.3)
        x = 420 + k * 360
        check_icon(c, x - 90, 600, 20, a, GREEN)
        text(c, s, x - 60, 612, 32, "black", GREEN, a, align="left")
    text(c, "chácara COMERCIAL → empregado rural", W / 2, 740, 34, "black", AMBER, ep(t, C["24.x"] + 3.0, 0.5))


# ======================================================================
# fechamento
# ======================================================================

def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("25.a", "Empregado: P · P · N · S · O — a subordinação decide"),
            ("25.b", "comissão sem vínculo efetivo e mandato sem RPPS: empregado"),
            ("25.c", "Doméstico: C · P · R · S · 2 — idade mínima 18"),
            ("25.d", "Avulso: P · S · I — OGMO (porto) ou sindicato"),
            ("25.e", "E · E · A não recolhem para si: o risco é do terceiro")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 270 + k * 112 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["26.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Contribuinte individual", W / 2, 430, 64, "black", INK, a)
        pill(c, "o autônomo · o diarista · o diretor não empregado", W / 2, 540, CI, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a,
             anchor="center")
    ap = fw(t, C["26.pdf"], C["26.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["26.pdf"], 0.5)) * 20)
    cta(c, t, C["26.like"], C["26.sub"], C["26.bell"], C["26.com"], C["26.bye"], "Você acertou o caso do Carlos?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, mapa=b_mapa, emp_conceito=b_emp_conceito, ppnso=b_ppnso, subordinacao=b_subordinacao,
              diretor=b_diretor, temporario=b_temporario, comissao=b_comissao, mandato=b_mandato, emp_recolhe=b_emp_recolhe,
              dom_conceito=b_dom_conceito, cprs2=b_cprs2, dois_dias=b_dois_dias, idade=b_idade, lucro=b_lucro,
              avulso=b_avulso, psi=b_psi, ogmo=b_ogmo, cf7=b_cf7, recolhe=b_recolhe, perguntas=b_perguntas,
              pegadinhas=b_pegadinhas, q_ce=b_q_ce, q_caso=b_q_caso, resumo=b_resumo, cta=b_cta)
