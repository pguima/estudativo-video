"""Visual — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 3: remarcações, liquidações e o lucro que sobra (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: regua() (a RÉGUA DO CUSTO: eixo com "custo = 1", zona verde de lucro à direita e vermelha de
prejuízo à esquerda; seta que sobe até a etiqueta e outra que desce até o preço final), etiqueta() (etiqueta de loja com
o preço antigo riscado e o novo por cima), produto() (cartão de item com preço e custo escondido que aparece),
balanca() (balança de dois pratos que pende para o lado mais pesado), linha(), caixa(), conferido().
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
_s = importlib.util.spec_from_file_location("comum030", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_descontos_lucro_ep3_remarcacoes.mp4"
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


def regua(c, t, y, a, x0=260, x1=1660, vmax=2.0, sobe=0.0, desce=0.0, alvo_sobe=1.5, alvo_desce=1.0,
          rot_sobe="× 1,5", rot_desce="× 2/3", rot_etiq="ETIQUETA", rot_final="VENDA", marcas=(0.5, 1.0, 1.5, 2.0),
          fmt=None):
    """A RÉGUA DO CUSTO: eixo de 0 a vmax; o 1 é o custo. Zona verde (lucro) à direita do 1, vermelha à esquerda.
    sobe/desce = progresso das setas (custo → etiqueta, por cima; etiqueta → venda final, por baixo)."""
    if a <= 0:
        return
    X = lambda v: x0 + (x1 - x0) * v / vmax
    fmt = fmt or (lambda v: f"{v:.2f}".rstrip("0").rstrip(".").replace(".", ","))
    rrect(c, X(1.0), y - 26, x1 - X(1.0) + 30, 52, 12, GREEN, a * 0.12)
    rrect(c, x0 - 30, y - 26, X(1.0) - x0 + 30, 52, 12, RED, a * 0.10)
    text(c, "LUCRO →", x1 + 20, y + 125, 26, "black", GREEN, a, align="right")
    text(c, "← PREJUÍZO", x0 - 20, y + 125, 26, "black", RED, a, align="left")
    line(c, x0 - 30, y, x1 + 30, y, INK2, a, 5)
    for v in marcas:
        line(c, X(v), y - 18, X(v), y + 18, INK2, a, 4)
        text(c, fmt(v), X(v), y + 62, 28, "black", INK2 if v != 1.0 else BLUE, a)
    c.drawCircle(X(1.0), y, 16, paint(BLUE, a))
    pill(c, "CUSTO = 1", X(1.0), y - 70, BLUE, size=26, a=a, anchor="center", bounds=(0, 1920))
    if sobe > 0:
        u = ease_io(clamp(sobe))
        xa, xb = X(1.0), X(alvo_sobe)
        pts = 40
        path = skia.Path()
        for k in range(pts + 1):
            s_ = u * k / pts
            xx = xa + (xb - xa) * s_
            yy = y - 90 - 120 * math.sin(math.pi * s_)
            path.moveTo(xx, yy) if k == 0 else path.lineTo(xx, yy)
        c.drawPath(path, paint(PURPLE, a, stroke=6, cap_round=True))
        if u > 0.98:
            arrow(c, xb - 1, y - 92, xb, y - 40, PURPLE, a, 6, 20)
            c.drawCircle(xb, y, 14, paint(PURPLE, a))
            pill(c, rot_sobe, (xa + xb) / 2, y - 240, PURPLE, size=28, a=a, anchor="center", bounds=(0, 1920))
            text(c, rot_etiq, xb + 26, y - 60, 26, "black", PURPLE, a, align="left")
    if desce > 0:
        u = ease_io(clamp(desce))
        xa, xb = X(alvo_sobe), X(alvo_desce)
        pts = 40
        path = skia.Path()
        for k in range(pts + 1):
            s_ = u * k / pts
            xx = xa + (xb - xa) * s_
            yy = y + 100 + 110 * math.sin(math.pi * s_)
            path.moveTo(xx, yy) if k == 0 else path.lineTo(xx, yy)
        c.drawPath(path, paint(AMBER, a, stroke=6, cap_round=True))
        if u > 0.98:
            arrow(c, xb, y + 102, xb, y + 40, AMBER, a, 6, 20)
            col = GREEN if alvo_desce > 1.0005 else (RED if alvo_desce < 0.9995 else BLUE)
            c.drawCircle(xb, y, 18, paint(col, a))
            pill(c, rot_desce, (xa + xb) / 2, y + 250, AMBER, size=28, a=a, anchor="center", bounds=(0, 1920))
            text(c, rot_final, xb - 30, y + 130, 26, "black", col, a, align="right")


def etiqueta(c, cx, cy, antigo, novo, a, risco=0.0, novo_a=0.0, w=360, h=200, rot=-4):
    """etiqueta de loja (com furo e barbante); preço antigo riscado e o novo por cima, em vermelho"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    p = skia.Path()
    p.moveTo(-w / 2 + 60, -h / 2); p.lineTo(w / 2, -h / 2); p.lineTo(w / 2, h / 2); p.lineTo(-w / 2 + 60, h / 2)
    p.lineTo(-w / 2, 0); p.close()
    c.drawPath(p, paint("#FFF7E0", a))
    c.drawPath(p, paint(AMBER, a, stroke=4))
    c.drawCircle(-w / 2 + 50, 0, 12, paint("#FFFFFF", a))
    c.drawCircle(-w / 2 + 50, 0, 12, paint(AMBER, a, stroke=3))
    line(c, -w / 2 + 40, 0, -w / 2 - 50, -60, GRAY, a, 3)
    yy = -24 if novo else 10
    text_mid(c, antigo, 30, yy, 48 if not novo else 40, "black", INK if not novo else GRAY, a)
    if risco > 0:
        tw = text_w(antigo, "black", 40)
        strike(c, 30 - tw / 2 - 10, yy, 30 + tw / 2 + 10, yy, a * clamp(risco), RED, clamp(risco))
    if novo and novo_a > 0:
        text_mid(c, novo, 30, 46, 52, "black", RED, a * novo_a)
    c.restore()


def produto(c, cx, cy, a, nome, preco, custo=None, ac=0.0, col=None, w=420, h=300, icone="cel"):
    """cartão de item: ícone, preço de venda e o custo escondido que aparece (ac)"""
    if a <= 0:
        return
    col = col or INK
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#FFFFFF", a, shadow=True)
    # ícone simples
    if icone == "cel":
        rrect(c, cx - 34, cy - h / 2 + 26, 68, 110, 12, "#2B2F3A", a)
        rrect(c, cx - 26, cy - h / 2 + 36, 52, 84, 6, mix("#FFFFFF", BLUE, 0.35), a)
    else:
        for dx in (-42, 42):
            c.drawCircle(cx + dx, cy - h / 2 + 96, 30, paint(INK2, a, stroke=6))
        line(c, cx - 42, cy - h / 2 + 96, cx, cy - h / 2 + 60, INK2, a, 6)
        line(c, cx, cy - h / 2 + 60, cx + 42, cy - h / 2 + 96, INK2, a, 6)
        line(c, cx - 12, cy - h / 2 + 50, cx + 18, cy - h / 2 + 50, INK2, a, 6)
    text(c, nome, cx, cy - h / 2 + 168, 26, "black", col, a)
    text_mid(c, preco, cx, cy + 50, 46, "black", INK, a)
    if ac > 0:
        rrect(c, cx - w / 2 + 20, cy + 88, w - 40, 54, 14, mix("#FFFFFF", col, 0.14), a * ac)
        text_mid(c, custo, cx, cy + 115, 32, "black", col, a * ac)


def balanca(c, cx, cy, a, incl=0.0, esq="", dir_="", col_e=GREEN, col_d=RED, w=560):
    """balança de dois pratos; incl > 0 pende para a direita"""
    if a <= 0:
        return
    ang = 12 * clamp(incl, -1, 1)
    line(c, cx, cy, cx, cy + 220, INK2, a, 8)
    rrect(c, cx - 90, cy + 214, 180, 22, 8, INK2, a)
    c.drawCircle(cx, cy, 14, paint(INK2, a))
    rad = math.radians(ang)
    dx, dy = w / 2 * math.cos(rad), w / 2 * math.sin(rad)
    line(c, cx - dx, cy - dy, cx + dx, cy + dy, INK2, a, 8)
    for sx, sy, s_, col in ((cx - dx, cy - dy, esq, col_e), (cx + dx, cy + dy, dir_, col_d)):
        line(c, sx, sy, sx - 70, sy + 90, GRAY, a, 3)
        line(c, sx, sy, sx + 70, sy + 90, GRAY, a, 3)
        rrect(c, sx - 110, sy + 86, 220, 20, 10, col, a * 0.8)
        if s_:
            text_mid(c, s_, sx, sy + 150, 34, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REMARCAÇÕES E LIQUIDAÇÕES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    etiqueta(c, 560, 420, "R$ 150,00", "R$ 100,00", aa, risco=ep(t, C["01.b"], 0.8), novo_a=ep(t, C["01.b"] + 0.6, 0.5),
             w=460, h=240)
    if aa > 0:
        pill(c, "+ 50% de lucro", 560, 600, GREEN, size=32, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "liquidação: − 33%", 560, 670, AMBER, size=32, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1010, 290, 700, 150, 26, "#FFFFFF", acc, shadow=True)
        linha(c, [("50% − 33% = ", INK), ("17%", AMBER), (" ?", INK)], 1360, 365, 54, acc)
        strike(c, 1060, 365, 1660, 365, ep(t, C["01.d"], 0.5), RED, ep(t, C["01.d"], 0.5))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1010, 500, 700, 200, 26, mix("#FFFFFF", BLUE, 0.10), ad, shadow=True)
        text(c, "lucro que sobrou", 1360, 560, 30, "bold", GRAY, ad)
        text_mid(c, "ZERO", 1360, 630, 80, "black", BLUE, ad)
    if ep(t, C["01.d"] + 2.0, 0.4) > 0:
        selo(c, 1360, 800, ep(t, C["01.d"] + 2.0, 0.4), "VENDEU PELO CUSTO", RED, -4, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "remarcou e liquidou: ainda dá lucro?", GREEN),
             ("02.b", "lucro de p% + prejuízo de p%: por que não empata", AMBER)]
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
        text(c, "lucro sobre o custo", 560, 430 + d1, 36, "black", INK2, a1)
        K.mdraw(c, "lucro/custo", 560, 580 + d1, 60, PURPLE, a1, align="center")
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 440, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "EP. 2 · PORCENTAGEM", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        text(c, "em sequência: MULTIPLIQUE", 1360, 430 + d2, 36, "black", PURPLE, a2)
        text(c, "os fatores  (1,5 · 0,7 · …)", 1360, 480 + d2, 32, "bold", INK2, a2)
        a3 = ep(t, C["03.b"] + 3.2, 0.4)
        text(c, "para voltar: DIVIDA", 1360, 590 + d2, 36, "black", PURPLE, a3)
        text(c, "pelo fator  (600 ÷ 1,2)", 1360, 640 + d2, 32, "bold", INK2, a3)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "QUEIMA DE ESTOQUE", "ETIQUETA, REMARCAÇÃO, LIQUIDAÇÃO", BLUE),
                       ("05", "DOIS CELULARES", "MESMO PREÇO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 250, 620, 90, 20, RED, aa * 0.9)
            text_mid(c, "QUEIMA DE ESTOQUE", 540, 295, 46, "black", "#FFFFFF", aa)
        etiqueta(c, 540, 560, "R$ 199,90", "R$ 129,90", ep(t, C["04.b"], 0.5), risco=ep(t, C["04.b"] + 2.2, 0.6),
                 novo_a=ep(t, C["04.b"] + 3.0, 0.5), w=460, h=240)
        defs = [("04.b", "ETIQUETA", "o preço marcado no produto", BLUE),
                ("04.b", "REMARCAÇÃO", "trocar o preço: risca o antigo, põe o novo", BLUE),
                ("04.c", "LIQUIDAÇÃO", "desconto para esvaziar a loja", BLUE)]
        for k, (cue, nome, sig, col) in enumerate(defs):
            a, d = rise(t, C[cue] + (2.2 if k == 1 else 0))
            if a <= 0:
                continue
            y = 270 + k * 175 + d
            rrect(c, 960, y, 760, 145, 22, mix("#FFFFFF", BLUE, 0.06), a)
            text(c, nome, 1000, y + 60, 38, "black", col, a, align="left")
            text(c, sig, 1000, y + 110, 28, "bold", INK2, a, align="left")
        return
    aa = ep(t, C["05.a"], 0.5)
    produto(c, 620, 450, aa, "CELULAR 1", "R$ 600,00", col=GREEN)
    produto(c, 1300, 450, aa, "CELULAR 2", "R$ 600,00", col=RED)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        pill(c, "+ 20% (lucro)", 620, 660, GREEN, size=30, a=ab, anchor="center", bounds=(0, 1920))
        pill(c, "− 20% (prejuízo)", 1300, 660, RED, size=30, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        text_mid(c, "EMPATOU?", W / 2, 780, 64, "black", AMBER, acc)


# ======================================================================
# bloco a — a régua do custo
# ======================================================================

def b_regua(c, t, C, B):
    head_seq(c, t, C, [("06", "A RÉGUA DO CUSTO", "O CUSTO VALE 1", PURPLE),
                       ("07", "DESCONTO MENOR, MARGEM MAIOR", "A ASSIMETRIA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        regua(c, t, 520, aa, sobe=ep(t, C["06.b"] + 0.4, 1.2), desce=ep(t, C["06.c"] + 0.4, 1.2))
        ac = ep(t, C["06.c"] + 2.0, 0.5)
        if ac > 0:
            rrect(c, 230, 690, 500, 120, 22, mix("#FFFFFF", PURPLE, 0.10), ac, shadow=True)
            K.mdraw(c, "1,5 · 2/3 = 1", 480, 750, 50, PURPLE, ac, align="center")
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            selo(c, 1520, 270, ad, "NEM LUCRO, NEM PREJUÍZO", BLUE, -3, 28)
        return
    aa = ep(t, C["07.a"], 0.5)
    for k, (tit, val, sub, col) in enumerate((("CUSTO", "R$ 100,00", "", BLUE),
                                              ("ETIQUETA (+50%)", "R$ 150,00", "+ R$ 50 sobre 100", GREEN),
                                              ("LIQUIDAÇÃO (−1/3)", "R$ 100,00", "− R$ 50 sobre 150", AMBER))):
        a = ep(t, C["07.t"] + k * 0.7, 0.5)
        caixa(c, 440 + k * 520, 360, tit, val, col, a, 440, sub=sub)
        if k:
            arrow(c, 440 + (k - 1) * 520 + 225, 360, 440 + k * 520 - 225, 360, col, a, 5, 18)
    if aa > 0:
        regra(c, "o desconto incide sobre a ETIQUETA, que já é MAIOR", W / 2, 620, aa, 38, AMBER)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        text(c, "50 reais de 100 = 50%      ·      50 reais de 150 = 33,3%", W / 2, 760, 34, "black", INK2, ab)


# ======================================================================
# bloco b — o truque do 100
# ======================================================================

def b_cem(c, t, C, B):
    head(c, t, B["start"], "O TRUQUE DO 100", "O CUSTO VALE 100", GREEN)
    card(c, *CARD_R)
    vals = [("08.a", "CUSTO", "100", BLUE), ("08.b", "ETIQUETA", "150", GREEN), ("08.c", "LIQUIDAÇÃO", "100", AMBER)]
    ops = ["", "+ 50%", "− 1/3 (− 50)"]
    for k, (cue, tit, v, col) in enumerate(vals):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 200, 270 + d, 400, 230, 26, "#FFFFFF", a, shadow=True)
        text(c, tit, x, 320 + d, 28, "black", col, a)
        text_mid(c, v, x, 410 + d, 110, "black", col, a)
        if k:
            arrow(c, x - 540 + 210, 385, x - 215, 385, col, a, 5, 18)
            pill(c, ops[k], x - 270, 560, col, size=28, a=a, anchor="center", bounds=(0, 1920))
    if ep(t, C["08.c"] + 1.6, 0.4) > 0:
        selo(c, 1500, 230, ep(t, C["08.c"] + 1.6, 0.4), "VOLTOU AO CUSTO", BLUE, -4, 30)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        K.atalho(c, 360, 640, 1200, 190, "ATALHO DE PROVA",
                 ["questão só com porcentagens?", "invente o custo 100"], ad, 36)


# ======================================================================
# bloco c — lucro em um, prejuízo em outro
# ======================================================================

def b_dois(c, t, C, B):
    head_seq(c, t, C, [("09", "LUCRO EM UM, PREJUÍZO NO OUTRO", "ACHE CADA CUSTO", PURPLE),
                       ("10", "O RESULTADO GLOBAL", "A SOMA DAS DUAS VENDAS", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    aa = ep(t, C["09.a"], 0.5)
    if sid == "09":
        produto(c, 620, 420, aa, "BICICLETA 1 · + 50%", "R$ 300,00", "custo: R$ 200,00", ep(t, C["09.b"] + 2.2, 0.5),
                col=GREEN, icone="bike", w=500)
        produto(c, 1300, 420, aa, "BICICLETA 2 · − 50%", "R$ 300,00", "custo: R$ 600,00", ep(t, C["09.b"] + 4.6, 0.5),
                col=RED, icone="bike", w=500)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            regra(c, "custo = preço ÷ fator", W / 2, 670, ab, 40, PURPLE)
            linha(c, [("300 ÷ 1,5 = ", INK2), ("200", GREEN), ("      ·      300 ÷ 0,5 = ", INK2), ("600", RED)],
                  W / 2, 780, 38, ep(t, C["09.b"] + 2.2, 0.5))
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        caixa(c, 480, 330, "CUSTOU", "R$ 800,00", PURPLE, aa, 400, sub="200 + 600")
        caixa(c, 480, 560, "VENDEU", "R$ 600,00", BLUE, ep(t, C["10.a"] + 1.2, 0.5), 400, sub="300 + 300")
        if ep(t, C["10.a"] + 2.4, 0.5) > 0:
            selo(c, 480, 760, ep(t, C["10.a"] + 2.4, 0.5), "PREJUÍZO DE R$ 200,00", RED, -3, 30)
    ab = ep(t, C["10.b"], 0.5)
    balanca(c, 1300, 300, ab, incl=ep(t, C["10.b"] + 0.5, 1.2), esq="+ R$ 100", dir_="− R$ 300")
    if ab > 0:
        text(c, "50% de 200", 1020, 600, 26, "bold", GREEN, ab)
        text(c, "50% de 600", 1580, 640, 26, "bold", RED, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        K.atalho(c, 920, 690, 760, 150, "ATALHO", ["mesmo preço e mesmo p%: SEMPRE prejuízo"], acc, 30)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("11", "SUA VEZ", "PAUSE E TENTE", GREEN), ("12", "VAMOS JUNTOS", "FATORES E REAIS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        for k, (L, v, col) in enumerate((("CUSTO", "R$ 40,00", BLUE), ("ETIQUETA", "+ 50% do custo", GREEN),
                                         ("LIQUIDAÇÃO", "− 30% da etiqueta", AMBER))):
            caixa(c, W / 2 + (k - 1) * 520, 300, L, v, col, aa, 460)
    ab = ep(t, C["11.b"], 0.5)
    if t < C["12"]:
        if ab > 0:
            text_mid(c, "lucro ou prejuízo? de quanto sobre o custo?", W / 2, 470, 40, "black", INK, ab)
        pause_timer(c, t, C["11.end"] - 1.9, W / 2, 640)
        return
    a1 = ep(t, C["12.a"], 0.5)
    if a1 > 0:
        pill(c, "FATORES", 300, 480, PURPLE, size=26, a=a1, anchor="center", bounds=(0, 1920))
        linha(c, [("1,5 · 0,7 = ", INK), ("1,05", PURPLE), ("  →  lucro de ", INK2), ("5%", GREEN)], 1020, 480, 48, a1)
    a2 = ep(t, C["12.b"], 0.5)
    if a2 > 0:
        pill(c, "EM REAIS", 300, 610, BLUE, size=26, a=a2, anchor="center", bounds=(0, 1920))
        linha(c, [("40 → 60 → 42", INK), ("   lucro: ", INK2), ("R$ 2,00", GREEN)], 1020, 610, 48, a2)
    a3 = ep(t, C["12.c"], 0.5)
    if a3 > 0:
        linha(c, [("2 ÷ 40 = ", INK), ("5%", GREEN)], 900, 740, 48, a3)
        conferido(c, "os dois batem", 1180, 752, ep(t, C["12.c"] + 1.6, 0.4), True, 36)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Leve tudo para a régua do custo e multiplique os fatores.",
          "Desconto menor pode anular margem maior.",
          "Lucro de p% e prejuízo de p% no mesmo preço dão prejuízo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["13", "23"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "13" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Lucro de p% e prejuízo de p% se anulam", "+ 20 − 20 dá zero",
          "os custos são diferentes: ache cada custo e compare os totais"),
         ("Subtrair: margem 60% − liquidação 30% = 30%", "os dois estão em por cento",
          "60% do CUSTO, 30% da ETIQUETA: bases diferentes · multiplique os fatores"),
         ("Ler o fator como lucro: 1,05 = 105%", "é só passar a vírgula",
          "o 1 é o próprio custo: lucro é o que passa de 1 → 5%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["14", "15", "16"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTS9 = [("A", "12%", "", GREEN), ("B", "30%", "60 − 30: bases diferentes", RED),
         ("C", "42%", "60 · 0,7: desconto só na margem", RED), ("D", "60%", "ignorou a liquidação", RED),
         ("E", "112%", "leu o fator 1,12", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · EU FAÇO", "MARGEM QUE SOBRA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["17.a"], 0.4)
    yend = _enunciado(c, "Uma loja compra um tênis por R$ 50,00 e o etiqueta com 60% de lucro sobre o custo. Na "
                      "liquidação, dá 30% de desconto sobre o preço da etiqueta. Na venda feita durante a liquidação, o "
                      "lucro da loja em relação ao custo é de", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["18"], 0.3)), align="left")
    cues_in = {L: C[f"17.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"19.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 250, 680, 42, C["18.ok"], "A", cues_in, cues_x, gap=40)
    if t < C["18"]:
        pause_timer(c, t, C["17.end"] - 1.9, 540, 720)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["18"], 0.4), shadow=True)
    pill(c, "RÉGUA DO CUSTO", 540, y0 + 44, PURPLE, size=24, a=ep(t, C["18.a"], 0.4), anchor="center")
    linha(c, [("1,6 · 0,7 = ", INK), ("1,12", PURPLE), (" → ", INK2), ("12%", GREEN)], 540, y0 + 110, 34,
          ep(t, C["18.b"], 0.4))
    linha(c, [("50 → 80 → 56", INK), ("  lucro R$ 6,00", INK2)], 540, y0 + 175, 30, ep(t, C["18.c"], 0.4))
    linha(c, [("6 ÷ 50 = ", INK), ("12%", GREEN)], 480, y0 + 235, 30, ep(t, C["18.c"] + 3.5, 0.4))
    conferido(c, "confere", 640, y0 + 245, ep(t, C["18.c"] + 4.2, 0.4), True, 28)


ALTS4 = [("A", "nem lucro nem prejuízo", "se anulam?", RED), ("B", "lucro de R$ 50,00", "sinal trocado", RED),
         ("C", "prejuízo de R$ 24,00", "600 · 0,96", RED), ("D", "prejuízo de R$ 48,00", "1.200 · 0,96", RED),
         ("E", "prejuízo de R$ 50,00", "", GREEN)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · VOCÊ FAZ", "LUCRO EM UM, PREJUÍZO NO OUTRO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    yend = _enunciado(c, "Um lojista vendeu dois aparelhos por R$ 600,00 cada. No primeiro, teve lucro de 20% sobre o "
                      "preço de custo; no segundo, prejuízo de 20% sobre o preço de custo. Considerando as duas vendas, "
                      "o lojista teve", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["21"], 0.3)), align="left")
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 36, C["21.ok"], "E", cues_in, cues_x, gap=34)
    if t < C["21"]:
        pause_timer(c, t, C["20.end"] - 2.4, 540, 720, dur=2.1)
        return
    y0 = yend + 4
    if t < C["22.c"]:
        rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["21"], 0.4), shadow=True)
        linha(c, [("600 ÷ 1,2 = ", INK), ("500", GREEN)], 540, y0 + 60, 32, ep(t, C["21.a"], 0.4))
        linha(c, [("600 ÷ 0,8 = ", INK), ("750", RED)], 540, y0 + 115, 32, ep(t, C["21.a"] + 2.6, 0.4))
        linha(c, [("custo 1.250  ·  venda 1.200", INK2)], 540, y0 + 180, 30, ep(t, C["21.b"], 0.4))
        linha(c, [("prejuízo de ", INK), ("R$ 50,00", RED)], 540, y0 + 245, 34, ep(t, C["21.c"], 0.4))
        return
    ac = ep(t, C["22.c"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, mix("#FFFFFF", AMBER, 0.12), ac, shadow=True)
    text(c, "1,2 · 0,8 = 0,96 só vale", 540, y0 + 80, 32, "black", AMBER, ac)
    text(c, "para UM produto reajustado", 540, y0 + 125, 32, "black", AMBER, ac)
    text(c, "duas vezes", 540, y0 + 170, 32, "black", AMBER, ac)
    text(c, "aqui são DOIS custos diferentes", 540, y0 + 240, 28, "bold", INK2, ac)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DO ASSUNTO", PURPLE)
    itens = [("24.a", "juntamos tudo", "base · fatores · régua do custo"),
             ("24.b", "caçamos as pegadinhas", "soma de % · base trocada · empate"),
             ("24.c", "treinamos com inéditas", "no formato do ENEM")]
    for k, (cue, s, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 300 + d, 480, 300, 24, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x + 240, 370 + d, a, 34, bg=PURPLE)
        text(c, s, x + 240, 480 + d, 34 if len(s) < 24 else 28, "black", INK, a)
        text(c, sub, x + 240, 540 + d, 24, "bold", GRAY, a)
    pill(c, "ep. 4 · revisão", W / 2, 760, PURPLE, size=30, a=ep(t, C["24.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["25.like"], C["25.sub"], C["25.bell"], C["25.com"], C["25.bye"],
        "Etiqueta com 100% de lucro e liquidação de 50%: sobra lucro?", canal="no Estudativo", anki=C["25.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, regua=b_regua, cem=b_cem,
              dois=b_dois, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q9=b_q9, q4=b_q4, ponte=b_ponte,
              cta=b_cta)
