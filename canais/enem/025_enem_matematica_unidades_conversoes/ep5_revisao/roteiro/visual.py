"""Visual — Unidades de Medida e Conversões, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): escada · caixa de leite e cubo · relógio ·
fração com unidades riscadas. Caixa de leite, relógio e andares no mesmo traço dos visual.py dos eps 2 e 3.
Ícones das áreas nas questões (area_icone()): régua · aquário · ônibus · frasco · lâmpada.
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
_s = importlib.util.spec_from_file_location("comum025", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_unidades_ep5_revisao.mp4"
CARD_R = K.CARD_R
DEGRAU = "#EEF1F6"
LEITE = "#FBFBF6"
AGUA = "#5FA8E8"
CUBO_TOPO, CUBO_FRENTE, CUBO_LADO = "#C9DEF8", "#9CC3F0", "#7AAAE0"
UNID = ["km", "hm", "dam", "m", "dm", "cm", "mm"]


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças (mesmo traço dos episódios 1–3)
# ======================================================================

def mini_escada(c, cx, cy, s, a, hl=3):
    """escada de 7 degraus (ep1), do km (alto, esquerda) ao mm (baixo, direita)"""
    if a <= 0:
        return
    sw, sh = 46 * s, 22 * s
    x0, y0 = cx - 3.5 * sw, cy - 3.5 * sh
    floor = y0 + 7 * sh + 26 * s
    for i, u in enumerate(UNID):
        x, y = x0 + i * sw, y0 + i * sh
        rrect(c, x + 2, y, sw - 4, floor - y, 8 * s, mix(DEGRAU, BLUE, 0.18) if i == hl else DEGRAU, a, shadow=True)
        text_mid(c, u, x + sw / 2, y + 16 * s, 17 * s, "black", BLUE if i == hl else INK, a)


def caixa_leite(c, cx, base_y, w, h, a, rot="1 L"):
    """caixa de leite longa-vida (ep2)"""
    if a <= 0:
        return
    x = cx - w / 2
    top = base_y - h
    rrect(c, x, top, w, h, 6, LEITE, a, shadow=True)
    p = skia.Path(); p.moveTo(x, top + 2); p.lineTo(cx, top - w * 0.32); p.lineTo(x + w, top + 2); p.close()
    c.drawPath(p, paint("#ECEBE3", a)); c.drawPath(p, paint("#B8B8AE", a, stroke=2.5))
    rrect(c, x, top + h * 0.30, w, h * 0.36, 0, BLUE, a * 0.9)
    text_mid(c, "LEITE", cx, top + h * 0.42, w * 0.2, "black", "#FFFFFF", a)
    text_mid(c, rot, cx, top + h * 0.57, w * 0.24, "black", "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, top, w, h), 6, 6), paint("#B8B8AE", a, stroke=2.5))


def _iso(cx, cy, s, x, y, z):
    return (cx + (x - y) * s * 0.866, cy + (x + y) * s * 0.5 - z * s)


def _poly(c, pts, col, a, stroke=None):
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint(col, a))
    if stroke:
        c.drawPath(p, paint(stroke, a, stroke=2))


def cubo(c, cx, cy, s, a, div=3):
    """cubo isométrico de aresta 1 (em unidades s), com a grade de cubinhos nas faces visíveis"""
    if a <= 0:
        return
    P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
    _poly(c, [P(0, 0, 1), P(1, 0, 1), P(1, 1, 1), P(0, 1, 1)], CUBO_TOPO, a, "#5E86B8")
    _poly(c, [P(1, 0, 1), P(1, 1, 1), P(1, 1, 0), P(1, 0, 0)], CUBO_LADO, a, "#5E86B8")
    _poly(c, [P(0, 1, 1), P(1, 1, 1), P(1, 1, 0), P(0, 1, 0)], CUBO_FRENTE, a, "#5E86B8")
    pg = paint("#FFFFFF", a * 0.55, stroke=1.6)
    for k in range(1, div):
        f = k / div
        for (p0, p1) in ((P(f, 0, 1), P(f, 1, 1)), (P(0, f, 1), P(1, f, 1)), (P(1, f, 1), P(1, f, 0)),
                         (P(1, 0, f), P(1, 1, f)), (P(f, 1, 1), P(f, 1, 0)), (P(0, 1, f), P(1, 1, f))):
            c.drawLine(p0[0], p0[1], p1[0], p1[1], pg)


def relogio(c, cx, cy, r, minutos, a, col=None):
    """relógio analógico (ep3): setor de 0 até `minutos` pintado, marcas a cada 5 minutos"""
    if a <= 0:
        return
    col = col or GREEN
    c.drawCircle(cx, cy, r + 8, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 8, paint(INK, a, stroke=6))
    if minutos > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, min(minutos, 59.99) / 60 * 360, False); p.close()
        c.drawPath(p, paint(col, a * 0.28))
    for k in range(12):
        ang = -math.pi / 2 + k * math.pi / 6
        r0 = r - (r * 0.18 if k % 3 == 0 else r * 0.09)
        c.drawLine(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + r * math.cos(ang), cy + r * math.sin(ang),
                   paint(INK, a * 0.8, stroke=4 if k % 3 == 0 else 2))
    ang = -math.pi / 2 + minutos / 60 * 2 * math.pi
    c.drawLine(cx, cy, cx + (r - 14) * math.cos(ang), cy + (r - 14) * math.sin(ang), paint(col, a, stroke=7, cap_round=True))
    c.drawCircle(cx, cy, 7, paint(INK, a))


def fracao_txt(c, cx, cy, cima, baixo, size, a, col=None, risca=(False, False), risca_a=1.0):
    """fração de texto (unidades) com traço; risca = (riscar cima?, riscar baixo?)"""
    if a <= 0:
        return 0
    col = col or INK
    w = max(text_w(cima, "black", size), text_w(baixo, "black", size)) + 24
    text_mid(c, cima, cx, cy - size * 0.62, size, "black", col, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, PURPLE, a, 4)
    text_mid(c, baixo, cx, cy + size * 0.62, size, "black", col, a)
    for k, yy in ((0, cy - size * 0.62), (1, cy + size * 0.62)):
        if risca[k] and risca_a > 0:
            wt = text_w(cima if k == 0 else baixo, "black", size)
            line(c, cx - wt / 2 - 4, yy + size * 0.25, cx + wt / 2 + 4, yy - size * 0.25, RED, a * risca_a, 4)
    return w


def cadeia(c, cx, cy, s, a, risca_a=1.0):
    """ep4: 72 km/h · 1000 m / 1 km · 1 h / 3600 s, com km e h riscados"""
    if a <= 0:
        return
    sz = 34 * s
    fracao_txt(c, cx - 150 * s, cy, "72 km", "h", sz, a, risca=(True, True), risca_a=risca_a)
    text_mid(c, "·", cx - 78 * s, cy, sz, "black", INK2, a)
    fracao_txt(c, cx, cy, "1000 m", "1 km", sz, a, risca=(False, True), risca_a=risca_a)
    text_mid(c, "·", cx + 82 * s, cy, sz, "black", INK2, a)
    fracao_txt(c, cx + 160 * s, cy, "1 h", "3600 s", sz, a, risca=(True, False), risca_a=risca_a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 a escada
        mini_escada(c, 0, -30, 1.2, a)
        text_mid(c, "unidade menor, número maior", 0, 140, 26, "black", INK2, a)
    elif k == 1:    # ep2 caixa de leite e cubo
        caixa_leite(c, -80, 90, 70, 150, a)
        cubo(c, 60, -20, 70, a)
        text_mid(c, "1 L = 1 dm³", 0, 140, 28, "black", INK2, a)
    elif k == 2:    # ep3 o relógio
        relogio(c, 0, -10, 95, 24, a)
        text_mid(c, "de 60 em 60", 0, 140, 28, "black", INK2, a)
    elif k == 3:    # ep4 unidades riscadas
        cadeia(c, 0, -10, 1.1, a)
        text_mid(c, "risque: o que sobra é a resposta", 0, 140, 26, "black", INK2, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones das áreas das questões: régua · aquário · ônibus · frasco · lâmpada"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # régua (Geometria)
        rrect(c, -90, -22, 180, 44, 6, "#F4D68A", a, shadow=True)
        for i in range(19):
            h = 18 if i % 5 == 0 else 10
            line(c, -84 + i * 9.3, -22, -84 + i * 9.3, -22 + h, INK, a, 2)
    elif k == 1:    # aquário
        rrect(c, -80, -55, 160, 110, 10, mix("#FFFFFF", AGUA, 0.35), a, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(-80, -30, 160, 85), paint(mix("#FFFFFF", AGUA, 0.6), a))
        p = skia.Path(); p.moveTo(-10, 10); p.lineTo(20, -6); p.lineTo(20, 26); p.close()
        c.drawPath(p, paint(AMBER, a)); c.drawCircle(-22, 10, 18, paint(AMBER, a))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-80, -55, 160, 110), 10, 10), paint("#3E6FA8", a, stroke=3))
    elif k == 2:    # ônibus
        rrect(c, -95, -45, 190, 80, 14, GREEN, a, shadow=True)
        for i in range(4):
            rrect(c, -80 + i * 42, -34, 34, 28, 5, "#E8F6EE", a)
        c.drawCircle(-55, 40, 16, paint(INK, a)); c.drawCircle(55, 40, 16, paint(INK, a))
    elif k == 3:    # frasco (Química)
        p = skia.Path()
        p.moveTo(-18, -60); p.lineTo(18, -60); p.lineTo(18, -15); p.lineTo(60, 50); p.lineTo(-60, 50); p.lineTo(-18, -15)
        p.close()
        c.drawPath(p, paint("#FFFFFF", a))
        q = skia.Path(); q.moveTo(-38, 18); q.lineTo(38, 18); q.lineTo(60, 50); q.lineTo(-60, 50); q.close()
        c.drawPath(q, paint(mix("#FFFFFF", PURPLE, 0.45), a))
        c.drawPath(p, paint(INK, a, stroke=3))
    elif k == 4:    # lâmpada (conta de luz)
        c.drawCircle(0, -15, 46, paint(mix("#FFFFFF", AMBER, 0.55), a))
        c.drawCircle(0, -15, 46, paint(AMBER, a, stroke=4))
        rrect(c, -22, 28, 44, 34, 6, "#9AA4AE", a)
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    for k, (s, col) in enumerate((("MATEMÁTICA", BLUE), ("FÍSICA", PURPLE), ("QUÍMICA", GREEN), ("GEOGRAFIA", AMBER))):
        chip(c, s, 420 + k * 360, 250, col, aa * ep(t, C["01.a"] + 0.4 * k, 0.4), 34)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 340, 800, 230, 24, mix("#FFFFFF", RED, 0.08), ab, shadow=True)
        text(c, "3,5 t = 350 kg", 960, 445, 64, "black", INK, ab)
        line(c, 700, 425, 1220, 425, RED, ab, 6)
        text(c, "a conta fecha… e está errada", 960, 520, 32, "bold", RED, ab)
    ac = ep(t, C["01.c"], 0.5)
    chip(c, "TREINO", 640, 760, PURPLE, ac, 36)
    chip(c, "9 FRASES", 960, 760, AMBER, ep(t, C["01.c"] + 0.5, 0.4), 36)
    chip(c, "5 QUESTÕES", 1280, 760, GREEN, ep(t, C["01.c"] + 1.0, 0.4), 36)


ONDE = [("02.a", "GEOMETRIA", "m² com medidas em cm", 0), ("02.b", "FÍSICA", "km/h com tempo em s", 2),
        ("02.c", "QUÍMICA", "g/L com volume em mL", 3), ("02.d", "GEOGRAFIA", "hectares · toneladas", None),
        ("02.e", "DIA A DIA", "receita · água · luz", 4)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "O ERRO SILENCIOSO", "ONDE A CONVERSÃO DECIDE", BLUE)
    a0 = ep(t, C["02"], 0.5) * (1 - ep(t, C["02.a"], 0.4))
    pill(c, "a conta fecha, o número sai redondo… e está errado", W / 2, 470, RED, size=32, a=a0, anchor="center")
    for k, (cue, tit, sub, ic) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 330
        rrect(c, x - 150, 250 + d, 300, 440, 24, "#F7F7F5", a)
        if ic is not None:
            area_icone(c, ic, x, 400 + d, 0.9, a)
        else:
            text_mid(c, "1 ha", x, 400 + d, 60, "black", AMBER, a)
        text(c, tit, x, 560 + d, 30, "black", BLUE, a)
        para(c, sub, x, 610 + d, 23, "bold", INK2, a, 260, 28, align="center")


INDICE = [("EP. 1", "a escada · unidade menor, número maior"), ("EP. 2", "grade 100 · cubo 1 000 · caixa de leite = 1 L"),
          ("EP. 3", "relógio de 60 em 60 · dois andares"), ("EP. 4", "frações que valem 1 · risque as unidades")]
IND_CUES = ["03.a", "03.b", "04.a", "04.b"]
IND_POS = [(560, 190), (1360, 190), (560, 505), (1360, 505)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 360, y, 720, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 360, y, 720, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 330, y + 28, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x - 165, y + 130, 0.52 if k == 3 else 0.62, a)
        lns = s.split(" · ")
        for j, ln in enumerate(lns):
            sz = 26
            while text_w(ln, "black", sz) > 300:
                sz -= 1
            text(c, ln, x + 185, y + 140 + (j - (len(lns) - 1) / 2) * 36, sz, "black", INK if on_ else INK2, a)


FATOS = [("05.a", "1", "ÁREA × 100 · VOLUME × 1 000", "por degrau da escada", BLUE),
         ("05.b", "2", "1 L = 1 dm³", "1 m³ = 1 000 L", PURPLE),
         ("05.c", "3", "O TEMPO NÃO É DECIMAL", "depois da vírgula: × 60", GREEN)]


def b_fatos(c, t, C, B):
    frame(c, t, B["start"], "SE O TEMPO APERTAR", "OS TRÊS FATOS QUE RESOLVEM QUASE TUDO", GREEN)
    for k, (cue, n, tit, sub, col) in enumerate(FATOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 230 + d, 500, 530, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, n, x, 290 + d, a, 30, bg=col)
        if k == 0:
            cubo(c, x, 395 + d, 80, a)
        elif k == 1:
            caixa_leite(c, x, 545 + d, 80, 170, a)
        else:
            relogio(c, x, 450 + d, 95, 36, a)
        for j, ln in enumerate(tit.split(" · ")):
            text(c, ln, x, 630 + d + j * 40 - (20 if " · " in tit else 0), 30, "black", col, a)
        text(c, sub, x, 712 + d, 26, "bold", INK2, a)


# treino: (cue, de, para, cor)
TREINO = [("b", "2 m²", "20 000 cm²", BLUE), ("c", "0,3 m³", "300 dm³", BLUE), ("d", "2 500 cm³", "2,5 L", PURPLE),
          ("e", "4 m³", "4 000 L", PURPLE), ("f", "1,2 h", "1 h 12 min", GREEN), ("g", "0,6 h", "36 min", GREEN)]


def b_treino(c, t, C, B):
    head_seq(c, t, C, [("06", "TREINO-RELÂMPAGO", "SEIS CONVERSÕES", PURPLE),
                       ("07", "CONFERINDO", "ÁREA · LITRO · TEMPO", PURPLE)])
    card(c, *CARD_R)
    for k, (cue, de, pa, col) in enumerate(TREINO):
        a, d = rise(t, C[f"06.{cue}"])
        if a <= 0:
            continue
        r_, j = divmod(k, 3)
        x, y = 470 + j * 490, 230 + r_ * 245 + d
        ar = ep(t, C[f"07.{cue}"], 0.4) if t >= C["07"] else 0
        rrect(c, x - 220, y, 440, 205, 20, mix("#F7F7F5", col, 0.10 + 0.08 * ar), a)
        pill(c, ("ÁREA/VOLUME", "LITRO", "TEMPO")[k // 2], x, y + 26, col, size=17, a=a, anchor="center", bounds=(0, 1920))
        ftext(c, de, x, y + 95, 44, "black", INK, a)
        arrow(c, x, y + 112, x, y + 140, INK2, a, 4, 12)
        if ar <= 0:
            fmid(c, "?", x, y + 170, 46, "black", AMBER, a)
        else:
            sz = 44
            while ftw(pa, sz) > 400:
                sz -= 2
            ftext(c, pa, x, y + 186, sz, "black", col, ar)
    pause_timer(c, t, C["06.end"] - 1.9, W / 2, 770)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        boxed(c, 520, 728, 880, 84, AMBER, aa, 0.08)
        text_mid(c, "as de tempo são as que mais derrubam", W / 2, 770, 32, "black", INK, aa)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["08"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["08.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["08.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["08.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("área", "1 m² = 100 cm²", False, "1 m tem 100 cm",
     "área é uma grade: 100 × 100", "1 m² = 10 000 cm²", 1),
    ("volume", "1 m³ = 1 000 000 cm³", True, "um milhão parece demais",
     "é um cubo: 100 × 100 × 100", "100³ = 1 000 000", 1),
    ("volume e litro", "1 m³ = 1 litro", False, "os dois medem volume",
     "o litro é o DECÍMETRO cúbico", "1 m³ = 1 000 L", 1),
    ("tempo", "2,4 h = 2 h 40 min", False, "o 4 parece quarenta",
     "o relógio conta de 60 em 60: 0,4 × 60", "2 h 24 min", 2),
    ("velocidade", "km/h → m/s: divida por 3,6", True, "muita gente multiplica",
     "em m/s o número é sempre o MENOR", "72 km/h = 20 m/s", 3),
    ("massa", "1 t = 100 kg", False, "100 é um número redondo",
     "a tonelada é um quilo de quilos", "1 t = 1 000 kg", 0),
    ("área agrária", "1 ha = 10 000 m²", True, "muita gente lembra de 1 000",
     "quadrado de 100 m de lado: 100 × 100", "1 ha = 1 hm²", 1),
    ("somar medidas", "1,5 kg + 300 g = 301,5", False, "a conta fecha, sem alarme",
     "padronize antes: tudo em gramas", "1 500 + 300 = 1 800 g", 0),
    ("unidade composta", "g/cm³ → kg/m³: só o grama", False, "o grama salta aos olhos",
     "dois andares: converta massa e volume", "1,2 g/cm³ = 1 200 kg/m³", 3),
]
VF_IDS = [f"{9 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 400, 0.62, a0)
    text(c, ctx.upper(), 960, 310, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 60
    while ftw(conta, sz) > 760:
        sz -= 2
    fmid(c, conta, 960, 410, sz, "black", INK, a0)
    if ar > 0 and not ver:
        w = ftw(conta, sz)
        strike(c, 960 - w / 2 - 10, 415, 960 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 700, 30, "black", GREEN, ag, 760)
        szf = 44
        while ftw(fix, szf) > 600:
            szf -= 2
        fmid(c, fix, 1340, 715, szf, "black", GREEN, ag)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["18.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["18.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["18.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    text(c, "padronize as unidades em voz alta, antes da conta", W / 2, 740, 32, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: o que padronizar · passos: (cue, texto) · confere: (cue, texto)

Q = {
    "q1": dict(ids=("19", "20"), titulo="O TERRENO", area="GEOMETRIA", ic=0, ok="D",
               enun=[("a", "Um terreno retangular mede 250 m por 80 m.", False),
                     ("b", "A área desse terreno, em hectares, é", True)],
               alts=[("A", "0,02", "como se fosse km²", AMBER), ("B", "200", "usou o are (100 m²)", AMBER),
                     ("C", "20", "hectare de 1 000 m²", RED), ("D", "2", "", GREEN),
                     ("E", "200 000 000", "multiplicou", RED)],
               pad="tudo em metros", passos=[("a", "250 × 80 = 20 000 m²"), ("b", "20 000 ÷ 10 000 = 2 ha")],
               confere=("v", "≈ 3 campos de futebol")),
    "q2": dict(ids=("21", "22"), titulo="O AQUÁRIO", area="DIA A DIA", ic=1, ok="E",
               enun=[("a", "Um aquário tem 60 cm de comprimento, 30 cm de largura e 40 cm de altura.", False),
                     ("b", "Cheio, ele comporta", True)],
               alts=[("A", "72 000 litros", "cm³ como litro", RED), ("B", "7 200 litros", "degrau de 10", AMBER),
                     ("C", "720 litros", "degrau de 100", AMBER), ("D", "0,072 litro", "m³ como litro", RED),
                     ("E", "72 litros", "", GREEN)],
               pad="tudo em centímetros", passos=[("a", "60 × 30 × 40 = 72 000 cm³"), ("b", "72 000 ÷ 1 000 = 72 L")],
               confere=("v", "≈ 70 garrafas de 1 L")),
    "q3": dict(ids=("23", "24"), titulo="A VIAGEM DE ÔNIBUS", area="FÍSICA", ic=2, ok="C",
               enun=[("a", "Um ônibus mantém a velocidade de 25 m/s numa viagem de 216 km.", False),
                     ("b", "A viagem dura", True)],
               alts=[("A", "2 h 4 min", "0,4 h = 4 min", AMBER), ("B", "2 h 40 min", "décimo = minuto", RED),
                     ("C", "2 h 24 min", "", GREEN), ("D", "cerca de 8 h 38 min", "não converteu m/s", AMBER),
                     ("E", "cerca de 31 h", "3,6 ao contrário", RED)],
               pad="km com km/h", passos=[("a", "25 × 3,6 = 90 km/h"), ("b", "216 ÷ 90 = 2,4 h"),
                                          ("c", "0,4 × 60 = 24 min → 2 h 24 min")],
               confere=None),
    "q4": dict(ids=("25", "26"), titulo="A SOLUÇÃO DE AÇÚCAR", area="QUÍMICA", ic=3, ok="B",
               enun=[("a", "Foram dissolvidos 12 g de açúcar em água, formando 400 mL de solução.", False),
                     ("b", "A concentração, em gramas por litro, é", True)],
               alts=[("A", "0,03", "não converteu mL", RED), ("B", "30", "", GREEN), ("C", "3", "1 L = 100 mL?", AMBER),
                     ("D", "4,8", "multiplicou", RED), ("E", "300", "vírgula demais", AMBER)],
               pad="litro embaixo", passos=[("a", "400 mL = 0,4 L"), ("b", "12 ÷ 0,4 = 30 g/L")],
               confere=("v", "12 × 2,5 = 30 em 1 L")),
    "q5": dict(ids=("27", "28"), titulo="O SECADOR DE CABELO", area="CONTA DE LUZ", ic=4, ok="A",
               enun=[("a", "Um secador de cabelo de 2 000 W fica ligado 15 minutos por dia, durante 30 dias.", False),
                     ("b", "O consumo, em kWh, é", True)],
               alts=[("A", "15", "", GREEN), ("B", "9", "15 min = 0,15 h?", AMBER), ("C", "900", "minutos como horas", RED),
                     ("D", "15 000", "não passou W → kW", RED), ("E", "0,5", "só um dia", AMBER)],
               pad="quilowatt e hora", passos=[("a", "2 000 W = 2 kW · 15 min = 0,25 h"),
                                               ("b", "2 × 0,25 × 30 = 15 kWh")],
               confere=None),
}


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · {d['area']}", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        area_icone(c, d["ic"], 760, 230, 0.55, a0)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 170, 260, 650, 84, PURPLE, ad, 0.08)
                pill(c, "PADRONIZE", 190, 260, PURPLE, size=18, a=ad, bounds=(0, 1920))
                ftext(c, d["pad"], 190, 316, 30, "black", INK, ad, align="left")
            yy = 420
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                sz = 36
                while ftw(s, sz) > 640:
                    sz -= 2
                ftext(c, s, 180, yy, sz, "black", GREEN if last else INK, a, align="left")
                yy += 66
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, s, 190, yy + 10, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 30)
            result_box(c, f"Letra {d['ok']}", 1290, 690, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("29.b", "EP. 1", ["a escada nos dois sentidos", "unidade menor, número maior", "t · kg · g · mg",
                            "padronizar antes de calcular"]),
         ("29.c", "EP. 2", ["área × 100 · volume × 1 000", "1 ha = 10 000 m²", "1 L = 1 dm³ · 1 m³ = 1 000 L",
                            "1 L de água = 1 kg"]),
         ("30.a", "EP. 3", ["parte decimal da hora × 60", "km/h ↔ m/s com o 3,6", "unidade composta: dois andares"]),
         ("30.b", "EP. 4", ["análise dimensional", "o fator que o enunciado dá"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["29.a"], 0.5) * (1 - ep(t, C["29.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 2 else 1
        x = 170 if col_ == 0 else 990
        y0 = 190 + sum(len(CHECK[j][2]) * 46 + 34 for j in range(0 if col_ == 0 else 2, k))
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 46
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            K.ftext(c, it, x + 158, yy + 10, 27, "bold", INK, a, align="left")
    ae = ep(t, C["30.c"], 0.5)
    if ae > 0:
        boxed(c, 990, 690, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 740, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["31.a"], 0.5)
    ab = ep(t, C["31.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["31.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 230 + k * 82, 220 + r_ * 86
        rrect(c, x, y, 66, 70, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 560, 1460, 200, AMBER, ac, 0.10)
        area_icone(c, 2, 420, 660, 0.75, ac)
        area_icone(c, 3, 1500, 660, 0.85, ac)
        text_mid(c, "inclua FÍSICA e QUÍMICA", W / 2, 638, 40, "black", INK, ac)
        text_mid(c, "a conversão aparece no meio da conta", W / 2, 694, 30, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Escalas, plantas e mapas", W / 2, 330, 62, "black", PURPLE, aa)
    for k, s in enumerate(("1 : 100", "1 : 50 000", "cm → km")):
        chip(c, s, 640 + k * 320, 450, BLUE, aa * ep(t, C["32.a"] + 0.6 + 0.3 * k, 0.4), 34)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        boxed(c, 440, 540, 1040, 250, GREEN, ab, 0.08)
        mini_escada(c, 760, 665, 1.5, ab)
        text(c, "a escada de unidades", 1210, 650, 34, "black", GREEN, ab)
        text(c, "o tempo todo", 1210, 700, 34, "black", INK, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, onde=b_onde, indice=b_indice, fatos=b_fatos, treino=b_treino,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
