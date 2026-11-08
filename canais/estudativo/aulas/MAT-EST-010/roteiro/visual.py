"""Visual — Estudativo · MAT-EST-010: média geométrica e média harmônica.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): conta da vez à direita, resposta na esfera,
atalho no palco escuro, fichas brancas para a lista de dados, barra de 100% (barra100()) para dividir um total.
Novo nesta aula:
- MÉDIA = TROCAR POR IGUAIS: as colunas 4 e 9 viram duas colunas de 6,5 (a soma fica); o retângulo 4 x 9 vira o quadrado
  6 x 6 (a área, que é o produto, fica). É o que cada média guarda.
- CRESCIMENTO = FRASCOS (frasco()): a cultura de bactérias em três frascos, com as pontes ×2 e ×8.
- VELOCIDADE = ESTRADA (estrada()): o carro vai numa faixa e volta na outra; o tempo de cada km num cronômetro (cronometro()).
- ORDEM DAS MÉDIAS na E.reta: H < G < A.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-010_media_geometrica_e_harmonica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "crescimento", "harmonica", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
assert (4 + 9) / 2 == 6.5 and 6.5 + 6.5 == 13 and 4 * 9 == 36 == 6 * 6 and 2 * 4 * 8 == 64 == 4 ** 3
assert 2 * 8 == 16 and (2 + 8) / 2 == 5 and 5 * 5 == 25 and 4 * 4 == 16
assert (1 + 1.5) / 2 == 1.25 and 60 / 1.25 == 48 and 2 * 40 * 60 == 4800 and 4800 / (40 + 60) == 48
assert abs(1 / 40 + 1 / 60 - 1 / 24) < 1e-12 and 2 * 24 == 48 and 48 < (40 * 60) ** 0.5 < 50
assert 3 * 12 == 36 and 2 * 12 * 24 == 576 and 12 + 24 == 36 and 576 / 36 == 16 and (12 + 24) / 2 == 18


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³ ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def ficha(c, s, cx, cy, size, a=1.0, cor=None, borda=None):
    """um dado da lista: pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


def barra100(c, t, t0, x, y, w, h, partes, cores=None, rotulos=None, size=46, d=1.0, a=1.0):
    """frequência relativa: barra deitada de 100% dividida nas fatias (partes), cada fatia no seu tempo, com o rótulo dentro"""
    cores = cores or E._paleta(len(partes))
    tot = float(sum(partes))
    ts = t0 if isinstance(t0, (list, tuple)) else [t0 + d * i / len(partes) for i in range(len(partes))]
    xa = x
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    if t >= min(ts):
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.mix(FIO, PAPEL, 0.5), a))
        for i, v in enumerate(partes):
            wi = w * v / tot
            q = ease_io(prog(t, ts[i], 0.5))
            if q > 0:
                c.drawRect(skia.Rect.MakeXYWH(xa, y, wi * q, h), M.paint(cores[i], a))
            xa += wi
        c.restore()
        xa = x
        for i, v in enumerate(partes):
            wi = w * v / tot
            if i:
                M.line(c, xa, y, xa, y + h, PAPEL, a * ep(t, ts[i], 0.4), 5)
            s = rotulos[i] if rotulos else E._num(v) + "%"
            cor_t = BR if M.lum(cores[i]) < 0.5 else TINTA
            E.foco(c, t, ts[i] + 0.3, 0.4, lambda q, s=s, xa=xa, wi=wi, cor_t=cor_t: centro(c, s, xa + wi / 2, y + h / 2 + size * 0.36, size, "g", cor_t, q * a))
            xa += wi
        c.drawRRect(r, M.paint(TINTA, a * ep(t, min(ts), 0.4), stroke=3))


# ---------------- peças desta aula ----------------
def colunas_media(c, t, t0, tm, x, base, vals, media, u=50, bw=150, gap=90, size=60):
    """duas colunas (vals) que, em tm, viram colunas iguais à média: a soma fica"""
    q = ease_io(prog(t, tm, 1.0))
    for i, v in enumerate(vals):
        k = ease_back(prog(t, t0 + 0.15 * i, 0.6))
        if k <= 0:
            continue
        h = lerp(v, media, q) * u * min(1.0, k)
        cx = x + i * (bw + gap) + bw / 2
        M.rrect(c, cx - bw / 2, base - h, bw, h, 12, E.COR, 1.0)
        c.drawRect(skia.Rect.MakeXYWH(cx - bw / 2, base - 12, bw, 12), M.paint(E.COR))
        s = E._num(v) if q < 0.5 else E._num(media)
        centro(c, s, cx, base - h - 24, size, "g", COR if q >= 0.5 else TINTA, min(1.0, k) * (1 - 2 * min(q, 1 - q) * 0.9))
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x - 30, base, x + 2 * bw + gap + 30, base, TINTA, p, 5)


def ret_quadrado(c, t, t0, tm, cx, base, u=62):
    """o retângulo 4 x 9 que, em tm, vira o quadrado 6 x 6: a área (o produto, 36) fica"""
    k = ease_io(prog(t, t0, 0.6))
    if k <= 0:
        return
    q = ease_io(prog(t, tm, 1.1))
    lw, lh = lerp(9, 6, q), lerp(4, 6, q)
    w, h = lw * u, lh * u * k
    x, y = cx - w / 2, base - h
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.mix(E.COR, PAPEL, 0.82)))
    for nc, nl, al in ((9, 4, 1 - q), (6, 6, q)):
        if al <= 0.02:
            continue
        for i in range(1, nc):
            M.line(c, x + w * i / nc, y, x + w * i / nc, y + h, E.mix(E.COR, PAPEL, 0.55), al, 2)
        for j in range(1, nl):
            M.line(c, x, y + h * j / nl, x + w, y + h * j / nl, E.mix(E.COR, PAPEL, 0.55), al, 2)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.COR, 1, stroke=6))
    if k > 0.95:
        lb = ("9", "4") if q < 0.5 else ("6", "6")
        al = 1 - 2 * min(q, 1 - q) * 0.9
        centro(c, lb[0], cx, base + 70, 60, "g", TINTA, al)
        E.escreve(c, lb[1], x - 30 - E.larg(lb[1], "g", 60), y + h / 2 + 22, 60, "g", TINTA, al)


def frasco(c, cx, cy, s, n, a=1.0, cresce=1.0):
    """frasco de cultura com n bactérias (bolinhas) dentro; (cx, cy) = centro do corpo; s = escala"""
    if a <= 0:
        return
    bw, bh, nw, nh = 230 * s, 220 * s, 96 * s, 64 * s
    corpo = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - bw / 2, cy - bh / 2, bw, bh), 46 * s, 46 * s)
    c.drawRRect(corpo, M.paint(E.mix(E.COR, PAPEL, 0.88), a))
    c.drawRect(skia.Rect.MakeXYWH(cx - nw / 2, cy - bh / 2 - nh + 6 * s, nw, nh), M.paint(BR, a))
    pt = M.paint(TINTA, a, stroke=6 * s)
    c.drawRRect(corpo, pt)
    M.line(c, cx - nw / 2, cy - bh / 2 + 2, cx - nw / 2, cy - bh / 2 - nh, TINTA, a, 6 * s)
    M.line(c, cx + nw / 2, cy - bh / 2 + 2, cx + nw / 2, cy - bh / 2 - nh, TINTA, a, 6 * s)
    M.line(c, cx - nw / 2 - 14 * s, cy - bh / 2 - nh, cx + nw / 2 + 14 * s, cy - bh / 2 - nh, TINTA, a, 8 * s)
    lado = max(1, math.ceil(math.sqrt(n)))
    linhas = math.ceil(n / lado)
    p = 40 * s
    for k in range(n):
        i, j = k % lado, k // lado
        x = cx + (i - (lado - 1) / 2) * p
        y = cy + 10 * s + (j - (linhas - 1) / 2) * p
        r = 14 * s * ease_back(min(1.0, max(0.0, cresce * n - k)) if n > 1 else cresce)
        if r > 0:
            c.drawCircle(x, y, r, M.paint(E.COR, a))


def carro(c, x, y, a=1.0, vira=False):
    if a <= 0:
        return
    d = -1 if vira else 1
    M.rrect(c, x - 52, y - 30, 104, 40, 14, E.COR, a)
    M.rrect(c, x - 10 * d - 30, y - 56, 60, 34, 12, E.COR, a)
    M.rrect(c, x - 10 * d - 20, y - 48, 40, 18, 6, BR, a)
    for dx in (-30, 30):
        c.drawCircle(x + dx, y + 12, 13, M.paint(TINTA, a))
        c.drawCircle(x + dx, y + 12, 5, M.paint(BR, a))


def estrada(c, t, t0, x0, x1, y, ti, tv, a=1.0):
    """estrada de A até B: o carro vai pela faixa de cima (a partir de ti) e volta pela de baixo (a partir de tv)"""
    p = ep(t, t0, 0.6) * a
    if p <= 0:
        return
    M.rrect(c, x0, y - 60, x1 - x0, 120, 30, E.mix(TINTA2, PAPEL, 0.25), p)
    M.line(c, x0 + 40, y, x1 - 40, y, BR, p, 6, dash=[30, 24])
    for x, s in ((x0, "A"), (x1, "B")):
        c.drawCircle(x, y, 46, M.paint(TINTA, p))
        centro(c, s, x, y + 18, 50, "g", BR, p)
    ida, volta = ease_io(prog(t, ti, 1.6)), ease_io(prog(t, tv, 1.2))
    if t >= ti and t < tv:
        carro(c, lerp(x0 + 110, x1 - 110, ida), y - 22, a)
    elif t >= tv:
        carro(c, lerp(x1 - 110, x0 + 110, volta), y + 50, a, vira=True)


def cronometro(c, cx, cy, r, frac, a=1.0, cor=None):
    """cronômetro: o arco cheio até frac (1 volta = 2 minutos)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR, a))
    if frac > 0:
        p = skia.Path()
        p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * frac, False)
        p.close()
        c.drawPath(p, M.paint(E.mix(cor or E.COR, PAPEL, 0.3 if (cor or E.COR) == E.COR else 0.6), a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=7))
    M.rrect(c, cx - 18, cy - r - 30, 36, 24, 6, TINTA, a)
    ang = math.radians(-90 + 360 * frac)
    M.line(c, cx, cy, cx + r * 0.8 * math.cos(ang), cy + r * 0.8 * math.sin(ang), TINTA, a, 7)
    c.drawCircle(cx, cy, 10, M.paint(TINTA, a))


def ponto_reta(c, t, t0, vx, v, y, rot, cor, acima=True, size=48, oco=False, alto=70):
    k = ease_back(prog(t, t0, 0.4))
    if k <= 0:
        return
    if oco:
        c.drawCircle(vx(v), y, 18 * k, M.paint(PAPEL))
        c.drawCircle(vx(v), y, 18 * k, M.paint(cor, 1, stroke=6))
    else:
        c.drawCircle(vx(v), y, 18 * k, M.paint(cor))
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: centro(c, rot, vx(v), y - alto if acima else y + alto + size, size, "g", cor, a), sobe=6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a1, [("4", "g", 150, COR), ("e", "i", 120), ("9", "g", 150, COR)], W / 2, 290, "center", 0.15)
        for i, (ti, s, rot) in enumerate(((b1, "6,5", "a de sempre"), (c1, "6", "outra média"), (d1, "48", "40 e 60 km/h"))):
            x = 460 + 500 * i
            bola_txt(c, t, ti, s, x, 600, 130, 96)
            E.frase(c, t, ti + 0.3, ps(rot, "i", 50, TINTA2), x, 820, "center", 0.08)
        E.frase(c, t, d1 + 1.0, ps("uma terceira média", "i", 44, TINTA2), 1460, 890, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.4, [("qual média", "g", 100, COR)] + ps("usar", "i", 88), XE, 450, passo=0.14)
        E.frase(c, t, ta + 2.4, ps("em cada situação", "i", 88), XE, 590, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "a média aritmética:", "soma ÷ quantidade"), ("s03.c", "a raiz quadrada e a cúbica:", "r{9} = 3     r3{8} = 2"),
             ("s03.d", "a velocidade média:", "distância total ÷ tempo total"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 200 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 50), x + 40, y + 74, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 40, y + 160, 54, "g", COR)
    alvo = [200 + i * 240 + 170 for i in range(3)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    q2 = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 1000, "left", 0.1)


# ---------------- a ideia de toda média ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.2, ps("toda média faz", "i", 74) + [("a mesma coisa", "g", 80, COR)], W / 2, 190, "center", 0.1)
    colunas_media(c, t, a4, c4, 300, 900, (4, 9), 6.5)
    if t >= c4 + 0.6:   # a linha da média
        p = ep(t, c4 + 0.6, 0.6)
        y = 900 - 6.5 * 50
        M.line(c, 260, y, lerp(260, 750, p), y, TINTA2, 1, 4, dash=E.TRACO)
    X = 1340
    E.frase(c, t, a4, ps("troca vários números", "i", 58), X, 350, "center", 0.1)
    E.frase(c, t, a4 + 1.2, ps("por um só,", "i", 58) + [("repetido", "g", 62, COR)], X, 430, "center", 0.1)
    E.frase(c, t, b4, ps("a aritmética guarda", "i", 58) + [("a soma", "g", 62, COR)], X, 590, "center", 0.1)
    fcen(c, t, b4 + 1.0, "4 + 9 = 13", X, 720, 84)
    fcen(c, t, c4, "6,5 + 6,5 = 13", X, 860, 84, COR)


# ---------------- geométrica ----------------
def b_geometrica(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a5, [("média geométrica", "g", 76, COR)] + ps("guarda o", "i", 70) + [("produto", "g", 76)], W / 2, 190, "center", 0.1)
        ret_quadrado(c, t, b5, c5, 560, 820)
        E.foco(c, t, b5 + 0.6, 0.4, lambda a: centro(c, "36", 560, 820 - lerp(4, 6, ease_io(prog(t, c5, 1.1))) * 62 / 2 + 30, 80, "g", COR, a))
        X = 1400
        fcen(c, t, b5, "4 × 9 = 36", X, 380, 88)
        E.frase(c, t, lerp(b5, c5, 0.45), ps("que número, vezes ele mesmo?", "i", 50, TINTA2), X, 490, "center", 0.08)
        fcen(c, t, c5, "6 × 6 = 36", X, 630, 88, COR)
        fcen(c, t, d5, "G = r{4 · 9} = r{36} = 6", X, 820, 74, COR)
        E.frase(c, t, d5 + 0.6, ps("a raiz quadrada do produto", "i", 48, TINTA2), X, 920, "center", 0.08)
    fase(c, t, C["s05"], C["s06"] - 0.1, um)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("3 números →", "i", 72) + [("raiz cúbica", "g", 78, COR)], W / 2, 190, "center", 0.1)
    for i, s in enumerate(("2", "4", "8")):
        E.foco(c, t, a6 + 0.25 * i, 0.4, lambda a, s=s, i=i: ficha(c, s, 760 + 200 * i, 330, 72, a), sobe=30)
    fcen(c, t, b6, "2 × 4 × 8 = 64", W / 2, 540, 100)
    fcen(c, t, c6, "r3{64} = 4", W / 2, 720, 120, COR)
    fcen(c, t, lerp(c6, d6, 0.4), "4 × 4 × 4 = 64", W / 2, 820, 60, TINTA2)
    E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "multiplique todos e tire a raiz de índice = quantidade", W / 2, 950, 44, "g", a=a, cor=E.SOBRE))


# ---------------- crescimento ----------------
FX = (440, 960, 1480)


def b_crescimento(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s07"] + 0.2, ps("onde ela aparece? quando os números", "i", 62) + [("multiplicam", "g", 68, COR)],
                W / 2, 180, "center", 0.08)
        for i, (ti, n, rot) in enumerate(((a7, 1, "início"), (b7, 2, "dia 1"), (c7, 16, "dia 2"))):
            E.foco(c, t, ti, 0.5, lambda a, i=i, n=n, ti=ti: frasco(c, FX[i], 470, 1.15, n, a, prog(t, ti + 0.3, 0.8)), sobe=20)
            E.foco(c, t, ti + 0.2, 0.4, lambda a, i=i, rot=rot: centro(c, rot, FX[i], 680, 50, "i", TINTA2, a))
        E.ponte(c, t, b7, FX[0] + 150, FX[1] - 150, 480, "×2", size=52)
        E.ponte(c, t, c7, FX[1] + 150, FX[2] - 150, 480, "×8", size=52)
        E.chave(c, FX[0] - 130, FX[2] + 130, 740, TINTA, ep(t, d7, 0.6), 40, 6)
        E.foco(c, t, d7 + 0.3, 0.5, lambda a: E.pilula(c, "×16 no fim", W / 2, 870, 64, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, C["s08"] + 0.1, ps("crescimento", "i", 66) + [("médio por dia?", "g", 70, COR)], W / 2, 180, "center", 0.1)
    E.foco(c, t, C["s08"] + 0.4, 0.4, lambda a: E.formula(c, "×2  depois  ×8  =  ×16", W / 2, 270, 52, "g", TINTA2, a, "center"))
    L, R = 540, 1380
    E.frase(c, t, a8, [("aritmética", "g", 60)], L, 400, "center")
    fcen(c, t, a8 + 0.4, "(2 + 8) ÷ 2 = 5", L, 520, 74)
    fcen(c, t, b8, "×5 ×5 = ×25", L, 680, 78, ERRADO)
    E.foco(c, t, b8 + 0.6, 0.5, lambda a: E.selo(c, L - 150, 820, 44, False, a))
    E.frase(c, t, b8 + 0.7, ps("não dá 16", "i", 56, ERRADO), L - 80, 840, "left", 0.1)
    E.frase(c, t, c8, [("geométrica", "g", 60, COR)], R, 400, "center")
    fcen(c, t, c8 + 0.4, "r{16} = 4", R, 520, 80, COR)
    fcen(c, t, d8, "×4 ×4 = ×16", R, 680, 78, CERTO)
    E.foco(c, t, d8 + 0.6, 0.5, lambda a: E.selo(c, R - 150, 820, 44, True, a))
    E.frase(c, t, d8 + 0.7, ps("bate", "i", 56, CERTO), R - 80, 840, "left", 0.1)
    E.foco(c, t, lerp(d8, C["s08.end"], 0.45), 0.5, lambda a: E.pilula(c, "guarda o efeito total", W / 2, 960, 52, "g", a=a, cor=E.SOBRE))


# ---------------- harmônica ----------------
def b_harmonica(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")

    def um():
        E.frase(c, t, a9, [("média harmônica", "g", 80, COR)], W / 2, 180, "center")
        E.frase(c, t, a9 + 0.8, ps("velocidades em trechos de", "i", 54) + [("mesma distância", "g", 58)], W / 2, 260, "center", 0.08)
        estrada(c, t, a9 + 0.6, 300, 1620, 520, b9, c9)
        E.foco(c, t, b9, 0.4, lambda a: E.pilula(c, "ida: 40 km/h", 960, 395, 50, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, c9, 0.4, lambda a: E.pilula(c, "volta: 60 km/h", 960, 650, 50, "g", fundo=TINTA2, a=a))
        E.frase(c, t, d9, ps("média da viagem:", "i", 62) + [("48", "g", 84, COR)], 860, 820, "center", 0.1)
        E.foco(c, t, d9 + 0.6, 0.4, lambda a: E.escreve(c, "não 50", 1260, 820, 64, "g", ERRADO, a))
        if t >= d9 + 1.0:
            E.risco(c, 1250, 800, 1490, 780, t, d9 + 1.0, largura=9)
        E.frase(c, t, lerp(d9, C["s09.end"], 0.5), ps("mesmo tempo em cada velocidade? aí sim, a aritmética", "i", 46, TINTA2), W / 2, 950, "center", 0.06)
    fase(c, t, C["s09"], C["s10"] - 0.1, um)

    def dois():
        E.frase(c, t, a0, ps("pense em", "i", 72) + [("minutos por km", "g", 78, COR)], W / 2, 180, "center", 0.1)
        for i, (ti, v, m, f) in enumerate(((b0, "60 km/h", "1 km = 1 min", 0.5), (c0, "40 km/h", "1 km = 1,5 min", 0.75))):
            x = 600 + 720 * i
            E.foco(c, t, ti, 0.5, lambda a, x=x, f=f, ti=ti: cronometro(c, x, 400, 120, f * ease_io(prog(t, ti + 0.2, 1.0)), a, E.COR if i == 0 else TINTA2))
            E.frase(c, t, ti + 0.2, [(v, "b", 54, TINTA2)], x, 600, "center")
            fcen(c, t, ti + 0.5, m, x, 690, 70, COR)
        fcen(c, t, d0, "média: 1 min 15 s = 1,25 min", W / 2, 830, 66)
        fcen(c, t, e0, "60 ÷ 1,25 = 48 km/h", W / 2, 970, 80, COR)
    fase(c, t, C["s10"], C["s11"] - 0.1, dois)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, a1, ps("média dos", "i", 66) + [("inversos", "g", 72, COR)] + ps("e depois inverte de volta", "i", 66), W / 2, 180, "center", 0.1)
    fcen(c, t, b1, "40  →  f{1}{40}", 520, 420, 100)
    E.frase(c, t, b1 + 0.8, ps("a fração virada", "i", 46, TINTA2), 520, 520, "center", 0.08)
    fcen(c, t, c1, "H = n ÷ (f{1}{a} + f{1}{b} + ...)", 1340, 420, 84, COR)
    E.frase(c, t, c1 + 0.8, ps("n = quantos números", "i", 46, TINTA2), 1340, 560, "center", 0.08)
    fcen(c, t, d1, "f{1}{40} + f{1}{60} = f{3}{120} + f{2}{120} = f{5}{120} = f{1}{24}", W / 2, 730, 76)
    fcen(c, t, e1, "2 ÷ f{1}{24} = 2 × 24 = 48", W / 2, 920, 86, COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 170, "center", 0.1)
    E.frase(c, t, a2, ps("a aritmética para", "i", 60) + [("tudo", "g", 64, ERRADO)], W / 2, 260, "center", 0.1)
    fcen(c, t, b2, "(40 + 60) ÷ 2 = 50", 880, 410, 84, ERRADO)
    E.foco(c, t, b2 + 0.6, 0.5, lambda a: E.selo(c, 1420, 385, 46, False, a))
    E.foco(c, t, c2, 0.4, lambda a: E.escreve(c, "o tempo de cada km", 310, 510, 44, "i", TINTA2, a))
    barra100(c, t, [c2, c2 + 0.6], 310, 540, 1300, 100, [60, 40], [E.COR, TINTA2], ["40 km/h: 1,5 min", "60 km/h: 1 min"], size=44)
    E.frase(c, t, c2 + 1.0, ps("mais tempo no", "i", 50) + [("trecho lento", "g", 54, COR)], 960, 730, "center", 0.08)
    vx = E.reta(c, t, d2, 360, 1560, 930, 40, 60, [40, 45, 50, 55, 60], size=44)
    ponto_reta(c, t, d2 + 0.6, vx, 50, 930, "50", ERRADO, oco=True)
    ponto_reta(c, t, d2 + 1.0, vx, 48, 930, "48", COR, alto=110)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a3, [("2 valores", "g", 68, BR)] + ps("e a mesma distância", "i", 64, CLARO), W / 2, 270, "center", 0.1)
        fcen(c, t, b3, "f{2 · a · b}{a + b}", W / 2, 470, 120, BR)
        E.frase(c, t, b3 + 0.6, ps("o dobro do produto ÷ a soma", "i", 52, CLARO), W / 2, 610, "center", 0.08)
        fcen(c, t, c3, "2 × 40 × 60 = 4.800", 560, 760, 66, BR)
        fcen(c, t, lerp(c3, d3, 0.5), "40 + 60 = 100", 1380, 760, 66, BR)
        fcen(c, t, d3, "4.800 ÷ 100 = 48", W / 2, 930, 96, BR)
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, a4, ps("é a fórmula da", "i", 62, CLARO) + [("harmônica", "g", 66, BR)] + ps("pronta para 2 números", "i", 62, CLARO), W / 2, 190, "center", 0.1)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 330, 330, 44, False, a))
    E.frase(c, t, b4 + 0.1, ps("3 números ou mais: use a", "i", 56, CLARO) + [("soma dos inversos", "g", 58, BR)], 400, 350, "left", 0.08)
    vx = E.reta(c, t, c4, 360, 1560, 680, 47, 51, [47, 48, 49, 50, 51], escuro=True, size=44)
    for k, (v, rot) in enumerate(((48, "H = 48"), (2400 ** 0.5, "G ≈ 49"), (50, "A = 50"))):
        ponto_reta(c, t, c4 + 0.6 + 0.5 * k, vx, v, 680, rot, BR if k else CLARO, size=50, alto=60)
    E.frase(c, t, c4 + 2.0, ps("harmônica < geométrica < aritmética", "i", 56, CLARO), W / 2, 900, "center", 0.08)
    E.frase(c, t, c4 + 2.6, ps("(para 40 e 60)", "i", 44, CLARO), W / 2, 980, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, [("1)", "g", 60, COR)] + ps("média geométrica de", "i", 60) + [("3 e 12", "g", 64, COR)], XE, 320, passo=0.1)
    E.frase(c, t, b5, [("2)", "g", 60, COR)] + ps("ciclista sobe a ladeira a", "i", 60) + [("12 km/h", "g", 64, COR)], XE, 450, passo=0.1)
    E.frase(c, t, lerp(b5, c5, 0.5), ps("e desce pelo mesmo caminho a", "i", 60) + [("24 km/h", "g", 64, COR)], XE + 80, 540, passo=0.1)
    E.frase(c, t, c5, ps("velocidade média da", "i", 60) + [("subida e descida?", "g", 62)], XE + 80, 650, passo=0.1)
    E.relogio(c, t, C["s16.a"], 1560, 780, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s17.{k}"] for k in "abcdef")
    a8, b8 = C["s18.a"], C["s18.b"]
    L, R = 480, 1360

    def um():
        E.foco(c, t, a7, 0.5, lambda q: E.pilula(c, "1)", L, 220, 60, "g", a=q, cor=E.SOBRE))
        fcen(c, t, a7, "3 × 12 = 36", L, 420, 80)
        fcen(c, t, b7, "r{36} = 6", L, 580, 80)
        bola_txt(c, t, b7 + 0.5, "6", L, 780, 110, 110)
        if t >= c7 - 0.2:
            M.line(c, 900, 200, 900, 960, FIO, ep(t, c7 - 0.2, 0.4), 3)
        E.foco(c, t, c7, 0.5, lambda q: E.pilula(c, "2)", R, 220, 60, "g", a=q, cor=E.SOBRE))
        E.frase(c, t, c7, ps("mesma distância →", "i", 54) + [("harmônica", "g", 58, COR)], R, 340, "center", 0.08)
        fcen(c, t, d7, "2 × 12 × 24 = 576", R, 480, 70)
        fcen(c, t, e7, "12 + 24 = 36", R, 600, 70)
        fcen(c, t, f7, "576 ÷ 36 = 16", R, 740, 78, COR)
        E.foco(c, t, f7 + 0.6, 0.5, lambda q: E.pilula(c, "16 km/h", R, 880, 70, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s17"], C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.1, ps("confira:", "i", 70, COR), W / 2, 200, "center")
    fcen(c, t, a8, "16 < 18", W / 2, 380, 120)
    E.frase(c, t, a8 + 0.6, ps("18 = (12 + 24) ÷ 2, a aritmética", "i", 48, TINTA2), W / 2, 470, "center", 0.06)
    vx = E.reta(c, t, a8, 360, 1560, 700, 10, 26, [12, 16, 18, 24], size=44)
    ponto_reta(c, t, a8 + 0.6, vx, 18, 700, "", TINTA2)
    ponto_reta(c, t, a8 + 0.9, vx, 16, 700, "", E.COR)
    E.foco(c, t, a8 + 1.0, 0.4, lambda a: (E.escreve(c, "harmônica", vx(16) + 10 - E.larg("harmônica", "g", 44), 640, 44, "g", COR, a),
                                           E.escreve(c, "aritmética", vx(18) + 20, 640, 44, "g", TINTA2, a)))
    E.foco(c, t, b8, 0.5, lambda a: E.selo(c, 640, 900, 44, True, a))
    E.frase(c, t, b8 + 0.1, ps("faz sentido:", "i", 58) + [("a subida demora mais", "g", 60, COR)], 710, 922, "left", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("aritmética", "g", 70, COR)] + ps("guarda a soma", "i", 64)),
                 ("s19.b", [("geométrica", "g", 70, COR)] + ps("guarda o produto", "i", 64)),
                 ("s19.c", [("harmônica", "g", 70, COR)] + ps("velocidades em distâncias iguais", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("mediana", "g", 110, COR)], XE, 410)
    E.frase(c, t, a0 + 0.5, ps("o valor do meio da lista em ordem", "i", 50), XE, 490, passo=0.08)
    E.frase(c, t, b0, [("moda", "g", 110, COR)], XE, 660)
    E.frase(c, t, b0 + 0.5, ps("o valor que mais aparece", "i", 50), XE, 740, passo=0.08)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, geometrica=b_geometrica, crescimento=b_crescimento,
              harmonica=b_harmonica, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
