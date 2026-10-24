"""Visual — Comparação de Propostas e Tomada de Decisão, Episódio 1: a regra de ouro, comparar na mesma data (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho...).
Peças deste episódio: sacos() (a animação principal: linha do tempo com três sacos de dinheiro — 10.000, 11.000, 12.100 —
em datas diferentes; uma bandeirinha DATA FOCAL é fincada e os sacos viajam até ela, crescendo ou encolhendo pelo fator,
até ficarem do mesmo tamanho), saco(), bandeira(), trilha(), parcelas() (as parcelas do televisor voltando para a data
da compra e encolhendo para 1.000, 980 e 961), etiqueta(), placar() (loja × aplicação), linha().
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
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_propostas_ep1_mesma_data.mp4"
CARD_R = K.CARD_R
OURO = "#F4C542"
SACO = "#C9A15A"


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


def saco(c, x, y, r, s, a, col=None):
    """saco de dinheiro: corpo redondo, gargalo amarrado e o valor no meio (y = centro do corpo)"""
    if a <= 0:
        return
    col = col or SACO
    c.drawCircle(x, y + 6, r, paint("#000000", a * 0.10))
    pth = skia.Path()
    pth.moveTo(x - r * 0.42, y - r * 0.80)
    pth.lineTo(x - r * 0.62, y - r * 1.22)
    pth.lineTo(x + r * 0.62, y - r * 1.22)
    pth.lineTo(x + r * 0.42, y - r * 0.80)
    pth.close()
    c.drawPath(pth, paint(mix(col, "#000000", 0.08), a))
    c.drawCircle(x, y, r, paint(col, a))
    c.drawCircle(x - r * 0.28, y - r * 0.30, r * 0.30, paint("#FFFFFF", a * 0.18))
    rrect(c, x - r * 0.46, y - r * 0.92, r * 0.92, r * 0.16, r * 0.08, mix(col, "#000000", 0.35), a)
    text(c, "R$", x, y - r * 0.18, r * 0.34, "black", "#FFFFFF", a * 0.9)
    sz = r * 0.40 if len(s) <= 5 else r * 0.34
    text(c, s, x, y + r * 0.38, sz, "black", "#FFFFFF", a)


def bandeira(c, x, y, a, col=None, s="DATA FOCAL", sobe=1.0, alt=150):
    """bandeirinha fincada na linha do tempo (y = linha); `sobe` anima a fincada"""
    if a <= 0:
        return
    col = col or GREEN
    h = alt * ease_io(clamp(sobe))
    line(c, x, y, x, y - h, INK2, a, 6)
    if h > 60:
        pth = skia.Path()
        pth.moveTo(x, y - h)
        pth.lineTo(x + 120, y - h + 30)
        pth.lineTo(x, y - h + 60)
        pth.close()
        c.drawPath(pth, paint(col, a))
        pill(c, s, x, y - h - 30, col, size=22, a=a, anchor="center", bounds=(0, 1920))


def trilha(c, x0, y, n, passo, a, rot=None, destaque=None):
    """linha do tempo: traço deitado com as datas"""
    if a <= 0:
        return
    rot = rot or [f"{k} ano" if k == 1 else (f"{k} anos" if k else "hoje") for k in range(n + 1)]
    line(c, x0 - 70, y, x0 + passo * n + 70, y, INK2, a, 5)
    for k in range(n + 1):
        x = x0 + k * passo
        col = GREEN if destaque == k else (BLUE if k == 0 else INK2)
        c.drawCircle(x, y, 12, paint(col, a))
        text(c, rot[k], x, y + 46, 24, "bold", col if destaque == k else GRAY, a)


def _r_saco(v, base):
    return base * math.sqrt(v / 12100)


def sacos(c, t, a, itens, us, alvo, x0=360, y=300, passo=420, lane0=470, dl=150, base=62, n=2, ban=None, rot=None,
          alt=150):
    """itens = [(data, valor_de_partida, 'fator', valor_na_data_focal)]; us = progresso da viagem de cada saco (0 = na sua
    data, 1 = na data focal `alvo`). O saco cresce (para o futuro) ou encolhe (para hoje) enquanto viaja."""
    if a <= 0:
        return
    trilha(c, x0, y, n, passo, a, rot, destaque=alvo if (ban or 0) > 0.3 else None)
    xa = x0 + alvo * passo
    if ban is not None:
        bandeira(c, xa, y, a, sobe=ban, alt=alt)
    for j, ((k, v0, fat, v1), u) in enumerate(zip(itens, us)):
        yl = lane0 + j * dl
        xk = x0 + k * passo
        uu = ease_io(clamp(u))
        x = xk + (xa - xk) * uu
        v = v0 + (v1 - v0) * uu
        line(c, xk, y + 70, xk, yl - base - 10, LIGHT, a * (1 - clamp(u * 3)), 3, dash=[8, 8])
        if k != alvo:
            line(c, min(xk, xa), yl, max(xk, xa), yl, LINE, a * 0.8, 4, dash=[10, 10])
            if 0.05 < u < 0.98:
                pill(c, fat, (xk + xa) / 2, yl - base - 26, PURPLE, size=24, a=a, anchor="center", bounds=(0, 1920))
        rotulo = f"{v1:,.0f}".replace(",", ".") if u >= 0.98 else f"{v0:,.0f}".replace(",", ".")
        saco(c, x, yl, _r_saco(v, base), rotulo, a, GREEN if (u >= 0.98 and k != alvo) else None)


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


def parcelas(c, t, a, vals, us, x0=360, y=290, passo=380, lane0=440, dl=135, r=52, fat=("", "× 0,980", "× 0,961"),
             rot=("no ato", "30 dias", "60 dias"), alt=120):
    """as três parcelas do televisor (ato, 30 e 60 dias) voltando até a data da compra; encolhem pelo fator de desconto.
    vals = [(valor_na_data, valor_hoje)]"""
    if a <= 0:
        return
    trilha(c, x0, y, 2, passo, a, list(rot), destaque=0)
    bandeira(c, x0, y, a, s="HOJE", alt=alt)
    for j, ((v0, v1), u) in enumerate(zip(vals, us)):
        yl = lane0 + j * dl
        xk = x0 + j * passo
        uu = ease_io(clamp(u))
        x = xk + (x0 - xk) * uu
        if j:
            line(c, x0, yl, xk, yl, LINE, a * 0.8, 4, dash=[10, 10])
            if 0.05 < u < 0.98:
                pill(c, fat[j], (xk + x0) / 2, yl - r - 22, PURPLE, size=24, a=a, anchor="center", bounds=(0, 1920))
        rr = r * (1 - 0.18 * j * uu)
        moeda(c, x, yl, rr, v1 if u >= 0.98 else v0, BLUE if (u >= 0.98 or j == 0) else PURPLE, a)


def etiqueta(c, x, y, s, a, col=None, tit="À VISTA", w=330):
    """etiqueta de preço (cartão com furinho)"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x - w / 2, y - 80, w, 160, 24, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, y - 80, w, 160), 24, 24), paint(col, a, stroke=5))
    c.drawCircle(x - w / 2 + 30, y - 50, 9, paint(col, a))
    text(c, tit, x, y - 30, 26, "black", col, a, tracking=2)
    fmid(c, s, x, y + 30, 50, "black", INK, a)


def placar(c, cx, cy, a, loja, aplic, venc="loja", sub_loja="a loja cobra", sub_apl="a aplicação rende"):
    """disputa LOJA × APLICAÇÃO: dois cartões e o selo do vencedor"""
    if a <= 0:
        return
    for k, (tit, v, sub, col) in enumerate((("LOJA", loja, sub_loja, RED), ("APLICAÇÃO", aplic, sub_apl, GREEN))):
        x = cx - 260 + k * 520
        rrect(c, x - 220, cy - 120, 440, 240, 26, mix("#FFFFFF", col, 0.07), a, shadow=True)
        text(c, tit, x, cy - 70, 30, "black", col, a, tracking=2)
        fmid(c, v, x, cy + 5, 62, "black", INK, a)
        text(c, sub, x, cy + 80, 24, "bold", GRAY, a)
    text_mid(c, "×", cx, cy, 70, "black", INK2, a)


# ======================================================================
# abertura
# ======================================================================

S_SORTEIO = [(0, 10000, "× 1,21", 12100), (1, 11000, "× 1,1", 12100), (2, 12100, "", 12100)]
S_HOJE = [(0, 10000, "", 10000), (1, 11000, "÷ 1,1", 10000), (2, 12100, "÷ 1,21", 10000)]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "COMPARAÇÃO DE PROPOSTAS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    ac = ep(t, C["01.c"], 0.4)
    ad = ep(t, C["01.d"], 0.4)
    us = [ep(t, C["01.d"] + 1.0, 1.6), ep(t, C["01.d"] + 1.6, 1.4), 1.0]
    sacos(c, t, aa, S_SORTEIO, us if ad > 0 else [0, 0, 0], 2, x0=320, y=390, passo=360, lane0=530, dl=135, base=56,
          ban=ep(t, C["01.d"] + 0.3, 0.6) if ad > 0 else None)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        text(c, "Qual você escolhe?", 1440, 400, 56, "black", INK, ab)
    if ac > 0:
        selo(c, 1440, 540, ac * (1 - ad), "O MAIOR? PEGADINHA!", AMBER, -4, 40)
    if ad > 0:
        rrect(c, 1180, 470, 520, 120, 22, mix("#FFFFFF", GREEN, 0.12), ad, shadow=True)
        text_mid(c, "a 10% ao ano", 1440, 505, 30, "bold", INK2, ad)
        text_mid(c, "os três valem o mesmo", 1440, 555, 36, "black", GREEN, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI DECIDIR", GREEN)
    itens = [("02.a", "À VISTA OU PARCELAR", "qual proposta compensa", BLUE),
             ("02.b", "DATAS DIFERENTES", "comparar valores no tempo", PURPLE),
             ("02.c", "SEM O 'MAIOR NÚMERO'", "a pegadinha mais comum", AMBER)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 520
        rrect(c, x, 290 + d, 440, 420, 26, "#FFFFFF", a, shadow=True)
        rrect(c, x, 290 + d, 440, 70, 26, col, a * 0.14)
        text(c, tit, x + 220, 338 + d, 28 if len(tit) > 18 else 32, "black", col, a)
        if k == 0:
            etiqueta(c, x + 220, 490 + d, "R$ 2.900", a, BLUE, w=300)
        elif k == 1:
            for j, v in enumerate((10000, 11000, 12100)):
                saco(c, x + 110 + j * 110, 500 + d, _r_saco(v, 46), "", a)
        else:
            text_mid(c, "12.100 > 10.000?", x + 220, 490 + d, 40, "black", AMBER, a)
        para(c, sub, x + 30, 640 + d, 28, "bold", INK2, a, 380, 36, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE RÁPIDO", "SÉRIE DE EMPRÉSTIMOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 270 + d1, 720, 480, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "MOVER NO TEMPO", 560, 320 + d1, PURPLE, size=24, a=a1, anchor="center", bounds=(0, 1920))
        linha(c, [("futuro: ", INK2), ("× (1 + i)ⁿ", PURPLE)], 560, 430 + d1, 50, a1)
        linha(c, [("presente: ", INK2), ("÷ (1 + i)ⁿ", BLUE)], 560, 540 + d1, 50, ep(t, C["03.a"] + 4.0, 0.4))
        text(c, "cada parcela pelo SEU prazo", 560, 670 + d1, 28, "bold", GRAY, ep(t, C["03.a"] + 6.0, 0.4))
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 270 + d2, 720, 480, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "TAXA EMBUTIDA", 1360, 320 + d2, PURPLE, size=24, a=a2, anchor="center", bounds=(0, 1920))
        K.mdraw(c, "taxa = juros/financiado", 1360, 500 + d2, 56, PURPLE, a2, align="center")
        text(c, "financiado = o que você ficou devendo", 1360, 670 + d2, 26, "bold", GRAY, a2)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "O TELEVISOR", "À VISTA OU 3 VEZES?", BLUE),
                       ("05", "O SORTEIO", "HOJE OU DAQUI A 2 ANOS?", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 270, 420, 270, 24, INK, aa, shadow=True)
            rrect(c, 280, 290, 380, 210, 14, mix(BLUE, "#FFFFFF", 0.55), aa)
            rrect(c, 430, 540, 80, 40, 6, INK2, aa)
            etiqueta(c, 1000, 330, "R$ 2.900", aa, BLUE)
            etiqueta(c, 1440, 330, "3 × R$ 1.000", ep(t, C["04.a"] + 1.8, 0.4), PURPLE, "PARCELADO", w=400)
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            pill(c, "PROPOSTA = uma oferta, com valores e datas", 1220, 500, BLUE, size=28, a=ab, anchor="center",
                 bounds=(0, 1920))
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 640, 1400, 130, 22, mix("#FFFFFF", GREEN, 0.10), acc)
            text(c, "seu dinheiro guardado rende", 330, 718, 38, "black", INK2, acc, align="left")
            text(c, "2% ao mês", 1590, 718, 46, "black", GREEN, acc, align="right")
        return
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 280, 560, 330, 26, mix("#FFFFFF", AMBER, 0.14), aa, shadow=True)
        text(c, "BILHETE PREMIADO", 580, 350, 32, "black", AMBER, aa, tracking=2)
        text(c, "receber HOJE", 580, 450, 44, "black", INK, aa)
        text(c, "ou daqui a 2 ANOS", 580, 530, 44, "black", PURPLE, aa)
        saco(c, 1180, 470, 110, "hoje", aa)
        saco(c, 1520, 470, 130, "2 anos", ep(t, C["05.a"] + 2.0, 0.4))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        regra(c, "duas perguntas · a MESMA regra", W / 2, 740, ab, 40, PURPLE)


# ======================================================================
# bloco a — a regra de ouro
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("06", "DÁ PARA COMPARAR?", "DO JEITO QUE ESTÃO, NÃO", RED),
                       ("07", "A DATA FOCAL", "O PONTO DE ENCONTRO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            saco(c, 560, 420, _r_saco(10000, 120), "10.000", aa)
            text(c, "hoje", 560, 580, 30, "black", BLUE, aa)
            saco(c, 1360, 420, _r_saco(12100, 120), "12.100", aa)
            text(c, "daqui a 2 anos", 1360, 580, 30, "black", PURPLE, aa)
            text_mid(c, "?", 960, 420, 120, "black", RED, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            pill(c, "moedas de PAÍSES DIFERENTES", 960, 300, AMBER, size=30, a=ab, anchor="center", bounds=(0, 1920))
            linha(c, [("não se somam · ", INK2), ("não se comparam", RED)], W / 2, 660, 40, ep(t, C["06.b"] + 2.0, 0.4))
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            regra(c, "primeiro: CÂMBIO para a mesma data", W / 2, 770, acc, 38, PURPLE)
        return
    aa = ep(t, C["07.a"], 0.5)
    trilha(c, 420, 400, 2, 540, aa, destaque=2 if t > C["07.c"] else None)
    if aa > 0:
        bandeira(c, 1500, 400, aa, sobe=ep(t, C["07.c"], 0.8) if t > C["07.c"] else 0.0)
        pill(c, "DATA FOCAL = o ponto de encontro", W / 2, 260, BLUE, size=30, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 560, 1320, 120, 22, mix("#FFFFFF", BLUE, 0.08), ab)
        text(c, "VALOR EQUIVALENTE", 340, 612, 30, "black", BLUE, ab, align="left")
        text(c, "quanto o valor vale NA DATA FOCAL", 340, 655, 28, "bold", INK2, ab, align="left")
    acc = ep(t, C["07.c"] + 1.5, 0.5)
    if acc > 0:
        regra(c, "finque a bandeirinha · leve tudo até ela · só então compare", W / 2, 770, acc, 32, PURPLE)


# ======================================================================
# bloco b — qualquer data focal
# ======================================================================

def b_focal(c, t, C, B):
    head_seq(c, t, C, [("08", "QUAL DATA ESCOLHER?", "QUALQUER UMA", PURPLE),
                       ("09", "A CONCLUSÃO NÃO MUDA", "TODOS × O MESMO FATOR", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        if t < C["08.c"]:
            ab = ep(t, C["08.b"], 0.3)
            us = [1.0, ep(t, C["08.b"] + 1.0, 1.4), ep(t, C["08.b"] + 4.0, 1.6)] if ab > 0 else [0, 0, 0]
            sacos(c, t, aa, S_HOJE, us, 0, x0=420, y=390, passo=480, lane0=520, dl=118, base=48, alt=120,
                  ban=ep(t, C["08.b"], 0.6) if ab > 0 else None)
            pill(c, "10% ao ano", 1660, 300, GREEN, size=26, a=aa, anchor="center", bounds=(0, 1920))
            return
        us = [ep(t, C["08.c"] + 0.5, 1.4), ep(t, C["08.c"] + 1.2, 1.2), 1.0]
        sacos(c, t, 1.0, S_SORTEIO, us, 2, x0=420, y=390, passo=480, lane0=520, dl=118, base=48, alt=120,
              ban=ep(t, C["08.c"], 0.6))
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        for k, (tit, v, col) in enumerate((("BANDEIRA HOJE", "10.000 = 10.000 = 10.000", BLUE),
                                           ("BANDEIRA EM 2 ANOS", "12.100 = 12.100 = 12.100", PURPLE))):
            y = 300 + k * 170
            rrect(c, 300, y - 60, 1320, 120, 22, mix("#FFFFFF", col, 0.08), aa)
            text(c, tit, 340, y + 10, 28, "black", col, aa, align="left")
            text(c, v, 1580, y + 14, 40, "black", INK, aa, align="right")
        arrow(c, 960, 370, 960, 400, GREEN, aa, 5, 14)
        pill(c, "× 1,21 em todos", 1120, 385, GREEN, size=24, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        pill(c, "quem era maior continua maior", 960, 610, BLUE, size=30, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        K.atalho(c, 380, 680, 1160, 120, "DICA", ["escolha a data que deixa a conta MAIS SIMPLES"], acc, 36)


# ======================================================================
# bloco c — taxa de oportunidade
# ======================================================================

def b_taxa(c, t, C, B):
    head_seq(c, t, C, [("10", "QUAL TAXA USAR?", "A TAXA DE OPORTUNIDADE", BLUE),
                       ("11", "DE ONDE VEM?", "DO ENUNCIADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 250, 1400, 150, 22, mix("#FFFFFF", BLUE, 0.08), aa)
            text(c, "TAXA DE OPORTUNIDADE", 300, 310, 38, "black", BLUE, aa, align="left")
            text(c, "o que o seu dinheiro faria se ficasse com você", 300, 362, 32, "bold", INK2, aa, align="left")
        for k, (cue, tit, sub, col) in enumerate((("10.b", "TEM O DINHEIRO?", "quanto ele RENDERIA aplicado", GREEN),
                                                  ("10.c", "NÃO TEM?", "o JURO que pagaria emprestado", RED))):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            x = 260 + k * 720
            rrect(c, x, 450 + d, 680, 300, 24, "#FFFFFF", a, shadow=True)
            rrect(c, x, 450 + d, 680, 70, 24, col, a * 0.14)
            text(c, tit, x + 340, 498 + d, 32, "black", col, a)
            if k == 0:
                saco(c, x + 340, 620 + d, 60, "+%", a, GREEN)
            else:
                text_mid(c, "− juros", x + 340, 620 + d, 54, "black", RED, a)
            text(c, sub, x + 340, 720 + d, 28, "bold", INK2, a)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 270, 1320, 260, 22, "#FFFFFF", aa, shadow=True)
        text(c, "ENUNCIADO", 340, 320, 24, "black", GRAY, aa, align="left", tracking=2)
        text(c, "... ele aplicaria o dinheiro a", 340, 400, 38, "bold", INK2, aa, align="left")
        w0 = text_w("... ele aplicaria o dinheiro a ", "bold", 38)
        ag = ep(t, C["11.c"], 0.6)
        if ag > 0:
            rrect(c, 340 + w0 - 6, 362, (text_w("10% ao ano", "black", 38) + 12) * ag, 56, 8, OURO, aa * 0.7)
        text(c, "10% ao ano", 340 + w0, 400, 38, "black", INK, aa, align="left")
        text(c, "... do ponto de vista financeiro, ...", 340, 470, 38, "bold", INK2, aa, align="left")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        selo(c, 960, 640, ab, "SEM A TAXA: COMPARAÇÃO NÃO DEFINIDA", RED, -3, 32)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        K.atalho(c, 380, 700, 1160, 110, "DICA", ["antes de qualquer conta: GRIFE A TAXA"], acc, 36)


# ======================================================================
# bloco d — o televisor
# ======================================================================

TV = [("1.000", "1.000"), ("1.000", "980"), ("1.000", "961")]


def b_tv(c, t, C, B):
    head_seq(c, t, C, [("12", "À VISTA OU A PRAZO?", "A LINHA DO TEMPO", PURPLE),
                       ("13", "AS PARCELAS VIAJAM", "ATÉ A DATA DA COMPRA", PURPLE),
                       ("14", "ATALHO", "A VIAGEM SEM CALCULADORA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    if sid in ("12", "13"):
        aa = ep(t, C["12.a"], 0.5)
        us = [1.0, ep(t, C["13.b"], 1.4), ep(t, C["13.b"] + 2.6, 1.6)] if sid == "13" else [0, 0, 0]
        parcelas(c, t, aa, TV, us, x0=300, y=390, passo=320, lane0=510, dl=118, r=48)
        acc = ep(t, C["12.c"], 0.5)
        if sid == "12" and acc > 0:
            rrect(c, 1100, 400, 600, 330, 22, mix("#FFFFFF", BLUE, 0.06), acc, shadow=True)
            text(c, "FATOR DE DESCONTO", 1400, 450, 28, "black", BLUE, acc, tracking=2)
            K.mdraw(c, "1/fator", 1400, 520, 44, BLUE, acc, align="center")
            linha(c, [("1 mês: ", INK2), ("1 ÷ 1,02 ≈ 0,980", PURPLE)], 1400, 610, 34, ep(t, C["12.c"] + 4.0, 0.4))
            linha(c, [("2 meses: ", INK2), ("1 ÷ 1,02² ≈ 0,961", PURPLE)], 1400, 680, 34, ep(t, C["12.c"] + 7.0, 0.4))
        if sid == "13":
            etiqueta(c, 1440, 380, "R$ 2.900", ep(t, C["13.a"], 0.4), BLUE)
            acc = ep(t, C["13.c"], 0.5)
            if acc > 0:
                rrect(c, 1170, 520, 540, 120, 22, mix("#FFFFFF", PURPLE, 0.10), acc, shadow=True)
                text(c, "VALOR HOJE DO PARCELADO", 1440, 556, 22, "black", PURPLE, acc, tracking=1)
                linha(c, [("1.000 + 980 + 961 = ", INK), ("2.941", PURPLE)], 1440, 600, 34, acc)
            ad = ep(t, C["13.d"], 0.5)
            if ad > 0:
                linha(c, [("2.941 > 2.900 → ", INK2), ("PAGUE À VISTA", GREEN)], 1440, 720, 36, ad)
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        K.atalho(c, 300, 260, 1320, 170, "ATALHO",
                 ["1.000 × 0,980  =  tirar 2%  =  1.000 − 20  =  980"], aa, 40)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        moeda(c, 420, 560, 70, "1.000", BLUE, ab)
        text(c, "a parcela DO ATO não viaja:", 540, 550, 36, "black", INK, ab, align="left")
        text(c, "ela já nasce na data focal", 540, 600, 32, "bold", GRAY, ab, align="left")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        conferido(c, "valor hoje (2.941) < soma das parcelas (3.000)", 380, 760, acc, True, 36)


# ======================================================================
# bloco e — pela taxa embutida
# ======================================================================

def b_embutida(c, t, C, B):
    head_seq(c, t, C, [("15", "OUTRO CAMINHO", "LOJA × APLICAÇÃO", PURPLE),
                       ("16", "E SE RENDESSE MAIS?", "A DECISÃO SE INVERTE", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        ab = ep(t, C["15.b"], 0.5)
        placar(c, 960, 420, max(aa, 0.001) if aa > 0 else 0, "≈ 3,5%" if ab > 0 else "?", "2%" if ab > 0 else "?",
               sub_loja="pelo tempo, ao mês", sub_apl="ao mês")
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            regra(c, "a loja cobra MAIS → pague à vista", W / 2, 690, acc, 40, GREEN)
            text(c, "mesma decisão do valor hoje", W / 2, 790, 28, "bold", GRAY, acc)
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        pill(c, "aplicação a 5% ao mês", 960, 250, AMBER, size=30, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["16.b"], 0.5)
    us = [1.0, ep(t, C["16.b"] + 0.5, 1.2), ep(t, C["16.b"] + 1.6, 1.4)]
    parcelas(c, t, ab, [("1.000", "1.000"), ("1.000", "952"), ("1.000", "907")], us, x0=300, y=390, passo=300,
             lane0=510, dl=118, r=46, fat=("", "× 0,952", "× 0,907"))
    if ab > 0:
        linha(c, [("1.000 + 952 + 907 ≈ ", INK), ("2.859", PURPLE)], 1400, 440, 38, ep(t, C["16.b"] + 4.5, 0.4))
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        linha(c, [("2.859 < 2.900 → ", INK2), ("PARCELE", GREEN)], 1400, 560, 42, acc)
        text(c, "a loja cobra MENOS que a aplicação", 1400, 640, 28, "bold", GRAY, acc)
        text(c, "o dinheiro fica trabalhando", 1400, 690, 28, "bold", GRAY, acc)


# ======================================================================
# bloco f — "sem juros"
# ======================================================================

def b_semjuros(c, t, C, B):
    frame(c, t, B["start"], "\"SEM JUROS\"", "NÃO QUER DIZER \"TANTO FAZ\"", AMBER)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        etiqueta(c, 560, 360, "R$ 3.000", aa, BLUE)
        etiqueta(c, 1360, 360, "3 × R$ 1.000", aa, PURPLE, "SEM JUROS", w=420)
        text_mid(c, "=", 960, 360, 80, "black", INK2, aa * (1 - ep(t, C["17.b"], 0.4)))
        text_mid(c, "?", 960, 360, 80, "black", AMBER, ep(t, C["17.b"], 0.4) * (1 - ep(t, C["17.c"], 0.4)))
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        rrect(c, 1100, 500, 520, 120, 22, mix("#FFFFFF", PURPLE, 0.10), ab, shadow=True)
        text(c, "VALOR HOJE, A 2%", 1360, 538, 22, "black", PURPLE, ab, tracking=1)
        linha(c, [("≈ ", INK2), ("R$ 2.941", PURPLE)], 1360, 585, 40, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        text_mid(c, ">", 960, 360, 80, "black", GREEN, acc)
        regra(c, "mesmo valor, pago MAIS TARDE → PARCELE", W / 2, 740, acc, 38, GREEN)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "OS DOIS CAMINHOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        trilha(c, 360, 420, 1, 600, aa, ["hoje", "1 mês"], destaque=0 if t > C["19"] else None)
        etiqueta(c, 360, 620, "R$ 1.000", aa, BLUE, w=300)
        etiqueta(c, 960, 620, "R$ 1.050", aa, PURPLE, "EM 1 MÊS", w=300)
        pill(c, "seu dinheiro: 3% ao mês", 1450, 300, GREEN, size=28, a=aa, anchor="center", bounds=(0, 1920))
    if t < C["19"]:
        pause_timer(c, t, C["18.end"] - 1.9, 1450, 560)
        return
    bandeira(c, 360, 420, 1.0, s="HOJE", sobe=ep(t, C["19.a"], 0.6), alt=120)
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        rrect(c, 1200, 420, 520, 150, 22, "#FFFFFF", a1, shadow=True)
        text(c, "CAMINHO 1 · VALOR HOJE", 1460, 460, 22, "black", PURPLE, a1, tracking=1)
        linha(c, [("1.050 ÷ 1,03 ≈ ", INK), ("1.019,42", PURPLE)], 1460, 520, 34, a1)
    a2 = ep(t, C["19.b"], 0.5)
    if a2 > 0:
        rrect(c, 1200, 600, 520, 150, 22, "#FFFFFF", a2, shadow=True)
        text(c, "CAMINHO 2 · LOJA × APLICAÇÃO", 1460, 640, 22, "black", PURPLE, a2, tracking=1)
        linha(c, [("50 ÷ 1.000 = ", INK), ("5%", RED), ("  >  3%", GREEN)], 1460, 700, 34, a2)
    a3 = ep(t, C["19.c"], 0.5)
    if a3 > 0:
        selo(c, 660, 790, a3, "PAGUE À VISTA", GREEN, -4, 40)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Só se comparam valores na mesma data.",
          "A taxa que decide é a do seu dinheiro: a taxa de oportunidade.",
          "Se a loja cobra mais do que a aplicação rende, pague à vista."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Comparar valores de datas diferentes", "são todos em reais",
          "reais de DATAS diferentes · a 10% ao ano, 10.000 hoje = 12.100 em 2 anos"),
         ("Escolher pelo MAIOR número", "mais dinheiro é melhor",
          "o maior número costuma estar na data mais distante · primeiro a data focal"),
         ]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


def _questao(c, t, C, sc, sol, xs, alts, okL, enun, fonte, pausa=True, size_en=28, size_alt=30):
    """enunciado à esquerda (sai quando começa a resolução), alternativas à direita"""
    a0 = ep(t, C[f"{sc}.a"], 0.4) * (1 - ep(t, C[sol], 0.4))
    _enunciado(c, enun, a0, size=size_en)
    text(c, fonte, 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"{sc}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{xs}.x{L.lower()}"] for L in "ABCDE" if L != okL}
    K.alternativas(c, t, C, alts, 1000, 240, 700, size_alt, C[f"{sol}.ok"], okL, cues_in, cues_x, gap=22)
    if pausa and t < C[sol]:
        pause_timer(c, t, C[f"{sc}.end"] - 2.4, 1340, 800)


def _caixa_sol(c, t, C, sol):
    a = ep(t, C[sol], 0.4)
    if a > 0:
        rrect(c, 170, 230, 760, 600, 20, "#FFFFFF", a, shadow=True)
    return a


ALTS8 = [("A", "hoje é melhor: dinheiro hoje sempre vale mais", "regra geral, sem conta", RED),
         ("B", "em 1 ano é melhor: paga R$ 1.000 a mais", "decide sem conta", RED),
         ("C", "em 2 anos é melhor: é o maior valor", "compara nominais", RED),
         ("D", "hoje = 2 anos, mas 1 ano é pior", "deixou 11.000 parado", RED),
         ("E", "as três opções são equivalentes", "", GREEN)]


def b_q8(c, t, C, B):
    head_seq(c, t, C, [("23", "QUESTÃO 8 · EU FAÇO", "PRÊMIOS EM DATAS DIFERENTES", BLUE),
                       ("25", "AS OUTRAS ALTERNATIVAS", "DE ONDE VEM CADA ERRO", RED)])
    card(c, *CARD_R)
    _questao(c, t, C, "23", "24", "25", ALTS8, "E",
             "O ganhador de um sorteio pode escolher entre três formas de receber o prêmio: R$ 10.000,00 hoje; "
             "R$ 11.000,00 daqui a um ano; ou R$ 12.100,00 daqui a dois anos. Ele aplicaria o dinheiro a 10% ao ano, "
             "no regime de juros compostos. Do ponto de vista financeiro,", "Questão do material de estudo (seção 12)",
             pausa=False, size_alt=28)
    if t < C["24"]:
        return
    _caixa_sol(c, t, C, "24")
    a = ep(t, C["24.a"], 0.4)
    if a > 0:
        text(c, "agora a pergunta é de DECISÃO", 500, 285, 28, "black", PURPLE, a)
    ab = ep(t, C["24.b"], 0.4)
    us = [ep(t, C["24.b"] + 1.0, 1.6), ep(t, C["24.c"], 1.4), 1.0]
    sacos(c, t, ab, S_SORTEIO, us, 2, x0=290, y=430, passo=260, lane0=545, dl=78, base=34, alt=100,
          ban=ep(t, C["24.b"], 0.6))
    ad = ep(t, C["24.d"], 0.4)
    if ad > 0:
        rrect(c, 230, 770, 640, 50, 12, mix("#FFFFFF", GREEN, 0.15), ad)
        text_mid(c, "na mesma data: 12.100 = 12.100 = 12.100", 550, 795, 26, "black", GREEN, ad)


ALTS2 = [("A", "à vista: juros de ≈ 11,1% ao mês > 1% da aplicação", "", GREEN),
         ("B", "parcelar: o anúncio não menciona juros", "acreditou no \"sem juros\"", RED),
         ("C", "parcelar: R$ 500 rendem R$ 5, compensa o desconto", "R$ 5 × R$ 50", RED),
         ("D", "à vista: juros de 5% ao mês > 1%", "taxa errada", RED),
         ("E", "qualquer uma: total de R$ 1.000 nos dois", "à vista é R$ 950", RED)]


def b_q2(c, t, C, B):
    head_seq(c, t, C, [("26", "QUESTÃO 2 · VOCÊ FAZ", "DESCONTO À VISTA E APLICAÇÃO", BLUE),
                       ("27", "CONFIRA", "LOJA × APLICAÇÃO", GREEN),
                       ("28", "AS ARMADILHAS", "DE ONDE VEM CADA ERRO", RED)])
    card(c, *CARD_R)
    _questao(c, t, C, "26", "27", "28", ALTS2, "A",
             "Uma loja vende um produto por R$ 1.000,00 em 2 parcelas de R$ 500,00 (uma no ato e outra em 30 dias) ou "
             "com 5% de desconto à vista. Um cliente tem o dinheiro aplicado em um investimento que rende 1% ao mês. "
             "A decisão mais vantajosa para ele é", "Questão do material de estudo (seção 12)", size_alt=26)
    if t < C["27"]:
        return
    _caixa_sol(c, t, C, "27")
    linha(c, [("à vista: 1.000 × 0,95 = ", INK), ("950", BLUE)], 550, 300, 34, ep(t, C["27.a"], 0.4))
    pill(c, "a 1ª parcela é ENTRADA", 550, 380, PURPLE, size=24, a=ep(t, C["27.b"], 0.4), anchor="center")
    linha(c, [("financiado: 950 − 500 = ", INK), ("450", PURPLE)], 550, 450, 34, ep(t, C["27.b"] + 2.0, 0.4))
    a3 = ep(t, C["27.c"], 0.4)
    if a3 > 0:
        text(c, "paga 500 em 30 dias → juros de 50", 550, 535, 28, "bold", INK2, a3)
        linha(c, [("50 ÷ 450 ≈ ", INK), ("11,1% ao mês", RED)], 550, 600, 38, ep(t, C["27.c"] + 3.0, 0.4))
    a4 = ep(t, C["27.d"], 0.4)
    if a4 > 0:
        linha(c, [("loja 11,1%", RED), ("  >  ", INK2), ("aplicação 1%", GREEN)], 550, 690, 34, a4)
        selo(c, 550, 775, a4, "PAGUE À VISTA", GREEN, -3, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PARTE FIXA + PARTE VARIÁVEL", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        caixa(c, 560, 380, "PLANO A", "R$ 50 + R$ 0,50/min", BLUE, aa, 560)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        caixa(c, 1360, 380, "PLANO B", "R$ 80 + R$ 0,20/min", PURPLE, ab, 560)
    acc = ep(t, C["30.c"], 0.5)
    if acc > 0:
        text(c, "Qual é melhor?", W / 2, 600, 56, "black", INK, acc)
        selo(c, W / 2, 730, acc, "DEPENDE...", AMBER, -4, 50)


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Você costuma pagar à vista ou parcelar?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, regra=b_regra, focal=b_focal,
              taxa=b_taxa, tv=b_tv, embutida=b_embutida, semjuros=b_semjuros, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q8=b_q8, q2=b_q2, ponte=b_ponte, cta=b_cta)
