"""Visual — Velocidade, Densidade e Vazão, Episódio 2: velocidade média, distância total ÷ tempo total (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: relogio() e regua() (meia volta do ponteiro = 0,5 da régua, não 0,3), onibus() e trem(),
linha_tempo() (o ônibus andando, a parada pintada de cinza e o cronômetro correndo), velocimetro() e painel() (km/h × m/s),
grafico_ritmo() (o ritmo real × o ritmo constante imaginário), linha().
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
ARQUIVO_FINAL = "enem_matematica_velocidade_ep2_velocidade_media.mp4"
CARD_R = K.CARD_R
ESTRADA = "#6B7280"
PARADO = "#C9CED6"


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


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def relogio(c, cx, cy, r, minutos, a, col=None, num_a=1.0):
    """relógio analógico: setor de 0 até `minutos` pintado; números 0, 15, 30, 45"""
    if a <= 0:
        return
    col = col or GREEN
    c.drawCircle(cx, cy, r + 10, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 10, paint(INK, a, stroke=max(4, r * 0.05)))
    if minutos > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, min(minutos, 59.99) / 60 * 360, False); p.close()
        c.drawPath(p, paint(col, a * 0.3))
    for k in range(60):
        ang = -math.pi / 2 + k * math.pi / 30
        big = k % 5 == 0
        if not big and r < 90:
            continue
        r0 = r - (r * 0.16 if big else r * 0.07)
        c.drawLine(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + r * math.cos(ang), cy + r * math.sin(ang),
                   paint(INK if big else INK2, a * (0.8 if big else 0.4), stroke=4 if big else 2))
    if num_a > 0 and r >= 90:
        for m in (0, 15, 30, 45):
            ang = -math.pi / 2 + m / 60 * 2 * math.pi
            text_mid(c, str(m), cx + (r + 42) * math.cos(ang), cy + (r + 42) * math.sin(ang), 26, "black", PURPLE,
                     a * num_a)
    ang = -math.pi / 2 + minutos / 60 * 2 * math.pi
    c.drawLine(cx, cy, cx + (r * 0.82) * math.cos(ang), cy + (r * 0.82) * math.sin(ang),
               paint(col, a, stroke=max(4, r * 0.07), cap_round=True))
    c.drawCircle(cx, cy, max(5, r * 0.08), paint(INK, a))


def regua(c, x, y, w, a, valor=None, col=None, marca_errada=None, err_a=0.0):
    """régua decimal de 0 a 1 hora, com 10 divisões; `valor` = posição do marcador (0 a 1)"""
    if a <= 0:
        return
    col = col or GREEN
    rrect(c, x - 20, y - 40, w + 40, 120, 14, "#FFF6DD", a, shadow=True)
    for k in range(11):
        xx = x + w * k / 10
        big = k in (0, 5, 10)
        line(c, xx, y - 40, xx, y - 40 + (46 if big else 28), INK, a, 4 if big else 3)
        if big or k % 1 == 0:
            lab = "0" if k == 0 else ("1 h" if k == 10 else f"0,{k}")
            text(c, lab, xx, y + 46, 24 if big else 20, "black" if big else "bold", INK if big else GRAY, a)
    if marca_errada is not None and err_a > 0:
        xx = x + w * marca_errada
        c.drawLine(xx, y - 70, xx, y + 4, paint(RED, err_a, stroke=6, cap_round=True))
        check_icon(c, xx - 16, y - 116, 32, err_a, RED, "x")
    if valor is not None:
        xx = x + w * valor
        p = skia.Path(); p.moveTo(xx, y + 4); p.lineTo(xx - 16, y - 24); p.lineTo(xx + 16, y - 24); p.close()
        c.drawPath(p, paint(col, a))
        c.drawLine(xx, y - 70, xx, y - 24, paint(col, a, stroke=6, cap_round=True))


def onibus(c, cx, cy, s, a, col=BLUE):
    """ônibus de lado, virado para a direita (cy = linha da estrada)"""
    if a <= 0:
        return
    rrect(c, cx - s, cy - s * 0.78, 2 * s, s * 0.66, s * 0.14, col, a)
    for k in range(4):
        rrect(c, cx - s * 0.86 + k * s * 0.42, cy - s * 0.68, s * 0.32, s * 0.24, s * 0.05, "#DCE6FF", a)
    rrect(c, cx + s * 0.80, cy - s * 0.68, s * 0.14, s * 0.30, s * 0.04, "#DCE6FF", a)
    for fx in (-0.6, 0.6):
        c.drawCircle(cx + fx * s, cy - s * 0.12, s * 0.17, paint(INK, a))
        c.drawCircle(cx + fx * s, cy - s * 0.12, s * 0.07, paint("#C9CED6", a))


def trem(c, cx, cy, s, a, col=PURPLE):
    """trem de 2 vagões, virado para a direita (cy = trilho)"""
    if a <= 0:
        return
    line(c, cx - s * 2.3, cy, cx + s * 1.3, cy, INK2, a, 4)
    for k, x0 in enumerate((cx - s * 2.2, cx - s * 0.95)):
        rrect(c, x0, cy - s * 0.78, s * 1.15, s * 0.62, s * 0.12, col if k else mix(col, "#FFFFFF", 0.25), a)
        for j in range(3):
            rrect(c, x0 + s * 0.1 + j * s * 0.34, cy - s * 0.68, s * 0.24, s * 0.2, s * 0.04, "#EDE6FF", a)
        for fx in (0.25, 0.9):
            c.drawCircle(x0 + s * fx, cy - s * 0.1, s * 0.12, paint(INK, a))
    p = skia.Path(); p.moveTo(cx + s * 0.2, cy - s * 0.78); p.lineTo(cx + s * 0.95, cy - s * 0.78)
    p.quadTo(cx + s * 1.3, cy - s * 0.45, cx + s * 1.25, cy - s * 0.16); p.lineTo(cx + s * 0.2, cy - s * 0.16); p.close()
    c.drawPath(p, paint(col, a))
    c.drawCircle(cx + s * 0.45, cy - s * 0.1, s * 0.12, paint(INK, a))
    c.drawCircle(cx + s * 1.0, cy - s * 0.1, s * 0.12, paint(INK, a))


def carro(c, cx, cy, s, a, col=RED, flip=False):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy)
    if flip:
        c.scale(-1, 1)
    rrect(c, -s, -s * 0.45, 2 * s, s * 0.32, s * 0.12, col, a)
    rrect(c, -s * 0.55, -s * 0.74, s * 1.0, s * 0.34, s * 0.12, col, a)
    rrect(c, -s * 0.42, -s * 0.68, s * 0.36, s * 0.22, s * 0.05, "#DCE6FF", a)
    rrect(c, s * 0.02, -s * 0.68, s * 0.36, s * 0.22, s * 0.05, "#DCE6FF", a)
    for fx in (-0.55, 0.55):
        c.drawCircle(fx * s, -s * 0.12, s * 0.17, paint(INK, a))
    c.restore()


def velocimetro(c, cx, cy, r, val, vmax, a, unidade="km/h", size=80):
    """mostrador de velocímetro (meia-lua) com ponteiro em `val`"""
    if a <= 0:
        return
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, 180)
    c.drawPath(p, paint(INK, a, stroke=max(8, r * 0.08)))
    for k in range(0, 11):
        ang = math.pi + k / 10 * math.pi
        r0 = r - r * 0.18
        c.drawLine(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + (r - 8) * math.cos(ang),
                   cy + (r - 8) * math.sin(ang), paint(INK2, a, stroke=4))
    ang = math.pi + clamp(val / vmax) * math.pi
    c.drawLine(cx, cy, cx + (r * 0.76) * math.cos(ang), cy + (r * 0.76) * math.sin(ang),
               paint(RED, a, stroke=8, cap_round=True))
    c.drawCircle(cx, cy, 14, paint(INK, a))
    fmid(c, f"{val:g}".replace(".", ","), cx, cy + size * 0.85, size, "black", INK, a)
    text(c, unidade, cx, cy + size * 0.85 + size * 0.95, size * 0.42, "black", INK2, a)


def painel(c, cx, cy, val, a, unidade="m/s", col=None, w=380):
    """visor digital retangular (m/s)"""
    if a <= 0:
        return
    col = col or GREEN
    rrect(c, cx - w / 2, cy - 110, w, 220, 26, "#1F2430", a, shadow=True)
    fmid(c, val, cx, cy - 10, 96, "black", col, a)
    text(c, unidade, cx, cy + 80, 34, "black", "#C9CED8", a)


def cronometro(c, cx, cy, s, a, r=110):
    """cronômetro com visor digital"""
    if a <= 0:
        return
    rrect(c, cx - 18, cy - r - 30, 36, 34, 8, INK, a)
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=8))
    rrect(c, cx - r * 0.92, cy - 34, r * 1.84, 68, 14, "#1F2430", a)
    fmid(c, s, cx, cy, 40 if len(s) < 6 else 30, "black", AMBER, a)


def hm(h):
    """horas decimais -> '1 h 30 min'"""
    tot = int(round(h * 60))
    hh, mm = divmod(tot, 60)
    return f"{hh} h {mm:02d} min"


def linha_tempo(c, x, y, w, u, a, rev=(1, 1, 1), cron=True):
    """a viagem do ônibus: 1 h a 90 · 0,5 h parado (cinza) · 1 h a 90. u = horas decorridas (0 a 2,5)"""
    if a <= 0:
        return
    segs = [(0, 1, GREEN, "90 km", "1 h a 90 km/h"), (1, 1.5, PARADO, "0 km", "parado no posto"),
            (1.5, 2.5, GREEN, "90 km", "1 h a 90 km/h")]
    L = 2.5
    for k, (h0, h1, col, km, nota) in enumerate(segs):
        ra = a * rev[k]
        if ra <= 0:
            continue
        x0, x1 = x + w * h0 / L, x + w * h1 / L
        rrect(c, x0 + 3, y - 18, x1 - x0 - 6, 36, 10, col, ra)
        text(c, km, (x0 + x1) / 2, y - 40, 30, "black", INK if col != PARADO else GRAY, ra)
        text(c, nota, (x0 + x1) / 2, y + 60, 22, "bold", GRAY, ra)
    for k in range(6):
        xx = x + w * (k * 0.5) / L
        line(c, xx, y + 20, xx, y + 32, INK2, a, 3)
        text(c, f"{k * 0.5:g}".replace(".", ",") + " h", xx, y + 96, 20, "bold", INK2, a)
    # ônibus: anda nos trechos verdes, fica parado no cinza
    d = min(u, 1) + max(0, min(u, 2.5) - 1.5)
    bx = x + w * (min(u, 1) if u < 1.5 else 1.5 + (u - 1.5)) / L if u > 0 else x
    onibus(c, bx, y - 74, 46, a)
    if 1 <= u < 1.5:
        pill(c, "PARADO", bx, y - 168, GRAY, size=22, a=a, anchor="center")
    if cron:
        cronometro(c, x + w + 170, y - 30, hm(min(u, 2.5)), a)
        text(c, f"{d * 90:g} km".replace(".", ","), x + w + 170, y + 120, 34, "black", GREEN, a)


def grafico_ritmo(c, x, y, w, h, a, media_a=0.0):
    """velocidade × tempo: 90 — 0 — 90 (real) e a linha tracejada constante de 72 (o ritmo constante imaginário)"""
    if a <= 0:
        return
    line(c, x, y + h, x + w, y + h, INK, a, 4)
    line(c, x, y, x, y + h, INK, a, 4)
    text(c, "tempo", x + w - 40, y + h + 40, 22, "bold", GRAY, a)
    text(c, "velocidade", x + 10, y - 20, 22, "bold", GRAY, a, align="left")
    vy = lambda v: y + h - h * v / 100
    pts = [(0, 90), (1, 90), (1, 0), (1.5, 0), (1.5, 90), (2.5, 90)]
    p = skia.Path()
    for k, (hh, v) in enumerate(pts):
        X, Y = x + w * hh / 2.5, vy(v)
        (p.moveTo if k == 0 else p.lineTo)(X, Y)
    c.drawPath(p, paint(BLUE, a, stroke=6))
    text(c, "90", x - 30, vy(90) + 8, 22, "black", BLUE, a)
    if media_a > 0:
        yy = vy(72)
        n = 18
        for k in range(n):
            xx0 = x + w * k / n
            line(c, xx0, yy, xx0 + w / n * 0.6, yy, GREEN, media_a, 6)
        text(c, "72", x - 30, yy + 8, 22, "black", GREEN, media_a)
        text(c, "ritmo constante", x + w * 0.8, yy + 40, 22, "black", GREEN, media_a)
        text(c, "imaginário", x + w * 0.8, yy + 68, 22, "black", GREEN, media_a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "VELOCIDADE MÉDIA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        g = ep(t, C["01.a"], 2.5)
        trem(c, lerp(300, 620, g), 360, 110, aa)
        linha(c, [("180 km", GREEN), ("  em  ", INK2), ("2 h 30 min", AMBER)], 1300, 300, 64, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 470, 640, 150, 24, mix("#FFFFFF", RED, 0.08), ab)
        linha(c, [("180 km ÷ 2,30", RED)], 620, 545, 56, ab)
        check_icon(c, 905, 530, 40, ab, RED, "x")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 470, 640, 150, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("180 km ÷ 2,5 h = ", INK), ("72 km/h", GREEN)], 1300, 545, 46, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        relogio(c, 760, 760, 70, 30 * ep(t, C["01.d"], 1.0), ad)
        selo(c, 1200, 760, ad, "O ERRO ESTÁ NO RELÓGIO", AMBER, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular a velocidade média de qualquer viagem", "com parada ou sem parada"),
            ("02.b", "passar de km/h para m/s sem inverter", "÷ 3,6  ·  × 3,6")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [("03.a", "TAXA", "episódio 1", ["quanto de uma coisa", "POR unidade de outra"], "km/h = km POR hora", BLUE),
            ("03.b", "MINUTOS → HORA", "série de Unidades", ["divida por 60"], "30 min ÷ 60 = 0,5 h", PURPLE),
            ("03.c", "O FATOR 3,6", "série de Unidades", ["km/h → m/s:  ÷ 3,6", "m/s → km/h:  × 3,6"], "m/s é o número menor",
             GREEN)]
    for k, (cue, tit, ori, linhas, ex_, col) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 200 + k * 520
        rrect(c, x, 250, 480, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250, 480, 64, 24, col, a * 0.14)
        text(c, tit, x + 240, 294, 30, "black", col, a)
        text(c, ori, x + 240, 360, 22, "bold", GRAY, a)
        for j, s in enumerate(linhas):
            ftext(c, s, x + 240, 450 + j * 56, 32, "black", INK, a)
        rrect(c, x + 30, 600, 420, 80, 16, mix("#FFFFFF", col, 0.10), a)
        ftext(c, ex_, x + 240, 652, 28, "black", col, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA VIAGEM DE ÔNIBUS", "A MÉDIA FOI 90?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.4)
    line(c, 200, 470, 1720, 470, ESTRADA, a0, 10)
    for k in range(16):
        line(c, 220 + k * 95, 470, 260 + k * 95, 470, "#FFFFFF", a0, 3)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        onibus(c, lerp(260, 560, ep(t, C["04.a"], 2.0)), 462, 70, aa)
        velocimetro(c, 420, 650, 90, 90, 120, aa, size=46)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 820, 330, 240, 130, 14, "#F2F2EE", ab, shadow=True)
        rrect(c, 820, 330, 240, 40, 14, AMBER, ab)
        text(c, "POSTO", 940, 360, 24, "black", "#FFFFFF", ab)
        text(c, "parada: 30 min", 940, 430, 26, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        onibus(c, lerp(1150, 1500, ep(t, C["04.c"], 2.0)), 462, 70, acc)
        text(c, "90 km/h de novo", 1340, 560, 30, "black", INK2, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        rrect(c, 1340, 600, 330, 200, 30, "#1F2430", ad, shadow=True)
        rrect(c, 1360, 620, 290, 160, 18, "#FFFFFF", ad)
        text(c, "tempo estimado", 1505, 668, 24, "bold", GRAY, ad)
        text(c, "2 h 30 min", 1505, 735, 46, "black", BLUE, ad)
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        pergunta(c, "a viagem INTEIRA foi a 90 km/h?", 860, 720, ae, AMBER, 38)


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "VELOCIDADE MÉDIA", "O RITMO CONSTANTE IMAGINÁRIO", BLUE),
                       ("06", "A PALAVRA-CHAVE", "TOTAL", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        text(c, "VELOCIDADE MÉDIA", 560, 270, 52, "black", BLUE, aa)
        ab = ep(t, C["05.b"], 0.5)
        grafico_ritmo(c, 260, 360, 620, 330, ab, ep(t, C["05.b"] + 2.6, 0.6))
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            text_mid(c, "v  =", 1160, 480, 72, "black", INK, acc)
            fr(c, "distância total", "tempo total", 1480, 470, 58, INK, acc, num_col=GREEN, den_col=AMBER)
            boxed(c, 1020, 340, 700, 300, PURPLE, acc, 0.05)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 260, 700, 220, GREEN, aa, 0.08)
        text(c, "DISTÂNCIA TOTAL", 570, 320, 40, "black", GREEN, aa)
        text(c, "tudo o que foi percorrido,", 570, 390, 30, "bold", INK, aa)
        text(c, "da partida até a chegada", 570, 436, 30, "bold", INK, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        boxed(c, 1000, 260, 700, 220, AMBER, ab, 0.08)
        text(c, "TEMPO TOTAL", 1350, 320, 40, "black", AMBER, ab)
        text(c, "tudo o que o relógio marcou,", 1350, 390, 30, "bold", INK, ab)
        text(c, "sem pular nada", 1350, 436, 30, "bold", INK, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        fr(c, "distância TOTAL", "tempo TOTAL", 760, 640, 56, INK, acc, num_col=GREEN, den_col=AMBER)
        selo(c, 1370, 640, acc, "“TOTAL” É A DEFINIÇÃO INTEIRA", PURPLE, -3, 32)


# ======================================================================
# bloco b — o relógio e a hora decimal
# ======================================================================

def b_relogio(c, t, C, B):
    head_seq(c, t, C, [("07", "O RELÓGIO", "CONTA DE 60 EM 60", AMBER), ("08", "CONVERTA O TEMPO", "ANTES DE DIVIDIR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        a0 = ep(t, C["07"], 0.5)
        m = 30 * ep(t, C["07.b"], 1.6)
        relogio(c, 470, 500, 190, m, a0)
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            text(c, "60 minutos = 1 hora", 470, 790, 32, "black", PURPLE, aa)
        regua(c, 900, 470, 760, a0, valor=(m / 60 if t >= C["07.b"] else None),
              marca_errada=0.3, err_a=ep(t, C["07.c"] + 1.6, 0.4))
        ab = ep(t, C["07.b"] + 1.6, 0.4)
        if ab > 0:
            linha(c, [("30 min = ", INK), ("METADE", GREEN), (" da hora", INK)], 1280, 270, 40, ab)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            linha(c, [("30 min = ", INK), ("0,5 h", GREEN), ("    não  ", INK2), ("0,3 h", RED)], 1280, 640, 48, acc)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            pill(c, "HORA DECIMAL: a hora escrita com vírgula (0,5 h = meia hora)", 1280, 750, BLUE, size=24, a=ad,
                 anchor="center")
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        regra(c, "minutos  ÷  60  =  horas", W / 2, 290, aa, 48)
        linha(c, [("30 min ÷ 60 = ", INK), ("0,5 h", GREEN)], W / 2, 420, 60, ep(t, C["08.a"] + 1.6, 0.4))
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        linha(c, [("2 h 30 min", AMBER), ("  =  2 h + 0,5 h  =  ", INK), ("2,5 h", GREEN)], W / 2, 560, 60, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 720, acc, "CONVERTA O TEMPO ANTES DE DIVIDIR", PURPLE, -2, 40)


def b_atalho_rel(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "AS FATIAS DO RELÓGIO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 110, "ATALHO", ["pense nas FATIAS do relógio, sem fazer conta"], aa, 38)
    fatias = [("09.b", 15, "15 min", "1/4", "0,25 h", 0.0), ("09.b", 30, "30 min", "1/2", "0,5 h", 1.6),
              ("09.b", 45, "45 min", "3/4", "0,75 h", 3.4), ("09.c", 6, "6 min", "1/10", "0,1 h", 0.0)]
    for k, (cue, m, lab, frac, dec, dl) in enumerate(fatias):
        a = ep(t, C[cue] + dl, 0.5)
        if a <= 0:
            continue
        x = 360 + k * 400
        col = GREEN if k < 3 else AMBER
        relogio(c, x, 480, 105, m, a, col, num_a=0)
        text(c, lab, x, 660, 38, "black", INK, a)
        fmid(c, "= " + frac + " h", x, 720, 32, "black", INK2, a)
        rrect(c, x - 110, 750, 220, 64, 32, mix("#FFFFFF", col, 0.16), a)
        text(c, dec, x, 795, 38, "black", col, a)
    if ep(t, C["09.c"], 0.5) > 0:
        text(c, "CURINGA", 360 + 3 * 400, 350, 24, "black", AMBER, ep(t, C["09.c"], 0.5))


# ======================================================================
# bloco c — o trem
# ======================================================================

def b_trem(c, t, C, B):
    head_seq(c, t, C, [("10", "O TREM", "180 km EM 2 h 30 min", PURPLE), ("11", "ATALHO", "DOBRE OS DOIS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            trem(c, 460, 380, 110, aa)
            linha(c, [("distância total: ", INK), ("180 km", GREEN)], 1250, 290, 42, aa)
            linha(c, [("tempo total: ", INK), ("2,5 h", AMBER)], 1250, 370, 42, ep(t, C["10.a"] + 2.0, 0.4))
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            text_mid(c, "v  =", 640, 560, 68, "black", INK, ab)
            fr(c, "180 km", "2,5 h", 890, 550, 60, INK, ab, num_col=GREEN, den_col=AMBER)
            text_mid(c, "=", 1090, 560, 68, "black", INK, ab)
            text_mid(c, "72 km/h", 1340, 560, 76, "black", GREEN, ep(t, C["10.b"] + 2.4, 0.4))
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 460, 700, 1000, 100, 20, mix("#FFFFFF", RED, 0.08), acc)
            linha(c, [("180 km ÷ 2,3 ≈ 78,3", RED), ("   parece bom, está errado", INK2)], W / 2, 750, 36, acc)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 210, 1400, 120, "ATALHO", ["dividir por 2,5?  DOBRE os dois: a divisão não muda"], aa, 38)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("180 ÷ 2,5", INK)], 640, 480, 72, ab)
        g = ep(t, C["11.b"] + 0.6, 0.8)
        arrow(c, 900, 480, 900 + 160 * g, 480, GREEN, ab, 6, 18)
        text(c, "× 2 nos dois", 980, 440, 28, "black", GREEN, ab)
        linha(c, [("360 ÷ 5", GREEN)], 1300, 480, 72, ep(t, C["11.b"] + 1.4, 0.4))
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        linha(c, [("360 ÷ 5 = ", INK), ("72 km/h", GREEN)], W / 2, 650, 72, acc)
        conferido(c, "sem vírgula nenhuma", 780, 770, ep(t, C["11.c"] + 1.6, 0.4), True, 32)


# ======================================================================
# bloco d — a parada
# ======================================================================

def b_parada(c, t, C, B):
    head_seq(c, t, C, [("12", "A PARADA NO POSTO", "ENTRA NA CONTA?", AMBER),
                       ("13", "TEMPO PARADO", "TAMBÉM É TEMPO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    X0, Y0, WL = 220, 470, 1160
    if sid == "12":
        a0 = ep(t, C["12"], 0.5)
        # u avança: trecho 1 em 12.a, parada em 12.b, trecho 2 em 12.c
        u = (1.0 * ep(t, C["12.a"] + 0.4, 2.0) + 0.5 * ep(t, C["12.b"] + 0.4, 2.0) + 1.0 * ep(t, C["12.c"] + 0.4, 2.0))
        rev = (ep(t, C["12.a"], 0.4), ep(t, C["12.b"], 0.4), ep(t, C["12.c"], 0.4))
        linha_tempo(c, X0, Y0, WL, u, a0, rev)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 720, ad, "O CRONÔMETRO NÃO PARA NO POSTO", AMBER, -2, 40)
        return
    a0 = ep(t, C["13"], 0.5)
    linha_tempo(c, X0, 330, WL, 2.5, a0 * 0.9, cron=False)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        linha(c, [("distância: 90 + 0 + 90 = ", INK), ("180 km", GREEN)], 760, 520, 38, aa)
        linha(c, [("tempo: 1 + 0,5 + 1 = ", INK), ("2,5 h", AMBER)], 760, 580, 38, ep(t, C["13.a"] + 2.4, 0.4))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("180 km ÷ 2,5 h = ", INK), ("72 km/h", GREEN)], 760, 660, 46, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        velocimetro(c, 1560, 560, 100, 90, 120, acc, size=40)
        text(c, "velocímetro", 1560, 430, 24, "bold", GRAY, acc)
        rrect(c, 1450, 700, 220, 70, 35, mix("#FFFFFF", GREEN, 0.18), acc)
        text(c, "média: 72", 1560, 748, 32, "black", GREEN, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        regra(c, "Tempo parado também é tempo", 760, 790, ad, 36)


# ======================================================================
# bloco e — o fator 3,6
# ======================================================================

def b_fator(c, t, C, B):
    head_seq(c, t, C, [("14", "OUTRA UNIDADE", "km/h E m/s", PURPLE), ("15", "ATALHO", "m/s É SEMPRE O MENOR", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            pill(c, "m/s = metros POR segundo: quantos metros a cada segundo", W / 2, 240, BLUE, size=28, a=aa,
                 anchor="center")
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            velocimetro(c, 520, 520, 170, 54, 120, ab)
            g = ep(t, C["14.b"] + 1.0, 0.6)
            arrow(c, 760, 450, 760 + 300 * g, 450, PURPLE, ab, 6, 18)
            text(c, "÷ 3,6", 910, 420, 40, "black", PURPLE, ab * g)
            painel(c, 1360, 470, "15", ep(t, C["14.b"] + 2.6, 0.5))
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            g = ep(t, C["14.c"] + 0.6, 0.6)
            arrow(c, 1060, 640, 1060 - 300 * g, 640, GREEN, acc, 6, 18)
            text(c, "× 3,6", 910, 690, 40, "black", GREEN, acc * g)
            linha(c, [("15 m/s × 3,6 = ", INK), ("54 km/h", GREEN)], 1360, 700, 36, acc)
        return
    aa = ep(t, C["15.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 120, "ATALHO", ["o número em m/s é sempre o MENOR"], aa, 42)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        cronometro(c, 560, 520, "1 s", ab, r=120)
        text(c, "1 segundo: poucos metros", 560, 720, 30, "black", INK2, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 900, 400, 780, 130, 22, mix("#FFFFFF", PURPLE, 0.08), acc)
        linha(c, [("km/h → m/s: ", INK), ("diminui", PURPLE), (" → ÷ 3,6", PURPLE)], 1290, 465, 40, acc)
        a2 = ep(t, C["15.c"] + 2.6, 0.4)
        rrect(c, 900, 570, 780, 130, 22, mix("#FFFFFF", GREEN, 0.10), a2)
        linha(c, [("m/s → km/h: ", INK), ("aumenta", GREEN), (" → × 3,6", GREEN)], 1290, 635, 40, a2)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "O TEMPO TOTAL PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 210, 1480, 150, 24, "#F7F7F5", aa)
        linha(c, [("270 km", GREEN), ("  em  ", INK), ("3 h", AMBER), (" de estrada  +  ", INK), ("parada de 30 min", GRAY)],
              W / 2, 262, 48, aa)
        text(c, "velocidade média da viagem completa = ?", W / 2, 336, 32, "black", PURPLE, aa)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 560)
    if t < C["17"]:
        return
    a1 = ep(t, C["17.a"], 0.5)
    if a1 > 0:
        linha(c, [("tempo total: 3 h + 0,5 h = ", INK), ("3,5 h", AMBER)], W / 2, 450, 46, a1)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        linha(c, [("270 ÷ 3,5  →  dobre:  540 ÷ 7 ≈ ", INK), ("77 km/h", GREEN)], W / 2, 560, 46, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 630, 640, 90, 20, mix("#FFFFFF", RED, 0.08), acc)
        linha(c, [("sem a parada: 270 ÷ 3 = 90", RED)], 680, 675, 32, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        conferido(c, "77 < 90: a parada puxa para baixo", 1060, 690, ad, True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Velocidade média é distância total sobre tempo total.",
          "Tempo parado também é tempo.",
          "Trinta minutos são 0,5 hora, não 0,30."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Ler 2,5 h como 2 h 50 min (ou 30 min como 0,30 h)", "no dinheiro e no metro a vírgula funciona assim",
          "o relógio conta de 60 em 60: divida os minutos por 60"),
         ("Ignorar o tempo de parada no percurso completo", "parado, o ônibus não andou nada",
          "mas o relógio andou: o tempo parado entra no tempo total"),
         ("km/h = m/s, ou o 3,6 no sentido errado", "as duas são velocidade",
          "m/s é sempre o MENOR: ÷ 3,6 diminui · × 3,6 aumenta")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


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


ALTS1 = [("A", "60", "usou 3 h", RED), ("B", "66", "vizinho, sem erro comum", RED), ("C", "72", "", GREEN),
         ("D", "75", "vizinho, sem erro comum", RED), ("E", "90", "usou só as 2 h", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "VELOCIDADE MÉDIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Um trem percorre 180 quilômetros entre duas estações em 2 horas e 30 minutos. A velocidade "
                           "média desse trem, em quilômetros por hora, é de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["23.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["23"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        pill(c, "distância total ÷ tempo total", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["23"], 0.4), anchor="center")
        linha(c, [("2 h 30 min = ", INK), ("2,5 h", AMBER)], 540, y0 + 100, 32, ep(t, C["23.a"], 0.4))
        linha(c, [("180 km ÷ 2,5 h → 360 ÷ 5 = ", INK), ("72 km/h", GREEN)], 540, y0 + 160, 28, ep(t, C["23.b"], 0.4))
        conferido(c, "velocidade normal de trem", 230, y0 + 225, ep(t, C["23.c"], 0.4), True, 26)
    af = ep(t, C["24.f"], 0.5)
    if af > 0:
        rrect(c, 980, 700, 720, 110, 20, mix("#FFFFFF", AMBER, 0.14), af)
        text(c, "30 min lido como 0,30 h:  180 ÷ 2,3 ≈ 78 km/h", 1340, 748, 26, "black", AMBER, af)
        text(c, "(nem está entre as alternativas)", 1340, 788, 22, "bold", GRAY, af)


ALTS2 = [("A", "8", "parou em m/s", RED), ("B", "12,5", "repetiu o tempo", RED), ("C", "28,8", "", GREEN),
         ("D", "36", "arredondou: 100 m em 10 s", RED), ("E", "80", "multiplicou por 10", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · VOCÊ FAZ", "O ATLETA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Um atleta percorre 100 metros em 12,5 segundos. A velocidade média desse atleta, em "
                           "quilômetros por hora, é de", INK)], a0, 240, 28)
    text(c, "Questão do material de Razão (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["26.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 140)
    if t >= C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["26"], 0.4))
        linha(c, [("100 m ÷ 12,5 s = ", INK), ("8 m/s", BLUE)], 540, y0 + 60, 34, ep(t, C["26.a"], 0.4))
        linha(c, [("pede km/h: aumenta → × 3,6", PURPLE)], 540, y0 + 125, 26, ep(t, C["26.b"], 0.4))
        linha(c, [("8 m/s × 3,6 = ", INK), ("28,8 km/h", GREEN)], 540, y0 + 185, 34, ep(t, C["26.b"] + 2.0, 0.4))
        conferido(c, "velocista ≈ 30 km/h · corrida ≈ 12 km/h", 210, y0 + 255, ep(t, C["26.c"], 0.4), True, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A ARMADILHA DA MÉDIA", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        line(c, 300, 420, 1620, 420, ESTRADA, aa, 8)
        line(c, 300, 560, 1620, 560, ESTRADA, aa, 8)
        g = ep(t, C["29.a"], 1.6)
        carro(c, lerp(380, 1480, g), 412, 70, aa, RED)
        text(c, "ida: 60 km/h", 960, 370, 34, "black", INK, aa)
        g2 = ep(t, C["29.a"] + 1.8, 1.6)
        a2 = ep(t, C["29.a"] + 1.8, 0.3)
        carro(c, lerp(1480, 380, g2), 552, 70, a2, RED, flip=True)
        text(c, "volta: 40 km/h", 960, 620, 34, "black", INK, a2)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        text(c, "média = 50?", W / 2, 730, 64, "black", AMBER, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, 1320, 710, acc, "ERRADO", RED, -8, 40)
    pill(c, "ep. 3 · a armadilha da média", W / 2, 810, PURPLE, size=30, a=ep(t, C["29.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Você já tinha caído no erro do 2,30?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              relogio=b_relogio, atalho_rel=b_atalho_rel, trem=b_trem, parada=b_parada, fator=b_fator,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2, ponte=b_ponte, cta=b_cta)
