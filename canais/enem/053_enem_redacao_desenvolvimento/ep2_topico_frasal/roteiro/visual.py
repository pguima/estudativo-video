"""Visual — Redação ENEM, Desenvolvimento, Episódio 2: O tópico frasal (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): ícones e ficha das 5 etapas da entrega, tese do
estigma, rascunho com caligrafia, alternativas, recap, erros e CTA.
Novo aqui: a ETIQUETA DO ITEM em tamanho grande (etiqueta(): as vagas ficam em branco; as boas trazem "EIXO 1"/"EIXO 2"
e a afirmação a provar), a caixa com as etiquetas "coisa" × "item 1: liquidificador, 3 velocidades", as quatro frases
da tabela da seção 03 avaliadas ao vivo no rascunho, o teste do tópico frasal (a redação some e ficam só a tese, T1 e
T2 ligados por uma linha), os conectivos de abertura por relação de sentido e as Questões 1 e 3 (eixos marcados na tese).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep2_topico_frasal.mp4"

TOP = PARTE["topico"]           # azul do tópico frasal
COR_CON = "#0E8C9A"             # conectivo (azul-petróleo)
COR_EIXO = PARTE["topico"]      # eixo da tese
COR_AFI = "#D9480F"             # afirmação a provar


# ======================================================================
# utilidades novas: etiqueta grande, texto com trechos coloridos, mini-redação
# ======================================================================

def tag_shape(c, x, y, w, h, a, col, fill="#FFFFFF", sw=4, shadow=True):
    """etiqueta de item (bico à esquerda, furo e barbante)"""
    if a <= 0:
        return
    n = h * 0.36
    p = skia.Path()
    p.moveTo(x + n, y); p.lineTo(x + w - 14, y); p.quadTo(x + w, y, x + w, y + 14); p.lineTo(x + w, y + h - 14)
    p.quadTo(x + w, y + h, x + w - 14, y + h); p.lineTo(x + n, y + h); p.lineTo(x, y + h / 2); p.close()
    if shadow:
        c.save(); c.translate(0, 6)
        c.drawPath(p, paint("#000000", a * 0.08)); c.restore()
    c.drawPath(p, paint(fill, a))
    c.drawPath(p, paint(col, a, stroke=sw))
    c.drawCircle(x + n * 0.75, y + h / 2, min(12, h * 0.09), paint(BG, a))
    c.drawCircle(x + n * 0.75, y + h / 2, min(12, h * 0.09), paint(col, a, stroke=3))


def etiqueta_item(c, x, y, w, h, a, fields=None, col=None, blank=0.0, title=None, title_a=1.0):
    """etiqueta grande: fields = [(rótulo, valor, alpha, cor)] · blank = alpha das linhas vazias (etiqueta em branco)"""
    if a <= 0:
        return
    col = col or TOP
    tag_shape(c, x, y, w, h, a, col if not blank else LIGHT)
    x0 = x + h * 0.36 + 20
    if blank > 0:
        for j in range(2):
            line(c, x0 + 20, y + h * (0.38 + 0.28 * j), x + w - 40 - j * 90, y + h * (0.38 + 0.28 * j), LIGHT, a * blank, 6)
    if title and title_a > 0:
        pill(c, title, x0, y + 18 + max(20, h * 0.09) * 0.9, col, size=max(20, h * 0.09), a=a * title_a, bounds=(0, 1920))
    if fields:
        n = len(fields)
        top = y + (30 + max(20, h * 0.09) * 1.8 if title else 22)
        rowh = (y + h - 18 - top) / n
        for k, (lab, val, fa, fcol) in enumerate(fields):
            if fa <= 0:
                continue
            ls, vs = max(18, h * 0.085), max(24, h * 0.12)
            yy = top + rowh * k + rowh / 2 + vs * 0.35
            text(c, lab, x0, yy, ls, "black", GRAY, a * fa, align="left", tracking=1.5)
            text(c, val, x0 + text_w(lab, "black", ls) + 26, yy + 1, vs, "black", fcol, a * fa, align="left")


def rich(c, segs, x, y, size, maxw, lh, a, peso="bold", align="left"):
    """parágrafo com trechos coloridos: segs = [(texto, cor, alpha_cor, cor_fundo|None, alpha_fundo)]. Retorna nº linhas."""
    words = []
    for s, col, ca, bg, ba in segs:
        for w_ in s.split():
            words.append((w_, col, ca, bg, ba))
    lines, cur, cw = [], [], 0
    sp = text_w(" ", peso, size)
    for wd in words:
        ww = text_w(wd[0], peso, size)
        if cur and cw + sp + ww > maxw:
            lines.append((cur, cw)); cur, cw = [], 0
        cw = cw + (sp if cur else 0) + ww
        cur.append((wd, ww))
    if cur:
        lines.append((cur, cw))
    if a <= 0:
        return len(lines)
    for k, (ln, lw) in enumerate(lines):
        xx = x - lw / 2 if align == "center" else x
        yy = y + k * lh
        for j, ((s, col, ca, bg, ba), ww) in enumerate(ln):
            if bg and ba > 0:
                ext = sp if j < len(ln) - 1 else 0
                rrect(c, xx - 3, yy - size * 0.92, ww + ext + 6, size * 1.22, 6, mix("#FFFFFF", bg, 0.22), a * ba)
            text(c, s, xx, yy, size, peso, mix(INK, col, clamp(ca)), a, align="left")
            xx += ww + sp
    return len(lines)


RED_LINHAS = [("intro", 4), ("d1", 6), ("d2", 6), ("conc", 4)]


def redacao_mini(c, x, y, w, a, dim=0.0, hl_tese=0.0, hl_top=0.0, lh=24, gap=22):
    """folha de redação em miniatura (linhas cinza). Última linha da introdução = tese (laranja); 1ª linha de D1 e D2 =
    tópicos (azul). Retorna dict com o y de 'tese', 't1', 't2'."""
    pos = {}
    h = sum(n for _, n in RED_LINHAS) * lh + gap * 3 + 70
    if a > 0:
        rrect(c, x, y, w, h, 14, "#FFFFFF", a, shadow=True)
        text(c, "REDAÇÃO", x + 30, y + 40, 16, "black", LIGHT, a, align="left", tracking=2)
    yy = y + 70
    for key, n in RED_LINHAS:
        for j in range(n):
            ind = 40 if j == 0 else 0
            x1 = x + w - 40 - (120 if j == n - 1 else (j * 37) % 60)
            role = "tese" if key == "intro" and j == n - 1 else ("t1" if key == "d1" and j == 0 else
                                                                 ("t2" if key == "d2" and j == 0 else None))
            if role:
                pos[role] = yy
            col, aa = LIGHT, a * (1 - 0.8 * dim)
            if role == "tese" and hl_tese > 0:
                col, aa = mix(LIGHT, MOV["tese"], hl_tese), a
            if role in ("t1", "t2") and hl_top > 0:
                col, aa = mix(LIGHT, TOP, hl_top), a
            if a > 0:
                line(c, x + 30 + ind, yy, x1, yy, col, aa, 9 if role else 7)
            yy += lh
        yy += gap
    return pos


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], SERIE_SELO, "O TÓPICO FRASAL", BLUE)
    card(c, *CARD_R)
    aa, ab, ac, ad = (ep(t, C[f"01.{x}"], 0.5) for x in "abcd")
    pos = redacao_mini(c, 220, 190, 600, 1.0, dim=ab, hl_tese=aa, hl_top=ab)
    labs = [("tese", "TESE", MOV["tese"], aa), ("t1", "1ª FRASE · 2º PARÁGRAFO", TOP, ab),
            ("t2", "1ª FRASE · 3º PARÁGRAFO", TOP, ab)]
    ys = [250, 420, 590]
    for k, (role, lab, col, al) in enumerate(labs):
        if al <= 0:
            continue
        arrow(c, 830, pos[role], 960, ys[k] + 40, col, al, 4, 14, progress=al)
        rrect(c, 980, ys[k], 700, 90, 16, mix("#FFFFFF", col, 0.12), al, shadow=True)
        text_mid(c, lab, 1330, ys[k] + 45, 30, "black", col, al)
    if ac > 0:
        for k in range(2):
            y0, y1 = ys[k] + 92, ys[k + 1] - 2
            line(c, 1330, y0, 1330, y1, RED, ac, 5, dash=(10, 8))
            text_mid(c, "?", 1380, (y0 + y1) / 2, 40, "black", RED, ac)
        text(c, "formam um raciocínio?", 1330, 735, 30, "black", INK2, ac)
    if ad > 0:
        selo(c, 1330, 795, ad, "O CORRETOR TAMBÉM NÃO ACHA", RED, -3, 26)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI ESCREVER", GREEN)
    aa, ab, ac = (ep(t, C[f"02.{x}"], 0.5) for x in "abc")
    text(c, "primeiras frases de parágrafo que…", W / 2, 260, 44, "black", INK, aa)
    etiqueta_item(c, 560, 320, 820, 300, aa, title="TÓPICO FRASAL",
                  fields=[("RETOMA:", "um EIXO da tese", ab, COR_EIXO), ("VAI PROVAR:", "o quê, exatamente", ac, COR_AFI)])
    pill(c, "cada palavra nova, explicada", W / 2, 740, BLUE, size=28, a=ep(t, C["02.d"], 0.4), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "EP. 1 + SÉRIE INTRODUÇÃO", PURPLE)
    aa = ep(t, C["03"] + 0.3, 0.5)
    shw = [ep(t, C["03"] + 0.6 + 0.25 * k, 0.4) for k in range(5)]
    ficha_entrega(c, 180, 175, 720, aa, show=shw, lit=[ep(t, C["03.b"], 0.4), 0, 0, 0, 0], partes=1.0, rowh=100,
                  title="CADA PARÁGRAFO ENTREGA UM ITEM")
    ab = ep(t, C["03.b"], 0.5)
    x, y, w, size = 970, 230, 770, 28
    tese_card(c, x, y, w, ab, eixos=0, size=size, titulo="A TESE · ENEM 2020")
    if ab > 0:
        n = len(wrap("“" + TESE20 + "”", "bold", size, w - 60))
        yy = y + 96 + n * (size + 10) + 16
        pill(c, "EIXO 1 · desinformação", x + 36, yy, PARTE["topico"], size=22, a=ab * ep(t, C["03.c"], 0.4), bounds=(0, 1920))
        pill(c, "EIXO 2 · mídia", x + 380, yy, PARTE["argumento"], size=22, a=ab * ep(t, C["03.d"], 0.4), bounds=(0, 1920))
        text(c, "eixo = cada caminho que sustenta a sua posição", x, yy + 90, 26, "black", BLUE, ab, align="left")


# ======================================================================
# a caixa e as duas etiquetas · a analogia
# ======================================================================

def barbante(c, x0, y0, x1, y1, a):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(x0, y0); p.quadTo((x0 + x1) / 2, max(y0, y1) + 60, x1, y1)
    c.drawPath(p, paint(mix(KRAFT, "#000000", 0.3), a, stroke=3))


def b_etiquetas(c, t, C, B):
    frame(c, t, B["start"], "UMA CAIXA, DOIS ITENS", "QUAL ETIQUETA DIZ O QUE CHEGOU?", BLUE)
    at = ep(t, C["04"], 0.5)
    caixa(c, 790, 500, 340, 240, at, open_=0.0)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        barbante(c, 690, 330, 800, 500, aa)
        tag_shape(c, 200, 240, 500, 190, aa, LIGHT)
        text(c, "coisa", 470, 360, 64, "black", GRAY, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        barbante(c, 1230, 330, 1120, 500, ab)
        tag_shape(c, 1220, 240, 520, 190, ab, TOP)
        pill(c, "ITEM 1", 1310, 280, TOP, size=22, a=ab, bounds=(0, 1920))
        text(c, "liquidificador,", 1310, 350, 40, "black", INK, ab, align="left")
        text(c, "3 velocidades", 1310, 400, 40, "black", INK, ab, align="left")
    ac = ep(t, C["04.c"], 0.5)
    pill(c, "qual você entende ANTES de abrir?", W / 2, 795, BLUE, size=30, a=ac, anchor="center", bounds=(0, 1920))
    if ac > 0:
        text_mid(c, "?", 450, 490, 60, "black", RED, ac)
        check_icon(c, 1480, 490, 30, ac, GREEN)


def b_analogia(c, t, C, B):
    frame(c, t, B["start"], "A ANALOGIA DA SÉRIE", "A ETIQUETA DO ITEM", BLUE)
    at = ep(t, C["05"], 0.5)
    tag_shape(c, 200, 230, 620, 230, at, TOP)
    if at > 0:
        pill(c, "ITEM 1", 300, 280, TOP, size=22, a=at, bounds=(0, 1920))
        text(c, "liquidificador,", 300, 360, 44, "black", INK, at, align="left")
        text(c, "3 velocidades", 300, 418, 44, "black", INK, at, align="left")
    aa = ep(t, C["05.a"], 0.5)
    text(c, "=", 900, 380, 80, "black", GRAY, aa)
    text(c, "TÓPICO FRASAL", 1000, 370, 66, "black", TOP, aa, align="left")
    text(c, "no parágrafo de desenvolvimento", 1000, 420, 28, "bold", INK2, aa, align="left")
    text(c, "ELE DIZ:", 220, 545, 22, "black", GRAY, ep(t, C["05.b"], 0.4), align="left", tracking=2)
    for k, (cue, s) in enumerate((("b", "QUAL ITEM da lista está chegando"), ("c", "O QUE ele vai provar"))):
        a, d = rise(t, C[f"05.{cue}"])
        check_icon(c, 245, 610 + k * 90 + d, 26, a, GREEN)
        text(c, s, 290, 624 + k * 90 + d, 42, "black", INK, a, align="left")
    a5 = ep(t, C["05.a"] + 0.8, 0.5)
    for k, key in enumerate(KEYS):
        icone_etapa(c, key, 1160 + k * 120, 720, a5 * (1 if k == 0 else 0.35), 0.75)
    text(c, "1ª etapa da entrega", 1160, 812, 26, "black", TOP, a5)


# ======================================================================
# bloco a: definição
# ======================================================================

def b_definicao(c, t, C, B):
    sid = which(t, C, ["06", "07"])
    head_seq(c, t, C, [("06", "BLOCO 1 · DEFINIÇÃO", "O QUE É O TÓPICO FRASAL", BLUE),
                       ("07", "BLOCO 1 · DEFINIÇÃO", "“EM GERAL, A PRIMEIRA”", AMBER)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "06":
        aa = ep(t, q("a"), 0.5)
        at = ep(t, q("t"), 0.5)
        if at > 0:
            boxed(c, 200, 195, 1520, 200, BLUE, at, 0.07)
            text(c, "TÓPICO FRASAL", 240, 240, 22, "black", BLUE, at, align="left", tracking=2)
            text_mid(c, "= ?", W / 2, 310, 70, "black", BLUE, at * (1 - aa))
        if aa > 0:
            para(c, "a frase, em geral a 1ª do parágrafo, que anuncia o ARGUMENTO que ele vai desenvolver", 240, 300, 40,
                 "black", INK, aa, 1440, 48)
        pill(c, "argumento = a razão que sustenta a sua posição", 200, 445, BLUE, size=28, a=ep(t, q("g"), 0.4),
             bounds=(0, 1920))
        text(c, "ela faz 2 coisas:", 200, 530, 32, "black", INK2, ep(t, q("b"), 0.4), align="left")
        for k, (cue, s, col) in enumerate((("c", "retoma UM EIXO da introdução", COR_EIXO),
                                           ("d", "diz O QUE o parágrafo vai provar", COR_AFI))):
            a, d = rise(t, q(cue))
            x = 200 + k * 780
            if a > 0:
                rrect(c, x, 570 + d, 740, 220, 20, mix("#FFFFFF", col, 0.08), a, shadow=True)
            badge_num(c, k + 1, x + 60, 640 + d, a, 30, bg=col)
            para(c, s, x + 110, 652 + d, 34, "black", col, a, 600, 42)
            if k == 0:
                pill(c, "EIXO 1", x + 110, 740 + d, PARTE["topico"], size=20, a=a, bounds=(0, 1920))
                pill(c, "EIXO 2", x + 240, 740 + d, PARTE["argumento"], size=20, a=a, bounds=(0, 1920))
            else:
                pill(c, "afirmação a provar", x + 110, 740 + d, COR_AFI, size=20, a=a, bounds=(0, 1920))
        return
    at = ep(t, q("t"), 0.5)
    s1, s2 = "“em geral", ", a primeira”"
    sz = 72
    w1, w2 = text_w(s1, "black", sz), text_w(s2, "black", sz)
    x0 = W / 2 - (w1 + w2) / 2
    text(c, s1, x0, 320, sz, "black", AMBER, at, align="left")
    text(c, s2, x0 + w1, 320, sz, "black", INK, at, align="left")
    underline(c, x0 + 30, x0 + w1, 340, AMBER, at, ep(t, q("t") + 0.6, 0.6), 8)
    aa = ep(t, q("a"), 0.4)
    check_icon(c, 300, 450, 26, aa, GREEN)
    text(c, "1ª frase = o lugar MAIS COMUM", 345, 462, 38, "black", GREEN, aa, align="left")
    ab = ep(t, q("b"), 0.4)
    check_icon(c, 300, 540, 26, ab, PURPLE, "x")
    text(c, "não é regra oficial", 345, 552, 38, "black", PURPLE, ab, align="left")
    entrega_selo(c, 1400, 500, ep(t, q("c"), 0.4), -5, 40)
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        boxed(c, 220, 630, 1480, 150, GREEN, ad, 0.07)
        icone_etapa(c, "topico", 320, 705, ad, 0.9)
        text(c, "abrir pela etiqueta: o leitor sabe logo o que chegou", 400, 717, 36, "black", GREEN, ad, align="left")


# ======================================================================
# bloco b: eu faço — as quatro frases da tabela no rascunho
# ======================================================================

PX, PY, PW, PH = 150, 160, 1620, 680
HX, HS, HLH, HMW = 260, 34, 42, 960
ROW_Y = [PY + 190, PY + 318, PY + 446, PY + 574]
TAG_X, TAG_W, TAG_H = 1250, 490, 110
EIXO_V = [("—", "—"), ("—", "—"), ("1 · desinformação", "sustenta o estigma"), ("2 · mídia", "reforça o preconceito")]
AV_COL = [RED, RED, GREEN, GREEN]
CON_TXT = [None, None, "Em primeiro lugar,", "Além disso,"]
CALLOUT = {"08": ("ESTIGMA", "marca de preconceito colada em alguém"),
           "11": ("CONECTIVO DE ORDENAÇÃO", "liga partes do texto · marca a posição"),
           "12": ("CONECTIVO DE ADIÇÃO", "acrescenta mais uma razão")}
EU_IDS = ["08", "09", "10", "11", "12"]


def b_eufaco(c, t, C, B):
    sid = which(t, C, EU_IDS)
    head_seq(c, t, C, [("08", "EU FAÇO · AO VIVO", "4 CANDIDATAS · ENEM 2020", GREEN),
                       ("09", "CANDIDATA 1 DE 4", "QUE EIXO? O QUE PROVA?", GREEN),
                       ("10", "CANDIDATA 2 DE 4", "QUE EIXO? O QUE PROVA?", GREEN),
                       ("11", "CANDIDATA 3 DE 4", "QUE EIXO? O QUE PROVA?", GREEN),
                       ("12", "CANDIDATA 4 DE 4", "QUE EIXO? O QUE PROVA?", GREEN)])
    a = ep(t, C["08"], 0.5)
    paper(c, PX, PY, PW, PH, a, lh=HLH, top=ROW_Y[0] - 12 - 3 * HLH)
    aa = ep(t, C["08.a"], 0.4)
    text(c, "ENEM 2020 · “" + TEMA20 + "”", PX + 110, PY + 58, 22, "black", BLUE, aa, align="left")
    ae = ep(t, C["08.a"] + 0.8, 0.4)
    pill(c, "EIXO 1 · desinformação", PX + 110, PY + 106, PARTE["topico"], size=22, a=ae, bounds=(0, 1920))
    pill(c, "EIXO 2 · mídia", PX + 450, PY + 106, PARTE["argumento"], size=22, a=ae, bounds=(0, 1920))
    # callout de definição (canto superior direito)
    if sid in CALLOUT:
        cue = {"08": "08.b", "11": "11.c", "12": "12.c"}[sid]
        ak = ep(t, C[cue], 0.4) * (1 - prog(t, C[sid + ".end"] - 0.3, 0.3))
        if ak > 0:
            lab, s = CALLOUT[sid]
            cx0 = PX + 110 + text_w("ENEM 2020 · “" + TEMA20 + "”", "black", 22) + 30
            rrect(c, cx0, PY + 22, PX + PW - 20 - cx0, 108, 14, mix("#FFFFFF", BLUE, 0.10), ak, shadow=True)
            text(c, lab, cx0 + 22, PY + 60, 18, "black", BLUE, ak, align="left", tracking=1.5)
            text(c, s, cx0 + 22, PY + 104, 26, "black", INK, ak, align="left")
    # cena 08: a etiqueta-modelo com as duas perguntas
    if sid == "08":
        ac = ep(t, C["08.c"], 0.4)
        for k in range(4):
            badge_num(c, k + 1, PX + 40, ROW_Y[k] - 10, ac, 18, bg=LIGHT)
        aq = ep(t, C["08.q1"], 0.4)
        etiqueta_item(c, 520, 380, 860, 300, aq, title="A ETIQUETA DE CADA CANDIDATA",
                      fields=[("EIXO:", "que eixo você retoma?", aq, COR_EIXO),
                              ("PROVA:", "o que você vai provar?", ep(t, C["08.q2"], 0.4), COR_AFI)])
        return
    n_at = EU_IDS.index(sid) - 1
    for k in range(n_at + 1):
        s_ = TOPICOS[k][0]
        cid = EU_IDS[k + 1]
        cue = lambda x: C[f"{cid}.{x}"]
        y = ROW_Y[k]
        badge_num(c, k + 1, PX + 40, y - 10, 1, 18, bg=AV_COL[k] if t >= cue("v") else INK2)
        span = phrase_span(cid, s_, cue("s"), cue("s") + 3.5)
        nl = hand_para(c, s_, HX, y, HS, PEN, 1.0, HMW, HLH, wreveal(t, span))
        if CON_TXT[k]:
            uc = ep(t, cue("c"), 0.6)
            underline(c, HX, HX + hand_w(CON_TXT[k], HS), y + 9, COR_CON, 1.0, uc, 5)
        av = ep(t, cue("v"), 0.4)
        pill(c, TOPICOS[k][1], HX, y + nl * HLH - 6, AV_COL[k], size=20, a=av, bounds=(0, 1920))
        if k == 1:
            am = ep(t, cue("m"), 0.4) * (1 - av)
            pill(c, "parece melhor: traz exemplos", HX, y + nl * HLH - 6, AMBER, size=20, a=am, bounds=(0, 1920))
        ok = TOPICOS[k][2]
        a1, a2 = ep(t, cue("q1"), 0.4), ep(t, cue("q2"), 0.4)
        ta = max(a1, ep(t, cue("s"), 0.4) * 0.999)
        ev, pv = EIXO_V[k]
        etiqueta_item(c, TAG_X, y - 52, TAG_W, TAG_H, ta, col=TOP if ok else LIGHT,
                      fields=[("EIXO:", ev, a1, COR_EIXO if ok else RED), ("PROVA:", pv, a2, COR_AFI if ok else RED)])
        if not ok:
            ae = ep(t, cue("e"), 0.4)
            selo(c, TAG_X + 300, y - 2, ae, "“COISA”" if k == 0 else "EM BRANCO", RED, -6, 22)


# ======================================================================
# exemplo × contraexemplo
# ======================================================================

SEG_BOM = [[("Em primeiro lugar,", "con"), ("a desinformação sobre os transtornos mentais", "eixo"),
            ("sustenta o estigma que os cerca.", "afi")],
           [("Além disso,", "con"), ("representações midiáticas que associam o adoecimento psíquico à violência", "eixo"),
            ("reforçam o preconceito.", "afi")]]


def b_lado(c, t, C, B):
    head(c, t, B["start"], "LADO A LADO · MESMO TEMA", "EM BRANCO × COMPLETA", BLUE)
    for x in (160, 990):
        card(c, x, 150, 770, 690)
    aa = ep(t, C["13.a"], 0.4)
    pill(c, "ETIQUETAS EM BRANCO", 200, 205, RED, size=24, a=max(0.35, aa), bounds=(0, 1920))
    for k in range(2):
        y = 290 + k * 260
        para(c, "“" + TOPICOS[k][0] + "”", 200, y, 34, "bold", INK, 1.0, 690, 44)
        tag_shape(c, 200, y + 90, 300, 90, max(0.4, aa), LIGHT, shadow=False)
        if aa > 0:
            for j in range(2):
                line(c, 280, y + 122 + j * 26, 470 - j * 60, y + 122 + j * 26, LIGHT, aa, 5)
        text(c, TOPICOS[k][1].split(":")[0], 530, y + 146, 34, "black", RED, aa, align="left")
    ab = ep(t, C["13.b"], 0.4)
    pill(c, "ETIQUETAS COMPLETAS", 1030, 205, GREEN, size=24, a=max(0.35, ab), bounds=(0, 1920))
    cols = dict(con=COR_CON, eixo=COR_EIXO, afi=COR_AFI)
    cues = dict(con="13.b1", eixo="13.b2", afi="13.b3")
    lit = {k: ep(t, C[v], 0.4) for k, v in cues.items()}
    for k in range(2):
        y = 290 + k * 260
        segs = [(s, cols[r], lit[r], cols[r], lit[r]) for s, r in SEG_BOM[k]]
        n = rich(c, segs, 1030, y, 32, 700, 42, 1.0)
        yy = y + n * 42 + 8
        xx = 1030
        for r, lab in (("con", "conectivo"), ("eixo", f"eixo {k + 1}"), ("afi", "afirmação a provar")):
            x0, x1 = pill(c, lab, xx, yy, cols[r], size=21, a=lit[r], bounds=(0, 1920))
            xx += text_w(lab, "bold", 21) + 44
    ac = ep(t, C["13.c"], 0.4)
    pill(c, "mesmo tema · muda o TRABALHO da frase", W / 2, 800, BLUE, size=26, a=ac, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco c: o teste do tópico frasal
# ======================================================================

def b_teste(c, t, C, B):
    sid = which(t, C, ["14", "15"])
    head_seq(c, t, C, [("14", "BLOCO 2 · O TESTE DO TÓPICO FRASAL", "SÓ A TESE + OS TÓPICOS", GREEN),
                       ("15", "AO VIVO · TESTE DO TÓPICO FRASAL", "ENEM 2020", GREEN)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "14":
        aa, ab, ac, ad, ae, af = (ep(t, q(x), 0.5) for x in "abcdef")
        text(c, "TESTE DO TÓPICO FRASAL", 220, 215, 24, "black", GREEN, aa, align="left", tracking=2)
        pos = redacao_mini(c, 220, 240, 560, 1.0 - 0.35 * ac, dim=ab, hl_tese=ab, hl_top=ab, lh=21, gap=16)
        boxes = [("tese", "TESE", "a posição", MOV["tese"]), ("t1", "TÓPICO 1", "razão 1", TOP),
                 ("t2", "TÓPICO 2", "razão 2", TOP)]
        ys = [240, 390, 540]
        if ac > 0:
            line(c, 900, ys[0] + 55, 900, ys[2] + 55, GREEN, ac, 6, progress=ac)
        for k, (role, lab, sub, col) in enumerate(boxes):
            a = ep(t, q("c") + 0.25 * k, 0.4)
            if a <= 0:
                continue
            arrow(c, 790, pos[role], 860, ys[k] + 55, col, a * 0.8, 3, 12, progress=a)
            c.drawCircle(900, ys[k] + 55, 12, paint(col, a))
            rrect(c, 940, ys[k], 780, 110, 16, mix("#FFFFFF", col, 0.12), a, shadow=True)
            text(c, lab, 980, ys[k] + 68, 34, "black", col, a, align="left")
            text(c, sub, 1680, ys[k] + 68, 30, "black", INK2, a * ad, align="right")
        pill(c, "PROJETO DE TEXTO VISÍVEL  ✓", 1330, 710, GREEN, size=28, a=ae, anchor="center", bounds=(0, 1920))
        text(c, "projeto de texto = o plano da redação para defender a tese", 1330, 790, 26, "black", BLUE, af)
        return
    rows = [("TESE", TESE20, MOV["tese"]), ("T1", TOPICOS[2][0], TOP), ("T2", TOPICOS[3][0], TOP)]
    vagos = [None, TOPICOS[0][0], TOPICOS[1][0]]
    ae = ep(t, q("e"), 0.6)
    ys = [172, 390, 535]
    ad, af, ag = ep(t, q("d"), 0.4), ep(t, q("f"), 0.4), ep(t, q("g"), 0.4)
    lc = mix(GREEN, RED, ae)
    a_line = max(ep(t, q("c") + 0.5, 0.4), ae)
    if a_line > 0:
        line(c, 236, ys[0] + 60, 236, ys[2] + 60, lc, a_line, 6, dash=(12, 9) if ae > 0.5 else None)
    for k, (lab, s, col) in enumerate(rows):
        a = ep(t, q("abc"[k]), 0.4)
        if a <= 0:
            continue
        y = ys[k]
        h = 200 if k == 0 else 130
        rrect(c, 280, y, 1440, h, 16, mix("#FFFFFF", col, 0.08), a, shadow=True)
        c.drawCircle(236, y + 60, 16, paint(col if not (k and ae > 0.5) else GRAY, a))
        text(c, lab, 310, y + 38, 18, "black", col, a, align="left", tracking=2)
        if k == 0 or ae <= 0:
            para(c, s, 310, y + 80, 32, "bold", INK, a, 1380, 42)
        if k and ae > 0:
            if ae < 1:
                para(c, s, 310, y + 80, 32, "bold", INK, a * (1 - ae), 1380, 42)
            para(c, vagos[k], 310, y + 80, 32, "bold", GRAY, a * ae, 1380, 42)
    check_icon(c, 320, 715, 26, ad * (1 - ae), GREEN)
    text(c, "uma posição + duas razões: faz sentido SOZINHO", 362, 727, 36, "black", GREEN, ad * (1 - ae), align="left")
    check_icon(c, 320, 715, 26, af, RED, "x")
    text(c, "tópicos vagos: o raciocínio SOME", 362, 727, 36, "black", RED, af, align="left")
    pill(c, "= “revisão de coerência em dois minutos” · série Competência 3", W / 2, 795, PURPLE, size=26, a=ag,
         anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco d: o conectivo de abertura
# ======================================================================

def b_conectivo(c, t, C, B):
    sid = which(t, C, ["16", "17"])
    head_seq(c, t, C, [("16", "BLOCO 3 · O CONECTIVO DE ABERTURA", "A EXPRESSÃO QUE ABRE O PARÁGRAFO", BLUE),
                       ("17", "BLOCO 3 · O CONECTIVO DE ABERTURA", "PELA RELAÇÃO DE SENTIDO", GREEN)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "16":
        at = ep(t, q("t"), 0.4)
        text(c, "CONECTIVOS DE ABERTURA", W / 2, 235, 24, "black", GRAY, ep(t, q("a"), 0.4), tracking=2)
        xs = [370, 770, 1150, 1550]
        for k, cue in enumerate("bcde"):
            a, d = rise(t, q(cue))
            if at * (1 - a) > 0:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[k] - 150, 280, 300, 60), 22, 22),
                            paint(LIGHT, at * (1 - a), stroke=3))
                text_mid(c, "?", xs[k], 310, 34, "black", LIGHT, at * (1 - a))
            pill(c, CONECTIVOS_ABERTURA[k], xs[k], 310 + d, COR_CON, size=34, a=a, anchor="center", bounds=(0, 1920))
        af = ep(t, q("f"), 0.4)
        labs = ["introdução", "1º desenvolvimento", "2º desenvolvimento", "conclusão"]
        for k in range(4):
            a = ep(t, q("f") + 0.3 * k, 0.4)
            x = 220 + k * 380
            if a > 0:
                rrect(c, x, 430, 320, 150, 16, mix("#FFFFFF", BLUE, 0.06), a, shadow=True)
                for j in range(3):
                    line(c, x + 30, 490 + j * 26, x + 290 - j * 50, 490 + j * 26, LIGHT, a, 6)
                text(c, labs[k], x + 160, 465, 22, "black", INK2, a)
            if k < 3:
                arrow(c, x + 325, 505, x + 375, 505, GREEN, ep(t, q("f") + 0.3 * k + 0.3, 0.3), 5, 14)
        text(c, "PROGRESSÃO = o texto andando para a frente", W / 2, 650, 36, "black", GREEN, af)
        pill(c, "avaliado na Competência 4", W / 2, 750, PURPLE, size=30, a=ep(t, q("g"), 0.4), anchor="center",
             bounds=(0, 1920))
        return
    aa = ep(t, q("a"), 0.4)
    text_mid(c, "qualquer um serve?", W / 2, 255, 52, "black", INK2, ep(t, q("t"), 0.4) * (1 - aa))
    regra(c, "pela RELAÇÃO DE SENTIDO, não por hábito", 255, aa, 38, GREEN)
    cols = [("b", "ORDENA", ["em primeiro lugar"], BLUE, "1º · 2º · 3º"),
            ("c", "ACRESCENTA", ["além disso", "ademais"], COR_CON, "+"),
            ("d", "CONTRASTE", ["por outro lado"], AMBER, "⇄")]
    for k, (cue, lab, exs, col, sym) in enumerate(cols):
        a, d = rise(t, q(cue))
        x = 200 + k * 520
        if a <= 0:
            continue
        rrect(c, x, 350 + d, 480, 340, 20, mix("#FFFFFF", col, 0.08), a, shadow=True)
        text(c, lab, x + 240, 410 + d, 34, "black", col, a, tracking=2)
        if sym == "⇄":
            arrow(c, x + 170, 465 + d, x + 310, 465 + d, col, a, 6, 18)
            arrow(c, x + 310, 495 + d, x + 170, 495 + d, col, a, 6, 18)
        else:
            text(c, sym, x + 240, 505 + d, 50 if sym == "+" else 36, "black", col, a)
        for j, e in enumerate(exs):
            pill(c, e, x + 240, 570 + j * 56 + d, col, size=26, a=a, anchor="center", bounds=(0, 1920))
        if k == 2:
            text(c, "≠ simples acréscimo", x + 240, 660 + d, 28, "black", RED, a)
    pill(c, "série Conectivos aprofunda", W / 2, 775, BLUE, size=26, a=ep(t, q("e"), 0.4), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# recap, nós fazemos, erros
# ======================================================================

FRASES = ["Tópico frasal é a etiqueta do item: eixo + o que vou provar.",
          "Tese + tópicos em sequência: tem que fazer sentido sozinho.",
          "Conectivo pela relação, não por hábito."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("18", "30"), FRASES, cols=[TOP, GREEN, COR_CON])


def b_exercicio(c, t, C, B):
    sid = which(t, C, ["19", "20"])
    head_seq(c, t, C, [("19", "NÓS FAZEMOS", "TÓPICO FRASAL DO EIXO 2", AMBER), ("20", "NÓS FAZEMOS", "CONFERINDO", GREEN)])
    paper(c, PX, PY, PW, PH, 1.0, lh=56, top=PY + 330)
    a0 = ep(t, C["19.a"], 0.4)
    text(c, "A TESE · ENEM 2020", PX + 110, PY + 60, 18, "black", MOV["tese"], a0, align="left", tracking=2)
    para(c, "“" + TESE20 + "”", PX + 110, PY + 102, 28, "bold", INK, a0, 1440, 36)
    ab = ep(t, C["19.b"], 0.4)
    pill(c, "EIXO 1 · desinformação", PX + 110, PY + 212, LIGHT, size=24, a=a0, bounds=(0, 1920))
    pill(c, "EIXO 2 · mídia", PX + 470, PY + 212, PARTE["argumento"], size=28 if ab > 0.5 else 24, a=max(a0 * 0.5, ab),
         bounds=(0, 1920))
    ac = ep(t, C["19.c"], 0.4)
    pill(c, "+ conectivo de ADIÇÃO", PX + 760, PY + 212, COR_CON, size=28, a=ac, bounds=(0, 1920))
    if sid == "19":
        text(c, "seu tópico frasal:", PX + 110, PY + 318, 30, "black", GRAY, ab, align="left")
        pause_timer(c, t, C["19.p"] + 0.3, PX + PW - 120, PY + PH - 120)
        return
    span = phrase_span("20", TOPICOS[3][0], C["20.s"], C["20.k1"] - 0.4)
    hand_para(c, TOPICOS[3][0], PX + 110, PY + 380, 40, PEN, 1.0, 1400, 56, wreveal(t, span))
    ks = [("k1", "conectivo de adição", COR_CON), ("k2", "eixo 2 (mídia)", COR_EIXO), ("k3", "o que vai provar", COR_AFI)]
    for k, (cue, s, col) in enumerate(ks):
        a = ep(t, C["20." + cue], 0.4)
        x = PX + 130 + k * 470
        check_icon(c, x, PY + 560, 24, a, GREEN)
        text(c, s, x + 40, PY + 571, 32, "black", col, a, align="left")
    selo(c, PX + PW - 200, PY + 300, ep(t, C["20.d"], 0.4), "FUNCIONA ✓", GREEN, -5, 34)


ERROS = [("21", "Tópico que só DESCREVE o assunto: “Existem muitas doenças mentais…”", "a frase é verdadeira e fala do tema",
          "não defende nada: anuncie o argumento e o eixo"),
         ("22", "“Em primeiro lugar” no SEGUNDO parágrafo", "é o conectivo de abertura mais conhecido",
          "ele ordena (1º item): no 2º parágrafo, adição: “além disso”"),
         ("23", "“Por outro lado” sem contraste", "soa como “mais uma coisa a dizer”",
          "“por outro lado” anuncia contraste; para acrescentar, adição")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# Questão 1 (onde está o tópico frasal · Enem 2023)
# ======================================================================

Q1_FRASES = [("I", "No Brasil, a Constituição de 1988 declara homens e mulheres iguais em direitos e obrigações."),
             ("II", "Na prática, porém, o cuidado com filhos, idosos e doentes continua recaindo sobre as mulheres, sem "
                    "remuneração nem reconhecimento."),
             ("III", "Além disso, a herança de uma divisão de tarefas que atribui o cuidado ao feminino torna esse trabalho "
                     "invisível."),
             ("IV", "Essa herança se manifesta desde a infância, quando meninas são cobradas pelas tarefas domésticas de "
                    "que os meninos são dispensados.")]
Q1_ENUN = "A frase que funcionaria melhor como tópico frasal de um parágrafo sobre o eixo “herança cultural” é a"
ALT1 = [("A", "I, pois apresenta um repertório legal.", "25.A", "26.xa", "fundamentação de outro eixo", RED),
        ("B", "II, pois contrapõe a lei à realidade.", "25.B", "26.xb", "contraste lei × realidade (outro eixo)", RED),
        ("C", "IV, pois traz um exemplo do cotidiano.", "25.C", "26.xc", "exemplo: sustenta a III, não a anuncia", RED),
        ("D", "III, pois anuncia o argumento a ser desenvolvido e abre com conectivo de progressão.", "25.D", None, "",
         GREEN),
        ("E", "nenhuma, pois tópico frasal só pode ser uma pergunta.", "25.E", "26.xe", "inventa uma regra", RED)]


def q1_par(c, x, y, w, size, lh, a, alphas, hl=None, ok3=0.0, dim=0.0):
    """o parágrafo da Questão 1, uma frase por bloco (I)–(IV); hl[k] = destaque de leitura; ok3 = III em verde"""
    hl = hl or [0] * 4
    yy = y
    for k, (rn, s) in enumerate(Q1_FRASES):
        ak = a * alphas[k]
        lines = wrap(s, "bold", size, w - 70)
        h = len(lines) * lh
        if ak > 0:
            bg = GREEN if (k == 2 and ok3 > 0) else BLUE
            fa = ok3 if k == 2 else hl[k]
            if fa > 0:
                rrect(c, x - 12, yy - size - 6, w + 12, h + 12, 10, mix("#FFFFFF", bg, 0.16), ak * fa)
            col = INK if not (dim > 0 and k != 2) else mix(INK, LIGHT, dim)
            text(c, f"({rn})", x, yy, size, "black", GREEN if (k == 2 and ok3 > 0.5) else GRAY, ak, align="left")
            for j, ln in enumerate(lines):
                text(c, ln, x + 66, yy + j * lh, size, "bold", col, ak, align="left")
        yy += h + lh * 0.45
    return yy


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · ENEM 2023", "ONDE ESTÁ O TÓPICO FRASAL?", BLUE)
    card(c, *CARD_R)
    alt_on = ep(t, C["25"], 0.6)
    aa = ep(t, C["24.a"], 0.4)
    cues = [C[f"24.s{k + 1}"] for k in range(4)]
    alph = [ep(t, cu, 0.4) for cu in cues]
    ends = cues[1:] + [C["24.end"]]
    hl = [ep(t, cues[k], 0.3) * (1 - prog(t, ends[k] - 0.2, 0.3)) for k in range(4)]
    if alt_on < 1:
        a = 1 - alt_on
        text(c, "QUESTÃO 1 · Leia o parágrafo, escrito para o tema do Enem 2023:", 220, 225, 24, "black", GRAY,
             ep(t, C["24"], 0.4) * a, align="left")
        q1_par(c, 240, 305, 1440, 34, 46, a, alph, hl)
        text(c, PARAG_DIDATICO, 240, 805, 16, "medium", AMBER, aa * a, align="left")
    if alt_on <= 0:
        return
    a = alt_on
    ok = ep(t, C["26.a"], 0.5)
    text(c, "QUESTÃO 1 · ENEM 2023", 190, 215, 18, "black", GRAY, a, align="left", tracking=2)
    yy = q1_par(c, 190, 265, 880, 24, 31, a, [1] * 4, ok3=ok, dim=ok)
    para(c, Q1_ENUN, 190, yy + 22, 27, "black", INK, a, 880, 35)
    alts_panel(c, t, C, ALT1, 1110, 245, 630, 26, "26.ok", "D", 6, gap_why=34, why_size=20)
    pause_timer(c, t, C["25.end"] - 1.9, 990, 735)
    questao_rotulo(c, a)


# ======================================================================
# Questão 3 (o melhor tópico frasal · Enem 2021)
# ======================================================================

TESE21 = [("A falta de registro civil torna parte dos brasileiros invisível para o Estado, situação mantida", None),
          ("pela distância dos cartórios", "e1"), ("e", None), ("pela desinformação sobre a gratuidade do registro.", "e2")]
COR_E = dict(e1=PARTE["topico"], e2=PARTE["argumento"])
ALT3 = [("A", "Em primeiro lugar, a distância dos cartórios dificulta o registro em regiões isoladas.", "28.A", "29.xa",
         "repete o 1º eixo e usa “em primeiro lugar”", RED),
        ("B", "A cidadania é um direito de todos os seres humanos.", "28.B", "29.xb", "genérica: assunto amplo", RED),
        ("C", "Por fim, cabe ao governo resolver o problema do registro civil.", "28.C", "29.xc",
         "antecipa a proposta (papel da conclusão)", RED),
        ("D", "Muitos países têm sistemas eficientes de registro de nascimento.", "28.D", "29.xd",
         "sai do recorte brasileiro", RED),
        ("E", "Além disso, a desinformação sobre a gratuidade do registro afasta famílias de baixa renda dos cartórios.",
         "28.E", None, "", GREEN)]


def tese21(c, t, C, x, y, size, maxw, lh, a, quote=True):
    e = {k: ep(t, C[f"27.{k}"], 0.5) for k in ("e1", "e2")}
    segs = []
    for k, (s, r) in enumerate(TESE21):
        if quote and k == 0:
            s = "“" + s
        if quote and k == len(TESE21) - 1:
            s = s + "”"
        if r:
            segs.append((s, COR_E[r], e[r], COR_E[r], e[r]))
        else:
            segs.append((s, INK, 0, None, 0))
    return rich(c, segs, x, y, size, maxw, lh, a), e


def b_q3(c, t, C, B):
    sid = which(t, C, ["27", "28", "29"])
    head(c, t, B["start"], "QUESTÃO 3 · ENEM 2021", "O MELHOR TÓPICO FRASAL", BLUE)
    card(c, *CARD_R)
    if sid == "27":
        at = ep(t, C["27"], 0.4)
        text(c, "TEMA DO ENEM 2021", 220, 225, 18, "black", GRAY, at, align="left", tracking=2)
        text(c, "“" + TEMA21 + "”", 220, 262, 26, "bold", INK2, at, align="left")
        aa = ep(t, C["27.a"], 0.5)
        if aa > 0:
            rrect(c, 200, 300, 1520, 250, 18, "#FFFFFF", aa, shadow=True)
            rrect(c, 200, 300, 10, 250, 5, MOV["tese"], aa)
            text(c, "A TESE", 240, 345, 20, "black", MOV["tese"], aa, align="left", tracking=2)
        n, e = tese21(c, t, C, 240, 405, 36, 1440, 48, aa)
        pill(c, "EIXO 1 · distância dos cartórios", 220, 610, COR_E["e1"], size=26, a=e["e1"], bounds=(0, 1920))
        pill(c, "EIXO 2 · desinformação sobre a gratuidade", 800, 610, COR_E["e2"], size=26, a=e["e2"], bounds=(0, 1920))
        ar = ep(t, C["27.r"], 0.4)
        text(c, "registro civil = o registro oficial do nascimento", 220, 720, 30, "black", BLUE, ar, align="left")
        return
    text(c, "A TESE", 200, 210, 16, "black", MOV["tese"], 1, align="left", tracking=2)
    n, e = tese21(c, t, C, 200, 247, 24, 1520, 32, 1.0)
    yy = 247 + n * 32 + 4
    pill(c, "EIXO 1 · distância dos cartórios", 200, yy, COR_E["e1"], size=19, a=1, bounds=(0, 1920))
    pill(c, "EIXO 2 · desinformação sobre a gratuidade", 590, yy, COR_E["e2"], size=19, a=1, bounds=(0, 1920))
    aa = ep(t, C["28.a"], 0.4)
    text(c, "O tópico frasal mais adequado para o SEGUNDO parágrafo de desenvolvimento é:", 200, yy + 54, 28, "black",
         INK, aa, align="left")
    alts_panel(c, t, C, ALT3, 210, yy + 112, 1440, 26, "29.ok", "E", 6, gap_why=32, why_size=20)
    pause_timer(c, t, C["28.end"] - 1.9, 1660, yy + 30)
    questao_rotulo(c, aa)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ARGUMENTO E REPERTÓRIO", BLUE)
    items = [("a", "topico", "a ETIQUETA diz o que chegou"), ("b", "argumento", "POR QUE está na caixa"),
             ("c", "repertorio", "a NOTA FISCAL")]
    for k, (cue, key, s) in enumerate(items):
        a, d = rise(t, C[f"31.{cue}"])
        x = 460 + k * 500
        icone_etapa(c, key, x, 400 + d, a, 1.8)
        para(c, s, x, 560 + d, 34, "black", PARTE[key], a, 420, 42, align="center")
        if k == 0:
            check_icon(c, x + 80, 330 + d, 22, a, GREEN)
    pill(c, "Ep. 3 · ARGUMENTO e REPERTÓRIO", W / 2, 760, GREEN, size=30, a=ep(t, C["31.d"], 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "32", "Qual conectivo abre o seu 2º parágrafo?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, etiquetas=b_etiquetas, analogia=b_analogia,
              definicao=b_definicao, eufaco=b_eufaco, lado=b_lado, teste=b_teste, conectivo=b_conectivo, recap=b_recap,
              exercicio=b_exercicio, erros=b_erros, q1=b_q1, q3=b_q3, ponte=b_ponte, cta=b_cta)
