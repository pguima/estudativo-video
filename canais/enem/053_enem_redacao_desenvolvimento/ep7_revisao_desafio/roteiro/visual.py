"""Visual — Redação ENEM, Desenvolvimento, Episódio 7: Revisão geral, pegadinhas e desafio prático (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): ícones e ficha das 5 etapas da entrega, mini_entrega,
faixas do parágrafo, tese do estigma, rascunho com caligrafia, alternativas, selo, cronômetro de pausa e CTA.
Novo aqui: ÍNDICE VISUAL com os 6 ícones dos episódios (caixa aberta · etiqueta · nota fiscal · escada do "e daí?" ·
parágrafo numerado · caderno de oficina), V ou F com selo âmbar PEGADINHA e o episódio a rever, 5 questões inéditas
(tema fictício marcado "Tema elaborado para fins didáticos"), o desafio da seção 13 com o teste do tópico frasal ao vivo
e o checklist de domínio agrupado por episódio.
Cores: azul = definição/tema · verde = método · âmbar = armadilha · vermelho = erro/penalidade · roxo = regra oficial.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep7_revisao_desafio.mp4"
TEMA_DID = "Tema elaborado para fins didáticos."


# ======================================================================
# os 6 ícones dos episódios (índice visual)
# ======================================================================

def ic_caixa_aberta(c, cx, cy, s, a, col):
    rrect(c, cx - 9 * s, cy - 34 * s, 18 * s, 26 * s, 2 * s, "#FFFFFF", a, stroke=2.5 * s, stroke_color=col)
    line(c, cx - 5 * s, cy - 27 * s, cx + 5 * s, cy - 27 * s, col, a, 2 * s)
    rrect(c, cx - 28 * s, cy - 8 * s, 56 * s, 36 * s, 3 * s, mix("#FFFFFF", col, 0.25), a, stroke=3 * s, stroke_color=col)
    for sg in (-1, 1):
        p = skia.Path()
        p.moveTo(cx + sg * 28 * s, cy - 8 * s); p.lineTo(cx + sg * 44 * s, cy - 24 * s)
        p.lineTo(cx + sg * 20 * s, cy - 26 * s); p.lineTo(cx + sg * 4 * s, cy - 8 * s); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.40), a))
        c.drawPath(p, paint(col, a, stroke=3 * s))


def ic_escada(c, cx, cy, s, a, col):
    for k in range(3):
        h = (k + 1) * 15 * s
        rrect(c, cx - 36 * s + k * 22 * s, cy + 26 * s - h, 22 * s, h, 2 * s, mix("#FFFFFF", col, 0.20 + 0.15 * k), a,
              stroke=2.5 * s, stroke_color=col)
    text_mid(c, "?", cx + 28 * s, cy - 32 * s, 26 * s, "black", col, a)


def ic_paragrafo(c, cx, cy, s, a, col):
    rrect(c, cx - 28 * s, cy - 32 * s, 56 * s, 64 * s, 4 * s, "#FFFFFF", a, stroke=3 * s, stroke_color=col)
    for k in range(3):
        y = cy - 16 * s + k * 17 * s
        c.drawCircle(cx - 16 * s, y, 6 * s, paint(col, a))
        text_mid(c, str(k + 1), cx - 16 * s, y, 9 * s, "black", "#FFFFFF", a)
        line(c, cx - 6 * s, y, cx + 20 * s - (k % 2) * 8 * s, y, col, a * 0.7, 2.5 * s)


def ic_caderno(c, cx, cy, s, a, col):
    rrect(c, cx - 24 * s, cy - 28 * s, 50 * s, 58 * s, 5 * s, PAPER, a, stroke=3 * s, stroke_color=col)
    for k in range(5):
        c.drawCircle(cx - 24 * s, cy - 20 * s + k * 10 * s, 3.5 * s, paint(col, a, stroke=2 * s))
    for k in range(3):
        line(c, cx - 12 * s, cy - 10 * s + k * 12 * s, cx + 18 * s, cy - 10 * s + k * 12 * s, LIGHT, a, 2 * s)
    line(c, cx - 10 * s, cy + 18 * s, cx + 16 * s, cy - 2 * s, PEN, a, 3 * s)


EPS = [(ic_caixa_aberta, "anatomia do parágrafo", MOV["lista"]),
       (ic_etiqueta, "tópico frasal", PARTE["topico"]),
       (ic_nota, "argumento e repertório", PARTE["repertorio"]),
       (ic_escada, "análise e fechamento", PARTE["analise"]),
       (ic_paragrafo, "do fraco ao bom", PARTE["fechamento"]),
       (ic_caderno, "oficina em 5 linhas", GREEN)]


def ep_icone(c, k, cx, cy, a, s=1.0, label=True, disc=True):
    if a <= 0:
        return
    fn, nm, col = EPS[k]
    if disc:
        c.drawCircle(cx, cy, 46 * s, paint(mix("#FFFFFF", col, 0.14), a))
    fn(c, cx, cy, s, a, col)
    if label:
        text(c, f"EP. {k + 1}", cx, cy + 74 * s, 18 * s, "black", col, a, tracking=2)


# ======================================================================
# gancho e mapa da série
# ======================================================================

def b_hook(c, t, C, B):
    sid = which(t, C, ["01", "02"])
    head_seq(c, t, C, [("01", SERIE_SELO, "REVISÃO GERAL", PURPLE), ("02", SERIE_SELO, "NESTA REVISÃO", PURPLE)])
    card(c, *CARD_R)
    if sid == "01":
        aa, ab, ac = (ep(t, C[f"01.{x}"], 0.5) for x in "abc")
        text(c, "NO DESENVOLVIMENTO, A TESE É...", 220, 260, 28, "black", GRAY, aa, align="left", tracking=2)
        if aa > 0:
            rrect(c, 220, 300, 640, 150, 20, mix("#FFFFFF", GREEN, 0.10), aa, shadow=True)
            text(c, "PROVADA", 500, 403, 80, "black", GREEN, aa)
            check_icon(c, 780, 376, 34, aa, GREEN)
        if ab > 0:
            rrect(c, 220, 480, 640, 150, 20, mix("#FFFFFF", RED, 0.08), ab, shadow=True)
            text(c, "ou só REPETIDA", 540, 583, 64, "black", RED, ab)
        if ac > 0:
            caixa(c, 1110, 340, 300, 240, ac, open_=ep(t, C["01.c"] + 0.4, 0.8))
            rrect(c, 1140, 470, 240, 90, 8, "#FFFFFF", ac)
            text(c, "LISTA DA CAIXA", 1260, 500, 16, "black", MOV["lista"], ac, tracking=1.5)
            text(c, "contém 2 itens: A e B", 1260, 540, 22, "black", INK, ac)
            for k, L in enumerate("AB"):
                a_ = ep(t, C["01.c"] + 0.8 + 0.4 * k, 0.4)
                badge_num(c, L, 1500 + k * 110, 380, a_, 34, bg=MOV["lista"])
            pill(c, "seus parágrafos ENTREGAM?", 1260, 680, AMBER, size=30, a=ep(t, C["01.c"] + 1.2, 0.4), anchor="center",
                 bounds=(0, 1920))
        return
    rows = [("02.b", "as 3 ideias que mais rendem", GREEN), ("02.c", "V ou F: 10 pegadinhas", AMBER),
            ("02.d", "5 questões inéditas", BLUE), ("02.e", "desafio prático", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 270 + k * 92 + d
        badge_num(c, k + 1, 280, y - 14, a, 28, bg=col)
        text(c, s, 330, y, 40, "black", INK, a, align="left")
    for k in range(6):
        ep_icone(c, k, 1150 + (k % 3) * 190, 300 + (k // 3) * 200, ep(t, C["02.a"] + 0.15 * k, 0.4), 1.0)
    af = ep(t, C["02.f"], 0.4)
    pill(c, "pegue papel e caneta", W / 2, 740, GREEN, size=30, a=af, anchor="center", bounds=(0, 1920))


def b_mapa(c, t, C, B):
    frame(c, t, B["start"], "AS IMAGENS DA SÉRIE", "A ENTREGA EM 5 ETAPAS", PURPLE)
    q = lambda x: C[f"03.{x}"]
    shw = [ep(t, q("b"), 0.4), ep(t, q("c"), 0.4), ep(t, q("c") + 1.6, 0.4), ep(t, q("d"), 0.4), ep(t, q("d") + 1.5, 0.4)]
    ficha_entrega(c, 180, 175, 820, ep(t, q("t"), 0.5), show=shw, partes=1.0, rowh=94, title="CADA PARÁGRAFO ENTREGA UM ITEM")
    aa = ep(t, q("a"), 0.5)
    ep_icone(c, 0, 1130, 260, aa, 0.9, label=False)
    text(c, "1 parágrafo = 1 item da lista", 1200, 270, 30, "black", MOV["lista"], aa, align="left")
    ad = ep(t, q("d") + 3.0, 0.4)
    if ad > 0:
        bubble(c, "E DAÍ?", 1120, 360, 300, PARTE["fechamento"], ad, left=True, size=40, fg="#FFFFFF")
        text(c, "a pergunta do cliente", 1450, 410, 26, "bold", INK2, ad, align="left")
    for k, (cue, ic, s1, s2) in enumerate((("e", 4, "parágrafo-modelo", "juntou tudo"),
                                            ("f", 5, "rascunho de 5 linhas", "= a LISTA DE COMPRAS"))):
        a, d = rise(t, q(cue))
        y = 590 + k * 140 + d
        ep_icone(c, ic, 1150, y, a, 0.8, label=False)
        text(c, s1, 1215, y - 4, 30, "black", INK, a, align="left")
        text(c, s2, 1215, y + 34, 26, "bold", EPS[ic][2], a, align="left")


IDEIAS = [("05.a", 0, None, "um parágrafo = UM EIXO", "anunciado na introdução"),
          ("05.b", None, "analise", "repertório + ANÁLISE", "só assim ele é produtivo"),
          ("05.c", None, "fechamento", "a última frase: E DAÍ?", "liga o parágrafo de volta à tese")]


def b_ideias(c, t, C, B):
    head_seq(c, t, C, [("04", "TESTE DE MEMÓRIA", "QUAIS SÃO AS 3 IDEIAS?", PURPLE), ("05", "O QUE MAIS RENDE", "AS 3 IDEIAS", GREEN)])
    card(c, *CARD_R)
    if t < C["05"] - 0.05:
        a = ep(t, C["04.a"], 0.5)
        for k in range(3):
            badge_num(c, k + 1, 500 + k * 460, 400, a, 70, bg=LIGHT)
            text_mid(c, "?", 500 + k * 460, 540, 80, "black", GRAY, a)
        pause_timer(c, t, C["04.p"] + 0.4, W / 2, 700)
        return
    for k, (cue, ic, key, s, sub) in enumerate(IDEIAS):
        a, d = rise(t, C[cue])
        x = 200 + k * 520
        col = EPS[ic][2] if ic is not None else PARTE[key]
        if a > 0:
            rrect(c, x, 230 + d, 480, 470, 22, mix("#FFFFFF", col, 0.08), a, shadow=True)
        badge_num(c, k + 1, x + 60, 290 + d, a, 30, bg=col)
        if ic is not None:
            ep_icone(c, ic, x + 240, 360 + d, a, 1.1, label=False)
        else:
            icone_etapa(c, key, x + 240, 360 + d, a, 1.1)
        para(c, s, x + 240, 500 + d, 38, "black", col, a, 430, 46, align="center")
        para(c, sub, x + 240, 610 + d, 28, "bold", INK2, a, 420, 34, align="center")


# ======================================================================
# verdadeiro ou falso (os 10 erros da seção 11)
# ======================================================================

# (cena, afirmação, verdadeira?, por que engana, a regra certa, episódio a rever 0–5)
VF = [("06", "“A saúde mental é importante” já funciona como tópico frasal.", False,
       "a frase fala do tema", "anuncie o argumento e o eixo", 1),
      ("07", "Repetir a mesma opinião com outras palavras ainda não é argumentar.", True,
       "o parágrafo fica cheio", "diga POR QUE a afirmação procede", 2),
      ("08", "Se o parágrafo cita uma obra famosa, o repertório já está produtivo.", False,
       "um nome famoso impressiona", "resuma o conteúdo e analise", 2),
      ("09", "Depois do repertório, pode ir direto para o fechamento.", False,
       "a referência parece falar sozinha", "pergunte “e daí?” à referência: a análise é a autoria", 3),
      ("10", "“Assim, isso é um problema muito grave” é um bom fechamento.", False,
       "tem conectivo de fechamento", "ligue o eixo à tese", 3),
      ("11", "A última frase do parágrafo não deve trazer informação nova.", True,
       "parece desperdício não aproveitar mais uma ideia", "assunto novo no fim fica sem desenvolvimento", 3),
      ("12", "Tratar os dois eixos no mesmo parágrafo economiza linhas.", False,
       "parece eficiente", "um parágrafo, UM EIXO", 0),
      ("13", "O 2º parágrafo não deve repetir o argumento do 1º.", True,
       "repetir dá a impressão de reforçar", "cada parágrafo acrescenta algo novo", 5),
      ("14", "Uma citação longa e decorada vale mais do que uma paráfrase.", False,
       "parece mostrar que você sabe muito", "paráfrase curta e atribuição correta", 2),
      ("15", "As 5 partes do parágrafo são método, e não regra oficial do Inep.", True,
       "o modelo vem sempre na mesma ordem", "a ordem pode variar; o raciocínio não pode faltar", 0)]
VF_EXTRA = {"08": ("repertório mencionado sem uso tende a não ser produtivo", INK2),
            "10": ("recibo sem assinatura não vale", PARTE["fechamento"]),
            "12": ("senão a progressão fica confusa e um eixo some", INK2),
            "13": ("repetição desnecessária pesa na C3", INK2),
            "14": ("gaste as linhas na análise", INK2),
            "15": ("os descritores avaliam desenvolvimento e organização", PURPLE)}


def b_vf(c, t, C, B):
    ids = [v[0] for v in VF]
    sid = which(t, C, ids)
    n = ids.index(sid)
    _, frase, ok, engana, regra_, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 10", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    for k in range(10):
        badge_num(c, k + 1, 600 + k * 80, 205, 1, 20, bg=AMBER if k == n else (INK2 if k < n else LIGHT))
    q = lambda x: C[f"{sid}.{x}"]
    aq, d = rise(t, q("q"))
    ep_icone(c, ic, 280, 350 + d, aq, 0.9, label=False)
    text(c, f"EP. {ic + 1}", 280, 440 + d, 18, "black", EPS[ic][2], aq, tracking=2)
    shown = frase if frase.startswith("“") else "“" + frase + "”"
    para(c, shown, 380, 340 + d, 44, "black", INK, aq, 1220, 54)
    pause_timer(c, t, q("p") + 0.3, 1600, 560)
    ar = ep(t, q("r"), 0.4)
    if ar > 0:
        selo(c, 470, 560, ar, "VERDADEIRO" if ok else "FALSO", GREEN if ok else RED, -6, 52)
    aw = ep(t, q("w"), 0.4)
    if aw > 0:
        selo(c, 880, 560, aw, "PEGADINHA", AMBER, 4, 30)
        para(c, "engana: " + engana, 1030, 550, 26, "bold", INK2, aw, 640, 30)
    ak = ep(t, q("k"), 0.4)
    if ak > 0:
        rrect(c, 240, 670, 1440, 130, 18, mix("#FFFFFF", GREEN, 0.10), ak)
        if sid in VF_EXTRA:
            check_icon(c, 300, 712, 26, ak, GREEN)
            text(c, regra_, 350, 724, 34, "black", GREEN, ak, align="left")
            s2, col2 = VF_EXTRA[sid]
            text(c, s2, 350, 776, 26, "bold", col2, ep(t, q("k") + 1.6, 0.4), align="left")
        else:
            check_icon(c, 300, 735, 26, ak, GREEN)
            text(c, regra_, 350, 747, 34, "black", GREEN, ak, align="left")


# ======================================================================
# as 5 questões inéditas
# ======================================================================

def lembrando(c, t, C, cue, ic, s, etapa=None):
    ar = ep(t, C[cue], 0.4)
    if etapa:
        icone_etapa(c, etapa, 225, 255, ar, 0.62)
    else:
        ep_icone(c, ic, 225, 255, ar, 0.62, label=False)
    pill(c, "LEMBRANDO", 290, 228, PURPLE, size=17, a=ar, bounds=(0, 1920))
    para(c, s, 290, 282, 23, "black", PURPLE, ar, 450, 27)


def tema_bloco(c, t, C, cue, tema, y=370):
    aa = ep(t, C[cue], 0.4)
    text(c, "TEMA", 190, y, 16, "black", GRAY, aa, align="left", tracking=2)
    h = para(c, "“" + tema + "”", 190, y + 36, 26, "black", BLUE, aa, 550, 32)
    text(c, TEMA_DID, 190, y + 36 + h, 16, "medium", AMBER, aa, align="left")
    return y + 36 + h + 46


def eixos_bloco(c, t, C, cue, e1, e2, y, cue_i=None):
    a = ep(t, C[cue], 0.4)
    text(c, "EIXOS DA TESE", 190, y, 16, "black", GRAY, a, align="left", tracking=2)
    for k, (s, col) in enumerate(((e1, PARTE["topico"]), (e2, PARTE["argumento"]))):
        ak = ep(t, C[cue] + 0.6 * k, 0.4)
        yy = y + 40 + k * 56
        badge_num(c, k + 1, 206, yy, ak, 18, bg=col)
        text(c, s, 236, yy + 8, 24, "black", INK, ak, align="left")
        if k == 0 and cue_i:
            ai = ep(t, C[cue_i], 0.4)
            if ai > 0:
                xx = 236 + text_w(s, "black", 24) + 16
                lab = "1º parágrafo ✓" if xx + 150 < 740 else "✓"  # eixo longo: só o ✓, sem invadir as alternativas
                pill(c, lab, xx, yy, GREEN, size=16, a=ai, bounds=(0, 1920))
    return y + 40 + 2 * 56


def enunciado(c, t, C, cue, s, y):
    para(c, s, 190, y, 26, "black", INK, ep(t, C[cue], 0.4), 550, 32)


ALT1 = [("A", "O transporte coletivo é muito importante para as cidades.", "17.A", "18.xa", "vago: não anuncia argumento", RED),
        ("B", "Existem vários meios de transporte coletivo, como o ônibus e o metrô.", "17.B", "18.xb", "informativo: não defende nada", RED),
        ("C", "Em primeiro lugar, a baixa frequência dos ônibus afasta passageiros do transporte coletivo.", "17.C", None, "", GREEN),
        ("D", "Será que um dia o ônibus vai chegar no horário?", "17.D", "18.xd", "pergunta retórica", RED),
        ("E", "Por outro lado, a insegurança nos pontos também é um problema.", "17.E", "18.xe", "“por outro lado” sem contraste · outro eixo", RED)]


def b_q1(c, t, C, B):
    head(c, t, C["16"], "QUESTÃO 1 · INÉDITA", "O TÓPICO FRASAL DO EIXO", BLUE)
    card(c, *CARD_R)
    lembrando(c, t, C, "16.r", 1, "tópico frasal = ETIQUETA: anuncia o eixo e o que vai provar", "topico")
    y = tema_bloco(c, t, C, "16.a", "Desafios para ampliar o uso do transporte coletivo nas cidades brasileiras")
    y = eixos_bloco(c, t, C, "16.s", "baixa frequência dos ônibus", "insegurança nos pontos", y)
    enunciado(c, t, C, "16.e", "Qual frase funciona como tópico frasal do 1º eixo?", y + 10)
    alts_panel(c, t, C, ALT1, 790, 232, 950, 28, "18.ok", "C", 8)
    pause_timer(c, t, C["17.end"] - 1.9, 1600, 740)


Q2_FRASES = ["Em primeiro lugar, a falta de intérpretes de Libras nas empresas prejudica trabalhadores surdos.",
             "Isso ocorre porque, sem quem domine a língua de sinais, o funcionário surdo não acompanha reuniões.",
             "A Lei nº 10.436/2002 reconhece a Língua Brasileira de Sinais como meio legal de comunicação e expressão.",
             "Dessa forma, sem intérpretes, o trabalhador surdo continua à margem da empresa."]
Q2_KEYS = ["topico", "argumento", "repertorio", "fechamento"]
ALT2 = [("A", "um tópico frasal, pois o parágrafo não anuncia o argumento.", "20.A", "21.xa", "a frase 1 é a etiqueta", RED),
        ("B", "a análise, que confrontaria a lei com a realidade das empresas.", "20.B", None, "", GREEN),
        ("C", "um argumento, pois falta explicar por que a afirmação procede.", "20.C", "21.xc", "a frase 2 é o porquê", RED),
        ("D", "um fechamento, pois o parágrafo não volta à tese.", "20.D", "21.xd", "a frase 4 é o recibo", RED),
        ("E", "uma pergunta retórica no final, para envolver o leitor.", "20.E", "21.xe", "pergunta não amarra nada", RED)]


def b_q2(c, t, C, B):
    head(c, t, C["19"], "QUESTÃO 2 · INÉDITA", "A PARTE QUE FALTA", BLUE)
    card(c, *CARD_R)
    alt_on = ep(t, C["20"], 0.7)
    lembrando(c, t, C, "19.r", 3, "depois da NOTA FISCAL, o PRODUTO FUNCIONANDO: a análise", "analise")
    aa = ep(t, C["19.a"], 0.4)
    text(c, "TEMA", 190, 370, 16, "black", GRAY, aa, align="left", tracking=2)
    tema = "“Desafios para a inclusão de trabalhadores surdos no Brasil”"
    h = para(c, tema, 190, 406, 26, "black", BLUE, aa, lerp(1400, 550, alt_on), 32)
    text(c, TEMA_DID, 190, 406 + h, 16, "medium", AMBER, aa, align="left")
    y0 = 406 + h + lerp(50, 26, alt_on)
    ok = ep(t, C["21.ok"], 0.5)
    rv = [ep(t, C[f"19.s{k + 1}"], 0.4) for k in range(4)]
    size = lerp(28, 20, alt_on)
    lh = lerp(38, 26, alt_on)
    w = lerp(1460, 560, alt_on)
    gap = 40 * ok
    sp1 = faixas_paragrafo(c, 200, y0 + size, w, size, lh, Q2_FRASES[:3], Q2_KEYS[:3], 1.0, reveal=rv[:3], faixa=[ok] * 3)
    y4 = sp1[-1][1] + 6 + gap + size
    fr4 = "[4] " + Q2_FRASES[3]
    sp2 = faixas_paragrafo(c, 200, y4, w, size, lh, [fr4], ["fechamento"], 1.0, reveal=rv[3:], faixa=[ok], nums=False)
    if ok > 0:
        pill(c, "✗ falta: ANÁLISE (o produto funcionando)", 200, sp1[-1][1] + 6 + gap / 2 + 2, RED, size=18,
             a=ep(t, C["21.ok"] + 0.6, 0.4), bounds=(0, 1920))
    text(c, "Parágrafo elaborado para fins didáticos.", 200, sp2[-1][1] + 24, 16, "medium", AMBER, aa * clamp(rv[3]),
         align="left")
    ae = ep(t, C["19.e"], 0.4) * (1 - alt_on)
    if ae > 0:
        text(c, "O que mais falta a esse parágrafo?", 1730, 280, 34, "black", INK, ae, align="right")
    if alt_on > 0:
        alts_panel(c, t, C, ALT2, 790, 232, 950, 28, "21.ok", "B", 8)
        pause_timer(c, t, C["20.end"] - 1.9, 1600, 740)


ALT3 = [("A", "Esse filme é muito bonito e vale a pena assistir.", "23.A", "24.xa", "só elogia a obra", RED),
        ("B", "O diretor do filme é Giuseppe Tornatore.", "23.B", "24.xb", "repete a atribuição, sem uso", RED),
        ("C", "Dessa forma, isso é um problema muito grave.", "23.C", "24.xc", "pula a análise e fecha vago", RED),
        ("D", "Em muitas pequenas cidades brasileiras, porém, não há espaço parecido, e os moradores ficam sem um ponto de "
              "encontro e de cultura.", "23.D", None, "", GREEN),
        ("E", "Além disso, a internet mudou a forma de ver filmes.", "23.E", "24.xe", "assunto novo", RED)]


def b_q3(c, t, C, B):
    head(c, t, C["22"], "QUESTÃO 3 · INÉDITA", "ANÁLISE OU SÓ MENÇÃO?", BLUE)
    card(c, *CARD_R)
    lembrando(c, t, C, "22.r", 3, "parar na referência = CITAR · chegar ao que ela prova = ARGUMENTAR")
    y = tema_bloco(c, t, C, "22.a", "Desafios para manter espaços de cultura nas pequenas cidades brasileiras")
    at = ep(t, C["22.s"], 0.4)
    icone_etapa(c, "repertorio", 222, y + 10, at, 0.42, disc=False)
    text(c, "NOTA FISCAL (repertório)", 252, y + 6, 16, "black", PARTE["repertorio"], at, align="left", tracking=1.5)
    s = "No filme Cinema Paradiso, de Giuseppe Tornatore, a sala de cinema é o centro da vida cultural de uma pequena cidade."
    lines = wrap(s, "bold", 21, 510)
    hh = len(lines) * 28 + 22
    rrect(c, 180, y + 26, 560, hh, 12, mix("#FFFFFF", PARTE["repertorio"], 0.10), at)
    for j, ln in enumerate(lines):
        text(c, ln, 200, y + 58 + j * 28, 21, "bold", INK, at, align="left")
    enunciado(c, t, C, "22.e", "Qual frase, logo depois, faz ANÁLISE, e não só menção?", y + hh + 70)
    alts_panel(c, t, C, ALT3, 790, 232, 950, 28, "24.ok", "D", 8)
    ao = ep(t, C["24.ok"] + 1.0, 0.4)
    if ao > 0:
        icone_etapa(c, "analise", 1640, 780, ao, 0.6)
        text(c, "produto funcionando", 1580, 790, 22, "black", PARTE["analise"], ao, align="right")
    pause_timer(c, t, C["23.end"] - 1.9, 1600, 740)


ALT4 = [("A", "Desse modo, enquanto a coleta seletiva não chegar aos bairros, o descarte irregular continuará a marcar as "
              "cidades brasileiras.", "26.A", None, "", GREEN),
        ("B", "Assim, isso é algo muito triste e preocupante.", "26.B", "27.xb", "vago: “isso” e “triste” não dizem nada", RED),
        ("C", "Será que um dia as cidades vão ficar limpas?", "26.C", "27.xc", "pergunta retórica", RED),
        ("D", "Além disso, a poluição do ar também prejudica as cidades.", "26.D", "27.xd", "assunto novo no fim", RED),
        ("E", "Em primeiro lugar, a coleta seletiva é responsabilidade de todos.", "26.E", "27.xe", "reinicia o parágrafo", RED)]


def b_q4(c, t, C, B):
    head(c, t, C["25"], "QUESTÃO 4 · INÉDITA", "O FECHAMENTO QUE LIGA À TESE", BLUE)
    card(c, *CARD_R)
    lembrando(c, t, C, "25.r", 3, "fechamento = RECIBO ASSINADO: eixo → tese, sem informação nova", "fechamento")
    y = tema_bloco(c, t, C, "25.a", "Desafios para reduzir o descarte irregular de lixo nas cidades brasileiras")
    y = eixos_bloco(c, t, C, "25.s", "falta de coleta seletiva nos bairros", "pouca informação sobre a separação", y,
                    cue_i="25.i")
    enunciado(c, t, C, "25.e", "Qual frase fecha o parágrafo do 1º eixo?", y + 10)
    alts_panel(c, t, C, ALT4, 790, 232, 950, 28, "27.ok", "A", 8)
    pause_timer(c, t, C["26.end"] - 1.9, 1600, 740)


ALT5 = [("A", "Em primeiro lugar, a falta de limites nas famílias favorece o uso excessivo do celular.", "29.A", "30.xa",
         "repete o 1º eixo · “em primeiro lugar”", RED),
        ("B", "Por outro lado, a falta de limites em casa também é um problema.", "29.B", "30.xb",
         "“por outro lado” sem contraste", RED),
        ("C", "O celular é muito importante na vida dos jovens.", "29.C", "30.xc", "vago", RED),
        ("D", "Existem muitos aplicativos, como jogos e redes sociais.", "29.D", "30.xd", "só informa", RED),
        ("E", "Além disso, aplicativos pensados para prender a atenção fazem o estudante perder a noção do tempo.", "29.E",
         None, "", GREEN)]


def b_q5(c, t, C, B):
    head(c, t, C["28"], "QUESTÃO 5 · INÉDITA", "ABRINDO O SEGUNDO EIXO", BLUE)
    card(c, *CARD_R)
    lembrando(c, t, C, "28.r", 0, "cada parágrafo entrega UM item: o 2º não repete o 1º")
    y = tema_bloco(c, t, C, "28.a", "Os desafios do uso excessivo do celular entre estudantes brasileiros")
    y = eixos_bloco(c, t, C, "28.s", "falta de limites nas famílias", "aplicativos que prendem a atenção", y, cue_i="28.i")
    enunciado(c, t, C, "28.e", "Qual frase abre o 2º parágrafo de desenvolvimento?", y + 10)
    alts_panel(c, t, C, ALT5, 790, 232, 950, 28, "30.ok", "E", 8)
    pause_timer(c, t, C["29.end"] - 1.9, 1600, 740)


# ======================================================================
# desafio prático (seção 13)
# ======================================================================

def b_desafio(c, t, C, B):
    sid = which(t, C, ["31", "32"])
    head_seq(c, t, C, [("31", "DESAFIO PRÁTICO", "OS DOIS DESENVOLVIMENTOS DA SUA REDAÇÃO", AMBER),
                       ("32", "DESAFIO PRÁTICO", "DUAS CONFERÊNCIAS", AMBER)])
    card(c, *CARD_R)
    if sid == "31":
        steps = [("31.a", "retome uma introdução sua", "da série Introdução", None),
                 ("31.b", "escreva os 2 parágrafos", "de desenvolvimento: item A e item B", 0),
                 ("31.c", "planeje cada um em 5 linhas", "= a lista de compras", 5),
                 ("31.d", "redija", "cada linha vira uma ou duas frases", 4)]
        for k, (cue, s1, s2, ic) in enumerate(steps):
            a, d = rise(t, C[cue])
            y = 250 + k * 120 + d
            badge_num(c, k + 1, 230, y, a, 30, bg=AMBER)
            if ic is None:
                icone_peca(c, "lista", 330, y, a, 0.75)
            else:
                ep_icone(c, ic, 330, y, a, 0.75, label=False)
            text(c, s1, 400, y - 2, 38, "black", INK, a, align="left")
            text(c, s2, 400, y + 38, 26, "bold", INK2, a, align="left")
        ae = ep(t, C["31.e"], 0.4)
        if ae > 0:
            badge_num(c, 5, 230, 730, ae, 30, bg=AMBER)
            text(c, "marque cada parte:", 280, 742, 32, "black", INK, ae, align="left")
            x = 600
            for k, key in enumerate(KEYS):
                ak = ep(t, C["31.e"] + 0.5 + 0.4 * k, 0.3)
                x0, x1 = pill(c, NOMEP[key], x, 730, PARTE[key], size=24, a=ak, bounds=(0, 1920))
                x = x1 + 16 if ak > 0 else x + text_w(NOMEP[key], "bold", 24) + 46
        return
    aa = ep(t, C["32.a"], 0.4)
    text(c, "no fim, duas conferências:", 220, 260, 34, "black", INK2, aa, align="left")
    ab = ep(t, C["32.b"], 0.4)
    if ab > 0:
        boxed(c, 200, 310, 740, 460, PARTE["repertorio"], ab, 0.06)
        text(c, "TESTE DA RETIRADA", 570, 370, 30, "black", PARTE["repertorio"], ab, tracking=2)
        u = ep(t, C["32.b"] + 0.8, 1.2)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(370, 430, 140, 140), 18, 18), paint(LIGHT, ab, stroke=4))
        icone_etapa(c, "repertorio", 440 + 260 * u, 500, ab, 1.3)
        arrow(c, 530, 590, 760, 590, PARTE["repertorio"], ab * u, 5, 16, progress=u)
        text(c, "?", 440, 515, 48, "black", LIGHT, ab * u)
        para(c, "a nota fiscal sai e nada muda? então ela não trabalhava", 570, 650, 28, "black", INK, ab, 640, 36,
             align="center")
        text(c, "com cada repertório", 570, 740, 22, "bold", INK2, ab)
    ac = ep(t, C["32.c"], 0.4)
    if ac > 0:
        boxed(c, 980, 310, 740, 460, PARTE["topico"], ac, 0.06)
        text(c, "TESTE DO TÓPICO FRASAL", 1350, 370, 30, "black", PARTE["topico"], ac, tracking=2)
        for k, (s, col) in enumerate((("TESE", MOV["tese"]), ("TÓPICO 1", PARTE["topico"]), ("TÓPICO 2", PARTE["topico"]))):
            a = ep(t, C["32.c"] + 0.5 + 0.4 * k, 0.4)
            y = 430 + k * 90
            rrect(c, 1030, y, 640, 66, 12, "#FFFFFF", a, shadow=True)
            rrect(c, 1030, y, 10, 66, 5, col, a)
            text(c, s, 1064, y + 42, 22, "black", col, a, align="left", tracking=1.5)
            for j in range(2):
                line(c, 1230, y + 26 + j * 16, 1640 - j * 120, y + 26 + j * 16, LIGHT, a, 6)
        text(c, "lidos em sequência", 1350, 740, 22, "bold", INK2, ac)


def b_teste(c, t, C, B):
    sid = which(t, C, ["33", "34"])
    head_seq(c, t, C, [("33", "EU FAÇO · AO VIVO", "O TESTE DO TÓPICO FRASAL", GREEN),
                       ("34", "EU FAÇO · AO VIVO", "UM RACIOCÍNIO COMPLETO?", GREEN)])
    paper(c, 160, 150, 1600, 700, 1.0, lh=48, top=228)
    text(c, "ENEM 2020 · " + TEMA20, 260, 210, 22, "black", BLUE, ep(t, C["33.t"], 0.4), align="left")
    T1, T2 = TOPICOS[2][0], TOPICOS[3][0]
    items = [("33.a", "33.b", "TESE", TESE20, MOV["tese"], 332, "34.b", "POSIÇÃO: o estigma persiste"),
             ("33.b", "33.c", "TÓPICO 1", T1, PARTE["topico"], 524, "34.c", "RAZÃO 1: a desinformação"),
             ("33.c", "33.end", "TÓPICO 2", T2, PARTE["topico"], 668, "34.d", "RAZÃO 2: a mídia")]
    for cue0, cue1, lab, s, col, y, cue_k, tag in items:
        a = ep(t, C[cue0], 0.3)
        if sid == "33":
            rv = wreveal(t, phrase_span("33", s, C[cue0] + 0.6, C[cue1] - 0.4))
        else:
            rv = 1.0
        text(c, lab, 260, y - 52, 18, "black", col, a, align="left", tracking=2)
        hand_para(c, s, 260, y, 32, PEN, a, 1440, 48, rv)
        if sid == "34":
            ak = ep(t, C[cue_k], 0.4)
            pill(c, tag, 260 + text_w(lab, "black", 18) + 40, y - 58, col, size=20, a=ak, bounds=(0, 1920))
    if sid == "34":
        ae = ep(t, C["34.e"], 0.4)
        selo(c, 1480, 800, ae, "PROJETO DE TEXTO VISÍVEL ✓", GREEN, -4, 28)
        af = ep(t, C["34.f"], 0.4)
        pill(c, "agora é com você: a SUA redação", 260, 800, AMBER, size=26, a=af, bounds=(0, 1920))


# ======================================================================
# checklist de domínio (seção 13)
# ======================================================================

DOM = [("36.e1", ["nomeio as 5 partes e a pergunta de cada uma", "sei que o modelo é método, não critério oficial"]),
       ("36.e2", ["escrevo um tópico frasal que retoma um eixo", "escolho o conectivo de abertura pelo sentido"]),
       ("36.e3", ["explico com causa e consequência", "cito as estratégias listadas pela Cartilha",
                  "repertório com atribuição correta e paráfrase"]),
       ("37.e4", ["análise que liga a referência ao Brasil de hoje", "fechamento: eixo → tese, sem informação nova"]),
       ("37.e5", ["transformo “só opinião” em argumento", "reconheço e corrijo o repertório solto"]),
       ("37.e6", ["planejo um parágrafo em 5 linhas", "2 parágrafos: eixos diferentes, equilibrados"])]


def b_dominio(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE SABE EXPLICAR", PURPLE)
    a0 = ep(t, C["35.a"], 0.5)
    if t < C["36"] - 0.05:
        boxed(c, 300, 300, 1320, 170, PURPLE, a0, 0.07)
        text(c, "só o que você explicaria EM VOZ ALTA", W / 2, 370, 40, "black", PURPLE, a0)
        text(c, "para outra pessoa, sem consultar nada", W / 2, 430, 32, "bold", INK2, a0)
        ab = ep(t, C["35.b"], 0.4)
        pill(c, "não marcou? reveja o episódio correspondente", W / 2, 560, AMBER, size=30, a=ab, anchor="center")
        for k in range(6):
            ep_icone(c, k, 560 + k * 160, 680, ep(t, C["35.b"] + 0.5 + 0.12 * k, 0.4), 0.6, label=True)
        return
    for ci, idxs in enumerate(((0, 1, 2), (3, 4, 5))):
        y = 190
        for i in idxs:
            cue, itens = DOM[i]
            a = ep(t, C[cue], 0.4)
            x = 180 + ci * 800
            ep_icone(c, i, x + 36, y + 30, a, 0.6, label=False)
            text(c, f"EPISÓDIO {i + 1} · {EPS[i][1].upper()}", x + 90, y + 30, 20, "black", EPS[i][2], a, align="left",
                 tracking=2)
            for j, s in enumerate(itens):
                yy = y + 72 + j * 44
                rrect(c, x + 90, yy - 23, 28, 28, 6, "#FFFFFF", a, stroke=2.5, stroke_color=INK2)
                text(c, s, x + 132, yy, 26, "bold", INK, a * ep(t, C[cue] + 0.4 * j, 0.3), align="left")
            y += 82 + len(itens) * 44


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMA SÉRIE", "CONCLUSÃO", BLUE)
    aa = ep(t, C["38.a"], 0.5)
    for k, L in enumerate("AB"):
        a = ep(t, C["38.a"] + 0.4 * k, 0.4)
        text(c, f"ITEM {L} · {k + 1}º desenvolvimento", 420, 225 + k * 270, 22, "black", MOV["lista"], a, tracking=1.5)
        mini_entrega(c, 420, 340 + k * 270, a, [1, 1, 1, 1, 1], 1.0)
    selo(c, 420, 790, aa, "ENTREGUES ✓", GREEN, -4, 30)
    ab = ep(t, C["38.b"], 0.4)
    if ab > 0:
        text(c, "falta o último passo:", 780, 270, 30, "bold", INK2, ab, align="left")
        for k, s in enumerate(("conferir a entrega", "dizer o que fazer com o problema")):
            a = ep(t, C["38.b"] + 0.5 + 0.5 * k, 0.4)
            check_icon(c, 800, 330 + k * 60, 16, a, GREEN)
            text(c, s, 830, 342 + k * 60, 32, "black", INK, a, align="left")
    ac = ep(t, C["38.c"], 0.4)
    if ac > 0:
        text(c, "CONCLUSÃO", 1230, 520, 64, "black", BLUE, ac)
        x = 780
        for k, s in enumerate(("agente", "ação", "meio", "finalidade", "detalhamento")):
            ak = ep(t, C["38.c"] + 0.6 + 0.35 * k, 0.3)
            x0, x1 = pill(c, s, x, 610, BLUE, size=26, a=ak, bounds=(0, 1920))
            x = x1 + 14 if ak > 0 else x + text_w(s, "bold", 26) + 46
        pill(c, "Próxima série: Redação: Conclusão", 1230, 730, GREEN, size=28, a=ep(t, C["38.c"] + 2.4, 0.4),
             anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "39", "Quantas das dez você acertou no verdadeiro ou falso?")


BLOCKS = dict(hook=b_hook, mapa=b_mapa, ideias=b_ideias, vf=b_vf, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5,
              desafio=b_desafio, teste=b_teste, dominio=b_dominio, ponte=b_ponte, cta=b_cta)
