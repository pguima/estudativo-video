"""Visual — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 2: descontos encadeados, preço original, promoções e faixas
(tema claro). Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: carimbo() (o fator batendo no preço), carrinho_tela() (a tela final do carrinho, linha por linha, com
o total mudando), etiqueta(), pacotes() (a conta do caixa: unidades pagas × levadas), predio() (as faixas de desconto como
andares sendo preenchidos), cartaz(), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum030", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_descontos_ep2_promocoes.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
CINZA_PAGO = "#E4E4E0"


def brl(v):
    """158.4 -> 'R$ 158,40' (milhar com ponto)"""
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + s


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def carimbo(c, s, cx, cy, a, col=None, rot=-8, size=40):
    """o fator 'carimbado': entra grande e bate no lugar"""
    if a <= 0:
        return
    col = col or PURPLE
    u = clamp(a)
    sc = lerp(1.9, 1.0, ease_io(clamp(u / 0.6))) + 0.08 * ease_back(clamp((u - 0.6) / 0.4)) * (1 - u)
    c.save(); c.translate(cx, cy); c.rotate(rot); c.scale(sc, sc)
    w = text_w(s, "black", size) + 48
    h = size * 1.7
    rrect(c, -w / 2, -h / 2, w, h, 12, mix("#FFFFFF", col, 0.10), u)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 12, 12), paint(col, u, stroke=5))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 8, -h / 2 + 8, w - 16, h - 16), 8, 8),
                paint(col, u * 0.6, stroke=2))
    text_mid(c, s, 0, 0, size, "black", col, u)
    c.restore()


def etiqueta(c, s, cx, cy, a, col=None, size=44, sub=None):
    """etiqueta de preço com o furinho à esquerda"""
    if a <= 0:
        return
    col = col or AMBER
    w = text_w(s, "black", size) + 110
    h = size * 2.0
    x = cx - w / 2
    p = skia.Path()
    p.moveTo(x + 40, cy - h / 2); p.lineTo(x + w - 14, cy - h / 2)
    p.quadTo(x + w, cy - h / 2, x + w, cy - h / 2 + 14); p.lineTo(x + w, cy + h / 2 - 14)
    p.quadTo(x + w, cy + h / 2, x + w - 14, cy + h / 2); p.lineTo(x + 40, cy + h / 2); p.lineTo(x, cy); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.22), a))
    c.drawPath(p, paint(col, a, stroke=4))
    c.drawCircle(x + 34, cy, 9, paint("#FFFFFF", a)); c.drawCircle(x + 34, cy, 9, paint(col, a, stroke=3))
    text_mid(c, s, cx + 22, cy, size, "black", INK, a)
    if sub:
        text(c, sub, cx + 22, cy + h / 2 + 34, 24, "bold", GRAY, a)


def carrinho_tela(c, t, x, y, w, base, rows, cues, a, titulo="CARRINHO"):
    """tela final de compra. rows = [(rótulo, '× 0,80', fator, cor)]; cues = instante do carimbo de cada linha.
    O total começa no preço de etiqueta (base) e muda a cada carimbo."""
    if a <= 0:
        return
    h = 140 + len(rows) * 96 + 150
    rrect(c, x, y, w, h, 26, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 70, 26, BLUE, a * 0.12)
    text(c, titulo, x + 36, y + 47, 28, "black", BLUE, a, align="left", tracking=2)
    text(c, "etiqueta", x + 36, y + 120, 30, "bold", INK2, a, align="left")
    text(c, brl(base), x + w - 36, y + 120, 34, "black", INK, a, align="right")
    v = base
    for k, (lbl, fs, f, col) in enumerate(rows):
        yy = y + 140 + k * 96 + 48
        line(c, x + 30, yy - 48, x + w - 30, yy - 48, "#ECECE8", a, 2)
        text(c, lbl, x + 36, yy + 10, 30, "bold", INK2, a, align="left")
        u = ep(t, cues[k], 0.5)
        if u > 0:
            carimbo(c, fs, x + w - 150, yy, a * u, col, -6 if k % 2 else 6, 30)
            v *= f if u >= 0.5 else 1
    yt = y + h - 80
    line(c, x + 30, yt - 50, x + w - 30, yt - 50, INK, a, 3)
    text(c, "TOTAL", x + 36, yt + 12, 34, "black", INK, a, align="left")
    fim = all(t >= cc + 0.25 for cc in cues)
    text(c, brl(v), x + w - 36, yt + 14, 46, "black", GREEN if fim else INK, a, align="right")
    return v


def pacote(c, cx, cy, s, a, frac=1.0, col=None, gratis=False):
    """um pacote; frac = parte paga (1 = cheio, 0,5 = metade, 0 = grátis)"""
    if a <= 0:
        return
    col = col or BLUE
    x, y, w, h = cx - s * 0.42, cy - s * 0.55, s * 0.84, s * 1.1
    rrect(c, x, y, w, h, s * 0.1, CINZA_PAGO, a)
    if frac > 0:
        hh = h * frac
        c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y + h - hh, w, hh))
        rrect(c, x, y, w, h, s * 0.1, col, a)
        c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), s * 0.1, s * 0.1), paint(INK2, a, stroke=3))
    rrect(c, cx - s * 0.18, y - s * 0.1, s * 0.36, s * 0.16, s * 0.05, INK2, a)
    if gratis:
        text_mid(c, "GRÁTIS", cx, cy, s * 0.2, "black", GREEN, a)


def pacotes(c, cx, cy, fracs, s, a, gap=None, cols=None, gratis_txt=True):
    gap = gap or s * 1.05
    n = len(fracs)
    for k, f in enumerate(fracs):
        x = cx + (k - (n - 1) / 2) * gap
        pacote(c, x, cy, s, a, f, (cols or {}).get(k), gratis=(f == 0 and gratis_txt))


def cartaz(c, l1, l2, cx, cy, w, h, a, col=RED, rot=-3):
    """cartaz de promoção de supermercado"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    rrect(c, -w / 2, -h / 2, w, h, 18, "#FFF6C9", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 18, 18), paint(col, a, stroke=6))
    s1 = h * 0.2
    while text_w(l1, "black", s1) > w - 50:
        s1 -= 2
    text_mid(c, l1, 0, -h * 0.16, s1, "black", col, a)
    s2 = h * 0.125
    while text_w(l2, "black", s2) > w - 50:
        s2 -= 2
    text_mid(c, l2, 0, h * 0.22, s2, "black", INK, a)
    c.restore()


ANDARES = [("TÉRREO", "até R$ 200", "0%", GRAY), ("1º ANDAR", "de R$ 200 a R$ 400", "5%", BLUE),
           ("COBERTURA", "acima de R$ 400", "10%", GREEN)]


def predio(c, x, y_chao, w, hf, a, nivel, partes=(None, None, None), alf=(1, 1, 1), topo=200, mini=False):
    """três andares (0%, 5%, 10%), cada um valendo R$ 200 de altura (a cobertura mostra 'topo' reais).
    nivel = reais já 'enchidos' (0 → 600). partes = texto à direita de cada andar (conta da faixa)."""
    if a <= 0:
        return
    for k, (nm, faixa, tx, col) in enumerate(ANDARES):
        y = y_chao - (k + 1) * hf
        cap = 200 if k < 2 else topo
        rrect(c, x, y + 4, w, hf - 8, 14, "#F7F7F5", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y + 4, w, hf - 8), 14, 14), paint(col, a, stroke=4))
        cheio = clamp((nivel - 200 * k) / cap)
        if cheio > 0:
            hh = (hf - 8) * cheio
            c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y + 4 + (hf - 8) - hh, w, hh))
            rrect(c, x, y + 4, w, hf - 8, 14, mix("#FFFFFF", col, 0.35), a)
            c.restore()
        if mini:
            text_mid(c, tx, x + w / 2, y + hf / 2, 40, "black", col, a)
        else:
            text(c, nm, x + 26, y + 46, 24, "black", col, a, align="left", tracking=1)
            text(c, faixa, x + 26, y + 82, 22, "bold", INK2, a, align="left")
            text_mid(c, tx, x + w - 70, y + hf / 2, 50, "black", col, a)
        if partes[k]:
            text(c, partes[k], x + w + 40, y + hf / 2 + 14, 36, "black", col if k else INK2, a * alf[k], align="left")
    # telhado
    yt = y_chao - 3 * hf
    p = skia.Path(); p.moveTo(x - 20, yt + 4); p.lineTo(x + w / 2, yt - 60); p.lineTo(x + w + 20, yt + 4); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", INK2, 0.18), a))


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def barra_pct(c, x, y, w, h, frac, a, col=BLUE, rot_paga="paga", rot_desc="desconto"):
    """barra de 100% dividida em parte paga e desconto"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 12, mix("#FFFFFF", GREEN, 0.25), a)
    rrect(c, x, y, w * frac, h, 12, col, a)
    text_mid(c, rot_paga, x + w * frac / 2, y + h / 2, 30, "black", "#FFFFFF", a)
    if frac < 0.93:
        text_mid(c, rot_desc, x + w * (1 + frac) / 2, y + h / 2, 30, "black", GREEN, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DESCONTOS, ACRÉSCIMOS, LUCRO E PREJUÍZO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    cartaz(c, "2ª UNIDADE", "com 50% de desconto", 560, 430, 560, 280, aa, RED, -3)
    ab = ep(t, C["01.b"], 0.5)
    cartaz(c, "30% OFF", "em cada unidade", 1360, 430, 560, 280, ab, BLUE, 3)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        text_mid(c, "?", W / 2, 430, 140, "black", AMBER, acc * (1 - ep(t, C["01.e"], 0.4)))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "parece imbatível...", 560, 640, AMBER, size=30, a=ad, anchor="center")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, 560, 730, ae, "DÁ SÓ 25%", RED, -4, 40)
        selo(c, 1360, 730, ep(t, C["01.e"] + 1.2, 0.4), "30% DE VERDADE", GREEN, 4, 40)
    af = ep(t, C["01.f"], 0.5)
    if af > 0:
        regra(c, "hoje: DESMASCARAR PROMOÇÃO", W / 2, 840, af, 38, PURPLE)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "encadear descontos e acréscimos", "liquidação · Pix · frete"),
            ("02.b", "recuperar o preço original", "antes do desconto"),
            ("02.c", "comparar promoções", "leve 3, pague 2 · 2ª com 50%"),
            ("02.d", "calcular descontos por faixa", "o desconto progressivo")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + j * 140 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 52, 30, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "30 SEGUNDOS DE REVISÃO", "DA SÉRIE DE PORCENTAGEM", GREEN)
    cols = [("03.a", "FATOR", BLUE, [("+15%", "× 1,15"), ("−30%", "× 0,70")]),
            ("03.b", "EM SEQUÊNCIA", PURPLE, [("−20% e −10%", "× 0,8 × 0,9"), ("", "= × 0,72 → 28%")]),
            ("03.c", "VOLTAR", AMBER, [("R$ 84 com −30%", "84 ÷ 0,70"), ("", "= R$ 120")])]
    for k, (cue, tit, col, items) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 250, 460, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250, 460, 70, 24, col, a * 0.14)
        text(c, tit, x + 230, 297, 32, "black", col, a, tracking=2)
        for j, (l1, l2) in enumerate(items):
            yy = 420 + j * 160
            if l1:
                text(c, l1, x + 230, yy, 36, "bold", INK2, a)
            text(c, l2, x + 230, yy + 64, 46, "black", INK if j == 0 or k == 0 else col, a)
    if ep(t, C["03.b"], 0.5) > 0:
        pill(c, "multiplique os fatores", 220 + 510 + 230, 770, PURPLE, size=26, a=ep(t, C["03.b"] + 1.5, 0.4),
             anchor="center")
    if ep(t, C["03.c"], 0.5) > 0:
        pill(c, "divida pelo fator", 220 + 1020 + 230, 770, AMBER, size=26, a=ep(t, C["03.c"] + 1.0, 0.4), anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS CENAS DE COMPRA", "TRÊS JEITOS DE ESCREVER DESCONTO", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"], 0.5)
    if a1 > 0:
        rrect(c, 200, 240, 480, 440, 24, "#FFFFFF", a1, shadow=True)
        rrect(c, 200, 240, 480, 64, 24, BLUE, a1 * 0.12)
        text(c, "CARRINHO ON-LINE", 440, 283, 26, "black", BLUE, a1, tracking=1)
        for j, (l, v, col) in enumerate((("etiqueta", "R$ 300", INK), ("cupom", "−20%", RED), ("Pix", "−5%", RED),
                                         ("frete", "+10%", AMBER))):
            yy = 360 + j * 70
            text(c, l, 240, yy, 30, "bold", INK2, a1, align="left")
            text(c, v, 640, yy, 32, "black", col, a1, align="right")
        text(c, "TOTAL = ?", 440, 650, 36, "black", INK, a1)
    a2 = ep(t, C["04.b"], 0.5)
    cartaz(c, "LEVE 3", "PAGUE 2", 960, 460, 420, 300, a2, RED, -3)
    a3 = ep(t, C["04.c"], 0.5)
    if a3 > 0:
        rrect(c, 1240, 240, 480, 440, 24, "#FFFFFF", a3, shadow=True)
        rrect(c, 1240, 240, 480, 64, 24, GREEN, a3 * 0.14)
        text(c, "MATERIAL DE CONSTRUÇÃO", 1480, 283, 24, "black", GREEN, a3, tracking=1)
        text(c, "DESCONTO PROGRESSIVO", 1480, 360, 30, "black", INK, a3)
        for j, (s, hh) in enumerate((("0%", 80), ("5%", 150), ("10%", 220))):
            x = 1300 + j * 135
            rrect(c, x, 640 - hh, 110, hh, 10, mix("#FFFFFF", GREEN, 0.2 + 0.25 * j), a3)
            text_mid(c, s, x + 55, 640 - hh / 2, 32, "black", GREEN, a3)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "traduzir os três para a MESMA língua", W / 2, 770, ad, 36, PURPLE)


# ======================================================================
# bloco a — carimbos (encadeados com acréscimo no meio)
# ======================================================================

def b_carimbos(c, t, C, B):
    head_seq(c, t, C, [("05", "DESCONTOS ENCADEADOS", "COM ACRÉSCIMO NO MEIO", PURPLE),
                       ("06", "E SE A ORDEM MUDAR?", "OS CARIMBOS TROCAM DE LUGAR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        etiqueta(c, "R$ 200,00", 470, 330, aa, AMBER, 50, "preço de etiqueta")
        rows = [("liquidação  −20%", "× 0,80", 0.80, RED), ("Pix  −10%", "× 0,90", 0.90, RED),
                ("frete  +10%", "× 1,10", 1.10, AMBER)]
        carrinho_tela(c, t, 900, 220, 800, 200, rows, [C["05.c"] + 0.3, C["05.c"] + 2.4, C["05.d"] + 0.3], aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            boxed(c, 220, 470, 560, 210, BLUE, ab, 0.08)
            text(c, "CARIMBO = FATOR", 500, 530, 34, "black", BLUE, ab)
            text(c, "cada % multiplica o preço", 500, 580, 26, "bold", INK2, ab)
            text(c, "DESCONTOS ENCADEADOS:", 500, 632, 26, "black", BLUE, ab)
            text(c, "um carimbo atrás do outro", 500, 666, 24, "bold", INK2, ab)
        ac = ep(t, C["05.c"] + 3.2, 0.4)
        if ac > 0:
            linha(c, [("200 × 0,80 × 0,90 = ", INK), ("144", BLUE)], 500, 750, 38, ac)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            pill(c, "10% do valor JÁ descontado: 144 × 1,10", 500, 820, AMBER, size=24, a=ad, anchor="center")
        return
    rows = [("frete  +10%", "× 1,10", 1.10, AMBER), ("liquidação  −20%", "× 0,80", 0.80, RED),
            ("Pix  −10%", "× 0,90", 0.90, RED)]
    aa = ep(t, C["06.a"], 0.5)
    carrinho_tela(c, t, 900, 220, 800, 200, rows, [C["06.a"] + 0.6, C["06.a"] + 2.0, C["06.a"] + 3.4], ep(t, C["06"], 0.5),
                  "CARRINHO · OUTRA ORDEM")
    if aa > 0:
        linha(c, [("200 × 1,10 = 220", INK2)], 500, 330, 38, ep(t, C["06.a"] + 1.0, 0.4))
        linha(c, [("220 × 0,80 = 176", INK2)], 500, 410, 38, ep(t, C["06.a"] + 2.4, 0.4))
        linha(c, [("176 × 0,90 = ", INK2), ("158,40", GREEN)], 500, 490, 38, ep(t, C["06.a"] + 3.8, 0.4))
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        selo(c, 500, 620, ab, "O MESMO R$ 158,40", GREEN, -4, 40)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        regra(c, "carimbos se MULTIPLICAM · a ordem não muda", W / 2, 830, acc, 34)


def b_atalho1(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "UM FATOR SÓ", GREEN)
    a0 = ep(t, C["07"], 0.5)
    K.atalho(c, 260, 220, 1400, 120, "ATALHO", ["junte os carimbos ANTES de mexer no preço"], a0, 38)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        u = ep(t, C["07.a"] + 1.6, 1.0)
        for k, (s, col) in enumerate((("× 0,80", RED), ("× 0,90", RED), ("× 1,10", AMBER))):
            x0 = 520 + k * 300
            carimbo(c, s, lerp(x0, W / 2, u), 470, aa * (1 - u * 0.999), col, (-6, 5, -3)[k], 40)
        if u > 0:
            carimbo(c, "× 0,792", W / 2, 470, u, GREEN, -4, 60)
            text(c, "FATOR TOTAL", W / 2, 590, 30, "black", GREEN, u)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("R$ 200,00 × 0,792 = ", INK), ("R$ 158,40", GREEN)], W / 2, 690, 54, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "uma multiplicação só no preço", W / 2, 800, GREEN, size=30, a=acc, anchor="center")


# ======================================================================
# blocos b e c — desconto total equivalente, voltar ao preço
# ======================================================================

def b_equivalente(c, t, C, B):
    frame(c, t, B["start"], "DOIS DESCONTOS DE 10%", "DÃO 20%?", PURPLE)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("0,9 × 0,9 = ", INK), ("0,81", BLUE)], 560, 280, 56, aa)
        barra_pct(c, 260, 350, 600, 80, 0.81, ep(t, C["08.a"] + 1.4, 0.5), BLUE, "paga 81%", "19%")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        boxed(c, 1000, 240, 700, 260, BLUE, ab, 0.08)
        text(c, "DESCONTO TOTAL EQUIVALENTE", 1350, 296, 30, "black", BLUE, ab, tracking=1)
        text(c, "o desconto único com o mesmo efeito", 1350, 340, 26, "bold", INK2, ab)
        linha(c, [("1 − produto dos fatores", PURPLE)], 1350, 410, 40, ab)
        linha(c, [("1 − 0,81 = ", INK), ("19%", GREEN)], 1350, 470, 40, ep(t, C["08.b"] + 2.0, 0.4))
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 560, 1440, 200, 24, "#F7F7F5", acc)
        text(c, "−25% e −20%", 560, 620, 40, "black", INK2, acc)
        linha(c, [("0,75 × 0,8 = 0,6", INK)], 560, 700, 44, acc)
        linha(c, [("1 − 0,6 = ", INK), ("40%", GREEN)], 1150, 660, 60, ep(t, C["08.c"] + 1.8, 0.4))
        an = ep(t, C["08.c"] + 3.0, 0.4)
        if an > 0:
            text(c, "45%", 1520, 680, 52, "black", RED, an)
            strike(c, 1470, 660, 1570, 660, an, RED, an)


def b_voltar(c, t, C, B):
    frame(c, t, B["start"], "VOLTAR AO PREÇO", "DEPOIS DE +25%", AMBER)
    a0 = ep(t, C["09"], 0.5)
    # duas barras: 100 → 125
    if a0 > 0:
        g = ep(t, C["09"] + 0.6, 0.8)
        rrect(c, 300, 300, 400, 70, 12, BLUE, a0)
        text_mid(c, "100", 500, 335, 36, "black", "#FFFFFF", a0)
        arrow(c, 500, 390, 500, 440, AMBER, a0 * g, 5, 14)
        text(c, "× 1,25", 610, 430, 30, "black", AMBER, a0 * g, align="left")
        rrect(c, 300, 460, 500 * g, 70, 12, mix(BLUE, AMBER, 0.4), a0 * g)
        text_mid(c, "125", 300 + 250 * g, 495, 36, "black", "#FFFFFF", a0 * g)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        arrow(c, 500, 550, 500, 600, PURPLE, aa, 5, 14)
        text(c, "÷ 1,25", 610, 590, 30, "black", PURPLE, aa, align="left")
        rrect(c, 300, 620, 400, 70, 12, BLUE, aa)
        text_mid(c, "100 de novo", 500, 655, 32, "black", "#FFFFFF", aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        boxed(c, 980, 260, 700, 250, PURPLE, ab, 0.08)
        linha(c, [("÷ 1,25  =  × 0,8", PURPLE)], 1330, 330, 50, ab)
        linha(c, [("→ desconto de ", INK), ("20%", GREEN), (" basta", INK)], 1330, 410, 40, ab)
        linha(c, [("1,25 × 0,8 = ", INK), ("1", GREEN)], 1330, 475, 40, ep(t, C["09.b"] + 2.4, 0.4))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        boxed(c, 980, 560, 700, 170, AMBER, acc, 0.08)
        linha(c, [("+20% e −20%:  1,2 × 0,8 = ", INK), ("0,96", RED)], 1330, 620, 36, acc)
        text(c, "termina 4% ABAIXO (visto em Porcentagem)", 1330, 690, 26, "black", AMBER, acc)


# ======================================================================
# blocos d e e — desconto efetivo
# ======================================================================

def b_efetivo(c, t, C, B):
    head_seq(c, t, C, [("10", "LEVE 3, PAGUE 2", "QUANTO DE DESCONTO?", BLUE),
                       ("11", "2ª UNIDADE COM 50%", "A PROMOÇÃO DO GANCHO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            boxed(c, 220, 220, 1480, 150, BLUE, aa, 0.08)
            text(c, "DESCONTO EFETIVO: o desconto real, em % do preço cheio", W / 2, 278, 34, "black", BLUE, aa)
            linha(c, [("a CONTA DO CAIXA:  ", INK2), ("quanto você PAGA ÷ quanto você LEVA", PURPLE)], W / 2, 330, 30, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            pacotes(c, 520, 530, [1, 1, 0], 130, ab)
            linha(c, [("paga 2 de 3  →  desconto ", INK), ("1/3 ≈ 33,3%", GREEN)], 520, 690, 34, ep(t, C["10.b"] + 1.2, 0.4))
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            pacotes(c, 1360, 530, [1, 1, 1, 0], 110, acc)
            text(c, "LEVE 4, PAGUE 3", 1360, 420, 30, "black", RED, acc)
            linha(c, [("paga 3 de 4  →  desconto ", INK), ("25%", GREEN)], 1360, 690, 34, ep(t, C["10.c"] + 1.0, 0.4))
        if ab > 0:
            text(c, "LEVE 3, PAGUE 2", 520, 420, 30, "black", RED, ab)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        pacotes(c, 480, 450, [1, 0.5], 170, aa, gap=200, gratis_txt=False)
        text(c, "R$ 10", 380, 600, 34, "black", INK, aa)
        text(c, "R$ 5", 580, 600, 34, "black", INK, aa)
        linha(c, [("paga ", INK), ("R$ 15", BLUE), (" de R$ 20 = ", INK), ("75%", BLUE)], 480, 680, 38,
              ep(t, C["11.a"] + 1.6, 0.4))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        selo(c, 480, 780, ab, "DESCONTO EFETIVO: 25%", GREEN, -3, 36)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rows = [("leve 3, pague 2", "33,3%"), ("leve 4, pague 3", "25%"), ("2ª com 50%", "25%"), ("2ª grátis", "50%"),
                ("2ª com 30%", "15%")]
        rrect(c, 920, 230, 780, 450, 22, "#FFFFFF", acc, shadow=True)
        text(c, "PROMOÇÃO", 1100, 280, 24, "black", GRAY, acc, tracking=1)
        text(c, "DESCONTO EFETIVO", 1500, 280, 24, "black", GRAY, acc, tracking=1)
        for j, (p_, d_) in enumerate(rows):
            yy = 350 + j * 68
            aj = acc * ep(t, C["11.c"] + 0.2 * j, 0.3)
            text(c, p_, 1100, yy, 32, "bold", INK, aj)
            text(c, d_, 1500, yy, 36, "black", GREEN, aj)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        linha(c, [("no gancho:  ", INK2), ("30% em cada", GREEN), ("  >  ", INK), ("2ª com 50% = 25%", RED)], 1310, 760, 34,
              ad)


def b_quantidade(c, t, C, B):
    frame(c, t, B["start"], "LEVE 3, PAGUE 2", "E SE VOCÊ LEVAR 4?", AMBER)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        pacotes(c, 700, 420, [1, 1, 0, 1], 150, aa, gap=180, cols={3: AMBER})
        boxed(c, 700 - 270 - 90, 300, 540 + 150, 240, RED, aa * 0.8, 0.0, 20, 3)
        text(c, "a promoção: de 3 em 3", 700 - 90, 590, 28, "black", RED, aa)
        text(c, "preço cheio", 700 + 270, 590, 28, "black", AMBER, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        boxed(c, 1180, 280, 520, 260, BLUE, ab, 0.08)
        text(c, "pacote de R$ 10", 1440, 340, 30, "bold", INK2, ab)
        linha(c, [("leva 4: ", INK), ("R$ 40", INK)], 1440, 410, 40, ab)
        linha(c, [("paga: ", INK), ("R$ 30", BLUE)], 1440, 480, 40, ep(t, C["12.b"] + 1.4, 0.4))
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        linha(c, [("desconto efetivo: ", INK), ("25%", GREEN)], 700, 690, 52, acc)
        text(c, "33,3%", 1300, 700, 46, "black", RED, acc)
        strike(c, 1230, 684, 1370, 684, acc, RED, acc)
        pill(c, "depende de QUANTAS você compra", W / 2, 800, AMBER, size=30, a=ep(t, C["12.c"] + 2.0, 0.4),
             anchor="center")


def b_atalho2(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "PROMOÇÃO POR QUANTIDADE", GREEN)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        boxed(c, 360, 230, 1200, 280, GREEN, aa, 0.08)
        text(c, "ATALHO", W / 2, 275, 22, "black", GREEN, aa, tracking=2)
        text_mid(c, "desconto efetivo  =  1  −", 840, 400, 52, "black", INK, aa)
        fr(c, "pagas", "levadas", 1310, 390, 56, INK, aa, num_col=BLUE, den_col=GREEN)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        pill(c, "conte em UNIDADES", W / 2, 470, GREEN, size=26, a=ab, anchor="center")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        for k, (n_, d_, res, nm) in enumerate((("2", "3", "33,3%", "leve 3, pague 2"), ("1,5", "2", "25%", "2ª com 50%"))):
            x = 620 + k * 680
            ak = ep(t, C["13.c"] + 0.4 + 1.4 * k, 0.4)
            text(c, nm, x, 600, 28, "bold", GRAY, ak)
            text_mid(c, "1 −", x - 150, 700, 48, "black", INK, ak)
            fr(c, n_, d_, x - 40, 690, 52, INK, ak)
            text_mid(c, "= " + res, x + 130, 700, 48, "black", GREEN, ak)
        pill(c, "nem precisa do preço", W / 2, 800, GREEN, size=28, a=ep(t, C["13.c"] + 3.4, 0.4), anchor="center")


# ======================================================================
# bloco f — desconto por faixa (o prédio)
# ======================================================================

def b_faixa(c, t, C, B):
    head_seq(c, t, C, [("14", "DESCONTO POR FAIXA", "O PRÉDIO DO DESCONTO", BLUE),
                       ("15", "E 10% EM TUDO?", "A TAXA NÃO DESCE", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            boxed(c, 1180, 230, 520, 170, BLUE, aa, 0.08)
            text(c, "DESCONTO POR FAIXA", 1440, 285, 30, "black", BLUE, aa, tracking=1)
            text(c, "cada PARTE do valor ganha", 1440, 330, 26, "bold", INK2, aa)
            text(c, "a taxa da SUA faixa", 1440, 368, 26, "bold", INK2, aa)
        ab = ep(t, C["14.b"], 0.5)
        nivel = 500 * ep(t, C["14.c"], 2.0)
        alf = (ep(t, C["14.d"], 0.4), ep(t, C["14.d"] + 1.2, 0.4), ep(t, C["14.d"] + 2.4, 0.4))
        predio(c, 260, 790, 560, 150, ab, nivel, ("200 × 0% = 0", "200 × 5% = R$ 10", "100 × 10% = R$ 10"), alf, topo=200)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            text(c, "compra de R$ 500", 540, 830, 30, "black", INK, acc)
        ad = ep(t, C["14.d"] + 3.4, 0.4)
        if ad > 0:
            selo(c, 1440, 780, ad, "DESCONTO: R$ 20", GREEN, -3, 40)
        return
    predio(c, 260, 790, 560, 150, ep(t, C["15"], 0.4), 500,
           ("200 × 0% = 0", "200 × 5% = R$ 10", "100 × 10% = R$ 10"), (1, 1, 1))
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 1280, 260, 440, 200, RED, aa, 0.08)
        text(c, "10% de R$ 500", 1500, 330, 34, "black", RED, aa)
        text(c, "= R$ 50", 1500, 400, 50, "black", RED, aa)
        strike(c, 1320, 395, 1680, 395, ep(t, C["15.a"] + 1.4, 0.4), RED, aa)
        text(c, "mais que o DOBRO de R$ 20", 1500, 500, 26, "black", RED, ep(t, C["15.a"] + 1.4, 0.4))
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        regra(c, "a taxa do último andar NÃO DESCE", 1500, 620, ab, 28, PURPLE)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        pill(c, "funções definidas por partes: série própria", 1500, 730, BLUE, size=22, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "A CONTA DO CAIXA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    cartaz(c, "LEVE 5", "PAGUE 4", 560, 400, 420, 260, aa, RED, -3)
    if aa > 0:
        text(c, "desconto efetivo = ?", 1250, 410, 54, "black", INK, aa)
    pause_timer(c, t, C["16.end"] - 1.9, 1250, 560)
    if t < C["17"]:
        return
    a1 = ep(t, C["17.a"], 0.5)
    if a1 > 0:
        pacotes(c, 1250, 560, [1, 1, 1, 1, 0], 100, a1, gap=120)
        linha(c, [("paga 4 de 5 = ", INK), ("80%", BLUE)], 1250, 700, 40, ep(t, C["17.a"] + 1.0, 0.4))
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        selo(c, 560, 680, ab, "DESCONTO: 20%", GREEN, -3, 44)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        pill(c, "mais unidades por brinde → desconto MENOR", W / 2, 800, AMBER, size=28, a=acc, anchor="center")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Descontos e acréscimos em sequência: multiplique os fatores.",
          "Para voltar ao preço original, divida pelo fator.",
          "Toda promoção vira desconto efetivo antes da comparação."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Somar descontos sucessivos: 30% e 10% = 40%", "os dois descontos são do mesmo produto",
          "o 2º incide sobre um preço menor: 0,7 × 0,9 = 0,63 → 37%"),
         ("Voltar somando: R$ 68 depois de −15%, +15% = R$ 78,20", "pôr de volta os 15% parece desfazer",
          "os 15% eram do preço ANTIGO: 68 ÷ 0,85 = R$ 80"),
         ("Ler \"50% na segunda\" como 50% de desconto", "o 50 está enorme no cartaz",
          "vale para 1 unidade em 2: sobre o par, 25%"),
         ("A taxa da faixa mais alta sobre o valor todo", "a compra chegou na faixa dos 10%",
          "os 10% só pegam a parte que passou dos R$ 400")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21", "22"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTSN = [("A", "R$ 228,00", "esqueceu o frete", RED), ("B", "R$ 247,50", "somou os descontos", RED),
         ("C", "R$ 250,80", "", GREEN), ("D", "R$ 255,00", "somou tudo: −15%", RED),
         ("E", "R$ 258,00", "frete sobre a etiqueta", RED)]


def b_qn(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "LIQUIDAÇÃO, PIX E FRETE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4) * (1 - ep(t, C["24"], 0.4))
    _enunciado(c, [("Um produto tem preço de etiqueta de R$ 300,00. Na liquidação, há 20% de desconto; quem paga com Pix "
                    "ganha mais 5% de desconto sobre o valor já reduzido; e a entrega acrescenta 10% de frete sobre o "
                    "valor pago pelo produto. O cliente que compra com Pix e com entrega paga, no total,", INK)],
               a0, 240, 26)
    text(c, "Questão nova, no estilo do ENEM", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTSN, 1000, 250, 680, 42, C["24.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["24"]:
        a1 = ep(t, C["24"], 0.4)
        _painel(c, 230, a1)
        text(c, "R$ 300,00", 540, 300, 40, "black", INK, a1)
        for k, (s, col) in enumerate((("× 0,80", RED), ("× 0,95", RED), ("× 1,10", AMBER))):
            carimbo(c, s, 300 + k * 240, 400, ep(t, C["24.a"] + 1.2 * k, 0.5), col, (-6, 5, -4)[k], 32)
        linha(c, [("fator total: ", INK), ("0,836", PURPLE)], 540, 520, 40, ep(t, C["24.b"], 0.4))
        linha(c, [("300 × 0,836 = ", INK), ("R$ 250,80", GREEN)], 540, 620, 40, ep(t, C["24.c"], 0.4))
        conferido(c, "abaixo de R$ 300: plausível", 230, 730, ep(t, C["24.d"], 0.4), True, 28)


ALTS6 = [("A", "R$ 86,70", "descontou de novo", RED), ("B", "R$ 117,00", "somou 15 reais", RED),
         ("C", "R$ 117,30", "+15% sobre 102", RED), ("D", "R$ 120,00", "", GREEN),
         ("E", "R$ 680,00", "dividiu por 0,15", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "O PREÇO ANTES DO DESCONTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    yend = _enunciado(c, [("Após um desconto de 15%, uma camiseta passou a custar R$ 102,00. O preço da camiseta antes "
                           "do desconto era", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS6, 1000, 250, 680, 42, C["27.ok"], "D", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["26.end"] - 1.9, 540, yend + 160)
    if t >= C["27"]:
        y0 = yend + 10
        a1 = ep(t, C["27"], 0.4)
        _painel(c, y0, a1)
        carimbo(c, "× 0,85", 540, y0 + 70, a1, RED, -5, 34)
        linha(c, [("P = 102 ÷ 0,85 = ", INK), ("R$ 120,00", GREEN)], 540, y0 + 180, 36, ep(t, C["27.a"], 0.4))
        conferido(c, "120 × 0,85 = 102", 300, y0 + 270, ep(t, C["27.b"], 0.4), True, 30)


ALTS5 = [("A", "I, III, II", "", GREEN), ("B", "I, II, III", "50% parece mais que 30%", RED),
         ("C", "III, I, II", "leve 3 pague 2 < 30%?", RED), ("D", "II, I, III", "50% sobre tudo", RED),
         ("E", "III, II, I", "leve 3 pague 2 < 30%?", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "COMPARANDO PROMOÇÕES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4) * (1 - ep(t, C["29"], 0.4))
    yend = _enunciado(c, [("Uma pessoa precisa comprar 6 unidades de um produto vendido por R$ 12,00 a unidade. Três "
                           "lojas fazem promoções diferentes: loja I, \"leve 3, pague 2\"; loja II, \"segunda unidade "
                           "com 50% de desconto\"; loja III, \"30% de desconto em cada unidade\". Ordenando as lojas da "
                           "mais barata para a mais cara, para essa compra, obtém-se", INK)], a0, 240, 25)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 42, C["29.ok"], "A", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["28.end"] - 1.9, 540, min(yend + 90, 760), a=a0 if t < C["29"] else 0)
    if t >= C["29"]:
        a1 = ep(t, C["29"], 0.4)
        _painel(c, 230, a1)
        linha(c, [("preço cheio: 6 × 12 = ", INK), ("R$ 72,00", INK)], 540, 290, 32, a1)
        rows = [("29.a", "I", "paga 4 de 6", "R$ 48,00"), ("29.b", "II", "3 pares de R$ 18", "R$ 54,00"),
                ("29.c", "III", "72 × 0,70", "R$ 50,40")]
        for k, (cue, lj, conta, v) in enumerate(rows):
            ak = ep(t, C[cue], 0.4)
            yy = 390 + k * 100
            badge_num(c, lj, 240, yy - 10, ak, 26, bg=BLUE)
            text(c, conta, 290, yy, 30, "bold", INK2, ak, align="left")
            text(c, v, 870, yy, 36, "black", INK, ak, align="right")
        linha(c, [("ordem: ", INK), ("I, III, II", GREEN)], 540, 730, 40, ep(t, C["29.d"], 0.4))


ALTS8 = [("A", "R$ 510,00", "15% sobre tudo", RED), ("B", "R$ 540,00", "10% sobre tudo", RED),
         ("C", "R$ 560,00", "pulou o andar dos 5%", RED), ("D", "R$ 570,00", "", GREEN),
         ("E", "R$ 580,00", "só a cobertura", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · VOCÊ FAZ", "DESCONTO POR FAIXA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["31.a"], 0.4) * (1 - ep(t, C["32"], 0.4))
    yend = _enunciado(c, [("Uma loja de material de construção dá desconto progressivo: nenhum desconto sobre os "
                           "primeiros R$ 200,00 da compra, 5% sobre a parte da compra entre R$ 200,00 e R$ 400,00 e 10% "
                           "sobre a parte que exceder R$ 400,00. Um cliente fez uma compra de R$ 600,00. Ele pagou",
                           INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"31.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS8, 1000, 250, 680, 42, C["32.ok"], "D", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["31.end"] - 1.9, 540, min(yend + 90, 760), a=a0 if t < C["32"] else 0)
    if t >= C["32"]:
        a1 = ep(t, C["32"], 0.4)
        _painel(c, 230, a1)
        alf = (ep(t, C["32.a"], 0.4), ep(t, C["32.a"] + 1.0, 0.4), ep(t, C["32.a"] + 2.0, 0.4))
        predio(c, 230, 680, 240, 120, a1, 600 * ep(t, C["32"] + 0.3, 1.4), ("200 × 0% = 0", "200 × 5% = R$ 10",
                                                                           "200 × 10% = R$ 20"), alf, topo=200, mini=True)
        linha(c, [("desconto R$ 30  →  ", INK), ("R$ 570,00", GREEN)], 540, 760, 32, ep(t, C["32.b"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REMARCAÇÕES E LIQUIDAÇÕES", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 330, 360, 160, 22, "#F7F7F5", aa)
        text(c, "CUSTO", 440, 390, 30, "black", GRAY, aa, tracking=2)
        text(c, "da loja", 440, 440, 28, "bold", INK2, aa)
        arrow(c, 640, 410, 780, 410, AMBER, aa, 6, 18)
        carimbo(c, "+50%", 710, 340, ep(t, C["34.a"] + 1.0, 0.5), AMBER, -6, 30)
        etiqueta(c, "ETIQUETA", 990, 410, ep(t, C["34.a"] + 1.4, 0.5), AMBER, 40)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        arrow(c, 1190, 410, 1330, 410, RED, ab, 6, 18)
        carimbo(c, "−1/3", 1260, 340, ab, RED, 5, 30)
        rrect(c, 1360, 330, 340, 160, 22, mix("#FFFFFF", RED, 0.08), ab)
        text(c, "LIQUIDAÇÃO", 1530, 420, 32, "black", RED, ab, tracking=1)
    acc = ep(t, C["34.c"], 0.5)
    if acc > 0:
        text(c, "ainda LUCRA?", W / 2, 640, 80, "black", INK, acc)
    pill(c, "ep. 3 · remarcações, liquidações e o lucro que sobra", W / 2, 790, PURPLE, size=30,
         a=ep(t, C["34.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Qual promoção já te enganou?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, carimbos=b_carimbos,
              atalho1=b_atalho1, equivalente=b_equivalente, voltar=b_voltar, efetivo=b_efetivo, quantidade=b_quantidade,
              atalho2=b_atalho2, faixa=b_faixa, exercicio=b_exercicio, recap=b_recap, erros=b_erros, qn=b_qn, q6=b_q6,
              q5=b_q5, q8=b_q8, ponte=b_ponte, cta=b_cta)
