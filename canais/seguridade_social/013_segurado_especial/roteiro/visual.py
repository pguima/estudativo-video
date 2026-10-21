"""Visual do vídeo Seguridade 013 — Segurado especial (Lei 8.213, art. 11, VII e §§; CF, art. 195, §8º). Tema 'seguridade'.
Cores: segurado especial = verde (#16A36A, como no 012) · contribuinte individual = cinza-escuro · lei = verde-petróleo.
Reaproveita do 012 (rowbox), do 011 (chip, frame, lei_card) e do 010 (ce, tag, ok_x, pdf_card)."""
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
lei_card = V12.V11.lei_card

MARCA = ""
ARQUIVO_FINAL = "seguridade_013_segurado_especial.mp4"
CARD_R = (140, 150, 1640, 690)

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
ESP, CI = "#16A36A", "#3A3A3C"


def numero(c, n, sub, cx, cy, a, col=ESP, w=230, h=230, size=96):
    """quadrado colorido com um número grande e a legenda embaixo"""
    if a <= 0:
        return
    sc = 0.85 + 0.15 * ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(sc, sc)
    rrect(c, -w / 2, -h / 2, w, h, 26, col, a, shadow=True)
    text_mid(c, n, 0, -18, size, "black", "#FFFFFF", a)
    text_mid(c, sub, 0, h / 2 - 42, 24, "bold", "#FFFFFF", a)
    c.restore()


# ======================================================================
def b_hook(c, t, C, B):
    a0 = ep(t, B["start"], 0.5)
    pill(c, "CONCURSO INSS · AULA 13 · TEMPORADA 2", W / 2, 190, BLUE, size=30, a=a0, anchor="center")
    fatos = [("01.a", "sítio de 3 módulos fiscais", "com a esposa e o filho", ESP),
             ("01.b", "5 trabalhadores na safra", "contratados", ASSIST),
             ("01.c", "recebe Bolsa Família", "programa assistencial", GEST),
             ("01.d", "é vereador", "do município", RED)]
    for k, (cue, s1, s2, col) in enumerate(fatos):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 140 + (k % 2) * 830
        y = 270 + (k // 2) * 170 + d
        rrect(c, x, y, 780, 140, 24, "#FFFFFF", a, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 14, 140), paint(col, a))
        text(c, s1, x + 60, y + 62, 40, "black", INK, a, align="left")
        text(c, s2, x + 60, y + 108, 28, "bold", GRAY, a, align="left")
    ae = ep(t, C["01.e"], 0.5)
    chip(c, "AINDA É SEGURADO ESPECIAL?", W / 2, 700, ESP, ae, 46, 960)
    pill(c, "resolvemos juntos no fim da aula", W / 2, 820, ASSIST, size=30, a=ep(t, C["01.f"], 0.5), anchor="center")


def b_base(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 11, VII", "O SEGURADO ESPECIAL", ESP)
    a0 = ep(t, C["02.t"], 0.4)
    tag(c, "VII", 840, 250, ESP, a0, 52)
    text(c, "inciso", 1010, 268, 40, "black", GRAY, a0, align="left")
    ab, db = rise(t, C["02.b"])
    if ab > 0:
        text(c, "o único com base PRÓPRIA na Constituição", W / 2, 400, 40, "black", INK, ep(t, C["02.a"], 0.4))
        rrect(c, 560, 450 + db, 800, 130, 24, PREST, ab, shadow=True)
        text_mid(c, "CF, art. 195, §8º", W / 2, 515 + db, 54, "black", "#FFFFFF", ab)
    ok_x(c, "a categoria MAIS DETALHADA do RGPS", W / 2 - 30, 660, True, ep(t, C["02.c"], 0.5), 32)
    pill(c, "e uma das que MAIS CAEM", W / 2, 790, ASSIST, size=30, a=ep(t, C["02.d"], 0.5), anchor="center")


def b_elementos(c, t, C, B):
    frame(c, t, B["start"], "O CONCEITO", "OS 4 ELEMENTOS", ESP)
    rows = [("03.a", "PESSOA FÍSICA", ""),
            ("03.b", "MORA no imóvel rural", "ou em aglomerado próximo"),
            ("03.c", "INDIVIDUALMENTE ou em economia familiar", ""),
            ("03.d", "se encaixa numa das CONDIÇÕES da lei", "")]
    for k, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 120 + d
        badge_num(c, str(k + 1), 300, y - 14, a, 32, bg=ESP)
        text(c, s, 360, y, 42, "black", INK, a, align="left")
        if sub:
            text(c, sub, 360 + text_w(s, "black", 42) + 24, y, 32, "bold", GRAY, a, align="left")


def b_quem(c, t, C, B):
    frame(c, t, B["start"], "QUEM PODE SER", "AS CONDIÇÕES DA LEI", ESP)
    cards = [("04.a", "PRODUTOR", "agropecuária até 4 MF", "proprietário · parceiro · meeiro · arrendatário"),
             ("04.b", "SERINGUEIRO", "e extrativista vegetal", "principal meio de vida"),
             ("04.c", "PESCADOR", "ARTESANAL", "profissão habitual"),
             ("04.d", "A FAMÍLIA", "cônjuge · companheiro", "filho MAIOR DE 16 que trabalhe")]
    for k, (cue, s1, s2, s3) in enumerate(cards):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + (k % 2) * 780
        y = 210 + (k // 2) * 240 + d
        rrect(c, x, y, 760, 210, 24, mix("#FFFFFF", ESP, 0.08), a)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 14, 210), paint(ESP, a))
        text(c, s1, x + 50, y + 70, 44, "black", ESP, a, align="left")
        text(c, s2, x + 50, y + 125, 34, "black", INK, a, align="left")
        text(c, s3, x + 50, y + 175, 26, "bold", GRAY, a, align="left")


def b_sozinho(c, t, C, B):
    frame(c, t, B["start"], "PALAVRINHA QUE CAI", "INDIVIDUALMENTE OU...", ASSIST)
    a0 = ep(t, C["05.t"], 0.4)
    partes = [("“individualmente ", INK), ("OU", ASSIST), (" em economia familiar”", INK)]
    x = W / 2 - sum(text_w(s, "black", 60) for s, _ in partes) / 2
    for s, col in partes:
        text(c, s, x, 330, 60, "black", col, a0, align="left")
        x += text_w(s, "black", 60)
    aa, da = rise(t, C["05.a"])
    if aa > 0:
        c.drawCircle(560, 480 + da, 40, paint(ESP, aa))
        rrect(c, 502, 530 + da, 116, 100, 46, ESP, aa)
        text(c, "produtor SOZINHO", 680, 560 + da, 44, "black", INK, aa, align="left")
    pill(c, "PODE ser segurado especial", 680, 620, ESP, size=34, a=ep(t, C["05.b"], 0.4), bounds=(0, 1920))
    pill(c, "a família NÃO é obrigatória", W / 2, 780, RED, size=32, a=ep(t, C["05.c"], 0.5), anchor="center")


def b_economia(c, t, C, B):
    frame(c, t, B["start"], "LEI 8.213 · ART. 11, §1º", "REGIME DE ECONOMIA FAMILIAR", ESP)
    rows = [("06.a", "trabalho da família INDISPENSÁVEL à subsistência"),
            ("06.b", "e ao desenvolvimento do NÚCLEO FAMILIAR"),
            ("06.c", "MÚTUA DEPENDÊNCIA e colaboração")]
    for k, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 90 + d
        check_icon(c, 280, y - 14, 24, a, ESP)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")
    ad, dd = rise(t, C["06.d"])
    if ad > 0:
        rrect(c, 240, 500 + dd, 1440, 110, 22, RED, ad, shadow=True)
        text_mid(c, "SEM EMPREGADOS PERMANENTES", W / 2, 555 + dd, 52, "black", "#FFFFFF", ad)
        pill(c, "ponto de ouro", 1650, 500 + dd, ASSIST, size=24, a=ad, anchor="right", bounds=(0, 1920))
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        ok_x(c, "empregado PERMANENTE descaracteriza", 650, 690, False, ae, 28)
        ok_x(c, "ajuda EVENTUAL não", 1330, 690, True, ep(t, C["06.e"] + 2.2, 0.4), 28)


def b_modulo(c, t, C, B):
    frame(c, t, B["start"], "O QUE É", "MÓDULO FISCAL?", ESP)
    aa = ep(t, C["07.a"], 0.5)
    text(c, "medida agrária fixada POR MUNICÍPIO", W / 2, 270, 44, "black", INK, aa)
    ab = ep(t, C["07.b"], 0.6)
    if ab > 0:
        x0, x1 = 300, 1620
        line(c, x0, 400, x0 + (x1 - x0) * ab, 400, ESP, ab, 10)
        for v, xf in ((5, 0.0), (110, 1.0)):
            x = x0 + (x1 - x0) * xf
            c.drawCircle(x, 400, 18, paint(ESP, ab))
            text(c, f"{v} hectares", x, 470, 38, "black", ESP, ab)
        text(c, "conforme a região", W / 2, 470, 30, "bold", GRAY, ab)
    ac = ep(t, C["07.c"], 0.4)
    if ac > 0:
        rrect(c, 340, 560, 1240, 120, 22, "#F7F7F5", ac)
        text_mid(c, "“até 4 hectares”", 680, 620, 48, "black", INK, ac)
        ad = ep(t, C["07.d"], 0.4)
        if ad > 0:
            strike(c, 480, 620, 880, 620, ad, RED, ad)
            pill(c, "ERRADO: 4 MÓDULOS FISCAIS", 1540, 620, RED, size=30, a=ad, anchor="right", bounds=(0, 1920))


NUMS = [("08.a", "4", "módulos fiscais", ESP), ("08.b", "16", "anos do filho", PREST),
        ("08.c", "120", "pessoas/dia safra", ASSIST), ("08.d", "120", "dias trabalho fora", ASSIST),
        ("08.e", "120", "dias turismo rural", ASSIST), ("08.f", "50%", "cessão do imóvel", GEST)]


def b_numeros(c, t, C, B):
    frame(c, t, B["start"], "DECORE COMO UM BLOCO", "OS NÚMEROS DO ESPECIAL", ESP)
    ag = ep(t, C["08.g"], 0.4)
    for k, (cue, n, sub, col) in enumerate(NUMS):
        a = ep(t, C[cue], 0.45)
        cx = 300 + k * 264
        cy = 400 - 20 * ag * (1 if n == "120" else 0)
        numero(c, n, sub, cx, cy, a, col, 240, 240, 92 if len(n) < 3 else 80)
    if ag > 0:
        text(c, "4 · 16 · 3 × 120 · 50%", W / 2, 640, 70, "black", INK, ag)
    pill(c, "confira no texto atualizado: os limites já mudaram", W / 2, 760, RED, size=26,
         a=ep(t, C["08.h"], 0.5), anchor="center")


SAFRA = [("09.b", 1, 120), ("09.c", 4, 30), ("09.d", 10, 12), ("09.f", 6, 25)]


def b_safra(c, t, C, B):
    frame(c, t, B["start"], "A CONTA DA SAFRA", "PESSOAS × DIAS ≤ 120", ASSIST)
    aa = ep(t, C["09.a"], 0.5)
    text(c, "no ano civil, corridos ou intercalados", W / 2, 260, 34, "bold", GRAY, aa)
    for k, (cue, p, d) in enumerate(SAFRA):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 360 + k * 105 + dy
        passou = p * d > 120
        rrect(c, 320, y - 45, 1280, 90, 18, mix("#FFFFFF", RED, 0.10) if passou else "#F7F7F5", a)
        text(c, f"{p} {'pessoa' if p == 1 else 'pessoas'} × {d} dias", 380, y + 14, 40, "black", INK, a, align="left")
        ar = ep(t, C[cue] + (1.4 if passou else 1.0), 0.4)
        text(c, f"= {p * d}", 1180, y + 14, 44, "black", RED if passou else ESP, ar, align="right")
        check_icon(c, 1260, y, 24, ar, RED if passou else ESP, "x" if passou else "check")
        if passou:
            pill(c, "PASSOU!", 1560, y, RED, size=28, a=ep(t, C["09.g"], 0.4), anchor="right", bounds=(0, 1920))
    pill(c, "tudo dentro do limite", 1560, 465, ESP, size=24, a=ep(t, C["09.e"], 0.4) * (1 - ep(t, C["09.f"], 0.3)),
         anchor="right", bounds=(0, 1920))


def b_nao_desc(c, t, C, B):
    frame(c, t, B["start"], "ART. 11, §8º · NÃO DESCARACTERIZA", "CONTINUA SEGURADO ESPECIAL", GREEN)
    rows = [("10.a", "ceder a terceiros até 50% do imóvel"), ("10.b", "turismo rural com hospedagem, até 120 dias/ano"),
            ("10.c", "participar de COOPERATIVA"), ("10.d", "beneficiamento ARTESANAL da produção")]
    for k, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 92 + d
        check_icon(c, 280, y - 14, 24, a, GREEN)
        text(c, s, 330, y, 38, "bold", INK, a, align="left")
    ae, de = rise(t, C["10.e"])
    if ae > 0:
        rrect(c, 240, 600 + de, 1440, 110, 22, GREEN, ae, shadow=True)
        text_mid(c, "BOLSA FAMÍLIA / programa assistencial: NÃO descaracteriza", W / 2, 655 + de, 40, "black", "#FFFFFF", ae)
    pill(c, "cai muito", 1650, 600, ASSIST, size=26, a=ep(t, C["10.f"], 0.4), anchor="right", bounds=(0, 1920))


def b_outras_rendas(c, t, C, B):
    frame(c, t, B["start"], "ART. 11, §9º · OUTRAS RENDAS", "VEREADOR SIM, PREFEITO NÃO", ASSIST)
    rows = [("11.a", "trabalho remunerado fora, até 120 dias/ano", True),
            ("11.b", "dirigente SINDICAL dos trabalhadores rurais", True),
            ("11.c", "VEREADOR do município onde trabalha", True)]
    for k, (cue, s, ok) in enumerate(rows):
        rowbox(c, s, 260 + k * 120, ep(t, C[cue], 0.4), "PODE", GREEN, ep(t, C[cue] + 1.6, 0.4), 36)
    ae = ep(t, C["11.e"], 0.4)
    rowbox(c, "PREFEITO, deputado, senador", 620, ep(t, C["11.d"], 0.4), "NÃO", RED, ae, 36)
    pill(c, "vereador SIM · prefeito NÃO", W / 2, 790, INK, size=32, a=ep(t, C["11.f"], 0.5), anchor="center")


def b_exclusao(c, t, C, B):
    frame(c, t, B["start"], "ART. 11, §10 · QUANDO PERDE", "A BANCA COBRA A DATA", RED)
    for k, (cue, cr, top, s1, s2, when, col) in enumerate((
            ("12.a", "12.b", "CONDIÇÃO PRÓPRIA", "deixou os requisitos, virou outro", "segurado ou entrou em sociedade",
             "1º dia do MÊS DO FATO", RED),
            ("12.c", "12.d", "EXCESSO DE LIMITE", "estourou um dos 120", "(safra, trabalho fora, turismo)",
             "1º dia do MÊS SEGUINTE", ASSIST))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        card(c, x - 350, 230 + d, 700, 420, a)
        text(c, top, x, 300 + d, 36, "black", col, a, tracking=1.5)
        text(c, s1, x, 380 + d, 32, "bold", INK, a)
        text(c, s2, x, 425 + d, 32, "bold", INK, a)
        chip(c, when, x, 550 + d, col, ep(t, C[cr], 0.4), 34, 600)
    pill(c, "condição própria: mês do fato · excesso: mês seguinte", W / 2, 760, INK, size=28,
         a=ep(t, C["12.e"], 0.5), anchor="center")


def b_contribuicao(c, t, C, B):
    frame(c, t, B["start"], "CF, ART. 195, §8º · ART. 39", "COMO ELE CONTRIBUI", PREST)
    aa = ep(t, C["13.a"], 0.4)
    if aa > 0:
        text(c, "salário de contribuição", 560, 290, 40, "black", GRAY, aa)
        strike(c, 330, 276, 790, 276, aa, RED, ep(t, C["13.a"] + 0.4, 0.4))
    ab, db = rise(t, C["13.b"])
    if ab > 0:
        rrect(c, 960, 220 + db, 640, 150, 24, PREST, ab, shadow=True)
        text_mid(c, "alíquota sobre a", 1280, 270 + db, 30, "bold", "#FFFFFF", ab)
        text_mid(c, "COMERCIALIZAÇÃO DA PRODUÇÃO", 1280, 320 + db, 32, "black", "#FFFFFF", ab)
    for k, (cue, top, val, sub, col) in enumerate((
            ("13.c", "SÓ SOBRE A PRODUÇÃO", "1 salário mínimo", "art. 39, I", ESP),
            ("13.d", "+ FACULTATIVA (como CI)", "ACIMA do mínimo", "art. 39, II", GEST))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 570 + k * 780
        card(c, x - 340, 430 + d, 680, 240, a)
        text(c, top, x, 495 + d, 30, "black", GRAY, a, tracking=1.5)
        text(c, val, x, 580 + d, 50, "black", col, ep(t, C[cue] + (0 if k == 0 else 2.6), 0.4))
        text(c, sub, x, 635 + d, 26, "bold", INK2, a)


def b_comprova(c, t, C, B):
    frame(c, t, B["start"], "O DETALHE QUE MUDA TUDO", "COMPROVAÇÃO, NÃO RECOLHIMENTO", ESP)
    aa = ep(t, C["14.a"], 0.4)
    ok_x(c, "conta contribuições", 560, 300, False, aa, 34)
    ab = ep(t, C["14.b"], 0.4)
    ok_x(c, "COMPROVA ATIVIDADE RURAL", 1300, 300, True, ab, 34)
    ac, dc = rise(t, C["14.c"])
    if ac > 0:
        x0, x1, y = 340, 1580, 470 + dc
        line(c, x0, y, x1, y, LIGHT, ac, 6)
        for k in range(12):
            if k in (4, 5, 8):
                continue
            xs = x0 + k * (x1 - x0) / 12
            rrect(c, xs + 6, y - 26, (x1 - x0) / 12 - 12, 52, 10, ESP, ac * ep(t, C["14.c"] + 0.08 * k, 0.3))
        arrow(c, x1, y, x1 + 70, y, INK, ac, 4, 14)
        text(c, "pedido", x1 + 40, y + 70, 28, "black", INK, ac)
        text(c, "ainda que DESCONTÍNUA · período igual à carência", W / 2, y + 120, 32, "bold", INK2, ac)
    pill(c, "regime de COMPROVAÇÃO, não de recolhimento mensal", W / 2, 780, ESP, size=28,
         a=ep(t, C["14.d"], 0.5), anchor="center")


def b_pegadinhas(c, t, C, B):
    head(c, t, B["start"], "PEGADINHAS", "CERTO OU ERRADO?", RED)
    card(c, 200, 160, 1520, 700)
    items = [("15.p1", "15.r1", "o filho MENOR de 16 que trabalha com o grupo é especial", False, "tem que ser MAIOR de 16"),
             ("15.p2", "15.r2", "empregado permanente NÃO descaracteriza", False, "DESCARACTERIZA"),
             ("15.p3", "15.r3", "o especial NUNCA recebe mais que 1 salário mínimo", False, "pode, se contribuir facultativamente"),
             ("15.p4", "15.r4", "o pescador artesanal pode ser segurado especial", True, "art. 11, VII")]
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
    ce(c, t, C, "16.e", "16.r", "16.x",
       ["O segurado especial que exerce atividade remunerada", "por 150 dias no ano civil é excluído a contar do",
        "1º dia do mês da ocorrência."],
       "ERRADO", False, "excesso de limite: vale o MÊS SEGUINTE", "NÍVEL AVANÇADO", size=42)


CASO = [("17.a", "área de 3 módulos fiscais", "até 4"),
        ("17.b", "5 trabalhadores × 20 dias", "100 ≤ 120"),
        ("17.c", "recebe Bolsa Família", "não descaracteriza"),
        ("17.d", "vereador do município", "ressalva do §9º"),
        ("17.e", "filho de 17 anos", "maior de 16")]


def b_caso(c, t, C, B):
    head(c, t, B["start"], "O CASO DO JOÃO", "ITEM POR ITEM", ESP)
    card(c, 200, 160, 1520, 700)
    for k, (cue, s, why) in enumerate(CASO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 92 + d
        badge_num(c, str(k + 1), 280, y - 12, a, 24, bg=INK)
        text(c, s, 330, y, 36, "black", INK, a, align="left")
        ar = ep(t, C[cue] + 1.8, 0.4)
        text(c, why, 1450, y, 30, "bold", ESP, ar, align="right")
        check_icon(c, 1520, y - 12, 24, ar, ESP)
    af = ep(t, C["17.f"], 0.5) * (1 - ep(t, C["17.g"], 0.4))
    chip(c, "CONTINUAM SEGURADOS ESPECIAIS", W / 2, 760, ESP, af, 40, 1000)
    ag = ep(t, C["17.g"], 0.5)
    if ag > 0:
        rrect(c, 360, 705, 1200, 110, 22, mix("#FFFFFF", RED, 0.12), ag)
        text_mid(c, "e se fossem 7 × 20 = 140?  AÍ PERDIA", W / 2, 760, 40, "black", RED, ag)


def b_resumo(c, t, C, B):
    head(c, t, B["start"], "RESUMO", "O QUE LEVAR PARA A PROVA", GREEN)
    card(c, 200, 160, 1520, 700)
    rows = [("18.a", "art. 11, VII, com base na CF (art. 195, §8º)"),
            ("18.b", "individualmente OU em família · SEM empregados permanentes"),
            ("18.c", "números: 4 · 16 · 3 × 120 · 50%"),
            ("18.d", "vereador SIM, prefeito NÃO"),
            ("18.e", "contribui sobre a VENDA DA PRODUÇÃO · benefício de 1 SM")]
    for k, (cue, s) in enumerate(rows):
        a, dy = rise(t, C[cue])
        y = 270 + k * 112 + dy
        check_icon(c, 280, y - 12, 24, a, GREEN)
        text(c, s, 330, y, 36, "bold", INK, a, align="left")


def b_cta(c, t, C, B):
    a = fw(t, B["start"], C["19.pdf"] - 0.3)
    if a > 0:
        pill(c, "PRÓXIMA AULA", W / 2, 300, BLUE, size=30, a=a, anchor="center")
        text(c, "Facultativo e excluídos", W / 2, 430, 64, "black", INK, a)
        pill(c, "o “quem é quem” de todos os segurados", W / 2, 540, GEST, size=30, a=ep(t, B["start"] + 1.5, 0.4) * a,
             anchor="center")
    ap = fw(t, C["19.pdf"], C["19.like"] - 0.3)
    if ap > 0:
        pdf_card(c, ap, (1 - ep(t, C["19.pdf"], 0.5)) * 20)
    cta(c, t, C["19.like"], C["19.sub"], C["19.bell"], C["19.com"], C["19.bye"], "Você acertou o caso do João?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, base=b_base, elementos=b_elementos, quem=b_quem, sozinho=b_sozinho, economia=b_economia,
              modulo=b_modulo, numeros=b_numeros, safra=b_safra, nao_desc=b_nao_desc, outras_rendas=b_outras_rendas,
              exclusao=b_exclusao, contribuicao=b_contribuicao, comprova=b_comprova, pegadinhas=b_pegadinhas,
              q_ce=b_q_ce, caso=b_caso, resumo=b_resumo, cta=b_cta)
