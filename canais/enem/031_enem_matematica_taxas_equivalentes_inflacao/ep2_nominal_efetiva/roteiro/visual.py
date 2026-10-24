"""Visual — Taxas Equivalentes e Inflação, Episódio 2: taxa nominal × efetiva e taxas acumuladas (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: contrato() (folha com a letra miúda e o "capitalizados mensalmente" grifado), vitrine_caixa()
(etiqueta da VITRINE com a nominal × visor do CAIXA com a efetiva), fatias() (a etiqueta "24% a.a." cortada em 12
fatias de 2%, cada uma multiplicando o saldo até o caixa mostrar 26,8%), extrato() (três meses com a taxa e o FATOR com
sinal ao lado), tabela_nominal(), linha(), caixa(), conferido().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum031", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_taxas_inflacao_ep2_nominal_efetiva.mp4"
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


def contrato(c, x, y, a, grifo=0.0, w=640, h=520):
    """folha de contrato com linhas cinza e a cláusula da taxa; grifo = marca-texto sobre 'capitalizados mensalmente'"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    text(c, "CONTRATO DE EMPRÉSTIMO", x + w / 2, y + 60, 28, "black", INK2, a)
    for k in range(9):
        yy = y + 110 + k * 42
        if k in (4, 5):
            continue
        ww = w - 90 - (120 if k % 3 == 2 else 0)
        rrect(c, x + 45, yy, ww, 12, 6, "#D9DEE8", a)
    yy = y + 110 + 4 * 42 - 14
    if grifo > 0:
        rrect(c, x + 36, yy + 44, (w - 70) * clamp(grifo), 40, 8, "#FFE27A", a * 0.9)
    text(c, "Cláusula 3: taxa de 24% a.a.,", x + 45, yy + 26, 28, "bold", INK, a, align="left")
    text(c, "capitalizados mensalmente.", x + 45, yy + 74, 28, "bold", INK, a, align="left")
    text(c, "letra miúda", x + w - 30, y + h - 24, 20, "medium", GRAY, a, align="right")


def vitrine_caixa(c, cx, cy, a, nom="24% a.a.", efe="26,8% a.a.", ae=1.0, gap=520):
    """VITRINE (etiqueta com a nominal) × CAIXA (visor com a efetiva)"""
    if a <= 0:
        return
    x1, x2 = cx - gap / 2, cx + gap / 2
    rrect(c, x1 - 210, cy - 150, 420, 300, 26, mix("#FFFFFF", BLUE, 0.07), a, shadow=True)
    text(c, "VITRINE", x1, cy - 100, 28, "black", BLUE, a)
    rrect(c, x1 - 150, cy - 50, 300, 130, 18, "#FFF7E0", a, stroke=4, stroke_color=AMBER)
    text_mid(c, nom, x1, cy + 15, 56, "black", INK, a)
    text(c, "taxa NOMINAL", x1, cy + 125, 26, "bold", GRAY, a)
    if ae > 0:
        arrow(c, x1 + 225, cy, x2 - 225, cy, PURPLE, a * ae, 6, 22)
        rrect(c, x2 - 210, cy - 150, 420, 300, 26, mix("#FFFFFF", GREEN, 0.08), a * ae, shadow=True)
        text(c, "CAIXA", x2, cy - 100, 28, "black", GREEN, a * ae)
        rrect(c, x2 - 160, cy - 50, 320, 130, 14, "#1F2937", a * ae)
        text_mid(c, efe, x2, cy + 15, 54, "black", "#7CF29A", a * ae)
        text(c, "taxa EFETIVA", x2, cy + 125, 26, "bold", GRAY, a * ae)


def fatias(c, t, x0, y, a, t_corte, t_mult, w=1440, n=12, dur=6.0):
    """a etiqueta '24% a.a.' cortada em n fatias de 2%; depois cada fatia acende multiplicando o saldo (× 1,02)"""
    if a <= 0:
        return
    corte = ep(t, t_corte, 1.0)
    gap = 10 * corte
    fw = (w - gap * (n - 1)) / n
    k_on = int(clamp((t - t_mult) / dur) * n + 1e-6) if t >= t_mult else 0
    for k in range(n):
        x = x0 + k * (fw + gap)
        on = k < k_on
        col = GREEN if on else AMBER
        rrect(c, x, y, fw, 110, 12, mix("#FFFFFF", col, 0.25 if on else 0.12), a, stroke=3, stroke_color=col)
        if corte > 0.6:
            text_mid(c, "2%", x + fw / 2, y + 40, 30, "black", col, a)
            text(c, "× 1,02", x + fw / 2, y + 92, 20, "bold", INK2 if on else GRAY, a)
    if corte < 0.6:
        text_mid(c, "24% a.a.", x0 + w / 2, y + 55, 64, "black", AMBER, a * (1 - corte / 0.6))
    else:
        K.mdraw(c, "24% ÷ 12 = 2% por mês", x0 + w / 2, y - 34, 34, PURPLE, a * ep(t, t_corte + 0.6, 0.4), align="center")
    if t >= t_mult:
        v = 1.02 ** k_on
        s = f"{v:.3f}".replace(".", ",")
        rrect(c, x0 + w / 2 - 260, y + 160, 520, 110, 18, "#1F2937", a)
        text(c, "saldo", x0 + w / 2 - 230, y + 228, 24, "bold", "#9CA3AF", a, align="left")
        text_mid(c, f"× {s}", x0 + w / 2 + 40, y + 215, 54, "black", "#7CF29A", a)


def extrato(c, cx, y0, a, linhas, alfas, w=760, fator_a=1.0):
    """extrato do fundo: [(mês, taxa, fator, cor)]; fator com sinal ao lado de cada taxa"""
    if a <= 0:
        return
    h = 90 + len(linhas) * 92
    rrect(c, cx - w / 2, y0, w, h, 22, "#FFFFFF", a, shadow=True)
    text(c, "EXTRATO DO FUNDO", cx - w / 2 + 30, y0 + 52, 26, "black", INK2, a, align="left")
    text(c, "fator", cx + w / 2 - 90, y0 + 52, 24, "bold", PURPLE, a * fator_a)
    for k, (mes, tx, fat, col) in enumerate(linhas):
        aa = a * alfas[k]
        if aa <= 0:
            continue
        yy = y0 + 90 + k * 92
        rrect(c, cx - w / 2 + 20, yy, w - 40, 76, 14, mix("#FFFFFF", col, 0.10), aa)
        text_mid(c, mes, cx - w / 2 + 50, yy + 38, 30, "bold", INK2, aa, align="left")
        text_mid(c, tx, cx - 40, yy + 38, 44, "black", col, aa)
        if fator_a > 0:
            pill(c, fat, cx + w / 2 - 90, yy + 38, PURPLE, size=34, a=aa * fator_a, anchor="center", bounds=(0, 1920))


TAB = [("12% a.a. · mensal", "1% ao mês", "1,01¹² − 1", "≈ 12,68%"),
       ("24% a.a. · semestral", "12% ao semestre", "1,12² − 1", "25,44%"),
       ("24% a.a. · mensal", "2% ao mês", "1,02¹² − 1", "≈ 26,8%")]


def tabela_nominal(c, t, x, y, alfas, a=1.0, dest=None):
    """a tabela da seção 04: anúncio (nominal) · taxa por período · conta · efetiva anual"""
    if a <= 0:
        return
    cols = [(x, 470, "ANÚNCIO (NOMINAL)", BLUE), (x + 490, 330, "POR PERÍODO", PURPLE),
            (x + 840, 300, "CONTA", PURPLE), (x + 1160, 300, "EFETIVA ANUAL", GREEN)]
    for cx_, w_, tit, col in cols:
        rrect(c, cx_, y, w_, 56, 14, col, a * 0.15)
        text(c, tit, cx_ + w_ / 2, y + 38, 24, "black", col, a)
    for k, row in enumerate(TAB):
        aa = a * alfas[k]
        if aa <= 0:
            continue
        yy = y + 76 + k * 120
        hl = dest is not None and k in dest
        rrect(c, x - 10, yy - 6, 1480, 104, 18, mix("#FFFFFF", AMBER, 0.14) if hl else "#FFFFFF", aa, shadow=True)
        for (cx_, w_, _, col), s_, sz in zip(cols, row, (32, 32, 34, 44)):
            K.ftext(c, s_, cx_ + w_ / 2, yy + 60, sz, "black", GREEN if col == GREEN else INK, aa)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "TAXA NOMINAL × EFETIVA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    for k, (nome, efe, cue) in enumerate((("CONTRATO 1", "25,44%", "01.b"), ("CONTRATO 2", "26,8%", "01.c"))):
        x = 560 + k * 800
        if aa <= 0:
            continue
        rrect(c, x - 300, 260, 600, 440, 30, "#FFFFFF", aa, shadow=True)
        text(c, nome, x, 320, 30, "black", INK2, aa)
        rrect(c, x - 220, 360, 440, 130, 20, "#FFF7E0", aa)
        text_mid(c, "24% ao ano", x, 425, 58, "black", AMBER, aa)
        text(c, "anunciado", x, 530, 26, "bold", GRAY, aa)
        ab = ep(t, C[cue], 0.5)
        if ab > 0:
            text(c, "custa de verdade", x, 600, 26, "bold", INK2, ab)
            text_mid(c, efe, x, 655, 60, "black", RED, ab)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 800, ad, "MESMA PROPAGANDA, PREÇOS DIFERENTES", RED, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "transformar taxa nominal em efetiva", GREEN),
             ("02.b", "acumular taxas de meses diferentes sem somar", PURPLE)]
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
        pill(c, "EP. 1", 560, 330 + d1, GREEN, size=26, a=a1, anchor="center", bounds=(0, 1920))
        text(c, "trocar o período: ELEVE o fator", 560, 430 + d1, 34, "black", PURPLE, a1)
        K.mdraw(c, "1,01^{12} ≈ 1,127", 560, 540 + d1, 56, INK, a1, align="center")
        text(c, "fator primeiro, taxa depois", 560, 650 + d1, 30, "bold", GREEN, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 440, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "PORCENTAGEM", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        text(c, "em sequência: MULTIPLIQUE", 1360, 430 + d2, 34, "black", PURPLE, a2)
        text(c, "os fatores", 1360, 478 + d2, 34, "black", PURPLE, a2)
        a3 = ep(t, C["03.b"] + 3.5, 0.4)
        linha(c, [("− 10%  →  ", INK2), ("0,9", PURPLE)], 1360, 600 + d2, 56, a3)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "A LETRA MIÚDA", "CAPITALIZAÇÃO", BLUE),
                       ("05", "O EXTRATO DO FUNDO", "SUBIU, SUBIU, CAIU", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        contrato(c, 220, 260, ep(t, C["04.a"], 0.5), grifo=ep(t, C["04.a"] + 1.2, 1.0))
        defs = [("04.b", "CAPITALIZAR", "somar os juros ao saldo:", "a partir daí eles rendem juros"),
                ("04.c", "PERÍODO DE CAPITALIZAÇÃO", "de quanto em quanto tempo", "isso acontece (aqui: todo mês)")]
        for k, (cue, nome, s1, s2) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 290 + k * 250 + d
            rrect(c, 960, y, 760, 210, 22, mix("#FFFFFF", BLUE, 0.07), a)
            text(c, nome, 1000, y + 64, 36, "black", BLUE, a, align="left")
            text(c, s1, 1000, y + 122, 30, "bold", INK2, a, align="left")
            text(c, s2, 1000, y + 168, 30, "bold", INK2, a, align="left")
        return
    aa = ep(t, C["05.a"], 0.5)
    ab = C["05.b"]
    extrato(c, W / 2, 260, aa, [("mês 1", "+ 10%", "", GREEN), ("mês 2", "+ 20%", "", GREEN),
                                ("mês 3", "− 10%", "", RED)],
            [ep(t, ab, 0.4), ep(t, ab + 1.4, 0.4), ep(t, ab + 2.6, 0.4)], fator_a=0.0)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        text_mid(c, "rendeu quanto no total?", W / 2, 720, 50, "black", AMBER, acc)


# ======================================================================
# bloco a — taxa nominal
# ======================================================================

def b_nominal(c, t, C, B):
    head_seq(c, t, C, [("06", "TAXA NOMINAL", "VITRINE × CAIXA", BLUE),
                       ("07", "A ÚNICA DIVISÃO", "PELO NÚMERO DE CAPITALIZAÇÕES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 250, 1460, 120, 22, mix("#FFFFFF", BLUE, 0.08), aa)
            text(c, "NOMINAL: anunciada num período (ano), capitalizada em outro (mês)", W / 2, 325, 34, "black",
                 BLUE, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            text(c, "EFETIVA: a que você REALMENTE paga no período", W / 2, 440, 34, "black", GREEN, ab)
        vitrine_caixa(c, W / 2, 650, ep(t, C["06.c"], 0.5), efe="?", ae=ep(t, C["06.c"] + 1.6, 0.5))
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        regra(c, "a nominal só serve para DIVIDIR pelas capitalizações", W / 2, 290, aa, 40, PURPLE)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        K.mdraw(c, "24% ÷ 12 = 2% ao mês", W / 2, 450, 76, INK, ab, align="center")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "2% ao mês é EFETIVA: cobrada a cada mês", W / 2, 590, GREEN, size=36, a=acc, anchor="center",
             bounds=(0, 1920))
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 740, ad, "A ÚNICA DIVISÃO PERMITIDA", PURPLE, -3, 36)


# ======================================================================
# bloco b — capitalize
# ======================================================================

def b_capitaliza(c, t, C, B):
    head_seq(c, t, C, [("08", "DEPOIS, CAPITALIZE", "12 FATIAS DE 2%", PURPLE),
                       ("09", "ATALHO DE PROVA", "DIVIDA, ELEVE, TIRE 1", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        fatias(c, t, 240, 290, ep(t, C["08"], 0.4), C["08"] + 0.3, C["08.a"] + 0.5, dur=4.5)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            K.mdraw(c, "1,02^{12} ≈ 1,268", 560, 720, 60, PURPLE, ab, align="center")
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            linha(c, [("1,268 − 1  →  ", INK2), ("26,8% ao ano", GREEN)], 1330, 720, 54, acc)
            pill(c, "o preço do CAIXA", 1330, 800, GREEN, size=28, a=acc, anchor="center", bounds=(0, 1920))
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 260, 1400, 220, "NOMINAL → EFETIVA EM 3 PASSOS", ["1. DIVIDA pelas capitalizações",
                                                                          "2. ELEVE o fator · 3. TIRE 1"], aa, 40)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 560, 1200, 200, 24, "#FFFFFF", ab, shadow=True)
        text(c, "CONFIRA", W / 2, 615, 28, "black", GREEN, ab)
        linha(c, [("efetiva ", INK), ("um pouco ACIMA", GREEN), (" da nominal", INK)], W / 2, 690, 48, ab)


# ======================================================================
# bloco c — a tabela
# ======================================================================

def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("10", "MESMA NOMINAL, CUSTOS DIFERENTES", "A TABELA", PURPLE),
                       ("11", "A REGRA", "MAIS FREQUENTE, MAIOR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        al = [ep(t, C["10.a"], 0.5), ep(t, C["10.b"], 0.5), ep(t, C["10.c"], 0.5)]
        tabela_nominal(c, t, 220, 260, al, dest=(1, 2) if t >= C["10.c"] + 2.5 else None)
        if ep(t, C["10.c"] + 2.5, 0.4) > 0:
            selo(c, 1560, 760, ep(t, C["10.c"] + 2.5, 0.4), "O GANCHO, RESOLVIDO", GREEN, -4, 28)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        regra(c, "capitalização MAIS frequente → efetiva MAIOR", W / 2, 280, aa, 42, PURPLE)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 360, 1400, 120, 22, mix("#FFFFFF", AMBER, 0.12), ab)
        text(c, "para comparar: todas EFETIVAS no mesmo período", W / 2, 435, 38, "black", AMBER, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        K.atalho(c, 260, 520, 1400, 270, "ATALHO DO SEMESTRE",
                 ["efetiva = nominal + (taxa do semestre)²", "24% + 12%² = 24% + 1,44% = 25,44%"], acc, 38)


# ======================================================================
# bloco d — taxas acumuladas
# ======================================================================

def b_acumulada(c, t, C, B):
    head_seq(c, t, C, [("12", "TAXAS ACUMULADAS", "FATOR AO LADO DE CADA MÊS", PURPLE),
                       ("13", "POR QUE NÃO 20%?", "EM REAIS", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        a0 = C["12.a"]
        extrato(c, 620, 250, ep(t, C["12"], 0.4), [("mês 1", "+ 10%", "1,1", GREEN), ("mês 2", "+ 20%", "1,2", GREEN),
                                                  ("mês 3", "− 10%", "0,9", RED)],
                [1.0, 1.0, 1.0], w=760, fator_a=1.0 if t >= a0 else 0.0)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            rrect(c, 1080, 260, 620, 200, 24, mix("#FFFFFF", PURPLE, 0.08), ab, shadow=True)
            text(c, "MULTIPLIQUE", 1390, 310, 28, "black", PURPLE, ab)
            linha(c, [("1,1 · 1,2 · 0,9 = ", INK), ("1,188", PURPLE)], 1390, 390, 46, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            rrect(c, 1080, 500, 620, 160, 24, mix("#FFFFFF", GREEN, 0.10), acc, shadow=True)
            text(c, "TAXA ACUMULADA", 1390, 550, 26, "black", BLUE, acc)
            text_mid(c, "18,8%", 1390, 610, 64, "black", GREEN, acc)
            linha(c, [("10 + 20 − 10 = 20%", RED)], 1390, 740, 40, acc)
            strike(c, 1200, 740, 1580, 740, acc, RED, ep(t, C["12.c"] + 1.2, 0.6))
        return
    vals = [("13.a", "INÍCIO", "R$ 100,00", BLUE, ""), ("13.a", "MÊS 1", "R$ 110,00", GREEN, "+ 10%"),
            ("13.a", "MÊS 2", "R$ 132,00", GREEN, "+ 20%"), ("13.c", "MÊS 3", "R$ 118,80", RED, "− 10%")]
    for k, (cue, tit, v, col, op) in enumerate(vals):
        a = ep(t, C[cue] + (k * 0.9 if cue == "13.a" else 0), 0.5)
        x = 330 + k * 420
        caixa(c, x, 340, tit, v, col, a, 360)
        if k and a > 0:
            pill(c, op, x - 210, 450, col, size=26, a=a, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 540, 1320, 220, 24, mix("#FFFFFF", AMBER, 0.12), ab, shadow=True)
        text(c, "a queda incide sobre um valor JÁ MAIOR", W / 2, 610, 40, "black", AMBER, ab)
        linha(c, [("10% de 132 = ", INK), ("R$ 13,20", RED), ("   (não R$ 10,00)", GRAY)], W / 2, 690, 42, ab)


# ======================================================================
# bloco e — taxa média
# ======================================================================

def b_media(c, t, C, B):
    head_seq(c, t, C, [("14", "TAXA MÉDIA POR PERÍODO", "É A EQUIVALENTE", BLUE),
                       ("15", "E OS 10,5%?", "TESTE ELEVANDO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        caixa(c, 520, 340, "ACUMULADO EM 2 MESES", "+ 21%  (× 1,21)", BLUE, aa, 560)
        if aa > 0:
            linha(c, [("por mês: ", INK2), ("10,5%", AMBER), ("?", AMBER)], 1320, 340, 56, ep(t, C["14.a"] + 2.4, 0.4))
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            rrect(c, 260, 470, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.08), ab)
            text(c, "TAXA MÉDIA = a taxa CONSTANTE que dá o mesmo acumulado", W / 2, 540, 34, "black", BLUE, ab)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            K.mdraw(c, "1,1^{2} = 1,21", 700, 700, 66, PURPLE, acc, align="center")
            linha(c, [("→  ", INK2), ("10% ao mês", GREEN)], 1290, 700, 60, acc)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        K.mdraw(c, "1,105^{2} ≈ 1,221", 620, 330, 62, INK, aa, align="center")
        linha(c, [("→ 22,1% ", RED), ("> 21%", RED)], 1300, 330, 54, aa)
        selo(c, 1300, 440, ep(t, C["15.a"] + 2.5, 0.4), "PASSA DO ACUMULADO", RED, -3, 28)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        K.atalho(c, 260, 540, 1400, 220, "ATALHO DE PROVA",
                 ["taxa média? TESTE AS ALTERNATIVAS elevando:", "a que volta ao acumulado é a certa"], ab, 38)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "FATOR POR FATOR", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    for k, (L, v, col) in enumerate((("MÊS 1", "+ 20%", GREEN), ("MÊS 2", "− 10%", RED), ("MÊS 3", "+ 5%", GREEN))):
        caixa(c, W / 2 + (k - 1) * 480, 300, L, v, col, aa, 400)
    if t < C["17"]:
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            text_mid(c, "rendimento acumulado?", W / 2, 470, 46, "black", INK, ab)
        pause_timer(c, t, C["16.end"] - 1.9, W / 2, 640)
        return
    a1 = ep(t, C["17.a"], 0.5)
    if a1 > 0:
        for k, f in enumerate(("1,2", "0,9", "1,05")):
            pill(c, f, W / 2 + (k - 1) * 480, 400, PURPLE, size=36, a=a1, anchor="center", bounds=(0, 1920))
    a2 = ep(t, C["17.b"], 0.5)
    if a2 > 0:
        linha(c, [("1,2 · 0,9 = 1,08", INK2), ("   →   1,08 · 1,05 = ", INK), ("1,134", PURPLE)], W / 2, 540, 46, a2)
    a3 = ep(t, C["17.c"], 0.5)
    if a3 > 0:
        linha(c, [("acumulado: ", INK), ("13,4%", GREEN)], 760, 680, 58, a3)
        linha(c, [("soma: 15%", RED)], 1380, 680, 46, a3)
        strike(c, 1270, 680, 1490, 680, a3, RED, ep(t, C["17.c"] + 1.6, 0.6))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Taxa nominal: divida pelas capitalizações e capitalize.",
          "Taxas em sequência: multiplique os fatores, inclusive os menores que 1.",
          "Taxa média por período é a equivalente, não a média das porcentagens."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 60)


ERROS = [("Nominal pela efetiva: 12% a.a. capitalizados por mês = 12%", "é o número escrito no contrato",
          "é o preço da vitrine · no caixa: ≈ 12,68% ao ano"),
         ("Somar taxas: 10% e 20% = 30%", "por cento com por cento",
          "a 2ª incide sobre valor maior · 1,1 · 1,2 = 1,32 → 32%"),
         ("Esquecer de tirar o 1: fator 1,268 = 126,8%", "foi o que a conta deu",
          "o 1 é o seu próprio dinheiro · taxa = o que passa de 1 → 26,8%")]


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


ALTS3 = [("A", "9,00%", "taxa do semestre: só uma etapa", RED), ("B", "18,00%", "nominal tomada pela efetiva", RED),
         ("C", "18,81%", "", GREEN), ("D", "19,56%", "capitalizou por mês (1,015¹²)", RED),
         ("E", "118,81%", "fator sem tirar o 1", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "NOMINAL × EFETIVA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, "Um contrato de empréstimo informa uma taxa de 18% ao ano, com capitalização semestral. A taxa "
                      "efetiva anual desse contrato é de", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["23"], 0.3)), align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 42, C["23.ok"], "C", cues_in, cues_x, gap=40)
    if t < C["23"]:
        pause_timer(c, t, C["22.end"] - 1.9, 540, 620)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["23"], 0.4), shadow=True)
    pill(c, "“capitalização” → 18% é NOMINAL", 540, y0 + 44, BLUE, size=24, a=ep(t, C["23.a"], 0.4), anchor="center")
    linha(c, [("18% ÷ 2 = ", INK), ("9% ao semestre", PURPLE)], 540, y0 + 110, 32, ep(t, C["23.b"], 0.4))
    K.mdraw(c, "1,09^{2} = 1,1881", 540, y0 + 175, 36, INK, ep(t, C["23.c"], 0.4), align="center")
    linha(c, [("→ ", INK2), ("18,81% ao ano", GREEN)], 540, y0 + 235, 34, ep(t, C["23.c"] + 4.5, 0.4))
    ad = ep(t, C["23.d"], 0.4)
    if ad > 0:
        rrect(c, 200, y0 + 275, 680, 64, 14, mix("#FFFFFF", GREEN, 0.14), ad)
        text_mid(c, "atalho: 18% + 9%² = 18% + 0,81%", 540, y0 + 307, 28, "black", GREEN, ad)


ALTSN = [("A", "as duas, 36% a.a.", "nominal tomada pela efetiva", RED),
         ("B", "X, ≈ 39,2% a.a.", "X está certa, mas é a menor", RED),
         ("C", "Y, 36% a.a.", "esqueceu de capitalizar", RED),
         ("D", "Y, ≈ 42,6% a.a.", "", GREEN),
         ("E", "Y, ≈ 142,6% a.a.", "fator sem tirar o 1", RED)]


def b_qnova(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "QUAL FINANCEIRA CUSTA MAIS?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, "Duas financeiras anunciam empréstimos com taxa de 36% ao ano. A financeira X capitaliza os "
                      "juros semestralmente; a financeira Y, mensalmente. Considere 1,03¹² ≈ 1,426. Qual delas tem o "
                      "maior custo efetivo anual, e qual é esse custo?", a0, size=26)
    text(c, "Questão inédita", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)), align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTSN, 1000, 250, 680, 36, C["26.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 2.4, 540, 700, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["26"], 0.4), shadow=True)
    aa = ep(t, C["26.a"], 0.4)
    linha(c, [("X: 18% ao sem. → ", INK2), ("39,24%", PURPLE)], 540, y0 + 55, 32, aa)
    K.mdraw(c, "1,18^{2} = 1,3924", 540, y0 + 105, 28, GRAY, aa, align="center")
    ab = ep(t, C["26.b"], 0.4)
    linha(c, [("Y: 3% ao mês → ", INK2), ("≈ 42,6%", GREEN)], 540, y0 + 165, 32, ab)
    K.mdraw(c, "1,03^{12} ≈ 1,426", 540, y0 + 215, 28, GRAY, ab, align="center")
    if y0 + 270 < 830:
        conferido(c, "mais frequente, maior", 380, y0 + 268, ep(t, C["26.c"], 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "INFLAÇÃO", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        caixa(c, 620, 380, "PREÇOS", "+ 25%", RED, aa, 440)
        caixa(c, 1300, 380, "SALÁRIO", "parado", BLUE, aa, 440)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        text_mid(c, "perde 25% do poder de compra?", W / 2, 580, 54, "black", AMBER, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 720, acc, "NÃO · PRÓXIMO EPISÓDIO", PURPLE, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "O seu cartão mostra a taxa ao mês ou ao ano?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, nominal=b_nominal,
              capitaliza=b_capitaliza, tabela=b_tabela, acumulada=b_acumulada, media=b_media, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, qnova=b_qnova, ponte=b_ponte, cta=b_cta)
