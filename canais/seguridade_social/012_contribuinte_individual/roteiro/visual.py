"""Visual do vídeo Seguridade 012 — Contribuinte individual (Lei 8.213, art. 11, V). Tema 'seguridade'.
Cores: contribuinte individual = cinza-escuro (como no 011) · empregado = verde-petróleo · doméstico = roxo · avulso = âmbar ·
segurado especial = verde. Reaproveita do 011 (chip, frame) e do 010 (ce, tag, ok_x, pdf_card)."""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "011_empregado_domestico_avulso" / "roteiro" / "visual.py"
_s = importlib.util.spec_from_file_location("v011", _p)
V11 = importlib.util.module_from_spec(_s); _s.loader.exec_module(V11)
motor.set_theme("seguridade")
chip, frame, ce, tag, ok_x, pdf_card = V11.chip, V11.frame, V11.ce, V11.tag, V11.ok_x, V11.pdf_card

MARCA = ""
ARQUIVO_FINAL = "seguridade_012_contribuinte_individual.mp4"
CARD_R = (140, 150, 1640, 690)

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
EMP, DOM, AVU, CI, ESP = PREST, GEST, ASSIST, "#3A3A3C", "#16A36A"


def rowbox(c, s, y, a, res=None, col=CI, ra=None, size=38, x=220, w=1480):
    if a <= 0:
        return
    rrect(c, x, y - 52, w, 104, 18, "#F7F7F5", a)
    text(c, s, x + 40, y + 14, size, "black", INK, a, align="left")
    if res:
        pill(c, res, x + w - 30, y, col, size=30, a=a if ra is None else ra, anchor="right", bounds=(0, 1920))


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 12 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    pessoas = [("01.a", "diarista"), ("01.b", "pastor"), ("01.c", "síndico"), ("01.d", "médico com consultório")]
    af = ep(t, C["01.f"], 0.6)
    for k, (cue, s) in enumerate(pessoas):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        y = 400 + d - 60 * af
        c.drawCircle(x, y - 50, 46, paint(lerp_col(k, af), a))
        rrect(c, x - 66, y + 6, 132, 110, 50, lerp_col(k, af), a)
        text(c, s, x, y + 170, 34, "black", INK, a)
    ae = ep(t, C["01.e"], 0.4) * (1 - af)
    text(c, "o que eles têm em comum?", W / 2, 720, 50, "black", GRAY, ae)
    chip(c, "CONTRIBUINTE INDIVIDUAL", W / 2, 690, CI, af, 50, 880)
    pill(c, "a categoria de quem SOBRA", W / 2, 820, ASSIST, size=32, a=ep(t, C["01.g"], 0.5), anchor="center")


def lerp_col(k, f):
    base = ["#A3A3A3", "#A3A3A3", "#A3A3A3", "#A3A3A3"][k]
    return mix(base, CI, f)


def b_logica(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 11, V", "O CONTRIBUINTE INDIVIDUAL", CI)
    a0 = ep(t, C["02.t"], 0.4)
    tag(c, "V", 860, 240, CI, a0, 50)
    text(c, "inciso", 1000, 258, 40, "black", GRAY, a0, align="left")
    rows = [("02.a", "trabalha POR CONTA PRÓPRIA", True), ("02.b", "SEM subordinação", False), ("02.c", "SEM intermediação", False)]
    for k, (cue, s, pos) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 370 + k * 90 + d
        check_icon(c, 520, y - 14, 26, a, GREEN if pos else RED, "check" if pos else "x")
        text(c, s, 570, y, 48, "black", INK, a, align="left")
    ad = ep(t, C["02.d"], 0.5)
    pill(c, "categoria RESIDUAL: quem não cabe em outro lugar, cai aqui", W / 2, 720, ASSIST, size=32, a=ad, anchor="center")


FLUXO = [("03.a", "Tem SUBORDINAÇÃO?", "EMPREGADO / DOMÉSTICO", EMP),
         ("03.b", "Tem INTERMEDIAÇÃO (OGMO/sindicato)?", "AVULSO", AVU),
         ("03.c", "Rural, economia familiar, até 4 módulos?", "SEGURADO ESPECIAL", ESP),
         ("03.d", "NENHUM DOS ANTERIORES", "CONTRIBUINTE INDIVIDUAL", CI)]


def b_fluxo(c, t, C, B):
    frame(c, t, B["start"], "MÉTODO PARA QUALQUER QUESTÃO", "O FLUXOGRAMA", GREEN)
    for k, (cue, q, r, col) in enumerate(FLUXO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 240 + k * 120 + d
        last = k == 3
        if k > 0:
            line(c, 260, y - 90, 260, y - 30, LIGHT, a, 4)
        c.drawCircle(260, y, 18, paint(col, a))
        text(c, q, 300, y + 14, 38 if not last else 42, "black", INK, a, align="left")
        arrow(c, 1160, y, 1230, y, GRAY, a, 4, 14)
        pill(c, r, 1250, y, col, size=30 if not last else 32, a=ep(t, C[cue] + 0.6, 0.4), bounds=(0, 1920))
    pill(c, "o contribuinte individual é sempre a ÚLTIMA hipótese", W / 2, 790, CI, size=30, a=ep(t, C["03.e"], 0.5), anchor="center")


def b_historia(c, t, C, B):
    frame(c, t, B["start"], "POR QUE O INCISO É O V?", "LEI 9.876/1999", CI)
    aa = ep(t, C["04.a"], 0.5)
    for k, (rom, s) in enumerate((("III", "empresário"), ("IV", "autônomo"))):
        x = 520 + k * 360
        a = aa
        if a <= 0:
            continue
        rrect(c, x - 150, 230, 300, 200, 22, RED if t > C["04.b"] else INK2, a, shadow=True)
        text_mid(c, rom, x, 290, 56, "black", "#FFFFFF", a)
        text_mid(c, s, x, 370, 34, "black", "#FFFFFF", a)
    ab = ep(t, C["04.b"], 0.5)
    pill(c, "REVOGADOS em 1999", 700, 480, RED, size=30, a=ab, anchor="center")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        arrow(c, 1060, 330, 1200, 330, INK, acc, 6, 20, progress=acc)
        tag(c, "V", 1220, 330, CI, acc, 56)
        text(c, "contribuinte", 1470, 310, 42, "black", CI, acc)
        text(c, "individual", 1470, 360, 42, "black", CI, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        ok_x(c, "empresário e autônomo como categorias", W / 2 - 30, 680, False, ad, 34)


def b_rol1(c, t, C, B):
    frame(c, t, B["start"], "QUEM É CONTRIBUINTE INDIVIDUAL", "RURAL, GARIMPO E RELIGIOSOS", CI)
    pill(c, "decore o CONTEÚDO, não a letra", W / 2, 220, ASSIST, size=28, a=ep(t, C["05.t"] + 1.5, 0.4), anchor="center")
    rowbox(c, "produtor rural em área MAIOR que 4 módulos fiscais", 330, ep(t, C["05.a"], 0.4))
    rowbox(c, "ou em área menor, mas COM EMPREGADOS", 450, ep(t, C["05.b"], 0.4))
    rowbox(c, "quem explora GARIMPO", 570, ep(t, C["05.c"], 0.4))
    rowbox(c, "MINISTRO DE CONFISSÃO RELIGIOSA: pastor, padre, freira", 690, ep(t, C["05.d"], 0.4))


def b_rol2(c, t, C, B):
    frame(c, t, B["start"], "QUEM É CONTRIBUINTE INDIVIDUAL", "NA EMPRESA, SEM SER EMPREGADO", CI)
    rows = [("06.a", "titular de FIRMA INDIVIDUAL"), ("06.b", "DIRETOR NÃO EMPREGADO"),
            ("06.c", "membro de CONSELHO DE ADMINISTRAÇÃO de S.A."), ("06.d", "SÓCIO que recebe pelo trabalho"),
            ("06.e", "SÍNDICO de condomínio, se REMUNERADO")]
    for k, (cue, s) in enumerate(rows):
        rowbox(c, s, 260 + k * 112, ep(t, C[cue], 0.4), size=36)


def b_rol3(c, t, C, B):
    frame(c, t, B["start"], "QUEM É CONTRIBUINTE INDIVIDUAL", "AS DUAS PORTAS MAIS LARGAS", CI)
    for k, (cue, s1, s2) in enumerate((("07.a", "serviço EVENTUAL a empresas", "sem relação de emprego"),
                                      ("07.b", "atividade econômica urbana", "POR CONTA PRÓPRIA"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        card(c, x - 340, 240 + d, 680, 340, a)
        c.drawCircle(x, 320 + d, 40, paint(CI, a))
        text(c, s1, x, 440 + d, 38, "black", INK, a)
        text(c, s2, x, 500 + d, 36, "black", CI, a)
    ac = ep(t, C["07.c"], 0.5)
    pill(c, "COM fins lucrativos OU NÃO", 1350, 680, ASSIST, size=32, a=ac, anchor="center")


def b_sindico(c, t, C, B):
    frame(c, t, B["start"], "CAMPEÃO DE PROVA", "O SÍNDICO", ASSIST)
    rows = [("08.a", "síndico REMUNERADO", "CONTRIBUINTE INDIVIDUAL", CI),
            ("08.b", "síndico com ISENÇÃO DA TAXA de condomínio", "CONTRIBUINTE INDIVIDUAL", CI),
            ("08.d", "síndico NÃO remunerado", "NÃO É SEGURADO por essa atividade", RED)]
    for k, (cue, s, r, col) in enumerate(rows):
        a = ep(t, C[cue], 0.4)
        ra = ep(t, C[{"08.a": "08.a", "08.b": "08.c", "08.d": "08.e"}[cue]] + (0.8 if cue == "08.a" else 0), 0.4)
        rowbox(c, s, 290 + k * 170, a, r, col, ra, 38)
    pill(c, "isenção da taxa = remuneração", 900, 545, ASSIST, size=26, a=ep(t, C["08.c"], 0.4), anchor="center")


def b_casos(c, t, C, B):
    frame(c, t, B["start"], "MAIS CASOS QUE CAEM", "TODOS CONTRIBUINTES INDIVIDUAIS", CI)
    items = [("09.a", "diarista (até 2 dias)"), ("09.b", "médico com consultório"), ("09.c", "feirante"),
             ("09.c", "camelô"), ("09.c", "cabeleireiro autônomo"), ("09.d", "MEI")]
    for k, (cue, s) in enumerate(items):
        a, d = rise(t, C[cue] + (0.5 * (k - 2) if cue == "09.c" else 0))
        if a <= 0:
            continue
        x = 420 + (k % 3) * 540
        y = 300 + (k // 3) * 160 + d
        rrect(c, x - 240, y - 55, 480, 110, 22, CI, a, shadow=True)
        text_mid(c, s, x, y, 34, "black", "#FFFFFF", a)
    af = ep(t, C["09.f"], 0.5)
    if af > 0:
        rrect(c, 380, 640, 1160, 130, 22, mix("#FFFFFF", ASSIST, 0.12), af)
        text(c, "motorista de aplicativo → contribuinte individual", W / 2, 695, 36, "black", INK, af)
        text(c, "atenção: tema com discussão na Justiça", W / 2, 745, 30, "black", ASSIST, ep(t, C["09.f"] + 2.5, 0.4))


def b_rural(c, t, C, B):
    frame(c, t, B["start"], "A FRONTEIRA COM O", "SEGURADO ESPECIAL", CI)
    aa = ep(t, C["10.a"], 0.5)
    ab = ep(t, C["10.b"], 0.5)
    # régua de módulos fiscais
    if aa > 0:
        for k in range(8):
            x = 300 + k * 160
            rrect(c, x, 260, 150, 90, 12, ESP if k < 4 else CI, aa * ep(t, C["10.a"] + 0.1 * k, 0.3))
            text_mid(c, str(k + 1), x + 75, 305, 36, "black", "#FFFFFF", aa)
        line(c, 300 + 4 * 160 - 5, 230, 300 + 4 * 160 - 5, 380, RED, aa, 5)
        text(c, "4 módulos fiscais", 300 + 4 * 160 - 5, 420, 30, "black", RED, aa)
        text(c, "até 4: pode ser ESPECIAL", 600, 470, 30, "bold", ESP, aa)
        text(c, "mais de 4: CONTRIBUINTE INDIVIDUAL", 1290, 470, 30, "bold", CI, aa)
    if ab > 0:
        rowbox(c, "até 4 módulos, mas COM EMPREGADO PERMANENTE", 580, ab, "CONTRIBUINTE INDIVIDUAL", CI, ep(t, C["10.b"] + 1.2, 0.4), 34)
    pill(c, "passou de 4 OU tem empregado permanente → contribuinte individual", W / 2, 760, ASSIST, size=28,
         a=ep(t, C["10.c"], 0.5), anchor="center")


def b_filiacao(c, t, C, B):
    frame(c, t, B["start"], "COMO ELE ENTRA NO RGPS", "FILIAÇÃO E INSCRIÇÃO", CI)
    for k, (cue, lab, val, sub, col) in enumerate((("11.a", "FILIAÇÃO", "AUTOMÁTICA", "trabalhou com remuneração, está filiado", PREST),
                                                  ("11.b", "INSCRIÇÃO", "POR ELE MESMO", "o próprio segurado faz", CI))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        card(c, x - 340, 260 + d, 680, 360, a)
        text(c, lab, x, 340 + d, 34, "black", GRAY, a, tracking=2)
        text(c, val, x, 450 + d, 58, "black", col, a)
        text(c, sub, x, 530 + d, 30, "bold", INK2, a)


def b_recolhe(c, t, C, B):
    frame(c, t, B["start"], "QUEM RECOLHE?", "DEPENDE!", ASSIST)
    am = ep(t, C["12.m"], 0.5) * (1 - ep(t, C["12.b"], 0.4))
    if am > 0:
        pill(c, "C · F recolhem", W / 2, 360, CI, size=56, a=am, anchor="center")
        text(c, "a banca adora este detalhe", W / 2, 500, 40, "black", ASSIST, ep(t, C["12.a"], 0.4) * am)
    ab, db = rise(t, C["12.b"])
    if ab > 0:
        card(c, 220, 220 + db, 700, 470, ab)
        text(c, "presta serviço a uma", 570, 290 + db, 34, "bold", GRAY, ab)
        text(c, "EMPRESA", 570, 360 + db, 60, "black", INK, ab)
        chip(c, "a EMPRESA recolhe", 570, 480 + db, PREST, ep(t, C["12.c"], 0.4), 36, 520)
        text(c, "o risco NÃO é dele", 570, 610 + db, 36, "black", GREEN, ep(t, C["12.c"] + 1.4, 0.4))
    ad, dd = rise(t, C["12.d"])
    if ad > 0:
        card(c, 1000, 220 + dd, 700, 470, ad)
        text(c, "presta a PESSOA FÍSICA", 1350, 290 + dd, 34, "bold", GRAY, ad)
        text(c, "ou CONTA PRÓPRIA", 1350, 360 + dd, 50, "black", INK, ad)
        chip(c, "ELE MESMO recolhe", 1350, 480 + dd, CI, ep(t, C["12.e"], 0.4), 36, 520)
        text(c, "o risco É dele", 1350, 610 + dd, 36, "black", RED, ep(t, C["12.e"] + 1.4, 0.4))


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 160, 1520, 700)
    items = [("13.p1", "13.r1", "o síndico é SEMPRE contribuinte individual", False, "só se REMUNERADO"),
             ("13.p2", "13.r2", "o ministro de confissão religiosa é FACULTATIVO", False, "é contribuinte individual"),
             ("13.p3", "13.r3", "a filiação do CI depende de INSCRIÇÃO PRÉVIA", False, "a filiação é AUTOMÁTICA"),
             ("13.p4", "13.r4", "o diretor não empregado é contribuinte individual", True, "art. 11, V")]
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
    ce(c, t, C, "14.e", "14.r", "14.x",
       ["O contribuinte individual que presta serviço a", "empresa é SEMPRE responsável pelo recolhimento",
        "da própria contribuição."],
       "ERRADO", False, "a EMPRESA retém e recolhe", "SEMPRE?", size=44)


ALTS = [("A", "o diretor EMPREGADO de sociedade anônima", "16.xa", "empregado"),
        ("B", "o síndico de condomínio remunerado", None, ""),
        ("C", "o contratado por empresa de trabalho temporário", "16.xc", "empregado"),
        ("D", "o portuário intermediado pelo OGMO", "16.xd", "avulso"),
        ("E", "a faxineira que trabalha 4 dias por semana na mesma casa", "16.xe", "doméstica")]


def b_q_mult(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO DE PROVA", "É CONTRIBUINTE INDIVIDUAL:", CI)
    card(c, 200, 160, 1520, 700)
    aok = ep(t, C["16.ok"], 0.5)
    for k, (L, s, cx, why) in enumerate(ALTS):
        a, d = rise(t, C[f"15.{L.lower()}"])
        if a <= 0:
            continue
        y = 260 + k * 110 + d
        ok = cx is None
        if ok and aok > 0:
            rrect(c, 240, y - 48, 1440, 90, 16, GREEN, 0.15 * aok)
        badge_num(c, L, 300, y - 10, a, 26, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cx], 0.4) if cx else 0
        text(c, s, 350, y + 2, 36, "black", INK, a * (1 - 0.5 * ax), align="left")
        if ax > 0:
            strike(c, 346, y - 10, 354 + text_w(s, "black", 36), y - 10, ax, RED, ax)
            pill(c, why, 1660, y - 8, RED, size=26, a=ax, anchor="right", bounds=(0, 1920))
    pause_t = C["15.end"] - 1.9
    a_p = ep(t, pause_t, 0.3) * (1 - prog(t, pause_t + 2.0, 0.4))
    if a_p > 0:
        pill(c, "PAUSE E TENTE", W / 2, 820, ASSIST, size=32, a=a_p, anchor="center")
    if aok > 0:
        pill(c, "Letra B", W / 2, 820, GREEN, size=36, a=aok, anchor="center")


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("17.a", "por conta própria, sem subordinação e sem intermediação: RESIDUAL"),
            ("17.b", "Lei 9.876/1999: empresário + autônomo → contribuinte individual"),
            ("17.c", "síndico: só se REMUNERADO (isenção da taxa conta)"),
            ("17.d", "rural: mais de 4 módulos OU com empregado permanente"),
            ("17.e", "serviço a EMPRESA: a empresa recolhe · senão, ele mesmo")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 270 + k * 112 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 36, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["18.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Segurado especial", W / 2, 430, 64, "black", INK, a)
        pill(c, "o rural que mais cai na prova", W / 2, 540, ESP, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a, anchor="center")
    ap = fw(t, C["18.pdf"], C["18.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["18.pdf"], 0.5)) * 20)
    cta(c, t, C["18.like"], C["18.sub"], C["18.bell"], C["18.com"], C["18.bye"], "Qual desses casos você não sabia?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, logica=b_logica, fluxo=b_fluxo, historia=b_historia, rol1=b_rol1, rol2=b_rol2, rol3=b_rol3,
              sindico=b_sindico, casos=b_casos, rural=b_rural, filiacao=b_filiacao, recolhe=b_recolhe,
              pegadinhas=b_pegadinhas, q_ce=b_q_ce, q_mult=b_q_mult, resumo=b_resumo, cta=b_cta)
