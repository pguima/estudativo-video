"""Visual — Velocidade, Densidade e Vazão, Episódio 6: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, fr, alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): unidade com barra virando fração · relógio de 60 em 60 ·
balança de tempos 2 h × 3 h · cubinhos no aquário · tanque fatiado.
Ícones das áreas nas questões (area_icone()): velocímetro · estrada de ida e volta · balança · torneira · mapa.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
import re
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
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_velocidade_densidade_vazao_ep6_revisao.mp4"
CARD_R = K.CARD_R
AGUA = "#5FA8E8"
AGUA_CLARA = "#CFE5FA"
TERRA = "#E9E2C8"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def fit(s, size, maxw, peso="black"):
    while ftw(s, size, peso) > maxw and size > 14:
        size -= 1
    return size


# ======================================================================
# peças
# ======================================================================

def relogio(c, cx, cy, r, a, ponteiro=0.5):
    """relógio com 12 marcas; ponteiro em fração da volta (0,5 = meia hora)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=max(3, r * 0.07)))
    ang = -math.pi / 2 + 2 * math.pi * ponteiro
    p = skia.Path(); p.moveTo(cx, cy); p.lineTo(cx, cy - r * 0.86)
    p.arcTo(skia.Rect.MakeXYWH(cx - r * 0.86, cy - r * 0.86, r * 1.72, r * 1.72), -90, 360 * ponteiro, False); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", AMBER, 0.45), a))
    for k in range(12):
        an = 2 * math.pi * k / 12
        r0 = r * (0.78 if k % 3 else 0.70)
        line(c, cx + r0 * math.cos(an), cy + r0 * math.sin(an), cx + r * 0.9 * math.cos(an), cy + r * 0.9 * math.sin(an),
             INK, a, max(2, r * 0.04))
    line(c, cx, cy, cx + r * 0.75 * math.cos(ang), cy + r * 0.75 * math.sin(ang), RED, a, max(3, r * 0.07))
    line(c, cx, cy, cx, cy - r * 0.5, INK, a, max(3, r * 0.08))
    c.drawCircle(cx, cy, r * 0.07, paint(INK, a))


def balanca(c, cx, cy, s, a, esq="2 h", dir_="3 h"):
    """balança de pratos inclinada para o lado mais pesado (direita)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    rrect(c, -10, -60, 20, 150, 6, INK2, a)
    rrect(c, -70, 86, 140, 18, 8, INK2, a)
    tilt = 0.18
    x0, x1, y1 = -140, 140, -60 + 140 * tilt
    y0 = -60 - 140 * tilt
    line(c, x0, y0, x1, y1, INK, a, 8)
    for (x, y, rot, w) in ((x0, y0, esq, 100), (x1, y1, dir_, 150)):
        line(c, x, y, x - 50, y + 70, GRAY, a, 3); line(c, x, y, x + 50, y + 70, GRAY, a, 3)
        rrect(c, x - 60, y + 70, 120, 12, 6, INK2, a)
        rrect(c, x - w / 2 + 0, y + 70 - 46, w, 44, 8, mix("#FFFFFF", AMBER, 0.5), a)
        text_mid(c, rot, x, y + 70 - 24, 30, "black", INK, a)
    c.restore()


def aquario(c, cx, cy, s, a, cheio=1.0):
    """aquário com cubinhos (1 cm³) empilhados dentro"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    rrect(c, -130, -90 + 180 * (1 - cheio), 260, 180 * cheio, 8, mix("#FFFFFF", AGUA, 0.35), a)
    for i in range(5):
        for j in range(3):
            rrect(c, -110 + i * 44, 40 - j * 44, 40, 40, 4, mix("#FFFFFF", BLUE, 0.35 + 0.1 * ((i + j) % 2)), a)
    c.drawRect(skia.Rect.MakeXYWH(-130, -90, 260, 180), paint(INK, a, stroke=5))
    c.restore()


def tanque(c, cx, cy, s, a, fatias=4, cheio=0.5, col=None):
    """tanque cilíndrico de frente, dividido em fatias horizontais"""
    if a <= 0:
        return
    col = col or AGUA
    c.save(); c.translate(cx, cy); c.scale(s, s)
    w, h = 200, 240
    rrect(c, -w / 2, -h / 2, w, h, 18, "#FFFFFF", a)
    hh = h * cheio
    rrect(c, -w / 2, h / 2 - hh, w, hh, 14, mix("#FFFFFF", col, 0.55), a)
    for k in range(1, fatias):
        y = -h / 2 + h * k / fatias
        line(c, -w / 2, y, w / 2, y, INK2, a, 3)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 18, 18), paint(INK, a, stroke=5))
    c.restore()


def torneira(c, x, y, s, a, col=None):
    """torneira de parede com bico para baixo, em (x, y) = saída do bico"""
    if a <= 0:
        return
    col = col or INK2
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -90, -70, 90, 26, 10, col, a)
    rrect(c, -18, -70, 26, 70, 8, col, a)
    rrect(c, -62, -100, 40, 34, 8, col, a)
    line(c, -42, -100, -42, -112, col, a, 8)
    c.restore()


def velocimetro(c, cx, cy, r, a, frac=0.6):
    if a <= 0:
        return
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, 180)
    c.drawPath(p, paint(INK, a, stroke=max(4, r * 0.12)))
    for k in range(7):
        an = math.pi + math.pi * k / 6
        line(c, cx + r * 0.72 * math.cos(an), cy + r * 0.72 * math.sin(an), cx + r * 0.88 * math.cos(an),
             cy + r * 0.88 * math.sin(an), INK2, a, 3)
    an = math.pi + math.pi * frac
    line(c, cx, cy, cx + r * 0.8 * math.cos(an), cy + r * 0.8 * math.sin(an), RED, a, max(4, r * 0.08))
    c.drawCircle(cx, cy, r * 0.1, paint(INK, a))


def mapa(c, x, y, w, h, a):
    rrect(c, x, y, w, h, 10, TERRA, a, shadow=True)
    p = skia.Path(); p.moveTo(x + w * 0.2, y + h * 0.15); p.lineTo(x + w * 0.55, y + h * 0.1); p.lineTo(x + w * 0.5, y + h * 0.55)
    p.lineTo(x + w * 0.15, y + h * 0.6); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", GREEN, 0.4), a)); c.drawPath(p, paint(INK2, a, stroke=2))
    q = skia.Path(); q.moveTo(x + w * 0.55, y + h * 0.1); q.lineTo(x + w * 0.85, y + h * 0.3); q.lineTo(x + w * 0.8, y + h * 0.85)
    q.lineTo(x + w * 0.45, y + h * 0.9); q.lineTo(x + w * 0.5, y + h * 0.55); q.close()
    c.drawPath(q, paint(mix("#FFFFFF", AMBER, 0.45), a)); c.drawPath(q, paint(INK2, a, stroke=2))
    text_mid(c, "X", x + w * 0.36, y + h * 0.36, max(14, h * 0.16), "black", INK, a)
    text_mid(c, "Y", x + w * 0.66, y + h * 0.55, max(14, h * 0.16), "black", INK, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 a unidade com barra virando fração
        text_mid(c, "km/h", -70, -40, 54, "black", INK, a)
        arrow(c, 10, -40, 60, -40, INK2, a, 5, 14)
        K.fr(c, "km", "h", 120, -40, 46, PURPLE, a)
        text_mid(c, "÷", 0, 70, 70, "black", PURPLE, a)
    elif k == 1:    # ep2 relógio de 60 em 60
        relogio(c, 0, -10, 95, a, 0.5)
        text_mid(c, "30 min = 0,5 h", 0, 120, 30, "black", AMBER, a)
    elif k == 2:    # ep3 balança de tempos 2 h × 3 h
        balanca(c, 0, 0, 0.75, a)
    elif k == 3:    # ep4 cubinhos no aquário
        aquario(c, 0, 0, 0.75, a)
    elif k == 4:    # ep5 tanque fatiado
        tanque(c, 0, 0, 0.62, a, 4, 0.5)
        torneira(c, -40, -80, 0.55, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones das questões: velocímetro · ida e volta · balança · torneira · mapa"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:
        velocimetro(c, 0, 30, 90, a, 0.55)
    elif k == 1:
        arrow(c, -110, -20, 110, -20, GREEN, a, 7, 22)
        arrow(c, 110, 30, -110, 30, AMBER, a, 7, 22)
        text_mid(c, "90", 0, -54, 30, "black", GREEN, a)
        text_mid(c, "60", 0, 66, 30, "black", AMBER, a)
    elif k == 2:
        aquario(c, 0, 0, 0.55, a, 0.75)
    elif k == 3:
        tanque(c, 0, 10, 0.5, a, 4, 0.5)
        torneira(c, -30, -60, 0.45, a)
    elif k == 4:
        mapa(c, -110, -70, 220, 150, a)
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def WT_or(C, sid, palavra, cue, extra):
    """instante da palavra (tempos reais) ou, sem eles, o cue + extra"""
    try:
        return K.WT(C, sid, palavra)
    except Exception:
        return C[cue] + extra


# ======================================================================
# abertura
# ======================================================================

GANCHO = [("01.a", "VELOCIDADE MÉDIA", "FÍSICA", 0), ("01.b", "DENSIDADE", "QUÍMICA", 3),
          ("01.c", "DENSIDADE DEMOGRÁFICA", "GEOGRAFIA", 5)]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    junta = ep(t, C["01.e"], 0.8)
    for k, (cue, tit, area, ic) in enumerate(GANCHO):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 220 + d, 480, 360, 24, mix("#F7F7F5", BLUE, 0.08), a)
        if ic == 0:
            velocimetro(c, x, 380 + d, 90, a)
        elif ic == 3:
            aquario(c, x, 350 + d, 0.6, a)
        else:
            mapa(c, x - 110, 290 + d, 220, 130, a)
        pill(c, area, x, 245 + d, INK2, size=20, a=a, anchor="center")
        sz = fit(tit, 32, 440)
        text(c, tit, x, 520 + d, sz, "black", BLUE, a)
    ad = ep(t, C["01.d"], 0.5) * (1 - junta)
    text(c, "3 questões diferentes?", W / 2, 680, 46, "black", INK2, ad)
    if junta > 0:
        boxed(c, 460, 620, 1000, 110, PURPLE, junta, 0.10)
        K.fr(c, "quanto", "por unidade", 760, 675, 34, PURPLE, junta)
        text_mid(c, "uma só ideia", 1180, 675, 44, "black", PURPLE, junta)
    af = ep(t, C["01.f"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 800, AMBER, af, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 800, GREEN, ep(t, C["01.f"] + 0.5, 0.4), 34)


COBRA = [("02.a", "1", "VELOCIDADE MÉDIA", "trechos diferentes · a armadilha", BLUE, 0),
         ("02.b", "2", "DENSIDADE", "material · boia? · g/cm³ ↔ kg/m³", BLUE, 3),
         ("02.c", "3", "VAZÃO", "torneira + · ralo −", BLUE, 4),
         ("02.d", "4", "OUTRAS TAXAS", "km/L · g/L · hab/km²", PURPLE, -1)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "SEÇÃO 01", "O QUE A PROVA COBRA", BLUE)
    for k, (cue, n, tit, sub, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 440
        rrect(c, x - 200, 220 + d, 400, 560, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, n, x, 280 + d, a, 30, bg=col)
        if ic >= 0:
            icone(c, ic, x, 450 + d, 0.8, a)
        else:
            for j, u in enumerate(("km/L", "g/L", "hab/km²")):
                chip(c, u, x, 380 + d + j * 70, PURPLE, a, 30)
        text(c, tit, x, 640 + d, fit(tit, 32, 370), "black", col, a)
        for j, ln in enumerate(sub.split(" · ")):
            ftext(c, ln, x, 700 + d + j * 38, fit(ln, 26, 370, "bold"), "bold", INK2, a)


INDICE = [("EP. 1", "a barra é ÷ · preço do quilo"), ("EP. 2", "ritmo constante · cronômetro não para · 60 em 60"),
          ("EP. 3", "quem manda é o relógio · distância amiga"), ("EP. 4", "impressão digital · a água é a régua"),
          ("EP. 5", "pedaços do tanque · time e sabotador")]
IND_CUES = ["03.a", "03.b", "04.a", "04.b", "04.c"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 232 + k * 364
        y = 200
        rrect(c, x - 170, y, 340, 610, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 170, y, 340, 610), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=20, a=a, anchor="center")
        icone(c, k, x, y + 220, 0.78, a)
        for j, ln in enumerate(s.split(" · ")):
            ftext(c, ln, x, y + 430 + j * 48, fit(ln, 28, 310), "black", INK if on_ else INK2, a)


ONDE = [("05.a", "FÍSICA", "cinemática · hidrostática · vazão em canos"),
        ("05.b", "QUÍMICA", "densidade de soluções · concentração g/L"),
        ("05.c", "BIOLOGIA", "natalidade · mortalidade"),
        ("05.d", "GEOGRAFIA", "densidade demográfica · vazão de rios · produtividade")]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ MATEMÁTICA", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 220 + d, 380, 450, 24, mix("#F7F7F5", BLUE, 0.06), a)
        if k == 0:
            velocimetro(c, x, 380 + d, 80, a)
        elif k == 1:
            aquario(c, x, 340 + d, 0.5, a, 0.8)
        elif k == 2:
            for j in range(5):
                c.drawCircle(x - 80 + j * 40, 350 + d - j * 12, 16, paint(mix("#FFFFFF", GREEN, 0.3 + 0.12 * j), a))
            arrow(c, x - 100, 400 + d, x + 100, 340 + d, GREEN, a, 4, 12)
        else:
            mapa(c, x - 110, 280 + d, 220, 130, a)
        text(c, tit, x, 500 + d, 32, "black", BLUE, a)
        for j, ln in enumerate(sub.split(" · ")):
            ftext(c, ln, x, 556 + d + j * 36, fit(ln, 24, 350, "bold"), "bold", INK2, a)
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        boxed(c, 330, 715, 1260, 90, PURPLE, ae, 0.08)
        text_mid(c, "o mesmo conteúdo com outra roupa", W / 2, 760, 38, "black", PURPLE, ae)


HABITOS = [("06.a", "1", "UNIDADE AO LADO", "a barra já diz a conta"),
           ("06.b", "2", "PADRONIZE", "L/min com horas? · converta antes"),
           ("06.c", "3", "MUNDO REAL", "carro a 500 km/h? · caixa de 5 000 L?")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 250 + d, 500, 480, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=GREEN)
        text(c, tit, x, 450 + d, fit(tit, 44, 460), "black", GREEN, a)
        for j, ln in enumerate(sub.split(" · ")):
            ftext(c, ln, x, 540 + d + j * 46, fit(ln, 30, 460, "bold"), "bold", INK, a)


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
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["07.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["07.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("ida 60 · volta 40", "média = 50 km/h", False, "50 é a média dos números",
     "distância total ÷ tempo total", "48 km/h", 2),
    ("viagem com parada", "a parada entra no tempo", True, "parado, o carro não anda",
     "o cronômetro não para no posto", "todo o tempo conta", 1),
    ("o relógio", "2,5 h = 2 h 50 min", False, "o 5 parece virar 50",
     "o relógio conta de 60 em 60", "2 h 30 min", 1),
    ("20 m/s × 60 km/h", "20 m/s é mais devagar", False, "20 é menor que 60",
     "20 m/s × 3,6 = 72 km/h", "72 km/h > 60 km/h", 0),
    ("densidade", "0,9 g/cm³ = 900 kg/m³", True, "os números são muito diferentes",
     "g/cm³ → kg/m³: × 1 000", "0,9 × 1 000 = 900", 3),
    ("torneira 4 h · ralo 6 h", "1/4 + 1/6 por hora", False, "em torneiras, a gente soma",
     "o ralo é sabotador: subtraia", "1/4 − 1/6 = 1/12 → 12 h", 4),
    ("torneiras de 2 h e 3 h", "juntas: 5 h", False, "somar parece juntar",
     "some os pedaços, não os tempos", "1/2 + 1/3 = 5/6 → 1 h 12 min", 4),
    ("20 L/min · 600 L", "enche em 30 horas", False, "600 ÷ 20 dá mesmo 30",
     "a vazão é por minuto: padronize", "30 minutos", 4),
    ("prego × portão de ferro", "a mesma densidade", True, "o portão é mais pesado",
     "mais massa, mais volume: impressão digital", "7,8 g/cm³ nos dois", 3),
]
VF_IDS = [f"{8 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 420, 0.6, a0)
    text(c, ctx.upper(), 960, 310, fit(ctx.upper(), 30, 640), "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = fit(conta, 60, 680)
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
        ftext(c, regra_, 240, 715, fit(regra_, 32, 760), "black", GREEN, ag, align="left")
        fmid(c, fix, 1350, 715, fit(fix, 44, 620), "black", GREEN, ag)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["17.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["17.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["17.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    text(c, "a unidade ao lado de cada número", W / 2, 740, 32, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: a ideia · passos: (cue, texto) · confere: (cue, texto)

Q = {
    "q1": dict(ids=("18", "19"), titulo="A VIAGEM COM PARADA", area="FÍSICA", ic=0, ok="B",
               enun=[("a", "Um carro anda 70 km em 1 h, para 30 min num posto e anda mais 50 km em 30 min.", False),
                     ("b", "A velocidade média no percurso completo, em km/h, é", True)],
               alts=[("A", "85", "média das velocidades", AMBER), ("B", "60", "", GREEN),
                     ("C", "80", "esqueceu a parada", RED), ("D", "75", "30 min = 0,3 h?", RED),
                     ("E", "70", "só o 1º trecho", AMBER)],
               pad="distância total ÷ tempo total",
               passos=[("a", "70 km + 50 km = 120 km"), ("b", "1 h + 0,5 h + 0,5 h = 2 h"), ("c", "120 km ÷ 2 h = 60 km/h")],
               confere=None),
    "q2": dict(ids=("20", "21"), titulo="IDA E VOLTA", area="MATEMÁTICA", ic=1, ok="D",
               enun=[("a", "Um ônibus vai de uma cidade a outra, a 180 km, a 90 km/h, e volta pelo mesmo caminho a 60 km/h.",
                      False),
                     ("b", "A velocidade média na ida e volta, em km/h, é", True)],
               alts=[("A", "36", "esqueceu a volta", RED), ("B", "75", "média simples", AMBER),
                     ("C", "150", "somou as velocidades", RED), ("D", "72", "", GREEN),
                     ("E", "60", "o lento manda sozinho?", AMBER)],
               pad="quem manda é o relógio",
               passos=[("a", "ida: 180 km ÷ 90 km/h = 2 h · volta: 180 km ÷ 60 km/h = 3 h"),
                       ("b", "360 km ÷ 5 h = 72 km/h")],
               confere=("v", "72 < 75: puxou para a menor")),
    "q3": dict(ids=("22", "23"), titulo="BOIA OU AFUNDA?", area="QUÍMICA", ic=2, ok="A",
               enun=[("a", "Um bloco maciço tem massa de 600 g e volume de 750 cm³.", False),
                     ("b", "Na água, o bloco e a sua densidade são", True)],
               alts=[("A", "boia · 800 kg/m³", "", GREEN), ("B", "boia · 0,8 kg/m³", "esqueceu o × 1 000", RED),
                     ("C", "afunda · 1 250 kg/m³", "dividiu ao contrário", RED),
                     ("D", "afunda · 800 kg/m³", "800 contra 1? unidades!", AMBER),
                     ("E", "boia · 80 kg/m³", "usou × 100", RED)],
               pad="densidade = massa ÷ volume",
               passos=[("a", "600 g ÷ 750 cm³ = 0,8 g/cm³"), ("b", "0,8 < 1: boia · 0,8 × 1 000 = 800 kg/m³")],
               confere=None),
    "q4": dict(ids=("24", "25"), titulo="TORNEIRA E RALO", area="VAZÃO", ic=3, ok="E",
               enun=[("a", "Uma torneira enche um tanque em 3 h. O ralo, sozinho, esvazia o tanque cheio em 12 h.", False),
                     ("b", "Com o tanque vazio e os dois abertos, ele enche em", True)],
               alts=[("A", "2 h 24 min", "somou o ralo", RED), ("B", "2 h 40 min", "somou e leu 2,4 h errado", RED),
                     ("C", "9 h", "subtraiu os tempos", AMBER), ("D", "15 h", "somou os tempos", AMBER),
                     ("E", "4 h", "", GREEN)],
               pad="pedaços do tanque por hora",
               passos=[("a", "torneira: + 1/3 · ralo: − 1/12"), ("b", "4/12 − 1/12 = 3/12 = 1/4 → 4 h")],
               confere=("v", "4 h > 3 h: o sabotador atrasou")),
    "q5": dict(ids=("26", "27"), titulo="QUAL É MAIS DENSO?", area="GEOGRAFIA", ic=4, ok="C",
               enun=[("a", "X: 240 000 hab em 600 km². Y: 90 000 hab em 15 000 ha (1 km² = 100 ha).", False),
                     ("b", "A maior densidade demográfica é a de", True)],
               alts=[("A", "X: 400 contra 6", "não converteu o ha", RED), ("B", "X: tem mais habitantes", "comparou o total", RED),
                     ("C", "Y: 600 hab/km²", "", GREEN), ("D", "Y: 60 000 hab/km²", "hectare como m²", AMBER),
                     ("E", "X: 2 500 m² por hab", "inverteu a razão", AMBER)],
               pad="compare pela taxa, não pelo total",
               passos=[("a", "X: 240 000 hab ÷ 600 km² = 400 hab/km²"),
                       ("b", "Y: 15 000 ha = 150 km² · 90 000 ÷ 150 = 600 hab/km²")],
               confere=None),
}


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None):
    """para() que não quebra linha dentro de "240 000" nem entre número e unidade (espaço rígido)"""
    s = re.sub(r"(?<=\d) (?=\d{3})", " ", s)
    s = re.sub(r"(?<=\d) (?=(cm³|km²|km/h|km|min|ha|hab|g|h)\b)", " ", s)
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
        area_icone(c, d["ic"], 760, 230, 0.45, a0 * (1 - sol))
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 32, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 170, 260, 650, 84, PURPLE, ad, 0.08)
                pill(c, "PENSE", 190, 260, PURPLE, size=18, a=ad, bounds=(0, 1920))
                ftext(c, d["pad"], 190, 316, fit(d["pad"], 30, 610), "black", INK, ad, align="left")
            yy = 410
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                for ln in s.split(" · "):
                    ftext(c, ln, 180, yy, fit(ln, 34, 640), "black", GREEN if last else INK, a, align="left")
                    yy += 56
                yy += 6
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, s, 190, yy + 10, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, fit(s, 30, 580))
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("28.b", "EP. 1", ["mesma estrutura de razão", "a unidade decide × ou ÷", "valores de referência"]),
         ("28.c", "EP. 2", ["distância total ÷ tempo total", "a parada entra no tempo"]),
         ("28.d", "EP. 3", ["ida e volta ≠ média", "puxa para a menor"]),
         ("29.a", "EP. 4", ["flutuação: a água é a régua", "g/cm³ → kg/m³: × 1 000", "não depende da quantidade"]),
         ("29.b", "EP. 5", ["pedaços do tanque por hora", "ralo subtrai: o tempo aumenta", "minutos com horas: padronize"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["28.a"], 0.5) * (1 - ep(t, C["28.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    ys = {0: 205, 1: 205 + 3 * 44 + 40, 2: 205 + 5 * 44 + 80, 3: 205, 4: 205 + 3 * 44 + 40}
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 150 if k < 3 else 990
        y0 = ys[k]
        pill(c, ep_, x, y0 + 14, PURPLE, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 14 + j * 44
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            K.ftext(c, it, x + 158, yy + 10, fit(it, 27, 640, "bold"), "bold", INK, a, align="left")
    ae = ep(t, C["29.c"], 0.5)
    if ae > 0:
        boxed(c, 990, 640, 760, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1370, 690, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["30.a"], 0.5)
    ab = ep(t, C["30.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["30.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 230 + k * 82, 220 + r_ * 86
        rrect(c, x, y, 66, 70, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    ac = ep(t, C["30.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 560, 1460, 200, AMBER, ac, 0.10)
        velocimetro(c, 400, 690, 70, ac)
        aquario(c, 570, 660, 0.4, ac, 0.8)
        text_mid(c, "inclua FÍSICA", W / 2 + 160, 638, 40, "black", INK, ac)
        text_mid(c, "cinemática · hidrostática", W / 2 + 160, 694, 30, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "FIM DO BLOCO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    text(c, "MATEMÁTICA BÁSICA E PROPORCIONALIDADE", W / 2, 240, 40, "black", PURPLE, aa)
    for k in range(12):
        a = aa * ep(t, C["31.a"] + 0.4 + 0.08 * k, 0.3)
        x = W / 2 - 5.5 * 110 + k * 110
        badge_num(c, k + 1, x, 330, a, 26, bg=GREEN)
        check_icon(c, x + 26, 304, 12, a, GREEN)
    ab = ep(t, C["31.b"], 0.5)
    pill(c, "revise misturando os 12 temas", W / 2, 440, AMBER, size=32, a=ab, anchor="center")
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        boxed(c, 440, 540, 1040, 230, BLUE, ac, 0.08)
        text(c, "PRÓXIMO ASSUNTO", W / 2, 600, 26, "black", GRAY, ac, tracking=2)
        text(c, "Juros simples", W / 2, 680, 62, "black", BLUE, ac)
        text(c, "abre a Matemática Financeira", W / 2, 740, 30, "bold", INK2, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
