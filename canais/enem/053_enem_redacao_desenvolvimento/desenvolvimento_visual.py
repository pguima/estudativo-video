"""Visual compartilhado — Redação ENEM, série DESENVOLVIMENTO (053), tema claro.
Uso no roteiro/visual.py de cada episódio:
    import sys; from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from desenvolvimento_visual import *   # noqa
    usar_tempos(__file__)                  # liga phrase_span/wreveal ao audio/tempos.json do episódio
Reaproveita a série Introdução (052: introducao_visual — etiqueta, recap, erros, CTA com Anki) e, por ela, a série
Leitura da Proposta (014: rascunho com caligrafia, caixa, selo, pausa, alternativas, placar).
Novo aqui (analogia âncora da série): cada parágrafo de desenvolvimento ENTREGA UM ITEM da lista colada na caixa,
em 5 etapas — ETIQUETA DO ITEM (tópico frasal) · POR QUE ESTÁ NA CAIXA (argumento) · NOTA FISCAL (repertório) ·
PRODUTO FUNCIONANDO (análise) · RECIBO ASSINADO (fechamento). Ícones das etapas, a ficha da entrega (checklist),
as barras de peso típico, os textos EXATOS do material (seções 03–10) e o selo "método, não regra".
Cores com função: azul = definição/tema · verde = dica/método · âmbar = armadilha · vermelho = erro/penalidade ·
roxo = regra oficial (Cartilha). Cores das ETAPAS (faixas do parágrafo-modelo): PARTE[...]
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "052_enem_redacao_introducao"))
import introducao_visual as _iv
from introducao_visual import *  # noqa
import skia
import motor
motor.set_theme("claro")

SERIE_SELO = "REDAÇÃO ENEM · DESENVOLVIMENTO"
TEMA19 = "Democratização do acesso ao cinema no Brasil"
TEMA23 = "Desafios para o enfrentamento da invisibilidade do trabalho de cuidado realizado pela mulher no Brasil"
PARAG_DIDATICO = "Parágrafo elaborado para fins didáticos."


def usar_tempos(visual_file):
    _iv.usar_tempos(visual_file)


# ======================================================================
# as 5 etapas da entrega (analogia âncora da série)
# ======================================================================

PARTE = dict(topico="#2F6FED", argumento="#0E8C9A", repertorio="#B7791F", analise="#D9480F", fechamento="#C2255C")
ETAPAS = [  # chave, etapa da entrega, parte do parágrafo, pergunta
    ("topico", "ETIQUETA DO ITEM", "tópico frasal", "o que afirmo?"),
    ("argumento", "POR QUE ESTÁ NA CAIXA", "argumento", "por que procede?"),
    ("repertorio", "NOTA FISCAL", "repertório", "o que comprova?"),
    ("analise", "PRODUTO FUNCIONANDO", "análise", "o que isso mostra?"),
    ("fechamento", "RECIBO ASSINADO", "fechamento", "e daí? → tese"),
]
KEYS = [e[0] for e in ETAPAS]
ETAPA = {e[0]: e[1] for e in ETAPAS}
NOMEP = {e[0]: e[2] for e in ETAPAS}
PERGP = {e[0]: e[3] for e in ETAPAS}
PESO = dict(topico=0.42, argumento=0.62, repertorio=0.62, analise=1.0, fechamento=0.48)   # peso TÍPICO (seção 02)


def ic_etiqueta(c, cx, cy, s, a, col):
    p = skia.Path()
    p.moveTo(cx - 30 * s, cy - 20 * s); p.lineTo(cx + 14 * s, cy - 20 * s); p.lineTo(cx + 32 * s, cy)
    p.lineTo(cx + 14 * s, cy + 20 * s); p.lineTo(cx - 30 * s, cy + 20 * s); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.25), a))
    c.drawPath(p, paint(col, a, stroke=3 * s))
    c.drawCircle(cx + 12 * s, cy, 4.5 * s, paint(col, a))
    for k in range(2):
        line(c, cx - 22 * s, cy - 6 * s + k * 12 * s, cx + 2 * s - k * 8 * s, cy - 6 * s + k * 12 * s, col, a, 3 * s)


def ic_porque(c, cx, cy, s, a, col):
    rrect(c, cx - 30 * s, cy - 26 * s, 60 * s, 44 * s, 12 * s, mix("#FFFFFF", col, 0.25), a, stroke=3 * s, stroke_color=col)
    p = skia.Path(); p.moveTo(cx - 10 * s, cy + 16 * s); p.lineTo(cx - 18 * s, cy + 30 * s); p.lineTo(cx + 2 * s, cy + 17 * s)
    c.drawPath(p, paint(col, a))
    text_mid(c, "?", cx, cy - 4 * s, 34 * s, "black", col, a)


def ic_nota(c, cx, cy, s, a, col):
    p = skia.Path()
    x0, x1, y0, y1 = cx - 22 * s, cx + 22 * s, cy - 30 * s, cy + 30 * s
    p.moveTo(x0, y0); p.lineTo(x1, y0); p.lineTo(x1, y1)
    for k in range(4):   # borda serrilhada
        p.lineTo(x1 - (k * 11 + 5.5) * s, y1 - 6 * s); p.lineTo(x1 - (k + 1) * 11 * s, y1)
    p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(col, a, stroke=3 * s))
    for k in range(3):
        line(c, x0 + 8 * s, y0 + 12 * s + k * 10 * s, x1 - (8 + 8 * (k % 2)) * s, y0 + 12 * s + k * 10 * s, col, a, 2.5 * s)
    for k in range(7):
        c.drawRect(skia.Rect.MakeXYWH(x0 + 9 * s + k * 4 * s, y0 + 44 * s, (1.5 if k % 2 else 2.5) * s, 8 * s), paint(INK, a * 0.8))


def ic_produto(c, cx, cy, s, a, col):
    """liquidificador funcionando (copo + base + ondas de movimento)"""
    p = skia.Path()
    p.moveTo(cx - 18 * s, cy - 28 * s); p.lineTo(cx + 18 * s, cy - 28 * s); p.lineTo(cx + 12 * s, cy + 6 * s)
    p.lineTo(cx - 12 * s, cy + 6 * s); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.22), a))
    c.drawPath(p, paint(col, a, stroke=3 * s))
    rrect(c, cx - 18 * s, cy + 6 * s, 36 * s, 22 * s, 5 * s, col, a)
    c.drawCircle(cx, cy + 17 * s, 4 * s, paint("#FFFFFF", a))
    for k, dx in enumerate((-30, 30)):
        for j in range(2):
            x = cx + dx * s + (j * 7 if dx > 0 else -j * 7) * s
            line(c, x, cy - 18 * s, x, cy - 4 * s, col, a * (0.9 - 0.35 * j), 2.5 * s)


def ic_recibo(c, cx, cy, s, a, col):
    rrect(c, cx - 26 * s, cy - 30 * s, 52 * s, 60 * s, 4 * s, "#FFFFFF", a, stroke=3 * s, stroke_color=col)
    for k in range(2):
        line(c, cx - 18 * s, cy - 18 * s + k * 10 * s, cx + 16 * s - k * 10 * s, cy - 18 * s + k * 10 * s, col, a * 0.7, 2.5 * s)
    p = skia.Path(); p.moveTo(cx - 18 * s, cy + 14 * s)
    p.cubicTo(cx - 10 * s, cy, cx - 6 * s, cy + 24 * s, cx + 2 * s, cy + 10 * s)
    p.cubicTo(cx + 8 * s, cy + 2 * s, cx + 10 * s, cy + 20 * s, cx + 20 * s, cy + 8 * s)
    c.drawPath(p, paint(col, a, stroke=3 * s, cap_round=True))
    line(c, cx - 20 * s, cy + 22 * s, cx + 20 * s, cy + 22 * s, col, a * 0.5, 2 * s)


ICON_ETAPA = dict(topico=ic_etiqueta, argumento=ic_porque, repertorio=ic_nota, analise=ic_produto, fechamento=ic_recibo)


def icone_etapa(c, key, cx, cy, a, s=1.0, lit=True, disc=True):
    if a <= 0:
        return
    col = PARTE[key] if lit else LIGHT
    if disc:
        c.drawCircle(cx, cy, 46 * s, paint(mix("#FFFFFF", col, 0.14), a))
    ICON_ETAPA[key](c, cx, cy, s, a, col)


def ficha_entrega(c, x, y, w, a, show=None, lit=None, ok=None, falta=None, perguntas=0.0, partes=1.0, keys=None, rowh=96,
                  title="ENTREGA DO ITEM"):
    """ficha (checklist) das 5 etapas da entrega. show[k] = alpha de cada linha · lit[k] = destaque · ok[k] = ✓ verde ·
    falta[k] = ✗ vermelho · perguntas = alpha da pergunta de cada parte · partes = alpha do nome técnico. Retorna a altura."""
    if a <= 0:
        return 0
    keys = list(keys or KEYS)
    n = len(keys)
    show = show or [1.0] * n
    lit = lit or [0.0] * n
    ok = ok or [0.0] * n
    falta = falta or [0.0] * n
    h = 96 + n * rowh + 24
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 10, y + 10, w - 20, h - 20), 12, 12), paint(LIGHT, a, stroke=2))
    text(c, title, x + 36, y + 62, 20, "black", GRAY, a, align="left", tracking=2)
    yy = y + 96
    for k, key in enumerate(keys):
        col = PARTE[key]
        ra = a * clamp(show[k])
        line(c, x + 26, yy, x + w - 26, yy, LINE, a, 2)
        if ra > 0:
            if lit[k] > 0:
                rrect(c, x + 16, yy + 6, w - 32, rowh - 12, 12, mix("#FFFFFF", col, 0.14), ra * lit[k])
            icone_etapa(c, key, x + 70, yy + rowh / 2, ra, min(0.62, rowh / 150), disc=False)
            ty = yy + rowh / 2 + 10 if perguntas <= 0 else yy + rowh / 2 - 4
            text(c, ETAPA[key], x + 124, ty, min(30, rowh * 0.32), "black", col, ra, align="left", tracking=1)
            if perguntas > 0:
                text(c, "“" + PERGP[key] + "”", x + 124, yy + rowh / 2 + 28, 22, "bold", INK2, ra * perguntas, align="left")
            if partes > 0:
                pill(c, NOMEP[key], x + w - 40 - (70 if (ok[k] > 0 or falta[k] > 0) else 0), yy + rowh / 2, col, size=20,
                     a=ra * partes, anchor="right", bounds=(0, 1920))
            if ok[k] > 0:
                check_icon(c, x + w - 62, yy + rowh / 2, 22, ra * ok[k], GREEN)
            if falta[k] > 0:
                check_icon(c, x + w - 62, yy + rowh / 2, 22, ra * falta[k], RED, "x")
        yy += rowh
    return h


def mini_entrega(c, cx, cy, a, oks, s=1.0, keys=None, nomes=True):
    """checklist em miniatura das 5 etapas — oks[k]: 1 = presente (verde), 0 = ausente (vermelho), None = neutro"""
    if a <= 0:
        return
    keys = list(keys or KEYS)
    w, rh = 330 * s, 34 * s
    h = 14 * s + len(keys) * rh + 10 * s
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 10 * s, "#FFFFFF", a, shadow=True)
    for k, key in enumerate(keys):
        yy = y + 14 * s + k * rh
        o = oks[k] if k < len(oks) else None
        col = LIGHT if o is None else (GREEN if o else RED)
        rrect(c, x + 8 * s, yy + 3 * s, w - 16 * s, rh - 6 * s, 6 * s, mix("#FFFFFF", col, 0.18), a)
        ICON_ETAPA[key](c, x + 28 * s, yy + rh / 2, 0.3 * s, a, PARTE[key])
        if nomes:
            text(c, NOMEP[key], x + 50 * s, yy + rh / 2 + 6 * s, 16 * s, "black", INK2, a, align="left")
        if o is not None:
            check_icon(c, x + w - 24 * s, yy + rh / 2, 10 * s, a, col, "check" if o else "x")


def barras_peso(c, x, y, w, a, rowh=70, show=None, rotulos=1.0, aviso=1.0):
    """as 5 barras de peso típico (seção 02): a da análise é a mais longa"""
    show = show or [1.0] * 5
    for k, key in enumerate(KEYS):
        ak = a * clamp(show[k])
        if ak <= 0:
            continue
        yy = y + k * rowh
        text(c, NOMEP[key], x, yy + rowh * 0.5 + 9, 26, "black", PARTE[key], ak * rotulos, align="left")
        bw = (w - 260) * PESO[key] * ease_out(clamp(ak))
        rrect(c, x + 250, yy + rowh * 0.18, max(20, bw), rowh * 0.64, rowh * 0.2, PARTE[key], ak)
    pill(c, "proporção TÍPICA · não é regra", x + w, y + 5 * rowh + 30, AMBER, size=24, a=a * aviso, anchor="right",
         bounds=(0, 1920))


def faixas_paragrafo(c, x, y, w, size, lh, frases, keys, a, reveal=None, faixa=None, nums=True, col_txt=None, peso="bold"):
    """parágrafo com as frases numeradas [1]–[5], cada uma com faixa colorida da sua parte (faixa[k] 0–1).
    Retorna a lista de (y0, y1) de cada frase. Texto digitado (não manuscrito) para caber o parágrafo inteiro."""
    reveal = reveal or [1.0] * len(frases)
    faixa = faixa or [0.0] * len(frases)
    out, yy = [], y
    for k, s in enumerate(frases):
        lines = wrap(("[" + str(k + 1) + "] " if nums else "") + s, peso, size, w - 30)
        h = len(lines) * lh
        ak = a * clamp(reveal[k])
        if ak > 0:
            if faixa[k] > 0 and keys[k]:
                rrect(c, x - 14, yy - size - 4, w + 4, h + 10, 10, mix("#FFFFFF", PARTE[keys[k]], 0.16), ak * faixa[k])
                rrect(c, x - 14, yy - size - 4, 8, h + 10, 4, PARTE[keys[k]], ak * faixa[k])
            for j, ln in enumerate(lines):
                text(c, ln, x, yy + j * lh, size, peso, col_txt or INK, ak, align="left")
        out.append((yy - size, yy - size + h))
        yy += h + 6
    return out


def entrega_selo(c, x, y, a, rot=-4, size=24):
    """selo verde “MÉTODO, NÃO REGRA” (igual ao da série Introdução)"""
    selo(c, x, y, a, "MÉTODO, NÃO REGRA", GREEN, rot, size)


# ======================================================================
# textos EXATOS do material (Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html)
# ======================================================================

# seção 03 — tópicos frasais (tema 2020)
TOPICOS = [("A saúde mental é muito importante.", "vago: não anuncia argumento nem eixo", False),
           ("Existem muitas doenças mentais, como a depressão e a ansiedade.", "informativo: descreve o assunto, não defende nada", False),
           ("Em primeiro lugar, a desinformação sobre os transtornos mentais sustenta o estigma que os cerca.",
            "bom: conectivo de ordenação, eixo 1 e afirmação a provar", True),
           ("Além disso, representações midiáticas que associam o adoecimento psíquico à violência reforçam o preconceito.",
            "bom: conectivo de adição, eixo 2 e relação de causa", True)]
CONECTIVOS_ABERTURA = ["em primeiro lugar", "além disso", "ademais", "por outro lado"]

# seção 04 — o argumento
TOPICO_04 = "Em primeiro lugar, a desinformação sobre os transtornos mentais sustenta o estigma que os cerca."
ARGUMENTO_04 = ("Como pouco se discute saúde mental nas escolas e nas famílias, sintomas como a tristeza persistente ou a "
                "ansiedade intensa costumam ser interpretados como fraqueza de caráter, e não como condições que têm tratamento.")
ESTRATEGIAS = ["exemplos", "dados estatísticos", "pesquisas", "fatos comprováveis",
               "citações ou depoimentos de pessoas especializadas", "pequenas narrativas ilustrativas", "alusões históricas",
               "comparações entre fatos, situações, épocas ou lugares"]

# seção 05 — o repertório
REPERTORIO_DEF = ("informação, fato, citação ou experiência vivida que, relacionada ao tema, contribui como argumento")
ORIENTACOES_2026 = ["escolher referências específicas que realmente tenham relação com o tema",
                    "articular o repertório às ideias usadas para defender o ponto de vista",
                    "mostrar que entende o conteúdo citado e que ele fortalece a tese"]
APRESENTAR = [("quem/o quê + conteúdo exato",
               "“Em O Alienista, de Machado de Assis, o médico Simão Bacamarte recolhe à Casa Verde a maior parte da "
               "população de Itaguaí…”"),
              ("lei + o que ela determina",
               "“A Lei nº 10.216/2001, que trata dos direitos das pessoas com transtornos mentais, redirecionou o modelo de "
               "assistência em saúde mental…”"),
              ("fato histórico + data segura", "“Promulgada em 1988, a Constituição Federal…”")]

# seção 06 — a análise (degraus e perguntas)
DEGRAUS = [("O QUE A REFERÊNCIA MOSTRA", "O Alienista: o rótulo de “louco” servia para excluir", "parar aqui = citar"),
           ("COMO ISSO APARECE NO BRASIL HOJE", "quem sofre psiquicamente ainda é afastado, e não cuidado", ""),
           ("O QUE ISSO PROVA PARA A TESE", "o medo do julgamento adia a busca por tratamento", "chegar aqui = argumentar")]
PERGUNTAS_ANALISE = [("Por que isso acontece?", "a causa do problema"),
                     ("Isso ainda vale no Brasil de hoje? Como?", "a atualização da referência"),
                     ("Quem é afetado, e de que forma?", "a consequência concreta"),
                     ("O que isso prova sobre a tese?", "a ligação com o ponto de vista")]

# seção 07 — fechamentos
FECHAMENTOS = [("Dessa forma, enquanto a informação não substituir o preconceito, o estigma continuará a afastar os "
                "brasileiros do tratamento.", "bom: retoma o eixo e o liga à tese", True),
               ("Assim, isso é um problema muito grave.", "vago: “isso” e “grave” não dizem nada sobre a tese", False),
               ("Além disso, a falta de psicólogos nas escolas também é um problema.",
                "abre assunto novo no lugar de fechar", False),
               ("Será que um dia isso vai mudar?", "pergunta retórica: não amarra o argumento", False)]
CONECTIVOS_FECHAMENTO = ["dessa forma", "assim", "desse modo", "logo", "por conseguinte"]

# seção 08 — parágrafo-modelo (eixo 1: desinformação)
MODELO = [
    "Em primeiro lugar, a desinformação sobre os transtornos mentais sustenta o estigma que os cerca.",
    "Como pouco se discute saúde mental nas escolas e nas famílias, sintomas como a tristeza persistente ou a ansiedade "
    "intensa costumam ser interpretados como fraqueza de caráter, e não como condições que têm tratamento.",
    "Essa confusão tem raízes antigas: em O Alienista, Machado de Assis satiriza o médico Simão Bacamarte, que, com critérios "
    "arbitrários, recolhe à Casa Verde a maior parte da população de Itaguaí, mostrando como o rótulo de “louco” podia servir "
    "para excluir.",
    "Mais de um século depois, os critérios mudaram, mas a lógica persiste: quem sofre psiquicamente ainda é visto como "
    "alguém a ser afastado, e não cuidado, o que leva muitos a adiar a busca por ajuda por medo do julgamento.",
    "Dessa forma, enquanto a informação não substituir o preconceito, o estigma continuará a afastar os brasileiros do "
    "tratamento.",
]
MODELO_OBS = ["conectivo de ordenação + eixo 1 da tese (desinformação)",
              "causa (“como pouco se discute”) e efeito (leitura de fraqueza)",
              "obra de domínio público, atribuição correta, conteúdo resumido em paráfrase",
              "atualiza a referência (“mais de um século depois”) e mostra a consequência concreta",
              "retoma o eixo e o liga à tese, sem informação nova"]

# seção 09 — versões fracas (eixo 1)
V1_OPINIAO = ("Em primeiro lugar, a desinformação é um grande problema. Muitas pessoas não sabem nada sobre doenças mentais e "
              "isso é muito ruim. As pessoas deveriam se informar mais. Dessa forma, a desinformação precisa acabar.")
V2_SOLTO = ("Em primeiro lugar, a desinformação sustenta o estigma. Machado de Assis escreveu O Alienista, obra muito "
            "importante da literatura brasileira. Dessa forma, o estigma das doenças mentais continua no Brasil.")

# seção 10 — rascunho em cinco linhas (eixo 2: mídia)
RASCUNHO = [("Tópico", "além disso, a mídia associa transtorno a violência", "topico"),
            ("Por quê", "noticiário e ficção destacam casos extremos → imagem de perigo", "argumento"),
            ("Repertório", "um exemplo que eu conheça de fato (série, filme, cobertura jornalística)", "repertorio"),
            ("Análise", "o público passa a temer quem tem diagnóstico → isolamento, silêncio", "analise"),
            ("Fecho", "assim, a mídia reforça o estigma que afasta do tratamento", "fechamento")]
MARCADOR_REP = "[aqui entra um exemplo que VOCÊ conhece de fato]"


# ======================================================================
# blocos-padrão
# ======================================================================

def cta_dev(c, t, C, sid, pergunta):
    """CTA padrão com flashcards: cena com cues {like}{sub}{bell}{com}{anki}{bye}"""
    cta_intro(c, t, C, sid, pergunta)


def tese_card(c, x, y, w, a, eixos=0.0, size=30, titulo="A TESE · ENEM 2020"):
    """a tese do estigma (fio das séries) com os 2 eixos marcados: desinformação (eixo 1) e mídia (eixo 2)"""
    if a <= 0:
        return 0
    lines = wrap("“" + TESE20 + "”", "bold", size, w - 60)
    h = 80 + len(lines) * (size + 10) + (70 if eixos > 0 else 20)
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, 10, h, 5, MOV["tese"], a)
    text(c, titulo, x + 36, y + 46, 20, "black", MOV["tese"], a, align="left", tracking=2)
    for j, ln in enumerate(lines):
        text(c, ln, x + 36, y + 96 + j * (size + 10), size, "bold", INK, a, align="left")
    if eixos > 0:
        yy = y + 96 + len(lines) * (size + 10) + 16
        pill(c, "EIXO 1 · desinformação", x + 36, yy, PARTE["topico"], size=22, a=a * eixos, bounds=(0, 1920))
        pill(c, "EIXO 2 · mídia", x + 380, yy, PARTE["argumento"], size=22, a=a * eixos, bounds=(0, 1920))
    return h
