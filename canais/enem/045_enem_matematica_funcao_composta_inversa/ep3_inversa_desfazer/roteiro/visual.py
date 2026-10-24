"""Visual — Função Composta e Função Inversa, Episódio 3: função inversa (desfazer o caminho) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: maquina(), esteira(), bola(), linha() (as mesmas do ep. 1), termometro() (escala dupla °C/°F),
pe() (meia e sapato).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
A IDA (f) é AZUL e a VOLTA (f⁻¹) é VERDE em todo o episódio; o "1/f" é sempre VERMELHO.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum045", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_composta_inversa_ep3_inversa_desfazer.mp4"
CARD_R = K.CARD_R
COL_IDA, COL_VOLTA = BLUE, GREEN


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def maquina(c, cx, cy, rot, col, a, brilho=0.0, w=220, h=150, size=60):
    """estação da esteira: caixa colorida com a operação grande"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 26, mix("#FFFFFF", col, 0.12 + 0.28 * brilho), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), paint(col, a, stroke=6))
    fmid(c, rot, cx, cy, size, "black", col, a)


def esteira(c, x0, x1, y, a):
    if a <= 0:
        return
    rrect(c, x0, y - 9, x1 - x0, 18, 9, "#D5D8DE", a)
    for k in range(int((x1 - x0) // 40) + 1):
        c.drawCircle(x0 + 10 + k * 40, y, 5, paint("#9AA0AA", a))


def bola(c, x, y, s, col, a, r=46):
    if a <= 0:
        return
    c.drawCircle(x, y, r, paint("#FFFFFF", a))
    c.drawCircle(x, y, r, paint(col, a, stroke=6))
    sz = r * 0.95
    while ftext_w(s, "black", sz) > r * 1.6 and sz > 16:
        sz -= 2
    fmid(c, s, x, y, sz, "black", col, a)


def viagem(c, t, t0, y, xs, nums, col, dur=1.2, r=44):
    """bola passando por 2 estações: xs = [x_entrada, x_est1, x_est2, x_saida]; nums = [entra, meio, sai]"""
    if t < t0:
        bola(c, xs[0], y, nums[0], INK, 1, r)
        return
    trechos = [(xs[0], xs[1], nums[0], INK), (xs[1], xs[2], nums[1], col), (xs[2], xs[3], nums[2], col)]
    k = min(2, int((t - t0) / dur))
    u = ep(t, t0 + k * dur, dur)
    xa, xb, s_, cc = trechos[k]
    bola(c, lerp(xa, xb, ease_io(u)), y, s_, cc, 1, r)


def termometro(c, cx, top, bot, nivel, a, marca=None):
    """tubo com escala dupla: °C à esquerda (30 a 42) e °F à direita; nivel = temperatura em °C mostrada pelo mercúrio"""
    if a <= 0:
        return
    def yC(C):
        return lerp(bot - 40, top + 30, (C - 30) / 12)
    rrect(c, cx - 26, top, 52, bot - top, 26, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 26, top, 52, bot - top), 26, 26), paint("#C9CDD4", a, stroke=4))
    c.drawCircle(cx, bot + 10, 44, paint(RED, a))
    yy = yC(nivel)
    rrect(c, cx - 12, yy, 24, bot + 10 - yy, 12, RED, a)
    for C_ in (30, 33, 36, 39, 42):
        y_ = yC(C_)
        line(c, cx - 46, y_, cx - 28, y_, INK2, a, 3)
        text(c, f"{C_}", cx - 56, y_ + 9, 26, "bold", INK2, a, align="right")
        F_ = 1.8 * C_ + 32
        line(c, cx + 28, y_, cx + 46, y_, INK2, a, 3)
        text(c, f"{F_:.1f}".replace(".", ",").replace(",0", ""), cx + 56, y_ + 9, 26, "bold", INK2, a, align="left")
    text(c, "°C", cx - 70, top - 14, 30, "black", COL_VOLTA, a)
    text(c, "°F", cx + 70, top - 14, 30, "black", COL_IDA, a)
    if marca:
        am = marca
        line(c, cx - 150, yy, cx + 150, yy, AMBER, am, 4)
        pill(c, "37 °C", cx - 230, yy, COL_VOLTA, size=28, a=am, anchor="center")
        pill(c, "98,6 °F", cx + 240, yy, COL_IDA, size=28, a=am, anchor="center")


def pe(c, cx, cy, itens, a, size=34, ok=True):
    """meia e sapato: ordem de duas etapas em fichas, com seta"""
    if a <= 0:
        return
    for k, (s_, col) in enumerate(itens):
        x = cx - 170 + k * 340
        rrect(c, x - 130, cy - 50, 260, 100, 22, mix("#FFFFFF", col, 0.14), a, shadow=True)
        fmid(c, s_, x, cy, size, "black", col, a)
    arrow(c, cx - 30, cy, cx + 30, cy, INK2, a, 5)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO INVERSA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    nivel = lerp(30.5, 37, ep(t, C["01.a"] + 0.4, 1.6))
    termometro(c, 560, 250, 720, nivel, aa)
    if aa > 0:
        text(c, "NOVA YORK", 560, 230 - 30, 26, "black", GRAY, aa)
        chip(c, "98,6 °F", 1150, 330, COL_IDA, aa, 64)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        chip(c, "FEBRE?", 1150, 470, AMBER, ab * (1 - ep(t, C["01.c"], 0.4)), 48)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        chip(c, "= 37 °C", 1150, 470, COL_VOLTA, acc, 60)
        selo(c, 1500, 470, ep(t, C["01.c"] + 1.2, 0.4), "SEM FEBRE", GREEN, -6, 30)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "a fórmula do CAMINHO DE VOLTA", 1250, 680, ad, 40, COL_VOLTA)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    for k, (cue, s_) in enumerate((("02.a", "calcular a INVERSA de qualquer função afim"),
                                   ("02.b", "inverter uma FRAÇÃO"),
                                   ("02.c", "nunca mais confundir f⁻¹ com 1/f"))):
        a, d = rise(t, C[cue])
        check_icon(c, 300, 316 + k * 150 + d, 34, a, GREEN)
        text(c, s_, 360, 330 + k * 150 + d, 50, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "isolar o x", 400, 270, 28, "bold", GRAY, aa)
        K.expr(c, "2x + 1 = 7", 400, 360, 54, aa)
        K.expr(c, "2x = 6", 400, 460, 50, ep(t, C["03.a"] + 2.2, 0.4))
        K.expr(c, "x = 3", 400, 560, 56, ep(t, C["03.a"] + 3.4, 0.4), cores={2: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "Função Afim", 1000, 270, 28, "bold", GRAY, ab)
        K.expr(c, "F = 1,8C + 32", 1000, 380, 54, ab, cores={0: COL_IDA})
        text(c, "Celsius → Fahrenheit", 1000, 470, 30, "black", COL_IDA, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        text(c, "episódio 1", 1560, 270, 28, "bold", GRAY, acc)
        rrect(c, 1400, 340, 320, 90, 20, mix("#FFFFFF", PURPLE, 0.14), acc)
        fmid(c, "MEIA → SAPATO", 1560, 385, 36, "black", PURPLE, acc)
        text(c, "a ordem importa", 1560, 480, 30, "black", PURPLE, acc)
    line(c, 700, 240, 700, 760, "#E6E6E2", ab, 3)
    line(c, 1300, 240, 1300, 760, "#E6E6E2", acc, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DESFAZER", "O ÚLTIMO PASSO SAI PRIMEIRO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "DE MANHÃ", 560, 260, 30, "black", COL_IDA, aa)
        pe(c, 560, 350, [("1º MEIA", COL_IDA), ("2º SAPATO", COL_IDA)], aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        text(c, "À NOITE (desfazer)", 560, 480, 30, "black", COL_VOLTA, ab)
        pe(c, 560, 570, [("1º SAPATO", COL_VOLTA), ("2º MEIA", COL_VOLTA)], ab)
        pill(c, "o último passo é o primeiro a ser desfeito", 560, 690, PURPLE, size=26, a=ep(t, C["04.b"] + 2.2, 0.4),
             anchor="center")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        termometro(c, 1430, 260, 640, 37, acc)
        text_mid(c, "°F  →  °C ?", 1430, 740, 40, "black", AMBER, acc)
    line(c, 1060, 240, 1060, 760, "#E6E6E2", acc, 3)


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "FUNÇÃO INVERSA", "O CAMINHO DE VOLTA", BLUE), ("06", "IDA E VOLTA", "É FICAR PARADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            bola(c, 560, 330, "a", INK, aa, 56)
            arrow(c, 640, 330, 1280, 330, COL_IDA, aa, 6, progress=ep(t, C["05.a"], 1.0))
            bola(c, 1360, 330, "b", COL_IDA, aa, 56)
            text(c, "ENTRADA", 560, 420, 26, "black", GRAY, aa)
            text(c, "SAÍDA", 1360, 420, 26, "black", GRAY, aa)
            fmid(c, "f", 960, 290, 44, "black", COL_IDA, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            arrow(c, 1280, 480, 640, 480, COL_VOLTA, ab, 6, progress=ep(t, C["05.b"], 1.0))
            fmid(c, "f⁻¹", 960, 520, 44, "black", COL_VOLTA, ab)
            text(c, "a saída vira entrada", 960, 590, 28, "black", COL_VOLTA, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            pill(c, "f⁻¹  lê-se  “f inversa”", 960, 660, BLUE, size=30, a=acc, anchor="center")
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            regra(c, "f(a) = b   →   f⁻¹(b) = a", W / 2, 760, ad, 44)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        bola(c, 480, 400, "x", INK, aa, 56)
        arrow(c, 550, 400, 860, 400, COL_IDA, aa, 6)
        maquina(c, 960, 400, "f", COL_IDA, aa, 0, 180, 120, 60)
        arrow(c, 1060, 400, 1300, 400, COL_VOLTA, aa, 6)
        maquina(c, 1400, 400, "f⁻¹", COL_VOLTA, ep(t, C["06.a"] + 1.0, 0.4), 0, 180, 120, 56)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        bola(c, 1620, 400, "x", COL_VOLTA, ab, 56)
        K.expr(c, "f^{-1}(f(x)) = x", W / 2, 580, 60, ab, cores={0: COL_VOLTA, 2: GREEN})
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        regra(c, "ida e volta = ficar parado", W / 2, 730, acc, 44, PURPLE)


# ======================================================================
# bloco b — f⁻¹ não é 1/f
# ======================================================================

def _curvas(c, a, x0, y0, w, h):
    """mini-gráfico: reta x/2 (verde) e curva 1/(2x) (vermelha), para x de 0,1 a 6"""
    if a <= 0:
        return
    rrect(c, x0, y0, w, h, 16, "#FFFFFF", a, shadow=True)
    ox, oy = x0 + 40, y0 + h - 40
    sx, sy = (w - 70) / 6, (h - 70) / 3.2
    line(c, ox, oy, ox + w - 60, oy, INK2, a, 3)
    line(c, ox, oy, ox, y0 + 20, INK2, a, 3)
    for fn, col in ((lambda x: x / 2, COL_VOLTA), (lambda x: 1 / (2 * x), RED)):
        p = skia.Path(); first = True
        for i in range(0, 241):
            x = 0.16 + i * (6 - 0.16) / 240
            yv = min(fn(x), 3.2)
            px, py = ox + x * sx, oy - yv * sy
            if first:
                p.moveTo(px, py); first = False
            else:
                p.lineTo(px, py)
        c.drawPath(p, paint(col, a, stroke=6))
    text(c, "x/2: reta", ox + w - 120, oy - 3 * sy + 20, 24, "black", COL_VOLTA, a)
    text(c, "1/(2x): curva", ox + 170, y0 + 50, 24, "black", RED, a)


def b_umsobre(c, t, C, B):
    head_seq(c, t, C, [("07", "O ⁻¹ NÃO É EXPOENTE", "f⁻¹ DESFAZ", AMBER), ("08", "x/2 OU 1/(2x)?", "FUNÇÕES DIFERENTES", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            linha(c, [("⁻¹", AMBER), ("  aqui quer dizer  ", INK), ("DESFAZER", COL_VOLTA)], W / 2, 270, 46, aa)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            K.expr(c, "f(x) = x + 3", 560, 400, 50, ab, cores={0: COL_IDA})
            K.expr(c, "f^{-1}(x) = x - 3", 560, 510, 54, ep(t, C["07.b"] + 1.6, 0.4), cores={0: COL_VOLTA})
            pill(c, "tira 3", 560, 600, COL_VOLTA, size=26, a=ep(t, C["07.b"] + 1.6, 0.4), anchor="center")
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            K.expr(c, "1/{x+3}", 1340, 440, 64, acc, cores={0: RED})
            text(c, "OUTRA COISA", 1340, 560, 30, "black", RED, acc)
            ac2 = ep(t, C["07.c"] + 1.8, 0.4)
            if ac2 > 0:
                rrect(c, 380, 660, 1160, 110, 22, "#FFFFFF", ac2, shadow=True)
                linha(c, [("x = 1:   ", GRAY), ("inversa → −2", COL_VOLTA), ("     ", INK), ("1/(x+3) → 0,25", RED)],
                      W / 2, 715, 38, ac2)
        line(c, 960, 340, 960, 620, "#E6E6E2", acc, 3)
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        K.expr(c, "f(x) = 2x", 480, 280, 48, aa, cores={0: COL_IDA})
        K.expr(c, "f^{-1}(x) = x/2", 480, 390, 54, aa, cores={0: COL_VOLTA})
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        K.expr(c, "1/{2x}", 480, 520, 54, ab, cores={0: RED})
        rrect(c, 200, 610, 560, 150, 20, "#FFFFFF", ab, shadow=True)
        linha(c, [("x = 4:  ", GRAY), ("x/2 = 2", COL_VOLTA)], 480, 650, 34, ab)
        linha(c, [("1/(2x) = 0,125", RED)], 480, 715, 34, ep(t, C["08.b"] + 1.6, 0.4))
    acc = ep(t, C["08.c"], 0.5)
    _curvas(c, acc, 900, 260, 820, 440)
    if acc > 0:
        selo(c, 1310, 760, ep(t, C["08.c"] + 1.2, 0.4), "NEM PERTO", RED, -4, 30)


# ======================================================================
# bloco c — a esteira e a receita
# ======================================================================

def b_esteira(c, t, C, B):
    head(c, t, B["start"], "A ESTEIRA", "IDA E VOLTA", BLUE)
    card(c, *CARD_R)
    # ida: 1 → ×2 → 2 → +1 → 3
    yi, yv = 360, 640
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        text(c, "IDA", 220, yi - 110, 28, "black", COL_IDA, aa, align="left")
        esteira(c, 220, 1700, yi + 90, aa)
        maquina(c, 700, yi, "×2", COL_IDA, aa, ep(t, C["09.a"] + 1.4, 0.3) * (1 - ep(t, C["09.a"] + 2.6, 0.3)))
        maquina(c, 1220, yi, "+1", COL_IDA, aa, ep(t, C["09.a"] + 2.6, 0.3) * (1 - ep(t, C["09.a"] + 3.8, 0.3)))
        viagem(c, t, C["09.a"] + 0.8, yi, [330, 700, 1220, 1590], ["1", "2", "3"], COL_IDA)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        text(c, "VOLTA (ao contrário)", 1700, yv - 110, 28, "black", COL_VOLTA, ab, align="right")
        esteira(c, 220, 1700, yv + 90, ab)
        maquina(c, 1220, yv, "−1", COL_VOLTA, ab, ep(t, C["09.b"] + 1.4, 0.3) * (1 - ep(t, C["09.b"] + 2.6, 0.3)))
        maquina(c, 700, yv, "÷2", COL_VOLTA, ab, ep(t, C["09.b"] + 2.6, 0.3) * (1 - ep(t, C["09.b"] + 3.8, 0.3)))
        viagem(c, t, C["09.b"] + 0.8, yv, [1590, 1220, 700, 330], ["3", "2", "1"], COL_VOLTA)
        pill(c, "1º desfaz o +1 · depois o ×2", W / 2, yv - 110, PURPLE, size=24, a=ep(t, C["09.b"] + 1.0, 0.4),
             anchor="center")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        selo(c, 330, yv + 160, acc, "VOLTOU AO 1", GREEN, -5, 26)


def b_receita(c, t, C, B):
    head(c, t, B["start"], "A RECEITA", "3 PASSOS", PURPLE)
    card(c, *CARD_R)
    X = 300
    passos = [("10.a", "1", "escreva y = f(x)", "y = 2x + 1"),
              ("10.b", "2", "isole o x", "x = {y-1}/2"),
              ("10.c", "3", "troque os nomes", "x ↔ y")]
    for k, (cue, n, rot, ex) in enumerate(passos):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 140 + d
        badge_num(c, n, X, y, a, 32, bg=PURPLE)
        text(c, rot, X + 60, y + 12, 36, "black", INK, a, align="left")
        K.expr(c, ex, 1250, y, 52, a)
    ab = ep(t, C["10.b"] + 1.4, 0.4)
    if ab > 0 and t < C["10.c"]:
        pill(c, "passe o 1 · divida por 2", 1250, 500, AMBER, size=24, a=ab, anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 480, 650, 960, 130, 24, mix("#FFFFFF", COL_VOLTA, 0.12), ad)
        K.expr(c, "f^{-1}(x) = {x-1}/2", W / 2, 715, 58, ad, cores={0: COL_VOLTA})


def b_teste(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TESTE COM UM PONTO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 360, 230, 1200, 130, "ATALHO", ["achou a inversa? se f(a) = b, confira se f⁻¹(b) = a"], aa, 32)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        K.expr(c, "f(1) = 2·1 + 1 = 3", 620, 480, 50, ab, cores={0: COL_IDA, 6: COL_IDA})
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        K.expr(c, "f^{-1}(3) = {3-1}/2 = 1", 1300, 480, 50, acc, cores={0: COL_VOLTA, 4: GREEN})
        arrow(c, 900, 600, 1020, 600, GREEN, acc, 5)
        selo(c, W / 2, 690, ep(t, C["11.c"] + 2.4, 0.4), "BATEU", GREEN, -5, 36)


# ======================================================================
# bloco d — a inversa da afim
# ======================================================================

def b_afim(c, t, C, B):
    head_seq(c, t, C, [("12", "INVERSA DA AFIM", "ORDEM CONTRÁRIA", PURPLE), ("13", "ATALHO", "SOMADO POR ÚLTIMO SAI PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            K.expr(c, "y = ax + b", W / 2, 280, 60, aa, cores={2: COL_IDA})
            pe(c, W / 2, 400, [("1º  ×a", COL_IDA), ("2º  +b", COL_IDA)], aa, 36)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            pe(c, W / 2, 540, [("1º  −b", COL_VOLTA), ("2º  ÷a", COL_VOLTA)], ab, 36)
            regra(c, "f⁻¹(x) = (x − b)/a", W / 2, 670, ep(t, C["12.b"] + 2.0, 0.4), 46)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            pill(c, "f cresce → f⁻¹ também cresce", W / 2, 770, BLUE, size=28, a=acc, anchor="center")
        return
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 300, 240, 1320, 150, "ATALHO", ["o que foi somado por último sai primeiro; depois divida pelo número do x"],
             aa, 30)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        K.expr(c, "5x + 4", 620, 540, 60, ab, cores={0: COL_IDA})
        arrow(c, 820, 540, 1000, 540, INK2, ab, 5)
        K.expr(c, "{x-4}/5", 1240, 540, 64, ep(t, C["13.b"] + 1.0, 0.4), cores={0: COL_VOLTA})
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 700, acc, "SEM MONTAR EQUAÇÃO", GREEN, -4, 30)


# ======================================================================
# bloco e — conversões
# ======================================================================

def b_conversao(c, t, C, B):
    head_seq(c, t, C, [("14", "CONVERSÃO", "°F DE VOLTA PARA °C", BLUE), ("15", "ATALHO", "LEIA DE TRÁS PARA FRENTE", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        a0 = ep(t, C["14"], 0.4)
        nivel = 37 if t < C["14.c"] else lerp(37, 37, 1)
        termometro(c, 360, 270, 680, nivel, a0, marca=ep(t, C["14.c"] + 3.0, 0.4))
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            K.expr(c, "F = 1,8C + 32", 1180, 290, 52, aa, cores={0: COL_IDA})
            pe(c, 1180, 400, [("1º  ×1,8", COL_IDA), ("2º  +32", COL_IDA)], aa, 32)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            pe(c, 1180, 520, [("1º  −32", COL_VOLTA), ("2º  ÷1,8", COL_VOLTA)], ab, 32)
            K.expr(c, "C = {F-32}/{1,8}", 1180, 650, 54, ep(t, C["14.b"] + 1.8, 0.4), cores={0: COL_VOLTA})
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            rrect(c, 760, 730, 840, 80, 18, mix("#FFFFFF", COL_VOLTA, 0.12), acc)
            linha(c, [("98,6 − 32 = 66,6", INK), ("   →   ", GRAY), ("66,6 ÷ 1,8 = 37 °C", COL_VOLTA)], 1180, 770, 34, acc)
        return
    aa = ep(t, C["15.a"], 0.5)
    K.atalho(c, 300, 240, 1320, 150, "ATALHO", ["toda conversão tem volta: leia a fórmula de trás para frente, com a conta oposta"],
             aa, 28)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        rrect(c, 440, 470, 1040, 200, 24, "#FFFFFF", ab, shadow=True)
        linha(c, [("TÁXI:  ", GRAY), ("preço", COL_IDA), (" pela distância", INK)], W / 2, 530, 40, ab)
        linha(c, [("→  ", GRAY), ("distância", COL_VOLTA), (" pelo preço", INK)], W / 2, 610, 40,
              ep(t, C["15.b"] + 1.4, 0.4))
        pill(c, "é a Questão 3", W / 2, 740, PURPLE, size=28, a=ep(t, C["15.b"] + 2.6, 0.4), anchor="center")


# ======================================================================
# bloco f — inversa com fração (exemplo nosso: (3x + 2)/(x − 4))
# ======================================================================

def b_fracao(c, t, C, B):
    head_seq(c, t, C, [("16", "INVERSA COM FRAÇÃO", "MULTIPLIQUE CRUZADO", PURPLE),
                       ("17", "O x APARECE DUAS VEZES", "PONHA EM EVIDÊNCIA", PURPLE),
                       ("18", "ATALHO", "O TRUQUE DA FRAÇÃO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17", "18"])
    X = 360
    if sid == "18":
        aa = ep(t, C["18.a"], 0.5)
        K.atalho(c, 300, 260, 1320, 170, "ATALHO", ["junte os x de um lado", "e ponha o x em evidência"], aa, 36)
        ab = ep(t, C["18.b"], 0.5)
        if ab > 0:
            K.expr(c, "x(y-3) = 4y + 2", W / 2, 560, 60, ab, cores={0: GREEN})
            text(c, "é assim que o x fica sozinho", W / 2, 670, 32, "black", INK, ab)
        return
    a0 = ep(t, C["16"], 0.4)
    if a0 > 0:
        K.expr(c, "f(x) = {3x+2}/{x-4}", 520, 250, 46, a0, cores={0: COL_IDA})
        text(c, "x ≠ 4", 880, 262, 26, "black", GRAY, ep(t, C["16.a"], 0.4), align="left")
    rows = [("16.b", "y(x-4) = 3x + 2", "multiplique cruzado"),
            ("16.c", "xy - 4y = 3x + 2", "distribua o y"),
            ("17.a", "xy - 3x = 4y + 2", "junte os x de um lado"),
            ("17.b", "x(y-3) = 4y + 2", "x em evidência"),
            ("17.c", "f^{-1}(x) = {4x+2}/{x-3}", "divida e troque os nomes")]
    for k, (cue, ex, rot) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 350 + k * 88
        col = COL_VOLTA if k == 4 else INK
        K.expr(c, ex, X + 340, y, 40, a, cores={0: col} if k == 4 else None)
        pill(c, rot, 1340, y, AMBER if k in (2, 3) else PURPLE, size=22, a=a, anchor="center")
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 680, 560, 120, 20, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("f(5) = 17", COL_IDA), ("   →   ", GRAY), ("f⁻¹(17) = 70/14 = 5", COL_VOLTA)], 1360, 740, 28, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "ORDEM CONTRÁRIA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        K.expr(c, "f(x) = 3x - 6", W / 2, 270, 58, aa, cores={0: COL_IDA})
        text(c, "ache f⁻¹ e teste com um ponto", W / 2, 360, 32, "black", INK, aa)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 560)
    if t < C["20"]:
        return
    a1 = ep(t, C["20.a"], 0.4)
    if a1 > 0:
        K.expr(c, "y + 6 = 3x", 560, 480, 46, a1)
        pill(c, "1º soma 6", 560, 560, COL_VOLTA, size=24, a=a1, anchor="center")
    a2 = ep(t, C["20.b"], 0.4)
    if a2 > 0:
        K.expr(c, "f^{-1}(x) = {x+6}/3", 1300, 500, 50, a2, cores={0: COL_VOLTA})
        pill(c, "2º divide por 3 · troca os nomes", 1300, 600, COL_VOLTA, size=24, a=a2, anchor="center")
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        rrect(c, 480, 660, 960, 110, 22, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("f(4) = 6", COL_IDA), ("   →   ", GRAY), ("f⁻¹(6) = 12/3 = 4", COL_VOLTA)], W / 2, 715, 38, acc)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["A inversa troca entrada e saída.",
          "Desfaça na ordem contrária: primeiro o último passo.",
          "f⁻¹ desfaz; 1/f só vira de cabeça para baixo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar que f⁻¹(x) = 1/f(x)", "em números, 2⁻¹ é mesmo 1/2",
          "no f, o ⁻¹ quer dizer DESFAZER: a inversa de x + 3 é x − 3"),
         ("Inversa de 2x + 1 = (x + 1)/2 ou x/2 − 1", "as contas são as mesmas da ida",
          "conta oposta, ordem contrária: (x − 1)/2 · com 3, as erradas não voltam ao 1"),
         ("Trocar as letras sem isolar: x = 2y + 1", "trocar os nomes é mesmo um dos passos",
          "é o ÚLTIMO passo: sem isolar, você só reescreveu a própria f")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24"], ERROS)


# ======================================================================
# questões
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


ALTS3 = [("A", "= x = {P-4,5}/{2,5}", "", GREEN), ("B", "= x = P/{2,5} - 4,5", "dividiu antes de subtrair", RED),
         ("C", "= x = {P+4,5}/{2,5}", "somou o 4,5", RED), ("D", "= x = 2,5P + 4,5", "trocou as letras sem isolar", RED),
         ("E", "= x = 1/{4,5+2,5P}", "“um sobre”", RED)]


def b_q3(c, t, C, B):
    head_seq(c, t, C, [("25", "QUESTÃO 3 · EU FAÇO", "A DISTÂNCIA PELO PREÇO", BLUE), ("26", "RESOLVENDO", "A VOLTA", COL_VOLTA),
                       ("27", "AS ERRADAS", "CADA UMA, UM ERRO", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    sid = which(t, C, ["25", "26", "27"])
    enun = ("Em uma cidade, o preço P, em reais, de uma corrida de táxi de x quilômetros é P = 4,5 + 2,5x. Um aplicativo "
            "quer mostrar ao passageiro quantos quilômetros ele pode percorrer com um valor P disponível. A expressão "
            "que fornece x em função de P é")
    yend = _enunciado(c, [(enun, INK)], a0 * (1 - ep(t, C["26"], 0.3)), 240, 26) if sid == "25" else 240
    if sid == "25":
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 36, C["26.ok"], "A", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 120)
    if sid == "26":
        y0 = 230
        _painel(c, y0, ep(t, C["26"], 0.4))
        aa = ep(t, C["26.a"], 0.4)
        if aa > 0:
            text(c, "IDA", 330, y0 + 70, 24, "black", COL_IDA, aa)
            linha(c, [("×2,5", COL_IDA), ("  →  ", GRAY), ("+4,5", COL_IDA)], 640, y0 + 60, 34, aa)
            text(c, "VOLTA", 330, y0 + 150, 24, "black", COL_VOLTA, ep(t, C["26.a"] + 2.4, 0.4))
            linha(c, [("−4,5", COL_VOLTA), ("  →  ", GRAY), ("÷2,5", COL_VOLTA)], 640, y0 + 140, 34,
                  ep(t, C["26.a"] + 2.4, 0.4))
        ab = ep(t, C["26.b"], 0.4)
        if ab > 0:
            K.expr(c, "x = {P-4,5}/{2,5}", 540, y0 + 260, 44, ab, cores={0: COL_VOLTA})
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            pill(c, "TESTE: P = R$ 37,00", 540, y0 + 370, GREEN, size=24, a=acc, anchor="center")
            text(c, "32,5 ÷ 2,5 = 13 km", 540, y0 + 440, 32, "black", COL_VOLTA, acc)
            text(c, "4,5 + 2,5 · 13 = 37  ✓", 540, y0 + 500, 32, "black", COL_IDA, ep(t, C["26.c"] + 2.6, 0.4))
    elif sid == "27":
        y0 = 230
        _painel(c, y0, ep(t, C["27"], 0.4))
        text(c, "com P = R$ 37,00", 540, y0 + 60, 26, "black", GRAY, ep(t, C["27"], 0.4))
        for k, (cue, s_) in enumerate((("xb", "B → 10,3 km"), ("xc", "C → 16,6 km"), ("xd", "D → 97"),
                                       ("xe", "E → 0,01"))):
            a = ep(t, C["27." + cue], 0.4)
            if a > 0:
                check_icon(c, 300, y0 + 132 + k * 70, 18, a, RED, "x")
                text(c, s_, 340, y0 + 142 + k * 70, 30, "black", INK, a, align="left")
        aa = ep(t, C["27.a"], 0.4)
        if aa > 0:
            selo(c, 540, y0 + 470, aa, "SÓ A A DÁ 13", GREEN, -4, 26)


ALTS8 = [("A", "= f^{-1}(x) = {3x+1}/{x-2}", "", GREEN), ("B", "= f^{-1}(x) = {x-3}/{2x+1}", "é o 1/f", RED),
         ("C", "= f^{-1}(x) = {3x+1}/{x+2}", "sinal do 2", RED), ("D", "= f^{-1}(x) = {3x-1}/{x-2}", "sinal do 1", RED),
         ("E", "= f^{-1}(x) = {2x+1}/{x-3}", "a própria f", RED)]


def b_q8(c, t, C, B):
    head_seq(c, t, C, [("28", "QUESTÃO 8 · VOCÊ FAZ", "INVERSA DE UMA FRAÇÃO", GREEN),
                       ("29", "CONFERINDO", "EVIDÊNCIA", PURPLE), ("30", "TESTE COM UM PONTO", "E AS ERRADAS", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    sid = which(t, C, ["28", "29", "30"])
    if sid == "28":
        _enunciado(c, [("A função", INK)], a0, 240, 26)
        K.expr(c, "f(x) = {2x+1}/{x-3}", 540, 320, 46, a0, cores={0: COL_IDA})
        yend = _enunciado(c, [("definida para x ≠ 3, é usada para converter um índice x em uma nota f(x) e admite "
                               "inversa no conjunto adequado. A lei de f⁻¹ é", INK)], a0, 400, 26)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 110)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS8, 1000, 240, 690, 30, C["29.ok"], "A", cues_in, cues_x, gap=18)
    if sid == "29":
        y0 = 230
        _painel(c, y0, ep(t, C["29"], 0.4))
        rows = [("29.a", "xy - 3y = 2x + 1"), ("29.b", "xy - 2x = 3y + 1"), ("29.b", "x(y-2) = 3y + 1"),
                ("29.c", "f^{-1}(x) = {3x+1}/{x-2}")]
        for k, (cue, ex) in enumerate(rows):
            a = ep(t, C[cue] + (1.8 if k == 2 else 0), 0.4)
            if a > 0:
                K.expr(c, ex, 540, y0 + 80 + k * 120, 40, a, cores={0: COL_VOLTA} if k == 3 else None)
    elif sid == "30":
        y0 = 230
        _painel(c, y0, ep(t, C["30"], 0.4))
        aa = ep(t, C["30.a"], 0.4)
        if aa > 0:
            K.expr(c, "f(4) = 9/1 = 9", 540, y0 + 80, 40, aa, cores={0: COL_IDA})
            K.expr(c, "f^{-1}(9) = 28/7 = 4", 540, y0 + 190, 40, ep(t, C["30.a"] + 2.2, 0.4), cores={0: COL_VOLTA})
        ab = ep(t, C["30.b"], 0.4)
        if ab > 0:
            pill(c, "com 9: B 6/19 · C 28/11 · D 26/7 · E 19/6", 540, y0 + 320, RED, size=22, a=ab, anchor="center")
            selo(c, 540, y0 + 440, ab, "SÓ A A VOLTA AO 4", GREEN, -4, 26)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUEM TEM INVERSA?", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    if aa > 0:
        K.expr(c, "f(x) = x^2", W / 2, 260, 52, aa, cores={0: COL_IDA})
        bola(c, 640, 380, "3", INK, aa, 50)
        bola(c, 640, 560, "−3", INK, aa, 50)
        bola(c, 1280, 470, "9", COL_IDA, aa, 60)
        arrow(c, 700, 395, 1210, 460, COL_IDA, aa, 5)
        arrow(c, 700, 545, 1210, 480, COL_IDA, aa, 5)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        chip(c, "veio de onde?", 1580, 470, AMBER, ab, 34)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        regra(c, "nem toda função pode ser desfeita", W / 2, 680, acc, 40, RED)
    pill(c, "ep. 4 · quem tem inversa e o espelho y = x", W / 2, 790, PURPLE, size=30, a=ep(t, C["32.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Que conversão você já fez de trás para frente?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              umsobre=b_umsobre, esteira=b_esteira, receita=b_receita, teste=b_teste, afim=b_afim,
              conversao=b_conversao, fracao=b_fracao, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3,
              q8=b_q8, ponte=b_ponte, cta=b_cta)
