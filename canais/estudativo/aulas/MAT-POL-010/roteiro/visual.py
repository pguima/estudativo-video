"""Visual — Estudativo · MAT-POL-010: eixos de simetria e dobraduras (hexágono regular: 6 eixos; 2 dobras e 1 furo: 4 furos).
Linguagem da geometria plana (MAT-ANG-001 a 020, MAT-POL-001 a 009): contornos em tinta; o EIXO de simetria é sempre uma linha
tracejada na cor da matéria (os eixos de vértice a vértice em COR, os de meio a meio de lado em TINTA2, como os dois tipos de
ângulo); pares espelhados com o mesmo número de tracinhos; ângulo reto = quadradinho; erro em vermelho, certo em verde; resposta
na esfera; atalho no palco escuro.
A dobra é animada como no papel: a metade gira sobre o eixo (a largura vai a cos θ) e, quando passa do meio, mostra o verso, mais
escuro, por cima da outra metade. Na folha, cada pedaço guarda os seus furos e recortes, já espelhados: ao fechar, as cópias caem
exatamente umas sobre as outras; ao abrir, aparecem espelhadas.
Peças locais: folha() (folha de até duas dobras, com furos e recortes), meio_coracao(), casinha(), eixo(), eixos_reg() (as n
direções dos eixos de um regular: de 180/n em 180/n a partir de um vértice), reg_pts(), pilha() (camadas empilhadas), ps(),
fcen(), bola_txt(), num_bola().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polígonos e Círculo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POL-010_eixos_de_simetria_e_dobraduras.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("eixo", "exemplos", "atalho", "dobra", "questao", "fim"))
BR = "#FFFFFF"
PAPEL_F, PAPEL_V = "#FFFFFF", "#E4E4EE"     # frente e verso da folha
FURO = "#2A2A33"
assert 3 + 3 == 6 and 2 * 2 == 4 and 4 * 2 == 8 and 2 ** 3 == 8


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def eixo(c, t, t0, P, Q, cor=None, ext=50, larg=5, d=0.5, a=1.0):
    """eixo de simetria: tracejado na cor da matéria, passando um pouco das pontas"""
    if t < t0 or a <= 0:
        return
    ux, uy = E._uni(*P, *Q)
    A, B = (P[0] - ux * ext, P[1] - uy * ext), (Q[0] + ux * ext, Q[1] + uy * ext)
    M.line(c, *A, *B, cor or E.COR, a, larg, dash=[18, 12], progress=ease_io(prog(t, t0, d)))


def reg_pts(n, cx, cy, r, giro=0.0):
    """os vértices de E.regular (um lado deitado embaixo)"""
    ini = 90 - 180 / n + giro
    return [(cx + r * math.cos(math.radians(ini + k * 360 / n)), cy + r * math.sin(math.radians(ini + k * 360 / n))) for k in range(n)]


def eixos_reg(n, cx, cy, r, giro=0.0, k_ext=1.12):
    """as n direções dos eixos do regular: de 180/n em 180/n a partir de um vértice; devolve [(P, Q, de_vertice)]"""
    ini = 90 - 180 / n + giro
    out = []
    for k in range(n):
        g = math.radians(ini + k * 180 / n)
        dx, dy = math.cos(g) * r * k_ext, math.sin(g) * r * k_ext
        out.append(((cx - dx, cy - dy), (cx + dx, cy + dy), k % 2 == 0 or n % 2 == 1))
    return out


def contorno(c, pts, cor, a=1.0, larg=6, fill=None, alfa=0.0):
    if a <= 0:
        return
    path = skia.Path(); path.addPoly([tuple(p) for p in pts], True)
    if fill and alfa > 0:
        c.drawPath(path, M.paint(fill, alfa * a))
    pa = M.paint(cor, a, stroke=larg); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pa)


def folha(c, x, y, w, h, p1=0.0, p2=0.0, furos=(), recortes=(), a=1.0, vinco=0.0, dobras=2):
    """folha de papel com até duas dobras: p1 = a metade da direita sobre a esquerda (eixo em pé no meio); p2 = a metade de baixo
    sobre a de cima. furos = [(x, y, r, alfa)] e recortes = [(pontos, alfa_tracejado, alfa_cheio)], em coordenadas da folha aberta,
    na metade (ou no quarto) de cima à esquerda: cada pedaço desenha a sua cópia espelhada. vinco = alfa das linhas de dobra
    tracejadas; dobras = 1 (só a dobra em pé) ou 2"""
    if a <= 0:
        return
    X1, Y1 = x + w / 2, y + h / 2
    c1, c2 = math.cos(math.pi * p1), math.cos(math.pi * p2)
    s1 = c1 if abs(c1) > 1e-3 else 1e-3
    s2 = c2 if abs(c2) > 1e-3 else 1e-3
    pecas = sorted(((i, j) for j in (0, 1) for i in (0, 1)), key=lambda q: (q[1] == 1 and p2 > 0.5) * 2 + (q[0] == 1 and p1 > 0.5))
    if a < 1:
        c.saveLayerAlpha(None, int(255 * a))
    for i, j in pecas:
        rx, ry = x + i * w / 2, y + j * h / 2
        c.save()
        if j == 1:
            c.translate(0, Y1); c.scale(1, s2); c.translate(0, -Y1)
        if i == 1:
            c.translate(X1, 0); c.scale(s1, 1); c.translate(-X1, 0)
        verso = (i == 1 and c1 < 0) != (j == 1 and c2 < 0)
        ret = skia.Rect.MakeXYWH(rx, ry, w / 2, h / 2)
        sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10))
        sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.drawRect(ret.makeOffset(4, 8), sombra)
        c.drawRect(ret, M.paint(PAPEL_V if verso else PAPEL_F))
        c.save()
        c.clipRect(ret)
        mx = (lambda px: px) if i == 0 else (lambda px: 2 * X1 - px)
        my = (lambda py: py) if (j == 0 or dobras == 1) else (lambda py: 2 * Y1 - py)
        for pts, ad, af in recortes:
            q = [(mx(px), my(py)) for px, py in pts]
            path = skia.Path(); path.addPoly(q, True)
            if af > 0:
                c.drawPath(path, M.paint(E.COR, af))
            if ad > 0:
                pd = M.paint(TINTA, ad, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
                c.drawPath(path, pd)
        for fx, fy, fr, fa in furos:
            if fa > 0:
                c.drawCircle(mx(fx), my(fy), fr, M.paint(FURO, fa))
        c.restore()
        # bordas de fora (as do meio são dobras)
        bx = [(rx, ry, rx + w / 2, ry) if j == 0 else None, (rx, ry + h / 2, rx + w / 2, ry + h / 2) if j == 1 else None,
              (rx, ry, rx, ry + h / 2) if i == 0 else None, (rx + w / 2, ry, rx + w / 2, ry + h / 2) if i == 1 else None]
        for seg in bx:
            if seg:
                M.line(c, *seg, TINTA2, 1.0, 3)
        if vinco > 0:
            if i == 0:
                M.line(c, rx + w / 2, ry, rx + w / 2, ry + h / 2, E.COR, vinco, 4, dash=[14, 10])
            if j == 0 and dobras == 2:
                M.line(c, rx, ry + h / 2, rx + w / 2, ry + h / 2, E.COR, vinco, 4, dash=[14, 10])
        c.restore()
    if a < 1:
        c.restore()


def meio_coracao(X1, cy, s, n=40):
    """a metade esquerda de um coração com o meio no eixo x = X1 (fecha pelo próprio eixo)"""
    pts = []
    for k in range(n + 1):
        u = math.pi * k / n
        hx = 16 * math.sin(u) ** 3
        hy = 13 * math.cos(u) - 5 * math.cos(2 * u) - 2 * math.cos(3 * u) - math.cos(4 * u)
        pts.append((X1 - s * hx, cy - s * hy))
    return pts


def casinha(cx, base, larg, alt, telhado):
    """a casinha simétrica: pontos do contorno, janelas e porta (todas espelhadas no eixo x = cx)"""
    L, R = cx - larg / 2, cx + larg / 2
    pts = [(cx, base - alt - telhado), (R, base - alt), (R, base), (L, base), (L, base - alt)]
    jan = [(L + 70, base - alt + 60, 90, 90), (R - 160, base - alt + 60, 90, 90)]
    porta = (cx - 45, base - 170, 90, 170)
    return pts, jan, porta


def desenha_casa(c, cx, base, larg, alt, telhado, d_contorno=1.0):
    """a casinha que se desenha em volta (d_contorno = 0..1); janelas e porta entram no fim"""
    pts, jan, porta = casinha(cx, base, larg, alt, telhado)
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(E.COR, 0.10 * d_contorno))
    E._contorno(c, pts, d_contorno, TINTA, 6)
    q = M.clamp((d_contorno - 0.6) / 0.4)
    for jx, jy, jw, jh in jan:
        c.drawRect(skia.Rect.MakeXYWH(jx, jy, jw, jh), M.paint(TINTA2, q, stroke=5))
    c.drawRect(skia.Rect.MakeXYWH(*porta), M.paint(E.COR, 0.35 * q))
    c.drawRect(skia.Rect.MakeXYWH(*porta), M.paint(TINTA, q, stroke=5))
    return pts


def pilha(c, cx, cy, w, h, n, a=1.0, furo=False):
    """n camadas de papel empilhadas, de leve deslocadas"""
    if a <= 0:
        return
    for k in range(n):
        off = (n - 1 - k) * 9
        ret = skia.Rect.MakeXYWH(cx - w / 2 + off, cy - h / 2 + off, w, h)
        c.drawRect(ret, M.paint(PAPEL_F if k % 2 == 0 else PAPEL_V, a))
        c.drawRect(ret, M.paint(TINTA2, a, stroke=3))
    if furo:
        c.drawCircle(cx, cy, 18, M.paint(FURO, a))


# ---------------- gancho ----------------
GX, GY, GW, GH = 220, 250, 720, 560


def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"], C["s01.e"]
    X = 1440

    def um():
        p1 = ease_io(prog(t, ka + 0.3, 1.0)) - ease_io(prog(t, kd + 0.6, 0.8))
        p2 = ease_io(prog(t, kb + 0.2, 1.0)) - ease_io(prog(t, kd, 0.6))
        fa = ep(t, kc + 0.3, 0.3)
        k = ease_back(prog(t, kc, 0.4))
        if 0 < k and t < kc + 0.6:  # o furador desce
            c.drawCircle(GX + GW / 4, GY + GH / 4, 40 * (1.3 - 0.3 * k), M.paint(E.COR, 0.35 * (1 - ep(t, kc + 0.4, 0.2))))
        E.foco(c, t, C["s01"], 0.5, lambda a: folha(c, GX, GY, GW, GH, p1, p2, [(GX + GW / 4, GY + GH / 4, 30, fa)], a=a))
        E.frase(c, t, ka, ps("dobre ao", "i", 72) + [("meio", "g", 76, COR)], X, 260, "center", 0.12)
        E.frase(c, t, kb, ps("e de novo", "i", 72) + [("ao meio", "g", 76, COR)], X, 380, "center", 0.12)
        E.frase(c, t, kc, [("1 furo", "g", 90)], X, 530, "center")
        E.frase(c, t, kd + 0.4, ps("ao abrir:", "i", 70), X, 680, "center", 0.12)
        E.frase(c, t, kd + 1.0, [("4 furos", "g", 110, COR)], X, 810, "center")
        E.frase(c, t, ke, ps("sem desenhar tudo", "i", 58, TINTA2), X, 940, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1530, 560, 240 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.4), [("eixos", "g", 100, COR)] + ps("de", "i", 90) + [("simetria", "g", 100, COR)], XE, 450, passo=0.14)
        E.frase(c, t, tb, ps("e o desenho da", "i", 80), XE, 610, passo=0.14)
        E.frase(c, t, tb + 0.7, [("dobradura", "g", 100)], XE, 740, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1530, 535, 78, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1530, 620, 78, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, y, w = 900, 220, 900
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 560, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("polígono regular:", "i", 60)], x + 44, y + 90)
    E.frase(c, t, C["s03.b"] + 0.6, [("lados iguais", "g", 66, COR)], x + 44, y + 180)
    E.frase(c, t, C["s03.b"] + 1.2, [("ângulos iguais", "g", 66, COR)], x + 44, y + 270)
    t2 = lerp(C["s03.b"], C["s03.end"], 0.55)
    E.regular(c, t, t2, 4, x + 250, y + 430, 105, iguais=[1] * 4, retos=(0, 1, 2, 3), preenche=0.08, d=0.6, r_ang=26)
    E.regular(c, t, t2 + 0.4, 6, x + 620, y + 430, 115, iguais=[1] * 6, preenche=0.08, d=0.6)
    E.cursor(c, x + w - 30, y + 530, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 930, "left", 0.12)


# ---------------- o eixo ----------------
HX, HB, HL, HA, HT = 560, 860, 520, 340, 220     # casinha: eixo em x = 560


def b_eixo(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    X = 1440
    topo = HB - HA - HT
    # a metade da direita gira sobre o eixo e cai em cima da esquerda; depois volta
    p = ease_io(prog(t, b4 + 0.2, 1.2)) - ease_io(prog(t, c4 + 1.4, 0.9))
    cs = math.cos(math.pi * p)
    if t >= C["s04"]:
        q = ease_io(prog(t, C["s04"], 1.0))
        c.save(); c.clipRect(skia.Rect.MakeLTRB(0, 0, HX, H))
        desenha_casa(c, HX, HB, HL, HA, HT, q)
        c.restore()
        c.save()
        c.translate(HX, 0); c.scale(cs if abs(cs) > 1e-3 else 1e-3, 1); c.translate(-HX, 0)
        c.clipRect(skia.Rect.MakeLTRB(HX, 0, W, H))
        if cs < 0:
            c.drawPath((lambda pa: (pa.addPoly(casinha(HX, HB, HL, HA, HT)[0], True), pa)[1])(skia.Path()), M.paint(E.COR, 0.18))
        desenha_casa(c, HX, HB, HL, HA, HT, q)
        c.restore()
    if c4 <= t < c4 + 1.4:
        k = 1 + 0.06 * math.sin(math.pi * M.clamp(prog(t, c4, 0.8)))
        E.foco(c, t, c4 + 0.2, 0.4, lambda a: E.selo(c, HX - 140, HB - 120, 56 * k, True, a))
    # o espelho e os pares
    if t >= a5:
        q = ep(t, a5, 0.5)
        ret = skia.Rect.MakeXYWH(HX - 9, topo - 70, 18, HB - topo + 140)
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeLinear([skia.Point(HX - 9, 0), skia.Point(HX + 9, 0)],
                                                    [M.hexc("#9FD3F5", 0.9 * q), M.hexc("#E8F6FF", 0.9 * q), M.hexc("#9FD3F5", 0.9 * q)]))
        c.drawRect(ret, g)
    eixo(c, t, a4, (HX, topo), (HX, HB), ext=70)
    L, R = HX - HL / 2, HX + HL / 2
    pares = (((L, HB - HA), (R, HB - HA), 1), ((L, HB), (R, HB), 2))
    for k, (P, Q, n) in enumerate(pares):
        tk = b5 + 0.4 * k
        for V in (P, Q):
            kk = ease_back(prog(t, tk, 0.35))
            if kk > 0:
                c.drawCircle(*V, 15 * kk, M.paint(E.COR if n == 1 else TINTA2))
        if t >= c5:
            Mm = (HX, P[1])
            M.line(c, *P, *Q, E.COR if n == 1 else TINTA2, ep(t, c5 + 0.2 * k, 0.4), 6)
            qq = ep(t, c5 + 0.4 + 0.2 * k, 0.4)
            E.marcas_iguais(c, P, Mm, n, TINTA, qq); E.marcas_iguais(c, Mm, Q, n, TINTA, qq)
            E.angulo(c, t, c5 + 0.6 + 0.2 * k, Mm, (HX, Mm[1] - 60), Q, r=40, reto=True)

    def txt4():
        E.frase(c, t, a4, [("eixo de simetria:", "g", 66, COR)], X, 260, "center")
        E.frase(c, t, a4 + 0.8, ps("duas metades espelhadas", "i", 58), X, 350, "center", 0.12)
        E.frase(c, t, b4, ps("o teste:", "i", 64) + [("dobrar", "g", 72, COR)], X, 520, "center", 0.12)
        E.frase(c, t, c4, ps("cai em cima:", "i", 64) + [("é eixo", "g", 72, CERTO)], X, 680, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, txt4)
    if t >= C["s05"]:
        E.frase(c, t, a5, ps("um", "i", 66) + [("espelho", "g", 74, COR)] + ps("na linha", "i", 66), X, 260, "center", 0.12)
        E.frase(c, t, b5, ps("cada ponto tem", "i", 62) + [("um par", "g", 68, COR)], X, 420, "center", 0.12)
        E.frase(c, t, b5 + 0.9, ps("na mesma distância", "i", 58, TINTA2), X, 510, "center", 0.12)
        E.frase(c, t, c5, ps("e cruza o eixo em", "i", 60), X, 670, "center", 0.12)
        E.frase(c, t, c5 + 0.6, [("ângulo reto", "g", 76)], X, 770, "center")


# ---------------- exemplos ----------------
def letra_a(c, cx, base, size, a=1.0):
    w_ = E.larg("A", "g", size)
    E.escreve(c, "A", cx - w_ / 2, base, size, "g", TINTA, a)


def b_exemplos(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    PX, CY = (330, 960, 1590), 470

    def tres():
        # letra A
        E.foco(c, t, a6, 0.5, lambda a: letra_a(c, PX[0], CY + 150, 440, a))
        eixo(c, t, a6 + 0.6, (PX[0], CY - 190), (PX[0], CY + 160), ext=30)
        # retângulo: em pé e deitado
        rw, rh = 440, 270
        E.retangulo(c, t, b6, PX[1] - rw / 2, CY - rh / 2, rw, rh, preenche=0.08, d=0.7)
        eixo(c, t, b6 + 0.6, (PX[1], CY - rh / 2), (PX[1], CY + rh / 2))
        eixo(c, t, b6 + 1.0, (PX[1] - rw / 2, CY), (PX[1] + rw / 2, CY))
        # quadrado: as duas e as diagonais
        l = 320
        E.quadrado(c, t, c6, PX[2] - l / 2, CY - l / 2, l, preenche=0.08, d=0.7, r_ang=30)
        eixo(c, t, c6 + 0.6, (PX[2], CY - l / 2), (PX[2], CY + l / 2))
        eixo(c, t, c6 + 0.8, (PX[2] - l / 2, CY), (PX[2] + l / 2, CY))
        eixo(c, t, d6, (PX[2] - l / 2, CY - l / 2), (PX[2] + l / 2, CY + l / 2), TINTA2)
        eixo(c, t, d6 + 0.3, (PX[2] - l / 2, CY + l / 2), (PX[2] + l / 2, CY - l / 2), TINTA2)
        for cx, ti, n, nome in ((PX[0], a6, "1 eixo", "letra A"), (PX[1], b6, "2 eixos", "retângulo"), (PX[2], c6, "4 eixos", "quadrado")):
            E.frase(c, t, ti + 0.4, [(nome, "i", 56, TINTA2)], cx, 790, "center")
            E.frase(c, t, ti + 0.8 if n != "4 eixos" else d6 + 0.4, [(n, "g", 80, COR)], cx, 900, "center")
    E.saida(c, t, C["s07"] - 0.1, tres)
    if C["s07"] - 0.1 <= t < C["s08"]:
        def dois():
            T3 = reg_pts(3, 560, 500, 300)
            E.regular(c, t, a7, 3, 560, 500, 300, iguais=[1, 1, 1], preenche=0.08, d=0.7)
            for k, (P, Q, _) in enumerate(eixos_reg(3, 560, 500, 300, k_ext=0.92)):
                eixo(c, t, a7 + 0.8 + 0.3 * k, P, Q)
            E.circulo(c, t, b7, 1400, 520, 270, o=None, d=0.8)
            if t >= c7:
                for k in range(8):
                    g = math.radians(k * 22.5 + 12 * (t - c7))
                    dx, dy = 310 * math.cos(g), 310 * math.sin(g)
                    M.line(c, 1400 - dx, 520 - dy, 1400 + dx, 520 + dy, E.COR, ep(t, c7 + 0.12 * k, 0.3), 4, dash=[18, 12])
            c.drawCircle(1400, 520, 9, M.paint(TINTA, ep(t, b7 + 0.4, 0.3)))
            E.frase(c, t, a7 + 0.4, [("equilátero", "i", 56, TINTA2)], 560, 880, "center")
            E.frase(c, t, a7 + 1.4, [("3 eixos", "g", 80, COR)], 560, 990, "center")
            E.frase(c, t, b7 + 0.4, [("círculo", "i", 56, TINTA2)], 1400, 880, "center")
            E.frase(c, t, c7, [("infinitos", "g", 80, COR)], 1400, 990, "center")
            _ = T3
        E.saida(c, t, C["s08"] - 0.1, dois)
    if t >= C["s08"]:
        E.regular(c, t, C["s08"], 6, 600, 540, 340, iguais=[1] * 6, preenche=0.08, d=0.8)
        X = 1440
        E.frase(c, t, a8, ps("hexágono", "i", 70) + [("regular", "g", 74, COR)], X, 230, "center", 0.12)
        k1 = k2 = 0
        for P, Q, vert in eixos_reg(6, 600, 540, 340, k_ext=1.08):
            if vert:
                eixo(c, t, b8 + 0.3 * k1, P, Q, E.COR, larg=6); k1 += 1
            else:
                eixo(c, t, c8 + 0.3 * k2, P, Q, TINTA2, larg=6); k2 += 1
        E.frase(c, t, b8, [("3", "g", 80, COR)] + ps("de vértice a vértice", "i", 56), X, 400, "center", 0.12)
        E.frase(c, t, c8, [("3", "g", 80, TINTA2)] + ps("de meio a meio de lado", "i", 56), X, 560, "center", 0.12)
        fcen(c, t, d8, "3 + 3 =", X - 80, 790, 96)
        bola_txt(c, t, d8 + 0.4, "6", X + 170, 760, 90, 100)
        E.frase(c, t, d8 + 0.9, [("eixos", "i", 60)], X + 170, 900, "center")


# ---------------- erro: a diagonal do retângulo ----------------
RX0, RY0, RW, RH = 160, 330, 820, 420


def b_erro(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    X = 1480
    TL, TR, BR_, BL = (RX0, RY0), (RX0 + RW, RY0), (RX0 + RW, RY0 + RH), (RX0, RY0 + RH)
    E.retangulo(c, t, C["s09"], RX0, RY0, RW, RH, preenche=0.0, d=0.6)
    eixo(c, t, a9, TL, BR_, ERRADO, ext=40)
    contorno(c, [TL, BL, BR_], TINTA, ep(t, b9, 0.4), 0.1, E.COR, 0.22)
    # o triângulo de cima vira sobre a diagonal
    p = ease_io(prog(t, c9, 1.3))
    if t >= b9:
        phi = math.degrees(math.atan2(BR_[1] - TL[1], BR_[0] - TL[0]))
        cs = math.cos(math.pi * p)
        c.save()
        c.translate(*TL); c.rotate(phi); c.scale(1, cs if abs(cs) > 1e-3 else 1e-3); c.rotate(-phi); c.translate(-TL[0], -TL[1])
        contorno(c, [TL, TR, BR_], TINTA, ep(t, b9 + 0.3, 0.4), 4, TINTA2 if cs > 0 else ERRADO, 0.2 if cs > 0 else 0.28)
        c.restore()
    if t >= c9 + 1.3:  # os pedaços que sobram para fora
        k = 1 + 0.15 * math.sin(math.pi * M.clamp(prog(t, c9 + 1.3, 0.8)))
        phi = math.atan2(RH, RW)
        # o reflexo de TR sobre a diagonal
        ux, uy = math.cos(phi), math.sin(phi)
        vx, vy = TR[0] - TL[0], TR[1] - TL[1]
        dp = vx * ux + vy * uy
        Rf = (TL[0] + 2 * dp * ux - vx, TL[1] + 2 * dp * uy - vy)
        c.drawCircle(*Rf, 20 * k, M.paint(ERRADO, ep(t, c9 + 1.3, 0.3)))
    E.frase(c, t, a9, ps("a diagonal", "i", 64) + [("é eixo?", "g", 72, ERRADO)], X, 250, "center", 0.12)
    E.frase(c, t, b9, ps("triângulos iguais:", "i", 60) + [("sim", "g", 68, CERTO)], X, 400, "center", 0.12)
    E.frase(c, t, c9, ps("dobre:", "i", 64) + [("sobra!", "g", 76, ERRADO)], X, 560, "center", 0.12)
    E.foco(c, t, c9 + 1.4, 0.5, lambda a: E.selo(c, X, 680, 50 * ease_back(prog(t, c9 + 1.4, 0.5)), False, a))
    E.frase(c, t, d9, ps("não basta ser igual:", "i", 56), X, 840, "center", 0.12)
    E.frase(c, t, d9 + 0.8, [("tem que encaixar", "g", 72, COR)], X, 940, "center")


# ---------------- atalho (palco escuro) ----------------
def reg_escuro(c, t, t0, n, cx, cy, r, a_ext=CLARO, a_mid=BR, ta=None, larg=6):
    pts = reg_pts(n, cx, cy, r)
    if t >= t0:
        E._contorno(c, pts, ease_io(prog(t, t0, 0.7)), BR, larg)
    ta = ta if ta is not None else t0 + 0.7
    for k, (P, Q, vert) in enumerate(eixos_reg(n, cx, cy, r, k_ext=1.1)):
        eixo(c, t, ta + 0.12 * k, P, Q, a_ext if vert else a_mid, ext=10, larg=4)


def b_atalho(c, t, C, b):
    palco(c, t)
    a10, b10, c10, d10, e10 = (C["s10." + k] for k in "abcde")
    a11, b11, c11, d11, e11, f11 = (C["s11." + k] for k in "abcdef")

    def linha():
        E.frase(c, t, a10, [("regular:", "g", 80, CLARO)] + ps("eixos =", "i", 76, BR) + [("lados", "g", 80, BR)], W / 2, 200, "center", 0.12)
        for cx, n, ti in ((300, 3, b10), (740, 4, c10), (1180, 6, d10), (1620, 8, e10)):
            reg_escuro(c, t, ti, n, cx, 560, 170, CLARO, CLARO)
            E.foco(c, t, ti + 0.6, 0.4, lambda a, cx=cx, n=n: centro(c, str(n), cx, 880, 110, "g", BR, a))
    E.saida(c, t, C["s11"] - 0.1, linha)
    if t < C["s11"]:
        return
    reg_escuro(c, t, C["s11"], 6, 470, 580, 290, ta=99999)
    k1 = k2 = 0
    for P, Q, vert in eixos_reg(6, 470, 580, 290, k_ext=1.1):
        if vert:
            eixo(c, t, b11 + 0.25 * k1, P, Q, CLARO, ext=10, larg=5); k1 += 1
        else:
            eixo(c, t, c11 + 0.25 * k2, P, Q, BR, ext=10, larg=5); k2 += 1
    X = 1350
    E.frase(c, t, a11, ps("vértices e meios de lado", "i", 56, CLARO), X, 200, "center", 0.1)
    E.frase(c, t, a11 + 1.0, [("no eixo", "g", 66, BR)], X, 290, "center")
    E.frase(c, t, b11, [("6 vértices:", "g", 56, CLARO)] + ps("3 eixos", "i", 56, BR), X - 220, 420, "center", 0.12)
    E.frase(c, t, c11, [("6 lados:", "g", 56, BR)] + ps("+ 3", "i", 56, BR), X + 230, 420, "center", 0.12)
    E.foco(c, t, d11, 0.5, lambda a: E.pilula(c, "não vale se não for regular", X, 560, 54, "g", fundo=ERRADO, a=a))
    # retângulo: só 2
    rx, ry, rw, rh = 1010, 680, 330, 200
    if t >= e11:
        q = ep(t, e11, 0.4)
        contorno(c, [(rx, ry), (rx + rw, ry), (rx + rw, ry + rh), (rx, ry + rh)], BR, q, 5)
        eixo(c, t, e11 + 0.3, (rx + rw / 2, ry), (rx + rw / 2, ry + rh), CLARO, ext=24, larg=4)
        eixo(c, t, e11 + 0.5, (rx, ry + rh / 2), (rx + rw, ry + rh / 2), CLARO, ext=24, larg=4)
        E.foco(c, t, e11 + 0.4, 0.4, lambda a: centro(c, "só 2", rx + rw / 2, ry + rh + 90, 64, "g", BR, a))
    # paralelogramo: nenhum
    if t >= f11:
        px, py, pw, ph, dsl = 1450, 680, 300, 200, 110
        q = ep(t, f11, 0.4)
        contorno(c, [(px, py + ph), (px + pw, py + ph), (px + pw + dsl, py), (px + dsl, py)], BR, q, 5)
        E.foco(c, t, f11 + 0.3, 0.4, lambda a: centro(c, "nenhum", px + (pw + dsl) / 2, py + ph + 90, 64, "g", "#FF8A8E", a))


# ---------------- dobradura ----------------
FX, FY, FW, FH = 200, 260, 760, 580
TRI = [(FX + 90, FY + 110), (FX + 250, FY + 80), (FX + 190, FY + 230)]


def b_dobra(c, t, C, b):
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    X = 1450
    X1 = FX + FW / 2
    if t < C["s13"] - 0.1:
        def um():
            p1 = ease_io(prog(t, b12, 0.9)) - ease_io(prog(t, c12, 0.9))
            ad = ep(t, b12 + 1.0, 0.3) * (1 - ep(t, b12 + 1.8, 0.3))
            af = ep(t, b12 + 1.8, 0.3)
            folha(c, FX, FY, FW, FH, p1, 0, recortes=[(TRI, ad, af)], vinco=ep(t, a12, 0.4), a=ep(t, C["s12"], 0.4), dobras=1)
            E.frase(c, t, a12, ps("a dobra é um", "i", 66) + [("eixo", "g", 74, COR)], X, 270, "center", 0.12)
            E.frase(c, t, b12, ps("corta", "i", 66) + [("as camadas", "g", 70, COR)], X, 430, "center", 0.12)
            E.frase(c, t, b12 + 0.6, [("juntas", "g", 70, COR)], X, 520, "center")
            E.frase(c, t, c12, ps("ao abrir:", "i", 64), X, 680, "center", 0.12)
            E.frase(c, t, c12 + 0.6, [("espelhado", "g", 80, COR)], X, 790, "center")
        E.saida(c, t, C["s13"] - 0.1, um)
        return
    if t < C["s14"] - 0.1:
        def dois():
            p1 = ease_io(prog(t, b13, 0.8)) - ease_io(prog(t, d13 + 0.85, 0.5))
            p2 = ease_io(prog(t, c13, 0.8)) - ease_io(prog(t, d13 + 0.35, 0.5))
            fa = ep(t, d13, 0.3)
            folha(c, FX, FY, FW, FH, p1, p2, furos=[(FX + FW / 4, FY + FH / 4, 30, fa)], a=ep(t, C["s13"], 0.4))
            E.frase(c, t, a13, ps("cada dobra", "i", 66) + [("dobra", "g", 74, COR)], X, 250, "center", 0.12)
            E.frase(c, t, a13 + 0.6, ps("as camadas", "i", 66), X, 340, "center", 0.12)
            for k, (ti, n, s) in enumerate(((C["s13"], 1, "1"), (b13, 2, "2"), (c13, 4, "4"))):
                cx = X - 300 + k * 300
                E.foco(c, t, ti + 0.3, 0.4, lambda a, cx=cx, n=n: pilha(c, cx, 520, 150, 100, n, a))
                E.foco(c, t, ti + 0.5, 0.4, lambda a, cx=cx, s=s: centro(c, s, cx, 680, 80, "g", COR, a))
            E.frase(c, t, b13, ps("camadas", "i", 54, TINTA2), X, 760, "center")
            E.frase(c, t, d13, [("1 furo", "g", 70), ("→", "g", 70, TINTA2), ("4 furos", "g", 80, COR)], X, 920, "center", 0.2)
        E.saida(c, t, C["s14"] - 0.1, dois)
        return
    p1 = ease_io(prog(t, a14, 0.8)) - ease_io(prog(t, d14 + 0.3, 0.6))
    cor = meio_coracao(X1, FY + FH / 2 - 40, 9.5)
    ad = ep(t, c14, 0.3) * (1 - ep(t, d14, 0.25))
    af = ep(t, d14, 0.25)
    folha(c, FX, FY, FW, FH, p1, 0, recortes=[(cor, ad, af)], vinco=ep(t, C["s14"], 0.4), a=ep(t, C["s14"] - 0.15, 0.3), dobras=1)
    if c14 <= t < d14 + 0.5:  # o meio do coração fica na dobra
        M.line(c, X1, FY - 20, X1, FY + FH + 20, E.COR, ep(t, c14, 0.3) * (1 - ep(t, d14, 0.3)), 8)
    E.frase(c, t, a14, ps("corte", "i", 66) + [("na dobra", "g", 74, COR)], X, 270, "center", 0.12)
    E.frase(c, t, b14, ps("as cópias", "i", 62) + [("se juntam", "g", 70, COR)], X, 420, "center", 0.12)
    E.frase(c, t, b14 + 0.8, ps("a dobra vira o eixo", "i", 56, TINTA2), X, 510, "center", 0.12)
    E.frase(c, t, c14, ps("desenhe", "i", 66) + [("metade", "g", 74)], X, 680, "center", 0.12)
    E.frase(c, t, d14, ps("corte e", "i", 66) + [("abra", "g", 80, COR)], X, 830, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 150, passo=0.12)
    E.regular(c, t, a15, 5, 390, 470, 220, iguais=[1] * 5, preenche=0.08, d=0.7)
    E.foco(c, t, a15 + 0.8, 0.4, lambda a: centro(c, "eixos?", 390, 790, 70, "g", COR, a))
    E.foco(c, t, b15, 0.5, lambda a: pilha(c, 900, 470, 220, 160, 8 if t >= b15 + 0.6 else 4 if t >= b15 + 0.3 else 2, a))
    E.foco(c, t, b15 + 0.4, 0.4, lambda a: centro(c, "3 dobras", 900, 670, 60, "g", TINTA, a))
    if t >= c15:
        k = ease_back(prog(t, c15, 0.4))
        c.drawCircle(900, 470, 22 * k, M.paint(FURO))
    E.foco(c, t, d15, 0.4, lambda a: centro(c, "furos?", 900, 790, 70, "g", COR, a))
    E.frase(c, t, a15, ps("pentágono regular:", "i", 60) + [("quantos eixos?", "g", 64, COR)], W / 2, 920, "center", 0.12)
    E.frase(c, t, b15, ps("3 dobras e 1 furo:", "i", 60) + [("quantos furos?", "g", 64, COR)], W / 2, 1020, "center", 0.12)
    E.relogio(c, t, C["s16.a"], 1500, 400, 180)


def b_resposta(c, t, C, b):
    a17, b17 = C["s17.a"], C["s17.b"]
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    X = 1450
    if t < C["s18"] - 0.1:
        def um():
            P5 = reg_pts(5, 560, 560, 330)
            E.regular(c, t, C["s17"], 5, 560, 560, 330, iguais=[1] * 5, preenche=0.08, d=0.7)
            for k, (P, Q, _) in enumerate(eixos_reg(5, 560, 560, 330, k_ext=1.08)):
                eixo(c, t, a17 + 0.25 * k, P, Q, larg=5)
            if t >= b17:  # um eixo: do vértice de cima até o meio do lado de baixo
                V = min(P5, key=lambda p: p[1])
                Mb = ((P5[0][0] + P5[1][0]) / 2, (P5[0][1] + P5[1][1]) / 2)
                M.line(c, *V, *Mb, E.COR, ep(t, b17, 0.4), 10)
                for Q, tt in ((V, b17), (Mb, b17 + 0.4)):
                    kk = ease_back(prog(t, tt, 0.35))
                    if kk > 0:
                        c.drawCircle(*Q, 16 * kk, M.paint(E.COR))
                E.angulo(c, t, b17 + 0.6, Mb, V, P5[1], r=36, reto=True)
            E.frase(c, t, C["s17"] + 0.2, ps("5 lados", "i", 72), X, 260, "center")
            bola_txt(c, t, a17, "5", X - 120, 440, 90, 100)
            E.frase(c, t, a17 + 0.5, [("eixos", "g", 76, COR)], X + 90, 465, "left")
            E.frase(c, t, b17, ps("5 é ímpar:", "i", 60), X, 640, "center", 0.12)
            E.frase(c, t, b17 + 0.6, [("vértice → meio do lado", "g", 58, COR)], X, 740, "center")
        E.saida(c, t, C["s18"] - 0.1, um)
        return
    # as camadas dobram
    def pilhas():
        for k, (ti, n) in enumerate(((a18, 2), (b18, 4), (c18, 8))):
            cx = 250 + k * 330
            E.foco(c, t, ti, 0.4, lambda a, cx=cx, n=n: pilha(c, cx, 450, 200, 140, n, a))
            E.foco(c, t, ti + 0.3, 0.4, lambda a, cx=cx, n=n: centro(c, str(n), cx, 650, 90, "g", COR, a))
        E.frase(c, t, a18, ps("camadas", "i", 54, TINTA2), 580, 760, "center")
    E.saida(c, t, d18, pilhas)
    if t >= d18:
        ox, oy, ow, oh = 120, 280, 900, 520
        q = ep(t, d18, 0.5)
        c.drawRect(skia.Rect.MakeXYWH(ox, oy, ow, oh), M.paint(PAPEL_F, q))
        c.drawRect(skia.Rect.MakeXYWH(ox, oy, ow, oh), M.paint(TINTA2, q, stroke=3))
        for k in (1, 2, 3):
            M.line(c, ox + ow * k / 4, oy, ox + ow * k / 4, oy + oh, E.COR, q * 0.8, 4, dash=[14, 10])
        M.line(c, ox, oy + oh / 2, ox + ow, oy + oh / 2, E.COR, q * 0.8, 4, dash=[14, 10])
        u, v = 0.35, 0.4
        for i in range(4):
            for j in range(2):
                fx = ox + ow / 4 * (i + (u if i % 2 == 0 else 1 - u))
                fy = oy + oh / 2 * (j + (v if j % 2 == 0 else 1 - v))
                kk = ease_back(prog(t, d18 + 0.2 + 0.04 * (i + 4 * j), 0.3))
                if kk > 0:
                    c.drawCircle(fx, fy, 26 * kk, M.paint(FURO))
    fcen(c, t, a18, "1ª dobra: 2", X, 260, 70)
    fcen(c, t, b18, "2 × 2 = 4", X, 400, 80)
    fcen(c, t, c18, "4 × 2 = 8", X, 540, 80)
    bola_txt(c, t, d18 + 0.3, "8", X - 100, 740, 90, 100, CERTO)
    E.frase(c, t, d18 + 0.5, [("furos", "g", 76, CERTO)], X + 20, 765, "left")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", "eixo:", "a dobra encaixa as metades"), ("s19.b", "regular:", "eixos = lados"),
                 ("s19.c", "dobra do papel:", "um espelho"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 5, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 66, COR), (l2, "i", 68)], 350, y, "left", 0.2)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 80), XE, 230)
    E.frase(c, t, C["s20.a"], [("Espelhar, girar", "g", 100, COR)], XE, 360)
    E.frase(c, t, C["s20.a"] + 0.4, [("e deslizar", "g", 100, COR)], XE, 470)
    E.frase(c, t, C["s20.a"] + 0.9, ps("figuras na malha", "i", 70), XE, 570, passo=0.12)
    P = E.plano(c, t, C["s20.b"] - 0.3, 1010, 560, 560, 340, -4, 4, 0, 4, grade=True, size=34)
    E.ponto(c, t, C["s20.b"] + 0.3, P, 2, 3, "(2, 3)", lado=(1, -1), size=44)
    E.ponto(c, t, C["s20.b"] + 1.0, P, -2, 3, "(?, ?)", cor=TINTA2, lado=(-1, -1), size=44)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1580, p), lerp(560, 325, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2 - 300, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, eixo=b_eixo, exemplos=b_exemplos, erro=b_erro, atalho=b_atalho,
              dobra=b_dobra, questao=b_questao, resposta=b_resposta, fim=b_fim)
