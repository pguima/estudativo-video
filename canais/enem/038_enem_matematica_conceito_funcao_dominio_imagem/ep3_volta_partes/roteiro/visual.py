"""Visual — Conceito de Função, Episódio 3: o caminho de volta (f(x) = k) e as funções por partes (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: maquina() (funil de entrada, bandeja de saída; roda ao contrário no caminho de volta),
margem() (a etiqueta "dão o x" / "dão o y"), relogio_estac() (linha do tempo em blocos de 1 hora: 1ª hora azul, adicionais
roxas, o bloco que só começou acende inteiro), gavetas() (armário de faixas), linha().
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
_s = importlib.util.spec_from_file_location("comum038", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_ep3_volta_partes.mp4"
CARD_R = K.CARD_R
IDA = BLUE       # caminho de ida (dão o x)
VOLTA = AMBER    # caminho de volta (dão o y)
H1 = BLUE        # 1ª hora do estacionamento
HAD = PURPLE     # horas adicionais


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


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def margem(c, s, x, y, a, col=None):
    """a etiqueta da margem: 'dão o x' (azul, ida) ou 'dão o y' (âmbar, volta)"""
    if a <= 0:
        return
    col = col or (IDA if s.endswith("x") else VOLTA)
    w = ftext_w(s, "black", 30) + 50
    rrect(c, x, y - 32, w, 64, 12, mix("#FFFFFF", col, 0.14), a)
    line(c, x, y - 32, x, y + 32, col, a, 8)
    fmid(c, s, x + w / 2 + 4, y, 30, "black", col, a)


def chip_num(c, s, cx, cy, col, a, size=36):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 44
    rrect(c, cx - w / 2, cy - size * 0.85, w, size * 1.7, size * 0.5, col, a, shadow=True)
    fmid(c, s, cx, cy, size, "black", "#FFFFFF", a)


def maquina(c, cx, cy, a, rotulo="P(d) = 5 + 2,5d", entra=None, sai=None, prog=0.0, volta=False, s=1.0):
    """máquina de função: funil de entrada no alto (esquerda), corpo, bandeja de saída embaixo (direita).
    prog 0..1 move o número: na ida, entra pelo funil e sai na bandeja; na volta, entra pela bandeja e sai pelo funil."""
    if a <= 0:
        return
    bw, bh = 520 * s, 230 * s
    x0, y0 = cx - bw / 2, cy - bh / 2
    # funil
    fx = x0 + 110 * s
    pth = skia.Path()
    pth.moveTo(fx - 80 * s, y0 - 110 * s); pth.lineTo(fx + 80 * s, y0 - 110 * s)
    pth.lineTo(fx + 26 * s, y0); pth.lineTo(fx - 26 * s, y0); pth.close()
    c.drawPath(pth, paint(mix("#FFFFFF", IDA, 0.25), a))
    # corpo
    rrect(c, x0, y0, bw, bh, 28 * s, INK2, a, shadow=True)
    rrect(c, x0 + 24 * s, y0 + 60 * s, bw - 48 * s, 100 * s, 16 * s, "#FFFFFF", a)
    fmid(c, rotulo, cx, y0 + 110 * s, 38 * s, "black", PURPLE, a)
    for k in range(3):
        c.drawCircle(x0 + 44 * s + k * 34 * s, y0 + 32 * s, 9 * s, paint([GREEN, AMBER, RED][k], a))
    # engrenagem girando (no sentido do caminho)
    gx, gy, gr = x0 + bw - 60 * s, y0 + 32 * s, 18 * s
    ang = (-1 if volta else 1) * prog * 720
    for k in range(6):
        th = math.radians(ang + k * 60)
        line(c, gx, gy, gx + gr * math.cos(th), gy + gr * math.sin(th), "#FFFFFF", a, 5 * s)
    # bandeja
    tx, ty = x0 + bw - 40 * s, y0 + bh
    rrect(c, tx - 20 * s, ty, 220 * s, 26 * s, 12 * s, mix("#FFFFFF", GREEN, 0.35), a)
    rrect(c, tx + 180 * s, ty - 40 * s, 22 * s, 66 * s, 10 * s, mix("#FFFFFF", GREEN, 0.35), a)
    if volta:
        pill(c, "◀ VOLTA", cx, y0 - 50 * s, VOLTA, size=24 * s, a=a, anchor="center")
    # números em trânsito
    p_in = (fx, y0 - 160 * s)
    p_mid = (cx, cy)
    p_out = (tx + 90 * s, ty - 30 * s)
    if not volta:
        if entra and prog < 0.5:
            q = prog / 0.5
            chip_num(c, entra, lerp(p_in[0], p_mid[0], q), lerp(p_in[1], p_mid[1], q), IDA, a * (1 - max(0, q - 0.8) * 5))
        if sai and prog >= 0.5:
            q = (prog - 0.5) / 0.5
            chip_num(c, sai, lerp(p_mid[0], p_out[0], q), lerp(p_mid[1], p_out[1], q), GREEN, a * min(1, q * 5))
    else:
        if sai and prog < 0.5:
            q = prog / 0.5
            chip_num(c, sai, lerp(p_out[0], p_mid[0], q), lerp(p_out[1], p_mid[1], q), VOLTA, a * (1 - max(0, q - 0.8) * 5))
        if entra and prog >= 0.5:
            q = (prog - 0.5) / 0.5
            chip_num(c, entra, lerp(p_mid[0], p_in[0], q), lerp(p_mid[1], p_in[1], q), GREEN, a * min(1, q * 5))


def relogio_estac(c, x, y, minutos, a, prog=1.0, bw=190, bh=96, mostra_preco=True, acende=1.0, fracao_selo=0.0,
                  ignora=False):
    """linha do tempo do estacionamento em blocos de 1 hora. prog 0..1 = o tempo real correndo (barra de tempo cinza).
    acende 0..1 = os blocos cobrados acendendo; o último bloco (fração) acende inteiro. ignora=True deixa a fração apagada."""
    if a <= 0:
        return
    n = math.ceil(minutos / 60)
    usado = minutos * prog
    for k in range(n):
        xx = x + k * (bw + 12)
        rrect(c, xx, y, bw, bh, 14, "#EDEBE4", a)
        # tempo real (cinza escuro) dentro do bloco
        fill = max(0.0, min(1.0, (usado - 60 * k) / 60))
        if fill > 0:
            rrect(c, xx, y + bh - 16, bw * fill, 16, 8, INK2, a * 0.7)
        col = H1 if k == 0 else HAD
        ak = a * max(0.0, min(1.0, acende * n - k))
        if ignora and k == n - 1 and minutos % 60:
            ak = 0
        if ak > 0:
            rrect(c, xx, y, bw, bh - 18, 14, col, ak * 0.92)
            if mostra_preco:
                fmid(c, "R$ 10" if k == 0 else "+ R$ 4", xx + bw / 2, y + (bh - 18) / 2, 32, "black", "#FFFFFF", ak)
        text(c, f"{k}h–{k + 1}h", xx + bw / 2, y + bh + 36, 22, "bold", GRAY, a)
    if fracao_selo > 0 and minutos % 60:
        xx = x + (n - 1) * (bw + 12)
        selo(c, xx + bw / 2, y - 40, fracao_selo, "fração = hora cheia", GREEN, -5, 24)


def gavetas(c, x, y, a, itens, aberta=-1, w=520, gh=110):
    """armário de gavetas: itens = [(faixa, regra)]; a gaveta 'aberta' desliza para fora"""
    if a <= 0:
        return
    rrect(c, x - 20, y - 20, w + 40, len(itens) * (gh + 14) + 26, 20, "#D8D2C2", a, shadow=True)
    for k, (faixa, reg) in enumerate(itens):
        dx = 70 if k == aberta else 0
        yy = y + k * (gh + 14)
        rrect(c, x + dx, yy, w, gh, 14, "#FFFDF6", a)
        rrect(c, x + dx + w / 2 - 50, yy + gh - 30, 100, 14, 7, INK2, a)
        ftext(c, faixa, x + dx + 30, yy + 52, 32, "black", BLUE, a, align="left")
        ftext(c, reg, x + dx + w - 30, yy + 52, 30, "bold", PURPLE, a, align="right")


def placa(c, x, y, a, w=520):
    """placa do estacionamento"""
    if a <= 0:
        return
    rrect(c, x, y, w, 300, 22, "#1F4E9C", a, shadow=True)
    text(c, "E", x + 70, y + 110, 90, "black", "#FFFFFF", a)
    ftext(c, "1ª hora: R$ 10,00", x + 130, y + 90, 36, "black", "#FFFFFF", a, align="left")
    ftext(c, "hora adicional", x + 130, y + 160, 34, "bold", "#FFFFFF", a, align="left")
    ftext(c, "ou fração: R$ 4,00", x + 130, y + 215, 36, "black", "#FFE9A8", a, align="left")
    rrect(c, x + w / 2 - 12, y + 300, 24, 140, 6, INK2, a)


def recibo(c, x, y, a):
    if a <= 0:
        return
    rrect(c, x, y, 360, 380, 10, "#FFFFFF", a, shadow=True)
    for k in range(9):
        c.drawCircle(x + 20 + k * 40, y + 380, 12, paint("#F3F2EE", a))
    text(c, "TÁXI", x + 180, y + 70, 44, "black", INK, a)
    line(c, x + 30, y + 100, x + 330, y + 100, "#D8D2C2", a, 3, dash=(10, 8))
    ftext(c, "distância:", x + 40, y + 170, 30, "bold", GRAY, a, align="left")
    ftext(c, "? km", x + 320, y + 170, 36, "black", VOLTA, a, align="right")
    ftext(c, "total:", x + 40, y + 260, 30, "bold", GRAY, a, align="left")
    ftext(c, "R$ 30,00", x + 320, y + 260, 40, "black", INK, a, align="right")


def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 760, y1 - y0, 18, "#FFFFFF", a, shadow=True)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "CONCEITO DE FUNÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 560, 220, 800, 110, PURPLE, aa)
        fmid(c, "P(d) = 5 + 2,5d", W / 2, 275, 56, "black", PURPLE, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        recibo(c, 260, 380, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        linha(c, [("P(30) = 5 + 2,5 · 30 = ", INK), ("R$ 80,00", RED)], 1150, 470, 44, acc)
        text(c, "o preço de uma corrida de 30 km", 1150, 540, 30, "bold", GRAY, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1530, 590, ad, "ALTERNATIVA ERRADA", RED, -5, 28)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        rrect(c, 760, 640, 800, 110, 22, mix("#FFFFFF", VOLTA, 0.14), ae)
        fmid(c, "quantos km custam R$ 30,00?", 1160, 695, 44, "black", VOLTA, ae)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "saber quando CALCULAR f(x)", "dão o x"),
            ("02.b", "e quando RESOLVER f(x) = k", "dão o y"),
            ("02.c", "calcular qualquer tarifa por faixa", "sem cair no \"ou fração\"")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        ftext(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "NOTAÇÃO f(x)", 560, 290, 34, "black", BLUE, aa)
        text(c, "episódio 2", 560, 340, 26, "bold", GRAY, aa)
        fmid(c, "f(x) = saída", 560, 470, 60, "black", INK, aa)
        fmid(c, "quando a entrada é x", 560, 550, 34, "bold", GRAY, aa)
    ab = ep(t, C["03.b"], 0.5)
    line(c, 960, 240, 960, 790, "#E6E6E2", ab, 3)
    if ab > 0:
        text(c, "RESOLVER A EQUAÇÃO", 1370, 290, 34, "black", PURPLE, ab)
        text(c, "série de equações do 1º grau", 1370, 340, 26, "bold", GRAY, ab)
        fmid(c, "5 + 2,5d = 30", 1370, 440, 52, "black", INK, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        linha(c, [("− 5 dos dois lados:  ", GRAY), ("2,5d = 25", INK)], 1370, 550, 40, acc)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        linha(c, [("÷ 2,5:  ", GRAY), ("d = 10", GREEN)], 1370, 650, 48, ad)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS CENAS", "DO DIA A DIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    recibo(c, 300, 260, aa)
    if aa > 0:
        pill(c, "sei quanto PAGUEI · quero quanto ANDEI", 480, 720, VOLTA, size=26, a=ep(t, C["04.a"] + 2.5, 0.4),
             anchor="center")
    ab = ep(t, C["04.b"], 0.5)
    placa(c, 1080, 230, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        selo(c, W / 2 + 40, 770, acc, "AS DUAS TÊM PEGADINHA", AMBER, -4, 30)


# ======================================================================
# bloco a: ida × volta
# ======================================================================

def b_ida(c, t, C, B):
    head(c, t, B["start"], "CAMINHO DE IDA", "DÃO O x, VOCÊ CALCULA", IDA)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 220, 1480, 90, BLUE, aa)
        linha(c, [("CAMINHO DE IDA", BLUE), (": o enunciado dá o x e pede o resultado", INK)], W / 2, 265, 36, aa)
    ab = ep(t, C["05.b"], 0.5)
    margem(c, "dão o x", 220, 380, ab)
    if ab > 0:
        linha(c, [("andei ", INK), ("10 km", IDA), (". Quanto paguei?", INK)], 470, 380, 38, ab, align="left")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        linha(c, [("P(10) = 5 + 2,5 · 10 = 5 + 25 = ", INK), ("R$ 30", GREEN)], 640, 520, 40, acc)
    ad = ep(t, C["05.d"], 0.5)
    maquina(c, 1400, 640, ad, entra="10 km", sai="R$ 30", prog=ep(t, C["05.d"] + 0.3, 2.6), s=0.7)


def b_volta(c, t, C, B):
    head(c, t, B["start"], "CAMINHO DE VOLTA", "DÃO O y, VOCÊ RESOLVE", VOLTA)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 220, 1480, 90, BLUE, aa)
        linha(c, [("CAMINHO DE VOLTA", BLUE), (": dão o y e pedem o x que o produziu", INK)], W / 2, 265, 36, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 345, 700, 120, PURPLE, ab)
        fmid(c, "f(x) = k", 570, 390, 50, "black", PURPLE, ab)
        fmid(c, "fórmula = valor dado", 570, 440, 26, "bold", GRAY, ab)
    acc = ep(t, C["06.c"], 0.5)
    margem(c, "dão o y", 220, 540, acc)
    if acc > 0:
        fmid(c, "5 + 2,5d = 30", 640, 640, 54, "black", INK, acc)
        linha(c, [("d = ", INK), ("10 km", GREEN)], 640, 740, 50, ep(t, C["06.d"] + 2.6, 0.4))
    ad = ep(t, C["06.d"], 0.5)
    maquina(c, 1400, 600, ad, entra="10 km", sai="R$ 30", prog=ep(t, C["06.d"] + 0.3, 2.6), volta=True, s=0.7)


def b_atalho_volta(c, t, C, B):
    head(c, t, B["start"], "ATALHO DA VOLTA", "DESFAÇA DE TRÁS PARA FRENTE", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        steps = [("d", INK), ("× 2,5", PURPLE), ("+ 5", PURPLE), ("R$ 30", INK)]
        xs = [380, 760, 1140, 1520]
        for k, (s_, col) in enumerate(steps):
            if k in (0, 3):
                chip_num(c, s_, xs[k], 330, IDA if k == 0 else VOLTA, aa, 40)
            else:
                fmid(c, s_, xs[k], 330, 44, "black", col, aa)
            if k < 3:
                fmid(c, "→", (xs[k] + xs[k + 1]) / 2 + (40 if k == 0 else 0) - (40 if k == 2 else 0) + 0, 330, 40,
                     "black", GRAY, aa)
        text(c, "a fórmula (ida)", W / 2, 410, 26, "bold", GRAY, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        K.atalho(c, 300, 450, 1320, 220, "ATALHO · VOLTA = O CONTRÁRIO, NA ORDEM CONTRÁRIA",
                 ["R$ 30  − 5  →  25   ÷ 2,5  →  10 km"], ab, 46)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        conferido(c, "confira substituindo: P(10) = 5 + 25 = 30", 560, 760, acc, True, 36)


# ======================================================================
# bloco b: por que 80 engana
# ======================================================================

def b_oitenta(c, t, C, B):
    head(c, t, B["start"], "DE ONDE SAIU O 80?", "A RESPOSTA DE OUTRA PERGUNTA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("P(", INK), ("30", RED), (") = 5 + 2,5 · ", INK), ("30", RED), (" = 5 + 75 = ", INK), ("80", RED)],
              W / 2, 300, 54, aa)
        pill(c, "o 30 entrou no lugar do d", W / 2, 390, RED, size=28, a=aa, anchor="center")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        selo(c, 1560, 250, ab, "PARECE CERTO", AMBER, -8, 30)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 460, 620, 150, 20, mix("#FFFFFF", RED, 0.10), acc)
        fmid(c, "R$ 80 = corrida de 30 km", 610, 515, 36, "black", RED, acc)
        fmid(c, "ninguém perguntou isso", 610, 570, 28, "bold", GRAY, acc)
        rrect(c, 1000, 460, 620, 150, 20, mix("#FFFFFF", GREEN, 0.10), acc)
        fmid(c, "R$ 30 → ? km", 1310, 515, 36, "black", GREEN, acc)
        fmid(c, "a pergunta de verdade", 1310, 570, 28, "bold", GRAY, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        text(c, "antes de qualquer conta, na margem:", W / 2, 690, 30, "bold", INK2, ad)
        margem(c, "dão o x", 640, 760, ad)
        margem(c, "dão o y", 1040, 760, ad)
        fmid(c, "ou", 960, 760, 32, "black", GRAY, ad)


# ======================================================================
# bloco c: funções por partes
# ======================================================================

def b_partes(c, t, C, B):
    head(c, t, B["start"], "FUNÇÃO POR PARTES", "A REGRA MUDA NO CAMINHO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 220, 1480, 90, BLUE, aa)
        linha(c, [("FUNÇÃO POR PARTES", BLUE), (": a regra muda conforme a faixa do x", INK)], W / 2, 265, 36, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 345, 600, 90, BLUE, ab)
        linha(c, [("FAIXA", BLUE), (" = um intervalo de valores", INK)], 520, 390, 32, ab)
    acc = ep(t, C["09.c"], 0.5)
    itens = [("até 1 h", "R$ 10"), ("de 1 h a 2 h", "R$ 14"), ("de 2 h a 3 h", "R$ 18")]
    ad = ep(t, C["09.d"], 0.5)
    gavetas(c, 1040, 360, acc, itens, aberta=1 if ad > 0.5 else -1)
    if ad > 0:
        regra(c, "ANTES DE CALCULAR, ACHE A GAVETA", 560, 640, ad, 34, PURPLE)
        pill(c, "x = 1 h 30 min → gaveta 2", 560, 730, BLUE, size=28, a=ad, anchor="center")


# ======================================================================
# bloco d: o estacionamento
# ======================================================================

def b_fracao(c, t, C, B):
    head(c, t, B["start"], "HORA OU FRAÇÃO?", "O RELÓGIO DO ESTACIONAMENTO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 220, 1480, 90, BLUE, aa)
        linha(c, [("FRAÇÃO DE HORA", BLUE), (": um pedaço de hora (5, 15, 40 minutos)", INK)], W / 2, 265, 36, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("cada hora adicional ", INK), ("ou qualquer pedaço dela", AMBER), (" = R$ 4", PURPLE)], W / 2, 400, 40,
              ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        cx, cy, r = 560, 620, 120
        c.drawCircle(cx, cy, r, paint(HAD, acc))
        c.drawCircle(cx, cy, r - 14, paint("#FFFFFF", acc))
        fill = ep(t, C["10.c"] + 0.6, 1.0) * 0.08
        pth = skia.Path(); pth.moveTo(cx, cy)
        pth.arcTo(skia.Rect(cx - r + 20, cy - r + 20, cx + r - 20, cy + r - 20), -90, 360 * fill + 0.01, False); pth.close()
        c.drawPath(pth, paint(AMBER, acc))
        line(c, cx, cy, cx, cy - 90, INK, acc, 8)
        c.drawCircle(cx, cy, 10, paint(INK, acc))
        text(c, "5 min", cx, cy + r + 50, 30, "bold", GRAY, acc)
        a2 = ep(t, C["10.c"] + 1.8, 0.5)
        if a2 > 0:
            text_mid(c, "=", 820, 620, 70, "black", INK, a2)
            rrect(c, 920, 560, 260, 120, 16, HAD, a2)
            fmid(c, "+ R$ 4", 1050, 620, 44, "black", "#FFFFFF", a2)
            regra(c, "COMEÇOU A HORA, PAGOU A HORA INTEIRA", 1380, 760, a2, 30, PURPLE)


def b_estac(c, t, C, B):
    head(c, t, B["start"], "2 h 15 min", "QUANTO PAGA?", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    margem(c, "dão o x", 220, 240, a0)
    if a0 > 0:
        ftext(c, "o tempo é a entrada: só calcular", 470, 252, 32, "bold", GRAY, a0, align="left")
    aa = ep(t, C["11.a"], 0.5)
    ab = ep(t, C["11.b"], 0.5)
    acc = ep(t, C["11.c"], 0.5)
    acende = 0.34 * min(1, aa * 2) + 0.33 * ab + 0.33 * acc
    relogio_estac(c, 360, 360, 135, a0, ep(t, C["11"], 2.0), bw=360, bh=130, acende=acende, fracao_selo=acc)
    if aa > 0:
        linha(c, [("1ª hora: ", INK), ("R$ 10", H1)], 420, 640, 36, aa, align="left")
    if ab > 0:
        linha(c, [("+ 1 hora completa: ", INK), ("R$ 4", HAD)], 420, 700, 36, ab, align="left")
    if acc > 0:
        linha(c, [("+ 15 min (fração): ", INK), ("R$ 4", HAD)], 420, 760, 36, acc, align="left")
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 660, 560, 120, 22, GREEN, 0.14 * ad)
        linha(c, [("10 + 2 · 4 = ", INK), ("R$ 18", GREEN)], 1360, 720, 50, ad)


def b_atalho_estac(c, t, C, B):
    head(c, t, B["start"], "ATALHO DO ESTACIONAMENTO", "EM TRÊS PASSOS", GREEN)
    card(c, *CARD_R)
    rows = [("12.a", "1", "tire a 1ª hora", "2 h 15 − 1 h = 1 h 15"),
            ("12.b", "2", "arredonde o resto PARA CIMA", "1 h 15 → 2 horas"),
            ("12.c", "3", "× tarifa adicional + 1ª hora", "10 + 2 · 4 = R$ 18")]
    boxed(c, 240, 220, 1440, 560, GREEN, ep(t, C["12"], 0.4), 0.06)
    for j, (cue, n, s, ex) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + j * 160 + d
        badge_num(c, n, 320, y - 12, a, 34, bg=GREEN)
        ftext(c, s, 380, y, 44, "black", INK, a, align="left")
        ftext(c, ex, 1620, y, 38, "bold", GREEN if j == 2 else INK2, a, align="right")


# ======================================================================
# bloco e: outras funções por partes
# ======================================================================

def b_outras(c, t, C, B):
    head(c, t, B["start"], "ONDE MAIS APARECE", "TARIFAS POR FAIXA", BLUE)
    card(c, *CARD_R)
    itens = [("13.a", "ÁGUA", "cada faixa de consumo, um preço", BLUE),
             ("13.b", "ENERGIA", "também por faixa", AMBER),
             ("13.c", "IMPOSTO", "a alíquota (%) muda com a renda", PURPLE)]
    for j, (cue, s, sub, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 260 + j * 480
        rrect(c, x, 250 + d, 420, 330, 24, mix("#FFFFFF", col, 0.10), a)
        text(c, s, x + 210, 360 + d, 54, "black", col, a)
        for k in range(3):
            rrect(c, x + 60 + k * 105, 420 + d + (2 - k) * 20, 90, 60 + k * 20, 8, col, a * (0.4 + 0.25 * k))
        ftext(c, sub, x + 210, 640 + d, 26, "bold", INK2, a)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        pill(c, "série própria mais adiante · por enquanto: ACHE A GAVETA", W / 2, 760, GREEN, size=30, a=ad,
             anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "CAMINHO DE VOLTA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 215, 1400, 120, 24, "#F7F7F5", aa)
        linha(c, [("academia: ", INK), ("C(m) = 50 + 80m", PURPLE)], W / 2, 260, 46, aa)
        ftext(c, "matrícula R$ 50 · R$ 80 por mês", W / 2, 318, 26, "bold", GRAY, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("pagou ", INK), ("R$ 530", VOLTA), (" no total → quantos meses?", INK)], W / 2, 400, 40, ab)
    pause_timer(c, t, C["14.end"] - 1.9, W / 2, 580)
    if t < C["15"]:
        return
    a1 = ep(t, C["15.a"], 0.4)
    margem(c, "dão o y", 260, 490, a1)
    if a1 > 0:
        ftext(c, "deram o total, a saída", 510, 502, 30, "bold", GRAY, a1, align="left")
    ab2 = ep(t, C["15.b"], 0.5)
    if ab2 > 0:
        fmid(c, "50 + 80m = 530", 640, 600, 46, "black", INK, ab2)
        linha(c, [("− 50:  ", GRAY), ("80m = 480", INK)], 640, 680, 40, ep(t, C["15.b"] + 2.6, 0.4))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("÷ 80:  ", GRAY), ("m = 6 meses", GREEN)], 640, 760, 46, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 560, 560, 200, 20, "#FFFFFF", ad, shadow=True)
        fmid(c, "80 · 6 + 50", 1360, 620, 40, "black", INK, ad)
        fmid(c, "= 480 + 50 = 530", 1360, 680, 36, "black", INK, ad)
        conferido(c, "bateu", 1290, 740, ep(t, C["15.d"] + 3.0, 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Dão o x: calcule. Dão o y: resolva a equação.",
          "Em função por partes, primeiro ache a faixa.",
          "Hora ou fração: começou a hora, paga a hora."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Calcular f(30) quando o enunciado dá f(x) = 30", "o 30 está ali, pronto para entrar na fórmula",
          "o 30 é a SAÍDA: monte a equação e resolva"),
         ("Ignorar a fração: 1 h 30 min = só R$ 10", "meia hora não chega a ser uma hora",
          "\"ou fração\": a 2ª hora começou · 10 + 4 = R$ 14"),
         ("Cobrar a fração proporcionalmente: 10 + 2 = R$ 12", "parece justo pagar só pelo tempo usado",
          "\"ou fração\" = hora inteira · continua R$ 14"),
         ("Cobrar a 1ª hora como adicional: 10 + 2 · 4 = R$ 18", "são duas horas começadas",
          "a 1ª hora já está nos R$ 10 · tire a 1ª hora antes de contar")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19", "20"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

ENUN9 = ("Em uma cidade, o preço de uma corrida de táxi, em reais, é dado por P(d) = 5 + 2,5d, em que d é a distância "
         "percorrida em quilômetros. Um passageiro pagou R$ 30,00 por uma corrida. A distância percorrida foi de")
ALTS9 = [("A", "6 km", "30 ÷ 5: dividiu pela tarifa fixa", RED), ("B", "10 km", "", GREEN),
         ("C", "12 km", "30 ÷ 2,5: esqueceu o fixo", RED), ("D", "14 km", "somou o 5 em vez de tirar", RED),
         ("E", "80 km", "calculou P(30): a pegadinha", AMBER)]

ENUN2 = ("Um estacionamento cobra R$ 10,00 pela primeira hora e R$ 4,00 por hora adicional ou fração de hora. Um cliente "
         "deixou o carro estacionado por 3 horas e 20 minutos. Ele pagou")
ALTS2 = [("A", "R$ 18,00", "ignorou a fração", RED), ("B", "R$ 18,80", "3 h 20 lido como 3,2 h", RED),
         ("C", "R$ 19,33", "proporcional: 2,33 h", RED), ("D", "R$ 22,00", "", GREEN),
         ("E", "R$ 26,00", "1ª hora também como adicional", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · EU FAÇO", "O CAMINHO DE VOLTA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [(ENUN9, INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS9, 1010, 260, 660, 44, C["22.ok"], "B", cues_in, cues_x, gap=34)
    if t < C["22"]:
        pause_timer(c, t, C["21.end"] - 1.9, 1340, 800)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["22"], 0.4))
    margem(c, "dão o y", 200, y0 + 50, ep(t, C["22"], 0.4))
    linha(c, [("5 + 2,5d = 30  →  2,5d = 25", INK)], 550, y0 + 125, 30, ep(t, C["22.a"], 0.4))
    linha(c, [("÷ 2,5:  ", GRAY), ("d = 10 km", GREEN)], 550, y0 + 190, 34, ep(t, C["22.b"], 0.4))
    conferido(c, "P(10) = 5 + 25 = 30", 240, y0 + 260, ep(t, C["22.c"], 0.4), True, 28)


def b_q2(c, t, C, B):
    head_seq(c, t, C, [("24", "QUESTÃO 2 · VOCÊ FAZ", "PAUSE E RESOLVA", GREEN),
                       ("25", "CONFERINDO", "ACHE A GAVETA", GREEN), ("26", "E AS ERRADAS?", "UMA POR UMA", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [(ENUN2, INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS2, 1010, 260, 660, 44, C["25.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["25"]:
        pause_timer(c, t, C["24.end"] - 1.9, 1340, 800)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["25"], 0.4))
    margem(c, "dão o x", 200, y0 + 50, ep(t, C["25"], 0.4))
    aa = ep(t, C["25.a"], 0.4)
    ab = ep(t, C["25.b"], 0.5)
    relogio_estac(c, 200, y0 + 105, 200, aa, 1.0, bw=160, bh=86, acende=0.25 + 0.75 * ab, fracao_selo=ab,
                  mostra_preco=True)
    linha(c, [("10 + 3 · 4 = ", INK), ("R$ 22", GREEN)], 550, y0 + 290, 40, ep(t, C["25.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O GRÁFICO", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        cx, cy = 640, 470
        line(c, 340, cy, 940, cy, GRAY, aa, 4)
        line(c, cx, 220, cx, 720, GRAY, aa, 4)
        c.drawCircle(cx, cy, 170, paint(BLUE, aa, stroke=10))
        text(c, "é gráfico de função?", 640, 790, 36, "black", INK, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        x = lerp(380, 600, ep(t, C["28.b"] + 0.5, 1.5))
        rrect(c, x - 16, 200, 32, 540, 8, AMBER, ab * 0.85)
        text(c, "a régua em pé", 1340, 430, 44, "black", AMBER, ab)
        text(c, "um teste de 1 segundo", 1340, 500, 34, "bold", GRAY, ab)
    pill(c, "ep. 4 · o gráfico: teste da reta vertical", 1340, 640, PURPLE, size=30, a=ep(t, C["28.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Já pagou hora cheia por poucos minutos?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, ida=b_ida, volta=b_volta,
              atalho_volta=b_atalho_volta, oitenta=b_oitenta, partes=b_partes, fracao=b_fracao, estac=b_estac,
              atalho_estac=b_atalho_estac, outras=b_outras, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q9=b_q9, q2=b_q2, ponte=b_ponte, cta=b_cta)
