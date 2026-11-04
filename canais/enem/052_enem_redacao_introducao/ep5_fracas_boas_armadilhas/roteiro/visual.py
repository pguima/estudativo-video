"""Visual — Redação ENEM, Introdução, Episódio 5: Introduções fracas × boas e as armadilhas (tema claro).
Usa o desenho da série (introducao_visual.py: etiqueta de 4 peças, mini_etiqueta, rascunho, alternativas, recap, CTA).
Novo: as três VERSÕES numa folha, frase a frase, com a mini-etiqueta à direita marcando o que tem (✓) e o que falta (✗);
teste da retirada animado na versão 2; quadro "o que mudou"; cartão de ARMADILHA com selo PEGADINHA (7, em duas cenas:
abertura e fechamento); folha de redação com a faixa de 1/5 a 1/4 (sugestão, não regra).
Cores: azul = definição/tema · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep5_fracas_boas_armadilhas.mp4"
KEYS = ["mapa", "rua", "tese", "lista"]


def sents_layout(sents, x, y, size, maxw, lh, gap=0):
    """posição (y inicial, nº de linhas) de cada frase, uma abaixo da outra"""
    out, yy = [], y
    for s in sents:
        n = len(wrap(s, "bold", size, maxw))
        out.append((yy, n))
        yy += n * lh + gap
    return out, yy


def versao_folha(c, t, C, sents, cues, hl=None, x=150, y=170, w=1080, h=660, size=34, lh=48, gone=None, title=""):
    """folha com a versão, uma frase por vez (cues = quando cada frase aparece).
    hl = [(alpha, cor)] destaque de cada frase · gone = [(alpha_sai, deslocamento)] para o teste da retirada"""
    paper(c, x, y, w, h, 1.0, lh=lh, top=y + 120 - 2 * lh + 6)
    text(c, title, x + 110, y + 48, 22, "black", GRAY, 1.0, align="left", tracking=2)
    lay, _ = sents_layout(sents, x + 110, y + 120, size, w - 160, lh)
    for k, (s, (yy, n)) in enumerate(zip(sents, lay)):
        a = ep(t, cues[k], 0.5)
        if a <= 0:
            continue
        dx, ga = 0.0, 1.0
        if gone and gone[k]:
            ga, dx = gone[k]
        if hl and hl[k][0] > 0:
            rrect(c, x + 96 + dx, yy - size - 6, w - 132, n * lh + 10, 10, hl[k][1], 0.16 * hl[k][0] * a * ga)
            rrect(c, x + 96 + dx, yy - size - 6, 8, n * lh + 10, 4, hl[k][1], hl[k][0] * a * ga)
        para(c, s, x + 110 + dx, yy, size, "bold", INK, a * ga, w - 160, lh)
    text(c, DIDATICO, x + 110, y + h - 22, 18, "medium", AMBER, ep(t, cues[0], 0.5), align="left")
    return lay


def nota(c, x, y, s, a, ok, w=480, size=26):
    """linha de análise com ✓/✗"""
    if a <= 0:
        return 0
    check_icon(c, x + 18, y - 8, 18, a, GREEN if ok else RED, "check" if ok else "x")
    return para(c, s, x + 50, y, size, "black", INK, a, w - 50, size + 6)


def etiqueta_lado(c, t, C, oks_cues, oks, x=1500, y=300, s=1.25):
    """mini-etiqueta à direita: cada faixa ganha a marca no seu cue"""
    vals = [oks[k] if (oks_cues[k] is not None and t >= C[oks_cues[k]]) else None for k in range(4)]
    mini_etiqueta(c, x, y, 1.0, vals, s)


# ======================================================================
# abertura
# ======================================================================

def mini_folha(c, cx, cy, a, rot, lab, col, lines=5, s=1.0):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    rrect(c, -150 * s, -190 * s, 300 * s, 380 * s, 10, PAPER, a, shadow=True)
    line(c, -110 * s, -180 * s, -110 * s, 180 * s, "#F3A6A6", a, 2)
    for k in range(lines):
        yy = -120 * s + k * 48 * s
        line(c, -96 * s, yy, 120 * s - (k % 3) * 40 * s, yy, mix(PEN, "#FFFFFF", 0.45), a, 6)
    c.restore()
    pill(c, lab, cx, cy + 230 * s, col, size=26, a=a, anchor="center", bounds=(0, 1920))


def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · INTRODUÇÃO", "FRACAS × BOAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "MESMO TEMA DO ENEM", W / 2, 230, 28, "black", GRAY, aa, tracking=3)
    cols = [("01.b", "GENÉRICA", INK2, -4), ("01.c", "CITA ARISTÓTELES", INK2, 2), ("01.d", "SEM FILÓSOFO", INK2, -2)]
    for k, (cue, lab, col, rot) in enumerate(cols):
        a, d = rise(t, C[cue])
        mini_folha(c, 470 + k * 490, 470 + d, a * aa, rot, lab, col, s=0.82)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        for k in range(3):
            text_mid(c, "?", 470 + k * 490, 450, 120, "black", BLUE, ae * 0.9)
    selo(c, W / 2, 790, ep(t, C["01.f"], 0.4), "QUASE TODO MUNDO ERRA", RED, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "NO FIM DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "dizer POR QUE uma introdução é fraca", RED, "x"), ("02.b", "e como CONSERTÁ-LA", GREEN, "check")]
    for k, (cue, s, col, kind) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 380 + k * 190 + d
        check_icon(c, 360, y - 16, 40, a, col, kind)
        text(c, s, 430, y, 56, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "A ETIQUETA COMPLETA", PURPLE)
    a0 = ep(t, C["03.a"], 0.5)
    sh = [ep(t, C["03." + k], 0.4) for k in "bcef"]
    cur = [1.0 if (t >= C["03." + k] and (j == 3 or t < C["03." + "bcef"[j + 1]])) else 0.0 for j, k in enumerate("bcef")]
    etiqueta_intro(c, 190, 175, 980, a0, show=sh, lit=cur, perguntas=0.0, movs=1.0, rowh=118)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        x0, y0 = 1250, 260
        rrect(c, x0, y0, 470, 470, 22, mix("#FFFFFF", AMBER, 0.08), ad, shadow=True)
        text(c, "TESTE DA RETIRADA", x0 + 235, y0 + 60, 28, "black", AMBER, ad, tracking=2)
        pull = ep(t, C["03.d"] + 0.8, 1.0)
        rrect(c, x0 + 60 + 160 * pull, y0 + 120, 300, 70, 12, "#FFFFFF", ad * (1 - 0.6 * pull), shadow=True)
        text_mid(c, "referência", x0 + 210 + 160 * pull, y0 + 155, 28, "black", BLUE, ad * (1 - 0.6 * pull))
        arrow(c, x0 + 80, y0 + 230, x0 + 390, y0 + 230, AMBER, ad * pull, 5, 16, progress=pull)
        para(c, "tirou e nada mudou?", x0 + 40, y0 + 320, 32, "black", INK, ad, 400, 40)
        para(c, "não trabalhava", x0 + 40, y0 + 380, 32, "black", RED, ep(t, C["03.d"] + 1.6, 0.4), 400, 40)


# ======================================================================
# três etiquetas para o mesmo endereço
# ======================================================================

def cartao_postal(c, x, y, w, h, a):
    rrect(c, x, y, w, h, 8, "#FFFFFF", a, shadow=True)
    rrect(c, x + 8, y + 8, w - 16, h - 16, 6, "#BFE3FF", a)
    c.drawCircle(x + w * 0.72, y + h * 0.32, h * 0.12, paint(AMBER, a))
    p = skia.Path(); p.moveTo(x + 8, y + h - 8); p.lineTo(x + w * 0.35, y + h * 0.42); p.lineTo(x + w * 0.55, y + h * 0.68)
    p.lineTo(x + w * 0.7, y + h * 0.52); p.lineTo(x + w - 8, y + h - 8); p.close()
    c.drawPath(p, paint(GREEN, a * 0.85))


def b_etiquetas(c, t, C, B):
    frame(c, t, B["start"], "TRÊS ETIQUETAS", "PARA O MESMO ENDEREÇO", BLUE)
    xs = [220, 760, 1300]
    a1, d1 = rise(t, C["04.a"])
    if a1 > 0:
        x, y = xs[0], 250 + d1
        rrect(c, x, y, 400, 300, 16, "#FFFFFF", a1, shadow=True)
        text(c, "PARA:", x + 30, y + 60, 20, "black", GRAY, a1, align="left", tracking=2)
        hand(c, "alguém,", x + 40, y + 140, 44, PEN, a1)
        hand(c, "em algum lugar", x + 40, y + 220, 44, PEN, a1)
    a2, d2 = rise(t, C["04.b"])
    if a2 > 0:
        x, y = xs[1], 250 + d2
        rrect(c, x, y, 400, 300, 16, "#FFFFFF", a2, shadow=True)
        text(c, "PARA:", x + 30, y + 60, 20, "black", GRAY, a2, align="left", tracking=2)
        c.save(); c.translate(x + 200, y + 175); c.rotate(-5)
        cartao_postal(c, -150, -85, 300, 170, a2)
        c.restore()
        text(c, "serve para qualquer cidade", x + 200, y + 340, 24, "bold", AMBER, a2)
    a3, d3 = rise(t, C["04.c"])
    if a3 > 0:
        mini_etiqueta(c, xs[2] + 200, 400 + d3, a3, [None] * 4, 1.3)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        truck(c, lerp(-260, xs[2] + 110, ease_out(ad)), 650, 1.0, BLUE, 1.0)
        for k in range(2):
            xmark(c, xs[k] + 200, 640 + 60, 40, ep(t, C["04.d"] + 0.8, 0.4))
        check_icon(c, xs[2] + 330, 720, 34, ep(t, C["04.d"] + 1.2, 0.4), GREEN)
    pill(c, "com as introduções, é igual", W / 2, 800, PURPLE, size=28, a=ep(t, C["04.e"], 0.4), anchor="center",
         bounds=(0, 1920))


def b_tema(c, t, C, B):
    frame(c, t, B["start"], "O TEMA DAS 3 VERSÕES", "ENEM 2024", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    pill(c, "ENEM 2024", W / 2, 230, BLUE, size=26, a=aa, anchor="center", bounds=(0, 1920))
    text(c, "“" + TEMA24 + "”", W / 2, 320, 44, "black", BLUE, aa)
    pill(c, "as 3 versões foram elaboradas para fins didáticos", W / 2, 400, AMBER, size=24, a=ep(t, C["05.b"], 0.4),
         anchor="center", bounds=(0, 1920))
    for k in range(3):
        a = ep(t, C["05.c"] + 0.4 * k, 0.4)
        text(c, f"VERSÃO {k + 1}", 480 + k * 480, 500, 24, "black", INK2, a, tracking=2)
        mini_etiqueta(c, 480 + k * 480, 650, a, [None] * 4, 1.0)
        text_mid(c, "?", 480 + k * 480 + 175, 650, 60, "black", GRAY, a)


# ======================================================================
# versão 1
# ======================================================================

V1S = ["Desde os primórdios da humanidade, a cultura é fundamental para todos os povos.",
       "Nesse sentido, a herança africana também é importante e deve ser valorizada.",
       "Portanto, é necessário discutir esse tema."]


def b_v1(c, t, C, B):
    sid = which(t, C, ["06", "07"])
    head_seq(c, t, C, [("06", "VERSÃO 1", "A GENÉRICA", INK2), ("07", "VERSÃO 1 · ANÁLISE", "A GENÉRICA", RED)])
    an = sid == "07"
    hl = [(ep(t, C["07.m"], 0.4), RED), (ep(t, C["07.t2"], 0.4), RED), (ep(t, C["07.f"], 0.4), RED)] if an else None
    versao_folha(c, t, C, V1S, [C["06.a"], C["06.b"], C["06.c"]], hl=hl, title="VERSÃO 1 · GENÉRICA")
    a_et = ep(t, C["06.t"], 0.5)
    mini_etiqueta(c, 1520, 300, a_et, [None] * 4, 1.25) if not an else \
        etiqueta_lado(c, t, C, ["07.m", "07.m", "07.t2", "07.l"], [0, 0, 0, 0], 1520, 300)
    if not an:
        return
    selo(c, 1520, 140 + 330, ep(t, C["07.a"], 0.4) * (1 - ep(t, C["07.m"], 0.3)), "SOA FORMAL...", AMBER, -4, 30)
    y = 500
    for cue, s in (("07.m", "serve para QUALQUER tema"), ("07.t2", "tese que ninguém contestaria"),
                   ("07.l", "nada antecipado"), ("07.f", "só anuncia que haverá discussão")):
        y += nota(c, 1290, y, s, ep(t, C[cue], 0.4), False, 480, 26) + 18
    ar = ep(t, C["07.r"], 0.4)
    if ar > 0:
        rrect(c, 1270, 770, 500, 60, 14, mix("#FFFFFF", RED, 0.10), ar)
        text_mid(c, "C2 previsível · C3 pouco visível", 1520, 800, 24, "black", RED, ar)


# ======================================================================
# versão 2 (teste da retirada)
# ======================================================================

V2S = ["Segundo Aristóteles, o homem é um animal político.",
       "Dessa forma, a valorização da herança africana no Brasil é um desafio que precisa ser enfrentado por toda a sociedade."]


def b_v2(c, t, C, B):
    sid = which(t, C, ["08", "09"])
    head_seq(c, t, C, [("08", "VERSÃO 2", "O REPERTÓRIO DE BOLSO", INK2), ("09", "VERSÃO 2 · ANÁLISE", "O REPERTÓRIO DE BOLSO", RED)])
    an = sid == "09"
    gone = None
    hl = None
    if an:
        px = ep(t, C["09.x"] + 0.6, 1.0)
        back = ep(t, C["09.c"], 0.5)
        gone = [(1 - 0.85 * px * (1 - back), 260 * px * (1 - back)), None]
        hl = [(ep(t, C["09.b"], 0.4) * (1 - px * (1 - back)), AMBER), (ep(t, C["09.c"], 0.4), RED)]
    lay = versao_folha(c, t, C, V2S, [C["08.a"], C["08.b"]], hl=hl, gone=gone, title="VERSÃO 2 · REPERTÓRIO DE BOLSO")
    if not an:
        mini_etiqueta(c, 1520, 300, ep(t, C["08.t"], 0.5), [None] * 4, 1.25)
        return
    etiqueta_lado(c, t, C, ["09.b", "09.b", "09.c", "09.c"], [0, 0, 0, 0], 1520, 300)
    ab = ep(t, C["09.b"], 0.4) * (1 - ep(t, C["09.x"], 0.3))
    if ab > 0:
        c.save(); c.translate(1520, 560); c.rotate(-5)
        cartao_postal(c, -130, -75, 260, 150, ab)
        c.restore()
        text(c, "REPERTÓRIO DE BOLSO", 1520, 700, 24, "black", AMBER, ab, tracking=1)
        text(c, "serve para qualquer tema", 1520, 740, 22, "bold", INK2, ab)
    ax = ep(t, C["09.x"], 0.4) * (1 - ep(t, C["09.c"], 0.3))
    if ax > 0:
        text(c, "TESTE DA RETIRADA", 1520, 520, 28, "black", AMBER, ax, tracking=2)
        text(c, "apague Aristóteles...", 1520, 580, 28, "bold", INK2, ax)
        selo(c, 1520, 680, ep(t, C["09.y"], 0.4) * ax, "NADA MUDA", RED, -5, 40)
    ac = ep(t, C["09.c"], 0.4)
    if ac > 0:
        y = 500
        y += nota(c, 1290, y, "referência que sai sem perda", ac, False, 480) + 18
        y += nota(c, 1290, y, "a tese só REPETE o tema", ac, False, 480) + 18
        ad = ep(t, C["09.d"], 0.4)
        if ad > 0:
            rrect(c, 1270, 700, 500, 120, 14, mix("#FFFFFF", GREEN, 0.10), ad)
            text(c, "o problema não é o autor:", 1520, 748, 24, "bold", INK2, ad)
            text(c, "é o ENCAIXE", 1520, 796, 34, "black", GREEN, ad)


# ======================================================================
# versão 3 (boa)
# ======================================================================

def b_v3(c, t, C, B):
    sid = which(t, C, ["10", "11"])
    head_seq(c, t, C, [("10", "VERSÃO 3", "A BOA", INK2), ("11", "VERSÃO 3 · ANÁLISE", "A BOA", GREEN)])
    an = sid == "11"
    hl = [(ep(t, C["11.m"], 0.4), MOV["mapa"]), (ep(t, C["11.r"], 0.4), MOV["rua"]),
          (ep(t, C["11.e"], 0.4), MOV["tese"])] if an else None
    versao_folha(c, t, C, V3_BOA, [C["10.a"], C["10.b"], C["10.c"]], hl=hl, size=29, lh=41, title="VERSÃO 3 · BOA")
    if not an:
        mini_etiqueta(c, 1520, 300, ep(t, C["10.t"], 0.5), [None] * 4, 1.25)
        return
    etiqueta_lado(c, t, C, ["11.m", "11.r", "11.e", "11.l"], [1, 1, 1, 1], 1520, 300)
    selo(c, 1520, 470, ep(t, C["11.a"], 0.4) * (1 - ep(t, C["11.m"], 0.3)), "SEM FILÓSOFO NENHUM", GREEN, -4, 28)
    am = ep(t, C["11.m"], 0.4) * (1 - ep(t, C["11.r"], 0.3))
    if am > 0:
        pill(c, "LEGÍTIMA", 1290, 500, BLUE, size=24, a=am, bounds=(0, 1920))
        para(c, "fonte real, que dá para conferir", 1290, 570, 26, "bold", INK2, am, 480, 32)
        pill(c, "PERTINENTE", 1290, 650, BLUE, size=24, a=ep(t, C["11.m"] + 2.0, 0.4) * am,
             bounds=(0, 1920))
        para(c, "ligada ao tema", 1290, 720, 26, "bold", INK2, ep(t, C["11.m"] + 2.0, 0.4) * am, 480, 32)
    ar = ep(t, C["11.r"], 0.4) * (1 - ep(t, C["11.e"], 0.3))
    if ar > 0:
        text(c, "PONTE", 1520, 520, 26, "black", MOV["rua"], ar, tracking=2)
        rrect(c, 1290, 560, 220, 90, 12, mix("#FFFFFF", BLUE, 0.12), ar)
        text_mid(c, "a lei prevê", 1400, 605, 24, "black", BLUE, ar)
        text_mid(c, "×", 1520, 605, 44, "black", INK2, ar)
        rrect(c, 1540, 560, 220, 90, 12, mix("#FFFFFF", RED, 0.10), ar)
        text_mid(c, "o que acontece", 1650, 605, 24, "black", RED, ar)
    ae = ep(t, C["11.e"], 0.4) * (1 - ep(t, C["11.l"], 0.3))
    if ae > 0:
        text(c, "O RECORTE INTEIRO", 1520, 510, 22, "black", MOV["tese"], ae, tracking=2)
        for k, s in enumerate(["desafios", "valorização", "herança africana", "Brasil"]):
            a = ep(t, C["11.e"] + 0.8 + 0.5 * k, 0.3) * ae
            y = 570 + k * 60
            check_icon(c, 1340, y - 8, 18, a, GREEN)
            text(c, s, 1375, y, 28, "black", INK, a, align="left")
    al = ep(t, C["11.l"], 0.4)
    if al > 0:
        text(c, "LISTA DA CAIXA: 2 EIXOS", 1520, 510, 22, "black", MOV["lista"], al, tracking=2)
        for k, (lab, s) in enumerate((("A", "escola: aplicação irregular da lei"), ("B", "mídia: pouca visibilidade"))):
            a = ep(t, C["11.l"] + 0.6 + 0.8 * k, 0.4)
            y = 560 + k * 120
            rrect(c, 1280, y, 480, 96, 14, mix("#FFFFFF", MOV["lista"], 0.12), a)
            badge_num(c, lab, 1320, y + 48, a, 22, bg=MOV["lista"])
            para(c, s, 1360, y + 40, 26, "black", INK, a, 380, 30)


def b_mudou(c, t, C, B):
    frame(c, t, B["start"], "DA VERSÃO 1 PARA A 3", "O QUE MUDOU", PURPLE)
    aa = ep(t, C["12.t"], 0.5)
    text(c, "VERSÃO 1", 520, 240, 24, "black", RED, aa, tracking=2)
    text(c, "VERSÃO 3", 1340, 240, 24, "black", GREEN, aa, tracking=2)
    rows = [("12.a", "contexto genérico", "referência verificável, ligada ao recorte", "mapa"),
            ("12.b", "importância", "posição contestável", "tese"),
            ("12.c", "nenhum caminho", "dois eixos anunciados", "lista")]
    for k, (cue, s1, s2, key) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + k * 170 + d
        icone_peca(c, key, 230, y + 55, a, 0.8)
        rrect(c, 310, y, 440, 110, 16, mix("#FFFFFF", RED, 0.08), a)
        text_mid(c, s1, 530, y + 55, 32, "black", RED, a)
        arrow(c, 780, y + 55, 940, y + 55, INK2, a, 5, 18, progress=ep(t, C[cue] + 0.6, 0.5))
        rrect(c, 970, y, 740, 110, 16, mix("#FFFFFF", GREEN, 0.10), ep(t, C[cue] + 0.8, 0.4))
        text_mid(c, s2, 1340, y + 55, 32, "black", GREEN, ep(t, C[cue] + 0.8, 0.4))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    sid = which(t, C, ["13", "14"])
    head_seq(c, t, C, [("13", "NÓS FAZEMOS", "QUAL PEÇA VOCÊ CONSERTA PRIMEIRO?", GREEN), ("14", "NÓS FAZEMOS", "UMA BOA RESPOSTA", GREEN)])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        paper(c, 150, 170, 1080, 660, aa, lh=48, top=290 - 2 * 48 + 6)
        lay, _ = sents_layout(V1S, 260, 290, 34, 920, 48)
        for s, (yy, n) in zip(V1S, lay):
            para(c, s, 260, yy, 34, "bold", INK, aa, 920, 48)
        text(c, "VERSÃO 1", 260, 218, 22, "black", GRAY, aa, align="left", tracking=2)
        ab = ep(t, C["13.b"], 0.5)
        mini_etiqueta(c, 1520, 330, ab, [0, 0, 0, 0], 1.25)
        text(c, "qual peça primeiro? e como?", 1520, 520, 30, "black", INK, ab)
        pause_timer(c, t, C["13.p"] + 0.2, 1520, 680)
        return
    card(c, *CARD_R)
    passos = [("14.a", "tese", "ENDEREÇO: tome posição sobre o recorte"),
              ("14.b", "mapa", "MAPA: troque “desde os primórdios” por uma referência ligada ao recorte"),
              ("14.c", "rua", "RUA DE ACESSO: faça a ponte"),
              ("14.d", "lista", "LISTA DA CAIXA: anuncie os dois eixos")]
    for k, (cue, key, s) in enumerate(passos):
        a, d = rise(t, C[cue])
        y = 250 + k * 130 + d
        badge_num(c, k + 1, 250, y, a, 28, bg=MOV[key])
        icone_peca(c, key, 350, y, a, 0.75)
        para(c, s, 430, y + 12, 34, "black", INK, a, 1250, 40)
    ae = ep(t, C["14.e"], 0.4)
    pill(c, "= o caminho da VERSÃO 3", W / 2, 790, GREEN, size=30, a=ae, anchor="center", bounds=(0, 1920))


# ======================================================================
# recap
# ======================================================================

FRASES = ["Serve para qualquer tema? Não serve para o seu.",
          "Citação decorada não trabalha; referência com ponte trabalha.",
          "Pergunta não é tese; argumento fica para o desenvolvimento."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("15", "26"), FRASES)


# ======================================================================
# as 7 armadilhas
# ======================================================================

ARM = [("16.a1", "16.p1", "abertura universal", "“Desde os primórdios…”, “Hoje em dia, muito se fala sobre…”",
        "um começo seguro", "não informa nada sobre o recorte"),
       ("17.a2", "17.p2", "citação decorada", "frase de pensador encaixada em qualquer tema",
        "erudição", "repertório de bolso: tende a não ser produtivo"),
       ("17.a3", "17.p3", "autoria duvidosa", "frase “famosa” atribuída sem certeza",
        "citação de respeito", "repertório precisa ser legitimado"),
       ("18.a4", "18.p4", "dado sem fonte", "“pesquisas mostram que 90%…”",
        "preciso", "número que não se pode verificar fragiliza o argumento"),
       ("19.a5", "19.p5", "pergunta sem resposta", "“Até quando isso vai continuar?” encerrando a introdução",
        "um final forte", "a pergunta não substitui a tese"),
       ("20.a6", "20.p6", "introdução que já argumenta", "exemplos e explicações que seriam do desenvolvimento",
        "caprichada", "a introdução incha e os eixos se repetem depois"),
       ("20.a7", "20.p7", "tese que tangencia", "tese só sobre o assunto amplo",
        "estar no tema", "compromete o texto inteiro desde o início")]


def b_armadilhas(c, t, C, B):
    sid = which(t, C, ["16", "17", "18", "19", "20"])
    n = 0
    for k, a in enumerate(ARM):
        if t >= C[a[0]] - 0.05:
            n = k
    intro = (sid == "16" and t < C["16.a1"] - 0.05) or (sid == "19" and t < C["19.a5"] - 0.05)
    fase = "NA ABERTURA" if n < 4 and not (sid == "19") else "NO FECHAMENTO"
    head(c, t, C["16"] if fase == "NA ABERTURA" else C["19"], "AS 7 ARMADILHAS", fase, AMBER)
    card(c, *CARD_R)
    for k in range(7):
        done = k < n or (k == n and not intro)
        badge_num(c, k + 1, W / 2 - 240 + k * 80, 210, 1, 22, bg=AMBER if (k == n and not intro) else (INK2 if k < n else LIGHT))
    if intro:
        a = ep(t, C[sid + ".t"], 0.5)
        if sid == "16":
            text(c, "4 na ABERTURA", W / 2, 450, 64, "black", AMBER, a)
            text(c, "+ 3 no fechamento", W / 2, 540, 40, "bold", GRAY, a)
        else:
            text(c, "3 no FECHAMENTO", W / 2, 470, 64, "black", AMBER, a)
            text(c, "da introdução", W / 2, 550, 40, "bold", GRAY, a)
        return
    cue, cue_p, nome, ex, parece, mas = ARM[n]
    aa, d = rise(t, C[cue])
    text(c, nome.upper(), 220, 330 + d, 52, "black", INK, aa, align="left")
    selo(c, 1560, 320, ep(t, C[cue] + 0.3, 0.4), "PEGADINHA", AMBER, 5, 34)
    rrect(c, 220, 380 + d, 1480, 110, 14, PAPER, aa, shadow=True)
    para(c, ex, 260, 448 + d, 32, "bold", PEN, aa, 1400, 38)
    ap = ep(t, C[cue_p], 0.4)
    pill(c, "PARECE " + parece.upper(), 220, 560, AMBER, size=28, a=ap, bounds=(0, 1920))
    am = ep(t, C[cue_p] + 1.3, 0.4)
    check_icon(c, 240, 660, 26, am, RED, "x")
    para(c, "mas " + mas, 285, 672, 36, "black", RED, am, 1400, 42)
    if sid == "18":
        ak = ep(t, C["18.k"], 0.4)
        if ak > 0:
            rrect(c, 220, 735, 1480, 80, 14, mix("#FFFFFF", GREEN, 0.12), ak)
            check_icon(c, 270, 775, 22, ak, GREEN)
            text_mid(c, "conserto das 4: uma referência REAL, ligada ao RECORTE", 990, 775, 32, "black", GREEN, ak)


# ======================================================================
# tamanho
# ======================================================================

def b_tamanho(c, t, C, B):
    frame(c, t, B["start"], "E O TAMANHO?", "1/5 A 1/4 DO TEXTO", PURPLE)
    x, y, w, n, lh = 260, 190, 560, 30, 20.5
    rrect(c, x, y, w, n * lh + 40, 10, "#FFFFFF", 1.0, shadow=True)
    for k in range(n):
        yy = y + 30 + k * lh
        line(c, x + 50, yy, x + w - 30, yy, LIGHT, 1.0, 2)
        text(c, str(k + 1), x + 34, yy - 3, 11, "bold", GRAY, 1.0, align="right")
    ab = ep(t, C["21.b"], 0.5)
    grow = ep(t, C["21.d"], 0.8)
    h1 = (6 + 4 * grow) * lh
    if ab > 0:
        col = mix(GREEN, RED, grow)
        rrect(c, x + 44, y + 30 - lh + 4, w - 64, h1, 6, col, 0.22 * ab)
        line(c, x + w + 20, y + 30 - lh + 4, x + w + 20, y + 30 - lh + 4 + 6 * lh, GREEN, ab, 5)
        line(c, x + w + 40, y + 30 - lh + 4, x + w + 40, y + 30 - lh + 4 + 7.5 * lh, GREEN, ab * 0.6, 5)
        text(c, "introdução", x + w + 70, y + 80, 30, "black", GREEN, ab, align="left")
        text(c, "≈ 1/5 a 1/4 do texto", x + w + 70, y + 124, 30, "black", INK, ab, align="left")
        text(c, "(6 a 7 das 30 linhas)", x + w + 70, y + 164, 22, "bold", GRAY, ab, align="left")
    regra_a = ep(t, C["21.a"], 0.4)
    if regra_a > 0:
        rrect(c, 1000, 480 - 60, 620, 90, 18, mix("#FFFFFF", PURPLE, 0.10), regra_a)
        text_mid(c, "NÃO HÁ TAMANHO OFICIAL", 1310, 465, 36, "black", PURPLE, regra_a)
    selo(c, 1310, 600, ep(t, C["21.c"], 0.4), "SUGESTÃO, NÃO REGRA", GREEN, -4, 30)
    ad = ep(t, C["21.d"], 0.4)
    if ad > 0:
        check_icon(c, 1030, 740, 24, ad, RED, "x")
        para(c, "passou disso? provavelmente está argumentando antes da hora", 1070, 750, 28, "black", RED, ad, 600, 34)


# ======================================================================
# questão 1 (tema de 2025)
# ======================================================================

Q1 = [("A", "Desde sempre, os seres humanos envelhecem. Isso é algo natural e que acontece com todos. Portanto, é importante refletir sobre o envelhecimento.",
       "22.A", "25.xa", "genérica, sem tese contestável", RED),
      ("B", "O envelhecimento das células é estudado pela biologia há séculos. Os cientistas descobriram que o corpo perde funções com o tempo. Esse processo atinge todos os seres vivos.",
       "22.B", "25.xb", "processo biológico universal: TANGENCIAMENTO oficial", AMBER),
      ("C", "O Estatuto da Pessoa Idosa assegura às pessoas com 60 anos ou mais direitos como saúde, dignidade e convivência comunitária. No Brasil, contudo, a velhice ainda é vista sobretudo como perda, o que alimenta o etarismo e atrasa a adaptação das cidades a uma população que envelhece — dois desafios que mostram a urgência de novas perspectivas sobre a velhice.",
       "23.C", None, "", GREEN),
      ("D", "Segundo Platão, a sociedade ideal é governada pelos sábios. Assim, o envelhecimento é um tema que merece a atenção de todos.",
       "23.D", "25.xd", "repertório de bolso, sem posição", RED),
      ("E", "No Japão, a população idosa é numerosa e o país criou diversos serviços para ela. Por isso, o envelhecimento japonês é um exemplo de organização para o mundo.",
       "23.E", "25.xe", "sai do Brasil", RED)]
Q1_ET = [("24.c1", "mapa", "Estatuto da Pessoa Idosa"), ("24.c2", "rua", "“No Brasil, contudo”"),
         ("24.c3", "tese", "novas perspectivas sobre a velhice"), ("24.c4", "lista", "etarismo + adaptação das cidades")]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · ESTILO ENEM", "A MELHOR INTRODUÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["22.a"], 0.4)
    text(c, "ENEM 2025 · “" + TEMA25 + "”", 190, 205, 24, "black", BLUE, aa, align="left")
    text(c, "Qual introdução contextualiza, tem tese sobre o recorte completo e antecipa os argumentos?", 190, 240, 21,
         "bold", INK, aa, align="left")
    alts_panel(c, t, C, Q1, 190, 310, 1130, 21, "24.ok", "C", 6)
    pause_timer(c, t, C["23.end"] - 1.9, 1540, 560)
    ao = ep(t, C["24.ok"], 0.4)
    if ao > 0:
        x0 = 1370
        text(c, "A ETIQUETA DA C", x0 + 170, 300, 20, "black", GREEN, ao, tracking=2)
        for k, (cue, key, s) in enumerate(Q1_ET):
            a = ep(t, C[cue], 0.4)
            y = 360 + k * 110
            icone_peca(c, key, x0 + 30, y + 10, a, 0.55)
            text(c, [p[1] for p in PECAS if p[0] == key][0], x0 + 80, y, 20, "black", MOV[key], a, align="left")
            para(c, s, x0 + 80, y + 32, 21, "bold", INK, a, 260, 25)
            check_icon(c, x0 + 370, y + 4, 14, a, GREEN)
    questao_rotulo(c, aa)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "OFICINA: UMA INTRODUÇÃO DO ZERO", GREEN)
    aa = ep(t, C["27.a"], 0.5)
    text(c, "chega de ver os outros escreverem", W / 2, 260, 40, "black", GRAY, aa)
    rows = [("27.b", "você monta COMIGO, do zero", GREEN), ("27.c", "com um tema REAL do ENEM", BLUE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 390 + k * 130 + d
        badge_num(c, k + 1, 470, y - 16, a, 32, bg=col)
        text(c, s, 530, y, 52, "black", INK, a, align="left")
    ad = ep(t, C["27.d"], 0.5)
    if ad > 0:
        paper(c, 560, 640, 300, 170, ad, lh=34, top=660)
        pen_draw(c, 1000, 730, PEN, ad, -35, 1.0)
        pen_draw(c, 1150, 730, GREEN, ad, -35, 1.0)
        pen_draw(c, 1300, 730, AMBER, ad, -35, 1.0)


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "28", "Qual armadilha você já usou numa introdução?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, etiquetas=b_etiquetas, tema=b_tema, v1=b_v1, v2=b_v2,
              v3=b_v3, mudou=b_mudou, exercicio=b_exercicio, recap=b_recap, armadilhas=b_armadilhas, tamanho=b_tamanho,
              q1=b_q1, ponte=b_ponte, cta=b_cta)
