"""Visual — Redação ENEM, Desenvolvimento, Episódio 4: Análise e fechamento — o "e daí?" (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): ícones e ficha das 5 etapas da entrega, degraus, perguntas
de análise, fechamentos, conectivos, parágrafo-modelo, Versão 2, rascunho com caligrafia, alternativas, recap, erros e CTA.
Novo aqui: os dois entregadores (só a nota fiscal × o liquidificador ligado na cozinha do cliente + recibo), a ESCADA DE
TRÊS DEGRAUS com a pessoa que sobe e os selos CITOU (degrau 1) e ARGUMENTOU (degrau 3), o balão "E DAÍ?" depois de cada
referência, o RECIBO com campo de assinatura (fechamento), o salto repertório → fechamento (sinal de que falta análise),
o mapa dos conectivos (o "portanto" guardado para a conclusão) e a análise da Questão 2 elaborada para fins didáticos.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep4_analise_fechamento.mp4"
AN, FE, RP = PARTE["analise"], PARTE["fechamento"], PARTE["repertorio"]

# Questão 2 (seção 12) — parágrafo EXATO e a análise escrita na tela (elaborada para fins didáticos, sem dado novo)
Q2_PARAG = ["Em primeiro lugar, a concentração das salas de exibição limita o acesso ao cinema.",
            "Segundo o filme Cinema Paradiso, de Giuseppe Tornatore, a sala de cinema pode ser o centro da vida cultural "
            "de uma pequena cidade.",
            "Dessa forma, a concentração das salas é um problema."]
Q2_ANALISE = ["No Brasil, porém, muitas cidades do interior não têm sala de cinema.",
              "Sem ela, seus moradores ficam sem esse centro de vida cultural, e o acesso ao cinema fica longe de ser "
              "democrático."]
ANALISE_DIDATICA = "Análise elaborada para fins didáticos."


# ======================================================================
# componentes novos deste episódio
# ======================================================================

def edai(c, x, y, a, size=38, left=True, col=None):
    """balão “E DAÍ?” (a pergunta do cliente) — aparece depois de cada referência"""
    if a <= 0:
        return
    w = text_w("E DAÍ?", "bold", size) + 76
    s = 0.7 + 0.3 * ease_back(clamp(a))
    c.save(); c.translate(x, y); c.scale(s, s)
    bubble(c, "E DAÍ?", 0, 0, w, col or AN, a, left, size)
    c.restore()


def rich_para(c, segs, x, y, size, peso, maxw, lh, a, align="left"):
    """parágrafo com trechos coloridos/realçados: segs = [(texto, cor, cor_realce, alpha_realce)]. Retorna a altura."""
    words = []
    for s, col, hl, ha in segs:
        for w in s.split():
            words.append((w, col, hl, ha))
    sp = text_w(" ", peso, size)
    lines, cur, cw = [], [], 0
    for w in words:
        ww = text_w(w[0], peso, size)
        if cur and cw + sp + ww > maxw:
            lines.append((cur, cw)); cur, cw = [], 0
        cw = cw + (sp if cur else 0) + ww
        cur.append((w, ww))
    if cur:
        lines.append((cur, cw))
    if a > 0:
        for j, (ln, lw) in enumerate(lines):
            xx = x - lw / 2 if align == "center" else x
            yy = y + j * lh
            for k, ((s, col, hl, ha), ww) in enumerate(ln):
                if hl and ha > 0:
                    ext = sp if k < len(ln) - 1 and ln[k + 1][0][2] == hl else 0
                    rrect(c, xx - 4, yy - size * 0.92, ww + 8 + ext, size * 1.3, 6, mix("#FFFFFF", hl, 0.28), a * ha)
                text(c, s, xx, yy, size, peso, col or INK, a, align="left")
                xx += ww + sp
    return len(lines) * lh


def assinatura(c, x, y, w, a, prog_=1.0, col=None):
    """rubrica desenhada aos poucos (prog_ 0–1)"""
    if a <= 0 or prog_ <= 0:
        return
    n = 90
    pts = []
    for i in range(n + 1):
        u = i / n
        xx = x + w * u
        yy = y - 16 * math.sin(u * math.pi * 5.2) * (1 - 0.5 * u) - 10 * math.sin(u * math.pi * 1.3)
        pts.append((xx, yy))
    m = max(1, int(n * clamp(prog_)))
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:m + 1]:
        p.lineTo(*q)
    c.drawPath(p, paint(col or PEN, a, stroke=4, cap_round=True))


def recibo(c, x, y, w, h, a, linhas=(), assin=0.0, titulo="RECIBO DE ENTREGA", col=None, body=None, body_size=26):
    """recibo com campo de assinatura do cliente; linhas = [(rótulo, valor)]; body = texto livre no meio"""
    if a <= 0:
        return
    col = col or FE
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h)
    n = int(w // 28)
    for k in range(n):
        p.lineTo(x + w - (k + 0.5) * w / n, y + h - 12); p.lineTo(x + w - (k + 1) * w / n, y + h)
    p.close()
    shadow_rrect(c, x, y, w, h, 6, a)
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.5), a, stroke=2))
    rrect(c, x, y, w, 14, 0, col, a)
    text(c, titulo, x + w / 2, y + 62, 24, "black", col, a, tracking=3)
    line(c, x + 30, y + 86, x + w - 30, y + 86, LIGHT, a, 2, dash=[8, 6])
    yy = y + 132
    for lab, val in linhas:
        text(c, lab, x + 34, yy, 18, "black", GRAY, a, align="left", tracking=1.5)
        text(c, val, x + 34, yy + 36, 28, "black", INK, a, align="left")
        yy += 90
    if body:
        para(c, body, x + 34, yy, body_size, "bold", INK, a, w - 68, body_size * 1.3)
    fy = y + h - 70
    line(c, x + 34, fy, x + w - 34, fy, INK2, a, 2.5)
    text(c, "assinatura do cliente", x + 34, fy + 30, 18, "bold", GRAY, a, align="left")
    assinatura(c, x + 60, fy - 22, min(300, w - 140), a, assin)


def escada(c, x0, base, a, nivel, sw=200, sh=130, citou=0.0, argumentou=0.0, ps=0.8, show=(1, 1, 1)):
    """escada de 3 degraus (análise) com a pessoa que sobe: nivel 0 = chão · 1, 2, 3 = degraus"""
    if a <= 0:
        return
    for k in range(3):
        ak = a * clamp(show[k])
        if ak <= 0:
            continue
        top = base - (k + 1) * sh
        rrect(c, x0 + k * sw, top, sw, (k + 1) * sh, 8, mix("#FFFFFF", AN, 0.16 + 0.12 * k), ak)
        rrect(c, x0 + k * sw, top, sw, 12, 4, AN, ak)
        badge_num(c, k + 1, x0 + k * sw + 34, top + 42, ak, 22, bg=AN)
    line(c, x0 - 120, base, x0 + 3 * sw + 20, base, LIGHT, a, 4)
    # pessoa
    nv = clamp(nivel, 0, 3)
    k = min(2, int(nv)) if nv < 3 else 2
    f = nv - k if nv < 3 else 1.0

    def spot(j):
        if j == 0:
            return x0 - 60, base
        return x0 + (j - 1) * sw + sw / 2 + 10, base - j * sh
    xa, ya = spot(k)
    xb, yb = spot(k + 1)
    px = lerp(xa, xb, ease_io(f))
    py = lerp(ya, yb, ease_io(f)) - math.sin(math.pi * f) * 40
    person(c, px, py - 134 * ps, INK2, a, ps)
    # selos
    if citou > 0:
        selo(c, x0 + sw / 2 + 10, base - 34, a * citou, "CITOU", AMBER, -6, 26)
    if argumentou > 0:
        selo(c, x0 + 2 * sw + sw / 2, base - 40, a * argumentou, "ARGUMENTOU", GREEN, -6, 24)


def cliente(c, x, y, a, s=0.6, col=None):
    person(c, x, y, col or BLUE, a, s)


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], SERIE_SELO, "ANÁLISE E FECHAMENTO", AN)
    card(c, *CARD_R)
    aa, ab, ac, ad, ae = (ep(t, C[f"01.{x}"], 0.5) for x in "abcde")
    y0, h = 270, 230
    if aa > 0:
        rrect(c, 200, y0, 470, h, 20, mix("#FFFFFF", RP, 0.12), aa, shadow=True)
        icone_etapa(c, "repertorio", 280, y0 + 80, aa, 0.8, disc=False)
        text(c, "REPERTÓRIO", 340, y0 + 92, 30, "black", RP, aa, align="left", tracking=1)
        text(c, "Machado de Assis", 435, y0 + 170, 40, "black", INK, aa)
    if ab > 0:
        rrect(c, 1250, y0, 470, h, 20, mix("#FFFFFF", FE, 0.12), ab, shadow=True)
        icone_etapa(c, "fechamento", 1330, y0 + 80, ab, 0.8, disc=False)
        text(c, "FECHAMENTO", 1390, y0 + 92, 30, "black", FE, ab, align="left", tracking=1)
        para(c, "“Dessa forma, o problema é grave.”", 1485, y0 + 150, 32, "black", INK, ab, 420, 40, align="center")
    if ac > 0:
        selo(c, 960, 640, ac * (1 - ae), "ARGUMENTOU?", AMBER, -5, 40)
    # o meio do caminho
    if ad > 0:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(720, y0, 480, h), 20, 20)
        pp = paint(RED, ad * (1 - ae), stroke=4); pp.setPathEffect(skia.DashPathEffect.Make([16, 10], 0))
        c.drawRRect(r, pp)
        text_mid(c, "?", 960, y0 + h / 2 - 10, 90, "black", RED, ad * (1 - ae))
        text(c, "o meio do caminho", 960, y0 + h + 50, 30, "black", RED, ad * (1 - ae))
    if ae > 0:
        rrect(c, 720, y0, 480, h, 20, mix("#FFFFFF", AN, 0.16), ae, shadow=True)
        icone_etapa(c, "analise", 960, y0 + 80, ae, 0.9, disc=False)
        text(c, "ANÁLISE", 960, y0 + 185, 48, "black", AN, ae)
        pill(c, "o meio que vale mais", 960, 640, AN, size=32, a=ae, anchor="center", bounds=(0, 1920))
    for x0, x1, al in ((680, 712, ad), (1208, 1240, ad)):
        arrow(c, x0, y0 + h / 2, x1, y0 + h / 2, INK2, al, 4, 12)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "NESTA AULA", "AS DUAS ÚLTIMAS ETAPAS", GREEN)
    rows = [("02.a", "analise", "a ANÁLISE", "que faz a referência trabalhar"),
            ("02.b", "fechamento", "a FRASE FINAL", "que devolve o parágrafo para a tese")]
    for k, (cue, key, s1, s2) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + k * 220 + d
        icone_etapa(c, key, 380, y, a, 1.6)
        text(c, s1, 500, y - 4, 52, "black", PARTE[key], a, align="left")
        text(c, s2, 500, y + 50, 36, "bold", INK2, a, align="left")
    pill(c, "cada palavra nova, uma de cada vez", W / 2, 770, BLUE, size=28, a=ep(t, C["02.c"], 0.4), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "EPISÓDIO 3", PURPLE)
    aT, aa, ab, ac = (ep(t, C[f"03.{x}"], 0.4) for x in "tabc")
    lit = [0, aa * (1 - ab), ab * (1 - ac), ac, ac]
    ficha_entrega(c, 180, 175, 900, aT, lit=lit, ok=[aa, aa, ab, 0, 0], partes=1.0, rowh=100)
    for k, (al, key, s1, s2) in enumerate(((aa, "argumento", "ARGUMENTO", "explica POR QUE a afirmação procede"),
                                           (ab, "repertorio", "REPERTÓRIO", "conhecimento de fora da prova que COMPROVA"))):
        y = 270 + k * 190
        text(c, s1, 1140, y, 34, "black", PARTE[key], al, align="left")
        para(c, s2, 1140, y + 50, 30, "bold", INK, al, 580, 38)
    if ac > 0:
        rrect(c, 1120, 640, 600, 130, 18, mix("#FFFFFF", AN, 0.12), ac, shadow=True)
        text(c, "HOJE", 1150, 690, 22, "black", AN, ac, align="left", tracking=2)
        text(c, "as duas últimas etapas", 1150, 740, 36, "black", INK, ac, align="left")


# ======================================================================
# os dois entregadores e a analogia
# ======================================================================

def b_entrega(c, t, C, B):
    frame(c, t, B["start"], "DOIS ENTREGADORES", "QUAL PROVOU A ENTREGA?", BLUE)
    q = lambda x: C[f"04.{x}"]
    aT = ep(t, q("t"), 0.5)
    text(c, "ENTREGADOR 1", 540, 240, 26, "black", GRAY, aT, tracking=2)
    text(c, "ENTREGADOR 2", 1380, 240, 26, "black", GRAY, aT, tracking=2)
    line(c, 960, 210, 960, 780, LINE, aT, 3)
    # 1: mostra a nota fiscal e vai embora
    aa = ep(t, q("a"), 0.5)
    if aa > 0:
        u = ep(t, q("a") + 1.6, 1.4)
        px = 470 + 260 * u
        person(c, px, 400, BLUE, aa * (1 - 0.75 * u), 1.0)
        icone_etapa(c, "repertorio", px + 110 - 40 * u, 470, aa * (1 - 0.75 * u), 1.2, disc=False)
        text(c, "mostra a nota fiscal…", 540, 650, 32, "black", RP, aa)
        text(c, "…e vai embora", 540, 700, 32, "black", INK2, ep(t, q("a") + 1.6, 0.4))
    # 2: liga o liquidificador na cozinha do cliente
    ab = ep(t, q("b"), 0.5)
    if ab > 0:
        rrect(c, 1040, 566, 680, 22, 6, mix("#FFFFFF", GRAY, 0.4), ab)        # bancada
        person(c, 1110, 400, BLUE, ab, 0.9)
        cliente(c, 1620, 400, ab, 0.9, PURPLE)
        text(c, "cliente", 1620, 548, 22, "black", PURPLE, ab)
        sh = math.sin(t * 40) * 2.5 * ab
        icone_etapa(c, "analise", 1370 + sh, 500, ab, 2.2, disc=False)
        text(c, "liga na cozinha do cliente", 1380, 700, 30, "black", AN, ab)
    acc = ep(t, q("c"), 0.4)
    pill(c, "resolve o problema DELE ✓", 1380, 300, GREEN, size=26, a=acc * (1 - ep(t, q("d"), 0.3)), anchor="center",
         bounds=(0, 1920))
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        icone_etapa(c, "fechamento", 1620, 290, ad, 0.9)
        assinatura(c, 1590, 312, 60, ad, ep(t, q("d") + 0.3, 1.0), FE)
        text(c, "recibo assinado", 1440, 302, 26, "black", FE, ad, align="right")
    ae = ep(t, q("e"), 0.4)
    if ae > 0:
        check_icon(c, 400, 770, 26, ae, RED, "x")
        text(c, "só a nota", 440, 781, 28, "black", RED, ae, align="left")
        check_icon(c, 1230, 770, 26, ae, GREEN)
        text(c, "provou que o item serve", 1270, 781, 28, "black", GREEN, ae, align="left")


def b_analogia(c, t, C, B):
    frame(c, t, B["start"], "A ANALOGIA DA SÉRIE", "PRODUTO FUNCIONANDO · RECIBO", BLUE)
    q = lambda x: C[f"05.{x}"]
    aT, aa, ab, ac = (ep(t, q(x), 0.4) for x in "tabc")
    ficha_entrega(c, 170, 175, 820, aT, lit=[0, 0, 0, aa, ab], partes=1.0, rowh=100, show=[0.45, 0.45, 0.45, 1, 1])
    if aa > 0:
        rrect(c, 1040, 200, 690, 250, 20, mix("#FFFFFF", AN, 0.10), aa, shadow=True)
        text(c, "ANÁLISE", 1080, 260, 30, "black", AN, aa, align="left", tracking=2)
        para(c, "o produto funcionando na casa do cliente", 1080, 320, 34, "black", INK, aa, 620, 42)
        pill(c, "no Brasil de hoje", 1080, 410, AN, size=24, a=aa, bounds=(0, 1920))
    if ab > 0:
        rrect(c, 1040, 480, 690, 250, 20, mix("#FFFFFF", FE, 0.10), ab, shadow=True)
        text(c, "FECHAMENTO", 1080, 540, 30, "black", FE, ab, align="left", tracking=2)
        para(c, "a assinatura do recibo: amarra o item entregue à tese", 1080, 600, 34, "black", INK, ab, 620, 42)
    if ac > 0:
        edai(c, 560, 450, ac, 40)


# ======================================================================
# bloco a: o que é análise · o que a Cartilha elogia
# ======================================================================

def b_analise(c, t, C, B):
    sid = which(t, C, ["06", "07"])
    head_seq(c, t, C, [("06", "A ANÁLISE", "O QUE TRANSFORMA CITAÇÃO EM ARGUMENTO?", AN),
                       ("07", "A ANÁLISE", "O QUE A CARTILHA ELOGIA", PURPLE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "06":
        aa = ep(t, q("a"), 0.4)
        if aa > 0:
            boxed(c, 200, 200, 1520, 170, BLUE, aa, 0.07)
            text(c, "ANÁLISE  (ou APROFUNDAMENTO)", 240, 255, 26, "black", BLUE, aa, align="left", tracking=2)
            text(c, "interpretar o repertório à luz do problema", 240, 330, 46, "black", INK, aa, align="left")
        for k, (cue, s1, s2) in enumerate((("b", "o que ele mostra sobre a ", "REALIDADE BRASILEIRA"),
                                            ("c", "por que isso ", "SUSTENTA A TESE"))):
            a, d = rise(t, q(cue))
            y = 450 + k * 90 + d
            badge_num(c, k + 1, 240, y - 12, a, 24, bg=AN)
            text(c, s1, 290, y, 38, "bold", INK2, a, align="left")
            text(c, s2, 290 + text_w(s1, "bold", 38), y, 38, "black", AN, a, align="left")
        ad = ep(t, q("d"), 0.4)
        if ad > 0:
            icone_etapa(c, "analise", 270, 680, ad, 0.75)
            text(c, "é aqui que aparece a AUTORIA", 340, 672, 36, "black", AN, ad, align="left")
            text(c, "= dá para perceber o SEU raciocínio", 340, 718, 30, "bold", INK2, ad, align="left")
        pill(c, "como o corretor pontua: série Competência 3", 1700, 700, BLUE, size=22, a=ep(t, q("e"), 0.4),
             anchor="right", bounds=(0, 1920))
        return
    aT = ep(t, q("t"), 0.4)
    cartilha(c, 200, 220, aT, inep=aT, s=0.85)
    aa = ep(t, q("a"), 0.4)
    text(c, "COMENTÁRIO SOBRE UM USO PRODUTIVO DA CONSTITUIÇÃO DE 1988", 560, 250, 22, "black", PURPLE, aa, align="left",
         tracking=1)
    ab, ac, ad = (ep(t, q(x), 0.4) for x in "bcd")
    if ab > 0:
        boxed(c, 540, 280, 1180, 220, PURPLE, ab, 0.05)
        segs = [("o texto estabelece uma relação lógica entre o", INK, None, 0),
                ("antecedente histórico", INK, PURPLE, ab),
                ("e a", INK, None, 0), ("realidade atual,", INK, PURPLE, ac), ("evidenciando a", INK, None, 0),
                ("distância entre os direitos previstos e sua efetivação.", INK, RED, ad)]
        rich_para(c, segs, 580, 345, 34, "bold", 1100, 48, ab)
    # linha do tempo: passado → presente, com a distância
    if ab > 0:
        y = 640
        badge_num(c, "", 640, y, ab, 14, bg=PURPLE)
        text(c, "1988", 640, y - 40, 34, "black", PURPLE, ab)
        text(c, "antecedente histórico", 640, y + 50, 24, "black", INK2, ab)
        text(c, "= o fato do passado", 640, y + 84, 22, "bold", GRAY, ab)
    if ac > 0:
        arrow(c, 670, 640, 1210, 640, PURPLE, ac, 5, 18, progress=ac)
        badge_num(c, "", 1240, 640, ac, 14, bg=PURPLE)
        text(c, "HOJE", 1240, 600, 34, "black", PURPLE, ac)
        text(c, "realidade atual", 1240, 690, 24, "black", INK2, ac)
    if ad > 0:
        text(c, "direitos previstos", 1500, 600, 26, "black", INK, ad)
        line(c, 1400, 625, 1600, 625, INK, ad, 4)
        text(c, "efetivação", 1500, 700, 26, "black", INK, ad)
        line(c, 1400, 665, 1600, 665, INK, ad, 4)
        arrow(c, 1500, 632, 1500, 656, RED, ad, 4, 10)
        text(c, "a distância", 1640, 652, 22, "black", RED, ad, align="left")
    pill(c, "passado ligado ao presente = análise", 1700, 790, GREEN, size=26, a=ep(t, q("e"), 0.4), anchor="right",
         bounds=(0, 1920))


# ======================================================================
# bloco b: eu faço — a escada de três degraus no rascunho
# ======================================================================

EX0, EBASE = 230, 790
PPX, PPY, PPW, PPH = 900, 175, 860, 640
DLAB = [PPY + 150 + k * 160 for k in range(3)]


def b_escada(c, t, C, B):
    sid = which(t, C, ["08", "09", "10", "11"])
    head_seq(c, t, C, [("08", "EU FAÇO · AO VIVO", "A ESCADA DA ANÁLISE", GREEN),
                       ("09", "EU FAÇO · DEGRAU 1", "O QUE A REFERÊNCIA MOSTRA", GREEN),
                       ("10", "EU FAÇO · DEGRAU 2", "COMO ISSO APARECE NO BRASIL HOJE", GREEN),
                       ("11", "EU FAÇO · DEGRAU 3", "O QUE ISSO PROVA PARA A TESE", GREEN)])
    a0 = ep(t, C["08"], 0.5)
    lab = [ep(t, C[f"08.{x}"], 0.4) for x in "abc"]
    # pessoa: sobe um degrau em cada cena
    nivel = ep(t, C["09.c"], 0.9) + ep(t, C["10.b"], 0.9) + ep(t, C["11.b"], 0.9)
    citou = ep(t, C["09.d"], 0.4)
    argu = ep(t, C["11.c"], 0.4)
    escada(c, EX0, EBASE, a0, nivel, show=lab, citou=citou, argumentou=argu)
    # rascunho com os três degraus
    paper(c, PPX, PPY, PPW, PPH, a0, lh=40, top=PPY + 110)
    aref = ep(t, C["09.a"], 0.4)
    pill(c, "REFERÊNCIA", PPX + 110, PPY + 70, RP, size=20, a=aref, bounds=(0, 1920))
    text(c, "O Alienista, de Machado de Assis", PPX + 270, PPY + 78, 26, "black", INK, aref, align="left")
    spans = [(C["09.c"], C["09.d"] - 0.3), (C["10.b"], C["10.c"] - 0.3), (C["11.b"], C["11.c"] - 0.3)]
    for k, (titulo, frase, nota) in enumerate(DEGRAUS):
        y = DLAB[k]
        text(c, f"{k + 1} · {titulo}", PPX + 110, y, 22, "black", AN, a0 * lab[k], align="left", tracking=1.5)
        hand_para(c, frase, PPX + 110, y + 54, 31, PEN, a0, PPW - 150, 44, reveal=wreveal(t, spans[k]))
    pill(c, DEGRAUS[0][2], PPX + PPW - 30, DLAB[0] - 8, AMBER, size=18, a=citou, anchor="right", bounds=(0, 1920))
    pill(c, DEGRAUS[2][2], PPX + PPW - 30, DLAB[2] - 8, GREEN, size=18, a=argu, anchor="right", bounds=(0, 1920))
    # “e daí?” depois da referência
    ae = ep(t, C["09.e"], 0.4) * (1 - ep(t, C["10.b"], 0.4))
    edai(c, 560, 200, ae, 40)
    # atualização da referência
    au = ep(t, C["10.c"], 0.4) * (1 - ep(t, C["11.a"], 0.4))
    if au > 0:
        rrect(c, 170, 190, 690, 120, 16, mix("#FFFFFF", BLUE, 0.10), au, shadow=True)
        text(c, "ATUALIZAÇÃO DA REFERÊNCIA", 200, 238, 22, "black", BLUE, au, align="left", tracking=1.5)
        text(c, "= trazer a obra para o presente", 200, 285, 30, "bold", INK, au, align="left")
    ar = ep(t, C["11.d"], 0.4)
    if ar > 0:
        rrect(c, 160, 190, 500, 130, 16, "#FFFFFF", ar, shadow=True)
        text(c, "1º degrau = CITAR", 190, 242, 30, "black", AMBER, ar, align="left")
        text(c, "3º degrau = ARGUMENTAR", 190, 292, 30, "black", GREEN, ar, align="left")


# ======================================================================
# bloco c: as quatro perguntas de análise
# ======================================================================

GLOSA = ["a origem do problema", "trazer a referência para o presente", "o efeito na vida real das pessoas", ""]


def b_perguntas(c, t, C, B):
    head_seq(c, t, C, [("12", "QUANDO TRAVAR NA ESCADA", "4 PERGUNTAS DE ANÁLISE", GREEN),
                       ("13", "QUANDO TRAVAR NA ESCADA", "4 PERGUNTAS DE ANÁLISE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.4)
    text(c, "PERGUNTA DE ANÁLISE", 270, 230, 20, "black", GRAY, aa, align="left", tracking=2)
    text(c, "O QUE ELA PRODUZ", 1190, 230, 20, "black", GRAY, aa, align="left", tracking=2)
    ai = ep(t, C["12"], 0.4) * (1 - ep(t, C["12.b"], 0.4))
    if ai > 0:
        escada(c, 760, 760, ai, 1, sw=170, sh=110, ps=0.65)
        text_mid(c, "?", 860, 440, 100, "black", AN, ai)
    cues = [C["12.b"], C["12.c"], C["13.d"], C["13.e"]]
    shw = [ep(t, x, 0.4) for x in cues]
    af = ep(t, C["13.f"], 0.4)
    for k, (perg, prod) in enumerate(PERGUNTAS_ANALISE):
        a = shw[k]
        if a <= 0:
            continue
        y = 280 + k * 118
        cur = a * (1 - (shw[k + 1] if k < 3 else af))
        rrect(c, 180, y, 1560, 104, 16, mix("#FFFFFF", GREEN, 0.10), cur)
        line(c, 200, y + 104, 1720, y + 104, LINE, a, 2)
        badge_num(c, k + 1, 228, y + 52, a, 24, bg=GREEN)
        text(c, perg, 270, y + 64, 34, "black", INK, a, align="left")
        arrow(c, 1110, y + 52, 1165, y + 52, GREEN, a, 4, 12)
        text(c, prod, 1190, y + (50 if GLOSA[k] else 64), 32, "black", GREEN, a, align="left")
        if GLOSA[k]:
            text(c, "= " + GLOSA[k], 1190, y + 88, 22, "bold", GRAY, a, align="left")
    pill(c, "as respostas = a matéria-prima da sua análise", W / 2, 790, AN, size=28, a=af, anchor="center",
         bounds=(0, 1920))


# ======================================================================
# bloco d: o sinal de que falta análise
# ======================================================================

def b_sinal(c, t, C, B):
    frame(c, t, B["start"], "ARMADILHA", "O SINAL DE QUE FALTA ANÁLISE", AMBER)
    q = lambda x: C[f"14.{x}"]
    aT, aa, ab, acc, ad, ae = (ep(t, q(x), 0.4) for x in "tabcde")
    y0, h = 420, 220
    if aT > 0:
        rrect(c, 200, y0, 440, h, 20, mix("#FFFFFF", RP, 0.12), aT, shadow=True)
        icone_etapa(c, "repertorio", 270, y0 + 70, aT, 0.7, disc=False)
        text(c, "REPERTÓRIO", 320, y0 + 82, 28, "black", RP, aT, align="left", tracking=1)
        text(c, "a referência", 420, y0 + 160, 34, "bold", INK2, aT)
    if aa > 0:
        arrow(c, 420, y0 - 20, 420, y0 - 80, INK2, aa * (1 - ab), 4, 12)
        text(c, "e a frase seguinte?", 420, y0 - 100, 28, "black", INK2, aa * (1 - ab))
    if ab > 0:
        rrect(c, 1280, y0, 440, h, 20, mix("#FFFFFF", FE, 0.12), ab, shadow=True)
        icone_etapa(c, "fechamento", 1350, y0 + 70, ab, 0.7, disc=False)
        text(c, "FECHAMENTO", 1400, y0 + 82, 28, "black", FE, ab, align="left", tracking=1)
        para(c, "“Dessa forma, o problema é grave”", 1500, y0 + 150, 28, "black", INK, ab, 390, 34, align="center")
        # o salto por cima do meio
        p = skia.Path(); p.moveTo(560, y0 - 6); p.quadTo(960, y0 - 230, 1360, y0 - 6)
        c.drawPath(p, paint(RED, ab * (1 - ad), stroke=5, cap_round=True))
        arrow(c, 1340, y0 - 30, 1362, y0 - 4, RED, ab * (1 - ad), 5, 18)
        text(c, "SALTO", 960, y0 - 130, 26, "black", RED, ab * (1 - ad), tracking=2)
    if acc > 0:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(700, y0, 520, h), 20, 20)
        pp = paint(RED, acc * (1 - ae), stroke=4); pp.setPathEffect(skia.DashPathEffect.Make([16, 10], 0))
        c.drawRRect(r, pp)
        text(c, "faltou o meio", 960, y0 + 100, 36, "black", RED, acc * (1 - ae))
        text(c, "do caminho", 960, y0 + 150, 36, "black", RED, acc * (1 - ae))
    if ad > 0:
        edai(c, 820, 250, ad, 44)
    if ae > 0:
        rrect(c, 700, y0, 520, h, 20, mix("#FFFFFF", AN, 0.16), ae, shadow=True)
        icone_etapa(c, "analise", 960, y0 + 70, ae, 0.75, disc=False)
        text(c, "ANÁLISE", 960, y0 + 150, 40, "black", AN, ae)
        text(c, "a resposta ao “e daí?”", 960, y0 + 196, 26, "bold", INK2, ae)
        pill(c, "escreva a resposta ANTES de fechar", W / 2, 760, GREEN, size=28, a=ae, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco e: o fechamento (recibo)
# ======================================================================

def b_fechamento(c, t, C, B):
    sid = which(t, C, ["15", "16", "17"])
    head_seq(c, t, C, [("15", "O FECHAMENTO", "A ASSINATURA DO RECIBO", FE),
                       ("16", "O FECHAMENTO", "UM FECHAMENTO BOM", GREEN),
                       ("17", "O FECHAMENTO", "TRÊS FECHAMENTOS RUINS", RED)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "15":
        aa, ab, acc, ad = (ep(t, q(x), 0.4) for x in "abcd")
        recibo(c, 220, 200, 520, 590, ep(t, q("t"), 0.4),
               linhas=[("ITEM", "eixo do parágrafo"), ("ENTREGUE COM", "argumento · repertório · análise")],
               assin=ep(t, q("b"), 1.2), body=None)
        if aa > 0:
            boxed(c, 820, 200, 900, 230, BLUE, aa, 0.07)
            text(c, "FECHAMENTO = a última frase", 860, 260, 38, "black", BLUE, aa, align="left")
            para(c, "amarra o que foi desenvolvido ao ponto de vista do texto (a tese)", 860, 320, 32, "bold", INK, aa, 820, 42)
        if acc > 0:
            text(c, "muitos cursos chamam de", 860, 520, 30, "bold", INK2, acc, align="left")
            text(c, "“mini-conclusão”", 860, 600, 64, "black", FE, acc, align="left")
        if ad > 0:
            pill(c, "nome de MÉTODO, não termo oficial", 860, 690, GREEN, size=28, a=ad, bounds=(0, 1920))
            entrega_selo(c, 1520, 760, ad, -4, 26)
        return
    if sid == "16":
        aa, ab, acc, ad = (ep(t, q(x), 0.4) for x in "abcd")
        recibo(c, 200, 190, 470, 610, ep(t, q("t"), 0.4), linhas=[("ITEM", "eixo 1 · desinformação")],
               assin=ep(t, q("d"), 1.0))
        if ad > 0:
            selo(c, 435, 560, ad, "ASSINADO ✓", GREEN, -6, 30)
        text(c, "FECHAMENTO · seção 07", 740, 240, 20, "black", GRAY, aa, align="left", tracking=2)
        segs = [("Dessa forma,", FE, None, 0),
                ("enquanto a informação não substituir o preconceito,", INK, PARTE["topico"], ab),
                ("o estigma continuará a afastar os brasileiros do tratamento.", INK, MOV["tese"], acc)]
        rich_para(c, segs, 740, 310, 40, "black", 960, 54, aa)
        if ab > 0:
            pill(c, "retoma o EIXO", 740, 580, PARTE["topico"], size=24, a=ab, bounds=(0, 1920))
        if acc > 0:
            pill(c, "liga à TESE", 980, 580, MOV["tese"], size=24, a=acc, bounds=(0, 1920))
        if ad > 0:
            check_icon(c, 760, 690, 22, ad, GREEN)
            text(c, FECHAMENTOS[0][1], 800, 700, 30, "black", GREEN, ad, align="left")
        return
    # 17: a tabela inteira (o bom em cima, os ruins aparecendo)
    shw = [1.0, ep(t, q("a"), 0.4), ep(t, q("b"), 0.4), ep(t, q("c"), 0.4)]
    text(c, "FECHAMENTO", 200, 225, 20, "black", GRAY, 1, align="left", tracking=2)
    text(c, "AVALIAÇÃO", 1190, 225, 20, "black", GRAY, 1, align="left", tracking=2)
    for k, (s, aval, bom) in enumerate(FECHAMENTOS):
        a, d = (shw[k], 0) if k == 0 else rise(t, q("abc"[k - 1]))
        if a <= 0:
            continue
        y = 250 + k * 140 + d
        col = GREEN if bom else RED
        rrect(c, 180, y, 1560, 128, 14, mix("#FFFFFF", col, 0.07), a * (0.6 if k == 0 else 1))
        check_icon(c, 220, y + 64, 22, a, col, "check" if bom else "x")
        para(c, "“" + s + "”", 260, y + 52, 26 if k else 24, "bold", INK if k else INK2, a, 880, 32)
        para(c, aval, 1190, y + 52, 26, "black", col, a, 520, 32)
    ar = ep(t, q("c") + 2.5, 0.4)
    text(c, "pergunta retórica = feita sem esperar resposta", 1190, 818, 22, "bold", BLUE, ar, align="left")


# ======================================================================
# bloco f: os conectivos de fechamento
# ======================================================================

def b_conectivos(c, t, C, B):
    frame(c, t, B["start"], "OS CONECTIVOS DE FECHAMENTO", "A PALAVRA QUE ABRE A ÚLTIMA FRASE", FE)
    q = lambda x: C[f"18.{x}"]
    aT, aa, ab, acc, ad = (ep(t, q(x), 0.4) for x in "tabcd")
    ai = aT * (1 - aa)
    if ai > 0:
        text(c, "a última frase do parágrafo começa com…", W / 2, 420, 40, "black", INK2, ai)
        pill(c, "  ?  ", W / 2, 520, FE, size=48, a=ai, anchor="center", bounds=(0, 1920))
    if aa > 0:
        boxed(c, 200, 190, 1520, 130, BLUE, aa, 0.07)
        text(c, "CONECTIVO CONCLUSIVO", 240, 240, 24, "black", BLUE, aa, align="left", tracking=2)
        text(c, "conectivo = palavra que liga as ideias · o conclusivo avisa: o raciocínio chegou ao fim", 240, 290, 28,
             "bold", INK, aa, align="left")
    x = 200
    for k, s in enumerate(CONECTIVOS_FECHAMENTO):
        a = ep(t, q("b") + 0.45 * k, 0.3)
        x0, x1 = pill(c, s, x, 380, FE, size=30, a=a, bounds=(0, 1920))
        x = x + text_w(s, "bold", 30) + 30 * 1.24 + 24
    # mapa da redação: o “portanto” fica para a conclusão
    if acc > 0:
        blocos = [("INTRODUÇÃO", None, MOV["tese"]), ("1º DESENVOLVIMENTO", "dessa forma", FE),
                  ("2º DESENVOLVIMENTO", "assim", FE), ("CONCLUSÃO", "Portanto,", PURPLE)]
        for k, (nm, con, col) in enumerate(blocos):
            bx = 200 + k * 385
            rrect(c, bx, 470, 355, 250, 16, mix("#FFFFFF", col, 0.08), acc, shadow=True)
            text(c, nm, bx + 177, 515, 20, "black", col, acc, tracking=1.5)
            for j in range(3):
                line(c, bx + 30, 560 + j * 26, bx + 325 - (j % 2) * 60, 560 + j * 26, LIGHT, acc, 6)
            if con and k < 3:
                pill(c, "portanto", bx + 30, 668, LIGHT, INK2, size=20, a=acc * (1 - ad), bounds=(0, 1920))
                if ad > 0:
                    strike(c, bx + 26, 668, bx + 30 + text_w("portanto", "bold", 20) + 30, 668, ad, RED, ad)
                    pill(c, con, bx + 325, 668, FE, size=20, a=ad, anchor="right", bounds=(0, 1920))
            if k == 3:
                pill(c, con, bx + 30, 560, PURPLE, size=24, a=acc, bounds=(0, 1920))
        text(c, "evite no fim de cada parágrafo o “portanto” que vai abrir a conclusão", W / 2, 780, 28, "black", AMBER,
             acc * (1 - ad))
        text(c, "não repete a marca · a conclusão continua soando como conclusão", W / 2, 780, 28, "black", GREEN, ad)


# ======================================================================
# recap, nós fazemos
# ======================================================================

FRASES = ["Citar é o primeiro degrau; argumentar é o terceiro.", "Pergunte “e daí?” antes de fechar.",
          "Fechamento retoma o eixo e liga à tese, sem informação nova."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("19", "33"), FRASES, cols=[AN, AMBER, FE])


V2_FRASES = ["Em primeiro lugar, a desinformação sustenta o estigma.",
             "Machado de Assis escreveu O Alienista, obra muito importante da literatura brasileira.",
             "Dessa forma, o estigma das doenças mentais continua no Brasil."]
assert " ".join(V2_FRASES) == V2_SOLTO
M4_SEGS = ["Mais de um século depois,",
           "os critérios mudaram, mas a lógica persiste: quem sofre psiquicamente ainda é visto como alguém a ser afastado, "
           "e não cuidado, o que leva muitos a",
           "adiar a busca por ajuda", "por medo do julgamento."]
assert " ".join(M4_SEGS) == MODELO[3]
EXX, EXY, EXW, EXH = 150, 160, 1130, 680
EHX, EHS, EHLH, EHMW = 270, 32, 52, 940


def b_exercicio(c, t, C, B):
    sid = which(t, C, ["20", "21"])
    head_seq(c, t, C, [("20", "NÓS FAZEMOS", "ESCREVA A ANÁLISE QUE FALTA", AMBER),
                       ("21", "NÓS FAZEMOS", "COMPARE COM O MODELO", GREEN)])
    if sid == "20":
        q = lambda x: C[f"20.{x}"]
        a0 = ep(t, C["20"], 0.4)
        paper(c, EXX, EXY, EXW, EXH, a0, lh=EHLH, top=EXY + 150 - 2 - 2 * EHLH)
        text(c, "ENEM 2020 · Versão 2 · repertório solto", EXX + 110, EXY + 64, 24, "black", BLUE, a0, align="left")
        text(c, DIDATICO, EXX + 110, EXY + 100, 18, "medium", AMBER, a0, align="left")
        y = EXY + 150
        spans = [(q("a"), q("b") - 0.3), (q("b"), q("c") - 0.3), (q("c"), q("d") - 0.3)]
        for k, s in enumerate(V2_FRASES):
            if k == 2:
                ae = ep(t, q("e"), 0.4)
                if ae > 0:
                    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(EHX - 16, y - 34, EHMW, 2 * EHLH + 20), 12, 12)
                    rrect(c, EHX - 16, y - 34, EHMW, 2 * EHLH + 20, 12, mix("#FFFFFF", AN, 0.10), ae)
                    pp = paint(AN, ae, stroke=3); pp.setPathEffect(skia.DashPathEffect.Make([12, 8], 0))
                    c.drawRRect(r, pp)
                    text_mid(c, "a sua frase de ANÁLISE aqui", EHX - 16 + EHMW / 2, y - 34 + EHLH + 10, 30, "black", AN, ae)
                y += 2 * EHLH + 30
            n = hand_para(c, s, EHX, y, EHS, PEN, a0, EHMW, EHLH, reveal=wreveal(t, spans[k]))
            if k == 1:
                lines = hwrap(s, EHS, EHMW)
                ly = y + (n - 1) * EHLH
                lx = EHX + hand_w(lines[-1], EHS)
                ad = ep(t, q("d"), 0.4)
                for j, ln in enumerate(lines):
                    underline(c, EHX, EHX + hand_w(ln, EHS), y + j * EHLH + 10, RP, a0, clamp(ep(t, q("d"), 0.6) * n - j), 5)
                pill(c, "só mencionada", lx + 24, ly - 10, RP, size=20, a=ad, bounds=(0, 1920))
                edai(c, lx + 200, ly + 22, ad * (1 - ep(t, q("e"), 0.4)), 36)
            y += max(1, n) * EHLH + 10
        # as 4 perguntas ao lado
        ae = ep(t, q("e"), 0.4)
        card(c, 1320, 160, 450, 680, ae)
        if ae > 0:
            text(c, "AS 4 PERGUNTAS", 1360, 220, 22, "black", GREEN, ae, align="left", tracking=2)
            for k, (perg, prod) in enumerate(PERGUNTAS_ANALISE):
                yy = 280 + k * 120
                badge_num(c, k + 1, 1375, yy - 8, ae, 18, bg=GREEN)
                para(c, perg, 1410, yy, 24, "black", INK, ae, 330, 30)
                text(c, prod, 1410, yy + 64, 20, "bold", GREEN, ae, align="left")
        pause_timer(c, t, q("p") + 0.3, 1545, 760)
        return
    q = lambda x: C[f"21.{x}"]
    card(c, *CARD_R)
    aa = ep(t, q("a"), 0.4)
    text(c, "PARÁGRAFO-MODELO · seção 08 · frase [4] = análise", 200, 225, 22, "black", AN, aa, align="left", tracking=1.5)
    text(c, PARAG_DIDATICO, 200, 262, 18, "medium", AMBER, aa, align="left")
    para(c, "[3] " + MODELO[2], 200, 320, 22, "medium", GRAY, aa, 1520, 30)
    asx = ep(t, q("s"), 0.4)
    ab, acc = ep(t, q("b"), 0.4), ep(t, q("c"), 0.4)
    if asx > 0:
        rrect(c, 180, 440, 1560, 250, 14, mix("#FFFFFF", AN, 0.10), asx)
        rrect(c, 180, 440, 10, 250, 4, AN, asx)
        segs = [("[4] " + M4_SEGS[0], INK, BLUE, ab), (M4_SEGS[1], INK, None, 0), (M4_SEGS[2], INK, RED, acc),
                (M4_SEGS[3], INK, None, 0)]
        rich_para(c, segs, 220, 500, 34, "black", 1480, 48, asx)
    pill(c, "atualiza a referência", 220, 730, BLUE, size=24, a=ab, bounds=(0, 1920))
    pill(c, "consequência concreta", 560, 730, RED, size=24, a=acc, bounds=(0, 1920))
    ad = ep(t, q("d"), 0.4)
    if ad > 0:
        selo(c, 1480, 760, ad, "SUBIU A ESCADA ✓", GREEN, -4, 30)


# ======================================================================
# erros clássicos
# ======================================================================

ERROS = [("22", "Pular da referência direto para o fechamento", "uma obra famosa parece provar tudo sozinha",
          "a referência não fala sozinha: pergunte “e daí?” e escreva a análise"),
         ("23", "Fechar com “isso é muito grave”", "tem conectivo e soa como conclusão",
          "“isso é muito grave” não amarra nada: ligue o eixo à tese"),
         ("24", "Abrir um assunto novo na última frase", "parece que você acrescenta mais um argumento",
          "o assunto novo fica sem desenvolvimento: fechamento sem informação nova")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# Questão 2 (a parte que falta) e a análise didática
# ======================================================================

Q2_ENUN = "Considerando o modelo de parágrafo estudado, o que mais falta a esse trecho é"
ALT2 = [("A", "um tópico frasal, pois o parágrafo não indica seu argumento.", "26.A", "28.xa", "o tópico frasal existe",
         RED),
        ("B", "a análise, que relacionaria a referência à realidade brasileira — cidades do interior sem salas — e "
              "mostraria por que isso sustenta a tese.", "26.B", None, "", GREEN),
        ("C", "um fechamento, pois o parágrafo termina sem retomar a ideia.", "26.C", "28.xc",
         "o fechamento é fraco, mas existe", RED),
        ("D", "um repertório, pois filmes não são aceitos como repertório.", "27.D", "28.xd",
         "a Cartilha aceita filmes", RED),
        ("E", "uma proposta de intervenção completa, obrigatória em cada parágrafo.", "27.E", "28.xe",
         "inventa uma exigência", RED)]
Q2_KEYS = ["topico", "repertorio", "fechamento"]


def b_q2(c, t, C, B):
    sid = which(t, C, ["25", "26", "27", "28", "29"])
    if sid == "29":
        head(c, t, C["29"], "QUESTÃO 2 · E SE TIVESSE ANÁLISE?", "UMA ANÁLISE POSSÍVEL", AN)
        card(c, *CARD_R)
        q = lambda x: C[f"29.{x}"]
        aa = ep(t, C["29"], 0.4)
        text(c, "ENEM 2019 · “" + TEMA19 + "”", 200, 225, 22, "black", BLUE, aa, align="left")
        frases = [Q2_PARAG[0], Q2_PARAG[1], Q2_ANALISE[0], Q2_ANALISE[1], Q2_PARAG[2]]
        keys = ["topico", "repertorio", "analise", "analise", "fechamento"]
        rv = [1, 1, ep(t, q("b"), 0.5), ep(t, q("c"), 0.5), 1]
        lay = faixas_paragrafo(c, 214, 300, 1180, 30, 40, frases, keys, aa, reveal=rv, faixa=[1, 1, 1, 1, 1], nums=False,
                               peso="bold")
        ab = ep(t, q("b"), 0.4)
        edai(c, 1440, lay[1][0] - 10, aa * (1 - ab), 40)
        if ab > 0:
            arrow(c, 1440, (lay[2][0] + lay[3][1]) / 2, 1408, (lay[2][0] + lay[3][1]) / 2, AN, ab, 4, 14)
            text(c, "ANÁLISE", 1460, (lay[2][0] + lay[3][1]) / 2 - 10, 30, "black", AN, ab, align="left")
            text(c, "elaborada para", 1460, (lay[2][0] + lay[3][1]) / 2 + 26, 22, "black", AMBER, ab, align="left")
            text(c, "fins didáticos", 1460, (lay[2][0] + lay[3][1]) / 2 + 54, 22, "black", AMBER, ab, align="left")
        text(c, ANALISE_DIDATICA + " Sem dados novos: só o que o filme mostra e a falta de salas.", 214, lay[-1][1] + 50,
             20, "medium", AMBER, ab, align="left")
        ad = ep(t, q("d"), 0.4)
        if ad > 0:
            for k, s_ in enumerate(("1 · o filme mostra", "2 · o Brasil de hoje", "3 · o que prova para a tese")):
                a = ep(t, q("d") + 0.5 * k, 0.4)
                pill(c, s_, 214 + k * 420, 790, AN, size=26, a=a, bounds=(0, 1920))
        return
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A PARTE QUE FALTA", BLUE)
    card(c, *CARD_R)
    aT = ep(t, C["25"], 0.4)
    u = ep(t, C["26"], 0.6)          # parágrafo grande (cena 25) → coluna da esquerda (26–28)
    rv = [ep(t, C[f"25.s{k + 1}"], 0.4) for k in range(3)]
    # versão grande
    ag = aT * (1 - u)
    if ag > 0:
        text(c, "QUESTÃO 2", 200, 230, 20, "black", GRAY, ag, align="left", tracking=2)
        text(c, "ENEM 2019 · “" + TEMA19 + "”", 200, 290, 32, "black", BLUE, ag * ep(t, C["25.a"], 0.4), align="left")
        lay = faixas_paragrafo(c, 214, 400, 1480, 36, 50, Q2_PARAG, Q2_KEYS, ag, reveal=rv, faixa=rv, nums=False)
        edai(c, 1300, lay[1][1] + 10, ag * ep(t, C["25.s3"], 0.4), 38)
    # coluna da esquerda + alternativas
    if u > 0:
        text(c, "QUESTÃO 2 · ENEM 2019", 190, 225, 18, "black", GRAY, u, align="left", tracking=2)
        para(c, "“" + TEMA19 + "”", 190, 264, 22, "black", BLUE, u, 560, 28)
        lay = faixas_paragrafo(c, 204, 340, 540, 22, 29, Q2_PARAG, Q2_KEYS, u, faixa=[1, 1, 1], nums=False, peso="medium")
        para(c, Q2_ENUN, 190, lay[-1][1] + 50, 24, "black", INK, u * ep(t, C["26.b"], 0.4), 550, 30)
        aok = ep(t, C["28.ok"], 0.4)
        pill(c, "falta: ANÁLISE (entre o filme e o fechamento)", 190, 795, AN, size=20, a=aok, bounds=(0, 1920))
        alts_panel(c, t, C, ALT2, 800, 245, 940, 27, "28.ok", "B", 8)
        pause_timer(c, t, C["27.p"] + 0.3, 470, 750, dur=2.4)
        questao_rotulo(c, u)


# ======================================================================
# Questão 5 (o fechamento adequado)
# ======================================================================

Q5_ENUN = ("Um parágrafo de desenvolvimento discutiu como a ausência de creches públicas sobrecarrega as mulheres com o "
           "cuidado dos filhos (tema do Enem 2023). A frase que melhor fecha esse parágrafo é:")
ALT5 = [("A", "Além disso, a violência urbana também afeta as mulheres brasileiras.", "30.A", "32.xa",
         "assunto novo, fora do eixo", RED),
        ("B", "Será que um dia essa realidade vai mudar?", "30.B", "32.xb", "pergunta retórica", RED),
        ("C", "Desse modo, sem uma rede pública que divida o cuidado, esse trabalho continua recaindo sobre as mulheres e "
              "permanece invisível.", "30.C", None, "", GREEN),
        ("D", "Assim, isso é algo muito triste e preocupante.", "31.D", "32.xd", "vaga: “isso” e “triste”", RED),
        ("E", "Em primeiro lugar, as creches são instituições de ensino.", "31.E", "32.xe", "reinicia o parágrafo", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "O FECHAMENTO ADEQUADO", BLUE)
    card(c, *CARD_R)
    aT = ep(t, C["30"], 0.4)
    aa = ep(t, C["30.a"], 0.4)
    text(c, "QUESTÃO 5 · ENEM 2023", 190, 225, 18, "black", GRAY, aT, align="left", tracking=2)
    h = para(c, Q5_ENUN, 190, 280, 26, "black", INK, aa, 560, 34)
    recibo(c, 250, 280 + h + 10, 440, 290, aa, titulo="RECIBO", linhas=[], assin=ep(t, C["32.ok"] + 0.4, 1.0),
           body="eixo: falta de creches", body_size=24)
    alts_panel(c, t, C, ALT5, 800, 245, 940, 28, "32.ok", "C", 8)
    pause_timer(c, t, C["31.p"] + 0.3, 1600, 750, dur=2.4)
    pill(c, "conectivo + eixo + tese, sem informação nova", 800, 800, GREEN, size=22, a=ep(t, C["32.ok"] + 1.5, 0.4),
         bounds=(0, 1920))
    questao_rotulo(c, aT)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O PARÁGRAFO-MODELO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    for k, key in enumerate(KEYS):
        a = ep(t, C["34.a"] + 0.4 * k, 0.4)
        icone_etapa(c, key, 480 + k * 240, 300, a, 1.0)
        check_icon(c, 520 + k * 240, 340, 16, a, GREEN)
    text(c, "você já tem as 5 peças", W / 2, 420, 34, "black", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    for k, key in enumerate(KEYS):
        a = ep(t, C["34.b"] + 0.3 * k, 0.4)
        y = 500 + k * 54
        badge_num(c, k + 1, 330, y + 18, a, 18, bg=PARTE[key])
        rrect(c, 365, y + 4, [430, 470, 500, 520, 400][k], 28, 10, mix("#FFFFFF", PARTE[key], 0.35), a)
        text(c, NOMEP[key], 380, y + 26, 20, "black", PARTE[key], a, align="left")
    text(c, "comentado frase por frase", 580, 790, 28, "black", GREEN, ab)
    ac = ep(t, C["34.c"], 0.5)
    for k, oks in enumerate(([None] * 5, [None] * 5, [1, 1, 1, 1, 1])):
        a = ep(t, C["34.c"] + 0.5 * k, 0.4)
        mini_entrega(c, 1060 + k * 270, 620, a, oks, 0.74, nomes=False)
        text(c, f"VERSÃO {k + 1}", 1060 + k * 270, 750, 20, "black", INK2, a, tracking=2)
    pill(c, "PIOR  →  MELHOR", 1330, 800, INK2, size=22, a=ac, anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "35", "Em qual degrau da escada a sua análise costuma parar?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, entrega=b_entrega, analogia=b_analogia,
              analise=b_analise, escada=b_escada, perguntas=b_perguntas, sinal=b_sinal, fechamento=b_fechamento,
              conectivos=b_conectivos, recap=b_recap, exercicio=b_exercicio, erros=b_erros, q2=b_q2, q5=b_q5,
              ponte=b_ponte, cta=b_cta)
