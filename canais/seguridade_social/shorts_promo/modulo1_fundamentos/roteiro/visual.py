"""Visual do Short promocional — Seguridade Social, Módulo 1 (Fundamentos) no Estudativo. 1080x1920 (render.py --vertical).
Paleta do pedido: azul-escuro, branco e amarelo; os três pilares mantêm as cores fixas do canal (ESTILO.md).
Zona útil y=200–1560 (a interface do Shorts cobre o rodapé e a lateral direita). Cenas ilustrativas desenhadas aqui
(estudante, mesa, apostila, questão); o único material real é a capa da Aula 1 (001_conceito_e_tripe)."""
import math
from functools import lru_cache
from pathlib import Path
import numpy as np
import skia
import motor
import tech
from motor import *  # noqa
from tech import blur_paint, glow_text, hash01  # noqa

motor.PESOS["mono"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono"
motor.PESOS["monob"] = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold"

ARQUIVO_FINAL = "seguridade_short_modulo1_fundamentos.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o gancho aparece no primeiro quadro, sem fade
SOM = dict(intro=False, ganho_trilha=0.34, lufs=-14, bpm=118, sfx={
    "01.a": ["impact", "whoosh@+0.9"], "01.b": "confirm",
    "02.a": ["pop", "pop@+0.6", "pop@+1.2", "deny@+1.8"], "02.b": "lock",
    "03.a": "shimmer", "03.b": "data", "03.c": "impact",
    "04.a": "confirm", "04.b": ["confirm", "confirm@+0.5"],
    "05.a": "lock", "05.b": "shimmer"})

PROJ = Path(__file__).resolve().parent.parent
CAPA_AULA1 = PROJ.parent.parent / "001_conceito_e_tripe" / "youtube" / "capa_A_tripe.jpg"

NAVY, NAVY2, NAVY3 = "#07142F", "#0E2556", "#173A7A"
WHITE = "#FFFFFF"
INK2 = "#B9C6E4"
YEL = "#FFD23F"
SKY = "#5AA9FF"
SAUDE, PREV, ASSIST = "#E5484D", "#2BB3A3", "#E8A317"   # cores fixas dos pilares (previdência clareada p/ fundo escuro)
RED = "#FF5A5F"
SKIN, HAIR, SWEATER = "#F2C29B", "#2A1C14", "#3B6CF6"
CX = W / 2


def fade(t, t0, t1, d=0.3, d_out=0.25):
    return ep(t, t0, d) * (1 - prog(t, t1, d_out))


def shake(t, t0, amp=12, d=0.3):
    u = prog(t, t0, d)
    if u <= 0 or u >= 1:
        return 0.0, 0.0
    k = (1 - u) * amp
    return k * math.sin(t * 90), k * math.cos(t * 77)


def big(c, s, y, a, size=96, col=WHITE, hl=None, hl_col=YEL, maxw=960, peso="black"):
    """título grande centralizado; hl = trecho com marca-texto amarelo"""
    if a <= 0:
        return
    while text_w(s, peso, size) > maxw:
        size -= 2
    f = ease_out(clamp(a))
    yy = y + (1 - f) * 30
    x = CX - text_w(s, peso, size) / 2
    if hl and hl in s:
        pre = s[:s.index(hl)]
        hx = x + text_w(pre, peso, size)
        hw = text_w(hl, peso, size)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(hx - 10, yy - size * 0.84, (hw + 20) * ep(a, 0.35, 0.4), size * 1.08), 8, 8),
                    paint(hl_col, f))
        text(c, pre, x, yy, size, peso, col, f, align="left")
        text(c, hl, hx, yy, size, peso, NAVY, f, align="left")
        text(c, s[s.index(hl) + len(hl):], hx + hw, yy, size, peso, col, f, align="left")
    else:
        glow_text(c, s, CX, yy, size, peso, col, f, glow=0.12)


def wordmark(c, cx, cy, size, a, col=WHITE):
    """ESTUDATIVO: nome do canal em caixa alta, com um traço amarelo embaixo"""
    if a <= 0:
        return
    w = text_w("ESTUDATIVO", "black", size)
    text(c, "ESTUDATIVO", cx - w / 2, cy + size * 0.35, size, "black", col, a, align="left", tracking=0)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy + size * 0.55, w * ep(a, 0.2, 0.6), size * 0.12),
                                      4, 4), paint(YEL, a))


def pill(c, s, cx, cy, size, bg, fg, a, peso="black"):
    if a <= 0:
        return
    w = text_w(s, peso, size) + size * 1.2
    h = size * 1.8
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(r, blur_paint(bg, 0.45 * a, 20))
    c.drawRRect(r, paint(bg, a))
    text_mid(c, s, cx, cy, size, peso, fg, a)


@lru_cache(None)
def capa_aula1():
    return skia.Image.open(str(CAPA_AULA1))


# ---------------------------------------------------------------- personagem e objetos (ilustração)
def student(c, cx, cy, s, a, t, mood="duvida", look=0.0):
    """estudante em busto, traço chapado. mood: duvida | foco"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    sh = paint("#000000", 0.25 * a)
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 30))
    c.drawOval(skia.Rect.MakeXYWH(-230, 250, 460, 80), sh)
    # ombros e moletom
    p = skia.Path(); p.moveTo(-230, 300); p.cubicTo(-230, 150, -150, 110, 0, 110); p.cubicTo(150, 110, 230, 150, 230, 300); p.close()
    c.drawPath(p, paint(SWEATER, a))
    c.drawPath(p, paint("#2A4FD0", a * 0.5, stroke=6))
    c.drawRect(skia.Rect.MakeXYWH(-34, 70, 68, 60), paint("#E3AE86", a))   # pescoço
    # gola
    g = skia.Path(); g.moveTo(-60, 112); g.quadTo(0, 170, 60, 112); c.drawPath(g, paint("#FFFFFF", 0.85 * a, stroke=10, cap_round=True))
    # cabeça
    bob = math.sin(t * 2.2) * 3
    c.translate(look * 14, bob)
    c.drawCircle(-104, -10, 22, paint("#E3AE86", a)); c.drawCircle(104, -10, 22, paint("#E3AE86", a))  # orelhas
    c.drawOval(skia.Rect.MakeXYWH(-105, -125, 210, 230), paint(SKIN, a))
    hp = skia.Path(); hp.moveTo(-112, -10); hp.cubicTo(-125, -150, 125, -160, 112, -10); hp.cubicTo(80, -95, -40, -110, -112, -10); hp.close()
    c.drawPath(hp, paint(HAIR, a))
    # rosto
    ex = look * 10
    if mood == "duvida":
        c.drawLine(-62, -42, -22, -50, paint(HAIR, a, stroke=9, cap_round=True))
        c.drawLine(22, -56, 62, -40, paint(HAIR, a, stroke=9, cap_round=True))
        c.drawCircle(-42 + ex, -10, 10, paint("#1A1A1A", a)); c.drawCircle(42 + ex, -10, 10, paint("#1A1A1A", a))
        m = skia.Path(); m.moveTo(-26, 52); m.cubicTo(-10, 44, 6, 60, 26, 48)
        c.drawPath(m, paint("#9A4B3A", a, stroke=7, cap_round=True))
    else:
        c.drawLine(-62, -40, -22, -44, paint(HAIR, a, stroke=9, cap_round=True))
        c.drawLine(22, -44, 62, -40, paint(HAIR, a, stroke=9, cap_round=True))
        for x0 in (-42, 42):   # olhos olhando para baixo (concentrado)
            e = skia.Path(); e.moveTo(x0 - 14, -6); e.quadTo(x0, 6, x0 + 14, -6)
            c.drawPath(e, paint("#1A1A1A", a, stroke=7, cap_round=True))
        m = skia.Path(); m.moveTo(-24, 46); m.quadTo(0, 62, 24, 46)
        c.drawPath(m, paint("#9A4B3A", a, stroke=7, cap_round=True))
    c.restore()


def bubble_q(c, cx, cy, r, a, t):
    if a <= 0:
        return
    k = ease_back(clamp(a))
    c.save(); c.translate(cx, cy); c.scale(k, k)
    c.drawCircle(0, 0, r, blur_paint(YEL, 0.35 * a, 20))
    c.drawCircle(0, 0, r, paint(WHITE, a))
    c.drawCircle(-r * 0.75, r * 0.95, r * 0.18, paint(WHITE, a)); c.drawCircle(-r * 1.0, r * 1.3, r * 0.1, paint(WHITE, a))
    text_mid(c, "?", 0, math.sin(t * 5) * 4, r * 1.25, "black", NAVY2, a)
    c.restore()


def question_card(c, x, y, w, a, zoom=1.0, hl=0.0):
    """questão ilustrativa no estilo certo/errado (texto do art. 194 da Constituição)"""
    if a <= 0:
        return
    h = w * 0.78
    c.save(); c.translate(x + w / 2, y + h / 2); c.scale(zoom, zoom); c.translate(-(x + w / 2), -(y + h / 2))
    sh = paint("#000000", 0.35 * a); sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 26))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 8, y + 18, w, h), 22, 22), sh)
    rrect(c, x, y, w, h, 22, "#FBFAF5", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, 70), 22, 22), paint(NAVY2, a))
    c.drawRect(skia.Rect.MakeXYWH(x, y + 40, w, 30), paint(NAVY2, a))
    text(c, "QUESTÃO · SEGURIDADE SOCIAL", x + 32, y + 46, 26, "extrabold", WHITE, a, align="left")
    linhas = ["A seguridade social compreende um", "conjunto integrado de ações destinadas a",
              "assegurar os direitos relativos à saúde, à", "previdência e à assistência social."]
    for i, ln in enumerate(linhas):
        ly = y + 130 + i * 50
        if hl > 0 and i >= 2:
            c.drawRect(skia.Rect.MakeXYWH(x + 30, ly - 34, (text_w(ln, "medium", 33) + 8) * clamp(hl * 2 - (i - 2)), 44), paint(YEL, 0.75 * a))
        text(c, ln, x + 34, ly, 33, "medium", "#1F2433", a, align="left")
    for i, op in enumerate(("Certo", "Errado")):
        bx = x + 34 + i * 230
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, y + h - 92, 40, 40), 8, 8), paint("#6B7280", a, stroke=3))
        text(c, op, bx + 56, y + h - 60, 32, "semibold", "#1F2433", a, align="left")
    text(c, "exemplo ilustrativo", x + w - 30, y + h - 26, 20, "medium", "#9AA0AE", a, align="right")
    c.restore()


def sticky(c, s, cx, cy, col, a, rot=0.0, size=40):
    if a <= 0:
        return
    k = ease_back(clamp(a))
    w = max(220, text_w(s, "black", size) + 60)
    h = 140
    c.save(); c.translate(cx, cy); c.rotate(rot); c.scale(k, k)
    sh = paint("#000000", 0.35 * a); sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRect(skia.Rect.MakeXYWH(-w / 2 + 6, -h / 2 + 10, w, h), sh)
    c.drawRect(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), paint(col, a))
    c.drawRect(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, 18), paint("#000000", 0.08 * a))
    text_mid(c, s, 0, 6, size, "black", "#1F2433", a)
    c.restore()


def apostila(c, x, y, w, h, a, t, t_hl=None, rot=0.0):
    """apostila aberta com linhas de texto e marca-texto passando"""
    if a <= 0:
        return
    c.save(); c.translate(x + w / 2, y + h / 2); c.rotate(rot); c.translate(-(x + w / 2), -(y + h / 2))
    sh = paint("#000000", 0.4 * a); sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 24))
    c.drawRect(skia.Rect.MakeXYWH(x + 10, y + 20, w, h), sh)
    for i, xx in enumerate((x, x + w / 2)):
        c.drawRect(skia.Rect.MakeXYWH(xx, y, w / 2, h), paint("#FBFAF5" if i else "#F3F1EA", a))
    c.drawLine(x + w / 2, y + 10, x + w / 2, y + h - 10, paint("#D9D5C8", a, stroke=3))
    for col in (0, 1):
        for i in range(11):
            lx = x + 34 + col * w / 2
            lw = (w / 2 - 68) * (0.55 + 0.45 * hash01(i, col + 3))
            ly = y + 50 + i * (h - 90) / 10
            if t_hl is not None and col == 1 and i in (3, 4, 7):
                u = clamp((t - t_hl - (0.25 if i == 4 else 0.5 if i == 7 else 0)) / 0.35)
                c.drawRect(skia.Rect.MakeXYWH(lx - 4, ly - 12, (lw + 8) * u, 24), paint(YEL, 0.8 * a))
            c.drawRect(skia.Rect.MakeXYWH(lx, ly - 4, lw, 8), paint("#B7B2A4", a))
    c.restore()


def desk(c, a):
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeLinear(points=[(0, 1180), (0, 1920)], colors=[hexc("#2B2F45"), hexc("#151827")]))
    p.setAlphaf(a)
    c.drawRect(skia.Rect.MakeXYWH(0, 1180, W, 740), p)


# ---------------------------------------------------------------- fundo, legenda, moldura
@lru_cache(None)
def _bg():
    s = skia.Surface(W, H); c = s.getCanvas()
    p = skia.Paint()
    p.setShader(skia.GradientShader.MakeRadial(center=(W * 0.5, H * 0.3), radius=H * 0.8,
                                               colors=[hexc(NAVY3), hexc(NAVY2), hexc(NAVY)], positions=[0, 0.45, 1]))
    c.drawRect(skia.Rect.MakeWH(W, H), p)
    g = paint(SKY, 0.05, stroke=1.2)
    for y in range(0, H, 56):   # pauta de caderno
        c.drawLine(0, y, W, y, g)
    c.drawLine(120, 0, 120, H, paint(RED, 0.08, stroke=2))
    return s.makeImageSnapshot()


def BACKGROUND(c, t):
    c.drawImage(_bg(), 0, 0)
    for i in range(26):
        x = hash01(i, 1) * W + math.sin(t * 0.5 + i) * 10
        y = H - ((hash01(i, 3) * H + t * (14 + 30 * hash01(i, 5))) % (H + 40))
        c.drawCircle(x, y, 1.5 + 2.5 * hash01(i, 7), paint(YEL if i % 4 == 0 else WHITE, 0.10 + 0.18 * hash01(i, 9)))
    # luz que "acende" na virada dúvida -> clareza
    k = ep(t, CLAREZA[0], 1.2) if CLAREZA else 0
    if k > 0:
        c.drawCircle(CX, 760, 760, blur_paint(YEL, 0.10 * k, 200))


CLAREZA = []
CAP_Y = 1430


def _chunks(tokens):
    out, cur = [], []
    for tk in tokens:
        cur.append(tk)
        end = tk["disp"].rstrip()[-1:] in ".,:?!"
        if len(cur) >= 3 or end or sum(len(x["disp"]) + 1 for x in cur) > 18:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def CAPTION(c, scene, t):
    """legenda de Shorts: 1 a 3 palavras, grandes; palavra falada em amarelo; destaque *x* em azul-claro"""
    lt = t - scene["start"]
    chunks = scene.setdefault("_ch", _chunks(scene["tokens"]))
    for i, ch in enumerate(chunks):
        s = ch[0]["t0"] - 0.06
        e = chunks[i + 1][0]["t0"] - 0.06 if i + 1 < len(chunks) else scene["dur"] - 0.05
        if s <= lt < e:
            break
    else:
        return
    words = [tk["disp"].upper() for tk in ch]
    size, sp = 88, 24
    while sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1) > 960:
        size -= 3
    tot = sum(text_w(wd, "black", size) for wd in words) + sp * (len(words) - 1)
    pop = ease_back(clamp((lt - s) / 0.16))
    x = CX - tot / 2
    c.save(); c.translate(CX, CAP_Y); c.scale(0.86 + 0.14 * pop, 0.86 + 0.14 * pop); c.translate(-CX, -CAP_Y)
    f = motor.font("black", size)
    for tk, wd in zip(ch, words):
        ww = text_w(wd, "black", size)
        falando = tk["t0"] - 0.05 <= lt < tk["t1"] + 0.25
        col = YEL if falando else (SKY if tk["bold"] else WHITE)
        st = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.17, Color=skia.Color(4, 10, 28))
        st.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, st)
        c.drawString(wd, x, CAP_Y + size * 0.36, f, paint(col, 1.0))
        x += ww + sp
    c.restore()


def OVERLAY(c, t):
    # selo do curso no topo (não é logo animado: está lá desde o 1º quadro)
    pill(c, "SEGURIDADE SOCIAL · CONCURSO", CX, 150, 24, YEL, NAVY, 0.95, "extrabold")
    for t0 in GLITCH:   # corte seco com flash nas viradas
        u = (t - t0) / 0.18
        if 0 <= u < 1:
            c.drawRect(skia.Rect.MakeWH(W, H), paint(WHITE, 0.35 * (1 - u)))


GLITCH = []


def _cues(C):
    if not GLITCH:
        GLITCH[:] = [C["02.b"], C["03.a"] - 0.1, C["05.a"] - 0.1]
        CLAREZA[:] = [C["03.a"] - 0.1]


# ---------------------------------------------------------------- blocos
def b_gancho(c, t, C, B):
    _cues(C)
    ta, tb = C["01.a"], C["01.b"]
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    desk(c, a)
    # estudante em dúvida + questão; zoom rápido na questão
    z = 1.0 + 0.15 * ease_io(prog(t, ta + 0.25, 0.7))
    sx, sy = shake(t, ta, 10)
    c.save(); c.translate(sx, sy)
    student(c, 300, 820, 0.95 * (1 + (z - 1) * 0.3), a * (1 - prog(t, ta + 0.3, 0.4)), t, "duvida", look=0.8)
    bubble_q(c, 540, 660, 60, a * ep(t, ta, 0.25) * (1 - prog(t, ta + 0.4, 0.3)), t)
    question_card(c, 140, 720 + 110 * (1 - ease_io(prog(t, ta + 0.25, 0.7))),
                  800, a, zoom=z * (0.62 + 0.38 * ease_io(prog(t, ta + 0.25, 0.7))))
    c.restore()
    # frase do gancho já no primeiro quadro
    big(c, "VAI ESTUDAR", 330, a * (1 - prog(t, tb - 0.1, 0.2)), 104)
    big(c, "SEGURIDADE SOCIAL", 445, a * (1 - prog(t, tb - 0.1, 0.2)), 104, YEL)
    big(c, "PARA CONCURSO?", 560, a * (1 - prog(t, tb - 0.1, 0.2)), 104)
    ab = ep(t, tb, 0.2)
    if ab > 0:
        big(c, "COMECE POR AQUI", 400, ab, 110, hl="AQUI")
        # seta apontando para baixo (para o conteúdo)
        yy = 470 + math.sin(t * 9) * 10
        pth = skia.Path(); pth.moveTo(CX - 40, yy); pth.lineTo(CX + 40, yy); pth.lineTo(CX, yy + 50); pth.close()
        c.drawPath(pth, paint(YEL, ab))


CONCEITOS = [("art. 194", "#FFE97A", -6), ("art. 195", "#FFC1D0", 5), ("universalidade", "#BFE7FF", -3),
             ("equidade", "#C8F2C2", 7), ("tripé", "#FFE97A", -8), ("custeio", "#FFC1D0", 4)]


def b_decorar(c, t, C, B):
    _cues(C)
    ta, tb = C["02.a"], C["02.b"]
    a = fade(t, B["start"], B["end"])
    # cortes rápidos: apostila marcada -> post-its de conceitos -> questão marcada
    corte = int(max(0, t - ta) / 0.75)
    caos = a * (1 - prog(t, tb, 0.2))
    if caos > 0:
        if corte == 0:
            apostila(c, 90, 560, 900, 620, caos, t, t_hl=ta + 0.1, rot=-3)
        elif corte == 1:
            apostila(c, 60, 600, 960, 640, caos * 0.5, t, rot=4)
            for i, (s, col, r) in enumerate(CONCEITOS):
                sticky(c, s, 250 + (i % 2) * 520 + hash01(i, 2) * 40, 640 + (i // 2) * 190, col, caos * ep(t, ta + 0.75 + i * 0.07, 0.2), r)
        else:
            question_card(c, 140, 640, 800, caos, zoom=1.0 + 0.05 * (t - ta), hl=clamp((t - ta - 1.5) / 0.6))
            for i, (s, col, r) in enumerate(CONCEITOS[:4]):
                sticky(c, s, 200 + i * 230, 1180 + (i % 2) * 40, col, caos * 0.9, r, 32)
        big(c, "NÃO COMECE APENAS", 345, caos * ep(t, ta + 0.2, 0.25), 86)
        big(c, "DECORANDO!", 455, caos * ep(t, ta + 0.35, 0.25), 110, RED)
        # risco sobre "decorando"
        u = ep(t, ta + 1.9, 0.25)
        if u > 0:
            w = text_w("DECORANDO!", "black", 110)
            c.drawLine(CX - w / 2 - 10, 425, CX - w / 2 - 10 + (w + 20) * u, 410, paint(WHITE, caos, stroke=10, cap_round=True))
    ab = a * ep(t, tb, 0.2)
    if ab > 0:
        big(c, "ENTENDA OS", 470, ab, 110)
        big(c, "FUNDAMENTOS.", 600, ab, 120, hl="FUNDAMENTOS.")
        # alicerce: três blocos sustentando um bloco maior (ideia de base)
        for i, col in enumerate((SAUDE, PREV, ASSIST)):
            k = ep(t, tb + 0.25 + i * 0.12, 0.25)
            rrect(c, 160 + i * 270, 1000 + (1 - k) * 60, 220, 150, 16, col, ab * k)
        k = ep(t, tb + 0.7, 0.3)
        rrect(c, 160, 820 + (1 - k) * -60, 760, 150, 16, WHITE, ab * k)
        text_mid(c, "BASE", CX, 895 + (1 - k) * -60, 64, "black", NAVY, ab * k)


def b_modulo(c, t, C, B):
    _cues(C)
    ta, tb, tc = C["03.a"], C["03.b"], C["03.c"]
    a = fade(t, B["start"], B["end"])
    # dúvida -> clareza: conceitos soltos se organizam no tripé (conteúdo real da Aula 1)
    u = ease_io(prog(t, ta, 1.1))
    topo = (CX, 640)
    pil = [(230, 900, "SAÚDE", SAUDE), (CX, 1030, "PREVIDÊNCIA", PREV), (850, 900, "ASSISTÊNCIA", ASSIST)]
    soltos = [(160, 1150), (880, 560), (420, 1230)]
    k_tri = a * (1 - prog(t, tb + 0.2, 0.3))
    if k_tri > 0:
        for (px, py, s, col), (sx, sy) in zip(pil, soltos):
            x, y = lerp(sx, px, u), lerp(sy, py, u)
            c.drawLine(topo[0], topo[1] + 60, x, y - 50, paint(col, k_tri * u, stroke=6, cap_round=True))
            pill(c, s, x, y, 34, col, WHITE, k_tri)
        pill(c, "SEGURIDADE SOCIAL", topo[0], topo[1], 46, WHITE, NAVY, k_tri * ep(t, ta + 0.6, 0.3))
        wordmark(c, CX, 400, 96, k_tri * ep(t, ta, 0.3))
        text(c, "no canal", CX, 320, 40, "semibold", INK2, k_tri * ep(t, ta, 0.3))
    # o módulo: a capa real da Aula 1 + lista das 9 aulas
    am = a * ep(t, tb, 0.3)
    if am > 0:
        big(c, "SEGURIDADE SOCIAL", 360, am, 92)
        big(c, "MÓDULO 1", 480, am, 110, YEL)
        big(c, "FUNDAMENTOS", 600, am * ep(t, tc, 0.25), 112, hl="FUNDAMENTOS")
        cw, ch = 760, 760 * 9 / 16
        cx0, cy0 = CX - cw / 2, 720 + (1 - ease_out(am)) * 60
        sh = paint("#000000", 0.45 * am); sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 30))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx0 + 10, cy0 + 24, cw, ch), 20, 20), sh)
        c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx0, cy0, cw, ch), 20, 20), True)
        p = skia.Paint(AntiAlias=True); p.setAlphaf(am)
        c.drawImageRect(capa_aula1(), skia.Rect.MakeXYWH(cx0, cy0, cw, ch), skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear), p)
        c.restore()
        pill(c, "AULA 1 · O TRIPÉ", CX, cy0 + ch + 10, 30, YEL, NAVY, am)
        text(c, "9 aulas no módulo", CX, cy0 + ch + 92, 34, "bold", INK2, am * ep(t, tc, 0.3))


AULAS = ["O tripé", "Princípios I", "Princípios II", "Financiamento", "Art. 195", "Saúde e SUS", "Assistência",
         "BPC", "Previdência"]


def b_base(c, t, C, B):
    _cues(C)
    ta, tb = C["04.a"], C["04.b"]
    a = fade(t, B["start"], B["end"])
    big(c, "CONSTRUA", 330, a * ep(t, ta, 0.25), 104)
    big(c, "SUA BASE.", 445, a * ep(t, ta + 0.15, 0.25), 112, hl="BASE.")
    big(c, "AVANCE NOS SEUS ESTUDOS.", 560, a * ep(t, tb, 0.25), 70, SKY)
    desk(c, a)
    student(c, 270, 900, 0.85, a, t, "foco", look=0.6)
    # caderno com as aulas do módulo sendo marcadas (escada de progresso)
    x, y, w, h = 470, 690, 560, 640
    rrect(c, x, y, w, h, 18, "#FBFAF5", a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, 18, h), paint(SWEATER, a))
    text(c, "MÓDULO 1 · FUNDAMENTOS", x + 44, y + 58, 28, "black", NAVY2, a, align="left")
    for i, s in enumerate(AULAS):
        yy = y + 112 + i * 56
        k = ep(t, ta + 0.25 + i * 0.32, 0.18)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 44, yy - 30, 36, 36), 8, 8), paint("#9AA0AE", a, stroke=3))
        if k > 0:
            pth = skia.Path(); pth.moveTo(x + 50, yy - 12); pth.lineTo(x + 60, yy - 2); pth.lineTo(x + 76, yy - 26)
            c.drawPath(pth, paint("#16A36A", a * k, stroke=6, cap_round=True))
        text(c, f"Aula {i + 1} · {s}", x + 96, yy, 30, "semibold", "#1F2433", a, align="left")
    # lápis na mão
    lx, ly = 460 + 12 * math.sin(t * 7), 1120 + 8 * math.cos(t * 9)
    c.save(); c.translate(lx, ly); c.rotate(-35)
    c.drawRect(skia.Rect.MakeXYWH(-10, -150, 20, 150), paint(YEL, a))
    pth = skia.Path(); pth.moveTo(-10, 0); pth.lineTo(10, 0); pth.lineTo(0, 26); pth.close()
    c.drawPath(pth, paint("#E3AE86", a))
    c.restore()


def b_cta(c, t, C, B):
    _cues(C)
    ta, tb = C["05.a"], C["05.b"]
    a = ep(t, B["start"], 0.25)
    big(c, "COMECE PELO", 330, a, 96)
    big(c, "MÓDULO 1", 455, a, 140, hl="MÓDULO 1")
    text(c, "FUNDAMENTOS — SEGURIDADE SOCIAL", CX, 560, 44, "extrabold", WHITE, a * ep(t, ta + 0.2, 0.25))
    # cartão do canal
    k = ep(t, ta + 0.3, 0.35)
    x, y, w, h = 90, 640 + (1 - ease_out(k)) * 50, 900, 560
    rrect(c, x, y, w, h, 34, "#0B1C44", a * k)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 34, 34), paint(YEL, a * k * 0.9, stroke=4))
    cw, ch = 640, 360
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(CX - cw / 2, y + 50, cw, ch), 16, 16), True)
    p = skia.Paint(AntiAlias=True); p.setAlphaf(a * k)
    c.drawImageRect(capa_aula1(), skia.Rect.MakeXYWH(CX - cw / 2, y + 50, cw, ch), skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear), p)
    c.restore()
    wordmark(c, CX, y + h - 70, 92, a * k)
    # chamada final com pulso sutil
    kb = ep(t, ta + 0.8, 0.3)
    pulse = 1 + 0.04 * math.sin(t * 6) * kb
    c.save(); c.translate(CX, 1300); c.scale(pulse, pulse)
    pill(c, "ASSISTA À PLAYLIST NO CANAL!", 0, 0, 44, YEL, NAVY, a * kb)
    c.restore()


BLOCKS = dict(gancho=b_gancho, decorar=b_decorar, modulo=b_modulo, base=b_base, cta=b_cta)
