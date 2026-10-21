"""Visual — Matéria, Substâncias e Misturas, Episódio 4: Fases e componentes (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Reaproveita peças do ep. 1 (V) e do ep. 3 (V3: caixa de gases, granito).
Peças próprias deste episódio:
- Recipientes em corte lateral (copo, pote, béquer) com camadas; cada fase ganha um contorno numerado.
  Os três cubos de gelo ganham o MESMO número.
- colunas(): FOTO (fases, de cima para baixo) e RECEITA (componentes), preenchidas no ritmo da narração.
- tabela(): os exemplos (sistema · fases · componentes) se acumulando ao longo dos blocos.
"""
import importlib.util
import json
import math
import random
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_BASE = Path(__file__).resolve().parents[2]


def _load(nome, rel):
    spec = importlib.util.spec_from_file_location(nome, _BASE / rel / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


V = _load("visual_quimica_ep1", "ep1_materia_e_substancias")
V3 = _load("visual_quimica_ep3", "ep3_misturas")

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_ep4_fases_componentes.mp4"
CARD_R = (140, 150, 1640, 690)
LEFT = (140, 150, 1060, 650)
WATER = "#7FB2F0"
OIL = "#F2C230"
SAND = "#D9B26A"
ICE = "#E6F4FD"
BRONZE = "#B08D57"
ALC = "#9CC4F2"


# ======================================================================
# tempos das palavras
# ======================================================================

def _n(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9]", "", "".join(ch for ch in s if unicodedata.category(ch) != "Mn"))


@lru_cache(None)
def _words():
    p = Path(__file__).resolve().parents[1] / "audio" / "tempos.json"
    if not p.exists():
        return {}
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s["id"]: [(_n(w["disp"]), w["t0"]) for w in s.get("tokens", [])] for s in d["scenes"]}


def WT(C, sid, palavra, k=1, depois=None):
    ws = [(w, C[sid] + t0) for w, t0 in _words().get(sid, []) if w == _n(palavra)]
    if depois is not None:
        ws = [x for x in ws if x[1] >= depois - 0.05]
    if not ws:
        return (depois if depois is not None else C[sid]) + 1.2
    return ws[k - 1 if k > 0 else k][1]


# ======================================================================
# recipientes em corte lateral
# ======================================================================

def recipiente(c, x, y, w, h, a, camadas=(), objetos=(), bico=True):
    """camadas = [(f0, f1, cor, alpha)] em frações da altura a partir do fundo; objetos = funções (c, a) desenhadas por cima"""
    if a <= 0:
        return
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), True)
    for f0, f1, col, al in camadas:
        rrect(c, x, y + h * (1 - f1), w, h * (f1 - f0), 0, col, a * al)
    c.restore()
    for fn in objetos:
        fn(c, a)
    p = skia.Path()
    p.moveTo(x - (12 if bico else 0), y - 6); p.lineTo(x, y + 6); p.lineTo(x, y + h - 18); p.quadTo(x, y + h, x + 18, y + h)
    p.lineTo(x + w - 18, y + h); p.quadTo(x + w, y + h, x + w, y + h - 18); p.lineTo(x + w, y - 6)
    c.drawPath(p, paint("#9AA3AD", a, stroke=6, cap_round=True))
    line(c, x + 14, y + 30, x + 14, y + h - 30, "#FFFFFF", a * 0.7, 6)


def cubo(c, cx, cy, s, a, ang=0.0):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    rrect(c, -s / 2, -s / 2, s, s, s * 0.16, ICE, a * 0.95)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-s / 2, -s / 2, s, s), s * 0.16, s * 0.16), paint("#8FC3E8", a, stroke=3))
    line(c, -s * 0.28, -s * 0.28, s * 0.05, -s * 0.28, "#FFFFFF", a, 4)
    c.restore()


def areia_graos(c, x, y, w, h, a, seed=1):
    rnd = random.Random(seed)
    for k in range(int(w * h / 260)):
        c.drawCircle(x + rnd.uniform(4, w - 4), y + rnd.uniform(4, h - 4), rnd.uniform(2, 4), paint("#B88A3E", a))


def fase_box(c, x, y, w, h, n, a, col=None, badge_x=None):
    """contorno tracejado de uma fase + número"""
    col = PURPLE if col is None else col
    if a <= 0:
        return
    s_ = 0.85 + 0.15 * ease_back(clamp(a))
    rrect(c, x, y, w, h, 12, col, a * 0.10)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 12, 12), _dash(col, a))
    bx = (x + w + 34) if badge_x is None else badge_x
    c.save(); c.translate(bx, y + h / 2); c.scale(s_, s_)
    badge_num(c, n, 0, 0, a, 24, bg=col)
    c.restore()


def _dash(col, a):
    p = paint(col, a, stroke=4)
    p.setPathEffect(skia.DashPathEffect.Make([14, 9], 0))
    return p


# ---- sistemas usados na aula -------------------------------------------------

def sis_agua_oleo(c, x, y, w, h, a):
    recipiente(c, x, y, w, h, a, [(0, 0.45, WATER, 0.55), (0.45, 0.75, OIL, 0.8)])


def sis_gelo(c, x, y, w, h, a, t=0.0):
    lv = 0.72
    cubes = [(0.28, -8), (0.52, 6), (0.75, -4)]

    def obj(c, aa):
        for k, (fx, ang) in enumerate(cubes):
            bob = math.sin(t * 1.4 + k) * 3
            cubo(c, x + w * fx, y + h * (1 - lv) + 8 + bob, w * 0.2, aa, ang)
    recipiente(c, x, y, w, h, a, [(0, lv, WATER, 0.55)], [obj])
    return [(x + w * fx, y + h * (1 - lv) + 8, w * 0.2) for fx, _ in cubes], (x, y + h * (1 - lv) + 8 + w * 0.12, w, h * lv - w * 0.12 - 8)


def sis_alcool(c, x, y, w, h, a):
    recipiente(c, x, y, w, h, a, [(0, 0.72, ALC, 0.55)])


POTE = dict(areia=(0.0, 0.17), agua=(0.17, 0.52), oleo=(0.52, 0.8))


def sis_pote(c, x, y, w, h, a, t=0.0, mostra=("areia", "agua", "oleo", "gelo")):
    cam = []
    if "areia" in mostra:
        cam.append((POTE["areia"][0], POTE["areia"][1], SAND, 1.0))
    if "agua" in mostra:
        cam.append((POTE["agua"][0], POTE["agua"][1], WATER, 0.55))
    if "oleo" in mostra:
        cam.append((POTE["oleo"][0], POTE["oleo"][1], OIL, 0.8))
    s = w * 0.22

    def obj(c, aa):
        if "areia" in mostra:
            areia_graos(c, x + 4, y + h * (1 - POTE["areia"][1]) + 4, w - 8, h * POTE["areia"][1] - 10, aa)
        if "gelo" in mostra:
            yi = y + h * (1 - POTE["agua"][1])           # divisa óleo/água
            cubo(c, x + w * 0.6, yi + s * 0.1, s, aa, 5)  # 60% na água, 40% no óleo
    recipiente(c, x, y, w, h, a, cam, [obj])
    yi = y + h * (1 - POTE["agua"][1])
    return dict(oleo=(x + 6, y + h * (1 - POTE["oleo"][1]), w - 12, h * (POTE["oleo"][1] - POTE["agua"][1]) - 4),
                gelo=(x + w * 0.6 - s * 0.62, yi + s * 0.1 - s * 0.62, s * 1.24, s * 1.24),
                agua=(x + 6, yi + 4, w - 12, h * (POTE["agua"][1] - POTE["agua"][0]) - 8),
                areia=(x + 6, y + h * (1 - POTE["areia"][1]) + 2, w - 12, h * POTE["areia"][1] - 8))


def sis_bronze(c, x, y, w, h, a):
    def obj(c, aa):
        areia_graos(c, x + 4, y + h * 0.84 + 4, w - 8, h * 0.16 - 10, aa, 3)
        rrect(c, x + w * 0.3, y + h * 0.84 - h * 0.18, w * 0.4, h * 0.18, 10, BRONZE, aa, shadow=True)
        rrect(c, x + w * 0.33, y + h * 0.84 - h * 0.16, w * 0.3, 8, 4, "#FFFFFF", aa * 0.35)
    recipiente(c, x, y, w, h, a, [(0, 0.16, SAND, 1.0), (0.16, 0.74, WATER, 0.5)], [obj])
    return dict(agua=(x + 6, y + h * 0.26 + 4, w - 12, h * 0.36 - 12), bronze=(x + w * 0.27, y + h * 0.64, w * 0.46, h * 0.22),
                areia=(x + 6, y + h * 0.86, w - 12, h * 0.14 - 6))


# ======================================================================
# colunas FOTO / RECEITA e tabela
# ======================================================================

def icone_foto(c, cx, cy, a, col):
    rrect(c, cx - 22, cy - 14, 44, 30, 7, col, a)
    rrect(c, cx - 8, cy - 20, 16, 8, 3, col, a)
    c.drawCircle(cx, cy + 1, 9, paint("#FFFFFF", a))
    c.drawCircle(cx, cy + 1, 5, paint(col, a))


def icone_receita(c, cx, cy, a, col):
    rrect(c, cx - 17, cy - 22, 34, 44, 5, "#FFFFFF", a, stroke=3, stroke_color=col)
    for k in range(3):
        line(c, cx - 9, cy - 10 + k * 10, cx + 9, cy - 10 + k * 10, col, a, 3)


def colunas(c, t, x, y, w, h, foto, receita, tot_f=None, tot_r=None, a=1.0):
    """foto/receita = [(instante, texto, cor)] · tot_* = (instante, texto)"""
    if a <= 0:
        return
    card(c, x, y, w, h, a)
    cw = w / 2
    for k, (s, ic) in enumerate((("FOTO", icone_foto), ("RECEITA", icone_receita))):
        cx = x + cw * k + cw / 2
        ic(c, cx - text_w(s, "black", 26) / 2 - 34, y + 46, a, PURPLE)
        text_mid(c, s, cx + 14, y + 46, 26, "black", PURPLE, a)
        text_mid(c, "fases" if k == 0 else "componentes", cx, y + 84, 20, "bold", INK2, a)
    line(c, x + cw, y + 26, x + cw, y + h - 20, LINE, a, 2)
    for k, items in enumerate((foto, receita)):
        cx = x + cw * k + cw / 2
        for j, (tc, s, col) in enumerate(items):
            ak, dy = rise(t, tc)
            ak *= a
            if ak <= 0:
                continue
            yy = y + 130 + j * 50 + dy
            rrect(c, cx - cw / 2 + 14, yy - 20, cw - 28, 40, 10, col or LIGHT, ak * 0.25)
            if k == 0:
                badge_num(c, j + 1 if not s.startswith("=") else "", cx - cw / 2 + 36, yy, ak, 14, bg=PURPLE)
            text_mid(c, s.lstrip("="), cx + (8 if k == 0 else 0), yy, 22, "black", INK, ak)
        tot = tot_f if k == 0 else tot_r
        if tot:
            at = ep(t, tot[0], 0.5) * a
            if at > 0:
                s_ = 0.8 + 0.2 * ease_back(clamp(at))
                c.save(); c.translate(cx, y + h - 46); c.scale(s_, s_)
                rrect(c, -cw / 2 + 14, -26, cw - 28, 52, 14, GREEN, at * 0.14)
                text_mid(c, tot[1], 0, 0, 26, "black", GREEN, at)
                c.restore()


TABELA = [("10.c", "água + gelo", "2", "1"), ("11.c", "água + álcool", "1", "2"), ("12.a", "ar", "1", "vários"),
          ("12.b", "granito", "3", "3"), ("14.c", "água, óleo, areia, gelo", "4", "3"), ("15.d", "bronze", "1", "2")]


def tabela(c, t, C, x=1230, y=150, w=550, h=650, a=1.0):
    if a <= 0:
        return
    card(c, x, y, w, h, a)
    c1, c2 = x + w - 170, x + w - 70
    text(c, "SISTEMA", x + 30, y + 52, 20, "black", INK2, a, align="left")
    icone_foto(c, c1, y + 44, a, PURPLE)
    icone_receita(c, c2, y + 44, a, PURPLE)
    line(c, x + 20, y + 76, x + w - 20, y + 76, LINE, a, 2)
    for k, (cue, s, nf, nc) in enumerate(TABELA):
        tc = C[cue] if cue in C else 1e9
        ak = a * ep(t, tc, 0.4)
        if ak <= 0:
            continue
        yy = y + 120 + k * 84
        sz = 22 if text_w(s, "bold", 22) < w - 250 else 18
        text_mid(c, s, x + 30, yy, sz, "bold", INK, ak, align="left")
        text_mid(c, nf, c1, yy, 34, "black", PURPLE, ak)
        text_mid(c, nc, c2, yy, 34 if len(nc) < 3 else 20, "black", PURPLE, ak)
        if k < len(TABELA) - 1:
            line(c, x + 20, yy + 42, x + w - 20, yy + 42, LINE, ak, 1.5)


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    V.regra(c, s, cx, cy, a, size, col, w)


# ======================================================================
# gancho, promessa, pré-requisitos, sistema
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "FASES E COMPONENTES · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["01.a"], 0.5)
    cubes, _ = sis_gelo(c, 360, 260, 420, 480, a0, t)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "quantas fases?", 1220, 330, 60, "black", INK, ab)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        for k, (cx, cy, s) in enumerate(cubes):
            badge_num(c, k + 1, cx, cy - s * 0.8, ac * ep(t, C["01.c"] + 0.15 * k, 0.3), 22, bg=RED)
        badge_num(c, 4, 790, 600, ac * ep(t, C["01.c"] + 0.5, 0.3), 22, bg=RED)
        text(c, "4?", 1220, 500, 130, "black", RED, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        strike(c, 1150, 455, 1290, 455, ad, RED, ease_io(prog(t, C["01.d"], 0.4)))
        pill(c, "a pegadinha mais comum", 1220, 640, AMBER, size=30, fg=INK, a=ad, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONTAR", GREEN)
    for k, (cue, s, sub, ic) in enumerate((("02.c", "FOTO", "fases", icone_foto), ("02.c", "RECEITA", "componentes", icone_receita))):
        a, dy = rise(t, C[cue] + 0.8 * k)
        if a <= 0:
            continue
        x = 620 + k * 680
        card(c, x - 290, 220 + dy, 580, 440, a)
        c.save(); c.translate(x, 360 + dy); c.scale(3, 3)
        ic(c, 0, 0, a, PURPLE)
        c.restore()
        text(c, s, x, 540 + dy, 60, "black", PURPLE, a)
        text(c, sub, x, 600 + dy, 34, "bold", INK2, a)
    pill(c, "qualquer recipiente, sem cair em armadilha", W / 2, 760, GREEN, size=30, a=ep(t, C["02.b"], 0.5), anchor="center", bounds=(0, 1920))


def b_prereq(c, t, C, B):
    if t < C["04"] - 0.2:
        head(c, t, B["start"], "LEMBRETES", "SUBSTÂNCIA E MISTURA", BLUE)
        card(c, *CARD_R)
        aa = ep(t, C["03.a"], 0.5)
        V.mol(c, "H2O", 360, 330, 46, aa)
        text(c, "água", 360, 440, 30, "black", INK, aa)
        V.peca(c, 700, 330, 30, "C", aa, False); V.peca(c, 750, 330, 30, "C", aa, False); V.peca(c, 800, 330, 26, "O", aa, False)
        text(c, "álcool", 750, 440, 30, "black", INK, aa)
        V.defbox(c, "SUBSTÂNCIA", "1 tipo de montagem", 560, 600, aa, w=560)
        ab = ep(t, C["03.b"], 0.5)
        V3.vidro(c, 1150, 560, 200, 280, ab, "acucar", t, 1)
        text(c, "homogênea", 1150, 620, 28, "black", BLUE, ab)
        V3.vidro(c, 1450, 560, 200, 280, ab, "oleo")
        text(c, "heterogênea", 1450, 620, 28, "black", "#B07A00", ab)
        text(c, "uma coisa só  ×  partes diferentes", 1300, 720, 26, "bold", INK2, ab)
        return
    head(c, t, C["04"], "LEMBRETE", "DENSIDADE", BLUE)
    card(c, *CARD_R)
    V.defbox(c, "DENSIDADE", "quanto de massa cabe num mesmo espaço", 620, 260, ep(t, C["04.t"], 0.5), w=760)
    aa = ep(t, C["04.a"], 0.5)
    sis_agua_oleo(c, 1190, 240, 300, 440, aa)
    if aa > 0:
        arrow(c, 1530, 400, 1530, 340, GREEN, aa, 5, 16)
        text(c, "menos denso:", 1560, 360, 26, "black", GREEN, aa, align="left")
        text(c, "flutua", 1560, 395, 26, "black", GREEN, aa, align="left")
        arrow(c, 1530, 560, 1530, 620, BLUE, aa, 5, 16)
        text(c, "mais denso:", 1560, 580, 26, "black", BLUE, aa, align="left")
        text(c, "afunda", 1560, 615, 26, "black", BLUE, aa, align="left")
        regra(c, "+ denso afunda · − denso flutua", 620, 480, aa, 32, PURPLE, w=640)


def b_sistema(c, t, C, B):
    head(c, t, B["start"], "PALAVRA NOVA", "SISTEMA", BLUE)
    card(c, *CARD_R)
    V.defbox(c, "SISTEMA", "o que você está observando: o conteúdo do recipiente", W / 2, 250, ep(t, C["05.a"], 0.5), w=1000)
    for k, fn in enumerate((lambda a: sis_gelo(c, 300, 420, 260, 300, a, t), lambda a: sis_pote(c, 830, 380, 260, 340, a, t),
                            lambda a: sis_bronze(c, 1360, 400, 260, 320, a))):
        a = ep(t, C["05.a"] + 0.5 * k, 0.4)
        fn(a)
    pill(c, "a pergunta é sempre sobre um sistema", W / 2, 790, GREEN, size=26, a=ep(t, C["05.b"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos a-b: fase e componente
# ======================================================================

def b_fase(c, t, C, B):
    head(c, t, B["start"], "COMO CONTAR", "FASES: A FOTO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:   # moldura de foto
        rrect(c, 260, 200, 520, 600, 18, "#FFFFFF", aa, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(260, 200, 520, 600), 18, 18), paint(INK, aa, stroke=6))
        icone_foto(c, 300, 236, aa, INK)
        fl = 1 - prog(t, C["06.a"], 0.35)
        rrect(c, 260, 200, 520, 600, 18, "#FFFFFF", aa * fl * 0.9)
    sis_agua_oleo(c, 370, 300, 300, 440, ep(t, C["06.t"], 0.5))
    ac = ep(t, C["06.c"], 0.5)
    fase_box(c, 376, 300 + 440 * 0.25, 288, 440 * 0.3 - 4, 1, ac * ep(t, C["06.c"] + 0.8, 0.3))
    fase_box(c, 376, 300 + 440 * 0.55 + 4, 288, 440 * 0.45 - 12, 2, ac * ep(t, WT(C, "06", "dois", 1, C["06.c"]), 0.3))
    V.defbox(c, "FASE", "cada parte com a mesma aparência do começo ao fim", 1240, 330, ep(t, C["06.b"], 0.5), w=720)
    regra(c, "fases = o que o olho distingue na FOTO", 1240, 640, ep(t, C["06.d"], 0.5), 30, PURPLE, w=720)


def b_componente(c, t, C, B):
    head(c, t, B["start"], "COMO CONTAR", "COMPONENTES: A RECEITA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 520, 600, 14, "#FFFDF5", aa, shadow=True, stroke=3, stroke_color=LIGHT)
        icone_receita(c, 320, 260, aa, PURPLE)
        text(c, "RECEITA", 360, 272, 34, "black", PURPLE, aa, align="left")
        for k, (s, col) in enumerate((("água", WATER), ("óleo", OIL))):
            ak = ep(t, C["07.c"] + 0.7 * k, 0.4)
            rrect(c, 300, 340 + k * 90, 440, 64, 12, col, ak * 0.3)
            text_mid(c, f"• {s}", 330, 372 + k * 90, 36, "black", INK, ak, align="left")
        text(c, "2 componentes", 520, 720, 40, "black", GREEN, ep(t, C["07.c"] + 1.8, 0.4))
    V.defbox(c, "COMPONENTE", "cada substância presente no sistema", 1240, 330, ep(t, C["07.b"], 0.5), w=720)
    pill(c, "a lista de ingredientes", 1240, 470, PURPLE, size=30, a=ep(t, C["07.b"] + 1.6, 0.5), anchor="center", bounds=(0, 1920))


def b_colunas(c, t, C, B):
    head(c, t, B["start"], "O RITUAL", "DUAS COLUNAS", PURPLE)
    sis_agua_oleo(c, 300, 260, 320, 460, 1.0)
    colunas(c, t, 760, 170, 1000, 560,
            [(C["08.a"], "óleo", OIL), (C["08.a"] + 0.6, "água", WATER)],
            [(C["08.b"], "água", WATER), (C["08.b"] + 0.6, "óleo", OIL)],
            (C["08.a"] + 1.2, "2 fases"), (C["08.b"] + 1.2, "2 componentes"))
    ac = ep(t, C["08.c"], 0.5)
    pill(c, "1º FOTO, de cima para baixo  →  2º RECEITA", 1260, 790, PURPLE, size=28, a=ac * (1 - ep(t, C["08.d"], 0.4)), anchor="center", bounds=(0, 1920))
    pill(c, "só então as alternativas", 1260, 790, GREEN, size=28, a=ep(t, C["08.d"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco c: o copo com gelo
# ======================================================================

def b_gelo(c, t, C, B):
    head(c, t, B["start"], "O COPO DO COMEÇO", "TRÊS CUBOS = UMA FASE", PURPLE)
    card(c, 140, 150, 760, 690)
    cubes, liq = sis_gelo(c, 300, 300, 440, 460, 1.0, t)
    ab = ep(t, C["09.b"], 0.5) * (1 - ep(t, C["09.c"], 0.4))
    for k, (cx, cy, s) in enumerate(cubes):
        badge_num(c, k + 1, cx, cy - s * 0.85, ab, 20, bg=RED)
    ae = ep(t, C["09.e"], 0.5)
    for k, (cx, cy, s) in enumerate(cubes):
        ak = ae * ep(t, C["09.e"] + 0.25 * k, 0.3)
        if ak > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.66, cy - s * 0.66, s * 1.32, s * 1.32), 10, 10), _dash(PURPLE, ak))
            badge_num(c, 1, cx, cy - s * 0.92, ak, 20, bg=PURPLE)
    af = ep(t, C["09.f"], 0.5)
    lx, ly, lw, lh = liq
    fase_box(c, lx + 6, ly + 20, lw - 12, lh - 26, 2, af, badge_x=lx + lw + 40)
    ac = ep(t, C["09.c"], 0.5)
    pill(c, "mesma substância · mesmo estado", 1330, 260, INK2, size=28, a=ac, anchor="center", bounds=(0, 1920))
    regra(c, "pedaços da mesma coisa no mesmo estado = 1 FASE", 1330, 400, ep(t, C["09.d"], 0.5), 26, PURPLE, w=820)
    colunas(c, t, 960, 480, 740, 340,
            [(C["09.e"], "gelo (3 cubos)", ICE), (C["09.f"], "água líquida", WATER)],
            [(C["10.b"], "água (H₂O)", WATER)] if "10.b" in C else [],
            (C["09.f"] + 0.8, "2 fases"), (C["10.b"] + 0.8, "1 componente") if "10.b" in C else None,
            a=ep(t, C["09.e"], 0.5))
    aa10 = ep(t, C["10.a"], 0.5) * (1 - ep(t, C["10.b"], 0.4))
    pill(c, "gelo = água congelada", 1330, 260, BLUE, size=28, a=aa10, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco d: números independentes
# ======================================================================

def b_independentes(c, t, C, B):
    head(c, t, B["start"], "NÚMEROS", "INDEPENDENTES", PURPLE)
    card(c, *LEFT)
    regra(c, "um número NÃO decide o outro", 670, 230, ep(t, C["11.a"], 0.5), 30, PURPLE, w=720)
    ab = ep(t, C["11.b"], 0.5)
    sis_alcool(c, 260, 320, 260, 380, ab)
    text(c, "água + álcool", 390, 760, 30, "black", INK, ab)
    fase_box(c, 266, 320 + 380 * 0.28 + 4, 248, 380 * 0.72 - 12, 1, ep(t, C["11.b"] + 1.2, 0.4))
    colunas(c, t, 620, 310, 520, 420, [(C["11.b"] + 1.2, "transparente", ALC)],
            [(C["11.c"], "água", WATER), (C["11.c"] + 0.6, "álcool", ALC)],
            (C["11.b"] + 1.8, "1 fase"), (C["11.c"] + 1.2, "2 comp."), a=ep(t, C["11.b"], 0.5))
    tabela(c, t, C)


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "MAIS DOIS", "PARA FIXAR", PURPLE)
    card(c, *LEFT)
    for k, (cue, nome, nf, nc) in enumerate((("12.a", "AR", "1 fase", "N₂, O₂ e outros"), ("12.b", "GRANITO", "3 fases", "quartzo, feldspato, mica"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 540
        if k == 0:
            V3.gas_mix(c, x, 380 + dy, 380, 260, a, t)
        else:
            V3.granito(c, x, 380 + dy, 380, 260, a, 1.6)
        text(c, nome, x, 570 + dy, 36, "black", INK, a)
        pill(c, nf, x - 110, 640 + dy, PURPLE, size=24, a=a, anchor="center", bounds=(0, 1920))
        text(c, nc, x, 720 + dy, 24, "bold", INK2, a)
        icone_receita(c, x + 60, 640 + dy, a, PURPLE)
        text_mid(c, "vários" if k == 0 else "3", x + 110, 640 + dy, 26, "black", PURPLE, a, align="left")
    tabela(c, t, C)


# ======================================================================
# bloco e: camadas pela densidade
# ======================================================================

DENS = [("areia", "mais densa", SAND), ("água", "1,0", WATER), ("gelo", "0,92", ICE), ("óleo", "0,8", OIL)]


def b_camadas(c, t, C, B):
    head(c, t, B["start"], "VÁRIAS CAMADAS", "A ORDEM PELA DENSIDADE", BLUE)
    if t < C["14"] - 0.2:
        card(c, *CARD_R)
        mostra = ["areia"]
        if t >= C["13.c"] - 0.3:
            mostra += ["agua", "oleo"]
        elif t >= C["13.b"] - 0.3:
            mostra += ["agua"]
        if t >= C["13.d"] - 0.3:
            mostra += ["gelo"]
        a0 = ep(t, C["13.a"], 0.5)
        reg = sis_pote(c, 360, 230, 380, 520, a0, t, tuple(mostra))
        rows = [("13.b", "areia", "a mais densa: AFUNDA", "#B07A00"),
                ("13.c", "óleo 0,8", "menor que a água (1,0): fica POR CIMA", "#B07A00"),
                ("13.d", "gelo 0,92", "+ leve que a água, + pesado que o óleo", BLUE),
                ("13.e", "→ para na divisa", "atravessa o óleo e boia na água", PURPLE)]
        for k, (cue, s1, s2, col) in enumerate(rows):
            a, dy = rise(t, C[cue])
            if a <= 0:
                continue
            y = 280 + k * 120 + dy
            text(c, s1, 900, y, 36, "black", col, a, align="left")
            text(c, s2, 900, y + 44, 26, "bold", INK2, a, align="left")
        ae = ep(t, C["13.e"], 0.5)
        if ae > 0:
            gx, gy, gw, gh = reg["gelo"]
            c.drawCircle(gx + gw / 2, gy + gh / 2, gw * 0.75, _dash(AMBER, ae))
        return
    card(c, 140, 150, 820, 690)
    reg = sis_pote(c, 300, 230, 380, 520, 1.0, t)
    fotos = [("14.f1", "oleo", "óleo", OIL), ("14.f2", "gelo", "gelo", ICE), ("14.f3", "agua", "água", WATER), ("14.f4", "areia", "areia", SAND)]
    for k, (cue, key, s, col) in enumerate(fotos):
        x, y, w, h = reg[key]
        fase_box(c, x, y, w, h, k + 1, ep(t, C[cue], 0.35), badge_x=300 + 380 + 50 if key != "gelo" else x + w + 30)
    colunas(c, t, 1000, 170, 760, 560,
            [(C[cue], s, col) for cue, _, s, col in fotos],
            [(C["14.r1"], "óleo", OIL), (C["14.r2"], "água (líquida + gelo)", WATER), (C["14.r3"], "areia", SAND)],
            (C["14.f4"] + 0.8, "4 fases"), (C["14.c"] + 1.0, "3 componentes"))
    pill(c, "o gelo é água: não entra de novo", 1380, 790, AMBER, size=26, fg=INK, a=ep(t, C["14.c"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco f: o bronze
# ======================================================================

def b_bronze(c, t, C, B):
    head(c, t, B["start"], "O CASO DO", "BRONZE", BLUE)
    card(c, *LEFT)
    aa = ep(t, C["15.a"], 0.5)
    V3.blocos_liga(c, 400, 330, aa, ease_io(prog(t, C["15.a"] + 0.4, 2.2)))
    V.defbox(c, "LIGA HOMOGÊNEA", "metais derretidos juntos: endurecem como uma coisa só", 670, 560, aa, w=900)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        fase_box(c, 255, 330 + 60 - 80, 290, 90, 1, ab, badge_x=590)
    colunas(c, t, 680, 180, 460, 300, [(C["15.b"], "bloco único", BRONZE)],
            [(C["15.c"], "cobre", "#C77B43"), (C["15.c"] + 0.6, "estanho", "#A7ADB4")],
            (C["15.b"] + 0.8, "1 fase"), (C["15.c"] + 1.2, "2 comp."), a=ab)
    pill(c, "1 fase · 2 componentes", 670, 720, GREEN, size=28, a=ep(t, C["15.d"], 0.5), anchor="center", bounds=(0, 1920))
    tabela(c, t, C)


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Fase é a foto; componente é a receita.",
          "Pedaços da mesma coisa no mesmo estado: uma fase só.",
          "Os dois números são independentes: conte duas vezes."]


def b_recap(c, t, C, B):
    sid = "16" if B["start"] < C["28"] - 1 else "28"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", BLUE), ("b", GREEN), ("c", PURPLE))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 230, y - 16, a, 32, bg=col)
        text(c, FRASES[k], 290, y, 46, "black", INK, a, align="left")


def b_erro1(c, t, C, B):
    head(c, t, B["start"], "ERRO 1", "CADA CUBO, UMA FASE", RED)

    def ex(c, k, x, y, cw, a):
        if k == 2:
            for j in range(3):
                cubo(c, x + cw / 2 - 90 + j * 90, y + 470, 60, a, (-8, 5, -3)[j])
                badge_num(c, 1, x + cw / 2 - 90 + j * 90, y + 420, a, 16, bg=PURPLE)
    V.erro_tiles(c, t, [(C["17.a"], "O ERRO", ["!3 cubos =", "!3 fases"], RED),
                        (C["17.b"], "POR QUE PARECE CERTO", ["os cubos estão", "separados: você", "vê três coisas"], AMBER),
                        (C["17.c"], "A CORREÇÃO", ["mesma substância,", "mesmo estado", "!1 FASE"], GREEN)], ex)


def b_erro2(c, t, C, B):
    head(c, t, B["start"], "ERRO 2", "FASES = COMPONENTES?", RED)
    V.erro_tiles(c, t, [(C["18.a"], "O ERRO", ["!fases e componentes", "!dão o mesmo número"], RED),
                        (C["18.b"], "POR QUE PARECE CERTO", ["em água e óleo", "os dois dão 2"], AMBER),
                        (C["18.c"], "A CORREÇÃO", ["água + álcool:", "1 fase, 2 componentes", "!CONTE DUAS VEZES"], GREEN)])


def b_erro3(c, t, C, B):
    head(c, t, B["start"], "ERRO 3", "GELO E ÁGUA = 2 COMPONENTES?", RED)
    V.erro_tiles(c, t, [(C["19.a"], "O ERRO", ["!gelo e água:", "!2 componentes"], RED),
                        (C["19.b"], "POR QUE PARECE CERTO", ["um é sólido,", "o outro é líquido"], AMBER),
                        (C["19.c"], "A CORREÇÃO", ["a receita ignora", "o estado: H₂O", "!1 COMPONENTE"], GREEN)])


def b_erro4(c, t, C, B):
    head(c, t, B["start"], "ERRO 4", "LIGA = 2 FASES?", RED)
    V.erro_tiles(c, t, [(C["20.a"], "O ERRO", ["!2 metais da liga", "!= 2 fases"], RED),
                        (C["20.b"], "POR QUE PARECE CERTO", ["são dois", "ingredientes"], AMBER),
                        (C["20.c"], "A CORREÇÃO", ["a foto mostra", "um bloco uniforme", "!1 FASE"], GREEN)])


# ======================================================================
# questões 1, 4 e 9
# ======================================================================

def questao(c, t, C, B, sid_e, enun, alts, alt_cues, correta, cue_ok, sis, foto, receita, tot_f, tot_r, xs, pause_cue, sol_cue):
    """layout comum: enunciado + alternativas à esquerda · recipiente e colunas à direita"""
    card(c, 140, 160, 820, 660)
    pill(c, "QUESTÃO", 170, 204, BLUE, size=22, bounds=(0, 1920))
    for k, (cue, s) in enumerate(enun):
        text(c, s, 180, 280 + k * 42, 27, "black", INK if k < len(enun) - 1 else INK2, ep(t, C[cue], 0.5), align="left")
    y0 = 280 + len(enun) * 42 + 40
    aok = ep(t, C[cue_ok], 0.5)
    for k, s in enumerate(alts):
        L = "ABCDE"[k]
        a, d = rise(t, C[alt_cues[k]])
        y = y0 + k * 58 + d
        ok = L == correta
        if ok and aok > 0:
            rrect(c, 170, y - 38, 760, 54, 12, GREEN, 0.15 * aok)
        badge_num(c, L, 205, y - 12, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
        x_cue, why = xs.get(L, (None, ""))
        ax = ep(t, C[x_cue], 0.4) if x_cue else 0
        text(c, s, 245, y, 27, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 240, y - 10, 250 + text_w(s, "black", 27), y - 10, ax, RED, ax)
            text(c, why, 920, y - 2, 20, "black", RED, ax, align="right")
    V.pause_badge(c, 1200, 440, ep(t, C[pause_cue], 0.5) * (1 - prog(t, C[sol_cue] - 0.3, 0.4)))
    ar = ep(t, C[sol_cue], 0.5)
    if ar > 0:
        card(c, 1000, 160, 780, 660, ar)
        sis(c, ar)
        colunas(c, t, 1320, 180, 440, 620, foto, receita, tot_f, tot_r, a=ar)


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1", "ÁGUA E GELO", BLUE)

    def sis(c, a):
        cubes, liq = sis_gelo(c, 1030, 300, 230, 330, a, t)
        af = ep(t, C["22.f"], 0.4) * a
        for cx, cy, s in cubes:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.66, cy - s * 0.66, s * 1.32, s * 1.32), 8, 8), _dash(PURPLE, af))
        lx, ly, lw, lh = liq
        fase_box(c, lx + 6, ly + 14, lw - 12, lh - 20, 2, ep(t, C["22.f"] + 0.8, 0.4) * a, badge_x=lx + lw / 2)
        badge_num(c, 1, cubes[1][0], cubes[1][1] - cubes[1][2] * 0.9, af, 16, bg=PURPLE)
    questao(c, t, C, B, "21", [("21.e1", "Um copo contém água líquida e"), ("21.e1", "três cubos de gelo."), ("21.e2", "Esse sistema apresenta:")],
            ["1 componente e 1 fase", "1 componente e 2 fases", "1 componente e 4 fases", "2 componentes e 2 fases",
             "4 componentes e 4 fases"], ["21.a", "21.b", "21.c", "21.d", "21.e"], "B", "22.ok", sis,
            [(C["22.f"], "gelo ×3", ICE), (C["22.f"] + 0.8, "água líq.", WATER)], [(C["22.r"], "água", WATER)],
            (C["22.f"] + 1.4, "2 fases"), (C["22.r"] + 0.8, "1 comp."),
            {"C": ("22.x", "cada cubo como fase"), "D": ("22.xd", "gelo como outro componente"),
             "E": ("22.xe", "os dois erros"), "A": ("22.xa", "confundiu foto com receita")}, "21.p", "22.t")


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4", "CONTAGEM DE FASES", BLUE)

    def sis(c, a):
        reg = sis_pote(c, 1030, 260, 230, 400, a, t)
        for k, key in enumerate(("oleo", "gelo", "agua", "areia")):
            x, y, w, h = reg[key]
            fase_box(c, x, y, w, h, k + 1, ep(t, C["24.f"] + 0.5 * k, 0.3) * a, badge_x=1030 + 230 + 26 if key != "gelo" else x + w + 18)
    questao(c, t, C, B, "23", [("23.e1", "Recipiente com água líquida, óleo,"), ("23.e1", "areia e um cubo de gelo."),
                               ("23.e2", "Número de fases depois de alguns instantes:")],
            ["2", "3", "4", "5", "6"], ["23.a", "23.b", "23.c", "23.d", "23.e"], "C", "24.ok", sis,
            [(C["24.f"] + 0.5 * k, s, col) for k, (s, col) in enumerate((("óleo", OIL), ("gelo", ICE), ("água", WATER), ("areia", SAND)))],
            [(C["24.r"] + 0.4 * k, s, col) for k, (s, col) in enumerate((("óleo", OIL), ("água", WATER), ("areia", SAND)))],
            (C["24.f"] + 2.2, "4 fases"), (C["24.r"] + 1.4, "3 comp."),
            {"B": ("24.xb", "respondeu componentes"), "A": ("24.xa", "esqueceu os sólidos"),
             "D": ("24.xd", "inventou fase"), "E": ("24.xd", "inventou fases")}, "23.p", "24.t")


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9", "A LIGA NO BÉQUER", BLUE)

    def sis(c, a):
        reg = sis_bronze(c, 1030, 280, 230, 380, a)
        for k, key in enumerate(("agua", "bronze", "areia")):
            x, y, w, h = reg[key]
            fase_box(c, x, y, w, h, k + 1, ep(t, C["26.f"] + 0.5 * k, 0.3) * a, badge_x=1030 + 230 + 26)
    questao(c, t, C, B, "25", [("25.e1", "Béquer com bronze (liga homogênea"), ("25.e1", "de cobre e estanho), água e areia."),
                               ("25.e2", "Fases e componentes, respectivamente:")],
            ["3 e 3", "3 e 4", "4 e 3", "4 e 4", "2 e 4"], ["25.a", "25.b", "25.c", "25.d", "25.e"], "B", "26.ok", sis,
            [(C["26.f"] + 0.5 * k, s, col) for k, (s, col) in enumerate((("água", WATER), ("bronze", BRONZE), ("areia", SAND)))],
            [(C["26.r"] + 0.4 * k, s, col) for k, (s, col) in enumerate((("cobre", "#C77B43"), ("estanho", "#A7ADB4"), ("água", WATER), ("areia", SAND)))],
            (C["26.f"] + 1.8, "3 fases"), (C["26.r"] + 1.8, "4 comp."),
            {"A": ("27.xa", "bronze como 1 componente"), "D": ("27.xd", "2 metais como 2 fases"),
             "C": ("27.xc", "trocou as colunas"), "E": ("27.xe", "juntou os sólidos")}, "25.p", "26.t")


# ======================================================================
# ponte e CTA
# ======================================================================

def relogio(c, cx, cy, r, a, t):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=8))
    for k in range(12):
        th = math.radians(k * 30)
        line(c, cx + (r - 18) * math.sin(th), cy - (r - 18) * math.cos(th), cx + (r - 8) * math.sin(th), cy - (r - 8) * math.cos(th), INK2, a, 4)
    th = math.radians(t * 60)
    line(c, cx, cy, cx + (r - 30) * math.sin(th), cy - (r - 30) * math.cos(th), RED, a, 5)
    line(c, cx, cy, cx, cy - r * 0.45, INK, a, 7)


def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A CURVA DE AQUECIMENTO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.t"], 0.5)
    recipiente(c, 300, 330, 240, 320, a0, [(0, 0.6, "#C9C3BC", 0.9)])
    text(c, "?", 420, 520, 100, "black", INK, a0)
    V.termometro(c, 760, 300, ep(t, C["29.a"], 0.5), 300, 0.6, RED)
    relogio(c, 1020, 450, 110, ep(t, C["29.b"], 0.5), t)
    ac = ep(t, C["29.c"], 0.5)
    if ac > 0:
        x0, y0 = 1250, 640
        pts = [(0, 0), (90, -110), (190, -110), (270, -230), (380, -230), (440, -320)]
        p = skia.Path(); p.moveTo(x0 + pts[0][0], y0 + pts[0][1])
        for x, y in pts[1:]:
            p.lineTo(x0 + x, y0 + y)
        c.drawPath(p, paint(BLUE, ac, stroke=6, cap_round=True))
        line(c, x0, y0, x0 + 460, y0, INK2, ac, 3)
        line(c, x0, y0, x0, y0 - 340, INK2, ac, 3)
        text(c, "é puro?", x0 + 230, y0 + 60, 34, "black", INK, ac)
    pill(c, "EPISÓDIO 5: A CURVA DE AQUECIMENTO", W / 2, 790, PURPLE, size=30, a=ep(t, C["29.d"], 0.5), anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"], "Antes desta aula, você respondia quatro fases?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, sistema=b_sistema, fase=b_fase, componente=b_componente,
              colunas=b_colunas, gelo=b_gelo, independentes=b_independentes, tabela=b_tabela, camadas=b_camadas,
              bronze=b_bronze, recap=b_recap, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, erro4=b_erro4,
              q1=b_q1, q4=b_q4, q9=b_q9, ponte=b_ponte, cta=b_cta)
