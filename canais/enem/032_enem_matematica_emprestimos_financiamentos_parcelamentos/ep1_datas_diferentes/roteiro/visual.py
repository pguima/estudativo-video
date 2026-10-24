"""Visual — Empréstimos, Financiamentos e Parcelamentos, Episódio 1: dinheiro em datas diferentes (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho...).
Peças deste episódio: cambio() (a animação principal: linha do tempo com as parcelas como moedinhas em cada data; cada
moedinha desce para a sua faixa e "viaja" até a data zero passando por um GUICHÊ DE CÂMBIO que a divide por 1,1, 1,21 ou
1,331 — só lá elas se juntam numa pilha), moeda(), maquina() (o saldo não pago entra e sai × 1,12), carne(), linha().
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
_s = importlib.util.spec_from_file_location("comum032", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_emprestimos_ep1_datas_diferentes.mp4"
CARD_R = K.CARD_R
OURO = "#F4C542"


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


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None, h=140):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    fmid(c, val, cx, cy + 22, 40 if ftext_w(val, "black", 40) < w - 30 else 32, "black", INK, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


def moeda(c, x, y, r, s, col, a, rs="R$"):
    """moedinha dourada com o valor; o anel mostra a data (roxo = futuro, azul = hoje)"""
    if a <= 0:
        return
    c.drawCircle(x, y + 5, r, paint("#000000", a * 0.10))
    c.drawCircle(x, y, r, paint(OURO, a))
    c.drawCircle(x, y, r - 7, paint(mix(OURO, "#FFFFFF", 0.45), a))
    c.drawCircle(x, y, r, paint(col, a, stroke=6))
    if rs:
        text(c, rs, x, y - r * 0.22, r * 0.36, "black", INK2, a)
    sz = r * 0.52 if len(s) <= 5 else r * 0.44
    text(c, s, x, y + r * 0.42, sz, "black", INK, a)


def guiche(c, x, y, fator, a, ativo=0.0):
    """guichê de câmbio: casinha com o letreiro "÷ fator" """
    if a <= 0:
        return
    col = mix(PURPLE, GREEN, ativo)
    rrect(c, x - 70, y - 62, 140, 124, 14, mix("#FFFFFF", col, 0.10), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 70, y - 62, 140, 124), 14, 14), paint(col, a, stroke=4))
    rrect(c, x - 82, y - 86, 164, 34, 10, col, a)
    text(c, "CÂMBIO", x, y - 61, 20, "black", "#FFFFFF", a, tracking=2)
    text(c, "÷ " + fator, x, y + 14, 30, "black", col, a)


def trilha(c, x0, y, n, passo, a, rot=("hoje", "1 mês", "2 meses", "3 meses"), destaque_zero=True):
    """linha do tempo: traço deitado com as datas 0, 1, 2, 3"""
    if a <= 0:
        return
    line(c, x0 - 70, y, x0 + passo * n + 70, y, INK2, a, 5)
    for k in range(n + 1):
        x = x0 + k * passo
        c.drawCircle(x, y, 12, paint(BLUE if (k == 0 and destaque_zero) else INK2, a))
        text(c, str(k), x, y - 26, 30, "black", BLUE if k == 0 else INK2, a)
        text(c, rot[k], x, y + 44, 22, "bold", BLUE if k == 0 else GRAY, a)


def cambio(c, t, a, parcelas, us, y=300, x0=360, passo=380, lane0=430, dl=120, r=48, n=None, gx=None):
    """parcelas = [(data, valor_futuro, fator, valor_hoje)]; us = progresso da viagem de cada uma (0 = parada na data,
    1 = chegou à data zero). Cada moedinha desce para a sua faixa e passa pelo guichê do SEU prazo."""
    if a <= 0:
        return
    n = n or max(p[0] for p in parcelas)
    trilha(c, x0, y, n, passo, a)
    for j, ((k, fut, fat, hoje), u) in enumerate(zip(parcelas, us)):
        yl = lane0 + j * dl
        xk = x0 + k * passo
        g = gx[j] if gx else (x0 + xk) / 2 + 30
        line(c, xk, y + 70, xk, yl - r - 6, LIGHT, a * (1 - clamp(u * 3)), 3, dash=[8, 8])
        line(c, x0 + r + 10, yl, xk - r, yl, LINE, a * 0.9, 4, dash=[10, 10])
        uu = ease_io(clamp(u))
        x = xk + (x0 - xk) * uu
        passou = x < g
        guiche(c, g, yl, fat, a, 1.0 if passou else 0.0)
        moeda(c, x, yl, r, hoje if passou else fut, BLUE if passou else PURPLE, a)


def carne(c, x, y, a, w=420):
    """carnê com três boletos e datas"""
    if a <= 0:
        return
    for k in range(3):
        yy = y + k * 70
        rrect(c, x, yy, w, 60, 10, "#FFFFFF", a, shadow=k == 0)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, yy, w, 60), 10, 10), paint(LIGHT, a, stroke=2))
        line(c, x + 90, yy + 6, x + 90, yy + 54, LIGHT, a, 2, dash=[5, 5])
        text(c, f"{k + 1}/3", x + 45, yy + 40, 24, "black", PURPLE, a)
        text(c, f"vence em {['10/11', '10/12', '10/01'][k]}", x + 110, yy + 40, 24, "bold", INK2, a, align="left")
        text(c, "R$ 1.331", x + w - 20, yy + 40, 24, "black", INK, a, align="right")


def maquina(c, x, y, a, fator="× 1,12", ativo=0.0):
    """máquina do rotativo: o saldo entra de um lado e sai multiplicado"""
    if a <= 0:
        return
    rrect(c, x - 120, y - 90, 240, 180, 24, mix("#FFFFFF", RED, 0.10 + 0.10 * ativo), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 120, y - 90, 240, 180), 24, 24), paint(RED, a, stroke=5))
    text(c, "ROTATIVO", x, y - 40, 24, "black", RED, a, tracking=2)
    text(c, fator, x, y + 30, 46, "black", RED, a)
    for k in range(3):
        c.drawCircle(x - 60 + k * 60, y + 66, 9, paint(RED if (ativo * 3 > k) else LIGHT, a))


# ======================================================================
# abertura
# ======================================================================

P_GANCHO = [(1, "1.210", "1,1", "1.100"), (2, "1.210", "1,21", "1.000")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EMPRÉSTIMOS E PARCELAMENTOS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 1040, 330, 700, 120, 22, "#FFFFFF", aa, shadow=True)
        linha(c, [("1.210 + 1.210 = ", INK), ("2.420", AMBER)], 1390, 390, 52, aa)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        pill(c, "na calculadora", 1390, 485, AMBER, size=26, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["01.c"], 0.5)
    us = [ep(t, C["01.c"] + 0.2, 1.6), ep(t, C["01.c"] + 0.8, 1.8)]
    cambio(c, t, aa, P_GANCHO, us, y=300, x0=300, passo=300, lane0=460, dl=175, n=2)
    if ac > 0 and us[1] > 0.95:
        rrect(c, 1040, 600, 700, 120, 22, mix("#FFFFFF", GREEN, 0.12), ac, shadow=True)
        linha(c, [("hoje: ", INK2), ("R$ 2.100,00", GREEN)], 1390, 660, 52, ep(t, C["01.c"] + 2.4, 0.4))
    ad = ep(t, C["01.d"], 0.4)
    if ad > 0:
        selo(c, 1390, 800, ad, "REAL + DÓLAR?", RED, -4, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CALCULAR", GREEN)
    itens = [("02.a", "QUANTO VALE HOJE", "uma sequência de parcelas", BLUE),
             ("02.b", "QUITAR ANTES", "quanto custa pagar a dívida hoje", PURPLE),
             ("02.c", "O ROTATIVO", "quanto cresce a fatura não paga", RED)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 520
        rrect(c, x, 290 + d, 440, 420, 26, "#FFFFFF", a, shadow=True)
        rrect(c, x, 290 + d, 440, 70, 26, col, a * 0.14)
        text(c, tit, x + 220, 338 + d, 32, "black", col, a)
        if k == 0:
            for j in range(3):
                moeda(c, x + 120 + j * 100, 480 + d, 42, "1.331", BLUE, a)
        elif k == 1:
            check_icon(c, x + 220, 480 + d, 60, a, PURPLE)
        else:
            maquina(c, x + 220, 485 + d, a * 0.999, "× 1,12")
        para(c, sub, x + 30, 640 + d, 28, "bold", INK2, a, 380, 36, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE RÁPIDO", "SÉRIE DE JUROS COMPOSTOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 270 + d1, 720, 460, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "PARA O FUTURO × · PARA HOJE ÷", 560, 320 + d1, PURPLE, size=24, a=a1, anchor="center",
             bounds=(0, 1920))
        K.mdraw(c, "M = C · (1+i)^{t}", 560, 450 + d1, 60, PURPLE, a1, align="center")
        K.mdraw(c, "C = M/(1+i)^{t}", 560, 610 + d1, 60, BLUE, ep(t, C["03.a"] + 3.0, 0.4), align="center")
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 270 + d2, 720, 460, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "AS DUAS POTÊNCIAS DA AULA", 1360, 320 + d2, GREEN, size=24, a=a2, anchor="center", bounds=(0, 1920))
        K.mdraw(c, "1,1^{2} = 1,21", 1360, 460 + d2, 66, INK, a2, align="center")
        K.mdraw(c, "1,1^{3} = 1,331", 1360, 610 + d2, 66, INK, ep(t, C["03.b"] + 2.5, 0.4), align="center")


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "TRÊS CENAS DO DIA A DIA", "A MESMA CONTA ESCONDIDA", BLUE),
                       ("05", "A LINHA DO TEMPO", "DATA ZERO = HOJE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        if aa > 0:
            text(c, "CARNÊ", 410, 270, 28, "black", PURPLE, aa)
            carne(c, 200, 300, aa)
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            rrect(c, 700, 280, 520, 230, 22, mix("#FFFFFF", GREEN, 0.10), ab, shadow=True)
            text(c, "AVISO DO BANCO", 960, 330, 24, "black", GREEN, ab, tracking=2)
            text(c, "Quite seu financiamento", 960, 400, 34, "black", INK, ab)
            text(c, "com DESCONTO!", 960, 455, 40, "black", GREEN, ab)
        ac = ep(t, C["04.c"], 0.5)
        if ac > 0:
            rrect(c, 1280, 270, 440, 300, 22, "#FFFFFF", ac, shadow=True)
            text(c, "FATURA DO CARTÃO", 1500, 320, 24, "black", INK2, ac, tracking=2)
            text(c, "R$ 2.000,00", 1500, 400, 48, "black", INK, ac)
            rrect(c, 1340, 450, 320, 80, 40, RED, ac)
            text_mid(c, "PAGAR O MÍNIMO", 1500, 490, 28, "black", "#FFFFFF", ac)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            regra(c, "três situações · a mesma conta escondida", W / 2, 720, ad, 40, PURPLE)
        return
    aa = ep(t, C["05.a"], 0.5)
    trilha(c, 400, 450, 3, 380, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        pill(c, "DATA ZERO = HOJE", 400, 330, BLUE, size=28, a=ab, anchor="center", bounds=(0, 1920))
        arrow(c, 400, 360, 400, 410, BLUE, ab, 4, 14)
    acc = ep(t, C["05.c"], 0.5)
    for k in range(1, 4):
        a, d = rise(t, C["05.c"] + 0.4 * k)
        moeda(c, 400 + k * 380, 330 + d, 48, "1.331", PURPLE, a)
    if acc > 0:
        regra(c, "cada parcela = uma moedinha na SUA data", W / 2, 680, acc, 40, BLUE)


# ======================================================================
# bloco a — mil hoje ≠ mil amanhã
# ======================================================================

def b_datas(c, t, C, B):
    head_seq(c, t, C, [("06", "MIL HOJE = MIL AMANHÃ?", "O DINHEIRO RENDE", BLUE),
                       ("07", "DOIS NOMES", "PRESENTE × FUTURO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            caixa(c, 520, 340, "HOJE", "R$ 1.000,00", BLUE, aa, 420)
            caixa(c, 1400, 340, "DAQUI A 1 MÊS", "R$ 1.100,00", PURPLE, ep(t, C["06.a"] + 2.0, 0.5), 420)
            arrow(c, 760, 340, 1160, 340, GREEN, ep(t, C["06.a"] + 1.4, 0.5), 6, 20)
            pill(c, "rende 10%", 960, 290, GREEN, size=28, a=ep(t, C["06.a"] + 1.4, 0.5), anchor="center",
                 bounds=(0, 1920))
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            moeda(c, 640, 600, 70, "hoje", BLUE, ab)
            moeda(c, 1280, 600, 70, "1 mês", PURPLE, ab, rs="US$")
            text_mid(c, "≠", 960, 600, 100, "black", RED, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            regra(c, "antes de somar: CÂMBIO para a mesma data", W / 2, 765, acc, 38, PURPLE)
        return
    defs = [("07.a", "VALOR PRESENTE", "quanto vale HOJE (data zero)", BLUE),
            ("07.b", "VALOR FUTURO", "quanto vale numa data depois", PURPLE),
            ("07.c", "FATOR", "o câmbio entre as datas: (1 + i) elevado aos meses", GREEN)]
    for k, (cue, nome, sig, col) in enumerate(defs):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 260 + k * 175 + d
        rrect(c, 260, y, 1400, 145, 22, mix("#FFFFFF", col, 0.07), a)
        text(c, nome, 300, y + 62, 40, "black", col, a, align="left")
        text(c, sig, 300, y + 114, 30, "bold", INK2, a, align="left")


# ======================================================================
# bloco b — levar e trazer
# ======================================================================

def b_levar(c, t, C, B):
    head_seq(c, t, C, [("08", "LEVAR E TRAZER", "× PARA O FUTURO · ÷ PARA HOJE", PURPLE),
                       ("09", "SEM CALCULADORA", "TIRE A VÍRGULA, DEVOLVA OS ZEROS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            arrow(c, 560, 260, 1360, 260, GREEN, aa, 6, 20)
            pill(c, "para o FUTURO: × fator", 960, 220, GREEN, size=28, a=aa, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            arrow(c, 1360, 330, 560, 330, PURPLE, ab, 6, 20)
            pill(c, "para o PRESENTE: ÷ fator", 960, 372, PURPLE, size=28, a=ab, anchor="center", bounds=(0, 1920))
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            cambio(c, t, acc, [(3, "2.662", "1,331", "2.000")], [ep(t, C["08.d"] + 1.0, 2.0)], y=490, x0=420,
                   passo=360, lane0=650, n=3)
        ad = ep(t, C["08.d"] + 4.0, 0.5)
        if ad > 0:
            rrect(c, 1180, 740, 560, 90, 18, mix("#FFFFFF", GREEN, 0.12), ad)
            linha(c, [("2.662 ÷ 1,331 = ", INK), ("R$ 2.000,00", GREEN)], 1460, 785, 38, ad)
        return
    rows = [("09.a", "÷ 1,1", "÷ 11", "+ 1 zero"), ("09.b", "÷ 1,21", "÷ 121", "+ 2 zeros"),
            ("09.c", "÷ 1,331", "÷ 1.331", "+ 3 zeros")]
    for k, (cue, f, s_, z) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 120 + d
        chip_ = lambda s, x, col: (rrect(c, x - 150, y - 45, 300, 90, 18, mix("#FFFFFF", col, 0.12), a),
                                  text_mid(c, s, x, y, 42, "black", col, a))
        chip_(f, 420, PURPLE)
        arrow(c, 590, y, 690, y, GREEN, a, 5, 16)
        chip_(s_, 860, INK2)
        arrow(c, 1030, y, 1130, y, GREEN, a, 5, 16)
        chip_(z, 1300, GREEN)
    ac = ep(t, C["09.c"] + 4.5, 0.5)
    if ac > 0:
        K.atalho(c, 380, 650, 1160, 150, "ATALHO",
                 ["2.662 ÷ 1.331 = 2   →   + 3 zeros   →   2.000"], ac, 38)


# ======================================================================
# bloco c — a sequência de parcelas
# ======================================================================

def b_sequencia(c, t, C, B):
    head_seq(c, t, C, [("10", "VÁRIAS PARCELAS", "CADA UMA PELO SEU PRAZO", PURPLE),
                       ("11", "AGORA PODE SOMAR", "A MESMA DATA", GREEN)])
    card(c, *CARD_R)
    u1 = ep(t, C["10.c"], 1.8)
    u2 = ep(t, C["10.d"], 2.2)
    cambio(c, t, ep(t, C["10.a"], 0.5), P_GANCHO, [u1, u2], y=290, x0=380, passo=440, lane0=450, dl=175, n=2)
    ab = ep(t, C["10.b"], 0.5) * (1 - ep(t, C["11"], 0.3))
    if ab > 0:
        regra(c, "cada moedinha viaja pelo SEU prazo", 1340, 770, ab, 34, PURPLE)
    if t < C["11"]:
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 1130, 400, 560, 140, 22, mix("#FFFFFF", GREEN, 0.12), aa, shadow=True)
        linha(c, [("1.100 + 1.000 = ", INK), ("2.100", GREEN)], 1410, 470, 48, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        pill(c, "valor justo À VISTA", 1410, 610, BLUE, size=28, a=ab, anchor="center", bounds=(0, 1920))
    ac = ep(t, C["11.c"], 0.5)
    if ac > 0:
        pill(c, "QUITAÇÃO ANTECIPADA: pagar hoje", 1410, 690, BLUE, size=28, a=ac, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco d — o rotativo
# ======================================================================

def b_rotativo(c, t, C, B):
    head_seq(c, t, C, [("12", "PAGAR O MÍNIMO?", "O ROTATIVO DO CARTÃO", RED),
                       ("13", "O ALUGUEL DO DINHEIRO", "JUROS SÓ SOBRE O SALDO", RED),
                       ("14", "TRÊS MESES SEM PAGAR", "JUROS SOBRE JUROS", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    if sid in ("12", "13"):
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            rrect(c, 220, 260, 460, 300, 22, "#FFFFFF", aa, shadow=True)
            text(c, "FATURA", 450, 310, 26, "black", INK2, aa, tracking=2)
            text(c, "R$ 2.000,00", 450, 390, 50, "black", INK, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            dx = 260 * ease_io(ep(t, C["12.b"] + 0.3, 1.0))
            rrect(c, 260 - dx * 0.2, 430 + dx, 380, 70, 16, mix("#FFFFFF", GREEN, 0.15), ab * (1 - clamp(dx / 200)))
            text_mid(c, "pagou R$ 500,00", 450 - dx * 0.2, 465 + dx, 30, "black", GREEN, ab * (1 - clamp(dx / 200)))
            caixa(c, 450, 690, "SALDO NÃO PAGO", "R$ 1.500,00", RED, ep(t, C["12.b"] + 1.6, 0.5), 400)
            pill(c, "= o ROTATIVO", 450, 800, RED, size=26, a=ep(t, C["12.b"] + 3.0, 0.5), anchor="center",
                 bounds=(0, 1920))
        acc = ep(t, C["12.c"], 0.5)
        ativo = ep(t, C["13.b"], 1.5) if sid == "13" else 0.0
        maquina(c, 1080, 420, acc, "× 1,12", ativo)
        if acc > 0 and sid == "12":
            pill(c, "12% ao mês · sobre QUANTO?", 1080, 580, AMBER, size=28, a=acc, anchor="center", bounds=(0, 1920))
        if sid == "13":
            aa = ep(t, C["13.a"], 0.5)
            if aa > 0:
                regra(c, "juros = aluguel: só do que AINDA está com você", 1150, 250, aa, 30, PURPLE)
            ab = ep(t, C["13.b"], 0.5)
            if ab > 0:
                arrow(c, 680, 690, 940, 470, RED, ab, 5, 18)
                arrow(c, 1210, 420, 1400, 420, RED, ep(t, C["13.b"] + 1.4, 0.4), 5, 18)
                caixa(c, 1560, 420, "PRÓXIMA FATURA", "R$ 1.680,00", RED, ep(t, C["13.b"] + 2.2, 0.5), 300)
                linha(c, [("1.500 × 1,12 = ", INK), ("1.680", RED)], 1180, 640, 40, ep(t, C["13.b"] + 2.2, 0.5))
            ac = ep(t, C["13.c"], 0.5)
            if ac > 0:
                selo(c, 1300, 760, ac, "NÃO sobre a fatura inteira", AMBER, -3, 30)
        return
    aa = ep(t, C["14.a"], 0.5)
    vals = ["1.500", "× 1,12", "× 1,12", "× 1,12"]
    for k, v in enumerate(vals):
        a = ep(t, C["14.a"] + 0.5 * k, 0.4)
        if a <= 0:
            continue
        x = 330 + k * 300
        if k == 0:
            caixa(c, x, 320, "SALDO", "R$ 1.500", RED, a, 240)
        else:
            arrow(c, x - 160, 320, x - 60, 320, RED, a, 5, 16)
            rrect(c, x - 60, 270, 200, 100, 18, mix("#FFFFFF", RED, 0.10), a)
            text_mid(c, v, x + 40, 300, 34, "black", RED, a)
            text(c, f"mês {k}", x + 40, 355, 22, "bold", GRAY, a)
    if aa > 0:
        linha(c, [("1,12³ ≈ 1,405", PURPLE)], 1560, 310, 40, ep(t, C["14.a"] + 2.5, 0.4))
        linha(c, [("1.500 × 1,405 ≈ ", INK), ("R$ 2.107,50", RED)], W / 2, 470, 48, ep(t, C["14.a"] + 4.0, 0.4))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 560, 560, 120, 20, mix("#FFFFFF", RED, 0.08), ab)
        text_mid(c, "12% + 12% + 12% = 36%", 580, 620, 34, "black", RED, ab)
        strike(c, 330, 620, 830, 620, ep(t, C["14.b"] + 1.5, 0.4), RED)
        rrect(c, 1000, 560, 600, 120, 20, mix("#FFFFFF", GREEN, 0.12), ep(t, C["14.b"] + 2.0, 0.4))
        text_mid(c, "juros sobre juros ≈ 40,5%", 1300, 620, 36, "black", GREEN, ep(t, C["14.b"] + 2.0, 0.4))
    ac = ep(t, C["14.c"], 0.5)
    if ac > 0:
        pill(c, "CHEQUE ESPECIAL: igual, sobre o saldo negativo", 700, 770, BLUE, size=26, a=ac, anchor="center",
             bounds=(0, 1920))
        pill(c, "taxa anual de 3 dígitos", 1440, 770, AMBER, size=26, a=ep(t, C["14.c"] + 3.5, 0.4),
             anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

P_NOS = [(1, "1.100", "1,1", "1.000"), (2, "1.210", "1,21", "1.000")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "CADA UMA PELO SEU PRAZO", GREEN)])
    card(c, *CARD_R)
    us = [ep(t, C["16.a"], 1.6), ep(t, C["16.b"], 1.8)] if t >= C["16"] else [0, 0]
    cambio(c, t, ep(t, C["15.a"], 0.5), P_NOS, us, y=290, x0=380, passo=440, lane0=450, dl=175, n=2)
    ap = ep(t, C["15.a"], 0.5)
    if ap > 0 and t < C["16"]:
        pill(c, "10% ao mês · quanto valem HOJE?", 960, 790, AMBER, size=28, a=ap, anchor="center", bounds=(0, 1920))
        pause_timer(c, t, C["15.end"] - 1.9, 1580, 440)
        return
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        rrect(c, 1170, 420, 520, 130, 22, mix("#FFFFFF", GREEN, 0.12), acc, shadow=True)
        linha(c, [("1.000 + 1.000 = ", INK), ("R$ 2.000", GREEN)], 1430, 485, 40, acc)
        conferido(c, "menor que 2.310", 1230, 640, ep(t, C["16.c"] + 3.0, 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Só se somam valores na mesma data.",
          "Para o futuro, multiplique pelo fator; para o presente, divida.",
          "Juros incidem sobre o que ainda se deve."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Somar parcelas de datas diferentes", "é exatamente o que a calculadora faz",
          "é somar real com dólar: duas de R$ 1.210 valem hoje R$ 2.100, não R$ 2.420"),
         ("Descontar todas pelo MESMO prazo", "uma conta só é mais rápida",
          "cada moedinha viaja pelo SEU prazo · as duas por 1 mês: R$ 2.100, não R$ 2.000"),
         ("Juros SIMPLES no rotativo", "10% + 10% = 20%",
          "juros sobre juros: 2 meses a 10% → × 1,21, não × 1,20")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


def _questao(c, t, C, sc, sol, xs, alts, okL, enun, fonte, pausa=True, size_en=28):
    """enunciado à esquerda (sai quando começa a resolução), alternativas à direita"""
    a0 = ep(t, C[f"{sc}.a"], 0.4) * (1 - ep(t, C[sol], 0.4))
    _enunciado(c, enun, a0, size=size_en)
    text(c, fonte, 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"{sc}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{xs}.x{L.lower()}"] for L in "ABCDE" if L != okL}
    K.alternativas(c, t, C, alts, 1000, 250, 680, 40, C[f"{sol}.ok"], okL, cues_in, cues_x, gap=30)
    if pausa and t < C[sol]:
        pause_timer(c, t, C[f"{sc}.end"] - (2.4 if sc == "27" else 1.9), 1340, 790)


def _caixa_sol(c, t, C, sol):
    a = ep(t, C[sol], 0.4)
    if a > 0:
        rrect(c, 170, 230, 760, 600, 20, "#FFFFFF", a, shadow=True)
    return a


ALTS7 = [("A", "R$ 880,00", "só 1 mês de juros", RED), ("B", "R$ 960,00", "juros simples (20%)", RED),
         ("C", "R$ 968,00", "", GREEN), ("D", "R$ 1.168,00", "somou os 200 pagos", RED),
         ("E", "R$ 1.210,00", "juros na fatura inteira", RED)]


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("21", "QUESTÃO 7 · EU FAÇO", "ROTATIVO DO CARTÃO", BLUE),
                       ("23", "AS OUTRAS ALTERNATIVAS", "DE ONDE VEM CADA ERRO", RED)])
    card(c, *CARD_R)
    _questao(c, t, C, "21", "22", "23", ALTS7, "C",
             "A fatura de um cartão de crédito era de R$ 1.000,00, e o titular pagou apenas R$ 200,00. Sobre o saldo "
             "restante incidem juros compostos de 10% ao mês. Se o titular não fizer nenhum outro pagamento nem novas "
             "compras, sua dívida dois meses depois será de", "Questão do material de estudo (seção 12)", pausa=False)
    if t < C["22"]:
        return
    _caixa_sol(c, t, C, "22")
    a = ep(t, C["22.a"], 0.4)
    trilha(c, 300, 340, 2, 250, a)
    caixa(c, 300, 480, "AINDA DEVE", "R$ 800", RED, a, 220, h=120)
    linha(c, [("1.000 − 200 = ", INK2), ("800", RED)], 550, 600, 34, ep(t, C["22.a"] + 2.0, 0.4))
    linha(c, [("2 meses: ", INK2), ("× 1,21", PURPLE)], 550, 670, 34, ep(t, C["22.b"], 0.4))
    linha(c, [("800 × 1,21 = ", INK), ("R$ 968,00", GREEN)], 550, 750, 38, ep(t, C["22.c"], 0.4))
    ae = ep(t, C["23.xe"] + 1.5, 0.4)
    if ae > 0:
        selo(c, 650, 470, ae, "ALUGUEL DE DINHEIRO QUE JÁ VOLTOU", RED, -3, 22)


ALTS6 = [("A", "R$ 1.936,00", "tirou 20% do total", RED), ("B", "R$ 2.000,00", "as duas por 2 meses", RED),
         ("C", "R$ 2.100,00", "", GREEN), ("D", "R$ 2.178,00", "tirou 10% do total", RED),
         ("E", "R$ 2.420,00", "somou sem trazer", RED)]


def b_q6(c, t, C, B):
    head_seq(c, t, C, [("24", "QUESTÃO 6 · NÓS FAZEMOS", "VALOR À VISTA EQUIVALENTE", BLUE),
                       ("26", "AS ERRADAS", "DE ONDE VEM CADA UMA", RED)])
    card(c, *CARD_R)
    _questao(c, t, C, "24", "25", "26", ALTS6, "C",
             "Uma compra pode ser paga em duas parcelas de R$ 1.210,00, com vencimentos em 30 e em 60 dias, sem "
             "entrada. Se a taxa de juros é de 10% ao mês, no regime composto, o valor à vista equivalente a esse "
             "parcelamento é", "Questão do material de estudo (seção 12)")
    if t < C["25"]:
        return
    _caixa_sol(c, t, C, "25")
    pill(c, "À VISTA = VALOR PRESENTE", 550, 290, PURPLE, size=26, a=ep(t, C["25.a"], 0.4), anchor="center")
    linha(c, [("1.210 ÷ 1,1 = ", INK), ("1.100", BLUE)], 550, 400, 40, ep(t, C["25.b"], 0.4))
    linha(c, [("1.210 ÷ 1,21 = ", INK), ("1.000", BLUE)], 550, 490, 40, ep(t, C["25.b"] + 3.2, 0.4))
    linha(c, [("1.100 + 1.000 = ", INK), ("R$ 2.100,00", GREEN)], 550, 600, 40, ep(t, C["25.c"], 0.4))
    conferido(c, "menor que R$ 2.420", 370, 700, ep(t, C["25.c"] + 2.0, 0.4), True, 30)
    ad = ep(t, C["26.d"], 0.4)
    if ad > 0:
        regra(c, "taxa NÃO é desconto: divida pelo fator", 550, 780, ad, 28, PURPLE)


ALTSN = [("A", "R$ 3.000,00", "as 3 por 3 meses", RED), ("B", "R$ 3.310,00", "", GREEN),
         ("C", "R$ 3.593,70", "tirou 10% de cada", RED), ("D", "R$ 3.630,00", "as 3 por 1 mês", RED),
         ("E", "R$ 3.993,00", "somou sem trazer", RED)]


def b_qn(c, t, C, B):
    head_seq(c, t, C, [("27", "QUESTÃO NOVA · VOCÊ FAZ", "QUITAÇÃO ANTECIPADA", BLUE),
                       ("28", "CONFIRA", "TRÊS PRAZOS, TRÊS CÂMBIOS", GREEN),
                       ("29", "AS ARMADILHAS", "DE ONDE VEM CADA ERRO", RED)])
    card(c, *CARD_R)
    _questao(c, t, C, "27", "28", "29", ALTSN, "B",
             "Um cliente deve as três últimas parcelas de um financiamento, de R$ 1.331,00 cada, com vencimentos daqui "
             "a 1, 2 e 3 meses. O contrato permite quitar a dívida hoje, trazendo cada parcela ao presente pela taxa "
             "do financiamento, 10% ao mês, no regime composto. Considere 1,1² = 1,21 e 1,1³ = 1,331. Para quitar a "
             "dívida hoje, o cliente deve pagar", "Questão inédita no estilo ENEM", size_en=25)
    if t < C["28"]:
        return
    _caixa_sol(c, t, C, "28")
    rows = [("1.331 ÷ 1,1 = ", "1.210", 0.0), ("1.331 ÷ 1,21 = ", "1.100", 3.0), ("1.331 ÷ 1,331 = ", "1.000", 6.0)]
    for k, (e, v, dt) in enumerate(rows):
        a = ep(t, C["28.b"] + dt, 0.4)
        if a <= 0:
            continue
        y = 380 + k * 95
        moeda(c, 260, y, 36, f"{k + 1} m", PURPLE, a, rs="")
        linha(c, [(e, INK), (v, BLUE)], 600, y, 38, a)
    pill(c, "3 moedinhas · 3 prazos · 3 câmbios", 550, 280, PURPLE, size=24, a=ep(t, C["28.a"], 0.4),
         anchor="center")
    linha(c, [("soma: ", INK2), ("R$ 3.310,00", GREEN)], 550, 690, 44, ep(t, C["28.c"], 0.4))
    conferido(c, "menor que R$ 3.993", 360, 780, ep(t, C["28.c"] + 2.5, 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ENTRADA + UMA PARCELA", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        caixa(c, 560, 360, "À VISTA", "R$ 1.900,00", BLUE, aa, 460)
        caixa(c, 1360, 360, "PARCELADO", "2 × R$ 1.000,00", PURPLE, aa, 460, sub="a 1ª no ato")
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        linha(c, [("R$ 100 a mais = ", INK), ("5% de juros?", AMBER)], W / 2, 590, 50, ab)
    acc = ep(t, C["31.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 730, acc, "MAIS QUE O DOBRO DISSO", RED, -4, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já pagou só o mínimo da fatura?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, datas=b_datas, levar=b_levar,
              sequencia=b_sequencia, rotativo=b_rotativo, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q7=b_q7, q6=b_q6, qn=b_qn, ponte=b_ponte, cta=b_cta)
