"""Visual — Matéria, Substâncias e Misturas, Episódio 3: Misturas homogêneas e heterogêneas (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Reaproveita as peças do ep. 1 (V) e do ep. 2 (V2: garrafa de água mineral, anel).
Peças próprias deste episódio:
- vidro(): cada material num copo transparente (açúcar dissolvendo, água e óleo, areia, leite, sangue…).
- lupa(): a "lente de microscópio" que amplia uma gota e revela as fases (leite, sangue).
- quadro(): o quadro PURA / HOMOGÊNEA / HETEROGÊNEA, que se preenche ao longo do vídeo.
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
V2 = _load("visual_quimica_ep2", "ep2_alotropia")

MARCA = ""
ARQUIVO_FINAL = "enem_quimica_materia_ep3_misturas.mp4"
CARD_R = (140, 150, 1640, 690)
LEFT = (140, 150, 1060, 650)          # área de conteúdo quando o quadro está à direita
WATER = "#7FB2F0"
OIL = "#F2C230"
GOLD = "#E8B53A"


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
# quadro de classificação
# ======================================================================

COLS = [("PURA", GREEN), ("HOMOGÊNEA", BLUE), ("HETEROGÊNEA", AMBER)]
QUADRO = [("05.c", 1, "água com açúcar"), ("06.b", 1, "água com sal"), ("08.a", 2, "água e óleo"), ("08.b", 2, "granito"),
          ("10.d", 1, "ar"), ("11.c", 2, "fumaça"), ("11.c", 2, "neblina"), ("12.c", 2, "leite"), ("13.c", 2, "sangue"),
          ("14.d", 1, "inox"), ("15.a", 1, "aço"), ("15.c", 1, "bronze"), ("15.d", 1, "latão"), ("15.e", 1, "ouro 18 k"),
          ("17.c", 1, "água mineral"), ("18.a", 0, "água destilada"), ("18.b", 1, "soro fisiológico")]


def quadro(c, t, C, x=1230, y=150, w=550, h=650, a=1.0, todos=False):
    if a <= 0:
        return
    card(c, x, y, w, h, a)
    cw = (w - 30) / 3
    for k, (s, col) in enumerate(COLS):
        cx = x + 15 + cw * k + cw / 2
        rrect(c, cx - cw / 2 + 4, y + 18, cw - 8, 46, 12, col, a * 0.16)
        text_mid(c, s, cx, y + 41, 19 if k else 22, "black", col if col != AMBER else "#B07A00", a)
        if k:
            line(c, x + 15 + cw * k, y + 80, x + 15 + cw * k, y + h - 20, LINE, a, 2)
    n = [0, 0, 0]
    for cue, col, lab in QUADRO:
        tc = C[cue] if cue in C else 1e9
        if not todos and t < tc - 0.05:
            continue
        ak = a if todos else a * ep(t, tc, 0.4)
        cx = x + 15 + cw * col + cw / 2
        yy = y + 106 + n[col] * 52
        n[col] += 1
        s_ = 1.0 if todos else 0.7 + 0.3 * ease_back(clamp(ep(t, tc, 0.4)))
        c.save(); c.translate(cx, yy); c.scale(s_, s_)
        rrect(c, -cw / 2 + 8, -21, cw - 16, 42, 12, COLS[col][1], ak * 0.12)
        sz = 19 if text_w(lab, "bold", 19) < cw - 28 else 16
        text_mid(c, lab, 0, 0, sz, "bold", INK, ak)
        c.restore()


# ======================================================================
# copos, lupa e objetos
# ======================================================================

def _glass_path(cx, by, w, h):
    tw, bw = w, w * 0.82
    p = skia.Path()
    p.moveTo(cx - tw / 2, by - h); p.lineTo(cx - bw / 2, by); p.lineTo(cx + bw / 2, by); p.lineTo(cx + tw / 2, by - h)
    return p, tw, bw


def _band(cx, by, w, h, f0, f1):
    """faixa do copo entre as alturas relativas f0 (baixo) e f1 (cima)"""
    tw, bw = w, w * 0.82
    wa, wb = bw + (tw - bw) * f0, bw + (tw - bw) * f1
    q = skia.Path()
    q.moveTo(cx - wb / 2, by - h * f1); q.lineTo(cx - wa / 2, by - h * f0); q.lineTo(cx + wa / 2, by - h * f0)
    q.lineTo(cx + wb / 2, by - h * f1); q.close()
    return q


def vidro(c, cx, by, w, h, a, kind="agua", t=0.0, mix_=1.0):
    """copo transparente com o material; mix_ (0..1) anima a mistura quando faz sentido"""
    if a <= 0:
        return
    rnd = random.Random(hash(kind) & 0xFFFF)
    lvl = 0.78
    if kind in ("agua", "destilada", "mineral", "sal", "acucar", "gas"):
        c.drawPath(_band(cx, by, w, h, 0.0, lvl), paint(WATER, a * 0.55))
        if kind == "acucar" or kind == "sal":
            for k in range(26):   # grãos sumindo
                x = cx + rnd.uniform(-0.32, 0.32) * w
                y0 = by - h * rnd.uniform(0.05, 0.7)
                c.drawCircle(x, y0, 4, paint("#FFFFFF", a * (1 - mix_) * 0.95))
            if mix_ < 1:
                for k in range(10):
                    x = cx + rnd.uniform(-0.25, 0.25) * w
                    c.drawRect(skia.Rect.MakeXYWH(x, by - 14 - rnd.uniform(0, 8), 7, 7), paint("#FFFFFF", a * (1 - mix_)))
        if kind == "gas":
            for k in range(12):
                ph = (t * 0.4 + k / 12) % 1.0
                x = cx + math.sin(k * 7.3) * 0.28 * w
                c.drawCircle(x, by - 10 - ph * h * lvl, 5, paint("#FFFFFF", a * 0.0))
    elif kind == "oleo":
        f = mix_
        c.drawPath(_band(cx, by, w, h, 0.0, 0.48), paint(WATER, a * 0.55))
        c.drawPath(_band(cx, by, w, h, 0.48, lvl), paint(OIL, a * 0.75))
        line(c, cx - w * 0.43, by - h * 0.48, cx + w * 0.43, by - h * 0.48, "#C9A227", a, 3)
    elif kind == "areia":
        c.drawPath(_band(cx, by, w, h, 0.0, lvl), paint(WATER, a * 0.5))
        c.drawPath(_band(cx, by, w, h, 0.0, 0.2), paint("#D9B26A", a))
        for k in range(40):
            x = cx + rnd.uniform(-0.36, 0.36) * w
            c.drawCircle(x, by - rnd.uniform(4, h * 0.18), 3, paint("#B88A3E", a))
    elif kind == "leite":
        c.drawPath(_band(cx, by, w, h, 0.0, lvl), paint("#FAF7F0", a))
        c.drawPath(_band(cx, by, w, h, 0.0, lvl), paint("#E8E2D4", a, stroke=2))
    elif kind == "sangue":
        c.drawPath(_band(cx, by, w, h, 0.0, lvl), paint("#B3202A", a * 0.92))
    p, tw, bw = _glass_path(cx, by, w, h)
    c.drawPath(p, paint("#9AA3AD", a, stroke=5, cap_round=True))
    line(c, cx - tw / 2 + 14, by - h + 20, cx - bw / 2 + 12, by - 20, "#FFFFFF", a * 0.8, 5)


def lupa(c, cx, cy, r, a, kind, t=0.0, f=1.0):
    """lente de microscópio: amplia uma gota e revela as fases"""
    if a <= 0:
        return
    rnd = random.Random(7 if kind == "leite" else 11)
    c.save()
    c.clipPath(skia.Path.Circle(cx, cy, r), doAntiAlias=True)
    if kind == "leite":
        c.drawCircle(cx, cy, r, paint(mix("#FAF7F0", "#EAF2FB", f), a))
        for k in range(26):
            x, y = cx + rnd.uniform(-1, 1) * r, cy + rnd.uniform(-1, 1) * r
            rr = rnd.uniform(10, 26) * f
            dx = math.sin(t * 0.8 + k) * 4
            c.drawCircle(x + dx, y, rr, paint("#FFF3C4", a))
            c.drawCircle(x + dx, y, rr, paint("#E3C565", a * f, stroke=2.5))
    else:
        c.drawCircle(cx, cy, r, paint(mix("#B3202A", "#F6DF9B", f), a))
        for k in range(16):
            x, y = cx + rnd.uniform(-1, 1) * r, cy + rnd.uniform(-1, 1) * r
            rx, ry = 34 * f, 26 * f
            dx = math.sin(t * 0.6 + k) * 5
            c.drawOval(skia.Rect.MakeXYWH(x + dx - rx, y - ry, 2 * rx, 2 * ry), paint("#C62828", a))
            c.drawOval(skia.Rect.MakeXYWH(x + dx - rx * 0.45, y - ry * 0.4, rx * 0.9, ry * 0.8), paint("#E57373", a * f))
    c.restore()
    c.drawCircle(cx, cy, r, paint("#3A3A3C", a, stroke=14))
    c.drawCircle(cx, cy, r + 9, paint("#8E8E93", a, stroke=4))


def salada(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    rnd = random.Random(3)
    for k in range(14):
        x = cx + rnd.uniform(-1, 1) * 120 * s
        y = cy - 20 * s + rnd.uniform(-1, 0.4) * 40 * s
        col, shape = [("#F7E27A", 0), ("#E5484D", 1), ("#7B3FA0", 2), ("#F28C28", 1), ("#9BD35A", 0)][k % 5]
        if shape == 0:
            c.drawOval(skia.Rect.MakeXYWH(x - 26 * s, y - 14 * s, 52 * s, 28 * s), paint(col, a))
        elif shape == 1:
            rrect(c, x - 20 * s, y - 20 * s, 40 * s, 40 * s, 8 * s, col, a)
        else:
            c.drawCircle(x, y, 18 * s, paint(col, a))
    p = skia.Path()
    p.moveTo(cx - 170 * s, cy); p.quadTo(cx, cy + 190 * s, cx + 170 * s, cy); p.close()
    c.drawPath(p, paint("#DDE6F0", a * 0.85))
    c.drawPath(p, paint("#9AA3AD", a, stroke=4))


def granito(c, cx, cy, w, h, a, zoom=1.0):
    if a <= 0:
        return
    rnd = random.Random(5)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, "#C9C3BC", a, shadow=True)
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), True)
    for k in range(int(260 * min(1.0, w * h / 200000))):
        x, y = cx + rnd.uniform(-0.5, 0.5) * w, cy + rnd.uniform(-0.5, 0.5) * h
        col = ["#2B2B2D", "#F5F2EE", "#D9A6A0"][k % 3]
        rr = rnd.uniform(3, 9) * zoom
        c.drawOval(skia.Rect.MakeXYWH(x - rr, y - rr * 0.7, 2 * rr, 1.4 * rr), paint(col, a))
    c.restore()


def soro(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    rrect(c, cx - 80 * s, cy - 120 * s, 160 * s, 220 * s, 40 * s, "#E3F0FB", a, shadow=True, stroke=3, stroke_color="#9AC1E8")
    rrect(c, cx - 70 * s, cy - 40 * s, 140 * s, 110 * s, 30 * s, WATER, a * 0.5)
    rrect(c, cx - 14 * s, cy + 100 * s, 28 * s, 50 * s, 6 * s, "#9AC1E8", a)
    c.drawCircle(cx, cy - 140 * s, 14 * s, paint("#9AC1E8", a, stroke=4))
    text_mid(c, "NaCl 0,9%", cx, cy - 80 * s, 22 * s, "black", BLUE, a)


def panela(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    g = skia.GradientShader.MakeLinear([skia.Point(cx - 150 * s, 0), skia.Point(cx + 150 * s, 0)],
                                       [skia.Color4f(0.62, 0.65, 0.69, a), skia.Color4f(0.92, 0.93, 0.95, a),
                                        skia.Color4f(0.58, 0.61, 0.65, a)])
    p = skia.Paint(AntiAlias=True); p.setShader(g)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 150 * s, cy - 70 * s, 300 * s, 140 * s), 20 * s, 20 * s), p)
    rrect(c, cx - 165 * s, cy - 80 * s, 330 * s, 20 * s, 10 * s, "#B8BCC2", a)
    rrect(c, cx + 160 * s, cy - 60 * s, 120 * s, 22 * s, 11 * s, "#3A3A3C", a)


def barra_ar(c, x, y, w, a, t, t0):
    """barra de composição do ar: 78% N₂, 21% O₂, 1% outros"""
    if a <= 0:
        return
    parts = [(0.78, V.EL["N"], "78% N₂"), (0.21, V.EL["O"], "21% O₂"), (0.01, "#8E8E93", "1%")]
    xx = x
    for k, (f, col, lab) in enumerate(parts):
        g = ease_io(prog(t, t0 + 0.6 * k, 0.7))
        ww = w * f * g
        rrect(c, xx, y, max(ww, 2), 70, 8, col, a * (0.9 if k < 2 else 1))
        if k < 2 and g > 0.5:
            text_mid(c, lab, xx + ww / 2, y + 35, 28, "black", "#FFFFFF", a)
        xx += w * f
    text(c, "1% outros", x + w + 10, y + 46, 22, "bold", INK2, a * ep(t, t0 + 1.6, 0.4), align="left")


def gas_mix(c, cx, cy, w, h, a, t, extra=None):
    """caixa de ar: moléculas de N₂ e O₂ misturadas por igual (extra: 'fuligem' ou 'gotas')"""
    if a <= 0:
        return
    rnd = random.Random(9)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, "#F4F8FD", a, stroke=3, stroke_color="#C9DAEE")
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 20, 20), True)
    for k in range(24):
        x0, y0 = rnd.uniform(-0.45, 0.45) * w, rnd.uniform(-0.42, 0.42) * h
        x = cx + x0 + math.sin(t * 0.7 + k * 1.7) * 10
        y = cy + y0 + math.cos(t * 0.6 + k * 2.3) * 8
        V.mol(c, "O2" if k % 5 == 0 else "N2", x, y, 9, a, label=False)
        if k % 5 == 0:
            pass
    if extra == "fuligem":
        for k in range(30):
            x, y = cx + rnd.uniform(-0.45, 0.45) * w, cy + rnd.uniform(-0.42, 0.42) * h
            c.drawCircle(x + math.sin(t + k) * 6, y, rnd.uniform(5, 9), paint("#2B2B2D", a))
    elif extra == "gotas":
        for k in range(22):
            x, y = cx + rnd.uniform(-0.45, 0.45) * w, cy + rnd.uniform(-0.42, 0.42) * h
            p = skia.Path()
            rr = rnd.uniform(7, 11)
            p.moveTo(x, y - rr * 1.6); p.quadTo(x + rr, y, x, y + rr); p.quadTo(x - rr, y, x, y - rr * 1.6)
            c.drawPath(p, paint("#4C8FE0", a))
    c.restore()


def blocos_liga(c, cx, cy, a, f):
    """dois metais (cobre e estanho) derretendo numa barra de cor única"""
    if a <= 0:
        return
    cu, sn = "#C77B43", "#A7ADB4"
    if f < 0.5:
        g = f / 0.5
        for k, col in enumerate((cu, sn)):
            x = cx + (-130 if k == 0 else 30) + (50 if k == 0 else -50) * g
            hh = 120 * (1 - 0.5 * g)
            rrect(c, x, cy + 60 - hh, 100, hh, 10 * (1 + g * 3), col, a)
        text(c, "cobre", cx - 80, cy + 110, 26, "bold", INK2, a * (1 - g))
        text(c, "estanho", cx + 80, cy + 110, 26, "bold", INK2, a * (1 - g))
    else:
        g = (f - 0.5) / 0.5
        col = mix(mix(cu, sn, 0.35), "#B08D57", g)
        rrect(c, cx - 140, cy + 60 - 60 * (1 + 0.3 * g), 280, 60 * (1 + 0.3 * g), 16, col, a, shadow=True)
        text(c, "bronze", cx, cy + 110, 26, "black", INK, a * g)


def quilates(c, cx, cy, a, t, t0, t1):
    """24 quadradinhos; 18 acendem em dourado"""
    if a <= 0:
        return
    s = 62
    for k in range(24):
        i, j = k % 6, k // 6
        x, y = cx - 3 * s + i * s, cy - 2 * s + j * s
        g = ep(t, t1 + 0.07 * k, 0.25) if k < 18 else 0
        rrect(c, x + 4, y + 4, s - 8, s - 8, 8, mix("#E5E5EA", GOLD, g), a * ep(t, t0 + 0.02 * k, 0.3))
        if g > 0.5:
            text_mid(c, "Au", x + s / 2, y + s / 2, 20, "black", "#7A5A12", a * g)


# ======================================================================
# gancho, promessa, pré-requisitos
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "QUÍMICA ENEM", "MISTURAS · EPISÓDIO 3", BLUE)
    items = [("01.a", "AR"), ("01.b", "ÁGUA MINERAL"), ("01.c", "OURO 18 QUILATES")]
    ae = ep(t, C["01.e"], 0.5)
    for k, (cue, s) in enumerate(items):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 500
        card(c, x, 190 + dy, 440, 460, a)
        if k == 0:
            gas_mix(c, x + 220, 400 + dy, 300, 240, a, t)
        elif k == 1:
            V2.garrafa(c, x + 220, 420 + dy, a)
        else:
            V2.anel(c, x + 220, 440 + dy, a)
        text(c, s, x + 220, 610 + dy, 32, "black", INK, a)
        if ae > 0:
            check_icon(c, x + 390, 240 + dy, 26, ae * ep(t, C["01.e"] + 0.3 * k, 0.3), RED, "x")
    ad = ep(t, C["01.d"], 0.5)
    pill(c, "substância pura?", W / 2, 720, BLUE, size=32, a=ad * (1 - ae), anchor="center", bounds=(0, 1920))
    pill(c, "NENHUM dos três", W / 2, 720, RED, size=32, a=ae, anchor="center", bounds=(0, 1920))
    af = ep(t, C["01.f"], 0.5)
    pill(c, "pegadinha clássica do ENEM", W / 2, 800, AMBER, size=28, fg=INK, a=af, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    head(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CLASSIFICAR", GREEN)
    ab = ep(t, C["02.b"], 0.5)
    for k, (s, col) in enumerate(COLS):
        a, dy = rise(t, C["02.b"] + 0.7 * k)
        if a <= 0:
            continue
        x = 330 + k * 630
        card(c, x - 270, 230 + dy, 540, 420, a)
        rrect(c, x - 270, 230 + dy, 540, 70, 28, col, a * 0.16)
        text_mid(c, s, x, 266 + dy, 34, "black", col if col != AMBER else "#B07A00", a)
        vidro(c, x, 600 + dy, 170, 240, a, ["destilada", "acucar", "oleo"][k])
    pill(c, "um ritual de 2 perguntas", W / 2, 760, PURPLE, size=30, a=ep(t, C["02.c"], 0.5), anchor="center", bounds=(0, 1920))


def b_prereq(c, t, C, B):
    head(c, t, B["start"], "LEMBRETE DO EPISÓDIO 1", "PURA × MISTURA", BLUE)
    card(c, *CARD_R)
    for side, (cue, titulo, corpo) in enumerate((("03.a", "SUBSTÂNCIA PURA", "1 tipo de montagem"),
                                                   ("03.b", "MISTURA", "2 ou mais substâncias juntas"))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 240 + side * 760
        V.bequer(c, x, 230, 520, 360, a, WATER, 0.86)
        rnd = random.Random(side)
        for j in range(3):
            for i in range(4):
                xx, yy = x + 80 + i * 120 + (40 if j % 2 else 0), 320 + j * 90
                if side == 1 and (i + j) % 2 == 1 and t > C["03.c"] - 0.2:
                    k_ = ep(t, C["03.c"], 0.4)
                    for q, (dx, dy_) in enumerate(((-14, 0), (14, 0), (0, -14), (0, 14))):
                        V.peca(c, xx + dx, yy + dy_, 10, "C" if q % 2 else "O", a * k_, label=False)
                else:
                    V.mol(c, "H2O", xx, yy, 18, a, label=False)
        V.defbox(c, titulo, corpo, x + 260, 720, a, w=600)
    pill(c, "água + açúcar", 1260, 190, INK2, size=24, a=ep(t, C["03.c"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# blocos a-b: fase, homogênea, heterogênea
# ======================================================================

def b_fase(c, t, C, B):
    head(c, t, B["start"], "PALAVRA NOVA", "FASE", BLUE)
    card(c, *CARD_R)
    V.defbox(c, "FASE", "cada parte com a mesma aparência do começo ao fim", 1150, 300, ep(t, C["04.a"], 0.5), w=900)
    ab = ep(t, C["04.b"], 0.5)
    vidro(c, 480, 760, 300, 480, ep(t, C["04.t"], 0.5), "oleo")
    if ab > 0:
        for k, (y, s, col) in enumerate(((440, "fase 1: óleo", "#B07A00"), (600, "fase 2: água", BLUE))):
            ak = ab * ep(t, C["04.b"] + 1.2 * k, 0.4)
            arrow(c, 820, y, 660, y, col, ak, 4, 16)
            text(c, s, 840, y + 12, 34, "black", col, ak, align="left")
    pill(c, "contar fases = contar as partes diferentes que você vê", 1150, 760, GREEN, size=26, a=ep(t, C["04.c"], 0.5),
         anchor="center", bounds=(0, 1920))


def b_homogenea(c, t, C, B):
    head(c, t, B["start"], "MISTURA", "HOMOGÊNEA", BLUE)
    card(c, *LEFT)
    f = ease_io(prog(t, C["05.a"], 1.6))
    vidro(c, 400, 700, 280, 420, 1.0, "acucar", t, f)
    if t < C["05.a"] + 1.6:
        x = 400 + 60 * math.sin((t - C["05.t"]) * 6)
        line(c, x, 260, 400 + (x - 400) * 0.4, 560, "#C0C4CA", ep(t, C["05.t"], 0.4), 10)
    ab = ep(t, C["05.b"], 0.5)
    pill(c, "UMA coisa só", 400, 760, INK2, size=28, a=ab, anchor="center", bounds=(0, 1920))
    V.defbox(c, "MISTURA HOMOGÊNEA", "aspecto uniforme · 1 fase", 860, 380, ep(t, C["05.c"], 0.5), w=520)
    text(c, "homo = igual por inteiro", 860, 560, 32, "black", BLUE, ep(t, C["05.d"], 0.5))
    quadro(c, t, C)


def b_solucao(c, t, C, B):
    head(c, t, B["start"], "UM APELIDO", "SOLUÇÃO", BLUE)
    card(c, *LEFT)
    V.defbox(c, "SOLUÇÃO = mistura homogênea", "", 670, 260, ep(t, C["06.a"], 0.5), w=760)
    ab = ep(t, C["06.b"], 0.5)
    vidro(c, 420, 720, 240, 320, ab, "sal", t, ease_io(prog(t, C["06.b"], 1.4)))
    text(c, "água com sal", 420, 770, 30, "black", INK, ab)
    ac = ep(t, C["06.c"], 0.5)
    gas_mix(c, 900, 560, 340, 260, ac, t)
    text(c, "ar (já já)", 900, 770, 30, "black", INK, ac)
    quadro(c, t, C)


def b_heterogenea(c, t, C, B):
    head(c, t, B["start"], "MISTURA", "HETEROGÊNEA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    salada(c, 500, 460, aa, 1.4)
    text(c, "salada de frutas", 500, 720, 34, "black", INK, aa)
    pill(c, "você vê os pedaços", 500, 780, INK2, size=26, a=ep(t, C["07.a"] + 1.4, 0.5), anchor="center", bounds=(0, 1920))
    V.defbox(c, "MISTURA HETEROGÊNEA", "2 ou mais fases que dá para distinguir", 1250, 380, ep(t, C["07.b"], 0.5), w=700)
    text(c, "hetero = diferente", 1250, 560, 34, "black", BLUE, ep(t, C["07.c"], 0.5))


def b_hetero_ex(c, t, C, B):
    head(c, t, B["start"], "HETEROGÊNEAS", "NO DIA A DIA", BLUE)
    card(c, *LEFT)
    aa = ep(t, C["08.a"], 0.5)
    vidro(c, 360, 680, 200, 290, aa, "oleo")
    text(c, "água e óleo", 360, 725, 30, "black", INK, aa)
    V.defbox(c, "IMISCÍVEIS", "não se misturam", 360, 255, ep(t, C["08.a"] + 1.8, 0.5), w=380)
    ab = ep(t, C["08.b"], 0.5)
    zoom = ep(t, C["08.b"] + 1.4, 0.8)
    granito(c, 860, 470, 340, 300, ab, 1 + zoom)
    text(c, "granito", 860, 670, 30, "black", INK, ab)
    text(c, "quartzo · feldspato · mica", 860, 715, 24, "bold", INK2, ep(t, C["08.b"] + 2.6, 0.5))
    pill(c, "2 ou mais fases → HETEROGÊNEA", 670, 775, AMBER, size=24, fg=INK, a=ep(t, C["08.c"], 0.5), anchor="center", bounds=(0, 1920))
    quadro(c, t, C)


RITUAL = [("é UMA substância só?", "sim → SUBSTÂNCIA PURA"), ("mais de uma → MISTURA:", "quantas FASES eu vejo?"),
          ("1 fase → HOMOGÊNEA", "2 ou mais → HETEROGÊNEA")]


def ritual(c, t, x, y, w, a, cues=None, dy=150, ativo=None, size=34):
    if a <= 0:
        return
    card(c, x, y, w, dy * 3 + 80, a)
    text(c, "RITUAL", x + 36, y + 56, 26, "black", PURPLE, a, align="left")
    for k, (s1, s2) in enumerate(RITUAL):
        ak = a * (ep(t, cues[k], 0.45) if cues else 1.0)
        if ak <= 0:
            continue
        yy = y + 80 + k * dy
        if ativo == k:
            rrect(c, x + 14, yy, w - 28, dy - 14, 16, PURPLE, ak * 0.12)
        badge_num(c, k + 1, x + 60, yy + (dy - 14) / 2, ak, 26, bg=PURPLE)
        text(c, s1, x + 110, yy + (dy - 14) / 2 - 4, size, "black", INK, ak, align="left")
        text(c, s2, x + 110, yy + (dy - 14) / 2 + size, size * 0.8, "bold", PURPLE, ak, align="left")


def b_ritual(c, t, C, B):
    head(c, t, B["start"], "O RITUAL", "DUAS PERGUNTAS", PURPLE)
    cues = [C["09.a"], C["09.b"], C["09.c"]]
    k = None
    for i, cu in enumerate(cues):
        if t >= cu:
            k = i
    ritual(c, t, 160, 170, 1000, ep(t, C["09.t"], 0.5), cues, ativo=k)
    ad = ep(t, C["09.d"], 0.5)
    card(c, 1220, 170, 540, 530, ep(t, C["09.t"], 0.5))
    lupa(c, 1490, 430, 170, ad, "leite", t, ad)
    text(c, "vale olhar até", 1490, 250, 30, "black", INK, ep(t, C["09.t"], 0.5) * (1 - ad) + ad)
    text(c, "no MICROSCÓPIO", 1490, 660, 32, "black", GREEN, ad)


# ======================================================================
# blocos c-d: gases, fumaça e neblina
# ======================================================================

def b_gases(c, t, C, B):
    head(c, t, B["start"], "E O AR?", "MISTURA DE GASES", BLUE)
    card(c, *LEFT)
    aa = ep(t, C["10.a"], 0.5)
    barra_ar(c, 200, 220, 760, aa, t, C["10.a"])
    pill(c, "várias substâncias → MISTURA", 580, 350, INK2, size=26, a=ep(t, C["10.b"], 0.5), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["10.c"], 0.5)
    gas_mix(c, 580, 560, 620, 260, ac, t)
    if ac > 0:
        text(c, "camadas? nunca", 580, 470, 30, "black", INK, ac * (1 - ep(t, C["10.d"], 0.4)))
    regra(c, "TODA mistura de gases é HOMOGÊNEA", 670, 760, ep(t, C["10.d"], 0.5), 30, PURPLE, w=880)
    quadro(c, t, C)


def regra(c, s, cx, cy, a, size=34, col=None, w=None):
    V.regra(c, s, cx, cy, a, size, col, w)


def b_fumaca(c, t, C, B):
    head(c, t, B["start"], "A EXCEÇÃO APARENTE", "FUMAÇA E NEBLINA", AMBER)
    card(c, *LEFT)
    for k, (cue, s, ex, sub) in enumerate((("11.a", "FUMAÇA", "fuligem", "pedacinhos SÓLIDOS"),
                                           ("11.b", "NEBLINA", "gotas", "gotinhas LÍQUIDAS"))):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 460
        gas_mix(c, x, 370 + dy, 380, 280, a, t, ex)
        text(c, s, x, 560 + dy, 34, "black", INK, a)
        text(c, sub + " no ar", x, 603 + dy, 26, "bold", INK2, a)
    pill(c, "não são só gases → HETEROGÊNEAS", 630, 670, AMBER, size=26, fg=INK, a=ep(t, C["11.c"], 0.5), anchor="center", bounds=(0, 1920))
    regra(c, "mistura SÓ de gases → homogênea", 630, 745, ep(t, C["11.d"], 0.5), 26, PURPLE, w=700)
    quadro(c, t, C)


# ======================================================================
# bloco e: leite e sangue
# ======================================================================

def _micro(c, t, C, sid, kind, nome, lab_fases):
    card(c, *LEFT)
    a0 = ep(t, C[f"{sid}.t"], 0.5)
    vidro(c, 330, 700, 240, 360, a0, kind)
    text(c, nome, 330, 760, 32, "black", INK, a0)
    aa = ep(t, C[f"{sid}.a"], 0.5)
    f = ease_io(prog(t, C[f"{sid}.a"] + 0.4, 1.4))
    if aa > 0:
        line(c, 400, 420, 610, 450, "#8E8E93", aa, 3, dash=[8, 8])
        c.drawCircle(400, 420, 18, paint("#8E8E93", aa, stroke=3))
    lupa(c, 820, 470, 215, aa, kind, t, f)
    pill(c, lab_fases, 820, 720, INK2, size=24, a=ep(t, C[f"{sid}.b"], 0.5), anchor="center", bounds=(0, 1920))


def b_leite(c, t, C, B):
    head(c, t, B["start"], "O LEITE É", "HOMOGÊNEO?", BLUE)
    _micro(c, t, C, "12", "leite", "leite", "gordura + líquido: 2 fases")
    pill(c, "HETEROGÊNEO", 820, 200, AMBER, size=28, fg=INK, a=ep(t, C["12.c"], 0.5), anchor="center", bounds=(0, 1920))
    pill(c, "às vezes, só no microscópio", 630, 790, GREEN, size=26, a=ep(t, C["12.d"], 0.5), anchor="center", bounds=(0, 1920))
    quadro(c, t, C)


def b_sangue(c, t, C, B):
    head(c, t, B["start"], "E O SANGUE?", "MESMA COISA", BLUE)
    _micro(c, t, C, "13", "sangue", "sangue", "glóbulos vermelhos + plasma")
    pill(c, "HETEROGÊNEO", 820, 200, AMBER, size=28, fg=INK, a=ep(t, C["13.c"], 0.5), anchor="center", bounds=(0, 1920))
    quadro(c, t, C)


# ======================================================================
# blocos f-g: ligas metálicas e quilate
# ======================================================================

def b_ligas(c, t, C, B):
    head(c, t, B["start"], "METAL PODE SER", "MISTURA?", BLUE)
    card(c, *LEFT)
    aa = ep(t, C["14.a"], 0.5)
    blocos_liga(c, 380, 380, aa, ease_io(prog(t, C["14.a"] + 0.6, 2.4)))
    V.defbox(c, "LIGA METÁLICA", "metal + outros elementos, endurece por inteiro", 670, 620, ep(t, C["14.b"], 0.5), w=900)
    ac = ep(t, C["14.c"], 0.5)
    panela(c, 900, 360, ac, 0.75)
    text(c, "inox: brilho igual", 900, 470, 26, "bold", INK2, ac)
    pill(c, "1 fase → mistura HOMOGÊNEA", 670, 760, BLUE, size=26, a=ep(t, C["14.d"], 0.5), anchor="center", bounds=(0, 1920))
    quadro(c, t, C)


LIGAS = [("15.a", "AÇO", "ferro + carbono"), ("15.b", "AÇO INOX", "ferro, carbono, cromo, níquel"),
         ("15.c", "BRONZE", "cobre + estanho"), ("15.d", "LATÃO", "cobre + zinco"), ("15.e", "OURO 18 K", "ouro + cobre + prata")]


def b_ligas_ex(c, t, C, B):
    head(c, t, B["start"], "LIGAS METÁLICAS", "SOLUÇÕES SÓLIDAS", BLUE)
    card(c, *LEFT)
    V.defbox(c, "SOLUÇÃO SÓLIDA", "uma solução que é sólida", 670, 240, ep(t, C["15.t"], 0.5), w=620)
    for k, (cue, s1, s2) in enumerate(LIGAS):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 360 + k * 82 + dy
        rrect(c, 200, y - 34, 940, 70, 16, BLUE, a * 0.07)
        rrect(c, 216, y - 20, 42, 42, 10, [  "#8C9096", "#C9CDD2", "#B08D57", "#D4B24C", GOLD][k], a)
        text(c, s1, 280, y + 12, 32, "black", INK, a, align="left")
        text(c, s2, 540, y + 10, 28, "bold", INK2, a, align="left")
    quadro(c, t, C)


def b_quilate(c, t, C, B):
    head(c, t, B["start"], "O QUE É", "QUILATE?", BLUE)
    card(c, *CARD_R)
    V.defbox(c, "QUILATE", "quanto de ouro há na peça, em 24 partes", 520, 270, ep(t, C["16.a"], 0.5), w=680)
    quilates(c, 520, 560, ep(t, C["16.b"], 0.5), t, C["16.b"], C["16.c"])
    ac = ep(t, C["16.c"], 0.5)
    text(c, "18 de ouro · 6 de outros metais", 520, 790, 30, "black", INK, ac)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        frac(c, "18", "24", 1150, 400, 90, INK, ad, "black")
        text_mid(c, "= 75%", 1380, 425, 90, "black", "#B07A00", ad)
        text(c, "de ouro", 1300, 520, 34, "black", INK2, ad)
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        V2.anel(c, 1140, 680, ae)
        text(c, "24 k = ouro puro, mas MOLE", 1500, 650, 28, "black", INK, ae)
        text(c, "outros metais → resistência", 1500, 700, 26, "bold", GREEN, ae)


# ======================================================================
# bloco h: enganos do cotidiano
# ======================================================================

def b_enganos(c, t, C, B):
    head(c, t, B["start"], "DOIS ENGANOS", "DO COTIDIANO", AMBER)
    card(c, *LEFT)
    aa, dy = rise(t, C["17.a"])
    if aa > 0:
        gas_mix(c, 380, 400 + dy, 400, 280, aa, t)
        text(c, "\"ar puro\"", 380, 600 + dy, 34, "black", INK, aa)
        text(c, "= ar LIMPO, não substância pura", 380, 645 + dy, 24, "bold", "#B07A00", aa)
    ab, dy2 = rise(t, C["17.b"])
    if ab > 0:
        V2.garrafa(c, 800, 420 + dy2, ab)
        card(c, 900, 260 + dy2, 260, 240, ab)
        text(c, "RÓTULO", 1030, 300 + dy2, 22, "black", BLUE, ab)
        for k, s in enumerate(("cálcio", "magnésio", "sódio")):
            text(c, s, 1030, 350 + dy2 + k * 44, 28, "black", INK, ab * ep(t, C["17.b"] + 0.8 + 0.4 * k, 0.4))
        text(c, "sais dissolvidos", 900, 600 + dy2, 28, "black", INK2, ab)
    pill(c, "água mineral = MISTURA HOMOGÊNEA", 670, 760, BLUE, size=26, a=ep(t, C["17.c"], 0.5), anchor="center", bounds=(0, 1920))
    quadro(c, t, C)


def b_destilada(c, t, C, B):
    head(c, t, B["start"], "EXISTE", "ÁGUA PURA?", BLUE)
    card(c, *LEFT)
    aa = ep(t, C["18.a"], 0.5)
    vidro(c, 380, 640, 240, 340, aa, "destilada")
    text(c, "água destilada", 380, 700, 32, "black", INK, aa)
    pill(c, "a que mais se aproxima de PURA", 380, 760, GREEN, size=24, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["18.b"], 0.5)
    soro(c, 880, 430, ab, 1.1)
    text(c, "soro fisiológico", 880, 640, 32, "black", INK, ab)
    text(c, "água + 0,9% de sal", 880, 690, 28, "bold", INK2, ab)
    pill(c, "MISTURA HOMOGÊNEA", 880, 760, BLUE, size=24, a=ep(t, C["18.c"], 0.5), anchor="center", bounds=(0, 1920))
    quadro(c, t, C)


# ======================================================================
# recapitulação e erros
# ======================================================================

FRASES = ["Uma fase: homogênea. Duas ou mais: heterogênea.",
          "Mistura de gases é sempre homogênea.",
          "Liga metálica é mistura, não substância pura."]


def b_recap(c, t, C, B):
    sid = "19" if B["start"] < C["31"] - 1 else "31"
    head(c, t, B["start"], "AS 3 FRASES", "PARA GUARDAR", GREEN)
    card(c, *CARD_R)
    for k, (cue, col) in enumerate((("a", BLUE), ("b", GREEN), ("c", PURPLE))):
        a, d = rise(t, C[f"{sid}.{cue}"])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 230, y - 16, a, 32, bg=col)
        text(c, FRASES[k], 290, y, 48, "black", INK, a, align="left")


def b_erro1(c, t, C, B):
    def ex(c, k, x, y, cw, a):
        if k == 2:
            gas_mix(c, x + cw / 2, y + 470, 260, 120, a, t)
    head(c, t, B["start"], "ERRO 1", "\"O AR É PURO\"", RED)
    V.erro_tiles(c, t, [(C["20.a"], "O ERRO", ["!o ar é", "!substância pura"], RED),
                        (C["20.b"], "POR QUE PARECE CERTO", ["invisível, uniforme", "e a gente fala", "\"ar puro\""], AMBER),
                        (C["20.c"], "A CORREÇÃO", ["vários gases", "!MISTURA", "!HOMOGÊNEA"], GREEN)], ex)


def b_erro2(c, t, C, B):
    def ex(c, k, x, y, cw, a):
        if k == 2:
            c.save(); c.translate(x + cw / 2, y + 470); c.scale(0.6, 0.6)
            V2.garrafa(c, 0, 0, a)
            c.restore()
    head(c, t, B["start"], "ERRO 2", "\"ÁGUA MINERAL É PURA\"", RED)
    V.erro_tiles(c, t, [(C["21.a"], "O ERRO", ["!água mineral", "!é pura"], RED),
                        (C["21.b"], "POR QUE PARECE CERTO", ["transparente e", "vem da natureza"], AMBER),
                        (C["21.c"], "A CORREÇÃO", ["sais dissolvidos", "!MISTURA", "!HOMOGÊNEA"], GREEN)], ex)


def b_erro3(c, t, C, B):
    def ex(c, k, x, y, cw, a):
        if k == 2:
            lupa(c, x + cw / 2 - 90, y + 470, 70, a, "leite", t, 1)
            lupa(c, x + cw / 2 + 90, y + 470, 70, a, "sangue", t, 1)
    head(c, t, B["start"], "ERRO 3", "\"LEITE E SANGUE SÃO HOMOGÊNEOS\"", RED)
    V.erro_tiles(c, t, [(C["22.a"], "O ERRO", ["!leite e sangue", "!são homogêneos"], RED),
                        (C["22.b"], "POR QUE PARECE CERTO", ["a olho nu", "parecem uma", "coisa só"], AMBER),
                        (C["22.c"], "A CORREÇÃO", ["microscópio:", "!HETEROGÊNEOS"], GREEN)], ex)


def b_erro4(c, t, C, B):
    def ex(c, k, x, y, cw, a):
        if k == 2:
            c.save(); c.translate(x + cw / 2, y + 480); c.scale(0.55, 0.55)
            quilates(c, 0, 0, a, 1e9, 0, 0)
            c.restore()
    head(c, t, B["start"], "ERRO 4", "\"OURO 18 K É PURO\"", RED)
    V.erro_tiles(c, t, [(C["23.a"], "O ERRO", ["!ouro 18 k", "!é ouro puro"], RED),
                        (C["23.b"], "POR QUE PARECE CERTO", ["é ouro de verdade,", "de joalheria"], AMBER),
                        (C["23.c"], "A CORREÇÃO", ["18 de 24 partes", "!LIGA: MISTURA"], GREEN)], ex)


# ======================================================================
# exercício rápido
# ======================================================================

EXER = [("24.a", "25.a", "água com gás", "gas", 1), ("24.b", "25.b", "aço", "aco", 1),
        ("24.c", "25.c", "água e areia", "areia", 2), ("24.d", "25.d", "gás oxigênio", "o2", 0)]


def b_exercicio(c, t, C, B):
    head(c, t, B["start"], "SUA VEZ", "PAUSE E CLASSIFIQUE", GREEN)
    for k, (cue, rcue, nome, kind, col) in enumerate(EXER):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 400
        card(c, x, 190 + dy, 360, 520, a)
        cx = x + 180
        if kind == "gas":
            vidro(c, cx, 460 + dy, 150, 200, a, "agua")
            rrect(c, cx - 30, 240 + dy, 60, 30, 6, BLUE, a)
            text(c, "fechada", cx, 500 + dy, 22, "bold", INK2, a)
        elif kind == "aco":
            rrect(c, cx - 110, 330 + dy, 220, 90, 14, "#8C9096", a, shadow=True)
            rrect(c, cx - 100, 340 + dy, 200, 14, 7, "#FFFFFF", a * 0.4)
        elif kind == "areia":
            vidro(c, cx, 480 + dy, 170, 230, a, "areia")
        else:
            V.cilindro(c, cx, 480 + dy, a, 0.7)
        text(c, nome, cx, 560 + dy, 32, "black", INK, a)
        ar = ep(t, C[rcue], 0.5) if rcue in C else 0
        text(c, "?", cx, 640 + dy, 60, "black", LIGHT, a * (1 - ar))
        if ar > 0:
            s, cc = COLS[col]
            pill(c, s, cx, 640 + dy, cc, size=26, fg=INK if cc == AMBER else None, a=ar, anchor="center", bounds=(0, 1920))
    V.pause_badge(c, W / 2 - 170, 740, ep(t, C["24.p"], 0.5) * (1 - prog(t, C["25.t"] - 0.3, 0.4)))


# ======================================================================
# questão 7
# ======================================================================

MATS = [("28.m1", "água mineral", 1, "água + sais"), ("28.m2", "ouro 18 quilates", 1, "ouro, cobre, prata"),
        ("28.m3", "gás oxigênio", 0, "só O₂"), ("29.m4", "ar filtrado", 1, "o filtro não separa os gases"),
        ("29.m5", "granito", 2, "3 minerais visíveis")]
ALTS = [("A", "apenas a água mineral", "30.a", "água mineral não é pura"),
        ("B", "apenas o ouro 18 quilates", "30.b", "18 k é liga"),
        ("C", "apenas o gás oxigênio", None, ""),
        ("D", "a água mineral e o gás oxigênio", "30.d", "ARMADILHA: tem sais"),
        ("E", "o ouro 18 quilates e o granito", "30.b", "liga e heterogênea")]
ALT_CUE = ["27.a", "27.b", "27.c", "27.d", "27.e"]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO ESTILO ENEM", "QUAL É SUBSTÂNCIA PURA?", BLUE)
    card(c, 140, 160, 860, 640)
    pill(c, "QUESTÃO", 170, 204, BLUE, size=22, bounds=(0, 1920))
    text(c, "Materiais: água mineral, ouro 18 quilates,", 180, 280, 28, "black", INK, ep(t, C["26.e1"], 0.5), align="left")
    text(c, "gás oxigênio, ar filtrado e granito.", 180, 322, 28, "black", INK, ep(t, C["26.e1"], 0.5), align="left")
    text(c, "Entre eles, é substância pura:", 180, 380, 28, "black", INK2, ep(t, C["26.e2"], 0.5), align="left")
    aok = ep(t, C["29.ok"], 0.5)
    for k, (L, s, cue_x, why) in enumerate(ALTS):
        a, d = rise(t, C[ALT_CUE[k]])
        y = 460 + k * 64 + d
        ok = cue_x is None
        if ok and aok > 0:
            rrect(c, 170, y - 40, 800, 58, 12, GREEN, 0.15 * aok)
        if L == "D":
            rrect(c, 170, y - 40, 800, 58, 12, AMBER, 0.16 * ep(t, C["30.d"], 0.4))
        badge_num(c, L, 205, y - 12, a, 21, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cue_x], 0.4) if cue_x else 0
        text(c, s, 245, y, 28, "black", INK, a * (1 - 0.55 * ax), align="left")
        if ax > 0:
            strike(c, 240, y - 10, 250 + text_w(s, "black", 28), y - 10, ax, RED, ax)
            text(c, why, 960, y - 2, 21, "black", RED if L != "D" else "#B07A00", ax, align="right")
    V.pause_badge(c, 1230, 420, ep(t, C["27.p"], 0.5) * (1 - prog(t, C["28.t"] - 0.3, 0.4)))
    ar = ep(t, C["28.t"], 0.5)
    sol_card(c, 1040, 160, 740, 640, ar)
    if ar <= 0:
        return
    for k, s in enumerate(("1 · uma substância só?", "2 · quantas fases?")):
        pill(c, s, 1200 + k * 340, 262, PURPLE, size=22, a=ar, anchor="center", bounds=(0, 1920))
    for k, (cue, nome, col, why) in enumerate(MATS):
        a, dy = rise(t, C[cue])
        if a <= 0:
            continue
        y = 340 + k * 86 + dy
        rrect(c, 1070, y - 36, 680, 74, 14, COLS[col][1], a * 0.10)
        text(c, nome, 1090, y - 2, 28, "black", INK, a, align="left")
        text(c, why, 1090, y + 28, 20, "bold", INK2, a, align="left")
        s, cc = COLS[col]
        pill(c, s, 1660, y, cc, size=20, fg=INK if cc == AMBER else None, a=a, anchor="center", bounds=(0, 1920))
    pill(c, "só o gás oxigênio → RESPOSTA C", 1410, 770, GREEN, size=26, a=ep(t, C["29.r"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    head(c, t, B["start"], "PRÓXIMO EPISÓDIO", "FASES E COMPONENTES", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["32.t"], 0.5)
    vidro(c, 620, 720, 320, 460, a0, "agua")
    for k, (dx, dy) in enumerate(((-60, -330), (40, -360), (-10, -300))):
        ak = a0 * ep(t, C["32.t"] + 0.6 + 0.3 * k, 0.4)
        rrect(c, 620 + dx - 40, 720 + dy - 40, 80, 80, 14, "#E8F4FC", ak, stroke=3, stroke_color="#9AC1E8")
    aa = ep(t, C["32.a"], 0.5)
    text(c, "quantas fases?", 1220, 360, 50, "black", INK, aa)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        text(c, "4?", 1220, 500, 110, "black", RED, ab)
        strike(c, 1150, 470, 1290, 470, ab, RED, ease_io(prog(t, C["32.b"] + 0.6, 0.4)))
    pill(c, "EPISÓDIO 4: FASES E COMPONENTES", 1220, 680, PURPLE, size=30, a=ep(t, C["32.c"], 0.5), anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Você achava que a água mineral era pura?")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, fase=b_fase, homogenea=b_homogenea, solucao=b_solucao,
              heterogenea=b_heterogenea, hetero_ex=b_hetero_ex, ritual=b_ritual, gases=b_gases, fumaca=b_fumaca,
              leite=b_leite, sangue=b_sangue, ligas=b_ligas, ligas_ex=b_ligas_ex, quilate=b_quilate, enganos=b_enganos,
              destilada=b_destilada, recap=b_recap, erro1=b_erro1, erro2=b_erro2, erro3=b_erro3, erro4=b_erro4,
              exercicio=b_exercicio, questao=b_questao, ponte=b_ponte, cta=b_cta)
