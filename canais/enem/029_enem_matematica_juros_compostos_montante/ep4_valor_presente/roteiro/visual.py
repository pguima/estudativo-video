"""Visual — Juros Compostos, Episódio 4: trazendo valores para hoje (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho...).
Peças deste episódio: linha_tempo() (HOJE ↔ DAQUI A 2 ANOS, seta para a direita "× fator" e para a esquerda "÷ fator";
o caminho errado "× 0,95 × 0,95" chega a um ponto abaixo do certo, em vermelho), filme() (o FILME AO CONTRÁRIO:
fita com setas ▶ e ◀), linha().
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
_s = importlib.util.spec_from_file_location("comum029", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_compostos_ep4_valor_presente.mp4"
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
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - 70, w, 140, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - 70, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - 37, 24, "black", col, a)
    fmid(c, val, cx, cy + 28, 40 if ftext_w(val, "black", 40) < w - 30 else 32, "black", INK, a)
    if sub:
        text(c, sub, cx, cy + 104, 24, "bold", GRAY, a)


def linha_tempo(c, t, y, a, hoje, futuro, fator, ida=0.0, volta=0.0, errado=None, ae=0.0, x0=420, x1=1500,
                rot_fut="DAQUI A 2 ANOS"):
    """HOJE ↔ FUTURO: seta de cima para a direita (× fator), de baixo para a esquerda (÷ fator).
    errado = (rótulo, valor) → caminho vermelho que chega abaixo do certo."""
    if a <= 0:
        return
    line(c, x0, y, x1, y, INK2, a, 5)
    for x, rot in ((x0, "HOJE"), (x1, rot_fut)):
        c.drawCircle(x, y, 14, paint(INK2, a))
        text(c, rot, x, y + 56, 26, "black", GRAY, a)
    caixa(c, x0, y - 170, "VALOR PRESENTE", hoje, BLUE, a, 330)
    caixa(c, x1, y - 170, "VALOR FUTURO", futuro, PURPLE, a, 330)
    xm0, xm1 = x0 + 200, x1 - 200
    if ida > 0:
        u = ease_io(clamp(ida))
        arrow(c, xm0, y - 200, xm0 + (xm1 - xm0) * u, y - 200, GREEN, a, 6, 20)
        pill(c, "× " + fator, (xm0 + xm1) / 2, y - 250, GREEN, size=30, a=a * clamp(ida * 2 - 1), anchor="center",
             bounds=(0, 1920))
    if volta > 0:
        u = ease_io(clamp(volta))
        arrow(c, xm1, y - 120, xm1 - (xm1 - xm0) * u, y - 120, PURPLE, a, 6, 20)
        pill(c, "÷ " + fator, (xm0 + xm1) / 2, y - 70, PURPLE, size=30, a=a * clamp(volta * 2 - 1), anchor="center",
             bounds=(0, 1920))
    if errado and ae > 0:
        rot, val = errado
        u = ease_io(clamp(ae))
        xe = x0 + 40
        pts = [(x1, y + 20), ((x0 + x1) / 2, y + 130), (xe, y + 200)]
        k = 1 if u < 0.5 else 2
        uu = u * 2 if u < 0.5 else u * 2 - 1
        line(c, pts[0][0], pts[0][1], pts[0][0] + (pts[1][0] - pts[0][0]) * (uu if k == 1 else 1),
             pts[0][1] + (pts[1][1] - pts[0][1]) * (uu if k == 1 else 1), RED, a, 5)
        if k == 2:
            arrow(c, pts[1][0], pts[1][1], pts[1][0] + (pts[2][0] - pts[1][0]) * uu,
                  pts[1][1] + (pts[2][1] - pts[1][1]) * uu, RED, a, 5, 18)
        pill(c, rot, (x0 + x1) / 2 + 40, y + 110, RED, size=26, a=a * clamp(ae * 2 - 0.6), anchor="center",
             bounds=(0, 1920))
        if u >= 0.99:
            rrect(c, xe - 170, y + 210, 340, 90, 18, mix("#FFFFFF", RED, 0.08), a)
            fmid(c, val, xe, y + 255, 34, "black", RED, a)


def filme(c, cx, cy, a, sentido=1, w=620, h=170):
    """fita de filme com quadros; sentido 1 = ▶ (futuro), -1 = ◀ (de volta para hoje)"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 16, "#2B2F3A", a)
    for k in range(12):
        x = cx - w / 2 + 20 + k * (w - 40) / 11
        rrect(c, x - 9, cy - h / 2 + 10, 18, 14, 3, "#FFFFFF", a * 0.8)
        rrect(c, x - 9, cy + h / 2 - 24, 18, 14, 3, "#FFFFFF", a * 0.8)
    col = GREEN if sentido > 0 else PURPLE
    for k in range(3):
        x = cx - w / 3 + k * w / 3
        rrect(c, x - 80, cy - 45, 160, 90, 10, mix("#FFFFFF", col, 0.25), a)
        tri = skia.Path()
        s = 26 * sentido
        tri.moveTo(x - s * 0.6, cy - 24); tri.lineTo(x + s * 0.8, cy); tri.lineTo(x - s * 0.6, cy + 24); tri.close()
        c.drawPath(tri, paint(col, a))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS COMPOSTOS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 200, 1320, 110, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("R$ 11.025,00", PURPLE), (" em 2 anos  ·  ", INK2), ("5% a.a.", PURPLE), ("  ·  hoje: ", INK2),
                  ("?", AMBER)], W / 2, 255, 50, aa)
    linha_tempo(c, t, 590, aa, "?", "R$ 11.025,00", "1,1025", rot_fut="DAQUI A 2 ANOS",
                errado=("− 5% − 5%", "R$ 9.950,06"), ae=ep(t, C["01.b"], 1.2))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1180, 740, 560, 110, 24, mix("#FFFFFF", GREEN, 0.12), acc, shadow=True)
        linha(c, [("certo: ", INK2), ("R$ 10.000,00", GREEN)], 1460, 795, 44, acc)
    if ep(t, C["01.b"] + 2.5, 0.4) > 0:
        selo(c, 820, 850, ep(t, C["01.b"] + 2.5, 0.4), "FICA DEVENDO", RED, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    if aa > 0:
        linha_tempo(c, t, 580, aa, "hoje", "futuro", "fator", volta=ep(t, C["02.a"] + 0.6, 1.0), rot_fut="FUTURO")
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        regra(c, "qualquer valor do futuro → hoje, com UMA divisão", W / 2, 760, ab, 42, GREEN)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 280 + d1, 720, 420, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "EP. 1", 560, 330 + d1, GREEN, size=26, a=a1, anchor="center", bounds=(0, 1920))
        K.mdraw(c, "M = C · (1+i)^{t}", 560, 470 + d1, 66, INK, a1, align="center")
        text(c, "o fator multiplica a cada período", 560, 600 + d1, 28, "bold", GRAY, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 420, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "PORCENTAGEM", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        text(c, "voltar ao valor original:", 1360, 420 + d2, 30, "bold", INK2, a2)
        text(c, "DIVIDA PELO FATOR", 1360, 480 + d2, 40, "black", PURPLE, a2)
        linha(c, [("R$ 125,00 ÷ 1,25 = ", INK), ("R$ 100,00", GREEN)], 1360, 600 + d2, 44, ep(t, C["03.b"] + 3.0, 0.4))


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "A FAMÍLIA E O CARRO", "QUANTO DEPOSITAR HOJE?", BLUE),
                       ("05", "DOIS NOMES", "PRESENTE × FUTURO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        if aa > 0:
            linha_tempo(c, t, 580, aa, "? hoje", "o carro novo", "?", rot_fut="DAQUI A 2 ANOS")
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            selo(c, 420, 280, ab, "QUANTO DEPOSITAR?", AMBER, -3, 34)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            regra(c, "a conta do episódio 1… AO CONTRÁRIO", W / 2, 760, acc, 40, PURPLE)
        return
    defs = [("05.a", "VALOR FUTURO", "quanto vale LÁ NA FRENTE", "= o montante M", PURPLE),
            ("05.b", "VALOR PRESENTE", "quanto vale HOJE", "= o capital C", BLUE),
            ("05.c", "TRAZER PARA HOJE", "achar o presente a partir do futuro", "", BLUE)]
    for k, (cue, nome, sig, eq, col) in enumerate(defs):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 170 + d
        rrect(c, 260, y, 1400, 140, 22, mix("#FFFFFF", BLUE, 0.06), a)
        text(c, nome, 300, y + 62, 40, "black", col, a, align="left")
        text(c, sig, 300, y + 112, 30, "bold", INK2, a, align="left")
        if eq:
            text(c, eq, 1620, y + 86, 38, "black", col, a, align="right")


# ======================================================================
# bloco a — a fórmula (o filme ao contrário)
# ======================================================================

def b_formula(c, t, C, B):
    head(c, t, B["start"], "O FILME AO CONTRÁRIO", "VALOR PRESENTE", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        filme(c, 620, 300, aa, 1)
        text(c, "para o FUTURO:  × fator", 1300, 315, 40, "black", GREEN, aa, align="left")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        filme(c, 620, 490, ab, -1)
        text(c, "para HOJE:  ÷ fator", 1300, 505, 40, "black", PURPLE, ab, align="left")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 620, 1000, 170, 26, mix("#FFFFFF", PURPLE, 0.10), acc, shadow=True)
        K.mdraw(c, "C = M/(1+i)^{t}", W / 2, 705, 64, PURPLE, acc, align="center")


# ======================================================================
# bloco b — o exemplo do material
# ======================================================================

def b_exemplo(c, t, C, B):
    head(c, t, B["start"], "O EXEMPLO", "PRIMEIRO O FATOR", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["07.a"], 0.5)
    for k, (L, v, col) in enumerate((("M", "R$ 11.025,00", PURPLE), ("i", "5% a.a.", AMBER), ("t", "2 anos", BLUE))):
        caixa(c, 520 + k * 440, 330, L, v, col, a0, 380)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        pill(c, "1º  o fator", 420, 530, PURPLE, size=28, a=ab, anchor="center", bounds=(0, 1920))
        linha(c, [("1,05² = ", INK), ("1,1025", PURPLE)], 1060, 530, 54, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "2º  a divisão", 420, 680, PURPLE, size=28, a=acc, anchor="center", bounds=(0, 1920))
        linha(c, [("11.025 ÷ 1,1025 = ", INK), ("R$ 10.000,00", GREEN)], 1060, 680, 54, acc)


# ======================================================================
# bloco c — tirar 5% não desfaz
# ======================================================================

def b_desfaz(c, t, C, B):
    head_seq(c, t, C, [("08", "TIRAR 5% DUAS VEZES?", "O CAMINHO ERRADO", AMBER),
                       ("09", "POR QUE NÃO VOLTA?", "TIRAR 10% NÃO DESFAZ 10%", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        linha_tempo(c, t, 560, aa, "R$ 10.000,00", "R$ 11.025,00", "1,1025", volta=1.0,
                    errado=("× 0,95 × 0,95", "R$ 9.950,06"), ae=ep(t, C["08.a"] + 0.5, 1.4))
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            selo(c, 1400, 760, ab, "FICARIA DEVENDO", RED, -3, 36)
        return
    for k, (cue, val, op, col) in enumerate((("09.a", "R$ 100,00", "", INK), ("09.a", "R$ 110,00", "+ 10%", GREEN),
                                             ("09.b", "R$ 99,00", "− 10%", RED))):
        a = ep(t, C[cue] + (0.8 if k == 1 else 0), 0.5)
        if a <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 200, 290, 400, 170, 24, "#FFFFFF", a, shadow=True)
        fmid(c, val, x, 375, 56, "black", col, a)
        if op:
            arrow(c, x - 500 + 210, 375, x - 215, 375, col, a, 5, 18)
            pill(c, op, x - 270, 320, col, size=28, a=a, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["09.b"] + 1.6, 0.4)
    if ab > 0:
        selo(c, 1500, 520, ab, "NÃO VOLTA PARA 100!", RED, -4, 30)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 600, 1320, 200, 24, mix("#FFFFFF", AMBER, 0.12), acc)
        text(c, "o desconto incide sobre um valor MAIOR", W / 2, 680, 42, "black", INK, acc)
        linha(c, [("só ", INK2), ("÷ 1,10", PURPLE), (" desfaz:  110 ÷ 1,1 = ", INK2), ("100", GREEN)], W / 2, 750, 40, acc)


# ======================================================================
# bloco d — a conferência
# ======================================================================

def b_confere(c, t, C, B):
    head(c, t, B["start"], "A CONFERÊNCIA", "MULTIPLIQUE DE VOLTA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 250, 1400, 130, 24, mix("#FFFFFF", BLUE, 0.07), aa)
        linha(c, [("hoje ", BLUE), ("<", INK), (" amanhã", PURPLE), ("   ·   saiu maior? você multiplicou", RED)],
              W / 2, 315, 40, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("10.000 × 1,1025 = ", INK), ("11.025", PURPLE)], W / 2, 490, 58, ab)
        conferido(c, "bateu", 1520, 505, ep(t, C["10.b"] + 3.0, 0.4), True, 36)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 600, 1200, 200, "ATALHO DE PROVA",
                 ["multiplique as alternativas pelo fator:", "a que vira o valor futuro é a certa"], acc, 34)


# ======================================================================
# bloco e — para que serve
# ======================================================================

def b_serve(c, t, C, B):
    head(c, t, B["start"], "PARA QUE SERVE?", "DATAS DIFERENTES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        caixa(c, 620, 380, "HOJE", "R$ 1.000,00", BLUE, aa, 420)
        caixa(c, 1300, 380, "DAQUI A 1 ANO", "R$ 1.000,00", PURPLE, aa, 420)
        text_mid(c, "≠", W / 2 + 0, 380, 110, "black", RED, ep(t, C["11.a"] + 2.5, 0.4))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        regra(c, "traga tudo para HOJE: a comparação fica justa", W / 2, 590, ab, 40, PURPLE)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        pill(c, "série: Empréstimos e financiamentos", 640, 760, BLUE, size=28, a=acc, anchor="center",
             bounds=(0, 1920))
        pill(c, "série: Comparação de propostas", 1300, 760, BLUE, size=28, a=ep(t, C["11.c"] + 1.2, 0.4),
             anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ", "PAUSE E TENTE", GREEN), ("13", "VAMOS JUNTOS", "FATOR, DIVISÃO, CONFERÊNCIA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        for k, (L, v, col) in enumerate((("VALOR FUTURO", "R$ 4.840,00", PURPLE), ("TAXA", "10% a.a.", AMBER),
                                         ("TEMPO", "2 anos", BLUE), ("HOJE", "?", GREEN))):
            caixa(c, W / 2 + (k - 1.5) * 400, 300, L, v, col, aa, 360)
    if t < C["13"]:
        pause_timer(c, t, C["12.end"] - 1.9, W / 2, 620)
        return
    linha(c, [("fator: 1,1² = ", INK), ("1,21", PURPLE)], W / 2, 470, 50, ep(t, C["13.a"], 0.4))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("4.840 ÷ 1,21 = ", INK), ("R$ 4.000,00", GREEN)], 640, 580, 50, ab)
        K.atalho(c, 1110, 520, 640, 130, "ATALHO", ["÷ 121 = 40  →  × 100"], ep(t, C["13.b"] + 3.0, 0.4), 32)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        linha(c, [("4.000 × 1,21 = 4.840", INK2)], W / 2, 740, 44, acc)
        conferido(c, "confere", 1360, 755, ep(t, C["13.c"] + 2.5, 0.4), True, 34)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Para o futuro, multiplique; para hoje, divida pelo mesmo fator.",
          "Tirar 10% não desfaz um aumento de 10%.",
          "Confira multiplicando de volta."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "22"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Tirar 5% a cada ano", "o dinheiro cresceu 5% por ano",
          "o desconto incide sobre um valor maior: R$ 9.950,06 · divida pelo fator"),
         ("Dividir pelo fator SIMPLES (1,10)", "5% + 5% = 10%",
          "juros compostos: fator 1,1025 · com 1,10 sai ≈ R$ 10.022,73"),
         ("Trazer só UM período (÷ 1,05)", "dividir já parece voltar no tempo",
          "são 2 anos: expoente 2 · com 1 ano sai R$ 10.500,00"),
         ("MULTIPLICAR pelo fator", "é a fórmula que você decorou",
          "multiplicar leva ao futuro: ≈ R$ 12.155,06 > valor futuro · impossível")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16", "17", "18"], ERROS)


# ======================================================================
# questão 3
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTS3 = [("A", "R$ 10.000,00", "", GREEN), ("B", "R$ 10.083,33", "÷ 1,20 (fator simples)", RED),
         ("C", "R$ 10.890,00", "tirou 10% uma vez", RED), ("D", "R$ 11.000,00", "só um ano (÷ 1,1)", RED),
         ("E", "R$ 14.641,00", "multiplicou pelo fator", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "QUANTO APLICAR HOJE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["19.a"], 0.4)
    yend = _enunciado(c, "Uma família quer ter R$ 12.100,00 daqui a 2 anos para trocar de carro. Ela encontrou uma "
                      "aplicação que rende juros compostos de 10% ao ano. O valor que deve ser aplicado hoje, em um "
                      "único depósito, é de", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["20"], 0.3)), align="left")
    cues_in = {L: C[f"19.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"21.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 42, C["20.ok"], "A", cues_in, cues_x, gap=34)
    if t < C["20"]:
        pause_timer(c, t, C["19.end"] - 1.9, 540, 720)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["20"], 0.4), shadow=True)
    pill(c, "VALOR PRESENTE: ÷ fator", 540, y0 + 46, PURPLE, size=24, a=ep(t, C["20.a"], 0.4), anchor="center")
    linha(c, [("fator: 1,1² = ", INK), ("1,21", PURPLE)], 540, y0 + 115, 32, ep(t, C["20.b"], 0.4))
    linha(c, [("12.100 ÷ 1,21 = ", INK), ("R$ 10.000,00", GREEN)], 540, y0 + 180, 32, ep(t, C["20.c"], 0.4))
    linha(c, [("10.000 × 1,21 = 12.100", INK2)], 540, y0 + 245, 28, ep(t, C["20.d"], 0.4))
    conferido(c, "confere", 430, y0 + 300, ep(t, C["20.d"] + 2.0, 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DE JUROS COMPOSTOS", PURPLE)
    itens = [("23.a", "juntamos tudo", "fator · expoente · valor presente"),
             ("23.b", "caçamos as pegadinhas", "soma de taxas · ÷ fator · simples"),
             ("23.c", "treinamos no formato do ENEM", "questões inéditas")]
    for k, (cue, s, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 300 + d, 480, 300, 24, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x + 240, 370 + d, a, 34, bg=PURPLE)
        text(c, s, x + 240, 480 + d, 34 if len(s) < 24 else 28, "black", INK, a)
        text(c, sub, x + 240, 540 + d, 24, "bold", GRAY, a)
    pill(c, "ep. 5 · revisão", W / 2, 760, PURPLE, size=30, a=ep(t, C["23.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["24.like"], C["24.sub"], C["24.bell"], C["24.com"], C["24.bye"],
        "Para ter R$ 1.000 daqui a 1 ano, a 10%, quanto aplicar hoje?", canal="no Estudativo", anki=C["24.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, formula=b_formula,
              exemplo=b_exemplo, desfaz=b_desfaz, confere=b_confere, serve=b_serve, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, ponte=b_ponte, cta=b_cta)
