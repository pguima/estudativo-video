"""Visual — Redação ENEM, Desenvolvimento, Episódio 1: Onde a tese é provada — as cinco partes do parágrafo (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): ícones e ficha das 5 etapas da entrega, barras de peso
típico, tese do estigma, rascunho com caligrafia, alternativas, recap, erros e CTA.
Novo aqui: as duas entregas (caixa fechada na calçada × entrega completa), a caixa da Introdução que se abre em dois
itens (A e B → um parágrafo cada), a mesa (tese = tampo, argumentos = pernas), a escada de 4 degraus que vira 5 partes
e o parágrafo-modelo da seção 08 escrito no rascunho com cada frase sublinhada na cor da sua parte.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep1_anatomia_paragrafo.mp4"


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], SERIE_SELO, "ONDE A TESE É PROVADA", BLUE)
    card(c, *CARD_R)
    aa, ab, ac, ad = (ep(t, C[f"01.{x}"], 0.5) for x in "abcd")
    # a introdução promete
    if aa > 0:
        rrect(c, 220, 230, 520, 200, 20, mix("#FFFFFF", MOV["tese"], 0.10), aa, shadow=True)
        text(c, "INTRODUÇÃO", 480, 290, 26, "black", GRAY, aa, tracking=2)
        text(c, "PROMETEU", 480, 375, 64, "black", MOV["tese"], aa)
    # o desenvolvimento prova... ou repete
    if ab > 0:
        arrow(c, 760, 300, 960, 300, GREEN, ab, 6, 20, progress=ab)
        rrect(c, 980, 230, 700, 200, 20, mix("#FFFFFF", GREEN, 0.10), ab, shadow=True)
        text(c, "DESENVOLVIMENTO", 1330, 290, 26, "black", GRAY, ab, tracking=2)
        text(c, "PROVA", 1300, 375, 64, "black", GREEN, ab * (1 - 0.6 * ac))
        check_icon(c, 1520, 352, 30, ab * (1 - 0.6 * ac), GREEN)
    if ac > 0:
        bubble(c, "…ou só REPETE a promessa", 1000, 470, 640, RED, ac, left=True, size=30)
    # quatro movimentos depois da 1ª frase
    if ad > 0:
        text(c, "depois da 1ª frase, 4 movimentos:", 220, 640, 30, "black", INK2, ad, align="left")
        for k, (s, key) in enumerate((("explicar", "argumento"), ("fundamentar", "repertorio"), ("analisar", "analise"),
                                      ("ligar à tese", "fechamento"))):
            a, d = rise(t, C["01.d"] + 0.3 + 0.25 * k)
            x = 220 + k * 370
            rrect(c, x, 680 + d, 340, 90, 16, mix("#FFFFFF", PARTE[key], 0.14), a)
            icone_etapa(c, key, x + 52, 725 + d, a, 0.55, disc=False)
            text(c, s, x + 100, 736 + d, 32, "black", PARTE[key], a, align="left")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "NESTA AULA", "5 PARTES · 5 PERGUNTAS", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    text(c, "as 5 partes do parágrafo de desenvolvimento", W / 2, 250, 44, "black", INK, aa)
    for k, key in enumerate(KEYS):
        a, d = rise(t, C["02.a"] + 0.4 + 0.25 * k)
        x = 320 + k * 320
        icone_etapa(c, key, x, 400 + d, a, 1.3)
        text(c, NOMEP[key], x, 520 + d, 30, "black", PARTE[key], a)
        ab = ep(t, C["02.b"] + 0.3 * k, 0.4)
        text(c, "“" + PERGP[key] + "”", x, 575 + d, 26, "bold", INK2, ab)
    pill(c, "cada palavra nova, uma de cada vez", W / 2, 740, BLUE, size=28, a=ep(t, C["02.c"], 0.4), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "SÉRIE INTRODUÇÃO", PURPLE)
    rows = [("03.a", "TESE + 2 EIXOS", "eixo = cada caminho que sustenta a sua posição", MOV["tese"]),
            ("03.b", "PROMESSA FEITA", "= promessa cobrada: cada eixo precisa ser provado", MOV["lista"])]
    for k, (cue, lab, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 250 + k * 110 + d
        pill(c, lab, 220, y, col, size=28, a=a, bounds=(0, 1920))
        text(c, s, 220 + text_w(lab, "bold", 28) + 80, y + 11, 32, "black", INK, a, align="left")
    ac = ep(t, C["03.c"], 0.5)
    ex = clamp(ep(t, C["03.d"], 0.4) + ep(t, C["03.e"], 0.4) * 0)
    tese_card(c, 220, 450, 1480, ac, eixos=0, size=32)
    if ac > 0:
        yy = 450 + 96 + 2 * 42 + 40
        pill(c, "EIXO 1 · desinformação", 256, yy, PARTE["topico"], size=26, a=ac * ep(t, C["03.d"], 0.4), bounds=(0, 1920))
        pill(c, "EIXO 2 · mídia", 640, yy, PARTE["argumento"], size=26, a=ac * ep(t, C["03.e"], 0.4), bounds=(0, 1920))


# ======================================================================
# as duas entregas e a analogia da série
# ======================================================================

def calcada(c, x, y, w, a):
    rrect(c, x, y, w, 26, 6, mix("#FFFFFF", GRAY, 0.35), a)
    for k in range(int(w // 120)):
        line(c, x + 60 + k * 120, y, x + 60 + k * 120, y + 26, "#FFFFFF", a, 3)


def b_entrega(c, t, C, B):
    frame(c, t, B["start"], "DUAS ENTREGAS", "QUAL DELAS É ENTREGA?", BLUE)
    q = lambda x: C[f"04.{x}"]
    aa = ep(t, q("a"), 0.5)
    # entrega 1: caixa fechada na calçada, caminhão indo embora
    if aa > 0:
        text(c, "ENTREGA 1", 520, 250, 26, "black", GRAY, aa, tracking=2)
        calcada(c, 200, 690, 660, aa)
        caixa(c, 280, 470, 260, 220, aa)
        u = ep(t, q("a") + 1.0, 2.0)
        truck(c, 600 + 240 * u, 560, aa * (1 - 0.7 * u), BLUE, 0.9)
    # entrega 2: abre, mostra, prova que funciona, recibo
    ab = ep(t, q("b"), 0.5)
    if ab > 0:
        text(c, "ENTREGA 2", 1400, 250, 26, "black", GRAY, ab, tracking=2)
        calcada(c, 1060, 690, 660, ab)
        caixa(c, 1110, 470, 260, 220, ab, open_=ep(t, q("b") + 0.3, 0.8))
        acc = ep(t, q("c"), 0.4)
        icone_etapa(c, "analise", 1240, 400, acc, 1.6, disc=False)
        ad = ep(t, q("d"), 0.4)
        pill(c, "funciona ✓", 1500, 420, GREEN, size=26, a=ad, anchor="center", bounds=(0, 1920))
        ae = ep(t, q("e"), 0.4)
        icone_etapa(c, "fechamento", 1560, 560, ae, 1.5)
        text(c, "recibo assinado", 1560, 660, 26, "black", PARTE["fechamento"], ae)
    af = ep(t, q("f"), 0.4)
    if af > 0:
        check_icon(c, 520, 770, 30, af, RED, "x")
        check_icon(c, 1390, 770, 30, af, GREEN)
        text(c, "caixa largada", 570, 781, 28, "black", RED, af, align="left")
        text(c, "entrega de verdade", 1440, 781, 28, "black", GREEN, af, align="left")


def mesa(c, cx, y, a, w=520, show_pernas=1.0):
    if a <= 0:
        return
    rrect(c, cx - w / 2, y, w, 60, 12, MOV["tese"], a, shadow=True)
    text_mid(c, "TESE", cx, y + 30, 30, "black", "#FFFFFF", a)
    for k, x in enumerate((cx - w / 2 + 50, cx + w / 2 - 80)):
        ak = a * clamp(show_pernas * 2 - k)
        rrect(c, x, y + 60, 30, 230, 6, PARTE["argumento"], ak)
        text(c, "argumento", x + 15, y + 330, 22, "black", PARTE["argumento"], ak)


def b_analogia(c, t, C, B):
    sid = which(t, C, ["05", "06"])
    head_seq(c, t, C, [("05", "A ANALOGIA DA SÉRIE", "A CAIXA SE ABRE", BLUE),
                       ("06", "A ANALOGIA DA SÉRIE", "AS 5 ETAPAS DA ENTREGA", BLUE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "05":
        aT = ep(t, q("t"), 0.5)
        op = ep(t, q("a"), 0.8)
        caixa(c, 260, 360, 380, 300, aT, open_=op)
        if aT > 0:
            rrect(c, 300, 470, 300, 120, 8, "#FFFFFF", aT)
            text(c, "LISTA DA CAIXA", 450, 512, 18, "black", MOV["lista"], aT, tracking=1.5)
            text(c, "contém 2 itens: A e B", 450, 560, 26, "black", INK, aT)
        for k, (cue, lab, s) in enumerate((("c", "A", "1º PARÁGRAFO DE DESENVOLVIMENTO"), ("d", "B", "2º PARÁGRAFO DE DESENVOLVIMENTO"))):
            a, d = rise(t, q(cue))
            y = 290 + k * 230 + d
            badge_num(c, lab, 760, y + 60, a, 40, bg=MOV["lista"])
            arrow(c, 820, y + 60, 940, y + 60, MOV["lista"], a, 5, 18, progress=a)
            rrect(c, 960, y, 700, 120, 18, mix("#FFFFFF", MOV["lista"], 0.10), a, shadow=True)
            text(c, s, 1310, y + 52, 26, "black", MOV["lista"], a)
            for j in range(3):
                line(c, 1000, y + 78 + j * 12, 1620 - j * 90, y + 78 + j * 12, LIGHT, a, 6)
        ab = ep(t, q("b"), 0.4)
        pill(c, "cada parágrafo ENTREGA UM ITEM", W / 2, 790, GREEN, size=30, a=ab, anchor="center", bounds=(0, 1920))
        return
    shw = [ep(t, q(x), 0.4) for x in "abcde"]
    lit = [shw[k] * (1 - (shw[k + 1] if k < 4 else ep(t, q("f"), 0.3))) for k in range(5)]
    af = ep(t, q("f"), 0.5)
    fx = 200 - 0 * af
    ficha_entrega(c, fx, 180, 860, ep(t, q("t"), 0.5), show=shw, lit=lit, partes=0, rowh=98)
    k_at = max((k for k in range(5) if shw[k] > 0), default=-1)
    if k_at >= 0 and af < 1:
        key = KEYS[k_at]
        ak = shw[k_at] * (1 - af)
        icone_etapa(c, key, 1430, 400, ak, 2.2)
        text(c, ETAPA[key], 1430, 580, 40, "black", PARTE[key], ak)
    if af > 0:
        text(c, "SÉRIE DE LINGUAGENS", 1430, 250, 22, "black", PURPLE, af, tracking=2)
        mesa(c, 1430, 330, af, 460, ep(t, q("f") + 1.0, 0.8))
    ag = ep(t, q("g"), 0.4)
    pill(c, "aqui: construir CADA PERNA", 1430, 760, GREEN, size=28, a=ag, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco a: o que o ENEM cobra aqui
# ======================================================================

def b_cobra(c, t, C, B):
    sid = which(t, C, ["07", "08"])
    head_seq(c, t, C, [("07", "O QUE O ENEM COBRA AQUI", "DUAS COMPETÊNCIAS EM JOGO", PURPLE),
                       ("08", "O QUE O ENEM COBRA AQUI", "O QUE A CARTILHA ASSOCIA", PURPLE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "07":
        aa = ep(t, q("a"), 0.4)
        text(c, "5 competências = 5 critérios de correção", 220, 250, 30, "black", INK2, aa, align="left")
        for k in range(5):
            on = k in (1, 2)
            badge_num(c, f"C{k + 1}", 1100 + k * 100, 240, ep(t, q("a") + 0.3 + 0.12 * k, 0.3), 34,
                      bg=PURPLE if on else LIGHT)
        for k, (cue, comp, s) in enumerate((("b", "C3", "seleciona, relaciona, organiza e interpreta informações, fatos e "
                                                       "opiniões em defesa de um ponto de vista"),
                                            ("c", "C2", "repertório sociocultural (conhecimento de fora da prova) "
                                                        "legitimado, pertinente e produtivo"))):
            a, d = rise(t, q(cue))
            y = 340 + k * 210 + d
            if a > 0:
                boxed(c, 220, y, 1480, 170, PURPLE, a, 0.06)
            badge_num(c, comp, 290, y + 85, a, 40, bg=PURPLE)
            para(c, s, 380, y + 72, 34, "black", INK, a, 1260, 44)
        return
    aa = ep(t, q("a"), 0.4)
    cartilha(c, 220, 230, aa, inep=aa, s=1.0)
    if aa > 0:
        text(c, "NÍVEIS MAIS ALTOS DA C3  ↔", 640, 300, 26, "black", PURPLE, aa, align="left", tracking=1)
        para(c, "desenvolvimento dos argumentos com explicitação da sua relevância", 640, 370, 36, "black", INK, aa, 1060, 46)
    ab = ep(t, q("b"), 0.4)
    if ab > 0:
        text(c, "+ AUTORIA", 640, 520, 44, "black", PARTE["analise"], ab, align="left")
        pill(c, "AUTORIA = dá para ver o SEU raciocínio, não só informação juntada", 640, 590, BLUE, size=24, a=ab,
             bounds=(0, 1920))
    pill(c, "cada competência terá a sua própria série", W / 2, 760, BLUE, size=26, a=ep(t, q("c"), 0.4), anchor="center")


# ======================================================================
# bloco b: as três ideias que mais rendem
# ======================================================================

IDEIAS = [("a", "um parágrafo = UM EIXO", "anunciado na introdução", MOV["lista"]),
          ("b", "repertório + ANÁLISE", "só assim ele é produtivo", PARTE["analise"]),
          ("c", "a última frase responde: E DAÍ?", "liga o parágrafo de volta à tese", PARTE["fechamento"])]


def b_ideias(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "3 IDEIAS PARA GUARDAR", GREEN)
    for k, (cue, s, sub, col) in enumerate(IDEIAS):
        a, d = rise(t, C[f"09.{cue}"])
        x = 200 + k * 520
        if a > 0:
            rrect(c, x, 280 + d, 480, 400, 22, mix("#FFFFFF", col, 0.08), a, shadow=True)
        badge_num(c, k + 1, x + 240, 360 + d, a, 44, bg=col)
        para(c, s, x + 240, 480 + d, 40, "black", col, a, 420, 48, align="center")
        para(c, sub, x + 240, 610 + d, 28, "bold", INK2, a, 420, 34, align="center")


# ======================================================================
# bloco c: as cinco partes e suas perguntas
# ======================================================================

DEF = dict(topico="anuncia o que o parágrafo vai provar (em geral, a 1ª frase)",
           argumento="explica POR QUE a afirmação procede",
           repertorio="conhecimento de fora que COMPROVA",
           analise="interpreta a referência à luz do problema",
           fechamento="liga tudo de volta à tese")


def b_partes(c, t, C, B):
    head_seq(c, t, C, [("10", "AS 5 PARTES", "UMA DE CADA VEZ", BLUE), ("11", "AS 5 PARTES", "5 PARTES · 5 PERGUNTAS", BLUE)])
    cues = [C["10.a"], C["10.b"], C["10.c"], C["11.d"], C["11.e"]]
    shw = [ep(t, x, 0.4) for x in cues]
    af = ep(t, C["11.f"], 0.4)
    lit = [shw[k] * (1 - (shw[k + 1] if k < 4 else af)) for k in range(5)]
    ficha_entrega(c, 140, 150, 980, 1.0, show=shw, lit=lit, perguntas=1.0, partes=1.0, rowh=118, title="AS 5 PARTES DO PARÁGRAFO")
    k_at = max((k for k in range(5) if shw[k] > 0), default=-1)
    if k_at >= 0 and af < 1:
        key = KEYS[k_at]
        a = shw[k_at] * (1 - af)
        icone_etapa(c, key, 1460, 360, a, 2.0)
        text(c, NOMEP[key].upper(), 1460, 520, 40, "black", PARTE[key], a)
        para(c, DEF[key], 1460, 590, 30, "bold", INK2, a, 560, 38, align="center")
    if af > 0:
        text(c, "5 PARTES", 1460, 400, 64, "black", INK, af)
        text(c, "5 PERGUNTAS", 1460, 480, 64, "black", INK, af)
        text(c, "= as 5 etapas da entrega", 1460, 560, 30, "black", GREEN, af)


# ======================================================================
# bloco d: o peso de cada parte
# ======================================================================

def b_peso(c, t, C, B):
    frame(c, t, B["start"], "O PESO DE CADA PARTE", "A ANÁLISE É A MAIS LONGA", BLUE)
    aa = ep(t, C["12.a"], 0.4)
    shw = [ep(t, C["12.a"] + 0.25 * k, 0.6) for k in range(5)]
    barras_peso(c, 220, 240, 1480, aa, rowh=82, show=shw, aviso=ep(t, C["12.d"], 0.4))
    ab = ep(t, C["12.b"], 0.4)
    if ab > 0:
        y = 240 + 3 * 82
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(200, y + 2, 1520, 78), 16, 16), paint(PARTE["analise"], ab, stroke=4))
        pill(c, "AUTORIA", 1640, y + 41, PARTE["analise"], size=24, a=ab, anchor="right", bounds=(0, 1920))
    ac = ep(t, C["12.c"], 0.4)
    icone_etapa(c, "analise", 300, 730, ac, 1.0)
    text(c, "o produto funcionando: o que o cliente mais quer ver", 370, 742, 30, "black", PARTE["analise"], ac, align="left")


# ======================================================================
# blocos e e f: a escada e método, não regra
# ======================================================================

def b_metodo(c, t, C, B):
    sid = which(t, C, ["13", "14"])
    head_seq(c, t, C, [("13", "DE ONDE VÊM AS 5 PARTES", "A ESCADA DE 4 DEGRAUS", PURPLE),
                       ("14", "UM AVISO IMPORTANTE", "MÉTODO, NÃO REGRA", GREEN)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "13":
        degraus = [("a1", "afirmar", ["topico"]), ("a2", "explicar", ["argumento"]), ("a3", "fundamentar", ["repertorio", "analise"]),
                   ("a4", "ligar", ["fechamento"])]
        ab = ep(t, q("b"), 0.6)
        for k, (cue, s, keys) in enumerate(degraus):
            a, d = rise(t, q(cue))
            x, y = 220 + k * 330, 620 - k * 95
            if a > 0:
                rrect(c, x, y + d, 320, 760 - y, 10, mix("#FFFFFF", PURPLE, 0.10 + 0.05 * k), a)
            text(c, s, x + 160, y + 50 + d, 34, "black", PURPLE, a)
            for j, key in enumerate(keys):
                kk = a * (ab if len(keys) > 1 else ep(t, q("b") + 0.8, 0.4))
                xx = x + 160 + (j - (len(keys) - 1) / 2) * 150
                icone_etapa(c, key, xx, y + 120 + d, kk, 0.7)
                text(c, NOMEP[key], xx, y + 190 + d, 20, "black", PARTE[key], kk)
        pill(c, "4 degraus → 5 partes", 1560, 260, PURPLE, size=28, a=ab, anchor="center", bounds=(0, 1920))
        pill(c, "série Competência 3: como o corretor pontua", 1560, 330, BLUE, size=22, a=ep(t, q("c"), 0.4), anchor="center",
             bounds=(0, 1920))
        return
    aa = ep(t, q("a"), 0.4)
    entrega_selo(c, 470, 260, aa, -4, 40)
    text(c, "método de estudo ≠ critério do Inep", 1190, 275, 38, "black", INK, aa)
    itens = [("b", "a ordem pode mudar (repertório antes da explicação)"), ("c", "duas partes cabem numa mesma frase"),
             ("d", "não há número oficial de parágrafos"), ("e", "2 desenvolvimentos: o mais comum, cabe bem na folha")]
    for k, (cue, s) in enumerate(itens):
        a, d = rise(t, q(cue))
        y = 380 + k * 70 + d
        check_icon(c, 240, y - 10, 20, a, GREEN)
        text(c, s, 280, y, 32, "black", INK, a, align="left")
    af = ep(t, q("f"), 0.4)
    if af > 0:
        boxed(c, 220, 670, 1480, 120, PURPLE, af, 0.06)
        text(c, "OS DESCRITORES AVALIAM", 250, 710, 20, "black", PURPLE, af, align="left", tracking=2)
        text(c, "informações relacionadas ao tema, organizadas, desenvolvidas e a serviço de um ponto de vista", 250, 760,
             28, "black", INK, af, align="left")


# ======================================================================
# eu faço / nós fazemos: o parágrafo-modelo no rascunho
# ======================================================================

PX, PY, PW, PH = 150, 160, 1620, 690
HX, HS, HLH, HMW = 270, 29, 46, 1440


def modelo_layout():
    out, y = [], PY + 150
    for s in MODELO:
        lines = hwrap(s, HS, HMW)
        out.append((s, y, len(lines), lines))
        y += len(lines) * HLH
    return out


_LAY = modelo_layout()


def rascunho_modelo(c, t, a, reveals=(1, 1, 1, 1, 1), under=(0, 0, 0, 0, 0), tema_a=1.0, icons=(0, 0, 0, 0, 0)):
    paper(c, PX, PY, PW, PH, a, lh=HLH, top=PY + 150 - 2 - 3 * HLH)
    text(c, "ENEM 2020 · D1 · eixo da desinformação", PX + 110, PY + 64, 24, "black", BLUE, a * tema_a, align="left")
    text(c, PARAG_DIDATICO, PX + 110, PY + 100, 18, "medium", AMBER, a * tema_a, align="left")
    for k, (s, y, n, lines) in enumerate(_LAY):
        hand_para(c, s, HX, y, HS, PEN, a, HMW, HLH, reveal=reveals[k])
        if under[k] > 0:
            for j, ln in enumerate(lines):
                fr = clamp(under[k] * n - j)
                if fr > 0:
                    underline(c, HX, HX + hand_w(ln, HS), y + j * HLH + 9, PARTE[KEYS[k]], a, fr, 5)
        if icons[k] > 0:
            icone_etapa(c, KEYS[k], PX + 75, y - 8, a * icons[k], 0.36)


def b_eufaco(c, t, C, B):
    sid = which(t, C, ["15", "16", "17"])
    head_seq(c, t, C, [("15", "EU FAÇO · AO VIVO", "O PARÁGRAFO NO RASCUNHO", GREEN),
                       ("16", "EU FAÇO · AO VIVO", "ENTREGANDO O ITEM A", GREEN),
                       ("17", "EU FAÇO · AO VIVO", "AS 5 ETAPAS, EM CORES", GREEN)])
    a = ep(t, C["15"], 0.5)
    ends = [C["16.s2"], C["16.s3"], C["17.s4"], C["17.s5"], C["17.m"]]
    starts = [C["16.s1"], C["16.s2"], C["16.s3"], C["17.s4"], C["17.s5"]]
    rv = [wreveal(t, (starts[k], ends[k] - 0.5)) for k in range(5)]
    cc = [C[f"17.c{k + 1}"] for k in range(5)]
    und = [ep(t, cc[k], 1.0) for k in range(5)]
    ics = [ep(t, cc[k] + 0.3, 0.4) for k in range(5)]
    rascunho_modelo(c, t, a, rv, und, ep(t, C["15.a"], 0.4), ics)
    if sid == "15":
        pill(c, "vou ler devagar", PX + PW - 60, PY + 64, GREEN, size=24, a=ep(t, C["15.b"], 0.4), anchor="right", bounds=(0, 1920))
    av = ep(t, C["17.v"], 0.4)
    pill(c, "frase por frase: episódio 5", PX + PW - 60, PY + PH - 46, BLUE, size=22, a=av, anchor="right", bounds=(0, 1920))


def b_exercicio(c, t, C, B):
    sid = which(t, C, ["20", "21"])
    head_seq(c, t, C, [("20", "NÓS FAZEMOS", "QUAL ETAPA É CADA FRASE?", AMBER), ("21", "NÓS FAZEMOS", "CONFERINDO", GREEN)])
    if sid == "20":
        rascunho_modelo(c, t, 1.0)
        pause_timer(c, t, C["20.p"] + 0.3, PX + PW - 110, PY + PH - 110)
        return
    und = [ep(t, C[f"21.s{k + 1}"], 1.0) for k in range(5)]
    ics = [ep(t, C[f"21.s{k + 1}"], 0.4) for k in range(5)]
    rascunho_modelo(c, t, 1.0, under=und, icons=ics)
    for k in range(5):
        s, y, n, lines = _LAY[k]
        x = HX + hand_w(lines[-1], HS) + 24
        yy = y + (n - 1) * HLH - 8
        lab = ETAPA[KEYS[k]].lower()
        if x + text_w(lab, "bold", 18) + 40 > PX + PW - 20:
            x = PX + PW - 40 - text_w(lab, "bold", 18) - 30
            yy -= 0
        pill(c, lab, x, yy, PARTE[KEYS[k]], size=18, a=ics[k], bounds=(0, 1920))
    ad = ep(t, C["21.d"], 0.4)
    selo(c, PX + PW - 300, PY + PH - 70, ad, "ARQUITETURA ✓", GREEN, -4, 28)


# ======================================================================
# exemplo × contraexemplo
# ======================================================================

def b_lado(c, t, C, B):
    head(c, t, B["start"], "LADO A LADO · MESMO EIXO", "5 PARTES × SÓ OPINIÃO", BLUE)
    for x in (160, 990):
        card(c, x, 150, 770, 690)
    pill(c, "COM AS 5 PARTES", 200, 200, GREEN, size=24, bounds=(0, 1920))
    faixas_paragrafo(c, 214, 262, 690, 17, 23, MODELO, KEYS, 1.0, faixa=[1] * 5, nums=False, peso="medium")
    mini_entrega(c, 545, 742, 1.0, [1, 1, 1, 1, 1], 0.9)
    aa = ep(t, C["18.a"], 0.5)
    pill(c, "SÓ OPINIÃO", 1030, 200, RED, size=24, a=aa, bounds=(0, 1920))
    para(c, V1_OPINIAO, 1030, 270, 27, "bold", INK, aa, 690, 36)
    text(c, DIDATICO, 1030, 470, 16, "medium", AMBER, aa, align="left")
    ab = ep(t, C["18.b"], 0.4)
    marks = [ab, ep(t, C["18.d"], 0.4), ep(t, C["18.e"], 0.4), ep(t, C["18.f"], 0.4), ab]
    oks = [1 if marks[0] > 0.5 else None, 0 if marks[1] > 0.5 else None, 0 if marks[2] > 0.5 else None,
           0 if marks[3] > 0.5 else None, 1 if marks[4] > 0.5 else None]
    mini_entrega(c, 1180, 650, aa, oks, 0.9)
    ac = ep(t, C["18.c"], 0.4)
    text(c, "o meio só REPETE", 1380, 560, 28, "black", RED, ac, align="left")
    ag = ep(t, C["18.g"], 0.4)
    selo(c, 1530, 760, ag, "CAIXA FECHADA", RED, -6, 30)


# ======================================================================
# recap, erros, questão 6, ponte, CTA
# ======================================================================

FRASES = ["Cada parágrafo entrega um item da lista.", "Etiqueta, por quê, nota fiscal, produto funcionando, recibo.",
          "Cinco partes é método; o raciocínio é que não pode faltar."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("19", "28"), FRASES, cols=[MOV["lista"], PARTE["analise"], GREEN])


ERROS = [("22", "Achar que desenvolver é “dar mais opiniões”", "o parágrafo fica mais cheio",
          "opinião repetida não é argumento: explique, comprove e analise"),
         ("23", "Achar que a ordem das 5 partes é obrigatória", "o modelo vem sempre na mesma sequência",
          "é método: a ordem varia; o que não pode faltar é o raciocínio"),
         ("24", "Gastar o parágrafo com a referência e não analisar", "citar uma obra famosa impressiona",
          "repertório só é produtivo com análise: é ali que aparece a autoria")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


Q6 = "Sobre a estrutura tópico frasal – argumento – repertório – análise – fechamento, é correto afirmar que"
ALT6 = [("A", "é exigida pela Cartilha do Participante, e a falta de qualquer parte zera a Competência 3.", "25.A", "27.xa",
         "inventa regra e punição", RED),
        ("B", "vale só para o primeiro parágrafo de desenvolvimento.", "25.B", "27.xb", "restringe sem motivo", RED),
        ("C", "proíbe que o repertório apareça antes da explicação do argumento.", "25.C", "27.xc",
         "sugestão virou proibição", RED),
        ("D", "dispensa o repertório, desde que o parágrafo tenha análise.", "26.D", "27.xd", "contraria a C2", RED),
        ("E", "é um método de estudo: as partes podem variar de ordem, mas os descritores avaliam se as informações estão "
              "relacionadas ao tema, organizadas e desenvolvidas em defesa de um ponto de vista.", "26.E", None, "", GREEN)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "MÉTODO OU REGRA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["25.a"], 0.4)
    text(c, "QUESTÃO 6", 190, 230, 18, "black", GRAY, aa, align="left", tracking=2)
    para(c, Q6, 190, 290, 30, "black", INK, aa, 540, 40)
    mini_entrega(c, 460, 560, aa, [None] * 5, 0.85)
    alts_panel(c, t, C, ALT6, 790, 232, 950, 23, "27.ok", "E", 6)
    pause_timer(c, t, C["26.end"] - 1.9, 460, 740)
    questao_rotulo(c, aa)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A ETIQUETA DO ITEM", BLUE)
    aa = ep(t, C["29.a"], 0.4)
    icone_etapa(c, "topico", 420, 400, aa, 2.4)
    text(c, "toda entrega começa pela ETIQUETA", 680, 400, 44, "black", PARTE["topico"], aa, align="left")
    ab = ep(t, C["29.b"], 0.4)
    if ab > 0:
        rrect(c, 680, 450, 520, 110, 16, "#FFFFFF", ab, shadow=True)
        text(c, "“coisa”", 940, 523, 44, "black", GRAY, ab)
        text(c, "etiqueta vaga = ninguém sabe o que chegou", 680, 620, 30, "black", RED, ab, align="left")
    pill(c, "Ep. 2 · o TÓPICO FRASAL", W / 2, 760, GREEN, size=30, a=ep(t, C["29.c"], 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "30", "Qual etapa da entrega o seu parágrafo costuma esquecer?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, entrega=b_entrega, analogia=b_analogia, cobra=b_cobra,
              ideias=b_ideias, partes=b_partes, peso=b_peso, metodo=b_metodo, eufaco=b_eufaco, lado=b_lado, recap=b_recap,
              exercicio=b_exercicio, erros=b_erros, q6=b_q6, ponte=b_ponte, cta=b_cta)
