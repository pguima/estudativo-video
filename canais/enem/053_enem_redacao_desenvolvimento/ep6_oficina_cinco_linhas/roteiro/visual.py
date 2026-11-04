"""Visual — Redação ENEM, Desenvolvimento, Episódio 6: Oficina — o segundo parágrafo em cinco linhas (tema claro).
Usa o desenho compartilhado da série (desenvolvimento_visual.py): etapas da entrega, ficha, tese do estigma, rascunho com
caligrafia, alternativas, recap, erros e CTA, e os textos EXATOS do material (RASCUNHO e MARCADOR_REP da seção 10).
Novo aqui: a LISTA DE COMPRAS (bolo) que vira o rascunho de cinco linhas; a LISTA de 5 linhas fixa à esquerda como
checklist (linha atual acesa, feitas com ✓, repertório em aberto em âmbar, ANÁLISE piscando vazia em vermelho com ✗ na
1ª tentativa e depois com ✓); o RASCUNHO à direita, escrito à mão no ritmo da fala (setas → desenhadas, porque a fonte
manuscrita não tem o glifo); as duas listas lado a lado; as cinco linhas viram o parágrafo; barras de equilíbrio D1 × D2;
e o "você faz" com a tese de 2021.
Cores: azul = tema/eixos · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial ·
cores das partes em PARTE (tópico azul, argumento azul-petróleo, repertório ocre, análise laranja-telha, fecho magenta).
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from desenvolvimento_visual import *  # noqa
usar_tempos(__file__)

ARQUIVO_FINAL = "enem_redacao_desenvolvimento_ep6_oficina_cinco_linhas.mp4"

# material, seção 10 (as cinco linhas, EXATAS) — rótulo, texto, chave da parte
LABELS = [r[0] for r in RASCUNHO]
REP_MATERIAL = RASCUNHO[2][1]
# o parágrafo do eixo 2 (elaborado para fins didáticos; repertório EM ABERTO)
S_D2 = ["Além disso, ao associar o adoecimento psíquico à violência, parte da mídia reforça a imagem de perigo que alimenta "
        "o estigma.",
        "Isso acontece porque o noticiário e a ficção costumam destacar casos extremos, o que fixa a imagem de que quem tem "
        "um transtorno mental é perigoso.",
        MARCADOR_REP,
        "Com isso, o público passa a temer quem tem diagnóstico, e quem sofre psiquicamente acaba empurrado para o isolamento "
        "e para o silêncio, em vez de buscar ajuda.",
        "Assim, a mídia reforça o estigma que afasta os brasileiros do tratamento."]
# Questão 3 do material: a tese de 2021 (EXATA)
TESE21 = ("A falta de registro civil torna parte dos brasileiros invisível para o Estado, situação mantida pela distância "
          "dos cartórios e pela desinformação sobre a gratuidade do registro.")
# "você faz": um rascunho possível (elaborado para fins didáticos; só causa e consequência; tópico = alternativa A da Q3)
R21 = ["em primeiro lugar, a distância dos cartórios dificulta o registro em regiões isoladas",
       "cartório longe → viagem cara e demorada → família adia o registro",
       MARCADOR_REP,
       "sem registro → invisível para o Estado → longe da cidadania",
       "assim, a distância dos cartórios mantém parte dos brasileiros invisível para o Estado"]

# lista à esquerda (checklist) e rascunho à direita
LX, LY, LW, LH = 40, 150, 400, 700
MX, MY, MW, MH = 470, 150, 1410, 700
LBX = MX + 110            # rótulo manuscrito da linha
CX = MX + 318             # conteúdo da linha
CW = MX + MW - 30 - CX    # largura do conteúdo
Y0, RH, RL = MY + 190, 104, 46   # baseline da 1ª linha, altura de cada linha do rascunho, entrelinha
HS = 34                   # tamanho da letra no rascunho


# ======================================================================
# letra manuscrita com setas (a fonte Caveat não tem "→")
# ======================================================================

def _aw(size):
    return size * 1.25


def harrow_w(s, size, bold=False):
    parts = [p.strip() for p in s.split("→")]
    gap = hand_w(" ", size, bold) * 1.2
    return sum(hand_w(p, size, bold) for p in parts) + (len(parts) - 1) * (_aw(size) + 2 * gap)


def harrow(c, s, x, y, size, color, a=1.0, reveal=1.0, bold=False):
    """uma linha manuscrita em que cada "→" vira uma seta desenhada; reveal escreve aos poucos"""
    if a <= 0 or reveal <= 0:
        return
    parts = [p.strip() for p in s.split("→")]
    total = sum(len(p) for p in parts) + len(parts) - 1
    n = total * clamp(reveal)
    gap = hand_w(" ", size, bold) * 1.2
    xx, used = x, 0
    for i, p in enumerate(parts):
        r = clamp((n - used) / max(1, len(p)))
        if r > 0:
            hand(c, p, xx, y, size, color, a, r, bold=bold)
        used += len(p)
        xx += hand_w(p, size, bold)
        if i < len(parts) - 1:
            ra = clamp(n - used)
            if ra > 0:
                arrow(c, xx + gap, y - size * 0.32, xx + gap + _aw(size), y - size * 0.32, color, a, max(2.5, size * 0.09),
                      size * 0.32, progress=ra)
            used += 1
            xx += _aw(size) + 2 * gap


def hwrap_arrow(s, size, maxw, bold=False):
    out, cur = [], ""
    for w in s.split():
        tst = (cur + " " + w).strip()
        if cur and harrow_w(tst, size, bold) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    return out


def hpara_arrow(c, s, x, y, size, color, a, maxw, lh, reveal=1.0, bold=False):
    """parágrafo manuscrito com setas, revelado em ordem; retorna nº de linhas"""
    lines = hwrap_arrow(s, size, maxw, bold)
    tot = sum(len(l) for l in lines)
    done = clamp(reveal) * tot
    if a > 0:
        for k, ln in enumerate(lines):
            harrow(c, ln, x, y + k * lh, size, color, a, clamp(done / max(1, len(ln))), bold)
            done -= len(ln)
    return len(lines)


def span(sid, phrase, C, dur=4.0, cue=None):
    t0 = C[cue] if cue else C[sid]
    return phrase_span(sid, phrase, t0, t0 + dur)


def blink(t, f=1.6):
    return 0.35 + 0.65 * (0.5 + 0.5 * math.cos(2 * math.pi * f * t))


def dashed_box(c, x, y, w, h, col, a, r=12, sw=3.5):
    if a <= 0:
        return
    rrect(c, x, y, w, h, r, col, 0.10 * a)
    p = skia.Paint(AntiAlias=True, Color=hexc(col, a), Style=skia.Paint.kStroke_Style, StrokeWidth=sw,
                   PathEffect=skia.DashPathEffect.Make([14, 10], 0))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), p)


# ======================================================================
# a LISTA (checklist das 5 linhas, fixa à esquerda)
# ======================================================================

def lista(c, t, a=1.0, cur=None, ok=None, falta=None, aberto=None, title="LISTA · 5 LINHAS", x=LX, y=LY, w=LW, rows=None):
    """cur = índice aceso · ok[k] = ✓ verde · falta[k] = ✗ vermelho piscando · aberto[k] = âmbar (repertório em aberto)"""
    if a <= 0:
        return
    ok = ok or [0] * 5
    falta = falta or [0] * 5
    aberto = aberto or [0] * 5
    rows = rows or [1.0] * 5
    rrect(c, x, y, w, LH, 24, "#FFFFFF", a, shadow=True)
    text(c, title, x + w / 2, y + 50, 20, "black", GRAY, a, tracking=2)
    for k, (lab, _, key) in enumerate(RASCUNHO):
        ra = a * clamp(rows[k])
        if ra <= 0:
            continue
        yy = y + 84 + k * 120
        col = PARTE[key]
        if falta[k] > 0:
            bl = blink(t)
            rrect(c, x + 14, yy, w - 28, 104, 16, mix("#FFFFFF", RED, 0.16), ra * falta[k] * bl)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 14, yy, w - 28, 104), 16, 16),
                        paint(RED, ra * falta[k] * bl, stroke=3))
        elif k == cur:
            rrect(c, x + 14, yy, w - 28, 104, 16, mix("#FFFFFF", col, 0.16), ra)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 14, yy, w - 28, 104), 16, 16), paint(col, ra, stroke=3))
        icone_etapa(c, key, x + 62, yy + 52, ra, 0.62, disc=False)
        text(c, lab, x + 110, yy + 50, 32, "black", col, ra, align="left")
        sub = "seu exemplo, de fato" if aberto[k] > 0 else ETAPA[key].lower()
        text(c, sub, x + 110, yy + 82, 17, "bold", AMBER if aberto[k] > 0 else GRAY, ra, align="left")
        cx_ = x + w - 50
        if falta[k] > 0:
            check_icon(c, cx_, yy + 52, 22, ra * falta[k] * (0.5 + 0.5 * blink(t)), RED, "x")
        elif ok[k] > 0:
            check_icon(c, cx_, yy + 52, 22, ra * ok[k], GREEN)
        elif aberto[k] > 0:
            check_icon(c, cx_, yy + 52, 22, ra * aberto[k], AMBER)
        else:
            c.drawCircle(cx_, yy + 52, 20, paint(LIGHT, ra, stroke=3))


# ======================================================================
# o RASCUNHO das cinco linhas (à direita)
# ======================================================================

def rascunho5(c, t, textos, rv, a=1.0, header="", sub=None, sub_col=AMBER, lit=None, rep_note=0.0, hole=0.0, hole_k=3,
              lab_a=None, size=HS):
    """textos[k] = conteúdo manuscrito (MARCADOR_REP em âmbar) · rv[k] = reveal · hole = alpha do buraco da análise"""
    paper(c, MX, MY, MW, MH, a, lh=RH, top=Y0 - 12 + 2)
    if a <= 0:
        return
    text(c, header, LBX, MY + 62, 22, "black", BLUE, a, align="left", tracking=1)
    if sub:
        text(c, sub, LBX, MY + 98, 18, "medium", sub_col, a, align="left")
    lab_a = lab_a or [1.0] * 5
    for k, (lab, _, key) in enumerate(RASCUNHO):
        yb = Y0 + k * RH
        la = a * clamp(lab_a[k])
        if lit and lit[k] > 0:
            rrect(c, LBX - 20, yb - 40, MW - 110 - 20 + 20, RH - 6, 12, mix("#FFFFFF", PARTE[key], 0.12), la * lit[k])
        hand(c, lab, LBX, yb, 34, PARTE[key], la, bold=True)
        s = textos[k]
        if s == MARCADOR_REP:
            hand(c, s, CX, yb, size, AMBER, a, rv[k], bold=True)
            if rep_note > 0:
                text(c, "material: “" + REP_MATERIAL + "”", CX, yb + 38, 20, "medium", GRAY, a * rep_note, align="left")
        elif s:
            hpara_arrow(c, s, CX, yb, size, PEN, a, CW, RL, rv[k])
    if hole > 0:
        yb = Y0 + hole_k * RH
        bl = blink(t)
        dashed_box(c, CX - 14, yb - 38, CW + 10, 56, RED, a * hole * bl)
        text(c, "vazia!", CX + 10, yb, 26, "black", RED, a * hole * bl, align="left")
        check_icon(c, CX + CW - 30, yb - 10, 18, a * hole * bl, RED, "x")


def linha_y(k):
    return Y0 + k * RH


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], SERIE_SELO, "OFICINA: O 2º PARÁGRAFO", GREEN)
    aa = ep(t, C["01.a"], 0.5)
    paper(c, 200, 220, 780, 600, aa, lh=86, top=380, rot=-2)
    ab = ep(t, C["01.b"], 0.5)
    pen_draw(c, 930, 330, PEN, ab, -30, 0.9)
    ac = ep(t, C["01.c"], 0.5)
    hand(c, "2º desenvolvimento", 300, 330, 44, PEN, ac, wreveal(t, (C["01.c"], C["01.c"] + 1.8)), bold=True)
    for k, (lab, _, key) in enumerate(RASCUNHO):
        a, d = rise(t, C["01.d"] + 0.2 * k)
        y = 450 + k * 80 + d
        badge_num(c, k + 1, 320, y - 12, a, 20, bg=PARTE[key])
        hand(c, lab, 360, y, 32, PARTE[key], a, bold=True)
        line(c, 560, y + 6, 900 - (k % 2) * 80, y + 6, LIGHT, a, 4)
    if ac > 0:
        rrect(c, 1080, 300, 640, 330, 22, "#FFFFFF", ac, shadow=True)
        rrect(c, 1080, 300, 10, 330, 5, BLUE, ac)
        text(c, "ENEM 2020", 1120, 360, 22, "black", BLUE, ac, align="left", tracking=2)
        para(c, "“" + TEMA20 + "”", 1120, 420, 34, "black", INK, ac, 560, 44)
        pill(c, "eixo 2 · mídia", 1120, 580, PARTE["argumento"], size=24, a=ac, bounds=(0, 1920))
    ad = ep(t, C["01.d"], 0.4)
    text(c, "5 linhas de rascunho", 1400, 730, 48, "black", GREEN, ad)


def clock(c, cx, cy, r, a, frac, label, sub="de rascunho"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 12, paint(GREEN, a * 0.16))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * clamp(frac), False,
              paint(GREEN, a, stroke=r * 0.16, cap_round=True))
    for k, ln in enumerate(label.split("\n")):
        text_mid(c, ln, cx, cy - 40 + k * r * 0.30, r * 0.24, "black", INK, a)
    text(c, sub, cx, cy + r * 0.52, r * 0.12, "bold", GRAY, a)


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DA AULA", "PLANEJAR E CONFERIR", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    ab = ep(t, C["02.b"], 0.5)
    lista(c, t, aa, x=260, y=150, rows=[ep(t, C["02.a"] + 0.2 * k, 0.3) for k in range(5)],
          ok=[ep(t, C["02.b"] + 0.25 * k, 0.3) for k in range(5)])
    clock(c, 1180, 430, 200, aa, prog(t, C["02.a"], 2.5), "poucos\nminutos", "para qualquer parágrafo")
    selo(c, 1180, 760, ab, "PRONTO ANTES DE ESCREVER", GREEN, -3, 34)


def b_material(c, t, C, B):
    frame(c, t, B["start"], "SEPARE AGORA", "PAPEL E CANETA", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    paper(c, 260, 220, 560, 420, aa, lh=48, top=290, rot=-3)
    text(c, "folha", 540, 700, 32, "black", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    pen_draw(c, 1000, 420, PEN, ab, 0, 1.0)
    text(c, "caneta", 1000, 700, 32, "black", INK2, ab)
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        hand(c, "rascunho", 330, 360, 48, PEN, ac, wreveal(t, (C["03.c"], C["03.c"] + 1.2)), bold=True)
        boxed(c, 1180, 250, 520, 400, BLUE, ac, 0.06)
        text(c, "RASCUNHO", 1440, 320, 26, "black", BLUE, ac, tracking=3)
        para(c, "o espaço de teste, onde você planeja antes de passar o texto a limpo", 1440, 400, 34, "black", INK, ac, 440,
             44, align="center")
    pill(c, "pegou? então vamos!", W / 2, 780, GREEN, size=28, a=ep(t, C["03.d"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# a lista de compras (concreto antes do abstrato)
# ======================================================================

ITENS = ["farinha", "ovos", "açúcar", "leite"]


def lista_compras(c, t, C, x, y, a, rv=None, vazia=0.0, bl=True):
    paper(c, x, y, 520, 560, a, lh=74, top=y + 150, margin=True)
    if a <= 0:
        return
    hand(c, "Lista · bolo", x + 110, y + 90, 40, PEN, a, bold=True)
    for k in range(5):
        yb = y + 162 + k * 74
        if k < 4:
            hand(c, "– " + ITENS[k], x + 110, yb, 36, PEN, a, 1.0 if rv is None else rv[k])
        elif vazia > 0:
            f = blink(t) if bl else 1.0
            dashed_box(c, x + 100, yb - 40, 360, 56, RED, a * vazia * f)
            text(c, "?", x + 130, yb, 34, "black", RED, a * vazia * f, align="left")


def b_lista(c, t, C, B):
    sid = which(t, C, ["04", "05"])
    head_seq(c, t, C, [("04", "UMA CENA DO DIA A DIA", "A LISTA DE COMPRAS", BLUE),
                       ("05", "O MÉTODO", "PLANEJAMENTO EM 5 LINHAS", GREEN)])
    card(c, *CARD_R)
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        V1.bolo(c, 1400, 470, aa, 1.3)
        text(c, "o bolo", 1400, 520, 30, "black", INK2, aa)
        ab = ep(t, C["04.b"], 0.5)
        rv = [ep(t, C["04.c"] + 0.7 * k, 0.5) for k in range(4)]
        lista_compras(c, t, C, 260, 190, ab, rv, ep(t, C["04.d"], 0.4))
        ae = ep(t, C["04.e"], 0.5)
        if ae > 0:
            xmark(c, 1400, 380, 70, ae * 0.9)
            pill(c, "volta para casa SEM O INGREDIENTE", 1400, 640, RED, size=28, a=ae, anchor="center", bounds=(0, 1920))
            text(c, "e só descobre na hora de bater a massa", 1400, 720, 26, "bold", INK2, ep(t, C["04.e"] + 1.2, 0.4))
        return
    lista_compras(c, t, C, 200, 210, 1.0, None, 1.0, bl=False)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 800, 200, 900, 150, GREEN, aa, 0.07)
        text(c, "PLANEJAMENTO EM 5 LINHAS", 840, 245, 22, "black", GREEN, aa, align="left", tracking=2)
        para(c, "antes de redigir o parágrafo inteiro, uma linha curta para cada parte", 840, 300, 30, "black", INK, aa, 820,
             38)
    ab = ep(t, C["05.b"], 0.5)
    arrow(c, 740, 520, 830, 520, GREEN, ab, 6, 18, progress=ab)
    if ab > 0:
        rrect(c, 860, 390, 840, 330, 18, PAPER, ab, shadow=True)
        for k, (lab, _, key) in enumerate(RASCUNHO):
            yb = 440 + k * 60
            hand(c, lab, 900, yb, 28, PARTE[key], ab * ep(t, C["05.b"] + 0.2 * k, 0.3), bold=True)
            line(c, 1100, yb + 6, 1640, yb + 6, LIGHT, ab, 3)
        dashed_box(c, 1090, 440 + 3 * 60 - 34, 560, 46, RED, ab * ep(t, C["05.c"], 0.4) * blink(t))
    pill(c, "= a LISTA DE COMPRAS do parágrafo", 1280, 372, GREEN, size=24, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["05.c"], 0.4)
    pill(c, "linha vazia = parágrafo ainda NÃO está pronto", W / 2, 785, RED, size=28, a=ac, anchor="center", bounds=(0, 1920))


# ======================================================================
# pré-requisitos e a palavra nova
# ======================================================================

def b_prereq(c, t, C, B):
    sid = which(t, C, ["06", "07"])
    head_seq(c, t, C, [("06", "REVISÃO RELÂMPAGO", "EPISÓDIOS 1 A 5", PURPLE), ("07", "REVISÃO RELÂMPAGO", "A NOSSA REDAÇÃO", PURPLE)])
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "06":
        shw = [ep(t, q(x), 0.4) for x in "bcdef"]
        ag = ep(t, q("g"), 0.4)
        lit = [shw[k] * (1 - (shw[k + 1] if k < 4 else ag)) for k in range(5)]
        aa = ep(t, q("a"), 0.4)
        ficha_entrega(c, 200, 170, 960, aa, show=shw, lit=lit, partes=1.0, rowh=110, title="CADA PARÁGRAFO ENTREGA UM ITEM")
        if ag > 0:
            bubble(c, "E DAÍ?", 1280, 340, 360, PARTE["fechamento"], ag, size=64)
            text(c, "a pergunta do cliente", 1460, 560, 30, "black", PARTE["fechamento"], ag)
        return
    aa = ep(t, q("a"), 0.4)
    h = tese_card(c, 200, 180, 1520, ep(t, q("t"), 0.4), eixos=0, size=30)
    if aa > 0:
        yy = 180 + 96 + 2 * 40 + 30
        pill(c, "EIXO 1 · desinformação", 236, yy, PARTE["topico"], size=24, a=ep(t, q("b"), 0.4), bounds=(0, 1920))
        pill(c, "EIXO 2 · mídia", 600, yy, PARTE["argumento"], size=24, a=ep(t, q("c"), 0.4), bounds=(0, 1920))
        text(c, "eixo = um caminho de prova da tese", 1680, yy + 8, 24, "bold", BLUE, aa, align="right")
    for k, (cue, tt, s, col, oks) in enumerate((("d", "D1 · EIXO 1", "desinformação · com O Alienista (ep. 5)", PARTE["topico"],
                                                  [1] * 5),
                                                 ("e", "D2 · EIXO 2", "mídia · HOJE, ao vivo", PARTE["argumento"], None))):
        a, d = rise(t, q(cue))
        x = 200 + k * 780
        if a <= 0:
            continue
        rrect(c, x, 520 + d, 740, 290, 20, mix("#FFFFFF", col, 0.07), a, shadow=True)
        text(c, tt, x + 36, 570 + d, 24, "black", col, a, align="left", tracking=2)
        text(c, s, x + 36, 612 + d, 24, "bold", INK2, a, align="left")
        if oks:
            mini_entrega(c, x + 250, 718 + d, a, oks, 0.85)
            selo(c, x + 590, 718 + d, a, "PRONTO", GREEN, -6, 30)
        else:
            text_mid(c, "?", x + 370, 720 + d, 110, "black", col, a)


def jornal(c, cx, cy, a, col):
    rrect(c, cx - 80, cy - 60, 160, 120, 8, "#FFFFFF", a, stroke=4, stroke_color=col)
    rrect(c, cx - 64, cy - 46, 128, 22, 4, col, a)
    for k in range(3):
        line(c, cx - 64, cy - 6 + k * 18, cx + 64 - (k % 2) * 40, cy - 6 + k * 18, col, a * 0.6, 5)


def claquete(c, cx, cy, a, col):
    rrect(c, cx - 80, cy - 30, 160, 90, 8, col, a)
    p = skia.Path(); p.moveTo(cx - 80, cy - 40); p.lineTo(cx + 74, cy - 70); p.lineTo(cx + 80, cy - 50); p.lineTo(cx - 74, cy - 20)
    p.close()
    c.drawPath(p, paint(mix(col, "#000000", 0.25), a))
    for k in range(4):
        line(c, cx - 60 + k * 36, cy - 32, cx - 46 + k * 36, cy - 58, "#FFFFFF", a, 5)


def b_midia(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COMEÇAR", "REPRESENTAÇÃO MIDIÁTICA", BLUE)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 200, 1480, 130, BLUE, aa, 0.06)
        text(c, "REPRESENTAÇÃO MIDIÁTICA", 260, 248, 22, "black", BLUE, aa, align="left", tracking=2)
        text(c, "o jeito como a mídia mostra alguma coisa", 260, 302, 38, "black", INK, aa, align="left")
    for k, (cue, fn, nm, d) in enumerate((("b", jornal, "noticiário", "= o jornal"),
                                          ("c", claquete, "ficção", "= histórias inventadas: filmes, séries, novelas"))):
        a, dy = rise(t, C["08." + cue])
        x = 220 + k * 760
        if a <= 0:
            continue
        rrect(c, x, 380 + dy, 720, 220, 20, "#FFFFFF", a, shadow=True)
        fn(c, x + 130, 490 + dy, a, BLUE)
        text(c, nm, x + 260, 470 + dy, 44, "black", BLUE, a, align="left")
        para(c, d, x + 260, 520 + dy, 26, "bold", INK2, a, 430, 32)
    ad = ep(t, C["08.d"], 0.4)
    if ad > 0:
        pill(c, "EIXO 2", 220, 700, PARTE["argumento"], size=26, a=ad, bounds=(0, 1920))
        text(c, "associam o adoecimento psíquico à VIOLÊNCIA", 380, 712, 36, "black", INK, ad, align="left")


# ======================================================================
# nós fazemos: questão 9
# ======================================================================

Q9 = ("A introdução de uma redação sobre o tema do Enem 2020 anunciou dois eixos: a desinformação sobre os transtornos e "
      "as representações midiáticas que os associam à violência. O primeiro parágrafo de desenvolvimento tratou da "
      "desinformação. A frase mais adequada para abrir o segundo é:")
ALT9 = [("A", "Em primeiro lugar, a desinformação sobre os transtornos mentais sustenta o estigma.", "09.A", "11.xa",
         "repete o 1º eixo", RED),
        ("B", "Portanto, cabe ao Ministério da Saúde criar campanhas sobre saúde mental.", "09.B", "11.xb",
         "salta para a proposta (conclusão)", RED),
        ("C", "Além disso, ao associar o adoecimento psíquico à violência, parte da mídia reforça a imagem de perigo que "
              "alimenta o estigma.", "10.C", None, "", GREEN),
        ("D", "A televisão foi inventada no início do século XX.", "10.D", "11.xd", "sem relação com o recorte", RED),
        ("E", "Por outro lado, a desinformação também é um problema.", "10.E", "11.xe",
         "“por outro lado” sem contraste + 1º eixo", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "NÓS FAZEMOS · QUESTÃO 9", "ABRINDO O SEGUNDO EIXO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.4)
    text(c, "QUESTÃO 9", 190, 230, 18, "black", GRAY, aa, align="left", tracking=2)
    para(c, Q9, 190, 285, 25, "black", INK, aa, 540, 34)
    alts_panel(c, t, C, ALT9, 790, 236, 950, 26, "11.ok", "C", 8)
    pause_timer(c, t, C["10.end"] - 1.9, 460, 720)
    ao = ep(t, C["11.ok"] + 1.0, 0.4)
    if ao > 0:
        rrect(c, 180, 640, 560, 150, 18, mix("#FFFFFF", PARTE["topico"], 0.10), ao)
        text(c, "a C abre o parágrafo:", 210, 690, 24, "black", INK2, ao, align="left")
        icone_etapa(c, "topico", 250, 745, ao, 0.55, disc=False)
        text(c, "vira a linha “Tópico”", 300, 756, 32, "black", PARTE["topico"], ao, align="left")
    questao_rotulo(c, aa)


# ======================================================================
# eu faço: as cinco linhas, com a 1ª tentativa imperfeita
# ======================================================================

def estado_eixo2(t, C):
    rv = [wreveal(t, span("12", "além disso, a mídia associa transtorno a violência", C, 3.5, "12.c")),
          wreveal(t, span("13", "noticiário e ficção destacam casos extremos, e isso gera imagem de perigo", C, 5.0, "13.b")),
          wreveal(t, span("14", "aqui entra um exemplo que você conhece de fato", C, 3.5, "14.d")),
          wreveal(t, span("18", "o público passa a temer quem tem diagnóstico, e isso leva ao isolamento e ao silêncio", C,
                          6.0, "18.b")),
          wreveal(t, span("16", "assim, a mídia reforça o estigma que afasta do tratamento", C, 4.0, "16.d"))]
    textos = [RASCUNHO[0][1], RASCUNHO[1][1], MARCADOR_REP, RASCUNHO[3][1], RASCUNHO[4][1]]
    return textos, rv


def b_eufaco(c, t, C, B):
    ids = ["12", "13", "14", "15", "16", "17", "18"]
    sid = which(t, C, ids)
    head_seq(c, t, C, [("12", "EU FAÇO · AO VIVO", "LINHA 1 · TÓPICO", GREEN), ("13", "EU FAÇO · AO VIVO", "LINHA 2 · POR QUÊ", GREEN),
                       ("14", "EU FAÇO · AO VIVO", "LINHA 3 · REPERTÓRIO", AMBER),
                       ("15", "EU FAÇO · AO VIVO", "POR QUE NÃO INVENTAR?", AMBER),
                       ("16", "1ª TENTATIVA", "COMO MUITA GENTE FAZ", AMBER), ("17", "1ª TENTATIVA", "E DAÍ?", RED),
                       ("18", "CORRIGINDO", "LINHA 4 · ANÁLISE", GREEN)])
    textos, rv = estado_eixo2(t, C)
    # lista à esquerda
    cur = {"12": 0, "13": 1, "14": 2, "15": 2, "16": 4 if t >= C["16.c"] else 3, "17": 3, "18": 3}[sid]
    if sid in ("12",) and t < C["12.b"]:
        cur = None
    hole = clamp(ep(t, C["17.e"], 0.3) * (1 - ep(t, C["18.b"], 0.3)))
    ok = [ep(t, C["12.c"] + 2.0, 0.3), ep(t, C["13.b"] + 3.0, 0.3), 0, ep(t, C["18.b"] + 3.0, 0.3), ep(t, C["16.d"] + 2.5, 0.3)]
    aberto = [0, 0, ep(t, C["14.d"] + 2.0, 0.3), 0, 0]
    falta = [0, 0, 0, hole, 0]
    lista(c, t, 1.0, cur=None if hole > 0 and cur == 3 else cur, ok=ok, falta=falta, aberto=aberto)
    lit = [0.0] * 5
    if cur is not None and hole <= 0:
        lit[cur] = 1.0
    sub = "As 5 linhas da seção 10 do material (exemplo do eixo 2: mídia)." if sid != "12" else None
    rascunho5(c, t, textos, rv, 1.0, "ENEM 2020 · D2 · EIXO DA MÍDIA", sub, AMBER, lit, rep_note=ep(t, C["14.b"], 0.4),
              hole=hole)
    if sid == "12":
        aa = ep(t, C["12.a"], 0.4) * (1 - ep(t, C["12.b"], 0.3))
        pill(c, "← a lista de compras: 1 linha por parte", LBX - 10, MY + 100, GREEN, size=22, a=aa, bounds=(0, 1920))
        ab = ep(t, C["12.b"], 0.4)
        pill(c, "da Questão 9, letra C", MX + MW - 40, MY + 100, PARTE["topico"], size=20, a=ab, anchor="right", bounds=(0, 1920))
    if sid == "13":
        ab = ep(t, C["13.a"], 0.4)
        pill(c, "por que procede?", MX + MW - 40, MY + 100, PARTE["argumento"], size=20, a=ab, anchor="right", bounds=(0, 1920))
        ac = ep(t, C["13.c"], 0.4)
        if ac > 0:
            lines = hwrap_arrow(textos[1], HS, CW)
            xa = CX + harrow_w(lines[0].split("→")[0].strip(), HS) + hand_w(" ", HS) * 1.2 + _aw(HS) / 2
            yb = linha_y(1)
            c.drawCircle(xa, yb - HS * 0.32, 34, paint(GREEN, ac, stroke=4))
            pill(c, "→ = causa e consequência", xa, yb + 46, GREEN, size=22, a=ac, anchor="center", bounds=(0, 1920))
    if sid == "14":
        ac = ep(t, C["14.c"], 0.4)
        pill(c, "NÃO invento nada", MX + MW - 40, MY + 100, RED, size=22, a=ac, anchor="right", bounds=(0, 1920))
    if sid == "15":
        o = ep(t, C["15.t"], 0.4)
        if o > 0:
            ox, oy, ow, oh = MX + 12, MY + 130, MW - 24, MH - 160
            rrect(c, ox, oy, ow, oh, 22, "#FFFFFF", o, shadow=True)
            icone_etapa(c, "repertorio", ox + 120, oy + 110, ep(t, C["15.a"], 0.4), 1.3)
            text(c, "repertório = a NOTA FISCAL do parágrafo", ox + 220, oy + 124, 40, "black", PARTE["repertorio"],
                 ep(t, C["15.a"], 0.4), align="left")
            ab = ep(t, C["15.b"], 0.4)
            selo(c, ox + 300, oy + 250, ab, "NOTA FISCAL FALSA", RED, -5, 36)
            para(c, "o corretor conhece a obra ou o caso → percebe o erro → o argumento perde a confiança", ox + 600, oy + 232,
                 30, "bold", INK2, ab, ow - 640, 38)
            acc = ep(t, C["15.c"], 0.4)
            text(c, "sem exemplo verdadeiro? OUTRO TIPO DE FUNDAMENTAÇÃO (o apoio do argumento):", ox + 60, oy + 370, 28,
                 "black", GREEN, acc, align="left")
            pill(c, "causa e consequência bem explicada", ox + 60, oy + 432, GREEN, size=30, a=ep(t, C["15.d"], 0.4),
                 bounds=(0, 1920))
            pill(c, "comparação entre situações", ox + 700, oy + 432, GREEN, size=30, a=ep(t, C["15.e"], 0.4), bounds=(0, 1920))
            af = ep(t, C["15.f"], 0.4)
            text(c, "simples, mas VERDADEIRO  >  inventado", ox + ow / 2, oy + 520, 46, "black", GREEN, af)
    if sid == "16":
        ab = ep(t, C["16.b"], 0.4)
        if ab > 0:
            y0, y1 = linha_y(2) - 10, linha_y(4) - 10
            p = skia.Path(); p.moveTo(MX + MW - 60, y0); p.cubicTo(MX + MW + 10, y0 + 40, MX + MW + 10, y1 - 40, MX + MW - 60, y1)
            c.drawPath(p, paint(AMBER, ab, stroke=5, cap_round=True))
            arrow(c, MX + MW - 40, y1 - 6, MX + MW - 62, y1, AMBER, ab, 5, 16)
            pill(c, "pulo direto para o fim", MX + MW - 80, linha_y(3) - 16, AMBER, size=22, a=ab * (1 - ep(t, C["16.d"], 0.3)),
                 anchor="right", bounds=(0, 1920))
        ae = ep(t, C["16.e"], 0.4)
        pill(c, "lista feita... será?", MX + MW - 40, MY + 100, AMBER, size=22, a=ae, anchor="right", bounds=(0, 1920))
    if sid == "17":
        aa = ep(t, C["17.a"], 0.4)
        bubble(c, "E DAÍ?", MX + MW - 430, MY + 40, 270, PARTE["fechamento"], aa * (1 - ep(t, C["17.d"], 0.3)), size=40)
        ad = ep(t, C["17.d"], 0.4)
        if ad > 0:
            y0, y1 = linha_y(2) - 10, linha_y(4) - 10
            p = skia.Path(); p.moveTo(MX + MW - 60, y0); p.cubicTo(MX + MW + 10, y0 + 40, MX + MW + 10, y1 - 40, MX + MW - 60, y1)
            c.drawPath(p, paint(RED, ad, stroke=5, cap_round=True))
            arrow(c, MX + MW - 40, y1 - 6, MX + MW - 62, y1, RED, ad, 5, 16)
            pill(c, "pulei do exemplo direto para o fecho!", MX + MW - 40, MY + 100, RED, size=22,
                 a=ad * (1 - ep(t, C["17.f"], 0.3)), anchor="right",
                 bounds=(0, 1920))
        af = ep(t, C["17.f"], 0.4)
        selo(c, MX + MW - 400, MY + 96, af, "NÃO ESTÁ PRONTO", RED, -4, 28)
    if sid == "18":
        aa = ep(t, C["18.a"], 0.4) * (1 - ep(t, C["18.c"], 0.3))
        pill(c, "quem é afetado, e de que forma?", MX + MW - 40, MY + 100, PARTE["analise"], size=22, a=aa, anchor="right",
             bounds=(0, 1920))
        ac = ep(t, C["18.c"], 0.4) * (1 - ep(t, C["18.e"], 0.3))
        pill(c, "diagnóstico = um profissional de saúde identifica o transtorno", MX + MW - 40, MY + 100, BLUE, size=20, a=ac,
             anchor="right", bounds=(0, 1920))
        ad = ep(t, C["18.d"], 0.4)
        icone_etapa(c, "analise", MX + 44, linha_y(3) - 10, ad, 0.42)
        selo(c, MX + MW - 320, MY + 100, ep(t, C["18.e"], 0.4), "LISTA PRONTA ✓", GREEN, -4, 28)


# ======================================================================
# lado a lado: 1ª tentativa × corrigida
# ======================================================================

def mini_lista(c, t, x, y, w, a, textos, ok, falta_k=None, lit=None, size=23, title="", tcol=INK, hole=0.0):
    rrect(c, x, y, w, 660, 22, PAPER, a, shadow=True)
    line(c, x + 60, y + 10, x + 60, y + 650, "#F3A6A6", a, 2.5)
    pill(c, title, x + 80, y + 48, tcol, size=22, a=a, bounds=(0, 1920))
    for k, (lab, _, key) in enumerate(RASCUNHO):
        yy = y + 112 + k * 112
        if lit and lit[k] > 0:
            rrect(c, x + 14, yy - 34, w - 28, 104, 12, mix("#FFFFFF", PARTE[key], 0.16), a * lit[k])
        hand(c, lab, x + 78, yy, 25, PARTE[key], a, bold=True)
        s = textos[k]
        if k == falta_k:
            bl = blink(t)
            dashed_box(c, x + 220, yy - 30, w - 300, 50, RED, a * bl)
            text(c, "vazia!", x + 240, yy + 2, 22, "black", RED, a * bl, align="left")
            check_icon(c, x + w - 44, yy - 6, 18, a * bl, RED, "x")
        else:
            if s == MARCADOR_REP:
                hpara_arrow(c, s, x + 210, yy, size, AMBER, a, w - 310, 36, bold=True)
            else:
                hpara_arrow(c, s, x + 210, yy, size, PEN, a, w - 280, 36)
            if ok:
                check_icon(c, x + w - 44, yy - 6, 18, a, AMBER if s == MARCADOR_REP else GREEN)


def b_lado(c, t, C, B):
    head(c, t, B["start"], "LADO A LADO · MESMA LISTA", "1ª TENTATIVA × CORRIGIDA", BLUE)
    textos = [RASCUNHO[0][1], RASCUNHO[1][1], MARCADOR_REP, RASCUNHO[3][1], RASCUNHO[4][1]]
    aa = ep(t, C["19.a"], 0.4)
    ab = ep(t, C["19.b"], 0.4)
    ac = ep(t, C["19.c"], 0.4)
    mini_lista(c, t, 140, 150, 800, 1.0, textos, True, falta_k=3, title="1ª TENTATIVA", tcol=RED,
               lit=[0, 0, aa * (1 - ab), 0, aa * (1 - ab)])
    mini_lista(c, t, 980, 150, 800, 1.0, textos, True, title="CORRIGIDA", tcol=GREEN,
               lit=[0, 0, 0, ab * (1 - ac), ac])
    if aa > 0:
        y0, y1 = 150 + 112 + 2 * 112 - 10, 150 + 112 + 4 * 112 - 10
        p = skia.Path(); p.moveTo(170, y0); p.cubicTo(110, y0 + 60, 110, y1 - 60, 170, y1)
        c.drawPath(p, paint(RED, aa, stroke=5, cap_round=True))
        arrow(c, 150, y1 - 8, 172, y1, RED, aa, 5, 16)
    pill(c, "o leitor fica sem saber o que aquilo prova", 540, 852, RED, size=22, a=aa, anchor="center", bounds=(0, 1920))
    pill(c, "consequência concreta: medo, isolamento, silêncio", 1380, 852, PARTE["analise"], size=22, a=ab * (1 - ac),
         anchor="center", bounds=(0, 1920))
    pill(c, "o fecho agora tem de onde sair", 1380, 852, GREEN, size=22, a=ac, anchor="center", bounds=(0, 1920))


# ======================================================================
# das cinco linhas ao parágrafo
# ======================================================================

PS, PL = 30, 45
TXP, TWP = MX + 110, MW - 170


def _plan_frases():
    out, y = [], MY + 160
    for k, s in enumerate(S_D2):
        lines = hwrap(s, PS, TWP, bold=(k == 2))
        out.append((y, lines))
        y += len(lines) * PL + 16
    return out


_PF = _plan_frases()


def b_frases(c, t, C, B):
    sid = which(t, C, ["20", "21"])
    head_seq(c, t, C, [("20", "EU FAÇO · EM VOZ ALTA", "CADA LINHA VIRA FRASE", GREEN),
                       ("21", "EU FAÇO · EM VOZ ALTA", "O 2º PARÁGRAFO", GREEN)])
    cues = [C["20.s1"], C["20.s2"], C["20.s3"], C["21.s4"], C["21.s5"]]
    k_at = max([k for k in range(5) if t >= cues[k] - 0.05] or [-1])
    lista(c, t, 1.0, cur=k_at if k_at >= 0 else None, ok=[1, 1, 0, 1, 1], aberto=[0, 0, 1, 0, 0])
    paper(c, MX, MY, MW, MH, 1.0, lh=PL, top=MY + 160 - 12 + 2)
    text(c, "ENEM 2020 · D2 · EIXO DA MÍDIA", TXP, MY + 62, 22, "black", BLUE, 1.0, align="left", tracking=1)
    text(c, PARAG_DIDATICO, TXP, MY + 98, 18, "medium", AMBER, 1.0, align="left")
    spoken = [S_D2[0], S_D2[1], None, S_D2[3], S_D2[4]]
    ends = [cues[1] - 0.5, cues[2] - 0.5, cues[2] + 2.5, cues[4] - 0.5, C["21.d"] - 0.4]
    for k, (y, lines) in enumerate(_PF):
        if t < cues[k] - 0.05:
            continue
        key = KEYS[k]
        sp = phrase_span("20" if k < 3 else "21", spoken[k], cues[k], ends[k]) if spoken[k] else (cues[k], ends[k])
        rv = wreveal(t, sp)
        h = len(lines) * PL
        rrect(c, TXP - 26, y - PS - 2, 8, h + 2, 4, PARTE[key], ep(t, cues[k], 0.3))
        icone_etapa(c, key, MX + 44, y - 8, ep(t, cues[k], 0.3), 0.36)
        hand_para(c, S_D2[k], TXP, y, PS, AMBER if k == 2 else PEN, 1.0, TWP, PL, rv, bold=(k == 2))
    ad = ep(t, C["21.d"], 0.4) if sid == "21" else 0
    selo(c, MX + MW - 390, MY + 90, ad, "REPERTÓRIO EM ABERTO", AMBER, -4, 26)


# ======================================================================
# equilíbrio entre os parágrafos
# ======================================================================

def barra(c, x, y, a, keys, unit, h=64, gap_k=None, gap_a=0.0, t=0.0):
    xx = x
    for key in KEYS:
        w = PESO[key] * unit
        if key in keys:
            rrect(c, xx, y, w - 6, h, 10, PARTE[key], a)
            xx += w
        elif key == gap_k and gap_a > 0:
            dashed_box(c, xx, y, w - 6, h, RED, a * gap_a * blink(t))
            text_mid(c, "análise?", xx + w / 2 - 3, y + h / 2, 22, "black", RED, a * gap_a * blink(t))
            xx += w
    return xx


def b_equilibrio(c, t, C, B):
    frame(c, t, B["start"], "DICA", "EQUILÍBRIO ENTRE OS PARÁGRAFOS", GREEN)
    at = ep(t, C["22.t"], 0.4)
    if at > 0:
        boxed(c, 220, 190, 1480, 110, GREEN, at, 0.06)
        text(c, "EQUILÍBRIO", 260, 232, 20, "black", GREEN, at, align="left", tracking=2)
        text(c, "os dois desenvolvimentos com tamanho parecido: os mais longos da redação", 260, 280, 30, "black", INK, at,
             align="left")
    unit = 330
    rows = [("22.a", "D1 · desinformação", KEYS, PARTE["topico"]), ("22.a", "D2 · corrigido", KEYS, PARTE["argumento"]),
            ("22.b", "D2 · 1ª tentativa", [k for k in KEYS if k != "analise"], RED)]
    for k, (cue, nm, keys, col) in enumerate(rows):
        a, d = rise(t, C[cue] + (0.4 if k == 1 else 0))
        y = 360 + k * 120 + d
        text(c, nm, 220, y + 42, 28, "black", col, a, align="left")
        gk = "analise" if k == 2 else None
        xend = barra(c, 560, y, a, keys, unit, 64, gk, ep(t, C["22.c"], 0.4) if k == 2 else 0, t)
        if k == 2 and a > 0:
            ab = ep(t, C["22.b"] + 0.8, 0.4) * (1 - ep(t, C["22.c"], 0.3))
            text(c, "mais curto!", xend + 20, y + 44, 30, "black", RED, ab, align="left")
    ac = ep(t, C["22.c"], 0.4)
    pill(c, "metade do outro = provavelmente falta ANÁLISE", W / 2, 740, RED, size=28, a=ac * (1 - ep(t, C["22.d"], 0.3)),
         anchor="center", bounds=(0, 1920))
    pill(c, "foi o buraco da nossa 1ª tentativa", W / 2, 740, AMBER, size=28, a=ep(t, C["22.d"], 0.4), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# recap, você faz, erros
# ======================================================================

FRASES = ["Cinco linhas antes do parágrafo.", "Linha vazia: parágrafo não está pronto.",
          "Repertório só o que você conhece de fato."]


def b_recap(c, t, C, B):
    recap(c, t, C, B, ("23", "31"), FRASES, cols=[GREEN, RED, AMBER])


def b_vocefaz(c, t, C, B):
    sid = which(t, C, ["24", "25", "26", "27"])
    head_seq(c, t, C, [("24", "VOCÊ FAZ · ENEM 2021", "A TESE", BLUE), ("25", "VOCÊ FAZ · ENEM 2021", "SUAS 5 LINHAS", AMBER),
                       ("26", "VOCÊ FAZ · ENEM 2021", "UM RASCUNHO POSSÍVEL", GREEN),
                       ("27", "VOCÊ FAZ · ENEM 2021", "UM RASCUNHO POSSÍVEL", GREEN)])
    if sid == "24":
        card(c, *CARD_R)
        aa = ep(t, C["24.a"], 0.4)
        text(c, "ENEM 2021", 220, 230, 22, "black", BLUE, ep(t, C["24.t"], 0.4), align="left", tracking=2)
        para(c, "“" + TEMA21 + "”", 220, 290, 36, "black", BLUE, ep(t, C["24.t"], 0.4), 1480, 46)
        pill(c, "registro civil = registro oficial de uma pessoa, feito no cartório", 220, 400, BLUE, size=24, a=aa,
             bounds=(0, 1920))
        ab = ep(t, C["24.b"], 0.4)
        if ab > 0:
            rrect(c, 200, 470, 1520, 300, 20, "#FFFFFF", ab, shadow=True)
            rrect(c, 200, 470, 10, 300, 5, MOV["tese"], ab)
            text(c, "A TESE (QUESTÃO 3 DO MATERIAL)", 240, 520, 20, "black", MOV["tese"], ab, align="left", tracking=2)
            sp = span("24", TESE21, C, 9.0, "24.b")
            para(c, "“" + TESE21 + "”", 240, 580, 34, "bold", INK, ab, 1440, 46)
            ex = ep(t, sp[0] + (sp[1] - sp[0]) * 0.55, 0.5)
            pill(c, "eixo: distância dos cartórios", 240, 735, PARTE["argumento"], size=22, a=ab * ex, bounds=(0, 1920))
            pill(c, "eixo: desinformação sobre a gratuidade", 640, 735, PARTE["argumento"], size=22,
                 a=ab * ep(t, sp[0] + (sp[1] - sp[0]) * 0.8, 0.5), bounds=(0, 1920))
        return
    if sid == "25":
        lista(c, t, 1.0, rows=[ep(t, C["25.b"] + 0.25 * k, 0.3) for k in range(5)])
        card(c, MX, MY, MW, MH)
        aa = ep(t, C["25.a"], 0.4)
        text(c, "SUA VEZ · EIXO", MX + 80, MY + 80, 22, "black", GRAY, aa, align="left", tracking=2)
        text(c, "distância dos cartórios", MX + 80, MY + 150, 52, "black", PARTE["argumento"], aa, align="left")
        steps = [("25.b", "1 · as cinco linhas de rascunho  ←"), ("25.c", "2 · confira: nenhuma linha vazia?"),
                 ("25.d", "3 · escreva o parágrafo")]
        for k, (cue, s) in enumerate(steps):
            a, d = rise(t, C[cue])
            text(c, s, MX + 80, MY + 280 + k * 80 + d, 36, "black", INK, a, align="left")
        pause_timer(c, t, C["25.p"] + 0.3, MX + MW / 2, MY + MH - 120, dur=2.0)
        return
    rv = [wreveal(t, span("26", "em primeiro lugar, a distância dos cartórios dificulta o registro em regiões isoladas", C,
                          5.0, "26.a")),
          wreveal(t, span("26", "cartório longe, viagem cara e demorada, e a família adia o registro", C, 4.0, "26.b")),
          ep(t, C["26.c"] + 0.4, 1.6),
          wreveal(t, span("27", "sem registro, a pessoa fica invisível para o Estado e longe da cidadania", C, 4.0, "27.d")),
          wreveal(t, span("27", "assim, a distância dos cartórios mantém parte dos brasileiros invisível para o Estado", C,
                          5.0, "27.e"))]
    cues = [C["26.a"], C["26.b"], C["26.c"], C["27.d"], C["27.e"]]
    k_at = max([k for k in range(5) if t >= cues[k] - 0.05] or [-1])
    ok = [ep(t, cues[k] + 2.5, 0.3) if k != 2 else 0 for k in range(5)]
    lista(c, t, 1.0, cur=k_at if k_at >= 0 and t < C["27.f"] else None, ok=ok, aberto=[0, 0, ep(t, cues[2] + 1.5, 0.3), 0, 0])
    lit = [0.0] * 5
    if 0 <= k_at and t < C["27.f"]:
        lit[k_at] = 1.0
    rascunho5(c, t, R21, rv, 1.0, "ENEM 2021 · EIXO: DISTÂNCIA DOS CARTÓRIOS", "Rascunho elaborado para fins didáticos.",
              AMBER, lit)
    ac = ep(t, C["26.c"] + 1.0, 0.4)
    text(c, "ou outra fundamentação verdadeira (ex.: causa e consequência)", CX, linha_y(2) + 34, 20, "bold", GREEN, ac,
         align="left")
    selo(c, MX + MW - 350, MY + 100, ep(t, C["27.f"], 0.4), "NENHUMA LINHA VAZIA", GREEN, -4, 26)
    pill(c, "5 linhas = no caminho ✓", MX + MW - 40, MY + MH - 26, GREEN, size=22, a=ep(t, C["27.g"], 0.4), anchor="right",
         bounds=(0, 1920))


ERROS = [("28", "Começar a escrever SEM RASCUNHO", "economiza tempo",
          "o buraco aparece na folha definitiva (a que vai para a correção), quando já não dá para consertar"),
         ("29", "INVENTAR um exemplo para preencher a linha", "a linha do repertório fica cheia",
          "nota fiscal falsa derruba a confiança: use o que conhece de fato ou outra fundamentação verdadeira"),
         ("30", "Deixar o 2º parágrafo MUITO MAIS CURTO que o 1º", "o tempo da prova está acabando",
          "metade do tamanho = provavelmente sem análise: confira a linha 4")]


def b_erros(c, t, C, B):
    erros(c, t, C, B, ERROS)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "ÚLTIMO EPISÓDIO DO ASSUNTO", "REVISÃO E DESAFIO", PURPLE)
    rows = [("32.b", "juntamos tudo", GREEN), ("32.c", "caçamos as PEGADINHAS", AMBER),
            ("32.d", "DESAFIO: os 2 desenvolvimentos da SUA redação", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 300, y - 16, a, 34, bg=col)
        para(c, s, 370, y, 52, "black", INK, a, 1300, 60)


def b_cta(c, t, C, B):
    cta_dev(c, t, C, "33", "Qual linha da sua lista costuma ficar vazia?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, material=b_material, lista=b_lista, prereq=b_prereq, midia=b_midia, q9=b_q9,
              eufaco=b_eufaco, lado=b_lado, frases=b_frases, equilibrio=b_equilibrio, recap=b_recap, vocefaz=b_vocefaz,
              erros=b_erros, ponte=b_ponte, cta=b_cta)
