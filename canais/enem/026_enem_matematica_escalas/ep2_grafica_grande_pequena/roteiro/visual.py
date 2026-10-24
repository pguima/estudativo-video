"""Visual — Escalas, Plantas e Mapas, Episódio 2: escala gráfica × numérica e escala grande × pequena (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: fr, alternativas, erro_cards, atalho...).
Peças deste episódio: folha_mapa() (mapa de papel com a barra gráfica e o número impresso, que escala inteiro na fotocópia),
celular() (o zoom do aplicativo de mapas, do bairro ao país, com a barra e a escala no canto — a mesma analogia da
Cartografia ep. 1), bairro()/scale_bar()/regiao() (copiadas da Cartografia ep. 1), linha() (texto com cor por trecho).
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
import mapas

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum026", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_escalas_ep2_grafica_grande_pequena.mp4"
CARD_R = K.CARD_R
SEA = "#DBEAFE"
LAND = "#86C18A"
LAND2 = "#5FA463"
PAPEL = "#FFFDF6"
ESTRADA = "#E0A458"

REGIAO = [(0.05, 0.35), (0.2, 0.1), (0.45, 0.05), (0.62, 0.15), (0.85, 0.08), (1.0, 0.3), (0.92, 0.55), (0.98, 0.8),
          (0.75, 0.95), (0.5, 0.88), (0.3, 1.0), (0.12, 0.85), (0.0, 0.6)]


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def blob(c, pts, x, y, w, h, col, a, stroke=None):
    if a <= 0:
        return
    p = skia.Path()
    P = [(x + u * w, y + v * h) for u, v in pts]
    p.moveTo(*P[0])
    for i in range(1, len(P)):
        p.quadTo(P[i - 1][0], P[i - 1][1], (P[i - 1][0] + P[i][0]) / 2, (P[i - 1][1] + P[i][1]) / 2)
    p.quadTo(P[-1][0], P[-1][1], (P[-1][0] + P[0][0]) / 2, (P[-1][1] + P[0][1]) / 2)
    p.close()
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint(stroke or LAND2, a, stroke=3))


def bairro(c, x, y, w, h, a, cols=5, rows=4):
    """ruas e quarteirões com casinhas (zoom aproximado)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, "#9CA3AF", a)
    gw, gh = w / cols, h / rows
    for i in range(cols):
        for j in range(rows):
            bx, by = x + i * gw + 8, y + j * gh + 8
            rrect(c, bx, by, gw - 16, gh - 16, 6, "#F3F4F6", a)
            for q in range(3):
                c.drawRect(skia.Rect.MakeXYWH(bx + 6 + q * (gw - 28) / 3, by + 6, (gw - 40) / 3, (gh - 28) / 2),
                           paint("#F59E0B", a * 0.75))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), paint(INK2, a, stroke=3))


def scale_bar(c, x, y, w, a, labels=("0", "5", "10 km"), size=22, hh=14):
    """barra gráfica de 2 segmentos (preto e branco) com os rótulos no início, no meio e no fim"""
    if a <= 0:
        return
    for k in range(2):
        c.drawRect(skia.Rect.MakeXYWH(x + k * w / 2, y, w / 2, hh), paint(INK if k == 0 else "#FFFFFF", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, hh), paint(INK, a, stroke=2))
    for k, s in enumerate(labels):
        if s:
            text(c, s, x + k * w / 2, y + hh + size * 1.25, size, "bold", INK2, a)


FW, FH = 440, 310   # folha de mapa em tamanho "original"


def folha_mapa(c, x, y, s, a, numero="1 : 50 000", barra=("0", "", "1 km"), barra_a=1.0, num_a=1.0):
    """mapa de papel (canto superior esquerdo em x, y) desenhado inteiro na escala s: terra, estrada, duas cidades,
    a barra gráfica (canto inferior esquerdo) e o número impresso (canto inferior direito) crescem/encolhem JUNTOS."""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, 0, 0, FW, FH, 10, PAPEL, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(0, 0, FW, FH), 10, 10), paint(INK2, a, stroke=2.5 / s))
    rrect(c, 14, 14, FW - 28, FH - 90, 8, SEA, a)
    blob(c, REGIAO, 40, 24, FW - 80, FH - 112, LAND, a)
    p = skia.Path(); p.moveTo(90, 150); p.cubicTo(170, 90, 260, 200, 350, 110)
    c.drawPath(p, paint(ESTRADA, a, stroke=7))
    for px, py in ((90, 150), (350, 110)):
        c.drawCircle(px, py, 10, paint(RED, a))
        c.drawCircle(px, py, 10, paint("#FFFFFF", a, stroke=3))
    scale_bar(c, 30, FH - 62, 120, a * barra_a, barra, 18, 10)
    text(c, numero, FW - 26, FH - 30, 26, "black", INK, a * num_a, align="right")
    c.restore()


def celular(c, px, py, pw, ph, z, a, escala="1 : 5 000", barra="100 m", barra_a=1.0, pulso=0.0):
    """celular com o mapa: z = 0 (bairro, zoom aproximado) → 1 (país inteiro, zoom afastado); no canto, a barra gráfica
    e a escala numérica da tela"""
    if a <= 0:
        return
    rrect(c, px, py, pw, ph, 50, INK, a, shadow=True)
    sx, sy, sw, sh = px + 22, py + 60, pw - 44, ph - 120
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(sx, sy, sw, sh), 20, 20), True)
    c.drawRect(skia.Rect.MakeXYWH(sx, sy, sw, sh), paint(SEA, a))
    zz = lerp(1.0, 0.25, z)
    cx, cy = sx + sw / 2, sy + sh / 2
    bw, bh = sw * 1.6 * zz, sh * 1.2 * zz
    bairro(c, cx - bw / 2, cy - bh / 2, bw, bh, a * (1 - 0.9 * z))
    mapas.draw_country(c, "Brazil", (sx + 20, sy + 40, sw - 40, sh - 140), a * z)
    c.restore()
    for k, s in enumerate(("+", "−")):
        c.drawCircle(sx + sw - 34, sy + 44 + k * 58, 24, paint("#FFFFFF", a))
        text_mid(c, s, sx + sw - 34, sy + 44 + k * 58, 34, "black", INK, a)
    # canto: barra gráfica + escala numérica
    rrect(c, sx + 12, sy + sh - 112, sw - 24, 100, 12, "#FFFFFF", a * 0.95)
    scale_bar(c, sx + 40, sy + sh - 100, 110, a * barra_a, ("0", "", barra), 18, 10)
    text(c, escala, sx + sw / 2, sy + sh - 26, 26, "black", BLUE, a)
    if pulso > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(sx + 12, sy + sh - 112, sw - 24, 100), 12, 12),
                    paint(GREEN, a * pulso * (0.5 + 0.5 * math.sin(motor_t[0] * 5)), stroke=5))


motor_t = [0.0]


def passo(c, n, s, x, y, a, col=None, size=36):
    """linha de passo numerado"""
    if a <= 0:
        return
    badge_num(c, n, x + 22, y - 12, a, 22, bg=col or PURPLE)
    ftext(c, s, x + 62, y, size, "black", INK, a, align="left")


def regua_cm(c, x, y, ncm, px_cm, a):
    """régua de ncm centímetros (px_cm px por cm), com o zero em x"""
    if a <= 0:
        return
    rrect(c, x - 16, y, ncm * px_cm + 32, 64, 8, "#E9C98F", a, shadow=True)
    for i in range(ncm * 10 + 1):
        xx = x + i * px_cm / 10
        if i % 10 == 0:
            line(c, xx, y, xx, y + 30, INK, a, 3)
            text(c, str(i // 10), xx, y + 56, 20, "bold", INK, a)
        else:
            line(c, xx, y, xx, y + (20 if i % 5 == 0 else 12), INK2, a, 1.5)
    text(c, "cm", x + ncm * px_cm + 34, y + 56, 20, "bold", GRAY, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    motor_t[0] = t
    head(c, t, B["start"], "MATEMÁTICA ENEM", "ESCALAS · EP. 2", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    folha_mapa(c, 220, 260, 1.0, aa)
    text(c, "original", 220 + FW / 2, 236, 28, "black", GRAY, aa)
    f = ep(t, C["01.a"] + 2.4, 1.4)
    s = lerp(1.0, 0.5, f)
    folha_mapa(c, 900, 260, s, aa * clamp(f * 4))
    text(c, "fotocópia reduzida à metade", 900 + FW * 0.5 / 2 + 40, 236, 28, "black", GRAY, ep(t, C["01.a"] + 2.4, 0.4))
    # o número impresso, ampliado numa etiqueta ao lado da cópia
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        line(c, 900 + (FW - 26) * 0.5, 260 + (FH - 30) * 0.5 - 8, 1330, 330, RED, ab, 2)
        rrect(c, 1250, 300, 380, 70, 14, "#FFFFFF", ab, shadow=True)
        text_mid(c, "ainda diz 1 : 50 000", 1440, 335, 30, "black", INK, ab)
        selo(c, 1440, 430, ab, "AGORA ESTÁ ERRADO", RED, -4, 30)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        line(c, 900 + 90 * 0.5, 260 + (FH - 62) * 0.5 + 6, 1080, 640, GREEN, ac, 2)
        selo(c, 1220, 650, ac, "A BARRA CONTINUA CERTA", GREEN, 3, 30)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        text(c, "POR QUÊ?", W / 2, 840, 80, "black", AMBER, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "converter a escala gráfica em numérica", "barra de 3 cm = 6 km  →  1 : 200 000"),
            ("02.b", "escolher o mapa certo para cada situação", "escala grande ou pequena?")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "DO EPISÓDIO 1", GREEN)
    at = ep(t, C["03.t"], 0.5)
    pill(c, "viu a aula de Cartografia? revisão com foco em Matemática", W / 2, 230, BLUE, size=28, a=at, anchor="center")
    nomes = [("MEDIDA REAL", "× denominador"), ("MEDIDA NO DESENHO", "÷ denominador"), ("A ESCALA", "desenho ÷ real")]
    for k, (n, sub) in enumerate(nomes):
        a = ep(t, C["03.a"] + 1.2 + 0.7 * k, 0.4)
        x = 480 + k * 480
        rrect(c, x - 210, 300, 420, 180, 22, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x, 300, a, 26, bg=PURPLE)
        text(c, n, x, 390, 34, "black", INK, a)
        text(c, sub, x, 440, 28, "bold", PURPLE, a)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        linha(c, [("cm  →  km:  ", INK), ("÷ 100 000", PURPLE)], W / 2, 590, 56, ab)
        fz = ep(t, C["03.b"] + 2.6, 0.6)
        linha(c, [("corte ", GREEN), ("5 zeros", GREEN)], W / 2, 690, 40, fz)


def b_celular(c, t, C, B):
    motor_t[0] = t
    head(c, t, B["start"], "NO CELULAR", "O ZOOM DO MAPA", BLUE)
    at = ep(t, C["04.t"], 0.5)
    z = ep(t, C["04.b"], 1.4)
    esc = "1 : 5 000" if z < 0.5 else "1 : 20 000 000"
    bar = "100 m" if z < 0.5 else "500 km"
    celular(c, 760, 170, 400, 680, z, at, esc, bar, pulso=ep(t, C["04.c"], 0.4))
    aa = ep(t, C["04.a"], 0.5)
    pill(c, "ZOOM APROXIMADO", 420, 360, GREEN, size=30, a=aa, anchor="center")
    text(c, "ruas e casas", 420, 430, 32, "black", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    pill(c, "ZOOM AFASTADO", 1500, 360, PURPLE, size=30, a=ab, anchor="center")
    text(c, "só o contorno do país", 1500, 430, 32, "black", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        text(c, "a BARRINHA no canto", 1500, 640, 34, "black", GREEN, acc)
        text(c, "muda junto com o zoom", 1500, 690, 30, "bold", INK2, acc)
        line(c, 1300, 680, 1150, 760, GREEN, acc, 3)


# ======================================================================
# bloco a — numérica × gráfica
# ======================================================================

def b_tipos(c, t, C, B):
    frame(c, t, B["start"], "DOIS JEITOS", "DE ESCREVER A ESCALA", BLUE)
    aa, ab, acc = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5), ep(t, C["05.c"], 0.5)
    for k, (a, tit, dfn) in enumerate(((aa, "ESCALA NUMÉRICA", "escrita com números"),
                                       (ab, "ESCALA GRÁFICA", "barra graduada: distâncias marcadas"))):
        x = 220 + k * 760
        rrect(c, x, 210, 720, 590, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 210, 720, 70, 24, BLUE, a * 0.14)
        text(c, tit, x + 360, 258, 34, "black", BLUE, a)
        text(c, dfn, x + 360, 330, 28, "bold", INK2, a)
    if aa > 0:
        text(c, "1 : 50 000", 580, 470, 90, "black", INK, aa)
        conferido(c, "direta para calcular", 270, 590, ep(t, C["05.a"] + 3.0, 0.4), True, 32)
    if ab > 0:
        scale_bar(c, 1110, 420, 460, ab, ("0", "0,5", "1 km"), 30, 28)
        conferido(c, "vale em qualquer ampliação", 1030, 590, ep(t, C["05.b"] + 4.5, 0.4), True, 32)
    if acc > 0:
        conferido(c, "falha se o mapa muda de tamanho", 270, 690, acc, False, 32)
        conferido(c, "exige régua para medir", 1030, 690, ep(t, C["05.c"] + 2.0, 0.4), False, 32)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# bloco b — a fotocópia
# ======================================================================

def b_copia(c, t, C, B):
    motor_t[0] = t
    head_seq(c, t, C, [("06", "A FOTOCÓPIA REDUZIDA", "POR QUE O NÚMERO ERRA?", AMBER),
                       ("07", "A BARRA VIAJA", "COM O MAPA", GREEN), ("08", "ATALHO", "CORRIGIR O NÚMERO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        a0 = ep(t, C["06.a"], 0.5)
        folha_mapa(c, 200, 230, 1.0, a0)
        text(c, "original", 200 + FW / 2, 214, 26, "black", GRAY, a0)
        # 1 cm destacado (= 40 px no papel original)
        if a0 > 0:
            rrect(c, 200 + 30, 230 + FH - 66, 60, 18, 4, GREEN, a0 * 0.35)
        ab = ep(t, C["06.b"], 0.5)
        f = ep(t, C["06.b"], 1.2)
        folha_mapa(c, 200 + 60, 600, lerp(0.7, 0.5, f), ab)
        text(c, "cópia reduzida à metade", 200 + 60 + FW * 0.25, 584, 24, "black", GRAY, ab)
        line(c, 1000, 210, 1000, 800, LINE, a0, 3)
        rows = [("06.a", [("original:  1 cm = ", INK), ("50 000 cm", INK), (" = ", INK), ("0,5 km", BLUE)]),
                ("06.b", [("cópia:  ", INK), ("0,5 cm", AMBER), (" = 0,5 km", INK)]),
                ("06.c", [("cópia:  1 cm = ", INK), ("1 km", BLUE), (" = 100 000 cm", INK)])]
        for k, (cue, partes) in enumerate(rows):
            a, dy = rise(t, C[cue])
            linha(c, partes, 1320, 300 + k * 110 + dy, 36, a)
        ad = ep(t, C["06.d"], 0.5)
        result_box(c, "escala real: 1 : 100 000", 1320, 640, 44, ad, GREEN)
        if ad > 0:
            text(c, "impresso: 1 : 50 000", 1320, 760, 34, "black", RED, ad)
            strike(c, 1150, 750, 1490, 750, ad, RED, ep(t, C["06.d"] + 0.6, 0.5))
        return
    if sid == "07":
        a0 = ep(t, C["07"], 0.4)
        f = ep(t, C["07.b"], 1.6)
        if t < C["07.b"]:
            folha_mapa(c, 220, 260, 0.8, a0)
            text(c, "original", 220 + FW * 0.4, 244, 26, "black", GRAY, a0)
            folha_mapa(c, 680, 260, 0.4, a0)
            text(c, "reduzida", 680 + FW * 0.2, 244, 26, "black", GRAY, a0)
            aa = ep(t, C["07.a"], 0.5)
            conferido(c, "a barra encolheu JUNTO", 680, 460, aa, True, 34)
            return
        folha_mapa(c, 180, 300, 0.6, a0)
        text(c, "original", 180 + FW * 0.3, 284, 26, "black", GRAY, a0)
        s = lerp(0.6, 1.2, f)
        folha_mapa(c, 520, 230, s, a0)
        text(c, "cópia ampliada 2×", 520 + FW * s / 2, 214, 26, "black", GRAY, ep(t, C["07.b"], 0.4))
        ab2 = ep(t, C["07.b"] + 1.8, 0.5)
        if ab2 > 0:
            bx, by = 520 + 30 * s, 230 + (FH - 62) * s
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx - 10, by - 10, 120 * s + 20, 10 * s + 40), 8, 8),
                        paint(GREEN, ab2, stroke=4))
            selo(c, 1400, 330, ab2, "CONTINUA CERTA", GREEN, -3, 32)
            text(c, "a barra cresceu junto", 1400, 420, 30, "bold", INK2, ab2)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            nx, ny = 520 + (FW - 26) * s, 230 + (FH - 30) * s
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(nx - 170 * s / 1.2, ny - 28 * s, 175 * s / 1.2, 40 * s), 8, 8),
                        paint(RED, acc, stroke=4))
            selo(c, 1400, 540, acc, "AGORA ESTÁ ERRADO", RED, 3, 32)
            text(c, "o número continua 1 : 50 000", 1400, 630, 30, "bold", INK2, acc)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            regra(c, "a barra VIAJA com o mapa; o número fica para trás", W / 2, 790, ad, 32)
        return
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 170, "ATALHO", ["AMPLIOU: divida o denominador  ·  REDUZIU: multiplique"], aa, 38)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "ampliou 2×", 560, 480, 34, "black", GREEN, ab)
        linha(c, [("50 000 ÷ 2 = ", INK), ("25 000", GREEN)], 560, 570, 48, ab)
        result_box(c, "1 : 25 000", 560, 690, 48, ep(t, C["08.b"] + 2.5, 0.4), GREEN)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        text(c, "reduziu à metade", 1360, 480, 34, "black", AMBER, acc)
        linha(c, [("50 000 × 2 = ", INK), ("100 000", AMBER)], 1360, 570, 48, acc)
        result_box(c, "1 : 100 000", 1360, 690, 48, ep(t, C["08.c"] + 1.8, 0.4), AMBER)
    line(c, 960, 450, 960, 760, LINE, ab, 3)


# ======================================================================
# bloco c — converter gráfica em numérica
# ======================================================================

PXCM = 110


def _barra_medida(c, t, x, y, ncm, rot, a, regua_a):
    """barra gráfica de ncm centímetros com o rótulo real e a régua embaixo"""
    if a <= 0:
        return
    rrect(c, x - 40, y - 70, ncm * PXCM + 80, 260, 18, PAPEL, a, shadow=True)
    scale_bar(c, x, y, ncm * PXCM, a, ("0", "", rot), 30, 22)
    regua_cm(c, x, y + 90, ncm, PXCM, regua_a)


def b_converter(c, t, C, B):
    head_seq(c, t, C, [("09", "O NOVO DE HOJE", "BARRA → NÚMERO", PURPLE), ("10", "SIMPLIFIQUE", "O DE CIMA VIRA 1", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        _barra_medida(c, t, 260, 300, 3, "6 km", aa, ep(t, C["09.b"], 0.5))
        passo(c, 1, "meça a barra: 3 cm", 1010, 290, ep(t, C["09.b"], 0.4))
        acc = ep(t, C["09.c"], 0.4)
        passo(c, 2, "mesma unidade: centímetros", 1010, 400, acc)
        linha(c, [("6 km × 100 000 = ", INK), ("600 000 cm", BLUE)], 1060, 470, 36, ep(t, C["09.c"] + 2.0, 0.4), align="left")
        ad = ep(t, C["09.d"], 0.4)
        passo(c, 3, "desenho ÷ real", 1010, 580, ad)
        if ad > 0:
            fr(c, "3 cm", "600 000 cm", 1240, 700, 46, None, ep(t, C["09.d"] + 1.8, 0.4))
        regra(c, "E = desenho ÷ real, na MESMA unidade", 560, 680, ep(t, C["09.d"], 0.5), 30)
        return
    a0 = ep(t, C["10"], 0.4)
    fr(c, "3", "600 000", 420, 330, 64, None, a0)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        text(c, "÷ 3", 560, 285, 34, "black", PURPLE, aa, align="left")
        text(c, "÷ 3", 560, 410, 34, "black", PURPLE, aa, align="left")
        text(c, "=", 660, 345, 64, "black", INK, aa)
        fr(c, "1", "200 000", 860, 330, 64, GREEN, ep(t, C["10.a"] + 2.4, 0.4))
    ab = ep(t, C["10.b"], 0.5)
    result_box(c, "1 : 200 000", 1340, 330, 60, ab, GREEN)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        K.atalho(c, 260, 520, 1400, 280, "ATALHO · OS 5 ZEROS DE VOLTA", [], acc)
        linha(c, [("6 km ÷ 3 cm = ", INK), ("2 km por cm", BLUE)], W / 2, 640, 44, ep(t, C["10.c"] + 1.0, 0.4))
        linha(c, [("2", INK), (" 00000", GREEN), ("  →  1 : 200 000", INK)], W / 2, 730, 44, ep(t, C["10.c"] + 3.5, 0.4))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("11", "SUA VEZ", "PAUSE E TENTE", GREEN), ("12", "VAMOS JUNTOS", "BARRA → NÚMERO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    _barra_medida(c, t, 300, 310, 2, "5 km", aa, aa)
    text(c, "escala numérica = ?", 1300, 340, 48, "black", INK, aa * (1 - ep(t, C["12"], 0.3)))
    pause_timer(c, t, C["11.end"] - 1.9, 1300, 520)
    if t >= C["12"]:
        a1 = ep(t, C["12.a"], 0.4)
        linha(c, [("5 km = 5 000 m = ", INK), ("500 000 cm", BLUE)], 1300, 300, 36, a1)
        ab = ep(t, C["12.b"], 0.4)
        if ab > 0:
            fr(c, "2 cm", "500 000 cm", 1130, 450, 40, None, ab)
            text(c, "=", 1300, 465, 48, "black", INK, ab)
            fr(c, "1", "250 000", 1440, 450, 48, GREEN, ep(t, C["12.b"] + 2.4, 0.4))
        result_box(c, "1 : 250 000", 1300, 600, 46, ep(t, C["12.b"] + 3.2, 0.4), GREEN)
        acc = ep(t, C["12.c"], 0.4)
        K.atalho(c, 300, 690, 1320, 120, "ATALHO", ["5 km ÷ 2 cm = 2,5 km por cm  →  + 5 zeros = 250 000"], acc, 32)


# ======================================================================
# blocos d, e — grande × pequena e a fração
# ======================================================================

def b_zoom(c, t, C, B):
    motor_t[0] = t
    head_seq(c, t, C, [("13", "ESCALA GRANDE OU PEQUENA?", "O ZOOM DO CELULAR", BLUE),
                       ("14", "O QUE MUDA", "DETALHE × TERRITÓRIO", BLUE)])
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        at = ep(t, C["13"], 0.5)
        z = ep(t, C["13.b"], 1.4)
        celular(c, 760, 170, 400, 680, z, at, "1 : 5 000" if z < 0.5 else "1 : 20 000 000", "100 m" if z < 0.5 else "500 km")
        aa = ep(t, C["13.a"], 0.5)
        pill(c, "1 : 5 000", 420, 330, GREEN, size=34, a=aa, anchor="center")
        text(c, "o bairro", 420, 400, 30, "black", INK2, aa)
        ab = ep(t, C["13.b"], 0.5)
        pill(c, "1 : 20 000 000", 1500, 330, PURPLE, size=34, a=ab, anchor="center")
        text(c, "o país inteiro", 1500, 400, 30, "black", INK2, ab)
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            text(c, "ESCALA GRANDE", 420, 560, 40, "black", GREEN, acc)
            text(c, "zoom aproximado", 420, 610, 30, "bold", INK2, acc)
            text(c, "dá para ver as ruas", 420, 650, 30, "bold", INK2, acc)
            a2 = ep(t, C["13.c"] + 3.6, 0.4)
            text(c, "ESCALA PEQUENA", 1500, 560, 40, "black", PURPLE, a2)
            text(c, "zoom afastado", 1500, 610, 30, "bold", INK2, a2)
            text(c, "só o contorno do país", 1500, 650, 30, "bold", INK2, a2)
        return
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    pill(c, "DETALHE = o quanto de coisa pequena dá para ver (rua, casa)", W / 2, 220, BLUE, size=26, a=aa, anchor="center")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        bairro(c, 300, 290, 520, 300, ab)
        text(c, "ESCALA GRANDE", 560, 640, 38, "black", GREEN, ab)
        text(c, "+ detalhe  ·  − território", 560, 690, 32, "bold", INK2, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 1100, 290, 520, 300, 14, SEA, acc)
        mapas.draw_country(c, "Brazil", (1110, 300, 500, 280), acc)
        text(c, "ESCALA PEQUENA", 1360, 640, 38, "black", PURPLE, acc)
        text(c, "− detalhe  ·  + território", 1360, 690, 32, "bold", INK2, acc)
    ad = ep(t, C["14.d"], 0.5)
    regra(c, "DENOMINADOR MENOR  →  ESCALA MAIOR", W / 2, 785, ad, 36)


def b_fracao(c, t, C, B):
    frame(c, t, B["start"], "O RACIOCÍNIO DA FRAÇÃO", "PARA NUNCA MAIS TROCAR", PURPLE)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        fr(c, "1", "10 000", 560, 300, 60, BLUE, aa)
        fr(c, "1", "10 000 000", 1360, 300, 60, PURPLE, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        K.pizza(c, 560, 540, 110, 2, 1, ab)
        fr(c, "1", "2", 720, 540, 40, INK, ab)
        K.pizza(c, 1360, 540, 110, 20, 1, ab)
        fr(c, "1", "20", 1530, 540, 40, INK, ab)
        text_mid(c, ">", 960, 540, 90, "black", GREEN, ep(t, C["15.b"] + 2.6, 0.4))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        text_mid(c, ">", 960, 300, 90, "black", GREEN, acc)
        text(c, "escala MAIOR", 560, 410, 30, "black", GREEN, acc)
        text(c, "escala menor", 1360, 410, 30, "black", GRAY, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        K.atalho(c, 560, 690, 800, 120, "ATALHO", [], ad)
        text_mid(c, "na dúvida, leia como FRAÇÃO", W / 2, 770, 34, "black", INK, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["A barra gráfica viaja com o mapa; o número não.", "Escala grande: zoom aproximado, mais detalhe.",
          "Denominador menor, escala maior."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 60)


ERROS = [("Achar que 1 : 250 000 é maior que 1 : 50 000", "250 000 é um número maior",
          "ele está EMBAIXO da fração: denominador maior, escala menor"),
         ("Confiar no número de um mapa ampliado ou reduzido", "está impresso no mapa, com cara de oficial",
          "o número não mudou com o papel: use a barra gráfica"),
         ("Converter a barra sem igualar as unidades", "4 cm e 10 km estão ali, prontos: \"4 : 10\"",
          "passe tudo para cm: 10 km = 1 000 000 cm")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# Questões 8 e 4 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS8 = [("A", "1 : 2 500", "parou nos metros", RED), ("B", "1 : 25 000", "um zero a menos", RED),
         ("C", "1 : 250 000", "", GREEN), ("D", "1 : 400 000", "multiplicou", RED),
         ("E", "1 : 2 500 000", "um zero a mais", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    _enunciado(c, [("Em um mapa, a escala gráfica é representada por uma barra de 4 cm de comprimento, "
                    "correspondente a 10 km no terreno.", INK), ("A escala numérica desse mapa é", BLUE)], a0, 250)
    text(c, "Questão 8 do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABDE"}
    if t >= C["20.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS8, 1000, 250, 680, 40, C["21.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["20.end"] - 1.9, 540, 620)
    if t >= C["21"]:
        ra = ep(t, C["21"], 0.4)
        rrect(c, 170, 470, 760, 340, 18, "#FFFFFF", ra, shadow=True)
        linha(c, [("10 km = 10 000 m = ", INK), ("1 000 000 cm", BLUE)], 550, 520, 32, ep(t, C["21.a"], 0.4))
        ab = ep(t, C["21.b"], 0.4)
        if ab > 0:
            fr(c, "4 cm", "1 000 000 cm", 380, 630, 34, None, ab)
            text(c, "=", 560, 642, 40, "black", INK, ab)
            fr(c, "1", "250 000", 700, 630, 40, GREEN, ep(t, C["21.b"] + 2.4, 0.4))
        conferido(c, "1 cm = 2,5 km → 4 cm = 10 km", 220, 770, ep(t, C["21.c"], 0.4), True, 28)


ALTS4 = [("A", "1 : 10 000", "", GREEN), ("B", "1 : 100 000", "afastado demais", RED),
         ("C", "1 : 500 000", "afastado demais", RED), ("D", "1 : 1 000 000", "afastado demais", RED),
         ("E", "1 : 10 000 000", "número maior ≠ escala maior", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Um estudante precisa de um mapa que mostre com o maior nível de detalhe possível as ruas de um "
                    "bairro.", INK), ("Entre as opções disponíveis, ele deve escolher a de escala", BLUE)], a0, 250)
    text(c, "Questão 4 do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"E": C["24.xe"], "B": C["24.xb"], "C": C["24.xb"] + 0.4, "D": C["24.xb"] + 0.8}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 40, C["24.ok"], "A", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["23.end"] - 1.9, 540, 620)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 470, 760, 340, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["24.a"], 0.4)
        text(c, "mais detalhe = escala MAIOR", 550, 530, 32, "black", GREEN, aa)
        text(c, "= denominador MENOR", 550, 580, 32, "black", PURPLE, ep(t, C["24.a"] + 2.4, 0.4))
        conferido(c, "1 : 10 000 → 1 cm = 100 m", 220, 670, ep(t, C["24.b"], 0.4), True, 30)
        conferido(c, "1 : 10 000 000 → 1 cm = 100 km", 220, 750, ep(t, C["24.xe"] + 2.5, 0.4), False, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PLANTAS E MAQUETES", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    if aa > 0:
        rrect(c, 420, 300, 160, 160, 6, BLUE, aa * 0.2)
        c.drawRect(skia.Rect.MakeXYWH(420, 300, 160, 160), paint(BLUE, aa, stroke=4))
        text_mid(c, "1 cm²", 500, 380, 40, "black", BLUE, aa)
        text(c, "planta 1 : 200", 500, 520, 34, "black", INK2, aa)
        text_mid(c, "→", 760, 380, 80, "black", INK, aa)
        text_mid(c, "? na vida real", 1100, 380, 60, "black", INK, aa)
    ab = ep(t, C["26.b"], 0.5)
    if ab > 0:
        text(c, "200 cm²", 1100, 560, 60, "black", RED, ab)
        strike(c, 980, 540, 1220, 540, ab, RED, ep(t, C["26.b"] + 1.0, 0.4))
        selo(c, 1100, 650, ep(t, C["26.b"] + 1.2, 0.4), "ERROU POR UM FATOR DE 200", RED, -3, 30)
    pill(c, "ep. 3 · plantas e maquetes", W / 2, 780, PURPLE, size=32, a=ep(t, C["26.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"],
        "Já tinha reparado na barrinha do mapa?", canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, celular=b_celular, tipos=b_tipos, copia=b_copia,
              converter=b_converter, exercicio=b_exercicio, zoom=b_zoom, fracao=b_fracao, recap=b_recap, erros=b_erros,
              q8=b_q8, q4=b_q4, ponte=b_ponte, cta=b_cta)
