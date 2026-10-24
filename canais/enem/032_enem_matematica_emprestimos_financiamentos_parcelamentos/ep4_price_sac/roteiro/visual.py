"""Visual — Empréstimos, Financiamentos e Parcelamentos, Episódio 4: o sistema Price e a comparação SAC × Price (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, fr, selo...).
Peças deste episódio: caixa() (a parcela da Price como caixa de tamanho fixo: juros em laranja em cima, amortização em
azul embaixo), barras() (o gráfico da seção 08, parcelas mês a mês nos dois sistemas), carne() (o carnê do crediário),
tabela() (as linhas da tabela da Price), linha() e brl().
Cores com função: azul = definição e amortização · laranja = juros · roxo = regra/fórmula · âmbar = armadilha ·
verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum032", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_emprestimos_ep4_price_sac.mp4"
CARD_R = K.CARD_R
ORANGE = "#F08A24"
PAPEL = K.PAPEL

# exemplo da seção 07: R$ 10.000,00, 5 parcelas, 4% a.m.  (amortização, juros) por mês
PRICE = [(1846.27, 400.00), (1920.12, 326.15), (1996.93, 249.34), (2076.80, 169.47), (2159.88, 86.39)]
SAC = [(2000, 400), (2000, 320), (2000, 240), (2000, 160), (2000, 80)]


def brl(v, rs=True):
    """2246.27 -> 'R$ 2.246,27'; inteiro sem centavos quando redondo e rs=False"""
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("R$ " if rs else "") + s


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


def caixa(c, x, y, w, h, juros, amort, a, rot=True, size=26, total=None):
    """a parcela como CAIXA de tamanho fixo: juros (laranja) em cima, amortização (azul) embaixo.
    juros e amort em reais; a altura de cada parte é proporcional (total = juros + amort, ou o dado)."""
    if a <= 0:
        return
    total = total or (juros + amort)
    hj = h * juros / total
    rrect(c, x, y, w, h, 14, "#FFFFFF", a, shadow=True)
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14))
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - (h - hj), w, h - hj), paint(BLUE, a))
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - total * h / total, w, hj), paint(ORANGE, a))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(INK2, a, stroke=4))
    if rot:
        if hj > size * 1.3:
            text_mid(c, brl(juros, False), x + w / 2, y + hj / 2, size, "black", "#FFFFFF", a)
        if h - hj > size * 1.3:
            text_mid(c, brl(amort, False), x + w / 2, y + hj + (h - hj) / 2, size, "black", "#FFFFFF", a)


def legenda(c, x, y, a, size=26):
    if a <= 0:
        return
    rrect(c, x, y - 14, 28, 28, 6, ORANGE, a)
    text(c, "juros", x + 40, y + 9, size, "black", ORANGE, a, align="left")
    x2 = x + 70 + text_w("juros", "black", size)
    rrect(c, x2, y - 14, 28, 28, 6, BLUE, a)
    text(c, "amortização (abate a dívida)", x2 + 40, y + 9, size, "black", BLUE, a, align="left")


def barras(c, x, y, w, h, dados, a, prog=1.0, tit="", col_tit=INK, vmax=2500, rot_parcela=True):
    """gráfico de barras empilhadas: 5 meses; dados = [(amort, juros)]. prog revela os meses um a um."""
    if a <= 0:
        return
    n = len(dados)
    bw = w / n * 0.62
    base = y + h
    line(c, x - 10, base, x + w + 10, base, INK2, a, 3)
    for k, (am, ju) in enumerate(dados):
        ak = a * clamp(prog * n - k)
        if ak <= 0:
            continue
        bx = x + w / n * (k + 0.5) - bw / 2
        ha, hj = h * am / vmax, h * ju / vmax
        rrect(c, bx, base - ha, bw, ha, 4, BLUE, ak)
        rrect(c, bx, base - ha - hj, bw, hj, 4, ORANGE, ak)
        text(c, f"{k + 1}º", bx + bw / 2, base + 34, 22, "bold", GRAY, ak)
        if rot_parcela:
            text(c, brl(am + ju, False), bx + bw / 2, base - ha - hj - 14, 19, "black", INK, ak)
    if tit:
        text(c, tit, x + w / 2, y - 26, 34, "black", col_tit, a)


def carne(c, x, y, w, h, a, n=12, valor="R$ 150,00"):
    """carnê de crediário: um bloco de folhas iguais, a da frente com o valor"""
    if a <= 0:
        return
    for k in range(4, 0, -1):
        rrect(c, x + k * 10, y - k * 10, w, h, 12, mix(PAPEL, INK2, 0.05 * k), a, shadow=k == 4)
    rrect(c, x, y, w, h, 12, PAPEL, a, shadow=True)
    rrect(c, x, y, w, 56, 12, mix("#FFFFFF", BLUE, 0.2), a)
    text(c, "CARNÊ · CREDIÁRIO", x + w / 2, y + 38, 24, "black", BLUE, a)
    text(c, f"parcela 1 de {n}", x + w / 2, y + 110, 28, "bold", INK2, a)
    text(c, valor, x + w / 2, y + 190, 56, "black", INK, a)
    for k in range(3):
        line(c, x + 30, y + 240 + k * 26, x + w - 30, y + 240 + k * 26, LINE, a, 3)


def tabela(c, x, y, linhas_, a, col_w=(110, 260, 220, 260, 240), size=30, destaque=None, alfas=None):
    """tabela da Price: cabeçalho + linhas [(mês, saldo, juros, amortização, parcela)]"""
    if a <= 0:
        return
    hdr = ["mês", "deve agora", "juros (4%)", "amortização", "parcela"]
    cols = [INK2, INK2, ORANGE, BLUE, INK2]
    W_ = sum(col_w)
    rrect(c, x, y, W_, 64, 12, "#F1F1EE", a)
    xx = x
    for k, s_ in enumerate(hdr):
        text(c, s_, xx + col_w[k] / 2, y + 42, 24, "black", cols[k], a)
        xx += col_w[k]
    for j, row in enumerate(linhas_):
        aj = a * (alfas[j] if alfas else 1)
        if aj <= 0:
            continue
        yy = y + 64 + j * 72
        if destaque == j:
            rrect(c, x, yy + 4, W_, 64, 10, mix("#FFFFFF", PURPLE, 0.08), aj)
        xx = x
        for k, s_ in enumerate(row):
            text(c, s_, xx + col_w[k] / 2, yy + 48, size, "black", cols[k] if k else INK, aj)
            xx += col_w[k]


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def agora(c, cx, cy, a, valor, size=30):
    """a pergunta âncora: quanto se deve AGORA?"""
    if a <= 0:
        return
    s = f"quanto se deve AGORA?  {valor}"
    w = ftext_w(s, "black", size) + 70
    rrect(c, cx - w / 2, cy - 32, w, 64, 32, mix("#FFFFFF", PURPLE, 0.12), a)
    fmid(c, s, cx, cy, size, "black", PURPLE, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EMPRÉSTIMOS E FINANCIAMENTOS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        for k, s_ in enumerate(("mesma dívida", "mesma taxa", "mesmo prazo")):
            chip(c, s_, 560 + k * 400, 250, INK2, ep(t, C["01.a"] + 0.5 * k, 0.4), 32, fill=False)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 340, 560, 330, 26, "#FFFFFF", ab, shadow=True)
        text(c, "SISTEMA 1", 580, 400, 30, "black", GRAY, ab)
        text(c, "juros pagos", 580, 470, 28, "bold", INK2, ab)
        text(c, "R$ 1.200,00", 580, 570, 66, "black", ORANGE, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1060, 340, 560, 330, 26, "#FFFFFF", acc, shadow=True)
        text(c, "SISTEMA 2", 1340, 400, 30, "black", GRAY, acc)
        text(c, "juros pagos", 1340, 470, 28, "bold", INK2, acc)
        text(c, "R$ 1.231,35", 1340, 570, 66, "black", ORANGE, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        text_mid(c, "?", W / 2, 510, 110, "black", AMBER, ad)
        selo(c, W / 2, 760, ad, "A TAXA É IGUAL. O QUE MUDA?", AMBER, -2, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular a parcela da Price com o fator dado", "parcela = valor financiado × fator"),
            ("02.b", "separar juros e amortização", "juros → amortização → novo saldo"),
            ("02.c", "dizer quando o SAC ou a Price paga menos", "SAC × Price, lado a lado")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 30, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE DO EPISÓDIO 3", "AS TRÊS CONTAS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    rows = [("1", "JUROS", "= taxa × saldo", ORANGE), ("2", "AMORTIZAÇÃO", "= parcela − juros", BLUE),
            ("3", "NOVO SALDO", "= saldo − amortização", PURPLE)]
    for k, (n_, tit, f_, col) in enumerate(rows):
        ak = ep(t, C["03.a"] + 0.8 + 1.6 * k, 0.4) if aa > 0 else 0
        if ak <= 0:
            continue
        y = 300 + k * 120
        badge_num(c, n_, 300, y, ak, 30, bg=col)
        text(c, tit, 360, y + 14, 40, "black", col, ak, align="left")
        text(c, f_, 720, y + 14, 40, "black", INK, ak, align="left")
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 1240, 270, 420, 330, 22, "#FFFFFF", ab, shadow=True)
        text(c, "SAC", 1450, 320, 34, "black", BLUE, ab)
        for k in range(5):
            rrect(c, 1290 + k * 66, 370, 56, 150, 8, mix("#FFFFFF", BLUE, 0.35), ab)
            text(c, "2 000", 1290 + k * 66 + 28, 452, 15, "black", BLUE, ab)
        text(c, "fatias IGUAIS de dívida", 1450, 570, 26, "black", BLUE, ab)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UM CARNÊ DE LOJA", "12 PARCELAS IGUAIS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    carne(c, 300, 270, 460, 330, aa)
    if aa > 0:
        text(c, "CREDIÁRIO = compra a prazo, em parcelas mensais", 540, 700, 26, "black", BLUE,
             ep(t, C["04.a"] + 0.8, 0.4))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 900, 300, 760, 260, 26, mix("#FFFFFF", AMBER, 0.10), ab)
        text(c, "parcela sempre igual...", 1280, 380, 40, "black", INK, ab)
        text(c, "a DÍVIDA cai sempre", 1280, 450, 44, "black", AMBER, ab)
        text(c, "o mesmo valor?", 1280, 510, 44, "black", AMBER, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        pill(c, "guarde o seu palpite", 1280, 640, PURPLE, size=30, a=acc, anchor="center")


# ======================================================================
# bloco a — a Price e o fator
# ======================================================================

def b_price(c, t, C, B):
    head_seq(c, t, C, [("05", "SISTEMA PRICE", "OU FRANCÊS", BLUE), ("06", "A PARCELA", "VALOR × FATOR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        text(c, "SISTEMA PRICE  (ou francês)", W / 2, 270, 56, "black", BLUE, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            for k in range(5):
                rrect(c, 420 + k * 230, 340, 170, 210, 14, mix("#FFFFFF", BLUE, 0.18), ab)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(420 + k * 230, 340, 170, 210), 14, 14),
                            paint(BLUE, ab, stroke=3))
                text(c, "parcela", 505 + k * 230, 430, 24, "bold", BLUE, ab)
                text(c, "IGUAL", 505 + k * 230, 480, 30, "black", BLUE, ab)
            text(c, "PARCELA FIXA: todas as parcelas iguais", W / 2, 610, 32, "black", BLUE, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 330, 660, 1260, 120, 22, mix("#FFFFFF", GREEN, 0.10), acc)
            text(c, "a fórmula NÃO é cobrada: a prova DÁ o fator (ou a parcela)", W / 2, 734, 34, "black", GREEN, acc)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        regra(c, "PARCELA  =  valor financiado  ×  fator", W / 2, 260, aa, 44)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        linha(c, [("R$ 10.000,00", BLUE), ("  ·  5 parcelas  ·  4% ao mês  ·  fator ", INK), ("0,224627", PURPLE)],
              W / 2, 380, 38, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 420, 450, 1080, 120, 22, "#FFFFFF", acc, shadow=True)
        linha(c, [("10.000 × 0,224627 ≈ ", INK), ("R$ 2.246,27", GREEN), (" por mês", INK)], W / 2, 510, 50, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        linha(c, [("sem juros: 10.000 ÷ 5 = R$ 2.000,00", INK2)], W / 2, 650, 34, ad)
        conferido(c, "com juros: um pouco mais", 720, 730, ep(t, C["06.d"] + 2.2, 0.4), True, 34)


def b_atalho1(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TOTAL DE JUROS DA PRICE", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 200, "ATALHO",
             ["total pago = parcela × nº de parcelas", "juros = total pago − valor financiado"], aa, 38)
    if aa > 0:
        linha(c, [("2.246,27 × 5 = ", INK), ("R$ 11.231,35", PURPLE), (" pagos", INK)], W / 2, 520, 50,
              ep(t, C["07.a"] + 1.6, 0.4))
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("11.231,35 − 10.000 = ", INK), ("R$ 1.231,35", ORANGE), (" de juros", INK)], W / 2, 630, 50, ab)
        selo(c, W / 2, 750, ep(t, C["07.b"] + 2.0, 0.4), "O NÚMERO DO COMEÇO DA AULA", AMBER, -2, 30)


# ======================================================================
# bloco b — a tabela e a caixa
# ======================================================================

def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("08", "1º MÊS", "JUROS → AMORTIZAÇÃO → SALDO", PURPLE),
                       ("09", "2º MÊS", "OS JUROS CAEM, A AMORTIZAÇÃO CRESCE", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    x0 = 330
    if sid == "08":
        agora(c, W / 2, 230, ep(t, C["08.a"], 0.5), "R$ 10.000,00")
        rows = [("1", "10.000,00", "400,00" if t >= C["08.b"] else "", "1.846,27" if t >= C["08.c"] else "",
                 "2.246,27")]
        tabela(c, x0, 300, rows, ep(t, C["08"], 0.5))
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            linha(c, [("juros = 4% × 10.000 = ", INK), ("400", ORANGE)], 560, 560, 38, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            linha(c, [("amortização = 2.246,27 − 400 = ", INK), ("1.846,27", BLUE)], 640, 630, 38, acc)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            linha(c, [("novo saldo = 10.000 − 1.846,27 = ", INK), ("8.153,73", PURPLE)], 660, 700, 38, ad)
        caixa(c, 1400, 470, 200, 260, 400, 1846.27, ep(t, C["08.b"], 0.5), size=24)
        return
    agora(c, W / 2, 230, ep(t, C["09"], 0.5), "R$ 8.153,73")
    rows = [("1", "10.000,00", "400,00", "1.846,27", "2.246,27"),
            ("2", "8.153,73", "326,15" if t >= C["09.a"] else "", "1.920,12" if t >= C["09.b"] else "", "2.246,27")]
    tabela(c, x0, 300, rows, 1.0, destaque=1)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        linha(c, [("juros ", INK), ("400 → 326,15", ORANGE), ("  ·  amortização ", INK), ("1.846,27 → 1.920,12", BLUE)],
              W / 2, 560, 34, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        regra(c, "AMORTIZAÇÃO CRESCENTE: a cada mês, mais da parcela abate a dívida", W / 2, 660, acc, 32, BLUE)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        pill(c, "o último mês acerta os centavos de arredondamento", W / 2, 760, GRAY, size=24, a=ad, anchor="center")


def b_caixa(c, t, C, B):
    head(c, t, B["start"], "A PARCELA É UMA CAIXA", "DE TAMANHO FIXO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.5)
    if a0 > 0:
        conferido(c, "a dívida NÃO cai sempre o mesmo valor", 300, 230, a0, False, 32)
    aa = ep(t, C["10.a"], 0.5)
    u = ep(t, C["10.b"], C["10.d"] - C["10.b"] + 1.0) if t >= C["10.b"] else 0
    for k, (am, ju) in enumerate(PRICE):
        ak = aa * clamp(u * 5 - k + 1) if k else aa
        if ak <= 0:
            continue
        x = 300 + k * 270
        caixa(c, x, 300, 200, 360, ju, am, ak, size=22)
        text(c, f"{k + 1}º mês", x + 100, 700, 26, "bold", GRAY, ak)
    legenda(c, 520, 770, ep(t, C["10.b"], 0.5))
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        pill(c, "quase toda azul", 300 + 4 * 270 + 100, 260, BLUE, size=24, a=ad, anchor="center")


# ======================================================================
# bloco c — a primeira linha
# ======================================================================

def b_linha1(c, t, C, B):
    head(c, t, B["start"], "A PRIMEIRA PARCELA", "SAC × PRICE", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    agora(c, W / 2, 230, aa, "R$ 10.000,00 nos dois")
    for k, (nome, am, col, sub) in enumerate((("SAC", 2000, BLUE, "10.000 ÷ 5 = 2.000 (fixa)"),
                                               ("PRICE", 1846.27, PURPLE, "2.246,27 − 400 = 1.846,27"))):
        x = 330 + k * 660
        if aa <= 0:
            continue
        rrect(c, x, 290, 600, 450, 24, "#FFFFFF", aa, shadow=True)
        text(c, nome, x + 300, 345, 38, "black", col, aa)
        linha(c, [("juros: 4% × 10.000 = ", INK), ("400", ORANGE)], x + 300, 420, 32, aa)
        ak = ep(t, C["11.b" if k == 0 else "11.c"], 0.5)
        if ak > 0:
            caixa(c, x + 60, 470, 180, 240, 400, am, ak, size=22, total=2400)
            text(c, "amortização", x + 420, 540, 26, "black", BLUE, ak)
            text(c, brl(am, False), x + 420, 600, 44, "black", BLUE, ak)
            text(c, sub, x + 420, 660, 20, "bold", GRAY, ak)
    if aa > 0:
        selo(c, W / 2, 790, ep(t, C["11.a"] + 2.4, 0.4), "JUROS DA 1ª PARCELA: IGUAIS", ORANGE, -2, 28)


def b_atalho2(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUANTO DA 1ª PARCELA ABATE A DÍVIDA?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 260, 260, 1400, 200, "SEM TABELA", ["abate  =  parcela  −  taxa × valor financiado"], aa, 46)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        linha(c, [("2.246,27 − 0,04 × 10.000 = ", INK), ("1.846,27", BLUE)], W / 2, 600, 48, ab)
        pill(c, "uma linha e acabou", W / 2, 710, GREEN, size=30, a=ep(t, C["12.b"] + 1.0, 0.4), anchor="center")


# ======================================================================
# bloco d — lado a lado
# ======================================================================

def b_lado(c, t, C, B):
    head_seq(c, t, C, [("13", "LADO A LADO", "MESMA DÍVIDA, PERFIS OPOSTOS", BLUE),
                       ("14", "QUEM PAGA MAIS?", "NO COMEÇO E NO TOTAL", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    aa = ep(t, C["13.a"], 0.5) if sid == "13" else 1
    ab = ep(t, C["13.b"], 0.5) if sid == "13" else 1
    pa = ep(t, C["13.a"], 2.0) if sid == "13" else 1
    pb = ep(t, C["13.b"], 2.0) if sid == "13" else 1
    barras(c, 260, 290, 600, 330, SAC, aa, pa, "SAC", BLUE)
    barras(c, 1060, 290, 600, 330, PRICE, ab, pb, "PRICE", PURPLE)
    legenda(c, 640, 225, ep(t, C["13"], 0.5), 24)
    if sid == "13":
        if aa > 0:
            text(c, "amortização CONSTANTE · parcela DIMINUI", 560, 710, 26, "black", BLUE, ep(t, C["13.a"] + 1.4, 0.4))
            text(c, "fatias iguais de dívida", 560, 750, 24, "bold", GRAY, ep(t, C["13.a"] + 1.4, 0.4))
        if ab > 0:
            text(c, "parcela CONSTANTE · amortização CRESCE", 1360, 710, 26, "black", PURPLE,
                 ep(t, C["13.b"] + 1.4, 0.4))
            text(c, "caixas iguais de pagamento", 1360, 750, 24, "bold", GRAY, ep(t, C["13.b"] + 1.4, 0.4))
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            pill(c, "nos dois, os JUROS (laranja) CAEM", W / 2, 805, ORANGE, size=24, a=acc, anchor="center")
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("1ª parcela: ", INK), ("2.400,00", BLUE)], 560, 700, 32, aa)
        linha(c, [("1ª parcela: ", INK), ("2.246,27", PURPLE)], 1360, 700, 32, aa)
    ab2 = ep(t, C["14.b"], 0.5)
    if ab2 > 0:
        linha(c, [("juros total: ", INK), ("1.200,00", GREEN)], 560, 745, 32, ab2)
        linha(c, [("juros total: ", INK), ("1.231,35", RED)], 1360, 745, 32, ab2)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 812, acc, "SAC: COMEÇA MAIS PESADO, TERMINA MAIS BARATO", GREEN, 0, 26)


# ======================================================================
# bloco e — por que o SAC paga menos
# ======================================================================

def b_porque(c, t, C, B):
    head_seq(c, t, C, [("15", "POR QUE O SAC PAGA MENOS?", "MESMA TAXA", PURPLE),
                       ("16", "ONDE CADA UM APARECE", "NA VIDA REAL", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        agora(c, W / 2, 230, aa, "depois da 1ª parcela")
        ab = ep(t, C["15.b"], 0.5)
        for k, (nome, deve, col) in enumerate((("SAC", 8000.0, BLUE), ("PRICE", 8153.73, PURPLE))):
            if ab <= 0:
                continue
            y = 330 + k * 150
            text(c, nome, 330, y + 14, 36, "black", col, ab, align="left")
            wbar = 900 * deve / 10000
            rrect(c, 520, y - 30, wbar, 60, 10, mix("#FFFFFF", col, 0.3), ab)
            text(c, "deve " + brl(deve), 540, y + 12, 30, "black", INK, ab, align="left")
            acc = ep(t, C["15.c"], 0.5)
            if acc > 0:
                linha(c, [("juros do 2º mês: ", INK), (brl(deve * 0.04, False), ORANGE)], 1580, y, 30, acc)
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            regra(c, "o SAC abate MAIS DEPRESSA → juro só incide sobre o que se deve", W / 2, 720, ad, 32)
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 260, 640, 440, 24, "#FFFFFF", aa, shadow=True)
        text(c, "SAC", 580, 320, 44, "black", BLUE, aa)
        # casinha
        p = skia.Path(); p.moveTo(480, 470); p.lineTo(580, 390); p.lineTo(680, 470); p.close()
        c.drawPath(p, paint(BLUE, aa))
        rrect(c, 500, 470, 160, 110, 6, mix("#FFFFFF", BLUE, 0.3), aa)
        text(c, "FINANCIAMENTO IMOBILIÁRIO", 580, 640, 26, "black", BLUE, aa)
        text(c, "a casa, em muitos anos", 580, 676, 22, "bold", GRAY, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        rrect(c, 1020, 260, 640, 440, 24, "#FFFFFF", ab, shadow=True)
        text(c, "PRICE", 1340, 320, 44, "black", PURPLE, ab)
        carne(c, 1230, 380, 200, 150, ab, valor="")
        text(c, "CREDIÁRIO · CRÉDITO PESSOAL", 1340, 640, 26, "black", PURPLE, ab)
        text(c, "parcela fixa = previsível", 1340, 676, 22, "bold", GRAY, ab)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "NA ORDEM", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 110, 24, "#F7F7F5", aa)
        linha(c, [("R$ 5.000,00", BLUE), ("  ·  Price  ·  5 × ", INK), ("R$ 1.091,77", PURPLE), ("  ·  3% ao mês", INK)],
              W / 2, 265, 44, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        for k, s_ in enumerate(("juros = ?", "amortização = ?", "saldo = ?")):
            chip(c, s_, 520 + k * 440, 390, (ORANGE, BLUE, PURPLE)[k], ab, 34, fill=False)
    if t < C["18"]:
        pause_timer(c, t, C["17.end"] - 1.9, W / 2, 600)
        return
    agora(c, W / 2, 480, ep(t, C["18.a"], 0.4), "R$ 5.000,00")
    rows = [("18.a", [("juros = 3% × 5.000 = ", INK), ("150,00", ORANGE)]),
            ("18.b", [("amortização = 1.091,77 − 150 = ", INK), ("941,77", BLUE)]),
            ("18.c", [("saldo = 5.000 − 941,77 = ", INK), ("R$ 4.058,23", GREEN)])]
    for k, (cue, partes) in enumerate(rows):
        linha(c, partes, 800, 570 + k * 80, 40, ep(t, C[cue] + (1.4 if k == 0 else 0), 0.4))
    caixa(c, 1450, 540, 170, 230, 150, 941.77, ep(t, C["18.b"], 0.5), size=22)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Na Price, a parcela é fixa e a amortização cresce.",
          "Na primeira parcela, os juros são iguais nos dois sistemas: taxa × valor financiado.",
          "Mesma taxa, mas o SAC paga menos juros porque abate a dívida mais cedo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 60)


ERROS = [("Achar que, na Price, a AMORTIZAÇÃO é constante", "alguma coisa é constante na Price...",
          "constante é a PARCELA; amortização constante é o SAC"),
         ("Achar que SAC e Price custam os MESMOS juros", "a taxa, o prazo e a dívida são iguais",
          "o juro depende de quanto se deve: o SAC deve menos mais cedo"),
         ("Abater a PARCELA INTEIRA: 10.000 − 2.246,27 = 7.753,73", "você pagou a parcela inteira",
          "os 400 de juros não abatem nada: só a AMORTIZAÇÃO sai do saldo (8.153,73)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questões do material
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


ALTS4 = [("A", "R$ 1.666,67", "ignorou os juros", RED), ("B", "R$ 1.700,00", "2% uma vez só", RED),
         ("C", "R$ 1.892,00", "", GREEN), ("D", "R$ 2.066,67", "juros simples", RED),
         ("E", "R$ 22.704,00", "total pago", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "PARCELA NA PRICE COM FATOR DADO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    yend = _enunciado(c, [("Uma pessoa financiou R$ 20.000,00 em 12 parcelas mensais iguais, pelo sistema Price, com "
                           "juros de 2% ao mês. Para essa taxa e esse prazo, o valor da parcela é obtido multiplicando-se "
                           "o valor financiado pelo fator 0,0946. O valor de cada parcela é", INK)], a0, 230, 25)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 40, C["24.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["24"], 0.4))
        pill(c, "PRICE · fator dado · ×", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["24"], 0.4), anchor="center")
        linha(c, [("20.000 × 0,0946 = ", INK), ("R$ 1.892,00", GREEN)], 540, y0 + 105, 32, ep(t, C["24.a"], 0.4))
        linha(c, [("sem juros: 20.000 ÷ 12 ≈ 1.666,67", INK2)], 540, y0 + 165, 26, ep(t, C["24.b"], 0.4))
        conferido(c, "com juros: um pouco mais", 260, y0 + 225, ep(t, C["24.b"] + 2.6, 0.4), True, 26)


ALTS9 = [("A", "R$ 1.492,00", "é a amortização", RED), ("B", "R$ 18.108,00", "abateu a parcela inteira", RED),
         ("C", "R$ 18.333,33", "amortização do SAC", RED), ("D", "R$ 18.508,00", "", GREEN),
         ("E", "R$ 20.400,00", "não descontou o pagamento", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · NÓS FAZEMOS", "SALDO DEVEDOR NA PRICE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    yend = _enunciado(c, [("No financiamento da questão 4 (R$ 20.000,00 em 12 parcelas de R$ 1.892,00, a 2% ao mês, pelo "
                           "sistema Price), o saldo devedor imediatamente após o pagamento da primeira parcela é", INK)],
                      a0, 230, 25)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS9, 1000, 250, 680, 40, C["27.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["27"]:
        pause_timer(c, t, C["26.end"] - 1.9, 540, yend + 150)
    if t >= C["27"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["27"], 0.4))
        agora(c, 540, y0 + 45, ep(t, C["27"], 0.4), "20.000", 22)
        linha(c, [("juros = 2% × 20.000 = ", INK), ("400", ORANGE)], 540, y0 + 110, 28, ep(t, C["27.a"], 0.4))
        linha(c, [("amortização = 1.892 − 400 = ", INK), ("1.492", BLUE)], 540, y0 + 165, 28, ep(t, C["27.b"], 0.4))
        linha(c, [("saldo = 20.000 − 1.492 = ", INK), ("18.508", GREEN)], 540, y0 + 220, 28, ep(t, C["27.c"], 0.4))
        conferido(c, "caiu pouco: no começo, muito juro", 230, y0 + 280, ep(t, C["27.d"], 0.4), True, 24)


ALTS5 = [("A", "no SAC, as parcelas diminuem ao longo do tempo, porque a amortização é constante e os juros incidem "
               "sobre um saldo cada vez menor.", "", GREEN),
         ("B", "na Price, a amortização é a mesma em todas as parcelas, e por isso as parcelas são iguais.",
          "", RED),
         ("C", "no SAC, os juros pagos em cada parcela são iguais, pois a taxa é fixa.", "", RED),
         ("D", "na Price, a primeira parcela é maior que a primeira parcela do SAC.", "", RED),
         ("E", "os dois sistemas resultam no mesmo total de juros, pois a taxa e o prazo são iguais.", "", RED)]
MOTIVOS5 = [("B", "troca: amortização constante é do SAC"), ("D", "troca: a 1ª parcela MAIOR é a do SAC"),
            ("C", "taxa fixa ≠ juros fixos: nos dois, os juros caem"), ("E", "apaga a diferença: o SAC paga menos")]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "SAC E PRICE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    yend = _enunciado(c, [("Um banco oferece o mesmo valor de financiamento, com a mesma taxa de juros e o mesmo número de "
                           "parcelas, pelo SAC ou pelo sistema Price. A respeito dessas duas opções, é correto afirmar que",
                           INK)], a0, 230, 24, 640)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["30"], 0.3)),
         align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS5, 880, 215, 830, 24, C["30.ok"], "A", cues_in, cues_x, gap=16)
    if t < C["30"]:
        pause_timer(c, t, C["29.end"] - 1.9, 480, yend + 150)
    if t >= C["30"]:
        y0 = yend + 4
        rrect(c, 170, y0, 680, 830 - y0, 18, "#FFFFFF", ep(t, C["30"], 0.4), shadow=True)
        pill(c, "A descreve exatamente o SAC", 510, y0 + 45, GREEN, size=22, a=ep(t, C["30.a"], 0.4), anchor="center")
        if t < C["31"]:
            barras(c, 260, y0 + 110, 500, 150, SAC, ep(t, C["30.a"], 0.4), 1.0, rot_parcela=False)
        else:
            for k, (L, m) in enumerate(MOTIVOS5):
                ak = ep(t, C[f"31.x{L.lower()}"], 0.4)
                badge_num(c, L, 210, y0 + 110 + k * 56, ak, 18, bg=RED)
                text(c, m, 240, y0 + 118 + k * 56, 21, "black", RED, ak, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    items = [("33.a", "JUNTAMOS TUDO", "parcelas · entrada · SAC · Price", BLUE),
             ("33.b", "CAÇAMOS AS PEGADINHAS", "os erros que mais custam pontos", AMBER),
             ("33.c", "QUESTÕES INÉDITAS", "treino no estilo do ENEM", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(items):
        a, d = rise(t, C[cue])
        x = 260 + k * 480
        rrect(c, x, 300 + d, 420, 320, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 300 + d, 420, 70, 24, col, a * 0.15)
        text(c, tit, x + 210, 346 + d, 28, "black", col, a)
        para(c, sub, x + 40, 450 + d, 30, "bold", INK2, a, 340, 40)
    pill(c, "ep. 5 · revisão de empréstimos, financiamentos e parcelamentos", W / 2, 760, PURPLE, size=28,
         a=ep(t, C["33.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"],
        "Você sabia que a parcela fixa custa mais juros?", canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, price=b_price, atalho1=b_atalho1,
              tabela=b_tabela, caixa=b_caixa, linha1=b_linha1, atalho2=b_atalho2, lado=b_lado, porque=b_porque,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q9=b_q9, q5=b_q5, ponte=b_ponte, cta=b_cta)
