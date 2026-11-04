"""Visual — Redação ENEM, Introdução, Episódio 1: Da tese ao primeiro parágrafo — os três movimentos (tema claro).
Usa o desenho compartilhado da série (introducao_visual.py): etiqueta com 3 faixas (MAPA · ENDEREÇO + ENTREGA ·
LISTA DA CAIXA; a RUA DE ACESSO só entra no ep. 3), folha de rascunho com caligrafia, alternativas, recap, erros e CTA.
Novo aqui: a Versão 3 da seção 07 escrita no rascunho com cada movimento sublinhado na cor da peça, a barra de
proporções típicas ("não é regra") e a tabela movimento × competência.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep1_tres_movimentos.mp4"
K3 = ("mapa", "tese", "lista")
NOME = {p[0]: p[1] for p in PECAS}
PERG = {p[0]: p[3] for p in PECAS}
MOVN = {"mapa": "contextualização", "tese": "tese", "lista": "antecipação dos argumentos"}


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def folha_redacao(c, x, y, w, h, a, hl=0.0, generic=0.0):
    """folha com o 1º parágrafo em destaque (linhas = texto)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, "#FFFFFF", a, shadow=True)
    text(c, "FOLHA DE REDAÇÃO", x + w / 2, y + 44, 20, "black", GRAY, a, tracking=2)
    yy = y + 90
    for k in range(13):
        first = k < 3
        col = mix(LIGHT, MOV["tese"], 0.0) if not first else (mix(LIGHT, AMBER, generic) if generic else mix(LIGHT, BLUE, hl))
        x0 = x + 40 + (40 if k in (0, 3, 7, 10) else 0)
        line(c, x0, yy, x + w - 40 - (60 if k in (2, 6, 9, 12) else 0), yy, col, a, 9)
        yy += 36 if k not in (2, 6, 9) else 54
    if hl > 0:
        rrect(c, x + 20, y + 66, w - 40, 112, 10, mix("#FFFFFF", BLUE, 0.10), a * hl * (1 - generic))


def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · INTRODUÇÃO", "OS TRÊS MOVIMENTOS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    ac = ep(t, C["01.c"], 0.5)
    folha_redacao(c, 260, 190, 560, 620, aa, hl=aa, generic=ab * (1 - ac))
    pill(c, "1º PARÁGRAFO = o mais lido", 860, 250, BLUE, size=30, a=aa * (1 - ab), bounds=(0, 1920))
    if ab > 0 and ac < 1:
        selo(c, 540, 300, ab * (1 - ac), "SERVE PARA QUALQUER TEMA", AMBER, -5, 30)
        text(c, "= linhas desperdiçadas", 1180, 470, 44, "black", AMBER, ab * (1 - ac))
    if ac > 0:
        arrow(c, 840, 300, 1060, 400, GREEN, ac, 6, 20, progress=ac)
        etiqueta_intro(c, 1080, 230, 600, ac, keys=K3, movs=0, rowh=84, title="O TEXTO VAI PARA...")
        text(c, "o corretor já sabe para onde o texto vai", 1380, 700, 28, "black", GREEN, ep(t, C["01.c"] + 1.0, 0.5))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "NESTA AULA", "3 TAREFAS · 3 PERGUNTAS", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    text(c, "as 3 tarefas do 1º parágrafo", W / 2, 260, 44, "black", INK, aa)
    for k, key in enumerate(K3):
        a, d = rise(t, C["02.a"] + 0.4 + 0.3 * k)
        x = 460 + k * 500
        icone_peca(c, key, x, 420 + d, a, 1.5)
        ab = ep(t, C["02.b"] + 0.4 * k, 0.4)
        para(c, "“" + PERG[key] + "”", x, 560 + d, 30, "black", MOV[key], ab, 420, 38, align="center")
    pill(c, "cada palavra nova, uma de cada vez", W / 2, 760, BLUE, size=28, a=ep(t, C["02.c"], 0.4), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "SÉRIE LEITURA DA PROPOSTA", PURPLE)
    rows = [("03.a", "TEMA", "o recorte exato da prova = o ENDEREÇO de entrega", BLUE),
            ("03.b", "TESE", "a sua posição sobre ele = o que você ENTREGA", MOV["tese"]),
            ("03.c", "TESE PROVISÓRIA", "+ 2 EIXOS: os caminhos que sustentam a posição", GREEN)]
    for k, (cue, lab, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 250 + k * 130 + d
        pill(c, lab, 220, y, col, size=30, a=a, bounds=(0, 1920))
        text(c, s, 220 + text_w(lab, "bold", 30) + 90, y + 11, 34, "black", INK, a, align="left")
    pill(c, "Linguagens: compreensão global e tese → você já conhece", 220, 640, PURPLE, size=24, a=ep(t, C["03.d"], 0.4),
         bounds=(0, 1920))
    ae = ep(t, C["03.e"], 0.4)
    text(c, "agora: a ETIQUETA INTEIRA", 1640, 750, 44, "black", GREEN, ae, align="right")


# ======================================================================
# a etiqueta completa
# ======================================================================

EX, EY, EW, ERH = 820, 220, 900, 110


def b_etiqueta(c, t, C, B):
    sid = which(t, C, ["04", "05"])
    head_seq(c, t, C, [("04", "A ANALOGIA DA SÉRIE", "A ETIQUETA COMPLETA", BLUE),
                       ("05", "A ANALOGIA DA SÉRIE", "INTRODUÇÃO = ETIQUETA COMPLETA", BLUE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    rows_y = [EY + 96 + ERH * k + ERH / 2 for k in range(3)]
    if sid == "04":
        show = [ep(t, q(x), 0.4) for x in "bcd"]
        etiqueta_intro(c, EX, EY, EW, ep(t, q("a"), 0.5), show=show, keys=K3, movs=0, rowh=ERH)
        caixa(c, 260, 400, 380, 300, ep(t, q("t"), 0.5), label=True, label_a=ep(t, q("a"), 0.4))
        ae = ep(t, q("e"), 0.4)
        pill(c, "ninguém se perde ✓", 450, 780, GREEN, size=28, a=ae, anchor="center", bounds=(0, 1920))
        return
    lit = [ep(t, q(x), 0.4) * (1 - ep(t, q(n), 0.3)) for x, n in (("a", "b"), ("b", "c"), ("c", "d"))]
    etiqueta_intro(c, EX, EY, EW, 1.0, keys=K3, movs=0, rowh=ERH, lit=lit)
    aT = ep(t, q("t"), 0.4)
    text(c, "INTRODUÇÃO", 450, 250, 40, "black", INK, aT)
    text(c, "= o 1º parágrafo", 450, 292, 26, "bold", GRAY, aT)
    for k, (cue, key) in enumerate(zip("abc", K3)):
        a = ep(t, q(cue), 0.4)
        y = rows_y[k]
        pill(c, MOVN[key], 450, y, MOV[key], size=28, a=a, anchor="center", bounds=(0, 1920))
        arrow(c, 450 + text_w(MOVN[key], "bold", 28) / 2 + 40, y, EX - 12, y, MOV[key], a, 4, 14, progress=a)
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        boxed(c, 220, 700, 1480, 100, BLUE, ad, 0.08)
        text_mid(c, "DESENVOLVIMENTO = os parágrafos entre a introdução e a conclusão", W / 2 - 10, 750, 30, "black", BLUE, ad)


# ======================================================================
# bloco a: a introdução é avaliada sozinha?
# ======================================================================

def b_avalia(c, t, C, B):
    frame(c, t, B["start"], "A INTRODUÇÃO GANHA NOTA SOZINHA?", "O QUE O ENEM COBRA", BLUE)
    aa = ep(t, C["06.a"], 0.4)
    selo(c, 330, 260, aa, "NÃO", RED, -6, 54)
    text(c, "nenhum descritor avalia a introdução isoladamente", 460, 272, 34, "black", INK, aa, align="left")
    ad0 = ep(t, C["06.d0"], 0.4)
    pill(c, "DESCRITOR = a frase da grade que descreve cada nível de nota", 460, 340, BLUE, size=24, a=ad0, bounds=(0, 1920))
    ab = ep(t, C["06.b"], 0.4)
    text(c, "o Inep corrige o TEXTO INTEIRO", 220, 460, 32, "black", INK2, ab, align="left")
    for k in range(5):
        badge_num(c, f"C{k + 1}", 780 + k * 90, 449, ep(t, C["06.b"] + 0.4 + 0.15 * k, 0.3), 32, bg=PURPLE)
    ac = ep(t, C["06.c"], 0.4)
    text(c, "mas é na introdução que o corretor começa a perceber:", 220, 560, 30, "bold", GRAY, ac, align="left")
    itens = [("06.d", "ponto de vista", "C2", None), ("06.e", "projeto de texto", "C3", "o plano da redação"),
             ("06.f", "1º repertório", "C2", "o conhecimento de fora")]
    for k, (cue, s, comp, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        x = 220 + k * 500
        rrect(c, x, 600 + d, 460, 190, 18, mix("#FFFFFF", BLUE, 0.07), a, shadow=True)
        pill(c, comp, x + 400, 640 + d, PURPLE, size=22, a=a, anchor="center", bounds=(0, 1920))
        text(c, s, x + 30, 690 + d, 36, "black", BLUE, a, align="left")
        if sub:
            text(c, "= " + sub, x + 30, 750 + d, 26, "bold", INK2, a, align="left")


# ======================================================================
# blocos b e c: a Cartilha
# ======================================================================

def b_cartilha(c, t, C, B):
    frame(c, t, B["start"], "REGRA OFICIAL", "O QUE DIZ A CARTILHA", PURPLE)
    cartilha(c, 200, 230, ep(t, C["07.t"], 0.5), inep=ep(t, C["07.t"] + 1.5, 0.4), s=1.05)
    aa = ep(t, C["07.a"], 0.4)
    text(c, "A TAREFA, SEGUNDO A CARTILHA", 620, 260, 22, "black", PURPLE, aa, align="left", tracking=2)
    verbs = [("07.b", "inicie o texto apresentando seu ponto de vista"), ("07.b2", "desenvolva justificativas para comprová-lo"),
             ("07.b3", "e elabore uma conclusão")]
    for k, (cue, s) in enumerate(verbs):
        a, d = rise(t, C[cue])
        y = 320 + k * 62 + d
        badge_num(c, k + 1, 640, y - 10, a, 20, bg=PURPLE)
        text(c, s, 680, y, 32, "black", INK, a, align="left")
    ac = ep(t, C["07.c"], 0.4)
    if ac > 0:
        boxed(c, 620, 540, 1080, 250, PURPLE, ac, 0.06)
        text(c, "CARTILHA 2026 · COMENTÁRIOS DE REDAÇÕES DE NOTA ALTA", 650, 590, 20, "black", PURPLE, ac, align="left",
             tracking=1.5)
        text(c, "“na introdução, são apresentadas…”", 650, 640, 28, "bold", INK2, ac, align="left")
        for k, (cue, key, s) in enumerate((("07.d", "mapa", "a contextualização"), ("07.d2", "tese", "a tese"),
                                           ("07.d3", "lista", "a antecipação dos argumentos"))):
            a = ep(t, C[cue], 0.3)
            x = [650, 1000, 1210][k]
            pill(c, s, x, 720, MOV[key], size=26, a=a, bounds=(0, 1920))


# ======================================================================
# bloco d: três perguntas do leitor
# ======================================================================

def b_perguntas(c, t, C, B):
    frame(c, t, B["start"], "UM PARÁGRAFO", "TRÊS PERGUNTAS DO LEITOR", GREEN)
    for k, key in enumerate(K3):
        cue = "abc"[k]
        a, d = rise(t, C[f"08.{cue}"])
        y = 270 + k * 175 + d
        if a > 0:
            rrect(c, 200, y - 70, 1520, 145, 20, mix("#FFFFFF", MOV[key], 0.08), a)
        badge_num(c, k + 1, 250, y, a, 30, bg=MOV[key])
        text(c, "“" + PERG[key] + "”", 310, y + 12, 44, "black", INK, a, align="left")
        a2 = ep(t, C[f"08.{cue}2"], 0.4)
        icone_peca(c, key, 1250, y, a2, 0.8)
        text(c, NOME[key], 1320, y - 4, 28, "black", MOV[key], a2, align="left")
        text(c, MOVN[key], 1320, y + 34, 24, "bold", INK2, a2, align="left")


# ======================================================================
# bloco e: movimento × competência (tabela da seção 02)
# ======================================================================

TAB = [("09.a", "mapa", "Contextualização", "situar o problema e mostrar repertório pertinente", "C2"),
       ("09.b", "tese", "Tese", "tomar posição sobre o recorte completo", "C2 · C3"),
       ("09.c", "lista", "Antecipação", "anunciar os eixos do desenvolvimento", "C3"),
       ("09.d", None, "Articulação", "ligar as frases com conectivos e retomadas", "C4")]


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "CADA MOVIMENTO, UMA COMPETÊNCIA", "MOVIMENTO × COMPETÊNCIA", PURPLE)
    a0 = ep(t, C["09.t"], 0.4)
    for s, x in (("MOVIMENTO", 300), ("FUNÇÃO", 720), ("COMPETÊNCIA", 1500)):
        text(c, s, x, 230, 20, "black", GRAY, a0, align="left", tracking=2)
    for k, (cue, key, mov, fn, comp) in enumerate(TAB):
        a, d = rise(t, C[cue])
        y = 310 + k * 110 + d
        line(c, 200, y - 55, 1720, y - 55, LINE, a0, 2)
        if key:
            icone_peca(c, key, 245, y - 8, a, 0.55, disc=False)
        else:
            text_mid(c, "⇄", 245, y - 8, 44, "black", GRAY, a)
        text(c, mov, 300, y, 34, "black", MOV.get(key, INK2) if key else INK2, a, align="left")
        para(c, fn, 720, y - 4, 26, "bold", INK2, a, 700, 30)
        pill(c, comp, 1500, y - 10, PURPLE, size=28, a=a, bounds=(0, 1920))
    pill(c, "cada competência terá a sua própria série", W / 2, 790, BLUE, size=26, a=ep(t, C["09.e"], 0.4), anchor="center")


# ======================================================================
# bloco f: método, não regra
# ======================================================================

def barra(c, x, y, w, a, labels=1.0):
    parts = [("mapa", 0.42, "contextualização"), ("tese", 0.33, "tese"), ("lista", 0.25, "antecipação")]
    xx = x
    for k, (key, f, s) in enumerate(parts):
        ww = w * f
        rrect(c, xx + 3, y, ww - 6, 70, 12, MOV[key], a)
        text_mid(c, s, xx + ww / 2, y + 35, 28, "black", "#FFFFFF", a * labels)
        xx += ww


def b_metodo(c, t, C, B):
    sid = which(t, C, ["10", "11"])
    head_seq(c, t, C, [("10", "UM AVISO IMPORTANTE", "MÉTODO, NÃO REGRA", GREEN), ("11", "O QUE CONTA DE VERDADE", "OS DESCRITORES", PURPLE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "10":
        aa = ep(t, q("a"), 0.4)
        metodo_selo(c, 470, 270, aa, -4, 40)
        text(c, "método de estudo ≠ critério do Inep", 1190, 285, 38, "black", INK, aa)
        text(c, "a Cartilha NÃO exige:", 220, 410, 28, "black", PURPLE, ep(t, q("b"), 0.4), align="left")
        for k, (cue, s) in enumerate((("b", "número fixo de frases"), ("b2", "ordem obrigatória"), ("b3", "tamanho"))):
            a = ep(t, q(cue), 0.4)
            x = 220 + k * 500
            check_icon(c, x + 20, 480, 22, a, RED, "x")
            text(c, s, x + 60, 492, 32, "black", INK, a, align="left")
        ac = ep(t, q("c"), 0.5)
        barra(c, 260, 600, 1400 * ep(t, q("c"), 1.0) if ac < 1 else 1400, ac, ep(t, q("c") + 0.8, 0.4))
        pill(c, "proporção TÍPICA · não é regra", W / 2, 730, AMBER, size=28, a=ep(t, q("c") + 1.2, 0.4), anchor="center")
        return
    aa = ep(t, q("a"), 0.4)
    if aa > 0:
        boxed(c, 220, 220, 1480, 190, PURPLE, aa, 0.06)
        text(c, "O QUE OS DESCRITORES PEDEM", 260, 268, 20, "black", PURPLE, aa, align="left", tracking=2)
        text(c, "proposição, argumentação e conclusão", 260, 330, 34, "black", INK, aa, align="left")
        pill(c, "C2", 960, 320, PURPLE, size=26, a=aa, bounds=(0, 1920))
        a2 = ep(t, q("a2"), 0.4)
        text(c, "projeto de texto perceptível", 1060, 330, 34, "black", INK, a2, align="left")
        pill(c, "C3", 1580, 320, PURPLE, size=26, a=a2, bounds=(0, 1920))
    ab = ep(t, q("b"), 0.4)
    mini_etiqueta(c, 500, 600, ab, [1, 1, None], 1.1, keys=K3)
    text(c, "contextualiza + tese, sem anunciar eixos", 760, 570, 32, "black", INK, ab, align="left")
    text(c, "→ PODE FUNCIONAR", 760, 625, 36, "black", GREEN, ab, align="left")
    ac = ep(t, q("c"), 0.4)
    pill(c, "o modelo só REDUZ O RISCO de esquecer algo", 760, 715, GREEN, size=28, a=ac, bounds=(0, 1920))


# ======================================================================
# eu faço / nós fazemos: a Versão 3 no rascunho
# ======================================================================

PX, PY, PW, PH = 160, 170, 1600, 670
HX, HS, HLH, HMW = 290, 32, 50, 1420
LISTA = ["a aplicação irregular da lei nas escolas", "a pouca visibilidade na mídia"]


def v3_layout():
    out, y = [], PY + 150
    for k, s in enumerate(V3_BOA):
        lines = hwrap(s, HS, HMW)
        out.append((s, y, len(lines), lines))
        y += len(lines) * HLH
    return out


_LAY = v3_layout()


def rascunho_v3(c, t, a, reveals=(1, 1, 1), under=(0, 0, 0), tema_a=1.0, marks=(0, 0, 0)):
    paper(c, PX, PY, PW, PH, a, lh=HLH, top=PY + 150 - 2 - 3 * HLH)
    text(c, "TEMA 2024 · “" + TEMA24 + "”", PX + 110, PY + 64, 24, "black", BLUE, a * tema_a, align="left")
    text(c, DIDATICO, PX + 110, PY + 100, 18, "medium", AMBER, a * tema_a, align="left")
    cols = [MOV["mapa"], MOV["mapa"], MOV["tese"]]
    for k, (s, y, n, lines) in enumerate(_LAY):
        hand_para(c, s, HX, y, HS, PEN, a, HMW, HLH, reveal=reveals[k])
        if under[k] > 0:
            for j, ln in enumerate(lines):
                fr = clamp(under[k] * n - j)
                if fr > 0:
                    underline(c, HX, HX + hand_w(ln, HS), y + j * HLH + 10, cols[k], a, fr, 6)
    for k, key in enumerate(("mapa", "tese")):
        if marks[k] > 0:
            yy = _LAY[0][1] - 10 if key == "mapa" else _LAY[2][1] - 10
            icone_peca(c, key, PX + 97, yy, a * marks[k], 0.42)


def fim_pill(c, k, s, col, a):
    """pílula logo depois da última linha manuscrita da frase k"""
    _, y, n, lines = _LAY[k]
    x, yy = HX + hand_w(lines[-1], HS) + 30, y + (n - 1) * HLH - 10
    if x + text_w(s, "bold", 22) + 40 > PX + PW - 20:
        x, yy = HX, yy + HLH
    pill(c, s, x, yy, col, size=22, a=a, bounds=(0, 1920))


def lista_pills(c, a1, a2, y=PY + PH - 50):
    if a1 <= 0:
        return
    text(c, "LISTA DA CAIXA:", HX, y + 8, 22, "black", MOV["lista"], a1, align="left", tracking=1.5)
    pill(c, "① escola: aplicação irregular da lei", HX + 230, y, MOV["lista"], size=22, a=a1, bounds=(0, 1920))
    pill(c, "② mídia: pouca visibilidade", HX + 680, y, MOV["lista"], size=22, a=a2, bounds=(0, 1920))


def b_eufaco(c, t, C, B):
    sid = which(t, C, ["12", "13", "14"])
    head_seq(c, t, C, [("12", "EU FAÇO · AO VIVO", "A INTRODUÇÃO NO RASCUNHO", GREEN), ("13", "EU FAÇO · AO VIVO", "DE ONDE PARTE?", GREEN),
                       ("14", "EU FAÇO · AO VIVO", "O QUE DEFENDE? POR QUAIS CAMINHOS?", GREEN)])
    a = ep(t, C["12"], 0.5)
    r1 = wreveal(t, (C["13.s1"], C["13.s2"] - 0.5))
    r2 = wreveal(t, (C["13.s2"], C["13.m"] - 0.6))
    r3 = wreveal(t, (C["14.s3"], C["14.te"] - 0.6))
    um = ep(t, C["13.m"], 1.2)
    ut = ep(t, C["14.te"], 1.2)
    rascunho_v3(c, t, a, (r1, r2, r3), (um, um, ut), ep(t, C["12.a"], 0.4), (ep(t, C["13.m"] + 2.0, 0.4), ep(t, C["14.te"] + 2.0, 0.4)))
    if sid == "12":
        pill(c, "vou ler devagar", PX + PW - 60, PY + 64, GREEN, size=24, a=ep(t, C["12.b"], 0.4), anchor="right", bounds=(0, 1920))
    am = ep(t, C["13.m"] + 1.0, 0.4)
    fim_pill(c, 1, "MAPA: de onde parte a discussão?", MOV["mapa"], am)
    at = ep(t, C["14.te"] + 1.0, 0.4)
    fim_pill(c, 2, "ENDEREÇO: o que o autor defende?", MOV["tese"], at)
    lista_pills(c, ep(t, C["14.l1"], 0.4), ep(t, C["14.l2"], 0.4))
    av = ep(t, C["14.v"], 0.4)
    pill(c, "análise completa: episódio 5", PX + PW - 60, PY + PH - 50, BLUE, size=22, a=av, anchor="right", bounds=(0, 1920))


def b_exercicio(c, t, C, B):
    sid = which(t, C, ["17", "18"])
    head_seq(c, t, C, [("17", "NÓS FAZEMOS", "MARQUE OS 3 MOVIMENTOS", AMBER), ("18", "NÓS FAZEMOS", "CONFERINDO", GREEN)])
    if sid == "17":
        rascunho_v3(c, t, 1.0)
        pause_timer(c, t, C["17.p"] + 0.3, PX + PW - 110, PY + PH - 110)
        return
    um, ut = ep(t, C["18.a"], 1.5), ep(t, C["18.b"], 1.5)
    rascunho_v3(c, t, 1.0, under=(um, um, ut), marks=(ep(t, C["18.a"], 0.4), ep(t, C["18.b"], 0.4)))
    lista_pills(c, ep(t, C["18.c"], 0.4), ep(t, C["18.c"] + 1.6, 0.4))
    ad = ep(t, C["18.d"], 0.4)
    selo(c, PX + PW - 260, PY + PH - 70, ad, "MOVIMENTO ≠ FRASE", GREEN, -4, 28)


# ======================================================================
# exemplo × contraexemplo
# ======================================================================

def b_lado(c, t, C, B):
    head(c, t, B["start"], "LADO A LADO · TEMA 2024", "3 MOVIMENTOS × SÓ ANUNCIA", BLUE)
    for x, ok in ((160, True), (990, False)):
        card(c, x, 150, 770, 690)
    pill(c, "COM OS 3 MOVIMENTOS", 200, 200, GREEN, size=24, bounds=(0, 1920))
    para(c, " ".join(V3_BOA), 200, 270, 24, "bold", INK, 1.0, 690, 31)
    mini_etiqueta(c, 545, 735, 1.0, [1, 1, 1], 0.95, keys=K3)
    aa = ep(t, C["15.a"], 0.5)
    pill(c, "SÓ ANUNCIA", 1030, 200, RED, size=24, a=aa, bounds=(0, 1920))
    para(c, V1_GEN, 1030, 270, 28, "bold", INK, aa, 690, 37)
    text(c, DIDATICO, 1030, 520, 16, "medium", AMBER, aa, align="left")
    marks = [ep(t, C[f"15.{x}"], 0.4) for x in "bcd"]
    oks = [0 if m > 0.5 else None for m in marks]
    cx, cy, s = 1150, 690, 0.95
    mini_etiqueta(c, cx, cy, aa, oks, s, keys=K3)
    why = ["serve para qualquer tema", "quase ninguém discordaria", "só anuncia a discussão"]
    h = (30 + 3 * 34 + 10) * s
    for k, m in enumerate(marks):
        yy = cy - h / 2 + 30 * s + k * 34 * s + 17 * s
        text(c, why[k], 1320, yy + 8, 22, "black", RED, m, align="left")


# ======================================================================
# recap, erros, questão 6, ponte, CTA
# ======================================================================

FRASES = ["Mapa, endereço, lista da caixa.", "De onde parte? O que defende? Por quais caminhos?",
          "Três movimentos é método, não regra."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("16", "25"), FRASES, cols=[BLUE, MOV["tese"], GREEN])


ERROS = [("19", "Achar que a introdução não é avaliada", "nenhum descritor avalia a introdução sozinha",
          "o texto inteiro é corrigido: ali o corretor já vê ponto de vista, projeto e repertório"),
         ("20", "Achar que a introdução precisa ter EXATAMENTE 3 frases", "o modelo tem três movimentos",
          "movimento não é frase: sem número de frases, ordem ou tamanho"),
         ("21", "Começar sem tese, “só apresentando o tema”", "introduzir parece ser só apresentar o assunto",
          "a Cartilha orienta: inicie apresentando seu PONTO DE VISTA")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


Q6 = ("Um estudante afirma: “A introdução precisa ter exatamente três frases — contexto, tese e antecipação —, senão o "
      "Inep desconta pontos.” De acordo com a Cartilha do Participante, essa afirmação está")
ALT6 = [("A", "correta, pois o modelo em três frases é critério da Competência 2.", "22.A", "24.xa", "inventa um critério", RED),
        ("B", "incorreta: o modelo em três movimentos é um método útil, aparece nos comentários de redações de nota alta, mas a "
              "avaliação se faz pelas competências, sem número fixo de frases.", "22.B", None, "", GREEN),
        ("C", "correta, pois cada frase ausente reduz 40 pontos na Competência 3.", "23.C", "24.xc", "inventa “descontos”", RED),
        ("D", "incorreta, pois a introdução não deve conter tese, que só aparece na conclusão.", "23.D", "24.xd",
         "a Cartilha: inicie apresentando o ponto de vista", RED),
        ("E", "correta apenas para textos com mais de 25 linhas.", "23.E", "24.xe", "inventa uma condição", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A ESTRUTURA É OBRIGATÓRIA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["22.a"], 0.4)
    text(c, "QUESTÃO 6", 190, 230, 18, "black", GRAY, aa, align="left", tracking=2)
    para(c, Q6, 190, 290, 28, "black", INK, aa, 540, 36)
    alts_panel(c, t, C, ALT6, 790, 232, 950, 23, "24.ok", "B", 6)
    pause_timer(c, t, C["23.end"] - 1.9, 460, 740)
    an = ep(t, C["24.niv"], 0.4)
    if an > 0:
        boxed(c, 180, 640, 560, 150, GREEN, an, 0.08)
        text(c, "correção por NÍVEIS descritos,", 460, 700, 26, "black", GREEN, an)
        text(c, "não por subtração de pontos", 460, 745, 26, "black", GREEN, an)
    questao_rotulo(c, aa)


DOORS = [("26.c", "lei", "§"), ("26.c2", "fato histórico", "1888"), ("26.c3", "número", "%"), ("26.c4", "conceito", "Aa")]


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUE MAPA USAR?", BLUE)
    aa = ep(t, C["26.a"], 0.4)
    icone_peca(c, "mapa", 360, 330, aa, 1.6)
    text(c, "toda entrega começa num MAPA", 520, 345, 44, "black", BLUE, aa, align="left")
    ab = ep(t, C["26.b"], 0.4)
    text(c, "mas que mapa?", 520, 400, 34, "bold", INK2, ab, align="left")
    for k, (cue, s, g) in enumerate(DOORS):
        a, d = rise(t, C[cue])
        x = 300 + k * 340
        rrect(c, x, 480 + d, 280, 220, 18, mix("#FFFFFF", BLUE, 0.08), a, shadow=True)
        text_mid(c, g, x + 140, 560 + d, 54, "black", BLUE, a)
        text(c, s, x + 140, 660 + d, 30, "black", INK, a)
    pill(c, "Ep. 2 · os QUATRO CAMINHOS da contextualização", W / 2, 785, GREEN, size=28, a=ep(t, C["26.d"], 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "27", "Qual das 3 perguntas do leitor a sua introdução costuma esquecer?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, etiqueta=b_etiqueta, avalia=b_avalia, cartilha=b_cartilha,
              perguntas=b_perguntas, tabela=b_tabela, metodo=b_metodo, eufaco=b_eufaco, lado=b_lado, recap=b_recap,
              exercicio=b_exercicio, erros=b_erros, q6=b_q6, ponte=b_ponte, cta=b_cta)
