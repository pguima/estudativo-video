"""Visual — Determinantes e Sistemas Lineares, Episódio 4: uma, infinitas ou nenhuma (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: sistema() (chave + equações), semaforo() (verde = D ≠ 0, amarelo = D = 0), retas() (o
mini-plano com duas retas: cruzam, paralelas ou coincidentes), tabela() (condição → classificação), porta() (a porta
(0, 0) do homogêneo, sempre aberta), camisetas() (gêmeas de camiseta igual × brigadas de costas).
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
_s = importlib.util.spec_from_file_location("comum049", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_determinantes_ep4_uma_infinitas_nenhuma.mp4"
CARD_R = K.CARD_R
LUZ_VERDE = "#1F9D55"
LUZ_AMAR = "#E8A317"


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


def chave(c, x, y0, y1, a, col=INK, sw=5):
    """a chave '{' do sistema, de y0 a y1"""
    if a <= 0:
        return
    ym = (y0 + y1) / 2
    d = 18
    p = skia.Path()
    p.moveTo(x + d, y0); p.quadTo(x, y0, x, y0 + d)
    p.lineTo(x, ym - d); p.quadTo(x, ym, x - d, ym); p.quadTo(x, ym, x, ym + d)
    p.lineTo(x, y1 - d); p.quadTo(x, y1, x + d, y1)
    c.drawPath(p, paint(col, a, stroke=sw))


def sistema(c, eqs, x, cy, size, a, cores=None, alfas=None, gap=None, col_chave=INK):
    """sistema com chave: eqs = lista de strings ou de [(trecho, cor)]; x = borda esquerda. Devolve a largura."""
    if a <= 0:
        return 0
    gap = gap or size * 1.45
    n = len(eqs)
    y0 = cy - (n - 1) * gap / 2
    chave(c, x, y0 - size * 0.75, y0 + (n - 1) * gap + size * 0.75, a, col_chave)
    wmax = 0
    for k, e in enumerate(eqs):
        aa = a * (alfas[k] if alfas else 1.0)
        partes = e if isinstance(e, list) else [(e, (cores or {}).get(k, INK))]
        wmax = max(wmax, linha(c, partes, x + 34, y0 + k * gap, size, aa, align="left"))
    return wmax + 34


def semaforo(c, cx, cy, s, luz, a, acende=1.0):
    """semáforo vertical: luz = 'verde' | 'amarelo' | None; acende 0 → 1"""
    if a <= 0:
        return
    w, h = s * 0.9, s * 2.5
    rrect(c, cx - w / 2, cy - h / 2, w, h, s * 0.25, "#2B2F36", a, shadow=True)
    cores = [("vermelho", "#D64545"), ("amarelo", LUZ_AMAR), ("verde", LUZ_VERDE)]
    for k, (nome, col) in enumerate(cores):
        yy = cy - h / 2 + s * 0.42 + k * s * 0.82
        on = acende if nome == luz else 0.0
        if on > 0:
            c.drawCircle(cx, yy, s * 0.42, paint(col, a * 0.35 * on))
        c.drawCircle(cx, yy, s * 0.3, paint(mix("#4A505A", col, on), a))


def retas(c, x0, y0, w, h, tipo, a, prog_=1.0, col1=BLUE, col2=PURPLE):
    """mini-plano com duas retas: tipo = 'cruzam' | 'paralelas' | 'coincidentes'"""
    if a <= 0:
        return
    rrect(c, x0, y0, w, h, 18, "#FFFFFF", a, shadow=True)
    line(c, x0 + 30, y0 + h - 40, x0 + w - 20, y0 + h - 40, "#C9CED6", a, 2)
    line(c, x0 + 50, y0 + 20, x0 + 50, y0 + h - 20, "#C9CED6", a, 2)
    xa, xb = x0 + 70, x0 + w - 40
    ya, yb = y0 + h - 70, y0 + 50

    def seg(dy, col, sw=6):
        xe = lerp(xa, xb, prog_)
        ye = lerp(ya + dy, yb + dy, prog_)
        line(c, xa, ya + dy, xe, ye, col, a, sw)
    if tipo == "cruzam":
        seg(0, col1)
        xe = lerp(xa, xb, prog_)
        line(c, xa, yb + 10, xe, lerp(yb + 10, ya - 10, prog_), col2, a, 6)
        if prog_ >= 1:
            c.drawCircle((xa + xb) / 2, (ya + yb) / 2, 11, paint(GREEN, a))
    elif tipo == "paralelas":
        seg(-34, col1); seg(34, col2)
    else:
        seg(0, col2, 14); seg(0, col1, 5)


def tabela(c, x, y, w, linhas_, a, alfas=None, titulo=("CONDIÇÃO", "CLASSIFICAÇÃO"), size=32, rh=78):
    """tabela condição → classificação: linhas_ = [(condição, classificação, cor)]"""
    if a <= 0:
        return
    h = 64 + len(linhas_) * rh
    rrect(c, x, y, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 64, 22, PURPLE, a * 0.14)
    text(c, titulo[0], x + w * 0.3, y + 42, 22, "black", PURPLE, a, tracking=2)
    text(c, titulo[1], x + w * 0.78, y + 42, 22, "black", PURPLE, a, tracking=2)
    for k, (cond, cls, col) in enumerate(linhas_):
        aa = a * (alfas[k] if alfas else 1.0)
        if aa <= 0:
            continue
        yy = y + 64 + k * rh + rh / 2
        if k:
            line(c, x + 20, yy - rh / 2, x + w - 20, yy - rh / 2, "#E3E6EB", aa, 2)
        fmid(c, cond, x + w * 0.3, yy, size, "black", INK, aa)
        chip(c, cls, x + w * 0.78, yy, col, aa, size * 0.8)


def porta(c, cx, cy, s, a, aberta=1.0, col=None):
    """a porta (0, 0) do homogêneo: batente + folha que gira para fora; letreiro (0, 0)"""
    if a <= 0:
        return
    col = col or GREEN
    w, h = s, s * 1.7
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0 - 12, y0 - 12, w + 24, h + 12, 10, mix("#FFFFFF", col, 0.25), a)
    rrect(c, x0, y0, w, h, 6, "#FFF8E6", a)
    fw = w * (1 - 0.72 * ease_io(aberta))
    rrect(c, x0, y0, fw, h, 6, col, a)
    c.drawCircle(x0 + fw - 16, cy, 7, paint("#FFFFFF", a))
    rrect(c, cx - w * 0.62, y0 - 78, w * 1.24, 58, 14, "#FFFFFF", a, shadow=True)
    fmid(c, "(0, 0)", cx, y0 - 49, 34, "black", col, a)


def camisetas(c, cx, cy, s, tipo, a):
    """duas figurinhas: 'gemeas' (mesma camiseta, lado a lado) ou 'brigadas' (de costas, cores diferentes)"""
    if a <= 0:
        return
    for k in (-1, 1):
        x = cx + k * s * 0.7
        col = BLUE if tipo == "gemeas" else (BLUE if k < 0 else RED)
        c.drawCircle(x, cy - s * 0.55, s * 0.28, paint("#F2C9A0", a))
        p = skia.Path()
        p.moveTo(x - s * 0.5, cy - s * 0.2); p.lineTo(x + s * 0.5, cy - s * 0.2)
        p.lineTo(x + s * 0.4, cy + s * 0.7); p.lineTo(x - s * 0.4, cy + s * 0.7); p.close()
        c.drawPath(p, paint(col, a))
    if tipo == "brigadas":
        fmid(c, "≠", cx, cy - s * 0.1, s * 0.7, "black", RED, a)
    else:
        fmid(c, "=", cx, cy - s * 0.1, s * 0.7, "black", GREEN, a)


GEM = ["x + 2y = 3", "2x + 4y = 6"]
BRI = ["x + 2y = 3", "2x + 4y = 7"]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DETERMINANTES E SISTEMAS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    sistema(c, ["x + y + z = 6", "x − y + 2z = 5", "2x + 3z = 11"], 220, 470, 50, aa)
    if aa > 0:
        rrect(c, 260, 650, 480, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("achou: ", INK2), ("(1, 2, 3)", BLUE)], 500, 705, 46, aa)
        selo(c, 1300, 380, ep(t, C["01.a"] + 4.0, 0.5), "“SOLUÇÃO ÚNICA!”", AMBER, -4, 40)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        strike(c, 1080, 380, 1520, 380, ab, RED)
        chip(c, "INFINITAS SOLUÇÕES", 1300, 540, RED, ab, 44)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        semaforo(c, 1300, 730, 54, "amarelo", acc, ep(t, C["01.c"] + 0.8, 0.5))
        text(c, "o determinante avisava", 1500, 740, 30, "black", INK2, acc, align="left")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "classificar qualquer sistema pelo determinante", "sem resolver"),
            ("02.b", "discutir um sistema com letras no lugar dos números", "k e m: os botões")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    tipos = [("cruzam", "1 solução"), ("paralelas", "nenhuma"), ("coincidentes", "infinitas")]
    for k, (tp, rot) in enumerate(tipos):
        a_ = ep(t, C["03.a"] + k * 1.4, 0.5)
        x = 260 + k * 480
        retas(c, x, 220, 400, 260, tp, a_, ep(t, C["03.a"] + k * 1.4, 0.8))
        if a_ > 0:
            text(c, rot, x + 200, 530, 34, "black", [GREEN, RED, BLUE][k], a_)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 600, 640, 150, 24, "#FFFFFF", ab, shadow=True)
        pill(c, "EPISÓDIO 1", 300, 640, PURPLE, size=22, a=ab)
        linha(c, [("det 2 × 2 = ", INK), ("ad − bc", PURPLE)], 580, 705, 42, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 600, 640, 150, 24, "#FFFFFF", acc, shadow=True)
        pill(c, "2º GRAU", 1060, 640, GREEN, size=22, a=acc)
        linha(c, [("k² = 4  →  ", INK), ("k = 2  ou  k = −2", GREEN)], 1340, 705, 40, acc)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "A MÁQUINA DE MISTURAS", "DOIS BOTÕES: k E m", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    if a0 > 0:
        rrect(c, 230, 260, 620, 460, 36, "#E9EDF3", a0, shadow=True)
        for k, (nome, ang) in enumerate((("k", -40), ("m", 25))):
            x = 400 + k * 280
            c.drawCircle(x, 420, 86, paint("#FFFFFF", a0))
            c.drawCircle(x, 420, 86, paint(PURPLE, a0, stroke=6))
            c.save(); c.translate(x, 420); c.rotate(ang + 60 * ep(t, C["04.a"], 1.2))
            line(c, 0, 0, 0, -66, PURPLE, a0, 10)
            c.restore()
            fmid(c, nome, x, 560, 60, "black", PURPLE, a0)
        text(c, "MISTURA", 540, 680, 26, "black", INK2, a0, tracking=2)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        sistema(c, ["x + 2y = 3", "2x + ky = m"], 1000, 340, 46, aa)
    ab = ep(t, C["04.b"], 0.5)
    for k, (s_, col) in enumerate((("UMA resposta?", GREEN), ("VÁRIAS?", BLUE), ("NENHUMA?", RED))):
        chip(c, s_, 1150 + (k - 1) * 260, 540, col, ep(t, C["04.b"] + 0.8 * k, 0.4) * (ab > 0), 30)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "basta UM número: o DETERMINANTE", 1250, 700, acc, 34, BLUE)


# ======================================================================
# bloco a — a tabela e o semáforo
# ======================================================================

def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("05", "QUANTAS SOLUÇÕES?", "SPD · SPI · SI", BLUE), ("06", "O SEMÁFORO", "D ≠ 0 VERDE · D = 0 AMARELO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        defs = [("05.a", "SPD", "possível e determinado", "UMA solução", GREEN, "cruzam"),
                ("05.b", "SPI", "possível e indeterminado", "INFINITAS", BLUE, "coincidentes"),
                ("05.c", "SI", "impossível", "NENHUMA", RED, "paralelas")]
        for k, (cue, sig, nome, qt, col, tp) in enumerate(defs):
            a, d = rise(t, C[cue])
            y = 250 + k * 170 + d
            if a > 0:
                rrect(c, 220, y, 1480, 140, 24, "#FFFFFF", a, shadow=True)
                chip(c, sig, 330, y + 70, col, a, 40)
                text(c, nome, 450, y + 62, 40, "black", BLUE, a, align="left")
                text(c, qt, 450, y + 110, 30, "bold", INK2, a, align="left")
                retas(c, 1430, y + 12, 240, 116, tp, a)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            pill(c, "quem decide primeiro: D, o determinante dos coeficientes", W / 2, 790, PURPLE, size=28, a=ad,
                 anchor="center")
        return
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    if aa > 0:
        semaforo(c, 420, 470, 90, "verde" if ab <= 0 else "amarelo", 1.0,
                 ep(t, C["06.a"] + 0.6, 0.5) if ab <= 0 else ep(t, C["06.b"], 0.5))
        rrect(c, 640, 280, 1040, 150, 24, mix("#FFFFFF", LUZ_VERDE, 0.12), aa)
        linha(c, [("D ≠ 0", LUZ_VERDE), ("  →  uma solução só (SPD)", INK)], 1160, 355, 46, aa)
    if ab > 0:
        rrect(c, 640, 470, 1040, 150, 24, mix("#FFFFFF", LUZ_AMAR, 0.16), ab)
        linha(c, [("D = 0", AMBER), ("  →  pare e olhe as equações", INK)], 1160, 545, 46, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        retas(c, 660, 660, 260, 150, "paralelas", acc)
        retas(c, 950, 660, 260, 150, "coincidentes", acc)
        text(c, "mesma inclinação", 1480, 725, 30, "black", PURPLE, acc)
        text(c, "→ D = 0", 1480, 775, 30, "black", PURPLE, acc)


# ======================================================================
# bloco b — gêmeas e brigadas
# ======================================================================

def b_gemeas(c, t, C, B):
    head_seq(c, t, C, [("07", "D = 0 NÃO É “IMPOSSÍVEL”", "GÊMEAS × BRIGADAS", AMBER), ("08", "CONFERINDO COM CONTA", "D, Dx E Dy", PURPLE),
                       ("09", "ATALHO", "O FATOR DOS DOIS LADOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        ab = ep(t, C["07.b"], 0.5)
        sistema(c, GEM, 230, 330, 46, aa)
        if aa > 0:
            pill(c, "× 2 inteirinha", 760, 330, PURPLE, size=24, a=ep(t, C["07.a"] + 4.5, 0.4))
        if ab > 0:
            camisetas(c, 1080, 330, 80, "gemeas", ab)
            retas(c, 1300, 230, 320, 200, "coincidentes", ab)
            chip(c, "GÊMEAS · compatíveis · SPI", 960, 480, BLUE, ab, 30)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            sistema(c, [[("x + 2y = 3", INK)], [("2x + 4y = ", INK), ("7", RED)]], 230, 640, 46, acc)
            pill(c, "o dobro daria 6", 760, 640, AMBER, size=24, a=acc)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            camisetas(c, 1080, 640, 80, "brigadas", ad)
            retas(c, 1300, 560, 320, 200, "paralelas", ad)
            chip(c, "BRIGADAS · contraditórias · SI", 960, 790, RED, ad, 30)
        return
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            rrect(c, 220, 230, 1480, 120, 24, mix("#FFFFFF", PURPLE, 0.08), aa)
            text(c, "Dx: troque a coluna do x pelos termos independentes (episódio 3)", W / 2, 302, 32, "black", PURPLE, aa)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            sistema(c, BRI, 250, 470, 40, ab)
            linha(c, [("Dx = 3 · 4 − 2 · 7 = ", INK), ("−2", RED), ("  ≠ 0", RED)], 1180, 470, 44, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            regra(c, "2 × 2:  D = 0  e  Dx ou Dy ≠ 0  →  SI", W / 2, 620, acc, 40)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            linha(c, [("gêmeas:  Dx = 0  e  Dy = 0", BLUE), ("  →  compare antes de concluir", INK2)], W / 2, 750, 34, ad)
        return
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 1060, 230, 640, 170, "ATALHO", ["fator do lado ESQUERDO", "aplique no lado DIREITO"], aa, 30)
    sistema(c, GEM, 260, 420, 54, 1.0, cores={1: mix(INK, BLUE, aa)})
    if aa > 0:
        arrow(c, 600, 380, 600, 450, PURPLE, aa, 5, 14)
        chip(c, "× 2", 690, 415, PURPLE, aa, 30)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        linha(c, [("3 × 2 = ", INK), ("6", GREEN), ("  ✓", GREEN)], 1380, 520, 48, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        chip(c, "bateu → GÊMEAS (SPI)", 760, 700, BLUE, acc, 34)
        chip(c, "não bateu → BRIGADAS (SI)", 1280, 700, RED, acc, 34)


# ======================================================================
# bloco c — discussão com parâmetro
# ======================================================================

TAB_C = [("k ≠ 9", "SPD", GREEN), ("k = 9  e  m = 6", "SPI", BLUE), ("k = 9  e  m ≠ 6", "SI", RED)]


def b_parametro(c, t, C, B):
    head_seq(c, t, C, [("10", "PARÂMETRO", "DISCUTIR O SISTEMA", BLUE), ("11", "PASSO 1", "O DETERMINANTE", PURPLE),
                       ("12", "PASSO 2", "O CASO D = 0", AMBER), ("13", "ATALHO", "DUAS PERGUNTAS, NESSA ORDEM", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12", "13"])
    eqs = [[("x + 3y = 2", INK)], [("3x + ", INK), ("k", PURPLE), ("y = ", INK), ("m", PURPLE)]]
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "PARÂMETRO: um número ajustável, como um botão", W / 2, 280, 36, "black", BLUE, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            text(c, "DISCUTIR: dizer se é SPD, SPI ou SI para cada valor", W / 2, 380, 34, "black", BLUE, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            sistema(c, eqs, 700, 600, 56, acc)
        return
    if sid == "11":
        sistema(c, eqs, 230, 330, 46, 1.0)
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            linha(c, [("D = 1 · k − 3 · 3 = ", INK), ("k − 9", PURPLE)], 1150, 330, 48, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            semaforo(c, 330, 640, 60, "verde", ab, ep(t, C["11.b"] + 0.6, 0.4))
        tabela(c, 560, 470, 1100, TAB_C, ab, alfas=[1, 0, 0])
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            pill(c, "o m nem entrou na conta", 1110, 790, AMBER, size=26, a=acc, anchor="center")
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        sistema(c, [[("x + 3y = 2", INK)], [("3x + ", INK), ("9", AMBER), ("y = ", INK), ("m", PURPLE)]], 230, 330, 46, 1.0)
        semaforo(c, 330, 640, 60, "amarelo", 1.0, 1.0)
        if aa > 0:
            chip(c, "× 3 no lado esquerdo", 1050, 290, PURPLE, aa, 30)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("2 × 3 = ", INK), ("6", GREEN)], 1450, 290, 44, ab)
        tabela(c, 560, 430, 1100, TAB_C, 1.0, alfas=[1, ab, ep(t, C["12.c"], 0.5)])
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            pill(c, "sempre a tabela: condição → classificação", 1110, 790, PURPLE, size=26, a=ad, anchor="center")
        return
    aa = ep(t, C["13.a"], 0.5)
    ab = ep(t, C["13.b"], 0.5)
    K.atalho(c, 260, 240, 1400, 360, "ATALHO", ["1º  ache o valor que ZERA o D  (o resto é SPD)",
                                                 "2º  só nesse valor, compare o lado direito"], max(aa, ab), 38)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        chip(c, "duas perguntas, nessa ordem", W / 2, 720, GREEN, acc, 36)


# ======================================================================
# bloco d — 3 × 3 e escalonamento
# ======================================================================

def b_escalona(c, t, C, B):
    head_seq(c, t, C, [("14", "SISTEMA 3 × 3", "D = k − 2", PURPLE), ("15", "ESCALONAR", "A LINHA 0 = 0", BLUE),
                       ("16", "E SE FOSSE 9?", "A LINHA 0 = 2", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    ult = "9" if sid == "16" else "7"
    kk = "k" if sid == "14" else "2"
    eqs = [[("x + y + z = 3", INK)], [("x + 2y + z = 4", INK)],
           [("2x + 3y + ", INK), (kk + "z", PURPLE if kk == "k" else INK), (" = ", INK), (ult, RED if ult == "9" else INK)]]
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        sistema(c, eqs, 230, 420, 46, aa)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            linha(c, [("D = ", INK), ("k − 2", PURPLE), ("  (Laplace)", GRAY)], 1150, 330, 48, ab)
            linha(c, [("k ≠ 2  →  ", INK), ("SPD", GREEN)], 1150, 430, 44, ep(t, C["14.b"] + 3.0, 0.5))
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            semaforo(c, 1000, 650, 54, "amarelo", acc, ep(t, C["14.c"] + 0.6, 0.4))
            text(c, "k = 2  →  ESCALONAR", 1350, 665, 40, "black", AMBER, acc)
        return
    sistema(c, eqs, 230, 330, 40, 1.0)
    aa = ep(t, C[f"{sid}.a"], 0.5)
    if sid == "15":
        if aa > 0 or t >= C["15"]:
            a0 = ep(t, C["15"], 0.5)
            text(c, "ESCALONAR: zerar a 1ª incógnita nas equações de baixo", 1240, 250, 28, "black", BLUE, a0)
        a1, a2, a3 = ep(t, C["15.a"], 0.5), ep(t, C["15.b"], 0.5), ep(t, C["15.c"], 0.5)
        rows = [(a1, "L2 − L1:", "y = 1", BLUE), (a2, "L3 − 2·L1:", "y = 1", BLUE), (a3, "subtraindo:", "0 = 0", GREEN)]
        for k, (a_, lab, res, col) in enumerate(rows):
            if a_ > 0:
                y = 420 + k * 100
                rrect(c, 900 + k * 60, y - 42, 760 - k * 60, 84, 18, mix("#FFFFFF", col, 0.10), a_)
                text(c, lab, 940 + k * 60, y + 12, 34, "black", INK2, a_, align="left")
                fmid(c, res, 1440, y, 46, "black", col, a_)
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            chip(c, "EQUAÇÃO REDUNDANTE → SPI", 1280, 760, BLUE, ad, 32)
        return
    a1, a2, a3 = aa, ep(t, C["16.b"], 0.5), ep(t, C["16.c"], 0.5)
    rows = [(1.0, "L2 − L1:", "y = 1", BLUE), (a1, "L3 − 2·L1:", "y = 3", RED), (a2, "subtraindo:", "0 = 2", RED)]
    for k, (a_, lab, res, col) in enumerate(rows):
        if a_ > 0:
            y = 420 + k * 100
            rrect(c, 900 + k * 60, y - 42, 760 - k * 60, 84, 18, mix("#FFFFFF", col, 0.10), a_)
            text(c, lab, 940 + k * 60, y + 12, 34, "black", INK2, a_, align="left")
            fmid(c, res, 1440, y, 46, "black", col, a_)
    if a3 > 0:
        chip(c, "CONTRADIÇÃO → SI", 1280, 760, RED, a3, 34)


# ======================================================================
# bloco e — homogêneo
# ======================================================================

def b_homogeneo(c, t, C, B):
    head_seq(c, t, C, [("17", "SISTEMA HOMOGÊNEO", "A PORTA (0, 0)", GREEN), ("18", "DOIS EXEMPLOS", "D ≠ 0 × D = 0", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18"])
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            sistema(c, [[("ax + by = ", INK), ("0", GREEN)], [("cx + dy = ", INK), ("0", GREEN)]], 260, 360, 50, aa)
            text(c, "HOMOGÊNEO: todo o lado direito é zero", 520, 560, 30, "black", BLUE, aa)
        ab = ep(t, C["17.b"], 0.5)
        if ab > 0:
            porta(c, 1150, 480, 170, ab, ep(t, C["17.b"] + 2.5, 0.8))
            text(c, "SOLUÇÃO TRIVIAL", 1150, 760, 30, "black", GREEN, ab)
        acc = ep(t, C["17.c"], 0.5)
        if acc > 0:
            selo(c, 1520, 330, acc, "NUNCA IMPOSSÍVEL", GREEN, 6, 30)
        ad = ep(t, C["17.d"], 0.5)
        if ad > 0:
            regra(c, "outras soluções  ⟺  D = 0", 520, 690, ad, 36)
        return
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        sistema(c, ["x + 2y = 0", "3x + 5y = 0"], 230, 340, 40, aa)
        linha(c, [("D = 5 − 6 = ", INK), ("−1", LUZ_VERDE)], 860, 340, 40, aa, align="left")
        semaforo(c, 1380, 340, 40, "verde", aa, ep(t, C["18.a"] + 1.0, 0.4))
        text(c, "só (0, 0)", 1560, 352, 32, "black", INK2, aa, align="left")
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        sistema(c, ["2x − y = 0", "6x − 3y = 0"], 230, 600, 40, ab)
        linha(c, [("D = −6 + 6 = ", INK), ("0", AMBER)], 860, 600, 40, ab, align="left")
        semaforo(c, 1380, 600, 40, "amarelo", ab, ep(t, C["18.b"] + 1.0, 0.4))
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        chip(c, "outras: (1, 2) ✓", 1600, 610, GREEN, acc, 28)


# ======================================================================
# nós fazemos
# ======================================================================

NF = ["2x − y = 1", "4x − 2y = 5"]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "D, FATOR E Dx", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["19", "20"])
    aa = ep(t, C["19.a"], 0.5)
    if sid == "19":
        sistema(c, NF, 660, 420, 64, aa)
        if aa > 0:
            text(c, "SPD, SPI ou SI?", W / 2, 640, 40, "black", PURPLE, aa)
        pause_timer(c, t, C["19.end"] - 1.9, W / 2, 750)
        return
    sistema(c, NF, 230, 330, 46, 1.0)
    a1 = ep(t, C["20.a"], 0.5)
    if a1 > 0:
        linha(c, [("D = 2·(−2) − (−1)·4 = −4 + 4 = ", INK), ("0", AMBER)], 1150, 290, 38, a1)
        semaforo(c, 340, 650, 54, "amarelo", a1, ep(t, C["20.a"] + 4.0, 0.4))
    a2 = ep(t, C["20.b"], 0.5)
    if a2 > 0:
        linha(c, [("fator × 2:   1 × 2 = 2  ≠  ", INK), ("5", RED)], 1150, 420, 40, a2)
        chip(c, "BRIGADAS → SI", 1150, 520, RED, a2, 34)
    a3 = ep(t, C["20.c"], 0.5)
    if a3 > 0:
        linha(c, [("Dx = 1·(−2) − (−1)·5 = −2 + 5 = ", INK), ("3", RED), ("  ≠ 0", RED)], 1150, 660, 36, a3)
        conf = ep(t, C["20.c"] + 4.0, 0.4)
        if conf > 0:
            check_icon(c, 1000, 745, 22, conf, GREEN)
            text(c, "impossível mesmo", 1040, 760, 30, "black", GREEN, conf, align="left")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["D diferente de zero: uma solução só.",
          "D igual a zero: gêmeas dão infinitas, brigadas dão nenhuma.",
          "Homogêneo nunca é impossível."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("D = 0, logo impossível", "zero lembra “nada”, nenhuma solução",
          "D = 0 é só o sinal amarelo: as gêmeas têm D = 0 e infinitas soluções"),
         ("Achei uma solução, então é SPD", "a conta fechou e a gente para de procurar",
          "nas gêmeas, (1, 1) e (3, 0) servem: achar uma não prova que é a única"),
         ("Homogêneo pode ser impossível", "todo sistema parece poder dar contradição",
          "com o lado direito todo zero, (0, 0) sempre serve: a porta está sempre aberta"),
         ("k² = 4  →  só k = 2", "o 2 vem primeiro na cabeça",
          "(−2)² também dá 4: são duas raízes, 2 e −2")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=240, size=26, w=1000):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 10
        y += 6
    return y


ALTS4 = [("A", "k = 4 e m ≠ 6.", "", GREEN), ("B", "k = 4 e m = 6.", "", RED),
         ("C", "k ≠ 4, para qualquer valor de m.", "", RED),
         ("D", "k = −4 e m ≠ 6.", "", RED), ("E", "k = 2 e m ≠ 3.", "", RED)]
MOT4 = [("xb", "B: gêmeas, infinitas (SPI)"), ("xc", "C: sinal verde, solução única (SPD)"),
        ("xd", "D: somou no determinante (k + 4)"), ("xe", "E: exigiu equações idênticas")]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "SISTEMA COM PARÂMETRO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    _enunciado(c, [("Um técnico descreve uma mistura pelo sistema abaixo, em que k e m são constantes reais "
                    "ajustáveis. O sistema não tem solução exatamente quando", INK)], a0, 236, 26, 900)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
          align="left")
    sistema(c, ["x + 2y = 3", "2x + ky = m"], 200, 420, 38, ep(t, C["26.a"] + 3.0, 0.4))
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS4, 1140, 250, 580, 28, C["27.ok"], "A", cues_in, cues_x, gap=22)
    if t < C["27"]:
        return
    if t >= C["28"]:
        for k, (q, s_) in enumerate(MOT4):
            a_ = ep(t, C[f"28.{q}"], 0.4)
            if a_ > 0:
                check_icon(c, 200, 560 + k * 60, 22, a_, RED, "x")
                ftext(c, s_, 240, 576 + k * 60, 28, "black", RED, a_, align="left")
        return
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        linha(c, [("D = k − 4", PURPLE), ("   k ≠ 4 → SPD", GREEN)], 200, 560, 34, aa, align="left")
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        linha(c, [("k = 4:  2x + 4y = m", INK), ("   (× 2)", PURPLE)], 200, 640, 34, ab, align="left")
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        linha(c, [("3 × 2 = 6  →  brigam se ", INK), ("m ≠ 6", RED)], 200, 720, 34, acc, align="left")
        semaforo(c, 1060, 640, 40, "amarelo", acc, 1.0)


ALTS7 = [("A", "k = 4.", "esqueceu o quadrado", RED), ("B", "k = 2, apenas.", "esqueceu o −2", RED),
         ("C", "k = 0.", "D = 4: só (0, 0)", RED), ("D", "k = 4 ou k = −4.", "resolveu k² = 16", RED),
         ("E", "k = 2 ou k = −2.", "", GREEN)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · NÓS FAZEMOS", "SISTEMA HOMOGÊNEO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    _enunciado(c, [("O sistema abaixo, com k real, sempre admite a solução x = y = 0. Ele admite também soluções "
                    "diferentes dessa quando", INK)], a0, 236, 26, 960)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - ep(t, C["30"], 0.3)),
          align="left")
    sistema(c, ["x + ky = 0", "kx + 4y = 0"], 200, 410, 38, ep(t, C["29.a"] + 3.0, 0.4))
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS7, 1230, 250, 480, 28, C["30.ok"], "E", cues_in, cues_x, gap=22)
    ap = ep(t, C["29.p"], 0.4) * (1 - ep(t, C["30"], 0.3))
    if ap > 0:
        chip(c, "que tipo de sistema é esse?", 620, 600, AMBER, ap, 28)
    if t < C["30"]:
        return
    a0b = ep(t, C["30"], 0.4)
    porta(c, 860, 470, 70, a0b, 1.0)
    aa = ep(t, C["30.a"], 0.4)
    if aa > 0:
        linha(c, [("D = 1·4 − k·k = ", INK), ("4 − k²", PURPLE)], 200, 580, 34, aa, align="left")
    ab = ep(t, C["30.b"], 0.4)
    if ab > 0:
        linha(c, [("4 − k² = 0  →  ", INK), ("k = 2  ou  k = −2", GREEN)], 200, 660, 34, ab, align="left")
    acc = ep(t, C["30.c"], 0.4)
    if acc > 0:
        ftext(c, "k = 2:  (2, −1) → 2 + 2·(−1) = 0 ✓", 200, 750, 28, "black", GREEN, acc, align="left")


ALTS9 = [("A", "possível e determinado, e (1, 2, 3) é sua única solução.", "", RED),
         ("B", "possível e indeterminado.", "", GREEN),
         ("C", "impossível, porque o determinante dos coeficientes é zero.", "", RED),
         ("D", "possível e determinado, com solução (0, 0, 0).", "", RED),
         ("E", "impossível, porque a terceira equação repete as outras.", "", RED)]
MOT9 = [("xa", "A: achou uma e parou"), ("xc", "C: D = 0 não é impossível"), ("xd", "D: (0, 0, 0) dá 0 ≠ 6"),
        ("xe", "E: repetir gera infinitas")]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "UMA SOLUÇÃO NÃO É A SOLUÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["32.a"], 0.4)
    _enunciado(c, [("Ao resolver o sistema abaixo, um estudante verificou que o terno (1, 2, 3) satisfaz as três "
                    "equações. Sobre esse sistema, é correto afirmar que ele é", INK)], a0, 236, 26, 900)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - ep(t, C["33"], 0.3)),
          align="left")
    ab = ep(t, C["33.a"], 0.4)
    cores = {0: mix(INK, BLUE, ab), 1: mix(INK, BLUE, ab), 2: mix(INK, GREEN, ab)}
    sistema(c, ["x + y + z = 6", "x − y + 2z = 5", "2x + 3z = 11"], 200, 470, 34, ep(t, C["32.a"] + 3.0, 0.4),
            cores=cores)
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"34.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS9, 1130, 240, 590, 24, C["33.ok"], "B", cues_in, cues_x, gap=16)
    pause_timer(c, t, C["32.end"] - 1.9, 760, 660)
    if t < C["33"]:
        return
    if t >= C["34"]:
        for k, (q, s_) in enumerate(MOT9):
            a_ = ep(t, C[f"34.{q}"], 0.4)
            if a_ > 0:
                check_icon(c, 200, 600 + k * 56, 22, a_, RED, "x")
                ftext(c, s_, 240, 616 + k * 56, 28, "black", RED, a_, align="left")
        return
    if ab > 0:
        linha(c, [("L1 + L2 = ", INK), ("2x + 3z = 11", GREEN), (" = L3", INK)], 200, 620, 32, ab, align="left")
    a2 = ep(t, C["33.b"], 0.4)
    if a2 > 0:
        linha(c, [("D = −3 + 1 + 2 = ", INK), ("0", AMBER), ("  (Laplace)", GRAY)], 200, 690, 32, a2, align="left")
        semaforo(c, 900, 690, 34, "amarelo", a2, 1.0)
    a3 = ep(t, C["33.c"], 0.4)
    if a3 > 0:
        ftext(c, "outra solução: (−0,5; 2,5; 4) ✓", 200, 770, 28, "black", GREEN, a3, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    for k, (s_, col) in enumerate((("JUNTAMOS TUDO", BLUE), ("PEGADINHAS", AMBER), ("QUESTÕES INÉDITAS", GREEN))):
        a_ = ep(t, C["36.a"] + k * 1.2, 0.5)
        chip(c, s_, W / 2, 330 + k * 150, col, a_, 46)
    pill(c, "ep. 5 · revisão de determinantes e sistemas", W / 2, 790, PURPLE, size=30, a=aa, anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"],
        "Você também achava que D = 0 era impossível?", canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, tabela=b_tabela,
              gemeas=b_gemeas, parametro=b_parametro, escalona=b_escalona, homogeneo=b_homogeneo,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q7=b_q7, q9=b_q9, ponte=b_ponte, cta=b_cta)
