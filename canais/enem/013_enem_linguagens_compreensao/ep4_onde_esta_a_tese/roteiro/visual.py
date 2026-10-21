"""Visual — Compreensão Global e Tese, Episódio 4: Onde a tese se esconde (tema claro).
Analogias: TRAILER (dedutivo) · FILME DE DETETIVE (indutivo) · FOTO SEM LEGENDA (implícito) ·
"Há quem diga que…" = balão do ADVERSÁRIO, riscado quando chega o "mas".
Três esquemas: dedutivo (tese em cima → apoios), indutivo (casos → seta → tese), implícito (fatos que se juntam numa tese pontilhada).
Questões 2 e 3: texto inteiro com marca-texto palavra a palavra + etiqueta com o nome do erro em cada alternativa.
Cores: azul = tese/definição · verde = pista/palavra-sinal · âmbar = armadilha · vermelho = erro · roxo = regra.
Peças reaproveitadas dos eps. 1 (V1), 2 (V2) e 3 (V3).
"""
import importlib.util
import json
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

HERE = Path(__file__).resolve().parent
SERIE = HERE.parent.parent


def _load(nome, path):
    spec = importlib.util.spec_from_file_location(nome, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V3 = _load("visual_ep3", SERIE / "ep3_alternativas_armadilha" / "roteiro" / "visual.py")
V2, V1 = V3.V2, V3.V1
motor.set_theme("claro")
try:   # a leitura (classe do ep. 2) usa os tempos deste episódio
    V2._SC = {s["id"]: s for s in json.load(open(HERE.parent / "audio" / "tempos.json", encoding="utf-8"))["scenes"]}
except Exception:
    V2._SC = {}

MARCA = ""
ARQUIVO_FINAL = "enem_linguagens_compreensao_ep4_onde_esta_a_tese.mp4"
CARD_R = (140, 150, 1640, 690)
C_OUTRO = "#8E8E93"

wrap, para, which, frame, head_seq, boxed, regra, selo, pause_timer = (
    V1.wrap, V1.para, V1.which, V1.frame, V1.head_seq, V1.boxed, V1.regra, V1.selo, V1.pause_timer)
wa_bubble, notas, Leitura, colored, person = V2.wa_bubble, V2.notas, V2.Leitura, V2.colored, V1.person


# ======================================================================
# esquemas
# ======================================================================

def caixa(c, x, y, w, h, col, a, s="", size=24, dashed=False, fill=0.12):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, col, a * fill)
    p = paint(col, a, stroke=4)
    if dashed:
        p.setPathEffect(skia.DashPathEffect.Make([12, 8], 0))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), p)
    if s:
        text_mid(c, s, x + w / 2, y + h / 2, size, "black", col, a)


def esq_dedutivo(c, cx, y, a_tese, a_apoio, a_retoma, w=420):
    caixa(c, cx - w / 2, y, w, 70, BLUE, a_tese, "TESE", 28)
    for k in range(3):
        x = cx - w / 2 + k * (w / 3) + 6
        aa = a_apoio * clamp((a_apoio * 3 - k))
        line(c, cx, y + 70, x + w / 6 - 6, y + 120, LIGHT, aa, 3)
        caixa(c, x, y + 120, w / 3 - 12, 60, INK2, aa, "apoio", 20, fill=0.06)
    caixa(c, cx - w / 2, y + 220, w, 56, BLUE, a_retoma, "tese de novo", 22, fill=0.05)


def esq_indutivo(c, cx, y, a_casos, a_tese, w=420):
    for k in range(3):
        aa = a_casos * clamp((a_casos * 3 - k))
        caixa(c, cx - w / 2 + k * (w / 3) + 6, y, w / 3 - 12, 60, INK2, aa, f"caso {k + 1}", 20, fill=0.06)
    arrow(c, cx, y + 76, cx, y + 140, GRAY, a_tese, 4, 16, progress=a_tese)
    caixa(c, cx - w / 2, y + 160, w, 70, BLUE, a_tese, "TESE", 28)


def esq_implicito(c, t, cx, y, a_fatos, a_tese, w=420):
    pts = [(-150, 0), (120, 20), (-60, 70), (160, 110), (-170, 120)]
    for k, (dx, dy) in enumerate(pts):
        aa = a_fatos * clamp((a_fatos * 5 - k))
        px, py = cx + dx * (1 - 0.35 * a_tese), y + dy * (1 - 0.3 * a_tese)
        c.drawCircle(px, py + 10, 14, paint(INK2, aa))
        line(c, px, py + 10, cx, y + 210, LIGHT, aa * a_tese, 2)
    caixa(c, cx - w / 2, y + 180, w, 70, BLUE, a_tese, "tese (ninguém escreveu)", 24, dashed=True, fill=0.04)


# ======================================================================
# desenhos das analogias
# ======================================================================

def trailer(c, x, y, a, a_fim):
    if a <= 0:
        return
    rrect(c, x, y, 640, 170, 12, "#1C1C1E", a, shadow=True)
    for k in range(9):
        rrect(c, x + 16 + k * 70, y + 10, 34, 16, 4, "#FFFFFF", a * 0.8)
        rrect(c, x + 16 + k * 70, y + 144, 34, 16, 4, "#FFFFFF", a * 0.8)
    for k in range(4):
        fx = x + 20 + k * 155
        on = k == 0
        rrect(c, fx, y + 38, 140, 94, 8, mix("#3A3A3C", BLUE, a_fim) if on else "#3A3A3C", a)
        text_mid(c, "FIM" if on else f"cena {k}", fx + 70, y + 85, 30 if on else 20, "black", "#FFFFFF", a)


def pistas(c, t, x, y, cues, a_rev):
    for k, (s, cue) in enumerate(zip(("pegada", "porta aberta", "copo quebrado"), cues)):
        a, d = rise(t, cue)
        pill(c, s, x + k * 200, y + d, INK2, size=24, a=a, anchor="center", bounds=(0, 1920))
        if k < 2:
            text(c, "→", x + k * 200 + 100, y + 9, 30, "black", GRAY, a)
    if a_rev > 0:
        c.save(); c.translate(x + 200, y + 110); sc = 0.8 + 0.2 * ease_back(clamp(a_rev)); c.scale(sc, sc)
        boxed(c, -170, -40, 340, 80, BLUE, a_rev, 0.12)
        text_mid(c, "O CULPADO!", 0, 0, 36, "black", BLUE, a_rev)
        c.restore()


def foto(c, x, y, w, h, a, legenda_a=1.0, cena="sol"):
    if a <= 0:
        return
    rrect(c, x, y, w, h + 70, 10, "#FFFFFF", a, shadow=True)
    rrect(c, x + 20, y + 20, w - 40, h - 40, 6, "#BFDBFE", a)
    if cena == "sol":
        rrect(c, x + 20, y + h * 0.62, w - 40, h * 0.38 - 20, 0, "#86EFAC", a)
        c.drawCircle(x + w * 0.75, y + h * 0.3, 34, paint("#FBBF24", a))
        for k in range(3):
            rrect(c, x + 60 + k * 90, y + h * 0.45, 50, h * 0.2, 4, "#94A3B8", a)
    else:   # fila no posto de saúde
        rrect(c, x + w - 210, y + 60, 170, h - 100, 6, "#E5E7EB", a)
        text_mid(c, "POSTO", x + w - 125, y + 100, 26, "black", RED, a)
        rrect(c, x + w - 150, y + h - 150, 50, 90, 4, "#64748B", a)
        for k in range(8):
            V1.person(c, x + 70 + k * 46, y + h - 120, ["#F97316", BLUE, "#16A36A", PURPLE][k % 4], a, 0.45)
    pe = paint(LIGHT, a * legenda_a, stroke=3); pe.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    c.drawLine(x + 30, y + h + 30, x + w - 30, y + h + 30, pe)
    text(c, "sem legenda", x + w / 2, y + h + 22, 20, "bold", GRAY, a * legenda_a)


def balao_outro(c, s, x, y, w, a, riscado=0.0, size=32):
    """balão do adversário (cinza), riscado quando surge o "mas" """
    if a <= 0:
        return 0
    person(c, x - 60, y + 40, C_OUTRO, a, 0.7)
    h = wa_bubble(c, [(s, INK2, 1 - 0.4 * riscado)], x, y, w, a, size, out=False)
    if riscado > 0:
        line(c, x + 20, y + h / 2, x + 20 + (w - 40) * riscado, y + h / 2 - 6, RED, a, 7)
    text(c, "a voz do OUTRO", x + 10, y - 14, 22, "black", C_OUTRO, a, align="left")
    return h


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "LINGUAGENS ENEM", "ONDE A TESE SE ESCONDE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "1ª FRASE DO TEXTO", 380, 300, 26, "black", GRAY, aa, align="left")
    boxed(c, 380, 320, 1160, 120, INK2, aa, 0.05)
    text_mid(c, "“Há quem diga que...”", 960, 380, 44, "black", INK2, aa)
    check_icon(c, 1600, 380, 30, aa * (1 - ep(t, C["01.b"], 0.3)), GREEN)
    pill(c, "a opinião do autor?", 960, 500, AMBER, INK, size=32, a=aa, anchor="center")
    ab = ep(t, C["01.b"], 0.4)
    line(c, 380, 380, 1540, 372, RED, ab, 8, progress=ab)
    selo(c, 960, 640, ep(t, C["01.b"] + 0.8, 0.4), "A OPINIÃO QUE O AUTOR DESTRÓI", RED, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "saber ONDE PROCURAR a tese", "começo, fim ou lugar nenhum"),
            ("02.b", "fugir da armadilha da 1ª FRASE", "a voz do outro não é a do autor")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")
        text(c, sub, 400, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DUAS LEMBRANÇAS", "EPISÓDIOS 1 E 3", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    pill(c, "EP. 1 · TESE", 560, 260, BLUE, size=30, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "o que o texto AFIRMA", 560, 360, 40, "black", INK, aa)
    text(c, "a frase para levar para casa", 560, 420, 32, "bold", GRAY, aa)
    ab = ep(t, C["03.b"], 0.5)
    pill(c, "EP. 3 · CONTRADIÇÃO", 1360, 260, AMBER, INK, size=30, a=ab, anchor="center", bounds=(0, 1920))
    V3.camisa(c, 1360, 480, 110, mix(AMBER, "#FFFFFF", 0.35), ab, avesso=True)
    text(c, "diz o OPOSTO do texto", 1360, 700, 34, "black", INK, ab)


# ======================================================================
# blocos A, B, C — dedutivo, indutivo, implícito
# ======================================================================

def b_dedutivo(c, t, C, B):
    head_seq(c, t, C, [("04", "O TRAILER QUE", "ENTREGA O FINAL", BLUE), ("05", "ORGANIZAÇÃO", "DEDUTIVA", BLUE)])
    card(c, *CARD_R)
    p5 = ep(t, C["05"], 0.6)
    if p5 < 1:
        a = 1 - p5
        trailer(c, 220, 260, a * ep(t, C["04.t"], 0.4), ep(t, C["04.a"], 0.5))
        text(c, "a conclusão vem PRIMEIRO", 540, 500, 36, "black", BLUE, a * ep(t, C["04.a"], 0.4))
        text(c, "e o resto prova", 540, 550, 32, "bold", INK2, a * ep(t, C["04.a"], 0.4))
    if p5 > 0:
        a = p5
        pill(c, "DEDUTIVO", 520, 250, BLUE, size=40, a=a, anchor="center", bounds=(0, 1920))
        text(c, "tese no começo, apoios depois", 520, 340, 36, "black", INK, a * ep(t, C["05.a"], 0.4))
        rows = [("05.b", "ARTIGO DE OPINIÃO", "alguém assina a própria opinião"),
                ("05.c", "REDAÇÃO DO ENEM", "o texto que você vai escrever"),
                ("06.a", "EDITORIAL", "a opinião do próprio jornal")]
        for k, (cue, g, sub) in enumerate(rows):
            al, d = rise(t, C[cue])
            al *= a
            y = 420 + k * 100 + d
            rrect(c, 230, y - 36, 600, 86, 14, "#F7F7F5", al)
            text(c, g, 260, y, 28, "black", BLUE, al, align="left")
            text(c, sub, 260, y + 34, 24, "bold", INK2, al, align="left")
        pill(c, "procure a tese no COMEÇO", 530, 790, GREEN, size=28, a=a * ep(t, C["06.b"], 0.4), anchor="center", bounds=(0, 1920))
    esq_dedutivo(c, 1360, 300, ep(t, C["04.b"], 0.5), ep(t, C["04.c"], 0.9), ep(t, C["04.d"], 0.5))
    text(c, "retoma no fim", 1360, 620, 24, "black", BLUE, ep(t, C["04.d"], 0.5))


def b_indutivo(c, t, C, B):
    head_seq(c, t, C, [("07", "O FILME", "DE DETETIVE", BLUE), ("08", "ORGANIZAÇÃO", "INDUTIVA", BLUE)])
    card(c, *CARD_R)
    p8 = ep(t, C["08"], 0.6)
    if p8 < 1:
        a = 1 - p8
        pistas(c, t, 320, 330, [C["07.a"], C["07.a"] + 0.6, C["07.a"] + 1.2], ep(t, C["07.b"], 0.5) * a)
        text(c, "pistas primeiro, revelação no FIM", 520, 600, 34, "black", BLUE, a * ep(t, C["07.b"], 0.4))
    if p8 > 0:
        a = p8
        pill(c, "INDUTIVO", 520, 250, BLUE, size=40, a=a, anchor="center", bounds=(0, 1920))
        text(c, "casos primeiro, tese no fim", 520, 340, 36, "black", INK, a * ep(t, C["08.t"], 0.4))
        rows = [("08.a", "CRÔNICA", "texto curto que parte de uma cena do dia a dia"), ("08.c", "CARTA", "")]
        for k, (cue, g, sub) in enumerate(rows):
            al, d = rise(t, C[cue])
            al *= a
            y = 430 + k * 110 + d
            rrect(c, 200, y - 36, 680, 86, 14, "#F7F7F5", al)
            text(c, g, 230, y + (0 if sub else 18), 28, "black", BLUE, al, align="left")
            if sub:
                text(c, sub, 230, y + 34, 22, "bold", INK2, al, align="left")
        pill(c, "quando quer convencer", 700, 430, AMBER, INK, size=20, a=a * ep(t, C["08.b"], 0.4), anchor="center", bounds=(0, 1920))
        pill(c, "procure a tese no FIM", 530, 790, GREEN, size=28, a=a * ep(t, C["08.d"], 0.4), anchor="center", bounds=(0, 1920))
    esq_indutivo(c, 1360, 320, ep(t, C["07.c"], 0.9), ep(t, C["07.d"], 0.5))


def b_implicita(c, t, C, B):
    head_seq(c, t, C, [("09", "A FOTO", "SEM LEGENDA", BLUE), ("10", "TESE", "IMPLÍCITA", BLUE)])
    card(c, *CARD_R)
    p10 = ep(t, C["10"], 0.6)
    if p10 < 1:
        a = 1 - p10
        foto(c, 240, 220, 520, 360, a * ep(t, C["09.a"], 0.4), ep(t, C["09.b"], 0.4))
        acc = ep(t, C["09.c"], 0.4) * a
        if acc > 0:
            for k, r in enumerate((10, 16, 22)):
                c.drawCircle(820 + k * 30, 380 - k * 40, r, paint("#FFFFFF", acc)); c.drawCircle(820 + k * 30, 380 - k * 40, r, paint(LIGHT, acc, stroke=2))
            text(c, "você monta o sentido", 820, 260, 30, "black", BLUE, acc, align="left")
        ad = ep(t, C["09.d"], 0.4) * a
        caixa(c, 240, 700, 880, 90, BLUE, ad, "TESE EXPLÍCITA = escrita numa frase", 28)
    if p10 > 0:
        a = p10
        pill(c, "TESE IMPLÍCITA", 560, 250, BLUE, size=40, a=a, anchor="center", bounds=(0, 1920))
        text(c, "nenhuma frase sozinha a diz", 560, 340, 36, "black", INK, a)
        text(c, "o LEITOR reconstrói", 560, 395, 34, "black", BLUE, a * ep(t, C["10.a"], 0.4))
        for k, g in enumerate(("crônica irônica", "poema", "anúncio", "tirinha")):
            pill(c, g, 260 + k * 160 + (40 if k else 0), 480, INK2, size=22, a=a * ep(t, C["10.b"] + 0.5 * k, 0.3), bounds=(0, 1920))
        acc = ep(t, C["10.c"], 0.4) * a
        rrect(c, 230, 540, 680, 100, 14, "#F7F7F5", acc)
        text(c, "CHARGE", 260, 578, 28, "black", BLUE, acc, align="left")
        text(c, "desenho de humor do jornal, que critica algo", 260, 615, 22, "bold", INK2, acc, align="left")
        pill(c, "episódio 6: como montar essa tese", 560, 760, PURPLE, size=26, a=a * ep(t, C["10.d"], 0.4), anchor="center", bounds=(0, 1920))
        esq_implicito(c, t, 1360, 280, ep(t, C["10.t"], 0.9), ep(t, C["10.a"], 0.8))


def b_esquemas(c, t, C, B):
    frame(c, t, B["start"], "OS TRÊS", "LADO A LADO", PURPLE)
    aa, ab, acc = ep(t, C["11.a"], 0.6), ep(t, C["11.b"], 0.6), ep(t, C["11.c"], 0.6)
    for k, (s, sub, a) in enumerate((("DEDUTIVO", "tese no COMEÇO", aa), ("INDUTIVO", "tese no FIM", ab),
                                    ("IMPLÍCITO", "tese em LUGAR NENHUM", acc))):
        x = 420 + k * 540
        text(c, s, x, 250, 34, "black", BLUE, a)
        text(c, sub, x, 760, 30, "black", INK2, a)
    esq_dedutivo(c, 420, 300, aa, aa, aa, 400)
    esq_indutivo(c, 960, 330, ab, ab, 400)
    esq_implicito(c, t, 1500, 320, acc, ep(t, C["11.c"] + 0.8, 0.8), 400)


# ======================================================================
# bloco D — a armadilha da primeira frase
# ======================================================================

def b_armadilha(c, t, C, B):
    head_seq(c, t, C, [("12", "A ARMADILHA DA", "PRIMEIRA FRASE", AMBER), ("13", "O AUTOR VAI", "REFUTAR", BLUE),
                       ("14", "A REGRA", "LEIA ATÉ O PRIMEIRO MAS", PURPLE)])
    card(c, *CARD_R)
    p13 = ep(t, C["13"], 0.6)
    if p13 < 1:
        a = 1 - p13
        for k, s in enumerate(("Há quem diga que…", "Muita gente acredita que…", "Diz-se que…")):
            pill(c, s, 300, 260 + k * 80, C_OUTRO, size=30, a=a * ep(t, C["12.a"] + 0.6 * k, 0.4), bounds=(0, 1920))
        ab = ep(t, C["12.b"], 0.4) * a
        text(c, "quem está falando?", 1300, 290, 36, "black", INK, ab)
        acc = ep(t, C["12.c"], 0.4) * a
        person(c, 1300, 400, C_OUTRO, acc, 1.1)
        text(c, "NÃO é o autor: é o OUTRO", 1300, 620, 34, "black", C_OUTRO, acc)
        ad = ep(t, C["12.d"], 0.4) * a
        text(c, "o adversário fala primeiro...", 960, 740, 34, "black", INK2, ad)
        text(c, "só para ser derrubado", 960, 790, 34, "black", RED, ep(t, C["12.d"] + 1.2, 0.4) * a)
    if p13 > 0:
        a = p13
        p14 = ep(t, C["14"], 0.6)
        at = ep(t, C["13.t"], 0.4) * a * (1 - p14)
        caixa(c, 300, 200, 1320, 70, BLUE, at, "REFUTAR = derrubar uma ideia, mostrando que está errada", 28)
        ab = ep(t, C["13.b"], 0.5)
        y0 = lerp(320, 220, p14)
        balao_outro(c, "Há quem diga que o celular na escola só atrapalha.", 360, y0, 760, a * ep(t, C["13.a"], 0.4), ab, 32)
        wa_bubble(c, [("Não é bem assim:", GREEN, 1), ("a escola deve ensinar a usar.", BLUE, 1)], 860, y0 + 170, 760, a * ab, 34)
        person(c, 1700, y0 + 210, BLUE, a * ab, 0.7)
        pill(c, "TESE: depois da virada", 1240, y0 + 320, BLUE, size=26, a=a * ep(t, C["13.c"], 0.4) * (1 - p14), anchor="center", bounds=(0, 1920))
        if p14 > 0:
            regra(c, "Leia até o primeiro MAS.", 640, p14 * ep(t, C["14.a"], 0.4), 42)
            for k, w in enumerate(("porém", "engano", "não é bem assim")):
                pill(c, w, 640 + k * 230, 740, GREEN, size=28, a=p14 * ep(t, C["14.b"] + 0.4 * k, 0.3), anchor="center", bounds=(0, 1920))
            selo(c, 1560, 760, p14 * ep(t, C["14.d"], 0.4), "1ª FRASE = CONTRADIÇÃO", AMBER, -5, 24)


def b_livre(c, t, C, B):
    frame(c, t, B["start"], "IMPLÍCITA", "NÃO QUER DIZER LIVRE", PURPLE)
    foto(c, 220, 200, 640, 420, ep(t, C["15.b"], 0.5), 1, cena="fila")
    acc = ep(t, C["15.c"], 0.4)
    check_icon(c, 990, 330, 30, acc, GREEN)
    text(c, "o atendimento está demorado", 1040, 342, 36, "black", GREEN, acc, align="left")
    ad = ep(t, C["15.d"], 0.4)
    check_icon(c, 990, 470, 30, ad, RED, "x")
    text(c, "o prefeito é corrupto", 1040, 482, 36, "black", RED, ad, align="left")
    text(c, "a foto NÃO mostra isso", 1040, 530, 26, "bold", GRAY, ep(t, C["15.d"] + 1.2, 0.4), align="left")
    regra(c, "Implícita não quer dizer livre: o texto precisa autorizar.", 760, ep(t, C["15.e"], 0.5), 32)


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Dedutivo: tese no começo. Indutivo: tese no fim. Implícito: tese em lugar nenhum.",
          "“Há quem diga” é a voz do outro, não a do autor.", "Leia até o primeiro “mas”."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 230, y - 16, a, 36, bg=PURPLE)
        if k == 0:
            text(c, "Dedutivo: tese no começo.", 300, y - 30, 40, "black", INK, a, align="left")
            text(c, "Indutivo: tese no fim.  Implícito: em lugar nenhum.", 300, y + 26, 40, "black", INK, a, align="left")
        else:
            text(c, s, 300, y, 48, "black", INK, a, align="left")


ERROS = [("17", "Tomar a PRIMEIRA FRASE como tese", "muito texto começa mesmo pela tese", "voz do outro? leia até o primeiro mas"),
         ("18", "Achar que texto que só conta CASOS não tem tese", "nenhuma frase do começo dá opinião", "filme de detetive: a revelação vem no FIM"),
         ("19", "INVENTAR uma conclusão na tese implícita", "se ninguém escreveu, parece que vale tudo", "só vale o que a foto mostra")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    para(c, err, 360, 345, 44, "black", RED, aa, 1300)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 480, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 560, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 678, 34, ac, GREEN)
    text(c, fix, 360, 694, 42, "black", GREEN, ac, align="left")


# ======================================================================
# questões 2 e 3
# ======================================================================

Q2_1 = "Há quem veja a feira livre como resquício de um tempo sem supermercado."
Q2 = Leitura(
    [("20", "f1", "c1", Q2_1),
     ("21", "f2", "c2", "Engano."),
     ("21", "f3", "c3", "A feira é onde o pequeno produtor vende sem intermediário, onde o preço se negocia olhando no olho e onde a cidade ainda se encontra na rua num domingo de manhã."),
     ("22", "f4", "c4", "Quando uma prefeitura transfere a feira para um galpão afastado, alegando problemas de trânsito, não está organizando o espaço: está empurrando para longe um dos últimos mercados em que quem planta conversa com quem come.")],
    [(0, "Há quem veja", "fill", AMBER, "20.c1"),
     (0, Q2_1, "strike", RED, "21.c2"),
     (1, "Engano.", "box", GREEN, None),
     (2, "vende sem intermediário,", "under", BLUE, "21.c3"),
     (2, "o preço se negocia olhando no olho", "under", BLUE, "21.c3"),
     (2, "a cidade ainda se encontra na rua", "under", BLUE, "21.c3"),
     (3, "alegando problemas de trânsito,", "under", AMBER, "22.c4"),
     (3, "está empurrando para longe um dos últimos mercados", "fill", BLUE, "22.d")])

Q3 = Leitura(
    [("25", "f1", "f2", "Na rua de cima, o portão quebrado ficou um ano sem conserto; logo vieram as pichações, depois o lixo acumulado na calçada."),
     ("25", "f2", "c2", "Na praça, o banco arrancado nunca foi reposto, e as famílias deixaram de ir."),
     ("26", "f3", "c3", "No posto de saúde, a lâmpada queimada da entrada transformou o fim de tarde em hora de medo."),
     ("26", "f4", "f5", "Nenhum desses problemas, isolado, parecia urgente."),
     ("26", "f5", "c5", "Juntos, ensinam uma lição que os orçamentos públicos costumam esquecer: a manutenção miúda e constante custa menos do que a reforma tardia, e é ela que mantém um espaço vivo.")],
    [(0, "o portão quebrado ficou um ano sem conserto;", "under", INK2, "25.c2"),
     (1, "o banco arrancado nunca foi reposto,", "under", INK2, "25.c2"),
     (2, "a lâmpada queimada da entrada", "under", INK2, "26.c3"),
     (4, "Juntos, ensinam uma lição", "box", GREEN, None),
     (4, "a manutenção miúda e constante custa menos do que a reforma tardia, e é ela que mantém um espaço vivo.", "fill", BLUE, "27.a")])

ALTS2 = [("A", "a feira livre; a feira é um resquício de um tempo em que não havia supermercados.", "23.a", "24.a", "CONTRADIÇÃO: a 1ª frase, que o autor derruba"),
         ("B", "o comércio de alimentos; os supermercados oferecem preços mais baixos que as feiras.", "23.b", "24.b", "NÃO ESTÁ NO TEXTO"),
         ("C", "o trânsito urbano; as prefeituras devem organizar o uso das ruas.", "23.c", "24.c", "CONTRADIÇÃO: a desculpa da prefeitura"),
         ("D", "a feira livre; a feira tem valor econômico e social que justifica mantê-la no espaço da rua.", "23.d", None, ""),
         ("E", "a agricultura familiar; o pequeno produtor precisa de mais crédito rural.", "23.e", "24.e", "EXTRAPOLAÇÃO")]
ALTS3 = [("A", "defende, desde a primeira frase, que pichações devem ser punidas com rigor.", "27.al", "29.a", "EXTRAPOLAÇÃO"),
         ("B", "relata casos particulares e só no final explicita a tese de que a manutenção constante é preferível à reforma tardia.", "27.bl", None, ""),
         ("C", "apresenta a tese no primeiro período e a retoma, com outras palavras, no último.", "28.cl", "29.c", "ORGANIZAÇÃO TROCADA: isso é o dedutivo"),
         ("D", "tem como ideia central a insegurança na entrada do posto de saúde.", "28.dl", "29.d", "REDUÇÃO"),
         ("E", "não apresenta tese, limitando-se a descrever problemas de um bairro.", "28.el", "29.e", "SEM TESE? (erro clássico 2)")]


def alternativas(c, t, C, alts, ok_cue, x0, y0, maxw, a=1.0, size=23):
    aok = ep(t, C[ok_cue], 0.5)
    y = y0
    for L, s, show, cx, why in alts:
        al, d = rise(t, C[show])
        al *= a
        lines = wrap(s, "black", size, maxw)
        hh = len(lines) * (size + 7) + 12 + (26 if cx else 0)
        ok = cx is None
        if ok and aok > 0:
            rrect(c, x0 - 70, y - 30 + d, maxw + 100, hh + 10, 12, GREEN, 0.14 * aok * a)
        badge_num(c, L, x0 - 40, y - 8 + d, al, 20, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cx], 0.4) * a if cx else 0
        for j, ln in enumerate(lines):
            text(c, ln, x0, y + d + j * (size + 7), size, "black", INK, al * (1 - 0.5 * ax), align="left")
            if ax > 0:
                strike(c, x0 - 4, y + d + j * (size + 7) - 8, x0 + 4 + text_w(ln, "black", size), y + d + j * (size + 7) - 8, ax, RED, ax)
        if ax > 0:
            pill(c, why, x0, y + d + len(lines) * (size + 7) + 2, AMBER, INK, size=17, a=ax, bounds=(0, 1920))
        y += hh + 18
    return aok


def b_questao2(c, t, C, B):
    head_seq(c, t, C, [("20", "EU FAÇO", "QUESTÃO 2 · A FEIRA LIVRE", BLUE), ("23", "EU FAÇO", "AS ALTERNATIVAS", AMBER)])
    card(c, *CARD_R)
    pill(c, "COMANDO: O assunto e a tese do texto são, respectivamente:", 200, 200, BLUE, size=24, a=ep(t, C["20.a"], 0.4), bounds=(0, 1920))
    ph = ep(t, C["23"], 0.7)
    if ph < 1:
        a = 1 - ph
        Q2.draw(c, t, C, 200, 300, 1060, 32, 50, a * ep(t, C["20.f1"] - 0.3, 0.4))
        notas(c, t, C, [("20.a", "RESPECTIVAMENTE", "primeiro o assunto, depois a tese", BLUE),
                        ("20.c1", "HÁ QUEM VEJA", "a voz do OUTRO · resquício = sobra", AMBER),
                        ("21.c2", "ENGANO = A VIRADA", "o autor derruba a 1ª frase", GREEN),
                        ("21.c3", "TRÊS MOTIVOS", "a feira TEM VALOR", BLUE),
                        ("22.c4", "ALEGANDO", "a desculpa da prefeitura", AMBER)], 1310, 270, 104, 430, a)
        ad = ep(t, C["22.d"], 0.5) * a
        if ad > 0:
            wa_bubble(c, [("Assunto:", INK2, 1), ("a feira livre.", INK, 1), ("Tese:", INK2, 1),
                          ("a feira tem valor, e deve ficar na rua.", BLUE, 1)], 200, 690, 1060, ad, 30)
    if ph > 0:
        Q2.draw(c, t, C, 190, 300, 600, 20, 30, ph * 0.9)
        wa_bubble(c, [("Assunto: a feira livre. Tese: a feira tem valor, e deve ficar na rua.", BLUE, 1)], 190, 640, 600, ph, 22)
        aok = alternativas(c, t, C, ALTS2, "24.ok", 920, 290, 760, ph, 22)
        result_box(c, "Letra D", 490, 790, 50, aok, GREEN)


def b_questao3(c, t, C, B):
    head_seq(c, t, C, [("25", "VOCÊ FAZ", "QUESTÃO 3 · OS CONSERTOS", GREEN), ("27", "VOCÊ FAZ", "DEDUTIVO OU INDUTIVO?", PURPLE)])
    card(c, *CARD_R)
    pill(c, "COMANDO: Quanto à construção do sentido global, o texto", 200, 200, BLUE, size=24, a=ep(t, C["25.a"], 0.4), bounds=(0, 1920))
    ph = ep(t, C["27.b"], 0.7)
    if ph < 1:
        a = 1 - ph
        Q3.draw(c, t, C, 200, 300, 1060, 31, 48, a * ep(t, C["25.f1"] - 0.3, 0.4))
        notas(c, t, C, [("25.a", "SENTIDO GLOBAL", "como o texto monta a sua ideia", BLUE),
                        ("25.c2", "CASO 1 · CASO 2", "um caso, outro caso", INK2),
                        ("26.c3", "CASO 3", "pista, pista, pista", INK2),
                        ("26.c5", "MANUTENÇÃO MIÚDA", "consertos pequenos, feitos sempre", BLUE)], 1310, 270, 104, 430, a)
        pause_timer(c, t, C["27.a"] - 1.7, 1520, 740, a)
        aa = ep(t, C["27.a"], 0.4) * a
        pill(c, "INDUTIVO: casos primeiro → tese no FIM", 730, 700, BLUE, size=34, a=aa, anchor="center", bounds=(0, 1920))
    if ph > 0:
        Q3.draw(c, t, C, 190, 300, 600, 20, 30, ph * 0.9)
        pill(c, "INDUTIVO: casos → tese no fim", 490, 680, BLUE, size=24, a=ph, anchor="center", bounds=(0, 1920))
        aok = alternativas(c, t, C, ALTS3, "29.ok", 920, 290, 760, ph, 22)
        pause_timer(c, t, C["28.end"] - 1.7, 490, 770, ph)
        result_box(c, "Letra B", 490, 790, 50, aok, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def placa(c, x, y, s, col, a):
    if a <= 0:
        return
    rrect(c, x - 8, y + 60, 16, 200, 4, "#64748B", a)
    w = text_w(s, "black", 30) + 60
    c.save(); c.translate(x, y + 30); c.rotate(-3)
    rrect(c, -w / 2, -45, w, 90, 14, col, a, shadow=True)
    text_mid(c, s, 0, 0, 30, "black", "#FFFFFF", a)
    c.restore()


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AS PISTAS QUE ENTREGAM A TESE", PURPLE)
    line(c, 200, 620, 1720, 620, LINE, ep(t, C["31.t"], 0.5), 20)
    for k, (cue, s, col) in enumerate((("31.a", "TÍTULO", BLUE), ("31.b", "COMEÇO DO PARÁGRAFO", INK2), ("31.c", "MAS · PORTANTO", GREEN))):
        placa(c, 440 + k * 520, 300, s, col, ep(t, C[cue], 0.5))
    pill(c, "ep. 5 · as pistas que entregam a tese", W / 2, 760, PURPLE, size=34, a=ep(t, C["31.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Você já marcou a primeira frase como tese?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, dedutivo=b_dedutivo, indutivo=b_indutivo,
              implicita=b_implicita, esquemas=b_esquemas, armadilha=b_armadilha, livre=b_livre, recap=b_recap,
              erros=b_erros, questao2=b_questao2, questao3=b_questao3, ponte=b_ponte, cta=b_cta)
