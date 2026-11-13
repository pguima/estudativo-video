"""Short-convite da trilha Divisibilidade, MMC e MDC (MAT-DIV-001 a 008) — 1080x1920, render.py --vertical.
Visual editorial do Estudativo (papel claro, Inter Black + Instrument Serif itálica, índigo da Matemática, palco escuro no macete).
Retenção: o 1º quadro já traz o desafio "4.572 ÷ 9 ?" (ENTRADA_SECA) e a contagem 3-2-1 segura o laço; a resposta e o macete
chegam em 5 s; virada para a dor; mural rolando com as capas reais das 8 aulas; busca "Estudativo" + playlist + inscreva-se.
Legenda queimada palavra a palavra em y≈1530 (funciona no mudo), fora da faixa dos botões das redes (direita e rodapé).
Todo instante vem de C[...] (marcadores do roteiro): troque o tempos.json pela voz real e o desenho acompanha."""
import math
from functools import lru_cache
from pathlib import Path

import skia
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ep, prog, lerp, ease_io, ease_out, ease_back, centro, clamp
import motor as M

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
BR = "#FFFFFF"
ARQUIVO_FINAL = "estudativo_MAT-DIV_convite_short.mp4"
MARCA = ""
ENTRADA_SECA = True
CX = W / 2
assert 4 + 5 + 7 + 2 == 18 and 18 % 9 == 0 and 4572 == 9 * 508

# Som de Short (todo Short leva trilha + efeitos): batida desde o 1º segundo, trilha presente, -14 LUFS.
# Efeitos acertados com o desenho: contagem 3-2-1 (tick), resposta (confirm), soma dos algarismos (pop), risco em
# "decoreba" (deny), MMC e MDC entrando (pop), contador das 8 aulas (data), digitação da busca (typing), clique no inscreva-se (click + notif).
_P = 0.61  # passo da contagem (≈ (fim de s01 − s01.b − 0.25) / 3 com a voz real)
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "s01.a": ["impact@+0.05"],
    "s01.b": [f"tick@+{0.25 + k * _P:.2f}" for k in range(3)],
    "s02.a": ["confirm", "shimmer@+0.35"],
    "s02.b": ["whoosh@-0.15"], "s02.c": [f"pop@+{0.35 * k:.2f}" for k in range(4)], "s02.d": ["data"],
    "s02.e": ["pop"], "s02.f": ["confirm"],
    "s03.a": ["deny@+1.1"], "s03.b": None,
    "s03.c": ["impact", "pop@+0.45", "pop@+0.65"],
    "s04.a": ["data@+0.4", "shimmer@+1.5"],
    "s05.a": ["typing@+0.35"], "s05.b": ["lock", "click@+2.55", "notif@+2.65"], "s05.c": ["shimmer"],
})

AULAS = Path(__file__).resolve().parents[3] / "aulas"
SAMP = skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear)
_ESCURO = []  # intervalos em que o fundo é o palco escuro (legenda clara)


@lru_cache(None)
def capa(i):
    p = next((AULAS / f"MAT-DIV-{i:03d}" / "youtube").glob("capa_A*.jpg"))
    return skia.Image.open(str(p))


def BACKGROUND(c, t):
    E.fundo(c, t)


def OVERLAY(c, t):
    E.acabamento(c, t)


# ---------------- peças ----------------
def palco_v(c, t, a=1.0):
    """palco escuro vertical com brilho da cor da matéria (atalhos e macetes)"""
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * a))
    c.drawRect(skia.Rect.MakeWH(W, H), M.paint("#07070F"))
    for cx, cy, r, f in ((200 + 40 * math.sin(t * 0.5), 260, 760, 0.8), (900, 1500 + 40 * math.cos(t * 0.4), 820, 0.6)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(E.COR, f), M.hexc(E.COR, 0.0)], [0.0, 1.0]))
        c.drawCircle(cx, cy, r, p)
    E.arco(c, 860, -160, 460, 30, 130, CLARO, 3, 0.25)
    c.restore()


def chip(c, t, t0, s, cx, cy, size, fundo=None, cor=BR, estilo="g"):
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, cx, cy, size, estilo=estilo, fundo=fundo, cor=cor, a=a))


def grande(c, t, t0, s, cx, y, size, cor=TINTA, estilo="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, estilo, cor, a), sobe=30, blur=22)


def pop(t, t0, d=0.45):
    return ease_back(prog(t, t0, d))


# ---------------- 1. desafio: 4.572 ÷ 9 ? com contagem ----------------
def b_desafio(c, t, C, b):
    tb, fim = C["s01.b"], C["s01.end"]
    # no 1º quadro, tudo já na tela (o gancho é visual)
    E.frase(c, t, -1, [("desafio", "i", 92, COR), ("relâmpago", "i", 92, TINTA2)], CX, 330, "center")
    k = 1 + 0.025 * math.sin(t * 5)
    c.save(); c.translate(CX, 760); c.scale(k, k)
    centro(c, "4.572", 0, 0, 250, "g", TINTA)
    c.restore()
    E.frase(c, t, -1, [("se divide por", "i", 84, TINTA2), ("9?", "g", 150, COR)], CX, 990, "center")
    # contagem 3-2-1 a partir de "três segundos"
    t3 = tb + 0.25
    passo = max(0.55, (fim - t3) / 3)
    if t >= t3:
        n = 3 - min(2, int((t - t3) / passo))
        f = (t - t3 - (3 - n) * passo) / passo
        r = 150 * pop(t, t3 + (3 - n) * passo, 0.35)
        E.bola(c, CX, 1270, r, E.COR)
        E.arco(c, CX, 1270, r + 30, -90, 360 * (1 - clamp(f)), TINTA, 10)
        if r > 20:
            centro(c, str(n), CX, 1270 + r * 0.42, r * 1.15, "g", BR)


# ---------------- 2. macete no palco ----------------
def b_macete(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s02.{k}"] for k in "abcdef")
    palco_v(c, t, ep(t, b["start"] - 0.05, 0.35))
    # a resposta logo de cara
    centro(c, "4.572 ÷ 9 ?", CX, 330, 110, "g", "#FFFFFF")
    s = pop(t, a_, 0.5)
    if s > 0:
        c.save(); c.translate(CX, 520); c.scale(s, s)
        E.pilula(c, "SIM!", 0, 0, 120, estilo="g", fundo=CERTO, cor=BR)
        c.restore()
    if t >= a_ + 0.35:
        E.selo(c, CX + 260, 470, 52 * pop(t, a_ + 0.35), True)
    # o macete: some os algarismos
    chip(c, t, b_ - 0.1, "macete", CX, 740, 54, fundo=E.COR, estilo="i")
    E.frase(c, t, b_ + 0.2, [("some os", "i", 86, CLARO), ("algarismos", "g", 92, "#FFFFFF")], CX, 900, "center", 0.2)
    # os quatro algarismos, um por fala
    for k, (dg, sinal) in enumerate((("4", ""), ("5", "+"), ("7", "+"), ("2", "+"))):
        x = CX - 330 + k * 220
        E.foco(c, t, c_ + 0.35 * k, 0.4, lambda a, x=x, dg=dg, sinal=sinal: (
            centro(c, sinal, x - 110, 1080, 96, "g", CLARO, a), centro(c, dg, x, 1090, 130, "g", "#FFFFFF", a)))
    s2 = pop(t, d_, 0.45)
    if s2 > 0:
        c.save(); c.translate(CX, 1250); c.scale(s2, s2)
        E.pilula(c, "= 18", 0, 0, 100, estilo="g", fundo=E.COR, cor=BR)
        c.restore()
    E.frase(c, t, e_, [("18 ÷ 9 = 2", "g", 84, "#5BE3A4")], CX, 1430, "center")
    if t >= f_:
        p = prog(t, f_, 0.6)
        E.arco(c, CX, 1404, 260 * (0.6 + 0.4 * ease_out(p)), 200, 140 * ease_io(p), "#5BE3A4", 7)


# ---------------- 3. virada: não é decoreba, é saber qual usar ----------------
def b_virada(c, t, C, b):
    a_, b_, c_ = (C[f"s03.{k}"] for k in "abc")
    E.frase(c, t, a_, [("MMC e MDC", "g", 96, TINTA), ("parecem", "i", 84, TINTA2)], CX, 330, "center", 0.15)
    E.frase(c, t, a_ + 0.5, [("decoreba", "g", 120, E.ERRADO)], CX, 490, "center")
    if t >= a_ + 1.1:
        w = E.larg("decoreba", "g", 120)
        E.risco(c, CX - w / 2 - 14, 462, CX + w / 2 + 14, 452, t, a_ + 1.1, largura=12)
    E.frase(c, t, b_, [("a prova só quer saber", "i", 76, TINTA2)], CX, 660, "center")
    E.frase(c, t, c_, [("qual", "g", 120, COR), ("usar", "g", 120, TINTA)], CX, 820, "center", 0.15)
    E.frase(c, t, c_ + 0.5, [("e", "i", 100, TINTA2), ("quando", "g", 120, COR)], CX, 960, "center", 0.15)
    # as duas ferramentas, com o "?" entre elas
    for k, (nome, dx) in enumerate((("MMC", -250), ("MDC", 250))):
        p = pop(t, c_ + 0.45 + 0.2 * k, 0.5)
        if p > 0:
            E.bola(c, CX + dx, 1230, 150 * p, E.COR)
            centro(c, nome, CX + dx, 1230 + 34 * p, 92 * p, "g", BR)
    if t >= c_ + 0.9:
        k = 1 + 0.08 * math.sin((t - c_) * 6)
        centro(c, "?", CX, 1280, 150 * k * ease_back(prog(t, c_ + 0.9, 0.4)), "g", TINTA)


# ---------------- 4. a trilha: 8 aulas do zero ----------------
TOPICOS = ("múltiplos e divisores", "regras de divisibilidade", "números primos", "MMC e MDC", "problemas de prova")
N_AULAS = 8


def b_trilha(c, t, C, b):
    a_ = C["s04.a"]
    ks = [C[f"s04.{k}"] for k in "bcdef"]
    # contador rolando até N_AULAS
    n = int(round(N_AULAS * ease_out(prog(t, a_ + 0.4, 0.9))))
    E.foco(c, t, a_, 0.4, lambda a: centro(c, str(max(1, n)), CX - 120, 400, 250, "g", COR, a))
    E.frase(c, t, a_ + 0.3, [("aulas", "g", 96, TINTA)], CX + 120, 330, "center")
    E.frase(c, t, a_ + 0.9, [("do", "i", 90, TINTA2), ("zero", "i", 90, COR)], CX + 120, 420, "center", 0.15)
    # mural rolando com as capas reais das aulas
    top, bot = 500, 1200
    ap = ep(t, a_ + 0.5, 0.6)
    if ap > 0:
        tw, th, gap = 316, 178, 18
        c.save()
        c.clipRect(skia.Rect.MakeLTRB(0, top, W, bot))
        x0 = CX - (3 * tw + 2 * gap) / 2
        rol = (t - a_) * 70
        for col in range(3):
            v = rol * (1.0 if col != 1 else -0.8) + col * 90
            for k in range(-1, 6):
                idx = (col * 3 + k + int(v // (th + gap))) % N_AULAS + 1
                y = top - 20 + k * (th + gap) - (v % (th + gap))
                x = x0 + col * (tw + gap)
                rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, tw, th), 14, 14)
                c.save(); c.clipRRect(rr, True)
                pt = skia.Paint(); pt.setAlphaf(ap)
                c.drawImageRect(capa(idx), skia.Rect.MakeXYWH(x, y, tw, th), SAMP, pt)
                c.restore()
        # bordas esfumadas no papel
        for y0, y1, inv in ((top, top + 70, False), (bot - 70, bot, True)):
            g = skia.Paint()
            cores = [M.hexc(E.PAPEL, 1.0), M.hexc(E.PAPEL, 0.0)]
            g.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y0), skia.Point(0, y1)], cores[::-1] if inv else cores))
            c.drawRect(skia.Rect.MakeLTRB(0, y0, W, y1), g)
        c.restore()
    # os assuntos, um por vez, na pílula
    for i, (k, s) in enumerate(zip(ks, TOPICOS)):
        fim = ks[i + 1] if i + 1 < len(ks) else b["end"] + 1
        if k <= t < fim + 0.25:
            sai = 1 - ease_io(prog(t, fim - 0.05, 0.25)) if i + 1 < len(ks) else 1
            sz = pop(t, k, 0.4)
            if sz > 0 and sai > 0:
                c.save(); c.translate(CX, 1320); c.scale(sz, sz)
                E.pilula(c, s, 0, 0, 66, estilo="g", fundo=E.COR, cor=BR, a=sai)
                c.restore()
    # bolinhas de progresso dos assuntos
    for i, k in enumerate(ks):
        x = CX + (i - 2) * 46
        on = t >= k
        c.drawCircle(x, 1430, 11 if on else 8, M.paint(E.COR if on else CINZA, 1 if on else 0.5))


# ---------------- 5. convite: busca, playlist, inscreva-se ----------------
BUSCA = "Estudativo"
PLAYLIST = "Divisibilidade, MMC e MDC do Zero"


def mix_cor(k):
    return M.mix(E.COR, '#FFFFFF', 0.35 * k)


def lupa(c, x, y, r, cor, a):
    c.drawCircle(x, y, r, M.paint(cor, a, stroke=7))
    M.line(c, x + r * 0.7, y + r * 0.7, x + r * 1.5, y + r * 1.5, cor, a, 8)


def b_cta(c, t, C, b):
    a_, b_, c_ = (C[f"s05.{k}"] for k in "abc")
    E.frase(c, t, a_ - 0.1, [("procure no", "i", 76, TINTA2), ("YouTube", "g", 80, TINTA)], CX, 260, "center", 0.12)
    # barra de busca digitando
    ab = ep(t, a_, 0.4)
    if ab > 0:
        x, y, w, h = 110, 340, W - 220, 130
        M.rrect(c, x, y, w, h, h / 2, BR, ab, shadow=True)
        M.rrect(c, x, y, w, h, h / 2, None, ab, stroke=3, stroke_color=E.FIO)
        lupa(c, x + 75, y + 58, 24, CINZA, ab)
        n = int(len(BUSCA) * clamp(prog(t, a_ + 0.35, 0.9)))
        E.escreve(c, BUSCA[:n], x + 140, y + 88, 66, "g", TINTA, ab)
        if (t * 2) % 1 < 0.6:
            xc = x + 140 + E.larg(BUSCA[:n], "g", 66) + 6
            M.rrect(c, xc, y + 34, 5, 64, 2, E.COR, ab)
    # cartão da playlist
    ap = ease_out(prog(t, b_, 0.5))
    if ap > 0:
        y0 = 560 + 60 * (1 - ap)
        x, w, h = 110, W - 220, 700
        cw, ch = w - 80, (w - 80) * 9 / 16
        for k, d in ((2, 28), (1, 14)):  # bordas das capas de trás: a pilha da playlist
            M.rrect(c, x + 40 + d, y0 + 40 - d, cw - 2 * d, ch, 18, mix_cor(k), ap)
        rr = skia.Rect.MakeXYWH(x + 40, y0 + 40, cw, ch)
        c.save(); c.clipRRect(skia.RRect.MakeRectXY(rr, 18, 18), True)
        pt = skia.Paint(); pt.setAlphaf(ap)
        c.drawImageRect(capa(2), rr, SAMP, pt)
        c.restore()
        E.pilula(c, "PLAYLIST · 8 AULAS", x + w / 2, y0 + 40 + ch + 62, 36, estilo="g", fundo=E.COR, cor=BR, a=ap)
        centro(c, "Divisibilidade,", x + w / 2, y0 + h - 76, 58, "g", TINTA, ap)
        centro(c, "MMC e MDC do Zero", x + w / 2, y0 + h - 10, 58, "g", COR, ap)
    # inscreva-se com clique
    ti = b_ + 1.6
    s = pop(t, ti, 0.45)
    if s > 0:
        clk = 1 - 0.06 * math.sin(math.pi * clamp(prog(t, ti + 0.9, 0.25)))
        c.save(); c.translate(CX, 1370); c.scale(s * clk, s * clk)
        inscrito = t >= ti + 1.0
        E.pilula(c, "INSCRITO ✓" if inscrito else "INSCREVA-SE", 0, 0, 64, estilo="g",
                 fundo=TINTA2 if inscrito else E.ERRADO, cor=BR)
        c.restore()
        p = ease_io(prog(t, ti + 0.2, 0.7))
        E.cursor(c, lerp(900, CX + 150, p), lerp(1520, 1405, p), ep(t, ti + 0.1, 0.3))


BLOCKS = dict(desafio=b_desafio, macete=b_macete, virada=b_virada, trilha=b_trilha, cta=b_cta)


# ---------------- legenda queimada (palavra a palavra) ----------------
def _limpa(s):
    return s.replace("*", "")


def CAPTION(c, s, t):
    toks = s["tokens"]
    if not toks:
        return
    rel = t - s["start"]
    # grupos de até 3 palavras / 20 caracteres, quebrando depois de pontuação
    grupos, g = [], []
    for i, tk in enumerate(toks):
        g.append(i)
        txt = " ".join(_limpa(toks[j]["disp"]) for j in g)
        if len(g) >= 3 or len(txt) >= 18 or tk["disp"].rstrip("*")[-1:] in ",.:?!…":
            grupos.append(g); g = []
    if g:
        grupos.append(g)
    atual = None
    for gi, g in enumerate(grupos):
        ini = toks[g[0]]["t0"] - 0.05
        fim = grupos[gi + 1] and toks[grupos[gi + 1][0]]["t0"] - 0.05 if gi + 1 < len(grupos) else toks[g[-1]]["t1"] + 0.6
        if ini <= rel < fim:
            atual = g
            break
    if atual is None:
        return
    escuro = s["block"] == "macete"
    size, y = 72, 1560
    pal = [_limpa(toks[j]["disp"]) for j in atual]
    ws = [E.larg(p, "g", size) for p in pal]
    esp = size * 0.28
    total = sum(ws) + esp * (len(ws) - 1)
    x = CX - total / 2
    # faixa de fundo para ler sobre qualquer tela
    M.rrect(c, x - 34, y - size - 12, total + 68, size + 52, 28, "#07070F" if not escuro else BR, 0.9 if not escuro else 0.95)
    for j, p, w in zip(atual, pal, ws):
        dita = toks[j]["t0"] <= rel
        cor = (CLARO if not escuro else E.COR) if dita else (BR if not escuro else TINTA)
        if toks[j]["t0"] <= rel < toks[j]["t1"] + 0.05:
            cor = "#FFD23F" if not escuro else E.COR
        E.escreve(c, p, x, y, size, "g", cor)
        x += w + esp
