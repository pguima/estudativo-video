"""Visual — Função Modular e Funções por Partes, Episódio 2: faixas progressivas (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo...).
Peças deste episódio: barra_cortada() (o valor como BARRA cortada em fatias que caem, cada uma, na sua CAIXINHA da
escada, com a alíquota em cima e o imposto da fatia dentro), barra_errada() (a barra inteira caindo na caixinha da taxa
maior, com o selo vermelho), grafico_T() (a lei por partes do imposto: chão, rampa de 10%, rampa de 20%), grafico_unica()
(faixa única com SALTO × progressivo contínuo), troco() (o excesso cobrado em cada fatia, que volta como parcela a
deduzir), linha(), caixa(), conferido().
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
_s = importlib.util.spec_from_file_location("comum044", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_modular_ep2_faixas_progressivas.mp4"
CARD_R = K.CARD_R
ISENTO = "#9AA3B2"

# as fatias dos dois exemplos: (tamanho, rótulo da fatia, alíquota, imposto da fatia, cor)
F7000 = [(2000, "R$ 2.000", "ISENTO", "R$ 0", ISENTO), (3000, "R$ 3.000", "10%", "R$ 300", BLUE),
         (2000, "R$ 2.000", "20%", "R$ 400", PURPLE)]
F4000 = [(1000, "R$ 1.000", "ISENTO", "R$ 0", ISENTO), (2000, "R$ 2.000", "5%", "R$ 100", BLUE),
         (1000, "R$ 1.000", "15%", "R$ 150", PURPLE)]


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
    text(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def caixa(c, cx, cy, tit, val, col, a, w=360, h=140):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    size = 44
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 22, size, "black", INK, a)


def _geo(x, w, partes, gap):
    tot = sum(p[0] for p in partes)
    livre = w - gap * (len(partes) - 1)
    xs, ws = [], []
    xx = x
    for p in partes:
        ww = livre * p[0] / tot
        xs.append(xx); ws.append(ww)
        xx += ww + gap
    return xs, ws


def barra_cortada(c, x, y, w, partes, a, corte=0.0, queda=0.0, caixas=0.0, tam=0.0, imp=0.0, h=90, base=800,
                  degrau=70, titulo="LUCRO R$ 7.000,00"):
    """a barra do valor: corte (0..1) abre os vãos entre as fatias; caixas (0..1) desenha a ESCADA de caixinhas
    (mais alta à direita); queda (0..1) leva cada fatia para dentro da sua caixinha; tam mostra o tamanho da fatia
    (sempre antes da taxa); imp mostra o imposto de cada fatia dentro da caixinha."""
    if a <= 0:
        return
    gap = 34 * ease_io(clamp(corte))
    xs, ws = _geo(x, w, partes, gap)
    n = len(partes)
    tops = [base - 200 - k * degrau for k in range(n)]
    if titulo:
        text(c, titulo, x + w / 2, y - 26, 30, "black", INK2, a * (1 - ease_io(clamp(queda))))
    ac = a * ease_io(clamp(caixas))
    for k, (val, rot, ali, im, col) in enumerate(partes):
        if ac > 0:
            bx, bw = xs[k] - 12, ws[k] + 24
            rrect(c, bx, tops[k], bw, base - tops[k], 18, mix("#FFFFFF", col, 0.10), ac)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, tops[k], bw, base - tops[k]), 18, 18),
                        paint(col, ac, stroke=4))
            pill(c, ali, bx + bw / 2, tops[k] - 6, col, size=26, a=ac, anchor="center", bounds=(0, 1920))
        u = ease_io(clamp((queda - 0.12 * k) / 0.76)) if queda > 0 else 0.0
        yy = y + (tops[k] + 26 - y) * u
        rrect(c, xs[k], yy, ws[k], h, 14, col, a * 0.92)
        at = a * clamp(tam)
        if at > 0:
            sz = 36
            while text_w(rot, "black", sz) > ws[k] - 16 and sz > 20:
                sz -= 2
            text_mid(c, rot, xs[k] + ws[k] / 2, yy + h / 2, sz, "black", "#FFFFFF", at)
        ai = a * clamp(imp) * (u if queda > 0 else 1.0)
        if ai > 0:
            text_mid(c, im, xs[k] + ws[k] / 2, yy + h + 62, 40, "black", col if col != ISENTO else INK2, ai)


def barra_errada(c, x, y, w, a, queda=0.0, sel=0.0, val="R$ 7.000", ali="20%", imp="R$ 1.400,00 — O DOBRO",
                 h=90, base=800):
    """o JEITO ERRADO: a barra inteira cai numa caixinha só (a da taxa maior)"""
    if a <= 0:
        return
    top = base - 260
    rrect(c, x - 14, top, w + 28, base - top, 18, mix("#FFFFFF", RED, 0.08), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 14, top, w + 28, base - top), 18, 18), paint(RED, a, stroke=4))
    pill(c, ali + " SOBRE TUDO", x + w / 2, top - 6, RED, size=26, a=a, anchor="center", bounds=(0, 1920))
    u = ease_io(clamp(queda))
    yy = y + (top + 30 - y) * u
    rrect(c, x, yy, w, h, 14, PURPLE, a * 0.92)
    text_mid(c, val, x + w / 2, yy + h / 2, 38, "black", "#FFFFFF", a)
    if sel > 0:
        selo(c, x + w / 2, top + 190, a * clamp(sel), imp, RED, -4, 28)


def _eixos(c, x, y, w, h, a, xl, yl):
    line(c, x, y + h, x + w + 20, y + h, INK2, a, 3)
    line(c, x, y + h, x, y - 20, INK2, a, 3)
    text(c, xl, x + w + 10, y + h + 80, 24, "bold", GRAY, a, align="right")
    text(c, yl, x - 10, y - 34, 24, "bold", GRAY, a, align="left")


def grafico_T(c, x, y, w, h, a, prog_=1.0, marca=0.0):
    """T(x) do exemplo: 0 até 2.000; 10% até 5.000; 20% depois (até 8.000). marca destaca (5.000; 300) e (7.000; 700)"""
    if a <= 0:
        return
    rrect(c, x - 70, y - 70, w + 120, h + 140, 18, "#FFFFFF", a, shadow=True)
    _eixos(c, x, y, w, h, a, "lucro (R$)", "imposto (R$)")
    T = lambda v: 0 if v <= 2000 else (0.1 * (v - 2000) if v <= 5000 else 300 + 0.2 * (v - 5000))
    X = lambda v: x + w * v / 8000
    Y = lambda v: y + h - h * v / 900
    u = clamp(prog_)
    pts = [(v, T(v)) for v in range(0, 8001, 100) if v <= 8000 * u]
    cols = lambda v: ISENTO if v <= 2000 else (BLUE if v <= 5000 else PURPLE)
    for (v0, t0_), (v1, t1_) in zip(pts, pts[1:]):
        line(c, X(v0), Y(t0_), X(v1), Y(t1_), cols(v1), a, 7)
    for v in (2000, 5000, 7000):
        if u * 8000 >= v:
            text(c, f"{v // 1000}.000", X(v), y + h + 40, 22, "bold", GRAY, a)
            line(c, X(v), y + h, X(v), Y(T(v)), LIGHT, a, 2, dash=[6, 6])
    am = a * clamp(marca)
    if am > 0:
        for v, lab, col in ((5000, "300", BLUE), (7000, "700", PURPLE)):
            c.drawCircle(X(v), Y(T(v)), 12, paint(col, am))
            text(c, lab, X(v) - 18, Y(T(v)) - 22, 28, "black", col, am, align="right")


def grafico_unica(c, x, y, w, h, a, salto=0.0, prog_=0.0):
    """faixa única: 5 · m até 20 m³ e 8 · m acima (SALTO em 20); progressivo contínuo 5 · m e 100 + 8 (m − 20) junto"""
    if a <= 0:
        return
    rrect(c, x - 70, y - 70, w + 120, h + 140, 18, "#FFFFFF", a, shadow=True)
    _eixos(c, x, y, w, h, a, "consumo (m³)", "conta (R$)")
    X = lambda m: x + w * m / 26
    Y = lambda v: y + h - h * v / 220
    line(c, X(0), Y(0), X(20), Y(100), BLUE, a, 7)
    c.drawCircle(X(20), Y(100), 10, paint(BLUE, a))
    au = a * clamp(salto)
    if au > 0:
        line(c, X(20), Y(160), X(26), Y(208), RED, au, 7)
        c.drawCircle(X(20), Y(160), 10, paint("#FFFFFF", au))
        c.drawCircle(X(20), Y(160), 10, paint(RED, au, stroke=4))
        line(c, X(20), Y(104), X(20), Y(156), RED, au, 3, dash=[8, 8])
        c.drawCircle(X(21), Y(168), 10, paint(RED, au))
        text(c, "21 m³ → R$ 168", X(21) - 20, Y(168) - 26, 26, "black", RED, au, align="right")
        text(c, "SALTO", X(20) - 18, Y(132), 26, "black", RED, au, align="right")
    ap = a * clamp(prog_)
    if ap > 0:
        line(c, X(20), Y(100), X(26), Y(148), GREEN, ap, 7, dash=[14, 10])
        text(c, "progressivo: só muda a inclinação", X(26) + 30, Y(45), 26, "black", GREEN, ap, align="right")
    text(c, "20 m³ → R$ 100", X(20) + 22, Y(100) + 52, 26, "black", BLUE, a, align="left")
    text(c, "20", X(20), y + h + 40, 22, "bold", GRAY, a)


def troco(c, x, y, w, a, u=1.0, h=86):
    """o excesso cobrado em cada fatia quando se aplica 20% sobre tudo: isento (400 a mais), meio (300 a mais), última (0)"""
    if a <= 0:
        return
    xs, ws = _geo(x, w, F7000, 34)
    dados = [("cobrou 400", "devia 0", "+ 400"), ("cobrou 600", "devia 300", "+ 300"), ("cobrou 400", "devia 400", "0")]
    for k, ((val, rot, ali, im, col), (cob, dev, ex)) in enumerate(zip(F7000, dados)):
        ak = a * ease_io(clamp((u - 0.3 * k) / 0.4))
        if ak <= 0:
            continue
        rrect(c, xs[k], y, ws[k], h, 14, col, ak * 0.92)
        sz = 34
        while text_w(rot, "black", sz) > ws[k] - 16 and sz > 20:
            sz -= 2
        text_mid(c, rot, xs[k] + ws[k] / 2, y + h / 2, sz, "black", "#FFFFFF", ak)
        text(c, cob, xs[k] + ws[k] / 2, y + h + 46, 28, "bold", INK2, ak)
        text(c, dev, xs[k] + ws[k] / 2, y + h + 86, 28, "bold", GRAY, ak)
        rrect(c, xs[k] + ws[k] / 2 - 90, y + h + 112, 180, 64, 16, GREEN if ex != "0" else LIGHT, ak * 0.9)
        text_mid(c, ex, xs[k] + ws[k] / 2, y + h + 144, 34, "black", "#FFFFFF" if ex != "0" else INK2, ak)


def _enunciado(c, s, a, y0=240, size=27, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 11
    return y + 8


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FAIXAS PROGRESSIVAS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    caixa(c, 520, 330, "LUCRO", "R$ 7.000,00", BLUE, aa, 560)
    caixa(c, 520, 530, "TAXA", "até 20%", BLUE, ep(t, C["01.a"] + 1.4, 0.5), 560)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 960, 260, 760, 160, 26, "#FFFFFF", ab, shadow=True)
        linha(c, [("7.000 · 0,20 = ", INK), ("R$ 1.400,00", AMBER)], 1340, 340, 50, ab)
        sc = ep(t, C["01.c"], 0.5)
        strike(c, 1000, 340, 1680, 340, sc, RED, sc)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 960, 460, 760, 200, 26, mix("#FFFFFF", GREEN, 0.10), acc, shadow=True)
        text(c, "a conta certa", 1340, 520, 30, "bold", GRAY, acc)
        text_mid(c, "R$ 700,00", 1340, 595, 80, "black", GREEN, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 750, ad, "A DIFERENÇA ESTÁ NUMA PALAVRA", AMBER, -3, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "calcular imposto ou tarifa FAIXA POR FAIXA", GREEN),
             ("02.b", "conferir pela PARCELA A DEDUZIR", PURPLE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 220 + d
        rrect(c, 260, y, 1400, 160, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 340, y + 80, 30, a, col)
        text_mid(c, s, 400, y + 80, 44, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 280 + d1, 720, 440, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "PORCENTAGEM", 560, 330 + d1, GREEN, size=26, a=a1, anchor="center", bounds=(0, 1920))
        text_mid(c, "10% de um valor", 560, 470 + d1, 48, "black", INK2, a1)
        text_mid(c, "= valor · 0,10", 560, 570 + d1, 60, "black", PURPLE, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 440, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "EPISÓDIO 1", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        text_mid(c, "1º localize a faixa", 1360, 470 + d2, 52, "black", BLUE, a2)
        text_mid(c, "2º calcule", 1360, 570 + d2, 52, "black", INK2, a2)


# ======================================================================
# concreto e bloco a
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "R$ 7.000,00 EM FATIAS", "CADA UMA NA SUA CAIXINHA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.t"], 0.5)
    corte = ep(t, C["04.a"], 1.0)
    cx_ = ep(t, C["04.b"], 0.6)
    queda = ep(t, C["04.b"] + 0.8, 2.0)
    barra_cortada(c, 260, 290, 1400, F7000, aa, corte=corte, queda=queda, caixas=cx_, tam=corte, imp=0)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        pill(c, "você já viu isso disfarçado de DESCONTO", W / 2, 236, AMBER, size=28, a=acc, anchor="center",
             bounds=(0, 1920))


def b_termos(c, t, C, B):
    head_seq(c, t, C, [("05", "AS PALAVRAS", "DEFINIÇÕES", BLUE),
                       ("06", "COBRANÇA PROGRESSIVA", "A ESCADA DE CAIXINHAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        defs = [("05.a", "ALÍQUOTA", "a porcentagem cobrada", "10%, 20%"),
                ("05.b", "ISENTO", "não paga nada naquela faixa", "R$ 0"),
                ("05.c", "EXCEDENTE", "a parte que ultrapassar o limite", "só o pedaço que passou")]
        for k, (cue, nome, sig, ex) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            x = 190 + k * 520
            rrect(c, x, 270 + d, 480, 480, 26, mix("#FFFFFF", BLUE, 0.06), a, shadow=True)
            text(c, nome, x + 240, 350 + d, 44, "black", BLUE, a)
            para(c, sig, x + 40, 450 + d, 34, "bold", INK2, a, 400, 44)
            rrect(c, x + 40, 610 + d, 400, 100, 18, "#FFFFFF", a, shadow=True)
            sz = 34
            while text_w(ex, "black", sz) > 370:
                sz -= 2
            text_mid(c, ex, x + 240, 660 + d, sz, "black", INK, a)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 230, 1460, 130, 24, mix("#FFFFFF", BLUE, 0.10), aa, shadow=True)
        text(c, "PROGRESSIVO", W / 2, 278, 28, "black", BLUE, aa)
        text_mid(c, "a alíquota maior incide SÓ sobre a parte que passa do limite", W / 2, 325, 36, "black", INK, aa)
    ab = ep(t, C["06.b"], 0.5)
    barra_cortada(c, 300, 420, 1320, F7000, ab, corte=1, queda=ep(t, C["06.b"] + 0.4, 1.6), caixas=1, tam=1, imp=0,
                  base=810, degrau=55, titulo="")


# ======================================================================
# bloco b — fatiando os 7.000
# ======================================================================

def b_fatias(c, t, C, B):
    head_seq(c, t, C, [("07", "FATIANDO OS R$ 7.000", "TAMANHO ANTES DA TAXA", PURPLE),
                       ("08", "O JEITO ERRADO", "TUDO NA CAIXINHA DE 20%", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        # fatia a fatia: a k-ésima cai quando o seu cue chega
        cues = [C["07.a"], C["07.b"], C["07.c"]]
        partes = F7000
        gap = 34
        xs, ws = _geo(260, 1400, partes, gap)
        tops = [800 - 200 - k * 70 for k in range(3)]
        for k, (val, rot, ali, im, col) in enumerate(partes):
            bx, bw = xs[k] - 12, ws[k] + 24
            rrect(c, bx, tops[k], bw, 800 - tops[k], 18, mix("#FFFFFF", col, 0.10), 1)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, tops[k], bw, 800 - tops[k]), 18, 18),
                        paint(col, 1, stroke=4))
            pill(c, ali, bx + bw / 2, tops[k] - 6, col, size=26, a=1, anchor="center", bounds=(0, 1920))
            u = ease_io(clamp((t - cues[k]) / 1.2)) if t >= cues[k] else 0.0
            yy = 260 + (tops[k] + 26 - 260) * u
            rrect(c, xs[k], yy, ws[k], 90, 14, col, 0.92)
            text_mid(c, rot, xs[k] + ws[k] / 2, yy + 45, 36, "black", "#FFFFFF", 1)
            ai = ep(t, cues[k] + 1.6, 0.5)
            if ai > 0:
                text_mid(c, im, xs[k] + ws[k] / 2, yy + 90 + 62, 40, "black", col if col != ISENTO else INK2, ai)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            rrect(c, 560, 196, 800, 70, 18, "#FFFFFF", ad, shadow=True)
            linha(c, [("0 + 300 + 400 = ", INK), ("R$ 700,00", GREEN)], W / 2, 231, 40, ad)
        return
    aa = ep(t, C["08.a"], 0.5)
    barra_errada(c, 300, 260, 820, aa, queda=ep(t, C["08.a"] + 0.3, 1.2), sel=ep(t, C["08.b"], 0.5))
    if aa > 0:
        text(c, "7.000 · 0,20", 710, 470, 34, "black", INK2, aa)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1200, 300, 470, 420, "ATALHO", ["escreva o", "TAMANHO DA FATIA", "antes da taxa"], acc, 36)


# ======================================================================
# bloco c — a lei da última faixa
# ======================================================================

def b_lei(c, t, C, B):
    head(c, t, B["start"], "A LEI DA ÚLTIMA FAIXA", "PARA x > 5.000", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 230, 820, 130, 24, mix("#FFFFFF", PURPLE, 0.08), aa, shadow=True)
        linha(c, [("T(x) = ", INK), ("300", BLUE), (" + ", INK), ("0,2", PURPLE), (" · (", INK), ("x − 5.000", GREEN),
                  (")", INK)], 610, 295, 46, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 200, 400, 820, 150, 22, "#FFFFFF", ab, shadow=True)
        text(c, "300 = imposto acumulado até a fronteira", 610, 455, 30, "black", BLUE, ab)
        text(c, "parte de onde a anterior parou (ep. 1)", 610, 510, 26, "bold", GRAY, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 200, 580, 820, 220, 22, "#FFFFFF", acc, shadow=True)
        text(c, "x − 5.000 = o pedaço que passou", 610, 632, 30, "black", GREEN, acc)
        linha(c, [("T(7.000) = 300 + 0,2 · 2.000 = ", INK), ("700", GREEN)], 610, 700, 34, acc)
        text(c, "acumulado + taxa × o que passou", 610, 770, 26, "black", GREEN, acc)
    grafico_T(c, 1170, 300, 480, 420, ep(t, C["09.t"], 0.5), prog_=ep(t, C["09.t"], 3.0), marca=ep(t, C["09.b"], 0.5))


# ======================================================================
# bloco d — progressiva × faixa única
# ======================================================================

def b_unica(c, t, C, B):
    head_seq(c, t, C, [("10", "PROGRESSIVA × FAIXA ÚNICA", "O ALARME", AMBER),
                       ("11", "A FRONTEIRA", "SALTO × RAMPA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "ALARME DO PROGRESSIVO", W / 2, 250, 30, "black", AMBER, aa)
            for k, s in enumerate(("parte", "excedente", "que ultrapassar")):
                pill(c, s, W / 2 + (k - 1) * 420, 320, AMBER, size=40, a=aa, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            rrect(c, 260, 420, 1400, 200, 24, "#FFFFFF", ab, shadow=True)
            text(c, "até 20 m³: R$ 5,00 por m³", W / 2, 490, 38, "bold", INK2, ab)
            text(c, "quem consome MAIS DE 20 m³ paga R$ 8,00 por m³", W / 2, 565, 40, "black", INK, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            selo(c, 620, 720, acc, "SEM \"EXCEDENTE\"", RED, -4, 34)
            text_mid(c, "R$ 8,00 vale para o consumo INTEIRO", 1250, 720, 40, "black", RED, acc)
        return
    grafico_unica(c, 300, 300, 800, 420, ep(t, C["11.t"], 0.5), salto=ep(t, C["11.b"], 0.8), prog_=ep(t, C["11.c"] + 2.5, 0.8))
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("20 · 5 = ", INK), ("R$ 100", BLUE)], 1470, 330, 44, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("21 · 8 = ", INK), ("R$ 168", RED)], 1470, 430, 44, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        selo(c, 1470, 560, acc, "+1 m³ → +R$ 68", RED, -4, 34)


# ======================================================================
# bloco e — parcela a deduzir
# ======================================================================

def b_parcela(c, t, C, B):
    head_seq(c, t, C, [("12", "PARCELA A DEDUZIR", "O ATALHO", GREEN),
                       ("13", "DE ONDE SAI O 700?", "O TROCO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 240, 1400, 120, 24, mix("#FFFFFF", BLUE, 0.10), aa, shadow=True)
            text(c, "PARCELA A DEDUZIR", W / 2, 285, 26, "black", BLUE, aa)
            text_mid(c, "um valor fixo que você SUBTRAI no fim", W / 2, 330, 36, "black", INK, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            text(c, "para x > 5.000", W / 2, 430, 28, "bold", GRAY, ab)
            linha(c, [("T(x) = ", INK), ("0,2 · x", PURPLE), (" − ", INK), ("700", GREEN)], W / 2, 500, 64, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            K.atalho(c, 400, 600, 1120, 190, "ATALHO",
                     ["1.400 − 700 = 700", "alíquota maior × tudo − parcela"], acc, 38)
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        regra(c, "cobra a taxa maior sobre tudo e DEVOLVE o que cobrou a mais", W / 2, 250, aa, 32, GREEN)
    u = 0.0
    if t >= C["13.b"]:
        u = 0.4 * clamp((t - C["13.b"]) / 1.0)
    if t >= C["13.c"]:
        u = 0.4 + 0.6 * clamp((t - C["13.c"]) / 1.5)
    troco(c, 260, 350, 1400, ep(t, C["13.b"], 0.4), u=u)
    ad = ep(t, C["13.c"] + 3.0, 0.5)
    if ad > 0:
        rrect(c, 660, 700, 600, 100, 22, mix("#FFFFFF", GREEN, 0.12), ad, shadow=True)
        linha(c, [("troco: 400 + 300 = ", INK), ("700", GREEN)], W / 2, 750, 44, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ · LUCRO DE R$ 4.000", "PAUSE E TENTE", GREEN),
                       ("15", "VAMOS JUNTOS", "FATIE PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    if t < C["15"]:
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            rows = [("até R$ 1.000", "isento", ISENTO), ("parte de R$ 1.000 a R$ 3.000", "5%", BLUE),
                    ("parte acima de R$ 3.000", "15%", PURPLE)]
            for k, (s, al, col) in enumerate(rows):
                y = 260 + k * 110
                rrect(c, 360, y, 1200, 90, 18, mix("#FFFFFF", col, 0.10), aa, shadow=True)
                text_mid(c, s, 400, y + 45, 38, "bold", INK, aa, align="left")
                text_mid(c, al, 1520, y + 45, 44, "black", col, aa, align="right")
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            text_mid(c, "lucro de R$ 4.000,00: quanto paga?", W / 2, 640, 46, "black", INK, ab)
        pause_timer(c, t, C["14.end"] - 1.9, W / 2, 760)
        return
    aa = ep(t, C["15.a"], 0.5)
    barra_cortada(c, 260, 260, 1400, F4000, aa, corte=1, queda=ep(t, C["15.a"] + 0.6, 1.8), caixas=1, tam=1,
                  imp=ep(t, C["15.b"], 0.5), titulo="LUCRO R$ 4.000,00")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 196, 800, 70, 18, "#FFFFFF", ab, shadow=True)
        linha(c, [("0 + 100 + 150 = ", INK), ("R$ 250,00", GREEN)], W / 2, 231, 40, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0 and t < C["15.d"]:
        selo(c, 470, 330, acc, "15% SOBRE TUDO = R$ 600", RED, -4, 26)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        rrect(c, 230, 300, 620, 86, 18, mix("#FFFFFF", GREEN, 0.12), ad, shadow=True)
        linha(c, [("troco: 600 − 350 = ", INK), ("250", GREEN)], 540, 343, 34, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Cada fatia paga a taxa da sua caixinha.",
          "\"Parte\", \"excedente\", \"que ultrapassar\": é progressivo.",
          "Parcela a deduzir: cobra tudo na taxa maior e devolve o excesso."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Taxa da última faixa sobre tudo: 15% de 4.000 = 600", "o lucro está NA faixa dos 15%",
          "só o pedaço acima de 3.000 mora nela: o certo é R$ 250"),
         ("Esquecer a isenção: 5% desde o zero = 300", "a primeira taxa da tabela é 5%",
          "o 1º mil não paga nada: a fatia dos 5% tem 2.000, não 3.000"),
         ("Esquecer a faixa do meio: 15% de 3.000 = 450", "a conta fica mais curta",
          "toda faixa entre o zero e o valor tem a sua fatia")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# questão 7 (eu faço) e questão 1 (você faz)
# ======================================================================

ALTS7 = [("A", "R$ 500,00", "10% de 5.000 e para", RED), ("B", "R$ 700,00", "", GREEN),
         ("C", "R$ 900,00", "10% desde o zero", RED), ("D", "R$ 1.000,00", "20% de 5.000", RED),
         ("E", "R$ 1.400,00", "20% do lucro inteiro", RED)]

ALTS1 = [("A", "R$ 136,00", "40 + 16 · 6", RED), ("B", "R$ 154,00", "", GREEN), ("C", "R$ 156,00", "26 · 6", RED),
         ("D", "R$ 184,00", "40 + 16 · 9", RED), ("E", "R$ 234,00", "26 · 9", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · EU FAÇO", "TAXA PROGRESSIVA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    yend = _enunciado(c, "Um município cobra uma taxa mensal sobre o lucro de pequenos negócios: a parte do lucro até "
                      "R$ 2.000,00 é isenta; a parte entre R$ 2.000,00 e R$ 5.000,00 paga 10%; a parte que exceder "
                      "R$ 5.000,00 paga 20%. Um negócio que teve lucro de R$ 7.000,00 no mês pagará de taxa", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["21"], 0.3)),
         align="left")
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 260, 680, 40, C["21.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["21"]:
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["21"], 0.4), shadow=True)
    at = ep(t, C["21.t"], 0.4)
    if at > 0:
        pill(c, "ALARME: \"a parte\", \"que exceder\"", 540, y0 + 40, AMBER, size=22, a=at, anchor="center",
             bounds=(0, 1920))
    linha(c, [("2.000 · 0  +  3.000 · 10%  +  2.000 · 20%", INK)], 540, y0 + 100, 26, ep(t, C["21.a"], 0.4))
    linha(c, [("0 + 300 + 400 = ", INK), ("700", GREEN)], 540, y0 + 160, 34, ep(t, C["21.b"], 0.4))
    linha(c, [("troco: 1.400 − 700 = ", INK), ("700", GREEN)], 540, y0 + 220, 30, ep(t, C["21.c"], 0.4))


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · VOCÊ FAZ", "CONTA DE ÁGUA POR FAIXAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    yend = _enunciado(c, "Uma companhia de saneamento cobra a água consumida no mês assim: tarifa mínima de R$ 40,00 "
                      "para consumo de até 10 m³; R$ 6,00 por m³ que exceder 10 m³, até 20 m³; e R$ 9,00 por m³ que "
                      "exceder 20 m³. Uma residência consumiu 26 m³ em um mês. O valor da conta foi", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 260, 680, 40, C["24.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["24"]:
        pause_timer(c, t, C["23.end"] - 2.4, 540, 720, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["24"], 0.4), shadow=True)
    aa = ep(t, C["24.a"], 0.4)
    if aa > 0:
        for k, (s, col) in enumerate((("10 m³ mínima", ISENTO), ("10 m³ · R$ 6", BLUE), ("6 m³ · R$ 9", PURPLE))):
            pill(c, s, 300 + k * 240, y0 + 45, col, size=22, a=aa, anchor="center", bounds=(0, 1920))
    linha(c, [("40 + 60 + 54 = ", INK), ("154", GREEN)], 540, y0 + 120, 36, ep(t, C["24.b"], 0.4))
    linha(c, [("R$ 154,00", GREEN)], 540, y0 + 190, 40, ep(t, C["24.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MÓDULO É DISTÂNCIA", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0:
        text_mid(c, "| x |", 560, 470, 200, "black", PURPLE, aa)
        text(c, "duas barrinhas", 560, 640, 34, "bold", GRAY, aa)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        text_mid(c, "| −7 | = ?", 1320, 330, 72, "black", INK, ab)
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        x0, y0 = 1320, 500
        line(c, x0 - 220, y0, x0, y0 + 220, PURPLE, acc, 8)
        line(c, x0, y0 + 220, x0 + 220, y0, PURPLE, acc, 8)
        text(c, "por que um V?", x0, y0 + 290, 34, "black", PURPLE, acc)


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"],
        "Lucro de R$ 9.000: quanto paga de taxa?", canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, termos=b_termos, fatias=b_fatias,
              lei=b_lei, unica=b_unica, parcela=b_parcela, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q7=b_q7, q1=b_q1, ponte=b_ponte, cta=b_cta)
