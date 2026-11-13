"""Short da questão 153 do ENEM 2025 (2º dia, caderno amarelo) — 1080x1920, ~1 min, render.py --vertical.
Modelo do Short antigo de questão (canais/enem/questoes/041): print da questão com marca-texto, alternativas com contagem
para pausar, o código montado em casas grandes e destacado (linha "2 · 08 · 109 · 0" crescendo embaixo), a letra D,
a armadilha (E, A e C), o atalho no palco escuro e o convite para a resolução completa.
Legenda queimada palavra a palavra em y≈1560. Todo instante vem de C[...] (marcadores do roteiro)."""
import math
from functools import lru_cache
from pathlib import Path

import skia
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ep, prog, lerp, ease_io, ease_out, ease_back, centro, clamp
import motor as M

E.usar("Matemática", "Questões do ENEM")
COR, CLARO = E.COR_TEXTO, E.CLARO
BR = "#FFFFFF"
ARQUIVO_FINAL = "estudativo_ENEM2025_questao153_short.mp4"
MARCA = ""
ENTRADA_SECA = True
CX = W / 2
CODIGO = "2081090"
ALT = (("A", "0109082"), ("B", "0281090"), ("C", "1010982"), ("D", "2081090"), ("E", "2810910"))
assert "2" + "08" + "109" + "0" == CODIGO == dict(ALT)["D"]
assert [l for l, x in ALT if x[0] == "2"] == ["D", "E"] and [l for l, x in ALT if x[:2] == "20"] == ["D"]
assert "2" + "8" + "109" + "10" == dict(ALT)["E"] and "0" + "109" + "08" + "2" == dict(ALT)["A"] and "10" + "109" + "8" + "2" == dict(ALT)["C"]

# Som de Short (todo Short leva trilha + efeitos): batida desde o 1º segundo, trilha presente, -14 LUFS.
# Efeitos acertados com o desenho: marca-texto (data), contagem para pausar (tick), cada pedaço do código (pop),
# o código e a letra D (impact + confirm), armadilha (deny), cortes do atalho (deny), clique no inscreva-se.
SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={
    "s01.a": ["impact@+0.05"], "s01.b": ["data"], "s01.c": ["data"], "s01.d": ["alert"],
    "s02.a": ["whoosh@-0.1"], "s02.b": ["pop"], "s02.c": [f"tick@+{1.0 + k:.2f}" for k in range(3)],
    "s03.b": ["pop@+0.3"], "s03.c": ["pop@+0.3", "pop@+0.55"], "s03.d": ["pop@+0.2", "pop@+0.5", "pop@+0.8"],
    "s03.e": ["pop@+0.6"], "s04.a": ["impact@+0.3"], "s04.b": ["confirm", "shimmer@+0.3"],
    "s05.b": ["deny@+0.4"], "s05.c": ["deny"], "s05.d": ["deny@+0.3", "deny@+0.7"],
    "s06.a": ["whoosh@-0.15"], "s06.b": ["deny", "deny@+0.25", "deny@+0.5"], "s06.d": ["deny", "confirm@+0.4"],
    "s07.a": ["pop@+0.8"], "s07.b": ["lock", "click@+2.55", "notif@+2.65"],
})

RESOLUCAO = Path(__file__).resolve().parents[2] / "ENEM2025-153" / "youtube"
ENUNCIADO = Path(__file__).resolve().parents[2] / "ENEM2025-153" / "enunciado" / "questao.png"
MARCA_TEXTO = "#FFE45C"
CERTO_V = "#1E9E5A"

SAMP = skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear)
_ESCURO = []  # intervalos em que o fundo é o palco escuro (legenda clara)


@lru_cache(None)
def capa():  # a capa publicada da resolução (renomeada) ou, se não houver, a capa A
    p = next(iter(sorted(q for q in RESOLUCAO.glob("*.jpg") if not q.name.startswith("capa_"))), None) \
        or next(RESOLUCAO.glob("capa_A*.jpg"))
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


# ---------------- casas e alternativas ----------------
GRUPOS = (("andar", 1, "2º andar"), ("setor", 2, "setor 08"), ("funcionário", 3, "func. 109"), ("turno", 1, "manhã = 0"))


def casas(c, t, t0, y, bw, bh, digs=None, gap=10, ggap=30, cor_dig=TINTA):
    """as 7 casas agrupadas; devolve (x0, x1) de cada grupo"""
    total = 7 * bw + 3 * gap + 3 * ggap
    x, gs, i = (W - total) / 2, [], 0
    for _, n, _ in GRUPOS:
        g0 = x
        for k in range(n):
            s_ = pop(t, t0 + 0.05 * i, 0.4)
            if s_ > 0:
                c.save(); c.translate(x + bw / 2, y + bh / 2); c.scale(s_, s_)
                M.rrect(c, -bw / 2, -bh / 2, bw, bh, 16, BR, 1, shadow=True)
                M.rrect(c, -bw / 2, -bh / 2, bw, bh, 16, None, 1, stroke=4, stroke_color=E.COR)
                if digs:
                    centro(c, digs[i], 0, bh * 0.22, bh * 0.62, "g", cor_dig)
                c.restore()
            x += bw + (gap if k < n - 1 else ggap)
            i += 1
        gs.append((g0, x - ggap))
    return gs


def alternativas(c, t, x0, y0, dy, dx, sz, ta, cortes=None, certo_t=None, escuro=False, rb=None):
    """as cinco alternativas, uma por linha; cortes = {letra: instante do risco}"""
    cortes = cortes or {}
    rb = rb or sz * 0.48
    for k, (l, x) in enumerate(ALT):
        y = y0 + k * dy
        a = ep(t, ta + 0.08 * k, 0.4)
        if a <= 0:
            continue
        tc = cortes.get(l)
        fora = tc is not None and t >= tc + 0.3
        aa = a * (0.3 if fora else 1)
        ok = l == "D" and certo_t is not None and t >= certo_t
        E.bola(c, x0 - rb * 2.3, y - sz * 0.36, rb, CERTO if ok else E.COR, aa)
        centro(c, l, x0 - rb * 2.3, y - sz * 0.36 + rb * 0.42, rb * 1.2, "g", BR, aa)
        for i, ch in enumerate(x):
            cor = "#5BE3A4" if ok else (BR if escuro else TINTA)
            centro(c, ch, x0 + i * dx + dx / 2, y, sz, "g", cor, aa)
        if tc is not None and t >= tc:
            E.risco(c, x0 - rb * 3.6, y - sz * 0.3, x0 + 7 * dx + 10, y - sz * 0.42, t, tc, largura=10)


@lru_cache(None)
def img_questao():
    return skia.Image.open(str(ENUNCIADO))


# ---------------- 1. o print da questão, com marca-texto ----------------
PH = 1000
PY = 270


def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")
    E.pilula(c, "ENEM 2025 · questão 153", CX, 200, 40, "g", fundo=E.COR, cor=BR)
    img = img_questao()
    k = PH / img.height()
    pw = img.width() * k
    px = CX - pw / 2
    M.rrect(c, px - 16, PY - 16, pw + 32, PH + 32, 20, BR, 1, shadow=True)
    c.drawImageRect(img, skia.Rect.MakeXYWH(px, PY, pw, PH), skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear))
    for t0, y0, y1 in ((b_, 360, 850), (c_, 878, 1035), (d_, 1055, 1105)):
        p = ease_io(prog(t, t0, 0.6))
        if p > 0:
            c.drawRect(skia.Rect.MakeXYWH(px + 6 * k, PY + y0 * k, (img.width() - 10) * k * p, (y1 - y0) * k), M.paint(MARCA_TEXTO, 0.42))
    # os 4 pedaços e os dados, em letra grande embaixo do print
    for j, (nome, _, dado) in enumerate(GRUPOS):
        x = 150 + j * 260
        E.foco(c, t, b_ + 0.45 * j, 0.4, lambda a, x=x, nome=nome: E.pilula(c, nome, x, 1345, 36, "g", fundo=E.COR, cor=BR, a=a))
        E.foco(c, t, c_ + (0.0, 0.9, 1.8, 3.0)[j], 0.4, lambda a, x=x, dado=dado: centro(c, dado, x, 1440, 40, "g", TINTA, a))


# ---------------- 2. as alternativas, "comenta antes de ver" e a contagem ----------------
def b_opcoes(c, t, C, b):
    a_, b_, c_ = (C[f"s02.{k}"] for k in "abc")
    E.pilula(c, "ENEM 2025 · questão 153", CX, 200, 40, "g", fundo=E.COR, cor=BR)
    E.frase(c, t, b["start"], [("qual é o", "i", 80, TINTA2), ("código?", "g", 90, COR)], CX, 350, "center")
    gs = casas(c, t, b["start"], 410, 104, 120)
    for (nome, _, dado), (g0, g1) in zip(GRUPOS, gs):
        cx = (g0 + g1) / 2
        centro(c, nome, cx, 580, 34, "g", COR)
        E.pilula(c, dado, cx, 650, 30, "b", fundo=TINTA, cor=BR)
    alternativas(c, t, 330, 850, 84, 64, 70, a_ - 0.2)
    E.foco(c, t, b_, 0.4, lambda a: E.pilula(c, "comenta antes de ver!", CX, 1300, 46, "g", fundo=E.ERRADO, cor=BR, a=a))
    # contagem para pausar: 3-2-1
    t3 = c_ + 1.0
    if t >= t3:
        n = 3 - min(2, int(t - t3))
        f = (t - t3) - (3 - n)
        rr = 95 * pop(t, t3 + (3 - n), 0.35)
        E.bola(c, 940, 1010, rr, E.COR)
        E.arco(c, 940, 1010, rr + 20, -90, 360 * (1 - clamp(f)), TINTA, 8)
        if rr > 20:
            centro(c, str(n), 940, 1010 + rr * 0.42, rr * 1.15, "g", BR)


# ---------------- 3. o código montado pedaço por pedaço ----------------
YB, BWS, BHS = 330, 124, 160
GRUPO_DE = (0, 1, 1, 2, 2, 2, 3)
CORES_G = (COR, E.ERRADO, TINTA, CERTO_V)    # uma cor por pedaço, na linha do código


def t_digitos(C):
    return [C["s03.b"] + 0.3, C["s03.c"] + 0.3, C["s03.c"] + 0.55, C["s03.d"] + 0.2, C["s03.d"] + 0.5, C["s03.d"] + 0.8,
            C["s03.e"] + 0.6]


def casas_codigo(c, t, C, t_ap, verde=False):
    td = t_digitos(C)
    total = 7 * BWS + 3 * 10 + 3 * 30
    x, gs, i = (W - total) / 2, [], 0
    for g, (_, n, _) in enumerate(GRUPOS):
        g0 = x
        for k in range(n):
            s_ = pop(t, t_ap + 0.05 * i, 0.4)
            if s_ > 0:
                c.save(); c.translate(x + BWS / 2, YB + BHS / 2); c.scale(s_, s_)
                M.rrect(c, -BWS / 2, -BHS / 2, BWS, BHS, 16, "#E9FFF2" if verde else BR, 1, shadow=True)
                M.rrect(c, -BWS / 2, -BHS / 2, BWS, BHS, 16, None, 1, stroke=6 if verde else 4,
                        stroke_color=CERTO if verde else CORES_G[g])
                if t >= td[i]:
                    k2 = pop(t, td[i], 0.4)
                    centro(c, CODIGO[i], 0, BHS * 0.22 * k2, BHS * 0.62 * k2, "g", CORES_G[g])
                c.restore()
            x += BWS + (10 if k < n - 1 else 30)
            i += 1
        gs.append((g0, x - 30))
    for g, ((nome, _, _), (g0, g1)) in enumerate(zip(GRUPOS, gs)):
        centro(c, nome, (g0 + g1) / 2, YB + BHS + 60, 38, "g", CORES_G[g])
    return gs, td


def linha_codigo(c, t, td, y, size=150):
    """o código crescendo em letra enorme, com os pedaços separados e coloridos"""
    pedacos = ("2", "08", "109", "0")
    ws = [E.larg(p, "g", size) for p in pedacos]
    esp = size * 0.35
    x = CX - (sum(ws) + esp * 3) / 2
    i = 0
    for g, (p, w) in enumerate(zip(pedacos, ws)):
        xx = x
        for ch in p:
            if t >= td[i]:
                k = pop(t, td[i], 0.4)
                E.escreve(c, ch, xx, y, size, "g", CORES_G[g], min(1, k * 1.4))
            xx += E.larg(ch, "g", size)
            i += 1
        if g < 3 and t >= td[i]:
            c.drawCircle(xx + esp / 2, y - size * 0.33, 9, M.paint(CINZA))
        x += w + esp


def b_conta(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s03.{k}"] for k in "abcde")
    E.frase(c, t, a_, [("pedaço", "g", 76, TINTA), ("por pedaço", "i", 76, COR)], CX, 230, "center", 0.15)
    gs, td = casas_codigo(c, t, C, a_)
    # o dado de cada pedaço aparece quando é usado
    for j, ((_, _, dado), (g0, g1), tj) in enumerate(zip(GRUPOS, gs, (b_, c_, d_, e_))):
        E.foco(c, t, tj, 0.4, lambda a, g0=g0, g1=g1, dado=dado, j=j: E.pilula(c, dado, (g0 + g1) / 2, 660, 30, "b", fundo=CORES_G[j], cor=BR, a=a))
    E.foco(c, t, c_ + 1.6, 0.4, lambda a: E.pilula(c, "setor = 2 casas → 08", CX, 760, 42, "g", fundo=E.ERRADO, cor=BR, a=a))
    E.foco(c, t, e_ + 0.2, 0.4, lambda a: E.pilula(c, "manhã = 0", CX, 860, 42, "g", fundo=CERTO_V, cor=BR, a=a))
    E.frase(c, t, a_ + 0.6, [("o código", "i", 64, TINTA2)], CX, 1080, "center")
    linha_codigo(c, t, td, 1260)


# ---------------- 4. o código em destaque e a letra D ----------------
def b_codigo(c, t, C, b):
    a_, b_ = C["s04.a"], C["s04.b"]
    verde = t >= a_ + 0.3
    E.frase(c, t, b["start"], [("o código", "i", 76, TINTA2)], CX, 230, "center")
    gs, td = casas_codigo(c, t, C, -10, verde=verde)
    # o código enorme, numa faixa que pulsa
    p = pop(t, a_ + 0.3, 0.5)
    if p > 0:
        k = p * (1 + 0.02 * math.sin((t - a_) * 6))
        c.save(); c.translate(CX, 900); c.scale(k, k)
        M.rrect(c, -470, -120, 940, 240, 120, CERTO, 1, shadow=True)
        centro(c, CODIGO, 0, 62, 170, "g", BR)
        c.restore()
    s = pop(t, b_, 0.5)
    if s > 0:
        E.bola(c, CX, 1250, 130 * s, CERTO)
        centro(c, "D", CX, 1250 + 56 * s, 150 * s, "g", BR)
        E.selo(c, CX + 140, 1150, 44 * pop(t, b_ + 0.3), True)


# ---------------- 5. a armadilha ----------------
def pedaco(c, x, y, s_, rot, errado, a, dw=62, h=110, size=74):
    w = max(len(s_) * dw + 28, dw * 2 + 10)
    x0 = x + (w - (len(s_) * dw + 28)) / 2   # dígitos centrados na caixa
    cor = E.ERRADO if errado else COR
    M.rrect(c, x, y - h / 2, w, h, 16, "#FFF1F1" if errado else BR, a, shadow=True)
    M.rrect(c, x, y - h / 2, w, h, 16, None, a, stroke=5, stroke_color=cor)
    for i, ch in enumerate(s_):
        centro(c, ch, x0 + 14 + dw * i + dw / 2, y + size * 0.36, size, "g", cor if errado else TINTA, a)
    centro(c, rot, x + w / 2, y + h / 2 + 40, 32, "b", cor, a)
    return w


def linha_alt(c, t, t0, l, pecas, y, escala=1.0):
    a = ep(t, t0, 0.45)
    if a <= 0:
        return
    E.bola(c, 110, y, 50 * escala, E.ERRADO, a)
    centro(c, l, 110, y + 22 * escala, 60 * escala, "g", BR, a)
    x = 190
    for s_, rot, err in pecas:
        x += pedaco(c, x, y, s_, rot, err, a, dw=62 * escala, h=110 * escala, size=74 * escala) + 16


def b_pegadinha(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s05.{k}"] for k in "abcd")
    E.frase(c, t, a_, [("a", "i", 90, TINTA2), ("armadilha", "g", 100, E.ERRADO)], CX, 260, "center", 0.15)
    linha_alt(c, t, b_, "E", [("2", "andar", 0), ("8", "sem o 0!", 1), ("109", "func.", 0), ("10", "hora!", 1)], 470)
    E.foco(c, t, c_, 0.4, lambda a: E.pilula(c, "10 é a hora, não o turno", CX, 680, 46, "g", fundo=E.ERRADO, cor=BR, a=a))
    E.frase(c, t, d_, [("ordem", "g", 70, TINTA), ("invertida", "i", 70, E.ERRADO)], CX, 850, "center", 0.15)
    linha_alt(c, t, d_ + 0.5, "A", [("0", "turno", 1), ("109", "func.", 0), ("08", "setor", 1), ("2", "andar", 1)], 990, 0.85)
    linha_alt(c, t, d_ + 0.9, "C", [("10", "hora!", 1), ("109", "func.", 0), ("8", "setor", 1), ("2", "andar", 1)], 1210, 0.85)


# ---------------- 6. o atalho, no palco ----------------
def b_macete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s06.{k}"] for k in "abcd")
    palco_v(c, t, ep(t, b["start"] - 0.05, 0.35))
    chip(c, t, a_ - 0.1, "atalho", CX, 280, 50, fundo=E.COR, estilo="i")
    E.frase(c, t, a_ + 0.3, [("elimine pelo", "i", 84, CLARO), ("começo", "g", 92, BR)], CX, 430, "center", 0.2)
    x0, y0, dy, dx, sz = 290, 640, 120, 92, 96
    for col, tc_ in ((0, a_ + 1.0), (1, c_)):
        p = ep(t, tc_, 0.4)
        if p > 0:
            M.rrect(c, x0 + col * dx + 2, y0 - sz - 22, dx - 4, dy * 4 + sz + 50, 20, E.COR, 0.6 * p)
    alternativas(c, t, x0, y0, dy, dx, sz, b["start"] - 0.1,
                 cortes={"A": b_, "B": b_ + 0.25, "C": b_ + 0.5, "E": d_}, certo_t=d_ + 0.4, escuro=True, rb=44)
    E.foco(c, t, a_ + 1.3, 0.45, lambda a: E.pilula(c, "1º dígito: andar 2", CX, 1250, 50, "g", fundo=E.COR, cor=BR, a=a))
    E.foco(c, t, c_ + 0.3, 0.45, lambda a: E.pilula(c, "2º dígito: setor 08", CX, 1370, 50, "g", fundo=E.COR, cor=BR, a=a))
    if t >= d_ + 0.4:
        E.selo(c, x0 + 7 * dx + 70, y0 + 3 * dy - 35, 50 * pop(t, d_ + 0.4), True)


# ---------------- 5. convite: busca, playlist, inscreva-se ----------------
BUSCA = "Estudativo"


def mix_cor(k):
    return M.mix(E.COR, '#FFFFFF', 0.35 * k)


def lupa(c, x, y, r, cor, a):
    c.drawCircle(x, y, r, M.paint(cor, a, stroke=7))
    M.line(c, x + r * 0.7, y + r * 0.7, x + r * 1.5, y + r * 1.5, cor, a, 8)


def b_cta(c, t, C, b):
    a_, b_ = C["s07.a"], C["s07.b"]
    E.frase(c, t, a_, [("você", "i", 90, TINTA2), ("acertou?", "g", 100, COR)], CX, 280, "center", 0.15)
    E.foco(c, t, a_ + 0.8, 0.4, lambda a: E.pilula(c, "conta nos comentários 👇".replace(" 👇", ""), CX, 420, 46, "g", fundo=TINTA, cor=BR, a=a))
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
        c.drawImageRect(capa(), rr, SAMP, pt)
        c.restore()
        E.pilula(c, "RESOLUÇÃO COMPLETA", x + w / 2, y0 + 40 + ch + 62, 36, estilo="g", fundo=E.COR, cor=BR, a=ap)
        centro(c, "ENEM 2025", x + w / 2, y0 + h - 76, 58, "g", TINTA, ap)
        centro(c, "questão 153", x + w / 2, y0 + h - 10, 58, "g", COR, ap)
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


BLOCKS = dict(gancho=b_gancho, opcoes=b_opcoes, conta=b_conta, codigo=b_codigo, pegadinha=b_pegadinha, macete=b_macete, cta=b_cta)


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
