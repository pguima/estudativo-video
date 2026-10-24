"""Visual — Empréstimos, Financiamentos e Parcelamentos, Episódio 3: o Sistema de Amortização Constante (SAC) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: divida() (a barra da dívida fatiada em fatias iguais, com a faixa laranja dos juros ao lado),
boleto() (o boleto com a parte azul da amortização e a parte laranja dos juros), tabela() (a tabela do SAC preenchida
célula por célula), escadinha() (os juros descendo sempre o mesmo degrau), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Laranja = juros (o aluguel do dinheiro); azul-claro = fatia de amortização.
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
ARQUIVO_FINAL = "enem_matematica_financiamentos_ep3_sac.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
LARANJA = "#F0892A"      # juros: o aluguel do dinheiro
FATIA = "#5B8DEF"        # fatia de amortização
FATIA_CL = "#DCE7FD"


def rs(v, cent=False):
    """dinheiro no formato brasileiro: 10000 -> '10.000' (cent=True -> '10.000,00')"""
    s = f"{v:,.2f}" if cent else f"{v:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


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


def divida(c, x, y, w, h, a, n=5, sairam=0.0, taxa=0.04, total=10000, juros=True, rot=True, jmax=None, saldo_lbl=False):
    """barra da dívida (total) fatiada em n fatias iguais. sairam = fatias já pagas (contínuo: a fatia saindo sobe e
    some). À direita, a faixa laranja dos juros: taxa × saldo que sobrou (largura proporcional)."""
    if a <= 0:
        return
    fw = w / n
    k = int(sairam)
    u = sairam - k
    for i in range(n):
        xi = x + i * fw
        if i < k:
            rrect(c, xi + 4, y, fw - 8, h, 10, "#F1F1EE", a)
            continue
        dy, al = 0, 1.0
        if i == k and u > 0:
            dy, al = -h * 1.2 * ease_io(u), 1 - ease_io(u)
        rrect(c, xi + 4, y + dy, fw - 8, h, 10, FATIA, a * al, shadow=True)
        if rot:
            text_mid(c, rs(total / n), xi + fw / 2, y + dy + h / 2, min(34, h * 0.36), "black", "#FFFFFF", a * al)
    saldo = total - total / n * sairam
    if saldo_lbl and not juros:
        text(c, f"saldo: R$ {rs(round(saldo))}", x + w / 2, y + h + 44, 30, "black", INK2, a)
    if juros:
        j = taxa * saldo
        jm = jmax or taxa * total
        jw = 230 * j / jm if jm else 0
        jx = x + w + 30
        if jw > 1:
            rrect(c, jx, y + h * 0.15, jw, h * 0.7, 10, LARANJA, a)
        text(c, f"juros: R$ {rs(round(j))}", jx, y + h + 44, 28, "black", LARANJA, a, align="left")
        text(c, f"saldo: R$ {rs(round(saldo))}", x + w / 2, y + h + 44, 28, "black", INK2, a)


def boleto(c, x, y, w, h, amort, juros, a, rot=True, escala=None, titulo=None):
    """boleto: a parcela = parte azul (amortização) + parte laranja (juros), empilhadas na horizontal"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    if titulo:
        text(c, titulo, x + w / 2, y + 40, 24, "black", GRAY, a)
    tot = amort + juros
    esc = escala or tot
    bw = (w - 60) * tot / esc
    ba = bw * amort / tot
    by, bh = y + h - 110, 70
    rrect(c, x + 30, by, ba, bh, 10, FATIA, a)
    rrect(c, x + 30 + ba + 4, by, bw - ba - 4, bh, 10, LARANJA, a)
    if rot:
        text_mid(c, rs(amort), x + 30 + ba / 2, by + bh / 2, 30, "black", "#FFFFFF", a)
        if bw - ba > 70:
            text_mid(c, rs(juros), x + 30 + ba + (bw - ba) / 2, by + bh / 2, 26, "black", "#FFFFFF", a)
    text(c, f"R$ {rs(tot, True)}", x + w / 2, y + (78 if titulo else 64), 42, "black", INK, a)


TAB_COLS = [("MÊS", 110), ("SALDO NO INÍCIO", 300), ("JUROS (4%)", 260), ("AMORTIZAÇÃO", 280), ("PARCELA", 260)]
TAB_COR = [GRAY, INK, LARANJA, BLUE, PURPLE]
SAC5 = [(k, 10000 - (k - 1) * 2000, 0.04 * (10000 - (k - 1) * 2000), 2000, 2000 + 0.04 * (10000 - (k - 1) * 2000))
        for k in range(1, 6)]


def tabela(c, x, y, a, celulas, rh=70, total=0.0, foco=None):
    """tabela do SAC (seção 06). celulas[r][col] = alfa de cada célula (0..1); total = alfa da linha de totais;
    foco = índice da coluna em destaque (fundo suave)."""
    if a <= 0:
        return
    tw = sum(w_ for _, w_ in TAB_COLS)
    rrect(c, x - 16, y - 16, tw + 32, rh * 7 + 40, 20, "#FFFFFF", a, shadow=True)
    cx = x
    for j, (tit, w_) in enumerate(TAB_COLS):
        if foco == j:
            rrect(c, cx + 4, y - 6, w_ - 8, rh * 7 + 12, 12, mix("#FFFFFF", TAB_COR[j], 0.12), a)
        text_mid(c, tit, cx + w_ / 2, y + rh / 2, 22, "black", TAB_COR[j] if j else GRAY, a)
        cx += w_
    line(c, x, y + rh, x + tw, y + rh, "#DADAD4", a, 3)
    for r, row in enumerate(SAC5):
        cx = x
        yy = y + rh * (r + 1) + rh / 2
        for j, (tit, w_) in enumerate(TAB_COLS):
            al = celulas[r][j] if r < len(celulas) else 0
            if al > 0:
                v = row[j]
                s = str(v) if j == 0 else rs(v, True)
                text_mid(c, s, cx + w_ / 2, yy, 32, "black", TAB_COR[j] if j else INK2, a * al)
            cx += w_
    if total > 0:
        yy = y + rh * 6 + rh / 2
        line(c, x, y + rh * 6, x + tw, y + rh * 6, "#DADAD4", a * total, 3)
        xs = [x]
        for _, w_ in TAB_COLS:
            xs.append(xs[-1] + w_)
        text_mid(c, "TOTAL", xs[0] + TAB_COLS[0][1] / 2 + 40, yy, 26, "black", INK, a * total)
        text_mid(c, rs(1200, True), xs[2] + TAB_COLS[2][1] / 2, yy, 34, "black", LARANJA, a * total)
        text_mid(c, rs(10000, True), xs[3] + TAB_COLS[3][1] / 2, yy, 34, "black", BLUE, a * total)
        text_mid(c, rs(11200, True), xs[4] + TAB_COLS[4][1] / 2, yy, 34, "black", PURPLE, a * total)


def escadinha(c, x0, y0, vals, a, passo_x=230, passo_y=62, col=None, degrau_lbl="− 80", lbl_a=1.0, size=40, alfas=None):
    """valores descendo uma escada (cada degrau desce passo_y); rótulo do degrau entre eles"""
    if a <= 0:
        return
    col = col or LARANJA
    for i, v in enumerate(vals):
        ai = a * (alfas[i] if alfas else 1)
        if ai <= 0:
            continue
        x, y = x0 + i * passo_x, y0 + i * passo_y
        rrect(c, x, y, passo_x - 16, 84, 14, mix("#FFFFFF", col, 0.16), ai)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, passo_x - 16, 84), 14, 14), paint(col, ai, stroke=3))
        text_mid(c, v, x + (passo_x - 16) / 2, y + 42, size, "black", col, ai)
        if i > 0 and degrau_lbl:
            text(c, degrau_lbl, x - 42, y + 62, 24, "black", RED, ai * lbl_a, align="center")


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EMPRÉSTIMOS E FINANCIAMENTOS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    boleto(c, 200, 230, 640, 300, 2000, 400, aa, rot=False, titulo="VOCÊ PAGOU")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        text(c, "A DÍVIDA", 1340, 260, 26, "black", GRAY, ab)
        g = ep(t, C["01.b"] + 0.6, 1.2)
        divida(c, 1000, 300, 680, 110, ab, 5, g, juros=False)
        linha(c, [("R$ 10.000 → ", INK2), ("R$ 8.000", BLUE)], 1340, 480, 38, ep(t, C["01.b"] + 1.6, 0.4))
        pill(c, "caiu só R$ 2.000", 1340, 550, BLUE, size=28, a=ep(t, C["01.b"] + 2.0, 0.4), anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 580, 580, 110, 20, mix("#FFFFFF", LARANJA, 0.14), acc)
        linha(c, [("e os outros ", INK), ("R$ 400", LARANJA), ("?", INK)], 520, 635, 46, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1340, 700, ad, "O ALUGUEL DO DINHEIRO", LARANJA, -3, 38)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "montar a tabela do SAC", "saldo → juros → amortização → parcela"),
            ("02.b", "calcular qualquer parcela sem montar todas", "direto na parcela que a questão pede"),
            ("02.c", "somar os juros do contrato inteiro de uma vez", "primeiro + último, sem somar um por um")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 30, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "PORCENTAGEM DE UM VALOR", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        linha(c, [("4%", PURPLE), ("  de  ", INK), ("R$ 10.000", INK)], W / 2, 280, 72, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        linha(c, [("por cento = ", INK), ("por CEM", BLUE), ("  →  4 em cada 100", INK2)], W / 2, 420, 44, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 520, 1200, 230, "ATALHO", ["10.000  →  tire 2 zeros  →  100",
                                                  "100 × 4  =  400"], acc, 40)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "O EXTRATO DO FINANCIAMENTO", "UM APARTAMENTO", BLUE)
    card(c, *CARD_R)
    vals = [("04.a", 2400, "1º BOLETO"), ("04.b", 2320, "2º BOLETO"), ("04.c", 2240, "3º BOLETO")]
    for k, (cue, v, tit) in enumerate(vals):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 230 + k * 500
        rrect(c, x, 250, 440, 300, 20, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250, 440, 60, 20, mix("#FFFFFF", BLUE, 0.14), a)
        text(c, tit, x + 220, 290, 26, "black", BLUE, a)
        text(c, f"R$ {rs(v, True)}", x + 220, 420, 50, "black", INK, a)
        for kk in range(4):
            line(c, x + 50, 470 + kk * 14, x + 390 - kk * 60, 470 + kk * 14, "#D8D8D2", a, 4)
        if k > 0:
            pill(c, "mais barato", x + 220, 590, GREEN, size=26, a=ep(t, C[cue] + 0.6, 0.4), anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pergunta(c, "por que a minha parcela DIMINUI?", W / 2, 720, ad, BLUE, 44)


# ======================================================================
# vocabulário e as três relações
# ======================================================================

def b_vocab(c, t, C, B):
    head_seq(c, t, C, [("05", "PALAVRA 1", "SALDO DEVEDOR", BLUE), ("06", "PALAVRA 2", "JUROS DA PARCELA", BLUE),
                       ("07", "PALAVRAS 3 E 4", "AMORTIZAÇÃO E PARCELA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06", "07"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 230, 1320, 130, BLUE, aa, 0.08)
            linha(c, [("SALDO DEVEDOR", BLUE), (" = quanto você ainda deve agora", INK)], W / 2, 295, 44, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            g = ep(t, C["05.b"] + 1.0, 3.0)
            divida(c, 420, 470, 900, 130, ab, 5, 5 * g, juros=False, saldo_lbl=True)
            text(c, "começa na dívida inteira", 420, 440, 26, "bold", GRAY, ab * (1 - g), align="left")
            if g > 0.98:
                text(c, "zero!", 870, 560, 56, "black", GREEN, ep(t, C["05.b"] + 4.0, 0.4))
        return
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 230, 1320, 130, BLUE, aa, 0.08)
            linha(c, [("JUROS", LARANJA), (" = o aluguel do dinheiro daquele mês", INK)], W / 2, 295, 44, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            linha(c, [("só se paga aluguel do que ", INK), ("AINDA DEVE", LARANJA)], W / 2, 450, 46, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            regra(c, "juros  =  taxa  ×  saldo do INÍCIO do mês", W / 2, 620, acc, 46)
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 230, 1320, 130, BLUE, aa, 0.08)
        linha(c, [("AMORTIZAÇÃO", BLUE), (" = a parte que ABATE a dívida", INK)], W / 2, 295, 44, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        boleto(c, 560, 420, 800, 260, 2000, 400, ab, titulo="PARCELA (PRESTAÇÃO)")
        pill(c, "amortização", 690, 720, FATIA, size=26, a=ab, anchor="center")
        pill(c, "juros", 1250, 720, LARANJA, size=26, a=ab, anchor="center")
        regra(c, "parcela = amortização + juros", W / 2, 800, ep(t, C["07.b"] + 2.4, 0.4), 34)


REL = ["juros = taxa × saldo anterior", "parcela = amortização + juros", "novo saldo = saldo anterior − amortização"]


def b_relacoes(c, t, C, B):
    head_seq(c, t, C, [("08", "AS TRÊS RELAÇÕES", "VALEM EM QUALQUER SISTEMA", PURPLE),
                       ("09", "REPARE NA TERCEIRA", "O SALDO CAI PELA AMORTIZAÇÃO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        text(c, "em QUALQUER financiamento", W / 2, 260, 34, "black", PURPLE, aa)
        for k, cue in enumerate(("08.b", "08.c", "08.d")):
            a, d = rise(t, C[cue])
            y = 380 + k * 140 + d
            badge_num(c, k + 1, 380, y - 14, a, 32, bg=PURPLE)
            boxed(c, 440, y - 62, 1100, 100, PURPLE, a, 0.06, 18, 3)
            text_mid(c, REL[k], 990, y - 12, 44, "black", INK, a)
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        regra(c, "novo saldo = saldo anterior − AMORTIZAÇÃO", W / 2, 250, aa, 38)
    ab = ep(t, C["09.b"], 0.5)
    boleto(c, 230, 360, 700, 280, 2000, 400, ab, titulo="A PARCELA DO GANCHO")
    if ab > 0:
        pill(c, "2.000 de amortização", 380, 690, FATIA, size=24, a=ep(t, C["09.b"] + 1.2, 0.4), anchor="center")
        pill(c, "400 de juros", 800, 690, LARANJA, size=24, a=ep(t, C["09.b"] + 2.0, 0.4), anchor="center")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        text(c, "os 400 pagaram o ALUGUEL", 1330, 380, 32, "black", LARANJA, acc)
        g = ep(t, C["09.c"] + 1.2, 1.2)
        divida(c, 1040, 450, 580, 100, acc, 5, g, juros=False)
        linha(c, [("só os ", INK), ("2.000", BLUE), (" derrubaram a dívida", INK)], 1330, 640, 34,
              ep(t, C["09.c"] + 2.0, 0.4))
        linha(c, [("10.000 → ", INK2), ("8.000", BLUE)], 1330, 710, 40, ep(t, C["09.c"] + 2.4, 0.4))


# ======================================================================
# blocos b, c — o SAC e a tabela
# ======================================================================

def b_sac(c, t, C, B):
    head_seq(c, t, C, [("10", "O SISTEMA DE HOJE", "SAC", BLUE), ("11", "EXEMPLO", "R$ 10.000 · 5 PARCELAS · 4% AO MÊS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 220, 1320, 130, BLUE, aa, 0.08)
            linha(c, [("SAC", BLUE), (" = Sistema de ", INK), ("Amortização Constante", BLUE)], W / 2, 285, 46, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            divida(c, 460, 420, 1000, 130, ab, 5, 0, juros=False, rot=False)
            text(c, "a dívida FATIADA EM FATIAS IGUAIS", W / 2, 610, 36, "black", BLUE, ep(t, C["10.b"] + 1.2, 0.4))
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            regra(c, "amortização = valor financiado ÷ nº de parcelas", W / 2, 740, acc, 38)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("R$ 10.000", INK), ("  ·  5 parcelas  ·  ", INK2), ("4% ao mês", LARANJA)], W / 2, 250, 48, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("10.000 ÷ 5 = ", INK), ("2.000 por fatia", BLUE)], W / 2, 350, 46, ab)
    g = 5 * ep(t, C["11.c"] + 0.3, 3.4)
    divida(c, 360, 450, 1000, 130, ep(t, C["11.b"], 0.5), 5, g, juros=False)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        text(c, f"mês {min(5, int(g) + (1 if g < 5 else 0))}", 1500, 525, 40, "black", PURPLE, acc)
        if g >= 4.98:
            selo(c, W / 2, 740, ep(t, C["11.c"] + 3.8, 0.4), "DÍVIDA PAGA", GREEN, -3, 34)


def _cels(t, plano):
    """plano = lista de linhas; cada linha = lista de instantes (um por coluna) ou None (célula apagada)"""
    out = []
    for row in plano:
        out.append([ep(t, x, 0.4) if x is not None else 0 for x in row])
    return out


TX, TY = 300, 210


def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("12", "A TABELA DO SAC", "SALDO → JUROS → AMORTIZAÇÃO → PARCELA", PURPLE),
                       ("13", "MÊS 2", "A MESMA ORDEM", PURPLE), ("14", "ATÉ O FIM", "OS TOTAIS", PURPLE),
                       ("15", "POR QUE A PARCELA DIMINUI?", "O JURO EMAGRECE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14", "15"])
    if sid == "15":
        _por_que(c, t, C)
        return
    r1 = [C["12.a"], C["12.a"], C["12.b"], C["12.c"], C["12.d"]]
    r2 = [C["13.a"], C["12.e"] + 1.0, C["13.a"] + 1.4, C["13.b"], C["13.b"] + 1.6]
    r3 = [C["14.a"]] * 3 + [C["14.a"] + 0.5] * 2
    r4 = [C["14.b"]] * 3 + [C["14.b"] + 0.5] * 2
    r5 = [C["14.c"]] * 3 + [C["14.c"] + 0.5] * 2
    plano = [r1, r2, r3, r4, r5]
    cel = _cels(t, plano)
    if t < C["13"]:
        cel[1] = [0, ep(t, C["12.e"], 0.4), 0, 0, 0]
    foco = 2 if t >= C["14.d"] else None
    tabela(c, TX, TY, ep(t, C["12"], 0.4), cel, 70, ep(t, C["14.d"] + 2.0, 0.5), foco)
    # anotação da linha do mês 1
    if sid == "12":
        notas = [("12.b", "4% de 10.000", 2), ("12.d", "2.000 + 400", 4)]
        for cue, s, col in notas:
            an = ep(t, C[cue] + 0.6, 0.4)
            xs = TX + sum(w_ for _, w_ in TAB_COLS[:col]) + TAB_COLS[col][1] / 2
            pill(c, s, xs, TY + 70 * 2 + 30, LARANJA if col == 2 else PURPLE, size=20, a=an, anchor="center")
        ae = ep(t, C["12.e"], 0.4)
        if ae > 0:
            x1 = TX + sum(w_ for _, w_ in TAB_COLS[:2]) - 20
            arrow(c, x1 + 30, TY + 70 * 1.5 + 22, x1 - 40, TY + 70 * 2.5 - 4, BLUE, ae, 5, 16)
            pill(c, "10.000 − 2.000 = 8.000", 1300, 760, BLUE, size=28, a=ae, anchor="center")
    if sid == "13":
        an = ep(t, C["13.a"] + 1.6, 0.4)
        pill(c, "4% de 8.000 = 320", 1300, 760, LARANJA, size=28, a=an * (1 - ep(t, C["13.c"], 0.3)), anchor="center")
        pill(c, "8.000 − 2.000 = 6.000", 1300, 760, BLUE, size=28, a=ep(t, C["13.c"], 0.3), anchor="center")
    if sid == "14":
        ad = ep(t, C["14.d"] + 3.0, 0.4)
        pill(c, "total pago = 10.000 + 1.200 = 11.200", 1300, 760 + 20, PURPLE, size=26, a=ad, anchor="center")


def _por_que(c, t, C):
    aa = ep(t, C["15.a"], 0.5)
    g = 4 * ep(t, C["15.b"] + 0.4, 3.0)
    divida(c, 320, 240, 900, 90, ep(t, C["15"], 0.5), 5, g, juros=True, jmax=400)
    if aa > 0:
        pill(c, "a FATIA é sempre a mesma: 2.000", 770, 205, BLUE, size=26, a=aa, anchor="center")
    # colunas das parcelas (azul fixo + laranja que emagrece)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        base_y = 800
        for k, (_, saldo, j, am, par) in enumerate(SAC5):
            ak = ep(t, C["15.c"] + 0.35 * k, 0.4)
            x = 360 + k * 260
            hb, hj = 2000 * 0.07, j * 0.35
            rrect(c, x, base_y - hb, 150, hb, 8, FATIA, ak)
            rrect(c, x, base_y - hb - hj - 4, 150, hj, 8, LARANJA, ak)
            text(c, rs(par), x + 75, base_y - hb - hj - 18, 26, "black", INK, ak)
            text(c, f"mês {k + 1}", x + 75, base_y + 34, 22, "bold", GRAY, ak)
        selo(c, 1560, 450, ep(t, C["15.c"] + 2.2, 0.4), "O JURO EMAGRECE JUNTO", LARANJA, -4, 26)


# ======================================================================
# bloco d — atalhos (escadinha, parcela k) · bloco e — soma dos juros
# ======================================================================

def b_escadinha(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A ESCADINHA DOS JUROS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["16"], 0.5)
    vals = ["400", "320", "240", "160", "80"]
    alf = [ep(t, C["16"] + 0.3 * i, 0.4) for i in range(5)]
    escadinha(c, 260, 210, vals, a0, 240, 50, LARANJA, "− 80", ep(t, C["16.a"], 0.4), 40, alf)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        boxed(c, 260, 520, 660, 140, BLUE, ab, 0.08)
        text(c, "PROGRESSÃO ARITMÉTICA (PA)", 590, 570, 28, "black", BLUE, ab)
        text(c, "lista que sobe ou desce sempre o mesmo valor", 590, 620, 24, "bold", INK2, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        K.atalho(c, 970, 510, 700, 160, "ATALHO", ["degrau = taxa × amortização", "4% × 2.000 = 80"], acc, 34)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        linha(c, [("parcelas: ", INK), ("2.400 → 2.320 → 2.240 → 2.160 → 2.080", PURPLE), ("   (− 80 também)", RED)],
              W / 2, 760, 32, ad)


def b_parcela_k(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUALQUER PARCELA, SEM A TABELA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 200, 1400, 150, "ATALHO", ["saldo da parcela k = financiado − (k − 1) × amortização"], aa, 38)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        text(c, "PARCELA 4: já saíram 3 fatias", 610, 410, 32, "black", PURPLE, ab)
        divida(c, 260, 450, 700, 110, ab, 5, 3 * ep(t, C["17.b"] + 0.6, 1.4), juros=False)
        linha(c, [("10.000 − 3 × 2.000 = ", INK), ("4.000", BLUE)], 610, 650, 40, ep(t, C["17.b"] + 2.2, 0.4))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        boxed(c, 1050, 420, 610, 290, PURPLE, acc, 0.06)
        linha(c, [("juros: 4% de 4.000 = ", INK), ("160", LARANJA)], 1355, 490, 34, acc)
        linha(c, [("parcela: 2.000 + 160 = ", INK), ("2.160", PURPLE)], 1355, 570, 34, ep(t, C["17.c"] + 1.4, 0.4))
        conferido(c, "bate com a tabela", 1150, 660, ep(t, C["17.c"] + 2.6, 0.4), True, 30)


def b_soma(c, t, C, B):
    head(c, t, B["start"], "SOMAR TODOS OS JUROS", "SEM SOMAR UM POR UM", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["18"], 0.5)
    vals = [400, 320, 240, 160, 80]
    xs = [420 + i * 270 for i in range(5)]
    y = 400
    for i, v in enumerate(vals):
        chip(c, str(v), xs[i], y, LARANJA, a0, 50, w=200)

    def arco(i, j, h, a, s):
        if a <= 0:
            return
        p = skia.Path(); p.moveTo(xs[i], y - 50); p.cubicTo(xs[i], y - 50 - h, xs[j], y - 50 - h, xs[j], y - 50)
        c.drawPath(p, paint(GREEN, a, stroke=5, cap_round=True))
        pill(c, s, (xs[i] + xs[j]) / 2, y - 50 - h * 0.75, GREEN, size=26, a=a, anchor="center")

    arco(0, 4, 150, ep(t, C["18.a"], 0.5), "400 + 80 = 480")
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        p = skia.Path(); p.moveTo(xs[1], y + 50); p.cubicTo(xs[1], y + 150, xs[3], y + 150, xs[3], y + 50)
        c.drawPath(p, paint(GREEN, ab, stroke=5, cap_round=True))
        pill(c, "320 + 160 = 480", xs[2], y + 135, GREEN, size=26, a=ab, anchor="center")
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        regra(c, "total = (primeiro + último) × quantidade ÷ 2", W / 2, 640, acc, 38)
        linha(c, [("(400 + 80) × 5 ÷ 2 = ", INK), ("1.200", LARANJA)], W / 2, 750, 46, ep(t, C["18.c"] + 3.0, 0.4))
    ad = ep(t, C["18.d"], 0.5)
    pill(c, "PA: série própria", 1650, 790, BLUE, size=22, a=ad, anchor="right")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "A PRIMEIRA E A ÚLTIMA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 110, 24, "#F7F7F5", aa)
        linha(c, [("R$ 12.000", INK), ("  ·  4 parcelas  ·  SAC  ·  ", INK2), ("5% ao mês", LARANJA)], W / 2, 265, 48, aa)
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0 and t < C["20"]:
        linha(c, [("1ª parcela = ?", PURPLE), ("        ", INK), ("última = ?", PURPLE)], W / 2, 410, 48, ab)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 600)
    if t < C["20"]:
        return
    a1 = ep(t, C["20.a"], 0.4)
    linha(c, [("fatia: 12.000 ÷ 4 = ", INK), ("3.000", BLUE)], W / 2, 390, 44, a1)
    for k, (cue, tit, saldo, j, par) in enumerate((("20.b", "1ª PARCELA", 12000, 600, 3600),
                                                     ("20.c", "ÚLTIMA (4ª)", 3000, 150, 3150))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 300 + k * 680
        boxed(c, x, 460, 620, 230, PURPLE, a, 0.06)
        text(c, tit, x + 310, 505, 28, "black", PURPLE, a)
        linha(c, [(f"saldo {rs(saldo)} → juros 5% = ", INK), (rs(j), LARANJA)], x + 310, 570, 30, a)
        linha(c, [("parcela: 3.000 + " + rs(j) + " = ", INK), (rs(par), PURPLE)], x + 310, 640, 34,
              ep(t, C[cue] + 1.6, 0.4))
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        linha(c, [("juros: (600 + 150) × 4 ÷ 2 = ", INK), ("1.500", LARANJA)], W / 2, 770, 40, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["No SAC, a amortização é fixa e os juros caem junto com o saldo.",
          "O saldo cai pela amortização, não pela parcela inteira.",
          "Juros do SAC somam como PA: primeiro mais último, vezes quantidade, dividido por 2."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 60)


ERROS = [("Abater a parcela inteira: 10.000 − 2.400 = 7.600", "você pagou 2.400 e a sensação é de que a dívida caiu isso",
          "os juros só pagam o aluguel: abata só a amortização → saldo 8.000"),
         ("Juros sobre o valor inicial todo mês: 400 × 5 = 2.000", "a taxa é a mesma todo mês: 4%",
          "a taxa incide sobre um saldo que CAI: os juros descem a escadinha → total 1.200")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23"], ERROS)


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


ALTS2 = [("A", "R$ 600,00", "só os juros", RED), ("B", "R$ 6.000,00", "só a amortização", RED),
         ("C", "R$ 6.060,00", "juros sobre a fatia", RED), ("D", "R$ 6.600,00", "", GREEN),
         ("E", "R$ 12.000,00", "juros dos 10 meses", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "A PRIMEIRA PARCELA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Um empresário financiou R$ 60.000,00 em 10 parcelas mensais pelo Sistema de Amortização "
                           "Constante (SAC), com juros de 1% ao mês sobre o saldo devedor. O valor da primeira parcela é", INK)],
                      a0, 240, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 42, C["25.ok"], "D", cues_in, cues_x, gap=34)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        pill(c, "1ª linha: saldo → juros → amortização → parcela", 540, y0 + 40, PURPLE, size=20, a=ep(t, C["25"], 0.4),
             anchor="center")
        linha(c, [("fatia: 60.000 ÷ 10 = ", INK), ("6.000", BLUE)], 540, y0 + 100, 30, ep(t, C["25.a"], 0.4))
        linha(c, [("juros: 1% de 60.000 = ", INK), ("600", LARANJA)], 540, y0 + 155, 30, ep(t, C["25.b"], 0.4))
        linha(c, [("parcela: 6.000 + 600 = ", INK), ("6.600", PURPLE)], 540, y0 + 210, 30, ep(t, C["25.c"], 0.4))
        conferido(c, "pouco mais que 1/10 da dívida", 230, y0 + 270, ep(t, C["25.d"], 0.4), True, 24)


ALTS3 = [("A", "R$ 3.000,00", "escadinha até zero", RED), ("B", "R$ 3.300,00", "", GREEN),
         ("C", "R$ 6.000,00", "juros constantes", RED), ("D", "R$ 6.600,00", "é a 1ª parcela", RED),
         ("E", "R$ 63.300,00", "é o total pago", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "O TOTAL DE JUROS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("No financiamento da questão anterior (R$ 60.000,00 em 10 parcelas pelo SAC, a 1% ao mês), "
                           "o total de juros pagos ao final do contrato é", INK)], a0, 240, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
         align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 42, C["28.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 140)
    if t >= C["28"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["28"], 0.4))
        linha(c, [("1º juro: ", INK), ("600", LARANJA)], 540, y0 + 50, 30, ep(t, C["28.a"], 0.4))
        linha(c, [("degrau: 1% de 6.000 = ", INK), ("60", RED)], 540, y0 + 105, 30, ep(t, C["28.b"], 0.4))
        linha(c, [("600, 540, 480 ... ", LARANJA), ("60", LARANJA)], 540, y0 + 160, 30, ep(t, C["28.b"] + 2.0, 0.4))
        ac = ep(t, C["28.c"], 0.4)
        pill(c, "o último NÃO é zero: 1% de 6.000 = 60", 540, y0 + 215, AMBER, size=20, a=ac, anchor="center")
        linha(c, [("(600 + 60) × 10 ÷ 2 = ", INK), ("3.300", GREEN)], 540, y0 + 275, 30, ep(t, C["28.d"], 0.4))
        conferido(c, "menos que 6.000", 230, y0 + 330, ep(t, C["29"], 0.4), True, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "SISTEMA PRICE", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        text(c, "e se todas as parcelas forem IGUAIS?", W / 2, 260, 40, "black", PURPLE, aa)
        for k in range(5):
            ak = ep(t, C["31.a"] + 0.3 * k, 0.4)
            x = 330 + k * 260
            rrect(c, x, 330, 220, 150, 16, "#FFFFFF", ak, shadow=True)
            text(c, "R$ ?", x + 110, 420, 44, "black", INK, ak)
            if k:
                text_mid(c, "=", x - 20, 405, 40, "black", GRAY, ak)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        chip(c, "SAC", 700, 610, BLUE, ab, 50)
        text_mid(c, "×", W / 2, 610, 60, "black", GRAY, ab)
        chip(c, "PARCELAS IGUAIS", 1230, 610, PURPLE, ab, 44)
        text(c, "quem paga MAIS juros no total?", W / 2, 720, 34, "black", AMBER, ep(t, C["31.b"] + 1.4, 0.4))
    pill(c, "ep. 4 · Sistema Price e SAC × Price", W / 2, 795, PURPLE, size=28, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você sabia que os juros não abatem a dívida?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, vocab=b_vocab, relacoes=b_relacoes,
              sac=b_sac, tabela=b_tabela, escadinha=b_escadinha, parcela_k=b_parcela_k, soma=b_soma, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q2=b_q2, q3=b_q3, ponte=b_ponte, cta=b_cta)
