"""Visual — Comparação de Propostas e Tomada de Decisão, Episódio 3: investimentos líquidos e custos escondidos (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: cartaz() (cartaz de banco com taxa e período), pilha() (a pilha de R$ 10.000,00 com o rendimento
em cima; o LEÃO do imposto morde só o topo), leao() (o leão estilizado), envelope() (o envelope do empréstimo que perde
a tarifa na porta), tabela() (taxas no mesmo período e já líquidas), linha(), caixa(), conferido().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum033", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_comparacao_ep3_liquido_custos.mp4"
CARD_R = K.CARD_R


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


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None, h=140):
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
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


def cartaz(c, cx, cy, banco, taxa, periodo, col, a, w=420, h=300, rot=0):
    """cartaz de banco: nome, taxa grande e o período"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    rrect(c, -w / 2, -h / 2, w, h, 26, "#FFFFFF", a, shadow=True)
    rrect(c, -w / 2, -h / 2, w, 64, 26, col, a)
    text(c, banco, 0, -h / 2 + 44, 28, "black", "#FFFFFF", a)
    size = 96
    while text_w(taxa, "black", size) > w - 40:
        size -= 4
    text_mid(c, taxa, 0, 20, size, "black", col, a)
    text(c, periodo, 0, h / 2 - 34, 34, "black", INK2, a)
    c.restore()


def leao(c, cx, cy, r, a, boca=0.0):
    """leão estilizado (o imposto): juba em pétalas, rosto, olhos e a boca que abre"""
    if a <= 0:
        return
    for k in range(14):
        ang = 2 * math.pi * k / 14
        c.drawCircle(cx + r * 0.95 * math.cos(ang), cy + r * 0.95 * math.sin(ang), r * 0.36, paint("#C8781E", a))
    c.drawCircle(cx, cy, r * 0.95, paint("#E89A2E", a))
    c.drawCircle(cx, cy + r * 0.08, r * 0.72, paint("#F6C35B", a))
    for sx in (-1, 1):
        c.drawCircle(cx + sx * r * 0.28, cy - r * 0.14, r * 0.09, paint(INK, a))
    c.drawCircle(cx, cy + r * 0.12, r * 0.11, paint("#7A3E10", a))
    hb = r * (0.10 + 0.28 * boca)
    rrect(c, cx - r * 0.30, cy + r * 0.30, r * 0.60, hb, r * 0.08, "#7A1E10", a)
    text(c, "IR", cx, cy - r * 1.42, 30, "black", AMBER, a)


def pilha(c, cx, base, a, mordida=0.0, w=420, h_base=330, h_top=120, rotulos=True):
    """a pilha de R$ 10.000 (azul, intacta) com o rendimento de R$ 1.200 (verde) em cima.
    mordida 0..1: o pedaço de R$ 240 (vermelho) sai do topo; sobram R$ 960."""
    if a <= 0:
        return
    rrect(c, cx - w / 2, base - h_base, w, h_base, 18, mix("#FFFFFF", BLUE, 0.20), a, shadow=True, stroke=4,
          stroke_color=BLUE)
    for k in range(1, 6):
        y = base - h_base * k / 6
        line(c, cx - w / 2 + 16, y, cx + w / 2 - 16, y, BLUE, a * 0.25, 3)
    text_mid(c, "R$ 10.000", cx, base - h_base / 2, 56, "black", BLUE, a)
    if rotulos:
        text(c, "já era seu", cx, base + 44, 28, "bold", GRAY, a)
    ytop = base - h_base - h_top - 10
    u = ease_io(clamp(mordida))
    wm = w * 0.2                                   # 240 / 1.200 = 20% do topo
    rrect(c, cx - w / 2, ytop, w - wm, h_top, 16, mix("#FFFFFF", GREEN, 0.22), a, shadow=True, stroke=4,
          stroke_color=GREEN)
    xr = cx + w / 2 - wm
    rrect(c, xr + 40 * u, ytop - 60 * u, wm, h_top, 16, mix("#FFFFFF", RED, 0.25), a * (1 - 0.35 * u), stroke=4,
          stroke_color=RED)
    text_mid(c, "240", xr + wm / 2 + 40 * u, ytop - 60 * u + h_top / 2, 30, "black", RED, a)
    lbl = "R$ 960" if u > 0.5 else "R$ 1.200"
    text_mid(c, lbl, cx - wm / 2 if u > 0.5 else cx, ytop + h_top / 2, 44, "black", GREEN, a)


def envelope(c, cx, cy, val, col, a, w=340, h=210, sub=None):
    """envelope de dinheiro com o valor"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, mix("#FFFFFF", col, 0.14), a, shadow=True, stroke=4, stroke_color=col)
    path = skia.Path()
    path.moveTo(cx - w / 2 + 8, cy - h / 2 + 8); path.lineTo(cx, cy - 6); path.lineTo(cx + w / 2 - 8, cy - h / 2 + 8)
    c.drawPath(path, paint(col, a * 0.6, stroke=4, cap_round=True))
    size = 50
    while text_w(val, "black", size) > w - 40:
        size -= 2
    text_mid(c, val, cx, cy + 46, size, "black", col, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 38, 26, "bold", GRAY, a)


def tabela(c, x, y, cols, rows, a_rows, widths, size=34, rh=78, cores=None):
    """tabela simples: cols = cabeçalho; rows = linhas de strings; a_rows = alfa de cada linha;
    cores = {(i, j): cor} para células destacadas"""
    tw = sum(widths)
    a0 = max(a_rows) if a_rows else 0
    if a0 <= 0:
        return
    rrect(c, x, y, tw, rh, 14, mix("#FFFFFF", PURPLE, 0.14), a0)
    xx = x
    for s_, w_ in zip(cols, widths):
        text_mid(c, s_, xx + w_ / 2, y + rh / 2, size * 0.75, "black", PURPLE, a0)
        xx += w_
    for i, (row, ar) in enumerate(zip(rows, a_rows)):
        if ar <= 0:
            continue
        yy = y + rh * (i + 1)
        rrect(c, x, yy + 4, tw, rh - 8, 12, "#FFFFFF", ar, shadow=True)
        xx = x
        for j, (s_, w_) in enumerate(zip(row, widths)):
            col = (cores or {}).get((i, j), INK)
            text_mid(c, s_, xx + w_ / 2, yy + rh / 2, size, "black", col, ar)
            xx += w_


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "O CUSTO ESCONDIDO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    cartaz(c, 520, 470, "EMPRÉSTIMO", "4%", "ao mês", BLUE, aa, w=520, h=380)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1020, 300, 700, 260, 26, mix("#FFFFFF", RED, 0.08), ab, shadow=True)
        text(c, "VOCÊ PAGA", 1370, 360, 32, "black", RED, ab)
        text_mid(c, "≈ 6,1% ao mês", 1370, 460, 76, "black", RED, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 1370, 680, acc, "TARIFA DE R$ 100 NO ATO", AMBER, -5, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "comparar aplicações pelo rendimento LÍQUIDO", GREEN),
             ("02.b", "calcular o custo efetivo de um empréstimo com tarifas", AMBER)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 220 + d
        rrect(c, 260, y, 1400, 160, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 340, y + 80, 30, a, col)
        text_mid(c, s, 400, y + 80, 42, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "3 LEMBRETES", "RÁPIDOS", GREEN)
    cards = [("03.a", "TAXAS EQUIVALENTES · EP. 1", "mudar o período?", "eleve o fator", "1,01¹²"),
             ("03.b", "TAXAS EQUIVALENTES · EP. 4", "tirar a inflação?", "divida os fatores", "1,10 ÷ 1,05"),
             ("03.c", "EMPRÉSTIMOS · EP. 2", "taxa embutida", "a mais ÷ financiado", "juros ÷ financiado")]
    for k, (cue, tag, s, regra_, ex) in enumerate(cards):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 280 + d, 480, 460, 24, "#FFFFFF", a, shadow=True)
        pill(c, tag, x + 240, 330 + d, GREEN, size=20, a=a, anchor="center", bounds=(0, 1920))
        text(c, s, x + 240, 440 + d, 34, "black", INK2, a)
        text(c, regra_, x + 240, 540 + d, 38, "black", PURPLE, a)
        text(c, ex, x + 240, 640 + d, 34, "bold", GRAY, a)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "TRÊS CARTAZES", "QUAL PAGA MAIS?", BLUE),
                       ("05", "O QUE A VITRINE NÃO MOSTRA", "IMPOSTO E TARIFA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        ab = ep(t, C["04.b"], 0.5)
        for k, (bc, tx, per, col) in enumerate((("BANCO 1", "1%", "ao mês", BLUE), ("BANCO 2", "12,5%", "ao ano", PURPLE),
                                               ("BANCO 3", "6%", "ao semestre", GREEN))):
            cartaz(c, 420 + k * 540, 470, bc, tx, per, col, ep(t, C["04.b"] + 1.2 * k, 0.5), rot=(-3, 2, -2)[k])
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            text_mid(c, "? ? ?", W / 2, 740, 64, "black", AMBER, acc)
        return
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 250, 680, 440, 24, "#FFFFFF", aa, shadow=True)
        text(c, "EXTRATO", 560, 310, 30, "black", GRAY, aa)
        for k, (l, v, col) in enumerate((("Saldo aplicado", "R$ 10.000,00", INK), ("Rendimento bruto", "R$ 1.200,00", GREEN),
                                         ("IR retido", "− R$ 240,00", RED))):
            y = 400 + k * 90
            text(c, l, 260, y, 32, "bold", INK2, aa, align="left")
            text(c, v, 860, y, 32, "black", col, aa, align="right")
        if ep(t, C["05.a"] + 2.0, 0.4) > 0:
            K.boxed(c, 240, 540, 640, 66, RED, ep(t, C["05.a"] + 2.0, 0.4), 0.06, 12, 4)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 1020, 250, 680, 440, 24, "#FFFFFF", ab, shadow=True)
        text(c, "CONTRATO", 1360, 310, 30, "black", GRAY, ab)
        for k, (l, v, col) in enumerate((("Valor contratado", "R$ 5.000,00", INK), ("Juros", "4% ao mês", BLUE),
                                         ("Tarifa de cadastro", "− R$ 100,00", RED))):
            y = 400 + k * 90
            text(c, l, 1060, y, 32, "bold", INK2, ab, align="left")
            text(c, v, 1660, y, 32, "black", col, ab, align="right")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        regra(c, "vitrine ≠ o que chega ao bolso", W / 2, 770, acc, 40, AMBER)


# ======================================================================
# bloco a — os três ajustes
# ======================================================================

def b_ajustes(c, t, C, B):
    head_seq(c, t, C, [("06", "ANTES DE COMPARAR", "OS TRÊS AJUSTES", PURPLE),
                       ("07", "AJUSTE 1", "O MESMO PERÍODO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        itens = [("06.a", "MESMO PERÍODO", "taxa equivalente: eleve o fator", BLUE),
                 ("06.b", "TIRE O IMPOSTO", "ele incide sobre o rendimento", AMBER),
                 ("06.c", "TIRE A INFLAÇÃO", "quando pedir: divida os fatores", PURPLE)]
        for k, (cue, nome, sig, col) in enumerate(itens):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 240 + k * 190 + d
            badge_num(c, k + 1, 260, y + 70, a, 30, bg=col)
            rrect(c, 320, y, 1300, 150, 22, mix("#FFFFFF", col, 0.07), a)
            text(c, nome, 360, y + 62, 40, "black", col, a, align="left")
            text(c, sig, 360, y + 116, 30, "bold", INK2, a, align="left")
        return
    aa = ep(t, C["07.a"], 0.5)
    cartaz(c, 460, 470, "BANCO 1", "1%", "ao mês", BLUE, ep(t, C["07"], 0.5), w=400, h=300)
    if aa > 0:
        arrow(c, 700, 470, 860, 470, PURPLE, aa, 6, 22)
        K.mdraw(c, "1,01^{12} ≈ 1,1268", 1240, 400, 58, PURPLE, aa, align="center")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("≈ ", INK), ("12,68% ao ano", GREEN)], 1240, 510, 54, ab)
        text(c, "contra 12,5% ao ano do cartaz anual", 1240, 590, 30, "bold", INK2, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "compare o que entra no bolso, não o que está na vitrine", W / 2, 760, acc, 36, GREEN)


# ======================================================================
# bloco b — o imposto
# ======================================================================

def b_imposto(c, t, C, B):
    head_seq(c, t, C, [("08", "O IMPOSTO", "BRUTO · ALÍQUOTA · LÍQUIDO", BLUE),
                       ("09", "X OU Y?", "A BRUTA MAIS ALTA PERDEU", AMBER),
                       ("10", "ATALHO", "O FATOR DO IMPOSTO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    if sid == "08":
        defs = [("08.a", "RENDIMENTO BRUTO", "o que rendeu antes do imposto"),
                ("08.b", "ALÍQUOTA", "a porcentagem do imposto (só sobre o que rendeu)"),
                ("08.c", "RENDIMENTO LÍQUIDO", "o que entra de verdade no bolso")]
        for k, (cue, nome, sig) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + k * 190 + d
            rrect(c, 260, y, 1400, 160, 22, mix("#FFFFFF", BLUE, 0.06), a)
            text(c, nome, 300, y + 66, 40, "black", BLUE, a, align="left")
            text(c, sig, 300, y + 122, 30, "bold", INK2, a, align="left")
        return
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        caixa(c, 560, 320, "APLICAÇÃO X", "12% · IR 20%", AMBER, aa, 560)
        caixa(c, 1360, 320, "APLICAÇÃO Y", "10% · isenta", BLUE, ep(t, C["09.a"] + 2.4, 0.5), 560)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            linha(c, [("12% · 0,8 = ", INK), ("9,6%", AMBER)], 560, 520, 52, ab)
            linha(c, [("10%", BLUE)], 1360, 520, 52, ep(t, C["09.b"] + 3.4, 0.5))
            text(c, "líquido", 560, 590, 28, "bold", GRAY, ab)
            text(c, "líquido", 1360, 590, 28, "bold", GRAY, ep(t, C["09.b"] + 3.4, 0.5))
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            selo(c, 1360, 700, acc, "Y RENDE MAIS", GREEN, -5, 40)
            strike(c, 400, 320, 720, 320, acc, RED, acc)
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        K.atalho(c, 300, 250, 1320, 230, "ATALHO · O FATOR DO IMPOSTO", ["imposto de 20% → fica 0,8 com você"], aa, 44)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("imposto de 15% → × ", INK), ("0,85", GREEN)], W / 2, 560, 46, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        regra(c, "líquida = bruta × (1 − alíquota)", W / 2, 700, acc, 44)


# ======================================================================
# bloco c — em reais (o leão morde só o topo)
# ======================================================================

def b_reais(c, t, C, B):
    head(c, t, B["start"], "EM REAIS", "O IMPOSTO MORDE SÓ O RENDIMENTO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    mord = prog(t, C["11.b"] + 1.0, 1.4)
    pilha(c, 560, 760, aa, mordida=mord)
    if aa > 0:
        linha(c, [("12% de 10.000 = ", INK), ("R$ 1.200", GREEN)], 1360, 290, 42, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        boca = 0.5 + 0.5 * math.sin(max(0.0, t - C["11.b"]) * 6) if mord < 1 else 0.2
        leao(c, 900, 330, 66, ab, boca)
        linha(c, [("20% de 1.200 = ", INK), ("R$ 240", RED)], 1360, 420, 42, ab)
        linha(c, [("não 20% de tudo = ", GRAY), ("R$ 2.240", GRAY)], 1360, 500, 34, ep(t, C["11.b"] + 3.2, 0.4))
        if ep(t, C["11.b"] + 3.2, 0.4) > 0:
            strike(c, 1140, 500, 1580, 500, ep(t, C["11.b"] + 3.6, 0.4), RED, ep(t, C["11.b"] + 3.6, 0.4))
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        selo(c, 560, 700, acc, "INTACTA", BLUE, -6, 30)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 1020, 600, 560, 180, 24, mix("#FFFFFF", GREEN, 0.10), ad, shadow=True)
        text(c, "RESGATE LÍQUIDO", 1300, 650, 28, "black", GREEN, ad)
        text(c, "10.000 + 1.200 − 240", 1300, 700, 28, "bold", INK2, ad)
        text_mid(c, "R$ 10.960", 1300, 750, 50, "black", GREEN, ad)


# ======================================================================
# bloco d — custos escondidos
# ======================================================================

def b_escondidos(c, t, C, B):
    head_seq(c, t, C, [("12", "CUSTOS ESCONDIDOS", "A TARIFA NA PORTA", AMBER),
                       ("13", "CET", "CUSTO EFETIVO TOTAL", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        for k, s_ in enumerate(("tarifas", "seguros", "taxas de abertura")):
            K.chip(c, s_, 520 + k * 440, 270, AMBER, ep(t, C["12.a"] + 0.6 * k, 0.4), 32)
        if ep(t, C["12.a"] + 2.6, 0.4) > 0:
            text(c, "tarifa = valor fixo cobrado por um serviço", W / 2, 360, 30, "bold", BLUE,
                 ep(t, C["12.a"] + 2.6, 0.4))
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            # o banco (porta) à esquerda; o envelope sai e perde R$ 100 na porta
            rrect(c, 230, 420, 240, 330, 18, mix("#FFFFFF", INK2, 0.12), ab, stroke=4, stroke_color=INK2)
            text(c, "BANCO", 350, 470, 30, "black", INK2, ab)
            u = ease_io(clamp((t - C["12.b"]) / 1.6))
            x = 560 + 260 * u
            envelope(c, x, 600, "R$ 5.000" if u < 0.6 else "R$ 4.900", BLUE if u < 0.6 else AMBER, ab, w=300, h=180)
            if u >= 0.6:
                a2 = ep(t, C["12.b"] + 1.0, 0.4)
                pill(c, "− R$ 100", 560, 480, RED, size=30, a=a2, anchor="center", bounds=(0, 1920))
                text(c, "você recebe", x, 740, 28, "bold", GRAY, a2)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            envelope(c, 1450, 600, "R$ 5.200", RED, acc, w=340, h=200, sub="cobrança no fim do mês")
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            pill(c, "encolhe o que você recebe · não encolhe o que você paga", W / 2, 820, AMBER, size=26, a=ad,
                 anchor="center", bounds=(0, 1920))
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 260, 1320, 240, 26, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
        text(c, "CET · CUSTO EFETIVO TOTAL", W / 2, 330, 44, "black", BLUE, aa)
        text(c, "a taxa que junta tudo", W / 2, 400, 34, "bold", INK2, aa)
        for k, s_ in enumerate(("juros", "tarifas", "seguros")):
            K.chip(c, s_, 700 + k * 260, 460, BLUE, ep(t, C["13.a"] + 1.4 + 0.4 * k, 0.4), 26)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 650, ab, "POR LEI, O BANCO PRECISA INFORMAR", PURPLE, -3, 40)


# ======================================================================
# bloco e — a conta do custo efetivo
# ======================================================================

def b_custo(c, t, C, B):
    head_seq(c, t, C, [("14", "A CONTA", "DIVIDA PELO QUE RECEBEU", PURPLE),
                       ("15", "ATALHO", "PAGO ÷ RECEBIDO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        caixa(c, 560, 320, "RECEBEU", "R$ 4.900", AMBER, aa, 480)
        caixa(c, 1360, 320, "PAGOU", "R$ 5.200", RED, ep(t, C["14.a"] + 1.6, 0.5), 480)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            linha(c, [("pagou a mais: 5.200 − 4.900 = ", INK), ("R$ 300", RED)], W / 2, 480, 44, ab)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            rrect(c, 560, 560, 800, 160, 24, "#FFFFFF", acc, shadow=True)
            K.mdraw(c, "300/4.900", 780, 640, 54, PURPLE, acc, align="center")
            text_mid(c, "≈ 6,1% ao mês", 1130, 640, 50, "black", RED, acc)
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            pill(c, "a mesma conta da taxa embutida · a tarifa faz o papel da entrada", W / 2, 790, PURPLE, size=24,
                 a=ad, anchor="center", bounds=(0, 1920))
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        K.atalho(c, 300, 250, 1320, 220, "ATALHO · O FATOR DO EMPRÉSTIMO", ["pago ÷ recebido, e tire o 1"], aa, 44)
        linha(c, [("5.200 ÷ 4.900 ≈ ", INK), ("1,061", PURPLE)], W / 2, 560, 56, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("1,061 − 1 = ", INK2), ("6,1%", GREEN)], W / 2, 660, 50, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        pill(c, "cobrança no ato → custo efetivo > taxa anunciada", W / 2, 780, AMBER, size=28, a=acc,
             anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "RECEBIDO × PAGO", GREEN)])
    card(c, *CARD_R)
    if t < C["17"]:
        aa = ep(t, C["16.a"], 0.5)
        caixa(c, 480, 320, "EMPRÉSTIMO", "R$ 2.000", BLUE, aa, 400)
        caixa(c, 960, 320, "JUROS", "5% · 1 mês", PURPLE, ep(t, C["16.a"] + 1.2, 0.5), 400)
        caixa(c, 1440, 320, "TARIFA NO ATO", "R$ 50", RED, ep(t, C["16.a"] + 2.4, 0.5), 400)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            text_mid(c, "qual é o custo efetivo?", W / 2, 500, 46, "black", INK, ab)
        pause_timer(c, t, C["16.end"] - 1.9, W / 2, 660)
        return
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        linha(c, [("recebe: 2.000 − 50 = ", INK), ("R$ 1.950", AMBER)], W / 2, 290, 46, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        linha(c, [("paga: 2.000 · 1,05 = ", INK), ("R$ 2.100", RED)], W / 2, 390, 46, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("a mais: ", INK), ("R$ 150", RED)], W / 2, 490, 46, acc)
        rrect(c, 560, 570, 800, 150, 24, "#FFFFFF", acc, shadow=True)
        K.mdraw(c, "150/1.950", 780, 645, 50, PURPLE, acc, align="center")
        text_mid(c, "≈ 7,7% no mês", 1130, 645, 48, "black", GREEN, acc)
        pill(c, "anunciado: 5%", W / 2, 790, AMBER, size=28, a=ep(t, C["17.c"] + 3.6, 0.4), anchor="center",
             bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Compare taxas no mesmo período e já líquidas.",
          "Imposto incide sobre o rendimento, não sobre o total.",
          "Custo efetivo é o que você paga a mais dividido pelo que você recebeu."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Tirar o imposto do valor total (20% de tudo)", "o extrato mostra tudo junto",
          "o imposto morde só o rendimento: 12% com 20% de IR rende 9,6% líquidos"),
         ("Comparar 1% ao mês com 12,5% ao ano direto", "12,5 é um número maior que 1",
          "1% ao mês vira 12,68% ao ano: supera os 12,5%"),
         ("Ignorar a tarifa cobrada no ato", "a taxa está no contrato, em letra grande",
          "divida o que pagou a mais pelo que recebeu: 300 ÷ 4.900 ≈ 6,1%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


def _fonte(c, a):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a, align="left")


ALTS7 = [("A", "2,0%", "só a tarifa: 100 ÷ 5.000", RED), ("B", "4,0%", "a taxa anunciada", RED),
         ("C", "4,1%", "esqueceu a tarifa: 200 ÷ 4.900", RED), ("D", "6,0%", "÷ 5.000 contratados", RED),
         ("E", "6,1%", "", GREEN)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · EU FAÇO", "CUSTO EFETIVO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, "Uma pessoa tomou R$ 5.000,00 emprestados por um mês, a juros de 4% ao mês. O banco cobrou uma "
                      "tarifa de R$ 100,00, descontada no momento da liberação do dinheiro. Ao final do mês, ela pagou o "
                      "valor emprestado mais os juros. O custo efetivo desse empréstimo no mês foi de, aproximadamente,",
                      a0)
    _fonte(c, a0 * (1 - ep(t, C["23"], 0.3)))
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 36, C["23.ok"], "E", cues_in, cues_x, gap=34)
    if t < C["23"]:
        return
    y0 = yend + 4
    ab = ep(t, C["23"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ab, shadow=True)
    linha(c, [("recebeu ", INK2), ("4.900", AMBER), (" · pagou ", INK2), ("5.200", RED)], 540, y0 + 60, 32,
          ep(t, C["23.a"], 0.4))
    if ep(t, C["23.b"], 0.4) > 0:
        K.mdraw(c, "300/4.900", 430, y0 + 150, 40, PURPLE, ep(t, C["23.b"], 0.4), align="center")
        text_mid(c, "≈ 6,1%", 680, y0 + 150, 42, "black", GREEN, ep(t, C["23.b"], 0.4))


ALTS4 = [("A", "Q: 12,5% > os 12% dos outros dois", "proporcional (12 · 1%, 2 · 6%)", RED),
         ("B", "R: capitaliza duas vezes no ano", "R dá 12,36%: ainda perde", RED),
         ("C", "qualquer um: todas ≈ 12% ao ano", "proporcional", RED),
         ("D", "P: 1% ao mês ≈ 12,7% ao ano", "", GREEN),
         ("E", "Q: anual sempre supera mensal", "generalização falsa", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · NÓS FAZEMOS", "TRÊS BANCOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCE"}
    if t < C["26"]:
        _enunciado(c, "Três bancos oferecem aplicações no regime de juros compostos: o banco P paga 1% ao mês; o "
                   "banco Q, 12,5% ao ano; o banco R, 6% ao semestre. Considere 1,01¹² ≈ 1,127. Para quem vai "
                   "aplicar por um ano, a melhor opção é", a0, size=30)
        _fonte(c, a0)
        K.alternativas(c, t, C, ALTS4, 1000, 250, 700, 28, C["26.ok"], "D", cues_in, cues_x, gap=30)
        pause_timer(c, t, C["25.end"] - 1.9, 540, 720)
        return
    if t < C["27"]:
        rows = [["P", "1% ao mês", "1,01¹² ≈ 1,127", "≈ 12,7%"], ["Q", "12,5% ao ano", "—", "12,5%"],
                ["R", "6% ao semestre", "1,06² = 1,1236", "12,36%"]]
        ar = [ep(t, C["26.a"], 0.4), ep(t, C["26.b"], 0.4), ep(t, C["26.c"], 0.4)]
        cores = {(0, 3): GREEN} if ep(t, C["26.d"], 0.4) > 0 else {}
        tabela(c, 260, 250, ["BANCO", "CARTAZ", "FATOR ANUAL", "AO ANO"], rows, ar, [200, 420, 440, 340], 38, 100,
               cores)
        if ep(t, C["26.a"], 0.4) > 0:
            pill(c, "você já calculou no ep. 1 de Taxas Equivalentes", W / 2, 700, BLUE, size=26,
                 a=ep(t, C["26.a"] + 2.0, 0.4), anchor="center", bounds=(0, 1920))
        ad = ep(t, C["26.d"], 0.4)
        if ad > 0:
            selo(c, W / 2, 790, ad, "LETRA D · BANCO P", GREEN, -3, 36)
        return
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0:
        K.atalho(c, 170, 250, 760, 220, "ATALHO · O QUADRADO", [("m", "1,06^2 = 1 + 0,12 + 0,0036")], aa, 38)
    alts = [(L, s_, "", col) for L, s_, _, col in ALTS4]
    K.alternativas(c, t, C, alts, 1000, 250, 700, 28, C["27"], "D", {L: C["27"] - 1 for L in "ABCDE"}, cues_x,
                   gap=30)
    motivos = [("27.xa", "A e C: taxas proporcionais (12 · 1%, 2 · 6%)", RED),
               ("27.xb", "B: R capitaliza, mas 12,36% ainda perde", RED),
               ("27.xe", "E: quem decide é a taxa equivalente", RED)]
    for k, (cue, s_, col) in enumerate(motivos):
        a = ep(t, C[cue], 0.4)
        if a > 0:
            check_icon(c, 200, 545 + k * 85, 22, a, col, "x")
            text(c, s_, 240, 556 + k * 85, 28, "black", col, a, align="left")


ALTS3 = [("A", "I, com R$ 960,00", "certo, mas < 1.000", AMBER), ("B", "II, com R$ 1.000,00", "", GREEN),
         ("C", "I, com R$ 1.200,00", "bruto: esqueceu o IR", RED), ("D", "III, com R$ 935,00", "certo, mas < 1.000", AMBER),
         ("E", "III, com R$ 1.100,00", "bruto: esqueceu o IR", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "RENDIMENTO LÍQUIDO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, "Uma pessoa vai aplicar R$ 10.000,00 por um ano e compara três opções: I) rende 12% ao ano, com "
                      "imposto de 20% sobre o rendimento; II) rende 10% ao ano, isenta de imposto; III) rende 11% ao "
                      "ano, com imposto de 15% sobre o rendimento. A opção de maior rendimento líquido e o valor desse "
                      "rendimento são", a0, size=26)
    _fonte(c, a0 * (1 - ep(t, C["29"], 0.3)))
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 34, C["29.ok"], "B", cues_in, cues_x, gap=34)
    if t < C["29"]:
        pause_timer(c, t, C["28.end"] - 2.4, 540, 740, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["29"], 0.4), shadow=True)
    for k, (cue, partes) in enumerate((("29.a", [("I: 1.200 · 0,8 = ", INK), ("960", AMBER)]),
                                       ("29.b", [("II: ", INK), ("1.000", GREEN), (" (isenta)", GRAY)]),
                                       ("29.c", [("III: 1.100 · 0,85 = ", INK), ("935", AMBER)]))):
        linha(c, partes, 540, y0 + 50 + k * 60, 32, ep(t, C[cue], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PONTO DE EQUILÍBRIO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    caixa(c, 620, 340, "CUSTO FIXO", "R$ 6.000 por mês", RED, aa, 560)
    caixa(c, 1300, 340, "CADA PEÇA DEIXA", "R$ 20", GREEN, ep(t, C["32.a"] + 1.8, 0.5), 480)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        text_mid(c, "quantas peças para não ter prejuízo?", W / 2, 560, 50, "black", AMBER, ab)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        pill(c, "ep. 4 · ponto de equilíbrio", W / 2, 700, PURPLE, size=36, a=acc, anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Você já olhou o CET de um empréstimo antes de assinar?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, ajustes=b_ajustes,
              imposto=b_imposto, reais=b_reais, escondidos=b_escondidos, custo=b_custo, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q7=b_q7, q4=b_q4, q3=b_q3, ponte=b_ponte, cta=b_cta)
