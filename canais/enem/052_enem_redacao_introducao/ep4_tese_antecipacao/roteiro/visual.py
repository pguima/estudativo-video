"""Visual — Redação ENEM, Introdução, Episódio 4: A tese e a antecipação dos eixos (tema claro).
Usa o desenho da série (introducao_visual.py: etiqueta de 4 faixas, rascunho com caligrafia, alternativas, recap, erros).
Novo: a CAIXA com a lista colada (liquidificador + jarra → chegou torradeira), os 4 CRITÉRIOS da tese como cartões,
a TABELA AO VIVO (4 frases do tema de 2024 × checklist ✓/✗ + veredito), o MAPA DO TEXTO (eixo A → 1º desenvolvimento,
eixo B → 2º, conclusão retoma os dois) e a promessa quebrada da Questão 5 (o item B chega trocado, alerta vermelho).
Cores: azul = definição · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep4_tese_antecipacao.mp4"
TESE_C, LISTA_C = MOV["tese"], MOV["lista"]

FRASES_TAB = [
    ("08", "A herança africana é um tema muito importante.", "f1", "NÃO É TESE", RED),
    ("09", "A herança africana deve ser valorizada.", "f2", "FRACA", AMBER),
    ("10", "A cultura africana é rica e diversa.", "f3", "NÃO P/ ESTE TEMA", RED),
    ("11", "A valorização da herança africana no Brasil é dificultada pela aplicação irregular do ensino de cultura "
           "afro-brasileira e pela pouca visibilidade dessa cultura na mídia.", "f4", "SIM", GREEN),
]
CRIT = ["clara", "contestável", "completa", "argumentável"]
# marcas (linha, coluna) → (cue, ok)
MARCAS = {(0, 1): ("08.x1", False), (0, 3): ("08.x1", False),
          (1, 0): ("09.x2", True), (1, 1): ("09.y2", False), (1, 2): ("09.z2", False),
          (2, 2): ("10.x3", False),
          (3, 1): ("11.x4", True), (3, 2): ("11.y4", True), (3, 3): ("11.z4", True), (3, 0): ("11.v4", True)}
TESE_BOA = FRASES_TAB[3][1]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "REDAÇÃO ENEM · INTRODUÇÃO", "A TESE E A ANTECIPAÇÃO", BLUE)
    card(c, *CARD_R)
    aa, d = rise(t, C["01.a"])
    text(c, "“A herança africana deve ser valorizada.”", W / 2, 300 + d, 56, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        selo(c, W / 2, 410, ab, "ISSO É TESE?", AMBER, -4, 44)
    ac = ep(t, C["01.c"], 0.4)
    check_icon(c, 420, 530, 26, ac, GREEN)
    text(c, "tem posição", 462, 540, 34, "black", GREEN, ac, align="left")
    ac2 = ep(t, C["01.c"] + 1.0, 0.4)
    check_icon(c, 860, 530, 26, ac2, AMBER, "x")
    text(c, "quase ninguém discordaria", 902, 540, 34, "black", AMBER, ac2, align="left")
    ad = ep(t, C["01.d"], 0.4)
    check_icon(c, 640, 610, 26, ad, RED, "x")
    text(c, "não diz o que IMPEDE a valorização", 682, 620, 34, "black", RED, ad, align="left")
    ae = ep(t, C["01.e"], 0.5)
    pill(c, "OPINIÃO", 760, 740, LIGHT, INK2, size=36, a=ae, anchor="center", bounds=(0, 1920))
    arrow(c, 860, 740, 1010, 740, INK2, ae, 5, 18, progress=ae)
    pill(c, "TESE", 1100, 740, TESE_C, size=36, a=ep(t, C["01.e"] + 0.8, 0.4), anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI ESCREVER UMA TESE...", GREEN)
    for k, s in enumerate(("CLARA", "CONTESTÁVEL", "COMPLETA")):
        a, d = rise(t, C["02.a"] + 0.6 * k)
        x = 420 + k * 350
        rrect(c, x - 160, 300 + d, 320, 150, 20, mix("#FFFFFF", TESE_C, 0.10), a)
        check_icon(c, x, 345 + d, 22, a, TESE_C)
        text(c, s, x, 415 + d, 34, "black", TESE_C, a)
    ab = ep(t, C["02.b"], 0.5)
    text(c, "+ 2 EIXOS", 1470, 400, 44, "black", LISTA_C, ab)
    icone_peca(c, "lista", 1470, 540, ab, 1.3)
    text(c, "que o resto do texto vai cumprir", W / 2, 720, 36, "bold", INK2, ab)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "O QUE VOCÊ JÁ SABE", PURPLE)
    rows = [("03.a", "tese", "BLOCOS da frase temática", "faltou um bloco? = TANGENCIAR", BLUE),
            ("03.b", "rua", "a PONTE (episódio 3)", "leva a referência até o recorte", GREEN),
            ("03.c", None, "CONTESTÁVEL (Linguagens)", "passa no teste da discordância: alguém poderia discordar", PURPLE)]
    for k, (cue, ic, s1, s2, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + k * 170 + d
        if ic:
            icone_peca(c, ic, 300, y, a, 1.0)
        else:
            c.drawCircle(300, y, 46, paint(mix("#FFFFFF", col, 0.14), a))
            person(c, 280, y - 22, PURPLE, a, 0.38)
            xmark(c, 326, y - 4, 12, a, RED, 6)
        text(c, s1, 380, y - 6, 40, "black", col, a, align="left")
        text(c, s2, 380, y + 44, 30, "bold", INK2, a, align="left")


# ======================================================================
# a caixa com a lista colada
# ======================================================================

def lista_colada(c, x, y, a, itens, alphas, title="CONTÉM:", w=360):
    rrect(c, x, y, w, 60 + 52 * len(itens), 10, "#FFFFFF", a, shadow=True)
    text(c, title, x + 24, y + 42, 22, "black", GRAY, a, align="left", tracking=2)
    for k, (s, col) in enumerate(itens):
        aa = a * alphas[k]
        badge_num(c, k + 1, x + 40, y + 86 + 52 * k, aa, 16, bg=col)
        text(c, s, x + 70, y + 96 + 52 * k, 30, "black", col, aa, align="left")


def b_caixa(c, t, C, B):
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        frame(c, t, B["start"], "UMA ENCOMENDA", "A LISTA COLADA NA CAIXA", LISTA_C)
        a0 = ep(t, C["04"], 0.5)
        op = ep(t, C["04.b"], 0.8)
        inner_a = ep(t, C["04.c"], 0.6)
        caixa(c, 330, 440, 420, 300, a0, open_=op, inner="TORRADEIRA" if inner_a > 0 else None, inner_a=inner_a)
        aa = ep(t, C["04.a"], 0.5)
        lista_colada(c, 960, 260, aa, [("liquidificador", INK), ("jarra", INK)], [1, 1], w=600)
        ac = ep(t, C["04.c"], 0.4)
        if ac > 0:
            strike(c, 1022, 405, 1120, 405, ac, RED, ac)
            text(c, "chegou: torradeira", 1160, 414, 30, "black", RED, ac, align="left")
        ad = ep(t, C["04.d"], 0.5)
        bubble(c, "Não foi isso que eu pedi!", 1000, 520, 560, RED, ad, size=34)
        ae = ep(t, C["04.e"], 0.4)
        if ae > 0:
            selo(c, 1280, 740, ae, "A LISTA PROMETEU", AMBER, -4, 34)
        return
    frame(c, t, C["05"], "A ETIQUETA DA INTRODUÇÃO", "TESE + LISTA DA CAIXA", TESE_C)
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    etiqueta_intro(c, 170, 175, 800, 1.0, lit=[0, 0, aa, ab], perguntas=1.0, movs=1.0, rowh=100)
    rrect(c, 1040, 220, 640, 170, 18, mix("#FFFFFF", TESE_C, 0.10), aa)
    text(c, "TESE", 1080, 275, 30, "black", TESE_C, aa, align="left", tracking=2)
    para(c, "o que você entrega: cobre o endereço INTEIRO", 1080, 325, 30, "bold", INK, aa, 570, 36)
    rrect(c, 1040, 420, 640, 170, 18, mix("#FFFFFF", LISTA_C, 0.10), ab)
    text(c, "ANTECIPAÇÃO", 1080, 475, 30, "black", LISTA_C, ab, align="left", tracking=2)
    para(c, "cada item da lista → 1 parágrafo de desenvolvimento", 1080, 525, 30, "bold", INK, ab, 570, 36)
    regra(c, "PROMESSA FEITA É PROMESSA COBRADA", 770, ep(t, C["05.c"], 0.5), 42)


# ======================================================================
# os 4 critérios
# ======================================================================

def b_criterios(c, t, C, B):
    sid = which(t, C, ["06", "07"])
    frame(c, t, B["start"], "A TESE", "O QUE É · O QUE A FAZ BOA", BLUE)
    if sid == "06":
        ad = ep(t, C["06.d"], 0.5)
        boxed(c, 260, 270, 1400, 170, BLUE, ad, 0.08)
        text(c, "TESE", 320, 340, 30, "black", BLUE, ad, align="left", tracking=2)
        text(c, "a POSIÇÃO que o texto vai defender sobre o tema", 320, 400, 40, "black", INK, ad, align="left")
        aq = ep(t, C["06.q"], 0.5)
        text(c, "o que faz uma tese ser BOA?", W / 2, 580, 50, "black", AMBER, aq)
        text(c, "4 critérios do material", W / 2, 650, 30, "bold", GRAY, aq)
        return
    expl = ["dá para resumir numa frase", "alguém poderia defender outra posição", "cobre todos os blocos da frase temática",
            "sustenta-se com fatos e raciocínio em 2 parágrafos"]
    for k, (nome, s) in enumerate(zip(CRIT, expl)):
        a, d = rise(t, C["07." + "abcd"[k]])
        x = 190 + k * 382
        rrect(c, x, 250 + d, 350, 420, 22, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250 + d, 350, 12, 6, BLUE, a)
        badge_num(c, k + 1, x + 175, 340 + d, a, 34, bg=BLUE)
        text(c, nome.upper(), x + 175, 440 + d, 34 if k != 3 else 30, "black", BLUE, a)
        para(c, s, x + 175, 510 + d, 28, "bold", INK2, a, 290, 36, align="center")


# ======================================================================
# eu faço: a tabela ao vivo
# ======================================================================

def b_eufaco(c, t, C, B):
    sid = which(t, C, ["08", "09", "10", "11"])
    n = ["08", "09", "10", "11"].index(sid)
    head(c, t, B["start"], "EU FAÇO · TEMA DE 2024", "É TESE OU NÃO É?", GREEN)
    paper(c, 140, 150, 1640, 700, 1.0, lh=56, top=200, margin=False)
    at = ep(t, C["08.tema"], 0.4)
    text(c, "“" + TEMA24 + "”", 200, 212, 28, "black", BLUE, at, align="left")
    for k, nm in enumerate(CRIT):
        text(c, nm, 1090 + k * 115, 280, 18, "black", GRAY, 1.0, align="center")
    line(c, 180, 300, 1740, 300, LIGHT, 1.0, 2)
    for i, (sc, fr, cue, ver, vcol) in enumerate(FRASES_TAB):
        if i > n:
            break
        y = 350 + i * 120
        if sid == sc:
            rev = wreveal(t, phrase_span(sc, fr, C[f"{sc}.{cue}"], C[f"{sc}.{cue}"] + 3.0))
        else:
            rev = 1.0
        hand_para(c, "“" + fr + "”", 190, y + 8, 25 if i == 3 else 30, PEN, 1.0, 840, 34, rev)
        for j in range(4):
            m = MARCAS.get((i, j))
            if m:
                cx = 1090 + j * 115
                am = ep(t, C[m[0]] + (0.3 if (i, j) == (3, 0) else 0), 0.3)
                check_icon(c, cx, y + 10, 22, am, GREEN if m[1] else RED, "check" if m[1] else "x")
        av = ep(t, C[f"{sc}.v{i + 1}"], 0.4)
        pill(c, ver, 1720, y + 10, vcol, size=20, a=av, anchor="right", bounds=(0, 1920))
        if i < 3:
            line(c, 180, y + 70, 1740, y + 70, LINE, 1.0, 1.5)


# ======================================================================
# primeira pessoa
# ======================================================================

def b_pessoa(c, t, C, B):
    frame(c, t, B["start"], "TESE EM PRIMEIRA PESSOA?", "PODE, MAS...", BLUE)
    aq = ep(t, C["12.q"], 0.5)
    bubble(c, "“Eu acredito que...”", 230, 230, 460, INK2, aq, size=36)
    aa = ep(t, C["12.a"], 0.4)
    if aa > 0:
        selo(c, 470, 430, aa, "CARTILHA: NÃO PROÍBE", PURPLE, -4, 30)
    ab = ep(t, C["12.b"], 0.5)
    boxed(c, 220, 540, 560, 150, BLUE, ab, 0.08)
    text(c, "REGISTRO IMPESSOAL", 500, 600, 28, "black", BLUE, ab, tracking=1)
    text(c, "o mais usado: não fala de si", 500, 650, 28, "bold", INK2, ab)
    opts = [("12.c", "“É preciso reconhecer que…”"), ("12.c", "“Evidencia-se que…”"), ("12.d", "afirmação direta")]
    for k, (cue, s) in enumerate(opts):
        a, d = rise(t, C[cue] + (0.9 * k if k < 2 else 0))
        y = 290 + k * 140 + d
        arrow(c, 840, y, 940, y, GREEN, a, 4, 16, progress=a)
        rrect(c, 960, y - 48, 660, 96, 18, mix("#FFFFFF", GREEN, 0.10), a)
        text_mid(c, s, 1290, y, 34, "black", GREEN, a)
    pill(c, "a série Impessoalidade aprofunda", W / 2, 780, LIGHT, INK2, size=24, a=ep(t, C["12.e"], 0.4), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# antecipar · mapa do texto · três formas · promessa cobrada
# ======================================================================

def b_antecipar(c, t, C, B):
    frame(c, t, B["start"], "ANTECIPAR", "A LISTA DA CAIXA", LISTA_C)
    aa = ep(t, C["13.a"], 0.5)
    icone_peca(c, "lista", 270, 300, aa, 1.2)
    para(c, "ANTECIPAR = anunciar, de forma breve, os EIXOS de cada parágrafo de desenvolvimento", 360, 285, 36, "black",
         INK, aa, 1240, 44)
    ab = ep(t, C["13.b"], 0.4)
    pill(c, "EIXO = cada caminho do seu argumento", 360, 400, BLUE, size=26, a=ab, bounds=(0, 1920))
    ac = ep(t, C["13.c"], 0.5)
    cartilha(c, 220, 470, ac, 0, 0.78)
    quotes = [("13.d", "“...antecipando, assim, os dois eixos argumentativos que serão desenvolvidos”"),
              ("13.e", "“...anunciando, portanto, o seu projeto de texto”")]
    for k, (cue, s) in enumerate(quotes):
        a, d = rise(t, C[cue])
        y = 490 + k * 150 + d
        rrect(c, 520, y, 1120, 120, 18, mix("#FFFFFF", PURPLE, 0.09), a)
        para(c, s, 560, y + 50, 30, "black", PURPLE, a, 1050, 38)
    text(c, "Cartilha do Participante, comentários de redações de nota alta", 520, 800, 18, "medium", GRAY, ac, align="left")


def _bloco(c, x, y, w, h, titulo, col, a, linhas=3, tag=None, tag_col=None, ta=1.0):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 16, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, 10, h, 5, col, a)
    text(c, titulo, x + 30, y + 42, 24, "black", col, a, align="left", tracking=1)
    for k in range(linhas):
        line(c, x + 30, y + 72 + k * 24, x + w - 30 - (k % 2) * 50, y + 72 + k * 24, LIGHT, a, 7)
    if tag:
        pill(c, tag, x + w - 20, y + 32, tag_col or col, size=20, a=a * ta, anchor="right", bounds=(0, 1920))


def b_mapa(c, t, C, B):
    frame(c, t, B["start"], "A INTRODUÇÃO COMO MAPA", "O PROJETO DE TEXTO", LISTA_C)
    aa = ep(t, C["14.a"], 0.5)
    _bloco(c, 200, 330, 400, 260, "INTRODUÇÃO", TESE_C, aa, 2)
    ab = ep(t, C["14.b"], 0.4)
    pill(c, "eixo A", 240, 490, BLUE, size=26, a=ab, bounds=(0, 1920))
    pill(c, "eixo B", 400, 490, AMBER, size=26, a=ep(t, C["14.b"] + 0.8, 0.4), bounds=(0, 1920))
    text(c, "na tese", 240, 560, 22, "bold", GRAY, ab, align="left")
    acd = [("14.c", "1º DESENVOLVIMENTO", "eixo A", BLUE, 220), ("14.d", "2º DESENVOLVIMENTO", "eixo B", AMBER, 520)]
    for cue, tt, tag, col, y in acd:
        a = ep(t, C[cue], 0.5)
        arrow(c, 610, 460, 790, y + 90, col, a, 5, 18, progress=a)
        _bloco(c, 800, y, 470, 180, tt, col, a, 3, tag, col)
    ae = ep(t, C["14.e"], 0.5)
    for y in (310, 610):
        arrow(c, 1280, y, 1390, 460, GREEN, ae, 5, 18, progress=ae)
    _bloco(c, 1400, 370, 330, 200, "CONCLUSÃO", GREEN, ae, 2)
    text(c, "retoma A e B na proposta", 1565, 600, 22, "bold", GREEN, ae)
    af = ep(t, C["14.f"], 0.5)
    pill(c, "PROJETO DE TEXTO · Competência 3", W / 2, 800, PURPLE, size=28, a=af, anchor="center", bounds=(0, 1920))


def b_formas(c, t, C, B):
    frame(c, t, B["start"], "3 FORMAS DE ANTECIPAR", "TEMA DE 2024", LISTA_C)
    rows = [("15.a", "dois substantivos coordenados", "“…dificultada pela aplicação irregular da lei e pela pouca visibilidade na mídia.”"),
            ("15.b", "causa e consequência", "“…pois o apagamento escolar alimenta preconceitos que, por sua vez, afastam os jovens dessas tradições.”"),
            ("15.c", "dois agentes", "“…problema que envolve tanto a escola quanto os meios de comunicação.”")]
    for k, (cue, nome, ex) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 225 + k * 200 + d
        badge_num(c, k + 1, 240, y + 30, a, 30, bg=LISTA_C)
        text(c, nome.upper(), 300, y + 40, 30, "black", LISTA_C, a, align="left", tracking=1)
        para(c, ex, 300, y + 100, 32, "bold", INK, a, 1340, 40)
    text(c, "Exemplos do material de estudo (seção 06)", CARD_R[0] + 40, 815, 18, "medium", GRAY, ep(t, C["15.a"], 0.4),
         align="left")


def b_cobrada(c, t, C, B):
    frame(c, t, B["start"], "PROMESSA FEITA É PROMESSA COBRADA", "COERÊNCIA (C3)", RED)
    aa = ep(t, C["16.b"], 0.5)
    lista_colada(c, 220, 230, aa, [("eixo A", BLUE), ("eixo B", AMBER)], [1, 1], "A INTRODUÇÃO PROMETE:")
    arrow(c, 600, 330, 760, 330, INK2, aa, 4, 16, progress=aa)
    _bloco(c, 780, 230, 400, 150, "1º DESENV.", BLUE, aa, 2, "eixo A ✓", GREEN)
    ab = ep(t, C["16.b"] + 1.5, 0.5)
    shake = 6 * math.sin(t * 40) * (1 - prog(t, C["16.c"], 0.8)) if t > C["16.c"] else 0
    c.save(); c.translate(shake, 0)
    _bloco(c, 1220, 230, 440, 150, "2º DESENV.", RED, ab, 2, "3º assunto ✗", RED)
    c.restore()
    ac = ep(t, C["16.c"], 0.4)
    if ac > 0:
        selo(c, 1440, 450, ac, "QUEBRA!", RED, 5, 36)
    ad = ep(t, C["16.d"], 0.5)
    boxed(c, 220, 520, 960, 110, BLUE, ad, 0.08)
    text_mid(c, "COERÊNCIA = o texto fazer sentido como um todo", 700, 575, 32, "black", BLUE, ad)
    ae = ep(t, C["16.e"], 0.5)
    rrect(c, 220, 670, 1460, 120, 18, mix("#FFFFFF", GREEN, 0.10), ae)
    badge_num(c, 1, 280, 730, ae, 24, bg=GREEN)
    text(c, "planeje os parágrafos no rascunho", 320, 740, 32, "black", GREEN, ae, align="left")
    arrow(c, 900, 730, 990, 730, GREEN, ae, 4, 16, progress=ae)
    badge_num(c, 2, 1030, 730, ae, 24, bg=GREEN)
    text(c, "DEPOIS escreva a antecipação", 1070, 740, 32, "black", GREEN, ae, align="left")


# ======================================================================
# a tese do estigma (fio das próximas séries)
# ======================================================================

def b_estigma(c, t, C, B):
    head(c, t, B["start"], "UMA TESE PARA GUARDAR · ENEM 2020", "O FIO DAS PRÓXIMAS SÉRIES", PURPLE)
    paper(c, 160, 150, 1600, 700, 1.0, lh=56, top=214)
    aa = ep(t, C["17.a"], 0.4)
    text(c, "“" + TEMA20 + "”", 260, 225, 30, "black", BLUE, aa, align="left")
    pill(c, "ESTIGMA = uma marca negativa que a sociedade cola numa pessoa", 260, 290, BLUE, size=22,
         a=ep(t, C["17.s"], 0.4), bounds=(0, 1920))
    ab = ep(t, C["17.b"], 0.3)
    rev = wreveal(t, phrase_span("17", TESE20, C["17.b"], C["17.c"]))
    hand_para(c, TESE20, 260, 400, 34, PEN, ab, 1400, 56, rev)
    ac = ep(t, C["17.c"], 0.4)
    pill(c, "EIXO A · desinformação", 260, 600, BLUE, size=28, a=ac, bounds=(0, 1920))
    ad = ep(t, C["17.d"], 0.4)
    pill(c, "EIXO B · representações midiáticas", 700, 600, AMBER, size=28, a=ad, bounds=(0, 1920))
    ae = ep(t, C["17.e"], 0.4)
    if ae > 0:
        selo(c, 470, 730, ae, "GUARDE ESTA TESE", PURPLE, -5, 34)
        text(c, "Desenvolvimento e Conclusão: vamos terminar esta redação", 820, 742, 28, "bold", INK2, ae, align="left")
    text(c, "Tese do material de estudo (elaborada para fins didáticos)", 260, 830, 16, "medium", GRAY, ab, align="left")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    sid = which(t, C, ["18", "19"])
    head(c, t, B["start"], "NÓS FAZEMOS", "DA TESE FRACA À TESE COM 2 EIXOS", GREEN)
    paper(c, 160, 150, 1600, 700, 1.0, lh=56, top=214)
    aa = ep(t, C["18.a"], 0.4)
    text(c, "TESE FRACA", 260, 250, 18, "black", AMBER, aa, align="left", tracking=2)
    hand(c, "A herança africana deve ser valorizada.", 260, 310, 38, PEN, aa)
    ab = ep(t, C["18.b"], 0.4)
    if sid == "18":
        hand(c, "+ eixo 1: ______________", 260, 430, 34, LISTA_C, ab)
        hand(c, "+ eixo 2: ______________", 260, 510, 34, LISTA_C, ab)
        text(c, "o que IMPEDE essa valorização?", 1000, 470, 32, "black", AMBER, ab, align="left")
        pause_timer(c, t, C["18.p"] + 0.3, 1500, 680, dur=2.4)
        return
    strike(c, 256, 298, 260 + hand_w("A herança africana deve ser valorizada.", 38), 298, ep(t, C["19.a"], 0.4), AMBER)
    text(c, "UMA RESPOSTA POSSÍVEL", 260, 410, 18, "black", GREEN, ep(t, C["19.a"], 0.4), align="left", tracking=2)
    rev = wreveal(t, phrase_span("19", TESE_BOA, C["19.b"], C["19.c"]))
    hand_para(c, TESE_BOA, 260, 470, 34, PEN, ep(t, C["19.b"], 0.3), 1400, 56, rev)
    ac = ep(t, C["19.c"], 0.4)
    for k, s in enumerate(("2 obstáculos nomeados", "todos os blocos")):
        check_icon(c, 290 + k * 520, 700, 22, ac, GREEN)
        text(c, s, 325 + k * 520, 710, 30, "black", GREEN, ac, align="left")


# ======================================================================
# recapitulação, erros
# ======================================================================

FRASES = ["Tese: clara, contestável, completa, argumentável.", "Antecipar é colar a lista na caixa.",
          "Promessa feita é promessa cobrada."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("20", "30"), FRASES, [TESE_C, LISTA_C, RED])


ERROS = [("21", "A tese que só declara importância", "usa as palavras do tema e soa séria",
          "importância não é posição: diga o que você DEFENDE"),
         ("22", "A tese que esquece um bloco da frase temática", "fala do assunto direitinho",
          "sem um bloco, tangencia desde a introdução: CONFIRA BLOCO A BLOCO"),
         ("23", "Anunciar um eixo que o texto não desenvolve", "a introdução ficou bonita e completa",
          "a promessa é cobrada: PLANEJE antes de anunciar")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# questão inédita (2017) e Questão 5
# ======================================================================

ALTI = [("A", "A educação de surdos é um assunto que merece a atenção de todos.", "24.A", "26.xa", "só declara importância", RED),
        ("B", "No Brasil, a formação educacional de surdos esbarra na escassez de escolas bilíngues e na falta de professores fluentes em Libras.", "24.B", None, "", GREEN),
        ("C", "Até quando os surdos vão esperar por uma escola de qualidade?", "25.C", "26.xc", "pergunta retórica não substitui a tese", RED),
        ("D", "Em vários países, pessoas surdas enfrentam dificuldades na escola.", "25.D", "26.xd", "sai do Brasil: assunto amplo", RED),
        ("E", "Este texto vai discutir os desafios para a formação educacional de surdos no Brasil.", "25.E", "26.xe", "anuncia o tema, não defende", RED)]


def b_qi(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ENEM 2017", "TESE COM ANTECIPAÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["24.a"], 0.4)
    text(c, "Questão elaborada para fins didáticos.", 190, 230, 18, "black", AMBER, aa, align="left")
    text(c, "TEMA", 190, 290, 16, "black", GRAY, aa, align="left", tracking=2)
    h = para(c, "“" + TEMA17 + "”", 190, 330, 28, "black", BLUE, aa, 540, 34)
    para(c, "A frase que apresenta uma tese e antecipa os dois eixos do desenvolvimento é:", 190, 330 + h + 30, 26, "bold",
         INK, aa, 540, 32)
    alts_panel(c, t, C, ALTI, 790, 240, 950, 25, "26.ok", "B", 8)
    pause_timer(c, t, C["25.p"] + 0.3, 460, 760, dur=2.4)
    ao = ep(t, C["26.ok"] + 1.5, 0.4)
    pill(c, "eixo A: escolas bilíngues", 190, 700, BLUE, size=22, a=ao, bounds=(0, 1920))
    pill(c, "eixo B: professores fluentes em Libras", 190, 760, AMBER, size=22, a=ep(t, C["26.ok"] + 2.3, 0.4),
         bounds=(0, 1920))


ALT5 = [("A", "a Competência 1, pois houve mudança de registro.", "28.A", "29.xa", "o enunciado não descreve isso", RED),
        ("B", "a Competência 4, pois faltam conectivos entre os parágrafos.", "28.B", "29.xb", "o enunciado não descreve isso", RED),
        ("C", "a Competência 5, que avalia apenas a introdução.", "28.C", "29.xc", "a C5 avalia a proposta de intervenção", RED),
        ("D", "a Competência 3, pois o projeto de texto anunciado na introdução não é cumprido pelo desenvolvimento.", "28.D", None, "", GREEN),
        ("E", "nenhuma competência, já que a introdução não é avaliada pelo Inep.", "28.E", "29.xe", "o texto inteiro é avaliado", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · PROMESSA NÃO CUMPRIDA", "QUE COMPETÊNCIA SOFRE?", BLUE)
    card(c, *CARD_R)
    x0 = 180
    aa = ep(t, C["27.a"], 0.4)
    text(c, "A INTRODUÇÃO PROMETE", x0, 230, 18, "black", GRAY, aa, align="left", tracking=2)
    for k, s in enumerate(("falta de salas fora das capitais", "preço dos ingressos")):
        a = ep(t, C["27.a"] + 1.2 * k, 0.4)
        badge_num(c, "AB"[k], x0 + 20, 270 + k * 50, a, 16, bg=[BLUE, AMBER][k])
        text(c, s, x0 + 50, 280 + k * 50, 26, "black", INK, a, align="left")
    text(c, "O DESENVOLVIMENTO ENTREGA", x0, 400, 18, "black", GRAY, ep(t, C["27.b"], 0.4), align="left", tracking=2)
    ab = ep(t, C["27.b"], 0.4)
    check_icon(c, x0 + 20, 440, 16, ab, GREEN)
    text(c, "1º: falta de salas", x0 + 50, 450, 26, "black", INK, ab, align="left")
    acc = ep(t, C["27.c"], 0.4)
    check_icon(c, x0 + 20, 490, 16, acc, RED, "x")
    text(c, "2º: qualidade dos roteiros", x0 + 50, 500, 26, "black", RED, acc, align="left")
    if acc > 0:
        selo(c, x0 + 270, 580, ep(t, C["27.c"] + 0.8, 0.4), "ITEM TROCADO!", RED, -4, 28)
    text(c, "Esse descompasso afeta principalmente:", x0, 680, 24, "bold", INK, ep(t, C["27.d"], 0.4), align="left")
    alts_panel(c, t, C, ALT5, 790, 240, 950, 25, "29.ok", "D", 8)
    pause_timer(c, t, C["28.p"] + 0.3, 600, 740, dur=2.4)
    at = ep(t, C["29.tr"], 0.4)
    pill(c, "a torradeira no lugar da jarra", x0, 760, AMBER, size=22, a=at,
         bounds=(0, 1920))
    questao_rotulo(c, ep(t, C["27.a"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "FRACAS × BOAS, LADO A LADO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    for k, key in enumerate(("mapa", "rua", "tese", "lista")):
        a = ep(t, C["31.a"] + 0.6 * k, 0.4)
        icone_peca(c, key, 560 + k * 270, 300, a, 1.1)
        check_icon(c, 600 + k * 270, 340, 16, a, GREEN)
    text(c, "todas as peças da etiqueta", W / 2, 420, 30, "bold", INK2, aa)
    ab = ep(t, C["31.b"], 0.5)
    for k, (nm, oks) in enumerate((("VERSÃO 1", [0, 0, 0, 0]), ("VERSÃO 2", [0, 0, 0, 0]), ("VERSÃO 3", [1, 1, 1, 1]))):
        a = ep(t, C["31.b"] + 0.5 * k, 0.4)
        mini_etiqueta(c, 560 + k * 400, 600, a, oks if k == 2 else [None] * 4, 0.9)
        text(c, nm, 560 + k * 400, 720, 24, "black", INK2, a, tracking=2)
    pill(c, "PIOR  →  MELHOR", W / 2, 780, INK2, size=24, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["31.c"], 0.4)
    if ac > 0:
        selo(c, 1560, 470, ac, "+ ARMADILHAS", AMBER, 6, 30)


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "32", "Como ficou a sua tese com dois eixos para a herança africana?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, caixa=b_caixa, criterios=b_criterios, eufaco=b_eufaco,
              pessoa=b_pessoa, antecipar=b_antecipar, mapa=b_mapa, formas=b_formas, cobrada=b_cobrada, estigma=b_estigma,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, qi=b_qi, q5=b_q5, ponte=b_ponte, cta=b_cta)
