"""Visual — Escalas, Plantas e Mapas, Episódio 4: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 3 ícones dos episódios (icone()): mapa com a tesoura nos 5 zeros · celular com zoom e
barra gráfica · maquete (caixa-d'água isométrica, n³).
Ícones das áreas nas questões (area_icone()): mapa rodoviário · semáforo · planta de lote · piscina · fotocópia.
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
_s = importlib.util.spec_from_file_location("comum026", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_escalas_ep4_revisao.mp4"
CARD_R = K.CARD_R
PAPEL = "#FBF7EC"
TERRA = "#E9E2C8"
AGUA = "#5FA8E8"
RUA = "#FFFFFF"
CUBO_TOPO, CUBO_FRENTE, CUBO_LADO = "#C9DEF8", "#9CC3F0", "#7AAAE0"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças
# ======================================================================

def tesoura(c, cx, cy, s, a, col=None):
    """tesoura aberta, lâminas para a direita"""
    if a <= 0:
        return
    col = col or RED
    c.save(); c.translate(cx, cy); c.scale(s, s)
    for sg in (-1, 1):
        c.drawCircle(-38, sg * 18, 15, paint(col, a, stroke=7))
        p = skia.Path(); p.moveTo(-26, sg * 10); p.lineTo(46, -sg * 16); p.lineTo(44, -sg * 8); p.lineTo(-20, sg * 4); p.close()
        c.drawPath(p, paint("#9AA4AE", a))
    c.drawCircle(-6, 0, 5, paint(INK, a))
    c.restore()


def mapa(c, x, y, w, h, a, estrada=True, cidades=True):
    """folha de mapa: terra, rio, estrada com duas cidades"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, TERRA, a, shadow=True)
    p = skia.Path(); p.moveTo(x + w * 0.62, y); p.cubicTo(x + w * 0.5, y + h * 0.35, x + w * 0.8, y + h * 0.6, x + w * 0.7, y + h)
    c.drawPath(p, paint(AGUA, a, stroke=max(3, w * 0.025)))
    if estrada:
        q = skia.Path(); q.moveTo(x + w * 0.15, y + h * 0.75); q.cubicTo(x + w * 0.35, y + h * 0.3, x + w * 0.6, y + h * 0.7,
                                                                       x + w * 0.85, y + h * 0.25)
        c.drawPath(q, paint(AMBER, a, stroke=max(3, w * 0.03)))
    if cidades:
        for (fx, fy) in ((0.15, 0.75), (0.85, 0.25)):
            c.drawCircle(x + w * fx, y + h * fy, max(5, w * 0.04), paint(RED, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), paint("#B8AE8A", a, stroke=2.5))


def celular(c, cx, cy, h, a, zoom=1.0):
    """celular com mapa de ruas na tela; zoom 1 = ruas largas (aproximado), 0 = só contorno"""
    if a <= 0:
        return
    w = h * 0.52
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, w * 0.14, INK, a, shadow=True)
    sx, sy, sw, sh = x + w * 0.07, y + h * 0.08, w * 0.86, h * 0.80
    rrect(c, sx, sy, sw, sh, 6, TERRA, a)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(sx, sy, sw, sh))
    passo = sw * (0.18 + 0.32 * zoom)
    lw = max(2, sw * 0.06 * zoom)
    k = 0
    while k * passo < sw + passo:
        line(c, sx + k * passo, sy, sx + k * passo, sy + sh, RUA, a, lw)
        line(c, sx, sy + k * passo, sx + sw, sy + k * passo, RUA, a, lw)
        k += 1
    c.restore()
    c.drawCircle(cx, y + h * 0.94, h * 0.025, paint("#FFFFFF", a * 0.7))


def barra_grafica(c, x, cy, w, a, rot="0     1,6 km", col=None):
    """barra graduada (escala gráfica) de largura w"""
    if a <= 0:
        return
    col = col or INK
    n = 4
    for i in range(n):
        rrect(c, x + i * w / n, cy - 7, w / n, 14, 0, col if i % 2 == 0 else "#FFFFFF", a)
    c.drawRect(skia.Rect.MakeXYWH(x, cy - 7, w, 14), paint(col, a, stroke=2))
    text(c, rot, x + w / 2, cy + 36, max(14, w * 0.11), "black", col, a)


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


def caixa(c, cx, cy, s, a, lx=1.0, ly=1.0, lz=1.0, div=0, topo=None, frente=None, lado=None):
    """caixa isométrica lx × ly × lz (em unidades s); div = grade nas faces visíveis"""
    if a <= 0:
        return
    P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
    _poly(c, [P(0, 0, lz), P(lx, 0, lz), P(lx, ly, lz), P(0, ly, lz)], topo or CUBO_TOPO, a, "#5E86B8")
    _poly(c, [P(lx, 0, lz), P(lx, ly, lz), P(lx, ly, 0), P(lx, 0, 0)], lado or CUBO_LADO, a, "#5E86B8")
    _poly(c, [P(0, ly, lz), P(lx, ly, lz), P(lx, ly, 0), P(0, ly, 0)], frente or CUBO_FRENTE, a, "#5E86B8")
    if div:
        pg = paint("#FFFFFF", a * 0.55, stroke=1.6)
        for k in range(1, div):
            f = k / div
            for (p0, p1) in ((P(f * lx, 0, lz), P(f * lx, ly, lz)), (P(0, f * ly, lz), P(lx, f * ly, lz)),
                             (P(lx, f * ly, lz), P(lx, f * ly, 0)), (P(lx, 0, f * lz), P(lx, ly, f * lz)),
                             (P(f * lx, ly, lz), P(f * lx, ly, 0)), (P(0, ly, f * lz), P(lx, ly, f * lz))):
                c.drawLine(p0[0], p0[1], p1[0], p1[1], pg)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 3 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 mapa com a tesoura nos 5 zeros
        mapa(c, -150, -120, 300, 170, a)
        text_mid(c, "1 : 500 000", -10, 100, 44, "black", INK, a)
        w = text_w("00 000", "black", 44)
        x1 = -10 + text_w("1 : 500 000", "black", 44) / 2
        line(c, x1 - w - 18, 118, x1 + 4, 84, RED, a, 5)
        tesoura(c, x1 + 62, 100, 0.6, a)
    elif k == 1:    # ep2 celular com zoom + barra gráfica
        celular(c, -70, -10, 240, a, 1.0)
        text_mid(c, "+", -70 + 62, -150, 40, "black", BLUE, a)
        celular(c, 80, 10, 170, a * 0.85, 0.0)
        barra_grafica(c, -10, 140, 150, a, "barra")
    elif k == 2:    # ep3 maquete (caixa-d'água) e o cubo
        caixa(c, -20, 30, 120, a, div=4)
        text(c, "n³", 120, -60, 64, "black", PURPLE, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones das questões: mapa rodoviário · semáforo · planta de lote · piscina · fotocópia"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # mapa rodoviário
        mapa(c, -100, -60, 200, 120, a)
    elif k == 1:    # semáforo
        rrect(c, -30, -75, 60, 150, 14, INK, a, shadow=True)
        for j, col in enumerate((RED, AMBER, GREEN)):
            c.drawCircle(0, -45 + j * 45, 16, paint(col, a))
    elif k == 2:    # planta de lote
        rrect(c, -100, -65, 200, 130, 6, "#FFFFFF", a, shadow=True)
        for i in range(1, 4):
            line(c, -100 + i * 50, -65, -100 + i * 50, 65, "#9CC3F0", a, 2)
        line(c, -100, 0, 100, 0, "#9CC3F0", a, 2)
        rrect(c, -50, -65, 50, 65, 0, mix("#FFFFFF", GREEN, 0.35), a)
        c.drawRect(skia.Rect.MakeXYWH(-100, -65, 200, 130), paint(INK, a, stroke=3))
    elif k == 3:    # piscina
        caixa(c, -10, -20, 34, a, lx=4.0, ly=2.0, lz=0.6, topo=mix("#FFFFFF", AGUA, 0.5))
    elif k == 4:    # fotocópia: folha pequena e folha ampliada
        mapa(c, -110, -10, 80, 56, a, cidades=False)
        arrow(c, -22, 18, 8, 18, INK2, a, 4, 12)
        mapa(c, 14, -60, 120, 112, a, cidades=False)
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
    if aa > 0:
        mapa(c, 760, 230, 400, 240, aa)
        text_mid(c, "1 : 250 000", 960, 520, 46, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    chip(c, "MATEMÁTICA", 560, 360, BLUE, ab, 40)
    chip(c, "GEOGRAFIA", 1360, 360, AMBER, ep(t, C["01.b"] + 0.4, 0.4), 40)
    ac = ep(t, C["01.c"], 0.5)
    text(c, "treino para as duas", W / 2, 640, 44, "black", GREEN, ac)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "8 FRASES V OU F", 760, 760, AMBER, ad, 36)
    chip(c, "5 QUESTÕES NOVAS", 1180, 760, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 36)


COBRA = [("02.a", "1", "A CADEIA DE CONVERSÃO", "cm → m → km", BLUE),
         ("02.b", "2", "A ESCALA DE ÁREA", "1 : n → 1 : n²", PURPLE),
         ("02.c", "3", "GRANDE × PEQUENA", "o nome parece invertido", AMBER)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "A CONTA É FÁCIL", "O QUE A PROVA COBRA", BLUE)
    a0 = ep(t, C["02"], 0.5) * (1 - ep(t, C["02.a"], 0.4))
    pill(c, "a conta da escala: uma multiplicação", W / 2, 470, GREEN, size=34, a=a0, anchor="center")
    for k, (cue, n, tit, sub, col) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 230 + d, 500, 530, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, n, x, 290 + d, a, 30, bg=col)
        if k == 0:
            for j, u in enumerate(("cm", "m", "km")):
                rrect(c, x - 200 + j * 140, 470 + d - j * 50, 120, 80 + j * 50, 10, mix("#FFFFFF", BLUE, 0.15 + 0.15 * j), a)
                text_mid(c, u, x - 140 + j * 140, 505 + d - j * 50, 34, "black", BLUE, a)
        elif k == 1:
            rrect(c, x - 150, 380 + d, 60, 60, 4, mix("#FFFFFF", PURPLE, 0.4), a)
            text_mid(c, "1 cm²", x - 120, 470 + d, 22, "black", INK2, a)
            arrow(c, x - 70, 410 + d, x - 20, 410 + d, INK2, a, 4, 12)
            for i in range(2):
                for j in range(2):
                    rrect(c, x + i * 70, 340 + d + j * 70, 66, 66, 4, mix("#FFFFFF", PURPLE, 0.25), a)
            text_mid(c, "4 m²", x + 68, 505 + d, 26, "black", PURPLE, a)
        else:
            celular(c, x - 90, 450 + d, 190, a, 1.0)
            celular(c, x + 90, 450 + d, 190, a, 0.0)
        text(c, tit, x, 640 + d, 30, "black", col, a)
        ftext(c, sub, x, 712 + d, 28, "bold", INK2, a)


INDICE = [("EP. 1", "foto encolhida · mapa → mundo: × · mundo → mapa: ÷ · corte 5 zeros"),
          ("EP. 2", "zoom aproximado = escala grande · denominador menor, escala maior · a barra viaja com o mapa"),
          ("EP. 3", "comprimento n · área n² · volume n³ · 1 : 100 = 1 cm é 1 m")]
IND_CUES = ["03.a", "04.a", "04.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 400 + k * 560
        y = 200
        rrect(c, x - 260, y, 520, 600, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 260, y, 520, 600), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 230, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 210, 0.9, a)
        lns = s.split(" · ")
        for j, ln in enumerate(lns):
            sz = 28
            while ftw(ln, sz) > 460:
                sz -= 1
            ftext(c, ln, x, y + 420 + j * 44, sz, "black", INK if on_ else INK2, a)


ONDE = [("05.a", "GEOGRAFIA", "cartas topográficas · curvas de nível"), ("05.b", "FÍSICA", "modelos reduzidos · lentes"),
        ("05.c", "ARQUITETURA", "plantas · urbanismo"), ("05.d", "MATEMÁTICA", "semelhança de figuras (série própria)")]


def onde_icone(c, k, cx, cy, a):
    if a <= 0:
        return
    if k == 0:      # curvas de nível
        for j in range(4):
            r = 90 - j * 22
            c.drawOval(skia.Rect.MakeXYWH(cx - r * 1.3, cy - r * 0.8, r * 2.6, r * 1.6), paint(mix("#8B6B3E", GREEN, j / 4), a, stroke=4))
    elif k == 1:    # lente
        p = skia.Path(); p.moveTo(cx, cy - 80); p.quadTo(cx + 40, cy, cx, cy + 80); p.quadTo(cx - 40, cy, cx, cy - 80); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", AGUA, 0.45), a)); c.drawPath(p, paint("#3E6FA8", a, stroke=3))
        arrow(c, cx - 110, cy - 30, cx - 6, cy - 30, AMBER, a, 4, 10)
        arrow(c, cx + 6, cy - 30, cx + 110, cy + 30, AMBER, a, 4, 10)
    elif k == 2:    # planta de casa
        area_icone(c, 2, cx, cy, 1.0, a)
    else:           # triângulos semelhantes
        for (ox, sc) in ((-70, 0.5), (40, 1.0)):
            p = skia.Path(); p.moveTo(cx + ox, cy + 60); p.lineTo(cx + ox + 110 * sc, cy + 60); p.lineTo(cx + ox, cy + 60 - 100 * sc)
            p.close()
            c.drawPath(p, paint(mix("#FFFFFF", PURPLE, 0.3), a)); c.drawPath(p, paint(PURPLE, a, stroke=3))


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ MATEMÁTICA", "ONDE A ESCALA APARECE", BLUE)
    for k, (cue, tit, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 230 + d, 380, 470, 24, mix("#F7F7F5", PURPLE if k == 3 else BLUE, 0.06), a)
        onde_icone(c, k, x, 380 + d, a)
        text(c, tit, x, 540 + d, 32, "black", PURPLE if k == 3 else BLUE, a)
        para(c, sub, x, 590 + d, 24, "bold", INK2, a, 320, 30, align="center")
    ad = ep(t, WT_or(C, "05", "lados", "05.d", 1.6), 0.5)
    if ad > 0:
        boxed(c, 330, 735, 1260, 80, PURPLE, ad, 0.08)
        text_mid(c, "lados: n  ·  áreas: n²  ·  volumes: n³", W / 2, 775, 34, "black", PURPLE, ad)


def WT_or(C, sid, palavra, cue, extra):
    """instante da palavra (tempos reais) ou, sem eles, o cue + extra"""
    try:
        return K.WT(C, sid, palavra)
    except Exception:
        return C[cue] + extra


HABITOS = [("06.a", "1", "TUDO EM CM", "antes de aplicar a escala"),
           ("06.b", "2", "QUAL PERGUNTA?", "real: × · desenho: ÷ · escala: razão"),
           ("06.c", "3", "FAZ SENTIDO?", "real do tamanho do mapa? · faltou um degrau")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 250 + d, 500, 480, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=GREEN)
        text(c, tit, x, 450 + d, 44, "black", GREEN, a)
        for j, ln in enumerate(sub.split(" · ")):
            ftext(c, ln, x, 540 + d + j * 46, 30, "bold", INK, a)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["07"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["07.a"], 0.5)
    for k in range(8):
        badge_num(c, k + 1, W / 2 - 3.5 * 90 + k * 90, 560, ep(t, C["07.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["07.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("mapa 1 : 100 000", "4 cm = 400 000 km", False, "a multiplicação está certa",
     "o resultado está em cm: corte 5 zeros", "400 000 cm = 4 km", 0),
    ("planta 1 : 50", "1 cm² = 50 cm²", False, "50 é o número da escala",
     "área tem dois lados: 50 × 50", "1 cm² = 2 500 cm²", 2),
    ("maquete 1 : 10", "volume real = 1 000 ×", True, "mil parece exagero",
     "três direções: 10 × 10 × 10", "10³ = 1 000", 2),
    ("grande × pequena", "1 : 50 000 > 1 : 250 000", True, "o número é menor",
     "fração: 1/2 > 1/20 · denominador menor, escala maior", "escala MAIOR", 1),
    ("2 cm valem 1 km", "escala 50 000 : 1", False, "100 000 ÷ 2 está certo",
     "escala é desenho sobre real", "1 : 50 000", 0),
    ("5 cm valem 10 km", "escala 1 : 2", False, "5/10 simplifica bonito",
     "padronize: 10 km = 1 000 000 cm", "1 : 200 000", 0),
    ("mapa ampliado", "a barra gráfica vale", True, "tudo mudou de tamanho",
     "a barra viaja com o mapa; o número, não", "barra ✓ · número ✗", 1),
    ("do real para o mapa", "multiplique pelo denominador", False, "a 1ª conta é ×",
     "do mundo para o mapa, o número encolhe", "divida", 0),
]
VF_IDS = [f"{8 + k:02d}" for k in range(8)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 8", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(8):
        badge_num(c, k + 1, W / 2 - 3.5 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 420, 0.6, a0)
    text(c, ctx.upper(), 960, 310, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 60
    while ftw(conta, sz) > 680:
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
        ftext(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = regra_.split(" · ")
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 705 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        szf = 44
        while ftw(fix, szf) > 560:
            szf -= 2
        fmid(c, fix, 1390, 715, szf, "black", GREEN, ag)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["16.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["16.a"] + 0.12 * k, 0.3)
        x = W / 2 - 3.5 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "5 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["16.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    text(c, "a unidade ao lado de cada número", W / 2, 740, 32, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: qual pergunta / ideia · passos: (cue, texto) · confere: (cue, texto)

Q = {
    "q1": dict(ids=("17", "18"), titulo="O MAPA RODOVIÁRIO", area="GEOGRAFIA", ic=0, ok="C",
               enun=[("a", "Num mapa rodoviário de escala 1 : 2 000 000, duas cidades estão a 7,5 cm.", False),
                     ("b", "A distância real, em quilômetros, é", True)],
               alts=[("A", "15", "cortou 6 zeros", AMBER), ("B", "1 500", "cortou só 4 zeros", AMBER),
                     ("C", "150", "", GREEN), ("D", "15 000", "pulou o degrau do metro", RED),
                     ("E", "150 000", "parou nos metros", RED)],
               pad="medida real: multiplique", passos=[("a", "7,5 cm × 2 000 000 = 15 000 000 cm"),
                                                       ("b", "÷ 100 000 → 150 km")],
               confere=("v", "atalho: 20 km/cm × 7,5 = 150 km")),
    "q2": dict(ids=("19", "20"), titulo="FAIXAS E SEMÁFOROS", area="PLANEJAMENTO URBANO", ic=1, ok="A",
               enun=[("a", "Uma prefeitura vai decidir onde pintar faixas de pedestres e instalar semáforos nos "
                           "cruzamentos do centro.", False),
                     ("b", "O mapa mais adequado tem escala", True)],
               alts=[("A", "1 : 2 000", "", GREEN), ("B", "1 : 20 000", "1 cm = 200 m", AMBER),
                     ("C", "1 : 200 000", "1 cm = 2 km", AMBER), ("D", "1 : 2 000 000", "1 cm = 20 km", AMBER),
                     ("E", "1 : 20 000 000", "denominador maior ≠ maior", RED)],
               pad="detalhe = zoom aproximado", passos=[("a", "mais detalhe = escala maior"),
                                                        ("b", "escala maior = menor denominador")],
               confere=("v", "1 : 2 000 → 1 cm = 20 m")),
    "q3": dict(ids=("21", "22"), titulo="O LOTE NA PLANTA", area="MATEMÁTICA", ic=2, ok="E",
               enun=[("a", "Na planta de um loteamento, na escala 1 : 500, um lote retangular mede 4 cm por 6 cm.", False),
                     ("b", "A área real do lote, em m², é", True)],
               alts=[("A", "1,2", "fator linear na área", RED), ("B", "120", "converteu um lado só", AMBER),
                     ("C", "60 000", "1 m² = 100 cm²?", AMBER), ("D", "6 000 000", "parou nos cm²", RED),
                     ("E", "600", "", GREEN)],
               pad="converta os lados primeiro", passos=[("a", "4 × 500 = 2 000 cm = 20 m · 6 × 500 = 30 m"),
                                                         ("b", "20 m × 30 m = 600 m²")],
               confere=("v", "lote de 20 m × 30 m: comum")),
    "q4": dict(ids=("23", "24"), titulo="A MAQUETE DA PISCINA", area="MAQUETE", ic=3, ok="B",
               enun=[("a", "Uma maquete de uma piscina, na escala 1 : 25, comporta 3,2 litros.", False),
                     ("b", "A piscina real comporta", True)],
               alts=[("A", "80 litros", "fator linear", RED), ("B", "50 000 litros", "", GREEN),
                     ("C", "2 000 litros", "fator de área", RED), ("D", "15 625 litros", "esqueceu os 3,2 L", AMBER),
                     ("E", "50 litros", "50 m³ não é 50 L", AMBER)],
               pad="volume: três direções → n³", passos=[("a", "25 × 25 × 25 = 15 625"),
                                                         ("b", "3,2 L × 15 625 = 50 000 L = 50 m³")],
               confere=("v", "10 m × 5 m × 1 m = 50 m³")),
    "q5": dict(ids=("25", "26"), titulo="O MAPA AMPLIADO", area="GEOGRAFIA", ic=4, ok="D",
               enun=[("a", "Um mapa 1 : 80 000 tem uma barra gráfica de 2 cm que vale 1,6 km. Ele foi ampliado ao "
                           "dobro numa fotocópia.", False),
                     ("b", "Na cópia,", True)],
               alts=[("A", "a numérica vale: 1 : 80 000", "confiou no número", RED),
                     ("B", "a barra vale; nova: 1 : 160 000", "multiplicou", AMBER),
                     ("C", "a barra não vale; nova: 1 : 40 000", "a barra cresce junto", RED),
                     ("D", "a barra vale; nova: 1 : 40 000", "", GREEN),
                     ("E", "a barra vale; nova: 1 : 20 000", "dobro ao quadrado", AMBER)],
               pad="a barra viaja com o mapa", passos=[("a", "barra: 4 cm = 1,6 km = 160 000 cm"),
                                                       ("b", "4 / 160 000 = 1 / 40 000")],
               confere=None),
}


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None):
    """para() que não quebra linha dentro de "1 : 2 000 000" nem entre número e unidade (espaço rígido)"""
    import re
    s = re.sub(r"(?<=\d) (?=\d{3})", " ", s)
    s = s.replace("1 : ", "1 : ")
    s = re.sub(r"(?<=\d) (?=(cm|km|m|litros)\b)", " ", s)
    lh = lh or size * 1.32
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and text_w(tst, peso, size) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    if a > 0:
        for k, ln in enumerate(out):
            text(c, ln, x, y + k * lh, size, peso, color, a, align="left")
    return len(out) * lh


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
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 32 if num == 5 else 34, C[f"{s2}.ok"], d["ok"], cues_in,
                       cues_x, gap=14)
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 170, 260, 650, 84, PURPLE, ad, 0.08)
                pill(c, "PENSE", 190, 260, PURPLE, size=18, a=ad, bounds=(0, 1920))
                ftext(c, d["pad"], 190, 316, 30, "black", INK, ad, align="left")
            yy = 420
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                for ln in s.split(" · "):
                    sz = 36
                    while ftw(ln, sz) > 640:
                        sz -= 2
                    ftext(c, ln, 180, yy, sz, "black", GREEN if last else INK, a, align="left")
                    yy += 60
                yy += 6
            if d["confere"]:
                cue, s = d["confere"]
                sz = 30
                while ftw(s, sz) > 580:
                    sz -= 2
                conferido(c, s, 190, yy + 10, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, sz)
            result_box(c, f"Letra {d['ok']}", 1290, 720 if num == 5 else 690, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("27.b", "EP. 1", ["escala = desenho ÷ real", "ler 1 : 250 000", "cm → m → km sem pular",
                            "atalho: n ÷ 100 000 km", "os três cálculos", "conferir se faz sentido"]),
         ("28.a", "EP. 2", ["denominador menor, escala maior", "barra gráfica → numérica", "a barra sobrevive à cópia"]),
         ("28.b", "EP. 3", ["área n² · volume n³", "lados antes da área", "maquete com o cubo", "1 : 100 = 1 cm é 1 m"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["27.a"], 0.5) * (1 - ep(t, C["27.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 1 else 1
        x = 170 if col_ == 0 else 990
        y0 = 200 + (0 if k < 2 else len(CHECK[1][2]) * 46 + 40)
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x + 40, y0 + 120, 0.28, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 46
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            K.ftext(c, it, x + 158, yy + 10, 27, "bold", INK, a, align="left")
    ae = ep(t, C["28.c"], 0.5)
    if ae > 0:
        boxed(c, 170, 690, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 530, 740, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["29.a"], 0.5)
    ab = ep(t, C["29.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["29.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 230 + k * 82, 220 + r_ * 86
        rrect(c, x, y, 66, 70, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    ac = ep(t, C["29.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 560, 1460, 200, AMBER, ac, 0.10)
        onde_icone(c, 0, 420, 660, ac * 0.9)
        text_mid(c, "inclua GEOGRAFIA", W / 2 + 80, 638, 40, "black", INK, ac)
        text_mid(c, "cartas topográficas · curvas de nível", W / 2 + 80, 694, 30, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Velocidade, densidade e vazão", W / 2, 330, 62, "black", PURPLE, aa)
    for k, s in enumerate(("km/h", "g/cm³", "L/min")):
        chip(c, s, 640 + k * 320, 450, BLUE, aa * ep(t, C["30.a"] + 0.6 + 0.3 * k, 0.4), 34)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        boxed(c, 440, 560, 1040, 200, GREEN, ab, 0.08)
        text(c, "fecha o bloco de", W / 2, 640, 34, "black", INK, ab)
        text(c, "PROPORCIONALIDADE", W / 2, 700, 44, "black", GREEN, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
