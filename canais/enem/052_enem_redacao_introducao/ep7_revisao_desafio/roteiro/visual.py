"""Visual — Redação ENEM, Introdução, Episódio 7: Revisão geral, pegadinhas e desafio prático (tema claro).
Desenho da série em introducao_visual.py (etiqueta de 4 faixas, ícones das peças, rascunho com caligrafia, alternativas).
Novo: ÍNDICE com os 6 ícones dos episódios (etiqueta · quatro portas · rua · lista da caixa · três colunas · caderno),
V ou F com selo PEGADINHA, 5 questões inéditas, CRONÔMETRO no desafio e checklist de domínio agrupado por episódio.
Cores: azul = definição/tema · verde = método · âmbar = armadilha · vermelho = erro/penalidade · roxo = regra oficial.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from introducao_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_introducao_ep7_revisao_desafio.mp4"
TEMA_DID = "Tema elaborado para fins didáticos."
NUC, DEL = BLUE, GREEN


# ======================================================================
# os 6 ícones dos episódios (índice visual)
# ======================================================================

def ic_etiqueta(c, cx, cy, s, a, col):
    rrect(c, cx - 32 * s, cy - 22 * s, 64 * s, 44 * s, 6 * s, "#FFFFFF", a, stroke=3 * s, stroke_color=col)
    for k in range(6):
        c.drawRect(skia.Rect.MakeXYWH(cx + (6 + k * 4) * s, cy - 14 * s, 2 * s, 12 * s), paint(col, a))
    for k in range(3):
        line(c, cx - 24 * s, cy + (2 + k * 7) * s - 6 * s, cx + (2 if k else -4) * s, cy + (2 + k * 7) * s - 6 * s, col, a, 3 * s)


def ic_portas(c, cx, cy, s, a, col):
    for k in range(4):
        x = cx - 34 * s + k * 18 * s
        rrect(c, x, cy - 22 * s, 14 * s, 44 * s, 3 * s, mix("#FFFFFF", col, 0.30), a, stroke=2.5 * s, stroke_color=col)
        c.drawCircle(x + 10 * s, cy + 2 * s, 1.8 * s, paint(col, a))


def ic_colunas(c, cx, cy, s, a, col):
    for k, cc in enumerate((RED, AMBER, GREEN)):
        x = cx - 32 * s + k * 22 * s
        rrect(c, x, cy - 26 * s, 18 * s, 52 * s, 3 * s, "#FFFFFF", a, stroke=2.5 * s, stroke_color=col)
        for j in range(3):
            line(c, x + 4 * s, cy - 14 * s + j * 9 * s, x + 14 * s, cy - 14 * s + j * 9 * s, LIGHT, a, 2 * s)
        c.drawCircle(x + 9 * s, cy + 16 * s, 4 * s, paint(cc if col != LIGHT else LIGHT, a))


def ic_caderno(c, cx, cy, s, a, col):
    rrect(c, cx - 24 * s, cy - 28 * s, 50 * s, 58 * s, 5 * s, PAPER, a, stroke=3 * s, stroke_color=col)
    for k in range(5):
        c.drawCircle(cx - 24 * s, cy - 20 * s + k * 10 * s, 3.5 * s, paint(col, a, stroke=2 * s))
    for k in range(3):
        line(c, cx - 12 * s, cy - 10 * s + k * 12 * s, cx + 18 * s, cy - 10 * s + k * 12 * s, LIGHT, a, 2 * s)
    line(c, cx - 10 * s, cy + 18 * s, cx + 16 * s, cy - 2 * s, PEN, a, 3 * s)


def _ic_rua(c, cx, cy, s, a, col):
    ICON_PECA["rua"](c, cx, cy, s, a, col)


def _ic_lista(c, cx, cy, s, a, col):
    ICON_PECA["lista"](c, cx, cy, s, a, col)


ICONES = [(ic_etiqueta, "etiqueta", BLUE), (ic_portas, "4 portas", BLUE), (_ic_rua, "ponte", GREEN), (_ic_lista, "lista", MOV["lista"]),
          (ic_colunas, "fraca × boa", AMBER), (ic_caderno, "oficina", PURPLE)]


def icone(c, k, cx, cy, a, s=1.0, lit=True, label=True):
    if a <= 0:
        return
    fn, nm, col = ICONES[k]
    col_ = col if lit else LIGHT
    c.drawCircle(cx, cy, 46 * s, paint(mix("#FFFFFF", col_, 0.14), a))
    fn(c, cx, cy, s, a, col_)
    if label:
        text(c, f"EP. {k + 1}", cx, cy + 74 * s, 18 * s, "black", col_ if lit else GRAY, a, tracking=2)


def ic_postal(c, cx, cy, s, a, col):
    rrect(c, cx - 34 * s, cy - 22 * s, 68 * s, 44 * s, 4 * s, "#FFFFFF", a, stroke=3 * s, stroke_color=col)
    rrect(c, cx - 28 * s, cy - 16 * s, 30 * s, 32 * s, 3 * s, mix("#FFFFFF", col, 0.35), a)
    c.drawCircle(cx - 13 * s, cy - 4 * s, 6 * s, paint(col, a))
    for k in range(3):
        line(c, cx + 8 * s, cy - 8 * s + k * 9 * s, cx + 28 * s, cy - 8 * s + k * 9 * s, col, a, 2 * s)


def cronometro(c, cx, cy, r, a, frac=1.0, label="10:00"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 12, paint(AMBER, a * 0.16))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * clamp(frac), False,
              paint(AMBER, a, stroke=r * 0.18, cap_round=True))
    rrect(c, cx - 14, cy - r - 30, 28, 22, 6, INK2, a)
    text_mid(c, label, cx, cy, r * 0.42, "black", INK, a)


# ======================================================================
# abertura e mapa da série
# ======================================================================

def b_hook(c, t, C, B):
    sid = which(t, C, ["01", "02"])
    head_seq(c, t, C, [("01", "REDAÇÃO ENEM · INTRODUÇÃO", "REVISÃO GERAL", PURPLE),
                       ("02", "REDAÇÃO ENEM · INTRODUÇÃO", "NESTA REVISÃO", PURPLE)])
    card(c, *CARD_R)
    if sid == "01":
        aa = ep(t, C["01.a"], 0.5)
        show = [ep(t, C["01.a"] + 0.4 * k, 0.4) for k in range(4)]
        ab = ep(t, C["01.b"], 0.5)
        ok = [ep(t, C["01.b"] + 0.8 + 0.4 * k, 0.3) for k in range(4)]
        etiqueta_intro(c, 220, 200, 860, aa, show=show, ok=ok, movs=1.0)
        selo(c, 1390, 330, aa, "1º PARÁGRAFO = PROMESSA", BLUE, -4, 34)
        text(c, "o corretor", 1390, 520, 40, "bold", INK2, ab)
        text(c, "COBRA", 1390, 620, 96, "black", RED, ab)
        return
    rows = [("02.b", "as 3 ideias que mais rendem", GREEN), ("02.c", "V ou F: 10 pegadinhas", AMBER),
            ("02.d", "5 questões inéditas", BLUE), ("02.e", "desafio: 3 temas reais", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 260 + k * 92 + d
        badge_num(c, k + 1, 300, y - 14, a, 28, bg=col)
        text(c, s, 350, y, 40, "black", INK, a, align="left")
    for k in range(6):
        icone(c, k, 1180 + (k % 3) * 160, 300 + (k // 3) * 190, ep(t, C["02.a"] + 0.15 * k, 0.4), 1.0)
    af = ep(t, C["02.f"], 0.4)
    pill(c, "pegue papel e caneta", W / 2, 690, GREEN, size=30, a=af, anchor="center", bounds=(0, 1920))


MAPA = [("03.a", "ic", 0, "introdução", "etiqueta completa"),
        ("03.b", "ic", 1, "contextualização", "mapa · 4 portas"),
        ("03.c", "ic", 2, "ponte", "rua de acesso"),
        ("03.d", "postal", None, "repertório de bolso", "cartão-postal genérico"),
        ("03.e", "casa", None, "tese", "a entrega no endereço inteiro"),
        ("03.f", "ic", 3, "antecipação", "lista da caixa"),
        ("03.g", "ic", 5, "oficina", "arrume a caixa antes da etiqueta")]


def b_mapa(c, t, C, B):
    frame(c, t, B["start"], "AS IMAGENS DA SÉRIE", "O MAPA DA REVISÃO", PURPLE)
    for k, (cue, kind, ic, s1, s2) in enumerate(MAPA):
        a, d = rise(t, C[cue])
        row = k // 4
        ncol = 4 if row == 0 else 3
        x = (210 if row == 0 else 400) + (k % 4 if row == 0 else k - 4) * 380
        y = 190 + row * 330 + d
        rrect(c, x, y, 350, 300, 20, "#FFFFFF", a, shadow=True)
        if kind == "ic":
            icone(c, ic, x + 175, y + 85, a, 0.85, label=False)
            col = ICONES[ic][2]
        elif kind == "postal":
            c.drawCircle(x + 175, y + 85, 46 * 0.85, paint(mix("#FFFFFF", AMBER, 0.14), a))
            ic_postal(c, x + 175, y + 85, 0.85, a, AMBER); col = AMBER
        else:
            icone_peca(c, "tese", x + 175, y + 85, a, 0.85); col = MOV["tese"]
        text(c, s1, x + 175, y + 180, 28, "black", INK, a)
        para(c, s2, x + 175, y + 225, 25, "black", col, a, 320, 30, align="center")
    af = ep(t, C["03.f"] + 2.0, 0.4)
    pill(c, "promessa feita é promessa cobrada", W / 2, 858, MOV["lista"], size=24, a=af, anchor="center", bounds=(0, 1920))


IDEIAS = [("05.a", "rua", "contextualização só ajuda com PONTE", "uma ponte explícita para o recorte do tema"),
          ("05.b", "tese", "tese é POSIÇÃO", "não a repetição da frase temática"),
          ("05.c", "lista", "anuncie DOIS EIXOS", "torna o projeto de texto visível")]


def b_ideias(c, t, C, B):
    head_seq(c, t, C, [("04", "TESTE DE MEMÓRIA", "QUAIS SÃO AS 3 IDEIAS?", PURPLE), ("05", "O QUE RENDE MAIS", "AS 3 IDEIAS", GREEN)])
    card(c, *CARD_R)
    if t < C["05"] - 0.05:
        a = ep(t, C["04.a"], 0.5)
        for k in range(3):
            badge_num(c, k + 1, 500 + k * 460, 420, a, 70, bg=LIGHT)
            text_mid(c, "?", 500 + k * 460, 560, 80, "black", GRAY, a)
        pause_timer(c, t, C["04.p"] + 0.4, W / 2, 720)
        return
    for k, (cue, key, s1, s2) in enumerate(IDEIAS):
        a, d = rise(t, C[cue])
        y = 290 + k * 190 + d
        badge_num(c, k + 1, 230, y, a, 30, bg=MOV[key])
        icone_peca(c, key, 340, y, a, 1.0)
        text(c, s1, 430, y - 2, 42, "black", INK, a, align="left")
        text(c, s2, 430, y + 50, 28, "bold", MOV[key], a, align="left")


# ======================================================================
# verdadeiro ou falso
# ======================================================================

VF = [("06", "Abrir com “desde os primórdios da humanidade” é um bom jeito de contextualizar qualquer tema.", False,
       "soa elegante e serve para tudo", "contextualize o recorte, não “a humanidade”", 4),
      ("07", "Se você tira a referência e nada muda, ela não estava trabalhando.", True,
       "a citação deixa o texto bonito", "faça a ponte entre a referência e o tema", 2),
      ("08", "Uma frase de pensador decorada serve para abrir qualquer redação.", False,
       "um nome famoso parece dar peso", "escolha uma referência ligada ao recorte", 2),
      ("09", "Um número sem fonte (“pesquisas mostram que 90%…”) deixa a introdução mais forte.", False,
       "o número parece preciso", "use só o que você pode verificar: repertório precisa ser legitimado", 1),
      ("10", "“É um tema muito importante” NÃO é tese.", True,
       "a frase usa as palavras da prova", "tome posição contestável", 3),
      ("11", "Uma tese que deixa um bloco da frase temática de fora já compromete o texto na introdução.", True,
       "falta só um pedacinho", "o tangenciamento começa na introdução: confira cada bloco", 3),
      ("12", "Anunciar os eixos na introdução é desperdiçar linhas.", False,
       "os eixos aparecem de novo no desenvolvimento", "antecipar os dois argumentos torna o projeto visível (C3)", 3),
      ("13", "A antecipação deve ser escrita DEPOIS de planejar os parágrafos de desenvolvimento.", True,
       "a introdução é o 1º parágrafo lido", "promessa sem entrega rompe a coerência", 5),
      ("14", "Quanto mais exemplos e explicações na introdução, melhor.", False,
       "parece mostrar que você sabe muito", "introdução longa rouba linhas: exemplos ficam no desenvolvimento", 4),
      ("15", "A introdução precisa ter exatamente três frases, senão perde pontos.", False,
       "o modelo aparece nas redações nota alta", "é método: o Inep avalia por competências", 0)]
VF_EXTRA = {"08": "A Cartilha alerta para o uso genérico desde 2025.",
            "15": "conta: proposição, projeto e repertório pertinente"}


def b_vf(c, t, C, B):
    ids = [v[0] for v in VF]
    sid = which(t, C, ids)
    n = ids.index(sid)
    _, frase, ok, engana, regra_, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 10", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    for k in range(10):
        badge_num(c, k + 1, 560 + k * 80, 205, 1, 20, bg=AMBER if k == n else (INK2 if k < n else LIGHT))
    q = lambda x: C[f"{sid}.{x}"]
    aq, d = rise(t, q("q"))
    icone(c, ic, 290, 360 + d, aq, 0.9, label=False)
    para(c, "“" + frase.replace("“", "‘").replace("”", "’") + "”", 380, 340 + d, 44, "black", INK, aq, 1180, 54)
    pause_timer(c, t, q("p") + 0.3, 1540, 560)
    ar = ep(t, q("r"), 0.4)
    if ar > 0:
        selo(c, 520, 560, ar, "VERDADEIRO" if ok else "FALSO", GREEN if ok else RED, -6, 56)
    aw = ep(t, q("w"), 0.4)
    if aw > 0:
        selo(c, 950, 560, aw, "PEGADINHA", AMBER, 4, 30)
        para(c, engana, 1100, 548, 26, "bold", INK2, aw, 520, 30)
    ak = ep(t, q("k"), 0.4)
    if ak > 0:
        rrect(c, 260, 680, 1400, 120, 18, mix("#FFFFFF", GREEN, 0.10), ak)
        check_icon(c, 310, 740 if sid not in VF_EXTRA else 722, 26, ak, GREEN)
        if sid in VF_EXTRA:
            text_mid(c, regra_, 990, 722, 32, "black", GREEN, ak)
            text_mid(c, VF_EXTRA[sid], 990, 768, 24, "bold", PURPLE if sid == "08" else INK2, ep(t, q("k") + 1.8, 0.4))
        else:
            text_mid(c, regra_, 990, 740, 32, "black", GREEN, ak)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

def questao(c, t, C, n, sub, lembra, ic, tema, enun, alts, okc, okL, trecho=None, extra=None, size=22, lsize=22):
    head(c, t, C[lembra[0]], f"QUESTÃO {n} · INÉDITA", sub, BLUE)
    card(c, *CARD_R)
    cue_r, s_r = lembra[1], lembra[2]
    ar = ep(t, C[cue_r], 0.4)
    icone(c, ic, 230, 250, ar, 0.7, label=False)
    pill(c, "LEMBRANDO", 300, 222, PURPLE, size=18, a=ar, bounds=(0, 1920))
    para(c, s_r, 300, 275, 22, "black", PURPLE, ar, 420, 26)
    aa = ep(t, C[enun[0]], 0.4)
    y = 365
    text(c, "TEMA", 190, y, 16, "black", GRAY, aa, align="left", tracking=2)
    h = para(c, "“" + tema + "”", 190, y + 38, 25, "black", BLUE, aa, 540, 31)
    text(c, TEMA_DID, 190, y + 38 + h + 2, 15, "medium", AMBER, aa, align="left")
    y = y + 38 + h + 44
    if trecho:
        at = ep(t, C[trecho[0]], 0.4)
        lines = wrap(trecho[1], "bold", lsize, 500)
        hh = len(lines) * (lsize + 7) + 26
        rrect(c, 180, y - lsize - 8, 560, hh, 12, mix("#FFFFFF", INK2, 0.06), at)
        line(c, 186, y - lsize - 2, 186, y - lsize - 14 + hh, INK2, at, 4)
        for j, ln in enumerate(lines):
            text(c, ln, 204, y + j * (lsize + 7), lsize, "bold", INK, at, align="left")
        y += hh + 22
    if enun[1]:
        ae = ep(t, C[enun[2]] if len(enun) > 2 else C[enun[0]], 0.4)
        para(c, enun[1], 190, y + 4, 22, "black", INK, ae, 540, 28)
    if extra:
        extra(c, t, C, y)
    alts_panel(c, t, C, alts, 790, 222, 950, size, okc, okL, 6)


ALT1 = [("A", "um dado estatístico, para dimensionar o problema.", "17.A", "18.xa", "não há número nenhum", RED),
        ("B", "um contexto histórico, para explicar a origem do problema.", "17.B", "18.xb", "não há data nem fato do passado", RED),
        ("C", "um conceito, para esclarecer o que está em jogo.", "17.C", None, "", GREEN),
        ("D", "uma lei, para mostrar o que está garantido.", "17.D", "18.xd", "fonte que não aparece no trecho", RED),
        ("E", "uma frase de pensador, para dar autoridade.", "17.E", "18.xd", "fonte que não aparece no trecho", RED)]


def b_q1(c, t, C, B):
    questao(c, t, C, 1, "QUAL PORTA?", ("16", "16.r", "4 portas: lei ou obra · história · dado · conceito"), 1,
            "Desafios para o descarte correto do lixo eletrônico no Brasil",
            ("16.a", "Essa contextualização recorre principalmente a:", "16.e"), ALT1, "18.ok", "C",
            trecho=("16.s", "“Chama-se lixo eletrônico todo aparelho elétrico ou eletrônico descartado, do celular quebrado à geladeira velha.”"),
            size=26)
    pause_timer(c, t, C["17.end"] - 1.9, 1560, 790)


ALT2 = [("A", "Nesse sentido, o Brasil é um país muito grande.", "20.A", "21.xa", "informação sem relação com o recorte", RED),
        ("B", "Dessa forma, a velhice sempre foi estudada pelos filósofos.", "20.B", "21.xb", "cartão-postal: salta para o assunto amplo", RED),
        ("C", "Por isso, todos os idosos brasileiros já convivem plenamente em comunidade.", "20.C", "21.xc", "elimina o problema a discutir", RED),
        ("D", "Pesquisas mostram que 90% dos idosos vivem sozinhos.", "20.D", "21.xd", "dado sem fonte", RED),
        ("E", "Na prática, contudo, muitos idosos brasileiros passam os dias isolados em casa, longe da convivência que a lei promete.", "20.E", None, "", GREEN)]


def b_q2(c, t, C, B):
    questao(c, t, C, 2, "QUAL FRASE FAZ A PONTE?", ("19", "19.r", "ponte = rua: leva do mapa até a porta"), 2,
            "Desafios para garantir a convivência comunitária da pessoa idosa no Brasil",
            ("19.a", "Qual frase faz a ponte?", "19.e"), ALT2, "21.ok", "E",
            trecho=("19.s", "“O Estatuto da Pessoa Idosa assegura às pessoas com 60 anos ou mais direitos como saúde, dignidade e convivência comunitária.”"),
            size=24, lsize=21)
    pause_timer(c, t, C["20.end"] - 1.9, 1560, 800)


ALT3 = [("A", "A água é um recurso muito importante para todos.", "23.A", "24.xa", "só declara importância", RED),
        ("B", "Nas cidades brasileiras, o desperdício de água persiste pela falta de manutenção das redes de distribuição e pela pouca conscientização sobre o consumo doméstico.", "23.B", None, "", GREEN),
        ("C", "Até quando vamos desperdiçar água?", "23.C", "24.xc", "pergunta não é tese", RED),
        ("D", "Este texto vai discutir os desafios para a redução do desperdício de água nas cidades brasileiras.", "23.D", "24.xd", "só anuncia o tema", RED),
        ("E", "Em todo o mundo, a água é essencial para a vida.", "23.E", "24.xe", "tangencia: assunto amplo, sem Brasil", RED)]


def b_q3(c, t, C, B):
    questao(c, t, C, 3, "QUAL É A TESE?", ("22", "22.r", "tese: clara · contestável · completa · argumentável"), 3,
            "Desafios para a redução do desperdício de água nas cidades brasileiras",
            ("22.a", "Qual frase é uma tese clara, contestável e completa?", "22.e"), ALT3, "24.ok", "B", size=24)
    pause_timer(c, t, C["23.end"] - 1.9, 460, 790)


ALT4 = [("A", "dois agentes.", "26.A", None, "", GREEN),
        ("B", "dois substantivos coordenados.", "26.B", "27.xb", "seria “pela falta disso e pela falta daquilo”", RED),
        ("C", "causa e consequência.", "26.C", "27.xc", "precisaria de “isso causa aquilo”", RED),
        ("D", "uma pergunta retórica, que substitui a tese.", "26.D", "27.xd", "não há pergunta", RED),
        ("E", "nenhuma: a frase não antecipa eixos.", "26.E", "27.xe", "os dois eixos estão ali", RED)]


def b_q4(c, t, C, B):
    questao(c, t, C, 4, "QUE FORMA DE ANTECIPAR?", ("25", "25.r", "3 formas: 2 substantivos · causa e consequência · 2 agentes"), 3,
            "Desafios para combater o sedentarismo entre jovens no Brasil",
            ("25.a", "Que forma de antecipar foi usada?", "25.e"), ALT4, "27.ok", "A",
            trecho=("25.s", "A tese termina assim: “…um problema que envolve tanto a escola quanto as famílias.”"), size=28)
    pause_timer(c, t, C["26.end"] - 1.9, 1560, 790)
    ao = ep(t, C["27.ok"] + 1.2, 0.4)
    if ao > 0:
        for k, (s, xx) in enumerate((("escola → 1º parágrafo", 900), ("famílias → 2º parágrafo", 1300))):
            pill(c, s, xx, 760, MOV["lista"], size=24, a=ep(t, C["27.ok"] + 1.2 + 0.5 * k, 0.4), bounds=(0, 1920))


ALT5 = [("A", "Ampliar a doação exige vencer a desinformação e levar postos de coleta para fora dos grandes centros.", "29.A", None, "", INK),
        ("B", "A doação esbarra no medo, alimentado pela desinformação, e na escassez de postos fora das capitais.", "29.B", None, "", INK),
        ("C", "O problema envolve tanto a informação da população quanto a distribuição dos postos de coleta.", "29.C", None, "", INK),
        ("D", "A doação esbarra na desinformação e no preço dos exames de sangue.", "29.D", None, "", GREEN),
        ("E", "É preciso combater o medo de doar e espalhar os postos pelo interior.", "29.E", None, "", INK)]
PLANO5 = [("28.i", "1º", "medo e desinformação sobre a doação"),
          ("28.ii", "2º", "falta de postos de coleta fora dos grandes centros")]


def _plano5(c, t, C, y):
    y = 600
    text(c, "DESENVOLVIMENTO PLANEJADO", 190, y - 20, 16, "black", GRAY, ep(t, C["28.i"], 0.4), align="left", tracking=2)
    for k, (cue, n, s) in enumerate(PLANO5):
        a = ep(t, C[cue], 0.4)
        yy = y + 30 + k * 80
        badge_num(c, n, 212, yy - 8, a, 22, bg=MOV["lista"])
        para(c, s, 250, yy, 22, "black", INK, a, 480, 26)


def b_q5(c, t, C, B):
    questao(c, t, C, 5, "PROMESSA NÃO CUMPRIDA", ("28", "28.r", "promessa feita é promessa cobrada"), 3,
            "Caminhos para ampliar a doação de sangue no Brasil",
            ("28.a", "Qual tese promete um eixo que esse desenvolvimento NÃO cumpre?", "28.e"), ALT5, "30.ok", "D",
            extra=_plano5, size=24)
    pause_timer(c, t, C["29.end"] - 1.9, 460, 560)
    ao = ep(t, C["30.ok"] + 1.0, 0.4)
    if ao > 0:
        pill(c, "prometeu o PREÇO DOS EXAMES · entregou os POSTOS", 1265, 792, RED, size=22, a=ao, anchor="center", bounds=(0, 1920))
    ax = ep(t, C["30.xo"], 0.4)
    if ax > 0:
        pill(c, "A, B, C e E: os dois eixos planejados", 1265, 842, GREEN, size=20, a=ax, anchor="center", bounds=(0, 1920))


# ======================================================================
# desafio prático
# ======================================================================

TEMAS = [("2020", TEMA20), ("2022", TEMA22), ("2025", TEMA25)]


def b_desafio(c, t, C, B):
    head(c, t, B["start"], "DESAFIO PRÁTICO", "3 TEMAS REAIS · 2 INTRODUÇÕES CADA", AMBER)
    card(c, *CARD_R)
    for k, (ano, tema) in enumerate(TEMAS):
        a = ep(t, C["31.a"] + 0.5 * k, 0.4)
        y = 240 + k * 76
        pill(c, ano, 200, y, BLUE, size=24, a=a, bounds=(0, 1920))
        text(c, tema, 310, y + 10, 26, "black", INK, a, align="left")
    ab = ep(t, C["31.b"], 0.5)
    cronometro(c, 1530, 330, 100, ab, 1 - 0.5 * prog(t, C["31.b"], 8.0), "10 min")
    cards = [("31.c", "INTRODUÇÃO 1", "contextualização HISTÓRICA ou LEGAL", BLUE),
             ("31.d", "INTRODUÇÃO 2", "contextualização com DADO ou CONCEITO", BLUE)]
    for k, (cue, s1, s2, col) in enumerate(cards):
        a = ep(t, C[cue], 0.4)
        x = 200 + k * 620
        rrect(c, x, 500, 580, 130, 16, mix("#FFFFFF", col, 0.08), a, shadow=True)
        text(c, s1, x + 30, 548, 20, "black", col, a, align="left", tracking=2)
        text(c, s2, x + 30, 598, 26, "black", INK, a, align="left")
    ae = ep(t, C["31.e"], 0.4)
    for k, (s, key) in enumerate((("ponte", "rua"), ("tese", "tese"), ("dois eixos", "lista"))):
        a = ae * ep(t, C["31.e"] + 0.4 * k, 0.3)
        icone_peca(c, key, 270 + k * 300, 712, a, 0.55)
        text(c, s, 310 + k * 300, 722, 28, "black", MOV[key], a, align="left")
    af = ep(t, C["31.f"], 0.4)
    pill(c, "depois: TESTE DA RETIRADA + a tese cobre todos os blocos?", W / 2, 800, PURPLE, size=24, a=af, anchor="center",
         bounds=(0, 1920))


T20 = [("O estigma", DEL, "PROBLEMA", None, "32.b"), ("associado às doenças mentais", NUC, "NÚCLEO", None, "32.b"),
       ("na sociedade brasileira", DEL, "LUGAR", None, "32.b")]
CONCEITO = "Estigma é uma marca negativa que a sociedade cola numa pessoa."
PONTE = "Na sociedade brasileira, essa marca ainda recai sobre quem tem um transtorno mental."


def b_modelo(c, t, C, B):
    sid = which(t, C, ["32", "33", "34", "35"])
    head_seq(c, t, C, [("32", "EU FAÇO O PLANEJAMENTO · 2020", "OS BLOCOS", GREEN), ("33", "EU FAÇO O PLANEJAMENTO · 2020", "TESE E EIXOS", GREEN),
                       ("34", "EU FAÇO O PLANEJAMENTO · 2020", "AS DUAS PORTAS", GREEN), ("35", "EU FAÇO O PLANEJAMENTO · 2020", "CONFERÊNCIA", GREEN)])
    paper(c, 160, 150, 1600, 700, 1.0, lh=56, top=214)
    if sid in ("32", "33"):
        aa = ep(t, C["32.a"], 0.4)
        text(c, "“" + TEMA20 + "”", W / 2, 210, 30, "black", BLUE, aa)
        show = [ep(t, C["32.b"] + 0.5 * k, 0.4) for k in range(3)]
        puzzle(c, t, C, T20, 270, 1.0, 28, show, obriga=False)
        if sid == "32":
            ac = ep(t, C["32.c"], 0.4)
            icone(c, 3, 760, 560, ac, 1.0, label=False)
            text(c, "a tese do episódio 4", 830, 572, 36, "black", MOV["lista"], ac, align="left")
            return
        span = phrase_span("33", TESE20, C["33.a"], C["33.b"])
        text(c, "TESE", 280, 440, 18, "black", MOV["tese"], 1.0, align="left", tracking=2)
        hand_para(c, TESE20, 280, 490, 32, PEN, 1.0, 1380, 50, wreveal(t, span))
        for k, (cue, s) in enumerate((("33.b", "EIXO A · desinformação"), ("33.c", "EIXO B · mídia"))):
            pill(c, s, 280 + k * 420, 680, MOV["lista"], size=28, a=ep(t, C[cue], 0.4), bounds=(0, 1920))
        ad = ep(t, C["33.d"], 0.5)
        caixa(c, 1340, 640, 170, 120, ad)
        check_icon(c, 1560, 700, 30, ad, GREEN)
        return
    # 34 e 35: as duas introduções lado a lado
    ret = ep(t, C["35.a"], 0.5) if sid == "35" else 0.0
    xs = [260, 990]
    text(c, "INTRODUÇÃO 1 · CONCEITO", xs[0], 250, 20, "black", BLUE, ep(t, C["34.a"], 0.4), align="left", tracking=2)
    a1 = ep(t, C["34.a"], 0.3)
    r1 = wreveal(t, phrase_span("34", CONCEITO, C["34.a"], C["34.b"])) if sid == "34" else 1.0
    hand_para(c, CONCEITO, xs[0], 310, 30, PEN, a1 * (1 - 0.65 * ret), 640, 48, r1)
    if ret > 0:
        for j, ln in enumerate(hwrap(CONCEITO, 30, 640)):
            strike(c, xs[0] - 6, 300 + j * 48, xs[0] + hand_w(ln, 30) + 6, 300 + j * 48, ret, RED, ret)
    ab = ep(t, C["34.b"], 0.3)
    text(c, "PONTE", xs[0], 440, 18, "black", GREEN, ab, align="left", tracking=2)
    r2 = wreveal(t, phrase_span("34", PONTE, C["34.b"], C["34.c"])) if sid == "34" else 1.0
    hand_para(c, PONTE, xs[0], 490, 30, PEN, ab, 640, 48, r2)
    if ret > 0:
        a_q = ep(t, C["35.a"] + 2.5, 0.4)
        mx = xs[0] + hand_w("Na sociedade brasileira, ", 30)
        rrect(c, mx - 6, 458, hand_w("essa marca", 30) + 12, 44, 10, AMBER, 0.28 * a_q)
        selo(c, xs[0] + 520, 610, a_q, "“ESSA MARCA”? DEPENDE DA DEFINIÇÃO", GREEN, -3, 22)
    ac = ep(t, C["34.c"], 0.4)
    text(c, "INTRODUÇÃO 2 · HISTÓRICA OU LEGAL", xs[1], 250, 20, "black", BLUE, ac, align="left", tracking=2)
    for k in range(3):
        hand(c, "_" * 30, xs[1], 310 + k * 56, 30, LIGHT, ac, pen=False)
    ad = ep(t, C["34.d"], 0.4)
    selo(c, xs[1] + 330, 520, ad, "SÓ O QUE VOCÊ PODE VERIFICAR", AMBER, -4, 24)
    text(c, "Definição e ponte elaboradas para fins didáticos.", 260, 830, 16, "medium", GRAY, ep(t, C["34.a"], 0.3), align="left")
    if sid == "35":
        ae0 = ep(t, C["35.e"], 0.5)
        for k, (cue, s) in enumerate((("35.b", "o estigma"), ("35.c", "doenças mentais"), ("35.d", "sociedade brasileira"))):
            a = ep(t, C[cue], 0.3) * (1 - ae0)
            check_icon(c, 280 + k * 380, 700, 22, a, GREEN)
            text(c, s, 314 + k * 380, 710, 30, "black", INK, a, align="left")
        ae = ep(t, C["35.e"], 0.5)
        if ae > 0:
            rrect(c, 360, 260, 1200, 500, 24, "#FFFFFF", ae, shadow=True)
            text(c, "AGORA É COM VOCÊ", W / 2, 380, 40, "black", AMBER, ae, tracking=2)
            for k, (ano, _) in enumerate(TEMAS):
                pill(c, ano, 640 + k * 320, 480, BLUE, size=40, a=ae * ep(t, C["35.e"] + 0.3 * k, 0.3), anchor="center",
                     bounds=(0, 1920))
            text(c, "2 introduções por tema", W / 2, 590, 32, "black", INK2, ae)
            cronometro(c, W / 2, 660, 62, ae, 1 - 0.3 * prog(t, C["35.e"], 5.0), "10 min")


# ======================================================================
# checklist de domínio
# ======================================================================

DOM = [("37.e1", 0, ["os 3 movimentos e a pergunta de cada um", "é método, não critério oficial", "a competência de cada movimento"]),
       ("37.e2", 1, ["as 4 portas da contextualização", "o risco típico de cada porta"]),
       ("37.e3", 2, ["a frase-ponte", "o teste da retirada"]),
       ("38.e4", 3, ["tese × importância × repetição do tema", "tese clara, contestável e completa", "3 formas de antecipar",
                     "promessa não cumprida afeta a C3"]),
       ("38.e5", 4, ["as armadilhas de abertura"]),
       ("38.e6", 5, ["introdução completa em até 10 min de rascunho"])]


def b_dominio(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE SABE EXPLICAR", PURPLE)
    a0 = ep(t, C["36.a"], 0.5)
    if t < C["37"] - 0.05:
        boxed(c, 300, 330, 1320, 170, PURPLE, a0, 0.07)
        text(c, "só o que você explicaria EM VOZ ALTA", W / 2, 400, 40, "black", PURPLE, a0)
        text(c, "para outra pessoa, sem consultar nada", W / 2, 460, 32, "bold", INK2, a0)
        pill(c, "não marcou? reveja o episódio correspondente", W / 2, 620, AMBER, size=30, a=ep(t, C["36.b"], 0.4), anchor="center")
        return
    for ci, idxs in enumerate(((0, 1, 2), (3, 4, 5))):
        y = 190
        for i in idxs:
            cue, ic, itens = DOM[i]
            a = ep(t, C[cue], 0.4)
            x = 190 + ci * 790
            icone(c, ic, x + 36, y + 34, a, 0.55, label=False)
            text(c, f"EPISÓDIO {i + 1}", x + 90, y + 28, 18, "black", ICONES[ic][2], a, align="left", tracking=2)
            for j, s in enumerate(itens):
                yy = y + 68 + j * 40
                rrect(c, x + 90, yy - 22, 26, 26, 6, "#FFFFFF", a, stroke=2.5, stroke_color=INK2)
                text(c, s, x + 130, yy, 24, "bold", INK, a * ep(t, C[cue] + 0.4 * j, 0.3), align="left")
            y += 76 + len(itens) * 40


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO ASSUNTO", "DESENVOLVIMENTO", BLUE)
    aa = ep(t, C["39.a"], 0.5)
    etiqueta_intro(c, 200, 190, 640, aa, ok=[aa] * 4, movs=0.0, rowh=84, title="ETIQUETA PRONTA")
    ab = ep(t, C["39.b"], 0.5)
    text(c, "DESENVOLVIMENTO", 1300, 250, 48, "black", BLUE, ab)
    for k, s in enumerate(("tópico frasal", "argumento", "repertório", "análise", "fechamento")):
        pill(c, s, 1300, 310 + k * 56, BLUE, size=24, a=ep(t, C["39.b"] + 0.5 + 0.4 * k, 0.3), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["39.c"], 0.5)
    for k, s in enumerate(("item A → 1º parágrafo", "item B → 2º parágrafo")):
        a = ep(t, C["39.c"] + 0.4 * k, 0.4)
        arrow(c, 860, 640 + k * 70, 1040, 640 + k * 70, MOV["lista"], a, 5, 16, progress=a)
        text(c, s, 1070, 652 + k * 70, 32, "black", MOV["lista"], a, align="left")
    text(c, "entregar cada item prometido", 1300, 820, 30, "bold", INK2, ac)


def b_cta(c, t, C, B):
    cta_intro(c, t, C, "40", "Quantas das dez você acertou no verdadeiro ou falso?")


BLOCKS = dict(hook=b_hook, mapa=b_mapa, ideias=b_ideias, vf=b_vf, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5,
              desafio=b_desafio, modelo=b_modelo, dominio=b_dominio, ponte=b_ponte, cta=b_cta)
