"""Visual — Velocidade, Densidade e Vazão, Episódio 3: a armadilha da média (ida a 60, volta a 40, média 48) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: barra_tempo() (blocos de 1 hora), balanca() (o lado com mais horas pesa mais), carro(), estrada()
(ida e volta pelo mesmo caminho), linha().
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
_s = importlib.util.spec_from_file_location("comum027", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_velocidade_ep3_armadilha_media.mp4"
CARD_R = K.CARD_R
IDA = BLUE      # trecho rápido (60 km/h)
VOLTA = AMBER   # trecho lento (40 km/h)


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


def barra_tempo(c, x, y, n, col, a, prog=1.0, bw=150, bh=84, rotulo=None, size=30):
    """barra de tempo: n blocos de 1 hora, aparecendo um a um conforme prog (0..1)"""
    if a <= 0:
        return
    if rotulo:
        text(c, rotulo, x, y - 18, 28, "black", col, a, align="left")
    for k in range(n):
        ak = a * max(0.0, min(1.0, prog * n - k))
        if ak <= 0:
            continue
        xx = x + k * (bw + 10)
        rrect(c, xx, y, bw, bh, 14, col, ak * 0.9)
        text_mid(c, "1 h", xx + bw / 2, y + bh / 2, size, "black", "#FFFFFF", ak)


def blocos(c, cx, base, n, col, a, s=56):
    """pilha de blocos de 1 h (para os pratos da balança), em fileiras de 3"""
    for k in range(n):
        row, colk = divmod(k, 3)
        m = min(3, n - row * 3)
        x = cx - m * (s + 6) / 2 + colk * (s + 6)
        y = base - (row + 1) * (s + 6)
        rrect(c, x, y, s, s, 10, col, a * 0.9)
        text_mid(c, "1h", x + s / 2, y + s / 2, 22, "black", "#FFFFFF", a)


def balanca(c, cx, cy, a, tilt, nl, nr, lab_l, lab_r, col_l=IDA, col_r=VOLTA, half=330):
    """balança de pratos: tilt > 0 abaixa o lado direito. Pratos com nl e nr blocos de 1 h."""
    if a <= 0:
        return
    ang = math.radians(9 * tilt)
    # coluna e base
    rrect(c, cx - 12, cy, 24, 230, 8, INK2, a)
    rrect(c, cx - 120, cy + 222, 240, 26, 10, INK2, a)
    c.drawCircle(cx, cy, 18, paint(INK, a))
    ends = []
    for sgn in (-1, 1):
        ex = cx + sgn * half * math.cos(ang)
        ey = cy + sgn * half * math.sin(ang)
        ends.append((ex, ey))
    line(c, ends[0][0], ends[0][1], ends[1][0], ends[1][1], INK, a, 12)
    for (ex, ey), n, lab, col in ((ends[0], nl, lab_l, col_l), (ends[1], nr, lab_r, col_r)):
        pan_y = ey + 190
        line(c, ex, ey, ex - 110, pan_y, GRAY, a, 3)
        line(c, ex, ey, ex + 110, pan_y, GRAY, a, 3)
        rrect(c, ex - 130, pan_y, 260, 18, 9, INK2, a)
        blocos(c, ex, pan_y, n, col, a)
        text(c, lab, ex, pan_y + 70, 34, "black", col, a)


def carro(c, cx, cy, s, a, col=BLUE, para_esq=False):
    if a <= 0:
        return
    sg = -1 if para_esq else 1
    rrect(c, cx - 60 * s, cy - 22 * s, 120 * s, 36 * s, 14 * s, col, a)
    rrect(c, cx - (30 if not para_esq else 26) * s + sg * 4 * s, cy - 46 * s, 56 * s, 30 * s, 12 * s, col, a)
    for dx in (-34, 34):
        c.drawCircle(cx + dx * s, cy + 16 * s, 13 * s, paint(INK, a))
        c.drawCircle(cx + dx * s, cy + 16 * s, 5 * s, paint("#FFFFFF", a))


def estrada(c, x0, x1, y, a, prog_ida=1.0, prog_volta=0.0, vi="60 km/h", vv="40 km/h", cidades=("A", "B")):
    """ida (em cima, para a direita) e volta (embaixo, para a esquerda) pelo mesmo caminho"""
    if a <= 0:
        return
    rrect(c, x0, y - 50, x1 - x0, 100, 50, "#E4E4E0", a)
    line(c, x0 + 60, y, x1 - 60, y, "#FFFFFF", a, 5, dash=(26, 20))
    for x, nome in ((x0, cidades[0]), (x1, cidades[1])):
        c.drawCircle(x, y, 40, paint("#FFFFFF", a))
        c.drawCircle(x, y, 32, paint(INK, a))
        text_mid(c, nome, x, y, 34, "black", "#FFFFFF", a)
    if prog_ida > 0:
        xi = lerp(x0 + 90, x1 - 90, prog_ida)
        carro(c, xi, y - 24, 0.6, a, IDA)
        pill(c, "ida: " + vi, (x0 + x1) / 2, y - 100, IDA, size=28, a=a, anchor="center")
    if prog_volta > 0:
        xv = lerp(x1 - 90, x0 + 90, prog_volta)
        carro(c, xv, y + 30, 0.6, a, VOLTA, para_esq=True)
        pill(c, "volta: " + vv, (x0 + x1) / 2, y + 100, VOLTA, size=28, a=a, anchor="center")


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


ENUNCIADO = ("Um motorista percorre o trajeto de ida entre duas cidades a uma velocidade média de 60 km/h e faz o "
             "trajeto de volta, pelo mesmo caminho, a 40 km/h. A velocidade média do percurso completo, de ida e volta, é de")
ALTS = [("A", "44 km/h", "não sai de raciocínio certo", RED), ("B", "46 km/h", "não sai de raciocínio certo", RED),
        ("C", "48 km/h", "", GREEN), ("D", "50 km/h", "média simples: a pegadinha", AMBER),
        ("E", "52 km/h", "impossível: acima da média simples", RED)]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "VELOCIDADE, DENSIDADE E VAZÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["01.a"], 0.4)
    _enunciado(c, [(ENUNCIADO, INK)], a0, 250, 30)
    estrada(c, 220, 860, 690, a0, ep(t, C["01.a"] + 0.5, 2.0), ep(t, C["01.a"] + 3.0, 2.5))
    cues_in = {L: C[f"01.q{L.lower()}"] for L in "ABCDE"}
    K.alternativas(c, t, C, ALTS, 1000, 260, 680, 44, 1e9, "C", cues_in, None, gap=34)
    pause_timer(c, t, C["01.end"] - 1.9, 1600, 785)
    ap = ep(t, C["01.p"], 0.4)
    if ap > 0:
        pill(c, "PAUSE · MARQUE · GUARDE", 1250, 785, PURPLE, size=30, a=ap, anchor="center")


def b_hook2(c, t, C, B):
    head(c, t, B["start"], "VOCÊ MARCOU 50?", "", AMBER)
    aa = ep(t, C["02.a"], 0.5)
    if aa > 0:
        text(c, "50 km/h", W / 2, 520, 220, "black", INK, aa)
        text(c, "a resposta da maioria", W / 2, 620, 40, "bold", GRAY, aa)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        selo(c, W / 2 + 520, 300, ab, "PEGADINHA", AMBER, -8, 50)
        pill(c, "e a maioria ERRA", W / 2, 760, RED, size=44, a=ab, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("03.a", "saber por que a resposta é 48 km/h", "e não 50 km/h"),
            ("03.b", "calcular de dois jeitos", "distância amiga · média harmônica"),
            ("03.c", "reconhecer quando a média simples funciona", "tempos iguais")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "VELOCIDADE MÉDIA", 560, 290, 34, "black", BLUE, aa)
        text(c, "episódio 2", 560, 340, 26, "bold", GRAY, aa)
        fr(c, "distância total", "tempo total", 560, 500, 54, INK, aa, num_col=BLUE, den_col=AMBER)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        text(c, "ACHAR O TEMPO", 1370, 290, 34, "black", PURPLE, ab)
        text(c, "episódio 1", 1370, 340, 26, "bold", GRAY, ab)
        fr(c, "distância", "velocidade", 1370, 480, 54, INK, ab)
        linha(c, [("120 km ÷ 60 km/h = ", INK), ("2 h", GREEN)], 1370, 650, 44, ep(t, C["04.b"] + 4.5, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "O MESMO CAMINHO", "DUAS VEZES POR DIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "MANHÃ · trânsito livre", 220, 300, 40, "black", IDA, aa, align="left")
        barra_tempo(c, 220, 340, 1, IDA, aa, ep(t, C["05.a"] + 0.4, 0.8), bw=220)
        text(c, "chega rapidinho", 480, 395, 32, "bold", GRAY, aa, align="left")
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        text(c, "TARDE · congestionamento", 220, 520, 40, "black", VOLTA, ab, align="left")
        barra_tempo(c, 220, 560, 3, VOLTA, ab, ep(t, C["05.b"] + 0.4, 2.0), bw=220)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        pergunta(c, "onde você passa MAIS TEMPO?", W / 2, 730, acc, PURPLE, 40)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1480, 600, ad, "NO LENTO", AMBER, -6, 48)


# ======================================================================
# bloco a: a resposta instintiva
# ======================================================================

def b_instinto(c, t, C, B):
    head(c, t, B["start"], "DE ONDE VEM O 50?", "A RESPOSTA INSTINTIVA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 230, 1320, 120, BLUE, aa)
        linha(c, [("MÉDIA SIMPLES", BLUE), ("  =  soma dos valores ÷ quantidade", INK)], W / 2, 290, 44, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        fr(c, "60 + 40", "2", 660, 500, 80, INK, ab)
        linha(c, [("= ", INK), ("50 km/h", AMBER)], 1160, 480, 80, ep(t, C["06.b"] + 2.4, 0.4))
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        selo(c, 1560, 395, acc, "PEGADINHA", AMBER, -8, 40)
        pill(c, "parece certo: fica bem no meio", W / 2, 650, AMBER, size=32, a=acc, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        linha(c, [("média das velocidades  ", RED), ("≠", INK), ("  velocidade média", GREEN)], W / 2, 770, 46, ad)


# ======================================================================
# bloco b: a distância amiga
# ======================================================================

def b_amiga(c, t, C, B):
    head_seq(c, t, C, [("07", "A DISTÂNCIA AMIGA", "INVENTE UM NÚMERO", GREEN),
                       ("08", "A CONTA DE CABEÇA", "DISTÂNCIA TOTAL ÷ TEMPO TOTAL", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0 and t < C["08"]:
        pill(c, "um número que 60 e 40 dividem certinho", W / 2, 280, GREEN, size=36, a=aa, anchor="center")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0 and t < C["08"]:
        linha(c, [("120 ÷ 60 = 2  ✓", INK), ("     ", INK), ("120 ÷ 40 = 3  ✓", INK)], W / 2, 420, 52, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        y = 600 if t < C["08"] else 300
        estrada(c, 360, 1560, y, acc, 1.0, 1.0 if t >= C["08"] else ep(t, C["07.c"] + 0.6, 1.4),
                vi="60 km/h", vv="40 km/h")
        text(c, "120 km", 960, y + 18, 34, "black", INK, acc)
    if t < C["08"]:
        return
    a1 = ep(t, C["08.a"], 0.5)
    if a1 > 0:
        linha(c, [("ida: 120 km ÷ 60 km/h = ", INK), ("2 h", IDA)], 620, 520, 40, a1)
        barra_tempo(c, 1060, 480, 2, IDA, a1, ep(t, C["08.a"] + 0.6, 0.8), bw=120, bh=76, size=26)
    a2 = ep(t, C["08.b"], 0.5)
    if a2 > 0:
        linha(c, [("volta: 120 km ÷ 40 km/h = ", INK), ("3 h", VOLTA)], 620, 630, 40, a2)
        barra_tempo(c, 1060, 590, 3, VOLTA, a2, ep(t, C["08.b"] + 0.6, 1.0), bw=120, bh=76, size=26)
    a3 = ep(t, C["08.c"], 0.5)
    if a3 > 0:
        linha(c, [("total: 240 km em 5 h", INK)], 620, 750, 40, a3)
    a4 = ep(t, C["08.d"], 0.5)
    if a4 > 0:
        rrect(c, 1100, 700, 520, 110, 22, GREEN, 0.14 * a4)
        linha(c, [("240 ÷ 5 = ", INK), ("48 km/h", GREEN)], 1360, 755, 48, a4)


def b_atalho_amiga(c, t, C, B):
    head(c, t, B["start"], "OUTRA DISTÂNCIA?", "O MESMO RESULTADO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        linha(c, [("240 km: ", INK), ("4 h", IDA), (" + ", INK), ("6 h", VOLTA), ("  →  480 km ÷ 10 h = ", INK),
                  ("48 km/h", GREEN)], W / 2, 310, 46, aa)
        conferido(c, "sempre 48", 820, 410, ep(t, C["09.a"] + 3.0, 0.4), True, 34)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        K.atalho(c, 300, 500, 1320, 290, "ATALHO · ESCOLHER A DISTÂNCIA AMIGA",
                 ["o PRODUTO sempre serve: 60 × 40 = 2 400 km",
                  "o MMC dá a menor: MMC(60, 40) = 120 km"], ab, 40)
        if ep(t, C["09.c"], 0.4) > 0:
            pill(c, "série de MMC", 1560, 760, GREEN, size=24, a=ep(t, C["09.c"], 0.4), anchor="right")


# ======================================================================
# bloco c: quem manda na média é o relógio
# ======================================================================

def b_relogio(c, t, C, B):
    sid = which(t, C, ["10", "11", "12"])
    head_seq(c, t, C, [("10", "MAS POR QUE MENOS?", "OLHE O RELÓGIO", BLUE),
                       ("11", "O PESO NA MÉDIA", "QUEM DÁ O PESO É O TEMPO", PURPLE),
                       ("12", "SEMPRE ABAIXO", "NUNCA ACIMA", PURPLE)])
    card(c, *CARD_R)
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        barra_tempo(c, 420, 330, 2, IDA, aa, ep(t, C["10.a"] + 0.6, 1.0), bw=200, bh=100, rotulo="IDA · 60 km/h · 120 km",
                    size=36)
        ab = ep(t, C["10.b"], 0.5)
        barra_tempo(c, 420, 540, 3, VOLTA, ab, ep(t, C["10.b"] + 0.4, 1.4), bw=200, bh=100,
                    rotulo="VOLTA · 40 km/h · 120 km", size=36)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            linha(c, [("distâncias ", INK), ("IGUAIS", GREEN), ("   ·   tempos ", INK), ("DIFERENTES", RED)],
                  W / 2, 760, 44, acc)
        return
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 225, 1320, 90, BLUE, aa)
            linha(c, [("PESO", BLUE), (" de um valor na média = o quanto ele conta no resultado", INK)], W / 2, 270, 34, aa)
        ab = ep(t, C["11.b"], 0.5)
        tilt = ep(t, C["11.b"] + 1.0, 1.4)
        balanca(c, W / 2, 400, ab, tilt, 2, 3, "60 km/h · 2 h", "40 km/h · 3 h")
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            g = ep(t, C["11.c"] + 1.6, 1.2)
            v = 50 - 2 * g
            text(c, "média", 360, 420, 34, "bold", GRAY, acc)
            text(c, f"{v:.0f} km/h" if g in (0, 1) else f"{v:.1f}".replace(".", ",") + " km/h", 360, 500, 64, "black",
                 GREEN if g >= 1 else AMBER, acc)
            arrow = ep(t, C["11.c"] + 1.6, 0.4)
            if arrow > 0:
                text(c, "↓", 360, 580, 60, "black", AMBER, arrow * (1 - g))
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            regra(c, "QUEM MANDA NA MÉDIA É O RELÓGIO", W / 2, 800, ad, 40, PURPLE)
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        pill(c, "distâncias iguais → o trecho lento SEMPRE dura mais", W / 2, 290, PURPLE, size=34, a=aa, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        x0, x1, y = 360, 1560, 520
        line(c, x0, y, x1, y, INK2, ab, 5)
        for v in range(40, 61, 2):
            x = lerp(x0, x1, (v - 40) / 20)
            line(c, x, y - 14, x, y + 14, INK2, ab, 3)
        for v, col, lab in ((40, VOLTA, "40"), (60, IDA, "60"), (50, AMBER, "50 média simples")):
            x = lerp(x0, x1, (v - 40) / 20)
            text(c, lab, x, y + 66, 32, "black", col, ab)
        x48 = lerp(x0, x1, 8 / 20)
        c.drawCircle(x48, y, 20, paint(GREEN, ab))
        text(c, "48", x48, y - 40, 40, "black", GREEN, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        x0, x1 = 360, 1560
        xa, xb = lerp(x0, x1, 0), lerp(x0, x1, 0.5)
        rrect(c, xa, 490, xb - xa, 60, 30, GREEN, 0.18 * acc)
        K.atalho(c, 380, 650, 1160, 150, "CONFERÊNCIA", ["a resposta fica ENTRE a menor velocidade e a média simples"],
                 acc, 34)


# ======================================================================
# bloco d: a fórmula
# ======================================================================

def b_formula(c, t, C, B):
    head_seq(c, t, C, [("13", "A FÓRMULA PRONTA", "MÉDIA HARMÔNICA", PURPLE),
                       ("14", "SÓ VALE PARA", "DISTÂNCIAS IGUAIS", AMBER)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 225, 1320, 90, BLUE, aa)
        linha(c, [("MÉDIA HARMÔNICA", BLUE), (": dá mais peso aos valores MENORES", INK)], W / 2, 270, 34, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        boxed(c, 560, 360, 800, 190, PURPLE, ab)
        text(c, "v  = ", 720, 475, 62, "black", PURPLE, ab)
        fr(c, "2 · v₁ · v₂", "v₁ + v₂", 1020, 455, 60, INK, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        fr(c, "2 · 60 · 40", "60 + 40", 640, 690, 48, INK, acc)
        text_mid(c, "=", 840, 690, 54, "black", INK, ep(t, C["13.c"] + 1.6, 0.4))
        fr(c, "4 800", "100", 960, 690, 48, INK, ep(t, C["13.c"] + 1.6, 0.4))
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        linha(c, [("= ", INK), ("48 km/h", GREEN)], 1200, 672, 56, ad)
    if t < C["14"]:
        return
    a1 = ep(t, C["14.a"], 0.5)
    if a1 > 0:
        selo(c, 1640, 520, a1, "SÓ COM DISTÂNCIAS IGUAIS", AMBER, -6, 26)
    a2 = ep(t, C["14.b"], 0.5)
    if a2 > 0:
        rrect(c, 460, 585, 1000, 170, 22, "#FFFFFF", a2, shadow=True)
        text(c, "fora desse caso:", W / 2, 630, 30, "bold", GRAY, a2)
        fr(c, "distância total", "tempo total", W / 2, 700, 40, INK, ep(t, C["14.c"], 0.4), num_col=BLUE, den_col=AMBER)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        pill(c, "ATALHO: o dobro do produto sobre a soma", W / 2, 795, GREEN, size=30, a=ad, anchor="center")


# ======================================================================
# bloco e: tempos iguais
# ======================================================================

def b_tempos(c, t, C, B):
    head_seq(c, t, C, [("15", "E A MÉDIA SIMPLES?", "QUANDO OS TEMPOS SÃO IGUAIS", GREEN),
                       ("16", "A REGRA COMPLETA", "QUAL MÉDIA USAR", PURPLE)])
    card(c, *CARD_R)
    if t < C["16"]:
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 225, 1320, 90, BLUE, aa)
            linha(c, [("TEMPOS IGUAIS", BLUE), (": o mesmo tanto de horas em cada velocidade", INK)], W / 2, 270, 34, aa)
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            barra_tempo(c, 300, 390, 2, IDA, ab, ep(t, C["15.b"] + 0.3, 0.8), bw=160, bh=80, rotulo="60 km/h", size=28)
            linha(c, [("→ 120 km", IDA)], 700, 430, 40, ab, align="left")
            a2 = ep(t, C["15.b"] + 3.0, 0.4)
            barra_tempo(c, 300, 560, 2, VOLTA, a2, ep(t, C["15.b"] + 3.2, 0.8), bw=160, bh=80, rotulo="40 km/h", size=28)
            linha(c, [("→ 80 km", VOLTA)], 700, 600, 40, a2, align="left")
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            linha(c, [("200 km ÷ 4 h = ", INK), ("50 km/h", GREEN)], 1300, 520, 52, acc)
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            selo(c, 1300, 690, ad, "SÓ COM TEMPOS IGUAIS", GREEN, -5, 36)
        return
    rows = [("16.a", "DISTÂNCIAS IGUAIS", "média harmônica · fica abaixo", AMBER),
            ("16.b", "TEMPOS IGUAIS", "média simples", GREEN),
            ("16.c", "NA DÚVIDA", "distância total ÷ tempo total", PURPLE)]
    for j, (cue, s, sub, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + j * 180 + d
        rrect(c, 300, y, 1320, 140, 24, col, 0.12 * a)
        text(c, s, 360, y + 85, 46, "black", col, a, align="left")
        text(c, sub, 1580, y + 85, 40, "bold", INK, a, align="right")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "DISTÂNCIA AMIGA E FÓRMULA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("ciclista: ida ", INK), ("30 km/h", VOLTA), (" · volta ", INK), ("60 km/h", IDA), ("  →  média = ?", INK)],
              W / 2, 285, 50, aa)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 560)
    if t < C["18"]:
        return
    a1 = ep(t, C["18.a"], 0.4)
    pill(c, "mesmo caminho → distâncias iguais · amiga: 60 km", W / 2, 395, GREEN, size=30, a=a1, anchor="center")
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        barra_tempo(c, 330, 490, 2, VOLTA, ab, ep(t, C["18.b"] + 0.3, 0.8), bw=150, bh=70, rotulo="ida 60 ÷ 30", size=26)
        barra_tempo(c, 1150, 490, 1, IDA, ep(t, C["18.b"] + 2.6, 0.4), 1.0, bw=150, bh=70, rotulo="volta 60 ÷ 60",
                    size=26)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        linha(c, [("120 km ÷ 3 h = ", INK), ("40 km/h", GREEN)], W / 2, 630, 56, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        linha(c, [("fórmula: 2 · 30 · 60 ÷ 90 = 3 600 ÷ 90 = ", INK2), ("40", GREEN)], W / 2, 725, 36, ad)
        conferido(c, "bateu", 1560, 740, ep(t, C["18.d"] + 3.5, 0.4), True, 30)
    ae = ep(t, C["18.e"], 0.5)
    if ae > 0:
        linha(c, [("média simples: 45 km/h", AMBER), ("  → acima da certa", INK2)], W / 2, 805, 34, ae)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Quem manda na média é o relógio.",
          "Distâncias iguais: o resultado fica abaixo da média simples.",
          "Na dúvida, distância total sobre tempo total, sempre."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Média das velocidades com distâncias iguais", "são dois números: soma e divide por 2",
          "o trecho lento dura mais e pesa mais: use a distância amiga"),
         ("Média harmônica com distâncias diferentes (100 km a 60 e 20 km a 40)", "a fórmula é rápida e já funcionou",
          "ela só vale com trechos iguais: distância total ÷ tempo total"),
         ("Média harmônica com TEMPOS iguais", "acabou de aprender que a média simples é pegadinha",
          "mesmo tempo em cada velocidade: a média simples É a certa")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questão do material e você faz
# ======================================================================

def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "A QUESTÃO DO COMEÇO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    yend = _enunciado(c, [(ENUNCIADO, INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS, 1000, 250, 680, 44, C["24.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["24"], 0.4))
        pill(c, "mesmo caminho → DISTÂNCIAS IGUAIS", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["24"], 0.4), anchor="center")
        linha(c, [("amiga 120 km: 2 h + 3 h → 240 ÷ 5 = ", INK), ("48", GREEN)], 540, y0 + 105, 26, ep(t, C["24.a"], 0.4))
        linha(c, [("harmônica: 4 800 ÷ 100 = ", INK), ("48", GREEN)], 540, y0 + 165, 28, ep(t, C["24.b"], 0.4))
        conferido(c, "entre 40 e 50: plausível", 230, y0 + 235, ep(t, C["24.c"], 0.4), True, 26)
    af = ep(t, C["25.f"], 0.5)
    if af > 0:
        selo(c, 1340, 790, af, "CONFIRA A SUA RESPOSTA DO COMEÇO", PURPLE, -2, 26)


def b_voce(c, t, C, B):
    head_seq(c, t, C, [("26", "VOCÊ FAZ", "PAUSE E RESOLVA", GREEN), ("27", "CONFERINDO", "O QUE É IGUAL AQUI?", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["26.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("1 h", PURPLE), (" a 80 km/h  +  ", INK), ("1 h", PURPLE), (" a 60 km/h  →  média = ?", INK)],
              W / 2, 285, 50, aa)
    pause_timer(c, t, C["26.end"] - 1.9, W / 2, 560)
    if t < C["27"]:
        return
    pill(c, "TEMPOS IGUAIS", W / 2, 395, PURPLE, size=32, a=ep(t, C["27"], 0.4), anchor="center")
    a1 = ep(t, C["27.a"], 0.5)
    if a1 > 0:
        barra_tempo(c, 330, 490, 1, IDA, a1, 1.0, bw=170, bh=70, rotulo="80 km/h → 80 km", size=26)
        barra_tempo(c, 1250, 490, 1, VOLTA, ep(t, C["27.a"] + 2.2, 0.4), 1.0, bw=170, bh=70, rotulo="60 km/h → 60 km",
                    size=26)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        linha(c, [("140 km ÷ 2 h = ", INK), ("70 km/h", GREEN)], W / 2, 630, 56, ab)
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        selo(c, 1500, 640, acc, "SÓ COM TEMPOS IGUAIS", GREEN, -5, 26)
        linha(c, [("(80 + 60) ÷ 2 = 70  ✓", GREEN)], W / 2, 715, 36, acc)
    ad = ep(t, C["27.d"], 0.5)
    if ad > 0:
        linha(c, [("harmônica aqui: 9 600 ÷ 140 ≈ 68,6  ✗  terceiro erro clássico", RED)], W / 2, 795, 32, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DENSIDADE", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        s = 220
        x, y = 520, 330
        rrect(c, x, y, s, s, 18, "#B8BEC6", aa, shadow=True)
        rrect(c, x + 16, y + 16, s - 32, 30, 10, "#D7DBE0", aa)
        linha(c, [("156 g", BLUE)], x + s / 2, y + s + 60, 48, aa)
        linha(c, [("20 cm³", AMBER)], x + s / 2, y + s + 130, 48, ep(t, C["29.a"] + 1.8, 0.4))
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        text(c, "?", 900, 500, 200, "black", AMBER, ab)
        text(c, "de que metal ele é feito?", 1320, 460, 40, "black", INK, ab)
        text(c, "sem laboratório", 1320, 520, 34, "bold", GRAY, ab)
    pill(c, "ep. 4 · densidade: identificar o material e decidir se flutua", W / 2, 800, PURPLE, size=30,
         a=ep(t, C["29.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Você marcou 50 no começo?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, hook2=b_hook2, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, instinto=b_instinto,
              amiga=b_amiga, atalho_amiga=b_atalho_amiga, relogio=b_relogio, formula=b_formula, tempos=b_tempos,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, voce=b_voce, ponte=b_ponte, cta=b_cta)
