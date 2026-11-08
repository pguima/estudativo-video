"""Visual — Estudativo · MAT-EST-019: gráficos que enganam (eixo cortado, escala irregular, figura fora de proporção).
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá) e dos gráficos de MAT-EST-003: cada categoria com a
sua cor de E._paleta; linha no tempo = E.serie; conta da vez à direita; resposta na esfera; atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- COLUNAS COM EIXO QUE PODE SER CORTADO (colunas_eixo()): o eixo do lado começa em vmin; o começo do eixo pode ser
  circulado (circula()) e o corte ganha o zigue-zague de eixo quebrado. O pedaço desenhado de cada coluna é medido com
  uma chave ao lado (pedaco()).
- GRÁFICO HONESTO x ENGANOSO lado a lado: o enganoso à esquerda, o honesto (eixo no zero) à direita.
- PICTOGRAMA (garrafa(), caixote()): a figura que dobra altura e largura; a área se mostra com a figura pequena
  repetida 2 x 2 dentro da grande (grade_area()).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-019_graficos_que_enganam.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("eixo", "escala", "figura", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(2)      # marca A, marca B
assert 50 - 45 == 5 and 55 - 45 == 10 and 55 - 50 == 5 and 5 / 50 == 0.1
assert (210 - 120) / 9 == 10 and 110 - 100 == 10 and 120 - 110 == 10
assert 2 * 2 == 4 and 6000 / 3000 == 2 and 4000 / 2000 == 2
assert 400 - 390 == 10 and 420 - 390 == 30 and 30 / 10 == 3 and 420 - 400 == 20 and 20 / 400 == 0.05


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


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados que entra coluna a coluna (de MAT-EST-001)"""
    h_lin = h_lin or size * 1.55
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, TINTA, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: E.formula(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a, "center"))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc: centro(c, s, cx, yy, size, "g", cc[0] if cc else TINTA, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, TINTA, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 and not s[0].isdigit() else "g", cc[0] if cc else TINTA, a))
    return bases


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


def fichas(c, t, t0, itens, x, y, w, size=44, gap=22, passo=0.06):
    """lista de dados em grade de fichas, da esquerda para a direita. itens = [texto]"""
    cx, cy = x, y
    h = size * 1.55
    for i, s in enumerate(itens):
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px = cx + wi / 2
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, cy=cy: ficha(c, s, px, cy, size, a), sobe=8)
        cx += wi + gap




def colunas_eixo(c, t, t0, dados, x, y, w, h, vmin, vmax, marcas, tv=None, quebra=None, size=46, cores=None, fmt=str, rot_t=None):
    """colunas com o eixo do lado começando em vmin (cortado se vmin > 0). dados = [(rótulo, valor)].
    tv = instante dos valores no topo (None: sem valores); quebra = instante do zigue-zague do corte. Devolve (vy, centros)"""
    cores = cores or CATS
    vy = lambda v: y + h - (v - vmin) / (vmax - vmin) * h
    p = ep(t, t0, 0.5)
    if p <= 0:
        return vy, []
    for v in marcas:
        if v != vmin:
            M.line(c, x, vy(v), x + w, vy(v), FIO, p, 2)
    M.line(c, x, y + h, x, y - 20, TINTA, 1, 4, progress=p)
    M.line(c, x - 10, y + h, x + w, y + h, TINTA, 1, 5, progress=p)
    for i, v in enumerate(marcas):
        E.foco(c, t, t0 + 0.15 + 0.04 * i, 0.4, lambda a, v=v: E.escreve(c, fmt(v), x - 20 - E.larg(fmt(v), "b", size), vy(v) + size * 0.36, size, "b", TINTA2, a), sobe=6)
    n = len(dados)
    slot = w / n
    bw = slot * 0.56
    cs = []
    for i, (rot, v) in enumerate(dados):
        cx = x + slot * (i + 0.5)
        q = ease_io(prog(t, t0 + 0.3 + 0.15 * i, 0.6))
        if q > 0:
            topo = lerp(y + h, vy(v), q)
            M.rrect(c, cx - bw / 2, topo, bw, y + h - topo, 10, cores[i], 1.0)
            c.drawRect(skia.Rect.MakeXYWH(cx - bw / 2, y + h - 12, bw, 12 * q), M.paint(cores[i]))
        E.foco(c, t, rot_t if rot_t is not None else t0 + 0.3, 0.4, lambda a, rot=rot, cx=cx: centro(c, rot, cx, y + h + 20 + size, size * 1.1, "g", TINTA, a), sobe=6)
        if tv is not None:
            E.foco(c, t, tv + 0.2 * i, 0.4, lambda a, v=v, cx=cx, i=i: centro(c, fmt(v), cx, vy(v) - 22, size * 1.15, "g", COR if i else TINTA, a), sobe=6)
        cs.append(cx)
    if quebra is not None:
        k = ep(t, quebra, 0.4)
        if k > 0:
            zy = y + h - 34
            pth = skia.Path(); pth.moveTo(x - 22, zy + 16)
            for j, dx in enumerate((-8, 8, -8, 8)):
                pth.lineTo(x + dx, zy - j * 12)
            c.drawRect(skia.Rect.MakeXYWH(x - 26, zy - 46, 52, 70), M.paint(PAPEL, k))
            M.line(c, x - 24, zy + 16, x + 24, zy + 4, ERRADO, k, 5)
            M.line(c, x - 24, zy - 6, x + 24, zy - 18, ERRADO, k, 5)
    return vy, cs


def circula(c, t, t0, cx, cy, r, cor=ERRADO):
    p = ep(t, t0, 0.5)
    if p > 0:
        E.arco(c, cx, cy, r, -90, 360 * p, cor, 6)


def pedaco(c, t, t0, x, y0, y1, rot, cor=ERRADO, size=48, lado=1):
    """chave vertical ao lado da coluna, de y0 (baixo) a y1 (cima), com o rótulo"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    ym = lerp(y0, y1, p)
    M.line(c, x, y0, x, ym, cor, 1, 5)
    M.line(c, x - 12 * lado, y0, x, y0, cor, 1, 5)
    if p > 0.95:
        M.line(c, x - 12 * lado, y1, x, y1, cor, 1, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.escreve(c, rot, x + 16, (y0 + y1) / 2 + size * 0.36, size, "g", cor, a) if lado > 0
                                          else E.escreve(c, rot, x - 16 - E.larg(rot, "g", size), (y0 + y1) / 2 + size * 0.36, size, "g", cor, a)), sobe=4)


def garrafa(c, cx, base, w, h, a=1.0, cor=None):
    """garrafa de leite: corpo arredondado e gargalo; (cx, base) = centro do fundo"""
    if a <= 0 or w <= 0 or h <= 0:
        return
    cor = cor or E.COR
    corpo_h, gw = h * 0.68, w * 0.42
    pth = skia.Path()
    pth.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - corpo_h, w, corpo_h), w * 0.18, w * 0.18))
    pth.addRect(skia.Rect.MakeXYWH(cx - gw / 2, base - h * 0.96, gw, h * 0.34))
    c.drawPath(pth, M.paint(E.mix(cor, PAPEL, 0.75), a))
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2 + 6, base - corpo_h * 0.55, w - 12, corpo_h * 0.55 - 6), M.paint(BR, a))
    c.drawPath(pth, M.paint(cor, a, stroke=max(4, w * 0.05)))
    c.drawRect(skia.Rect.MakeXYWH(cx - gw * 0.65, base - h, gw * 1.3, h * 0.07), M.paint(cor, a))


def caixote(c, cx, base, w, h, a=1.0, cor=None):
    """caixote de madeira de hortaliças"""
    if a <= 0 or w <= 0 or h <= 0:
        return
    cor = cor or E.COR
    r = skia.Rect.MakeXYWH(cx - w / 2, base - h, w, h)
    c.drawRect(r, M.paint(E.mix(cor, PAPEL, 0.75), a))
    for k in (1, 2):
        M.line(c, cx - w / 2, base - h * k / 3, cx + w / 2, base - h * k / 3, cor, a, max(3, w * 0.03))
    M.line(c, cx - w / 2, base, cx + w / 2, base - h, cor, a * 0.6, max(3, w * 0.03))
    c.drawRect(r, M.paint(cor, a, stroke=max(4, w * 0.05)))


def grade_area(c, t, t0, cx, base, w, h, cor=TINTA):
    """a figura pequena (w x h) repetida 2 x 2 dentro da grande (2w x 2h): 4 vezes a área"""
    for i in range(4):
        p = ep(t, t0 + 0.25 * i, 0.4)
        if p > 0:
            x0 = cx - w + (i % 2) * w
            y0 = base - 2 * h + (i // 2) * h
            r = skia.Rect.MakeXYWH(x0 + 4, y0 + 4, w - 8, h - 8)
            c.drawRect(r, M.paint(E.COR, 0.10 * p))
            pt = M.paint(cor, p, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
            c.drawRect(r, pt)
            centro(c, str(i + 1), x0 + w * (0.25 if i % 2 == 0 else 0.75), y0 + h * (0.75 if i < 2 else 0.5) + 22, 56, "g", COR, p)


# ---------------- gancho ----------------
GX, GY, GW, GH = 300, 300, 560, 480     # o anúncio (eixo cortado)


def anuncio(c, t, t0, tv=None, quebra=None, x=GX, y=GY, w=GW, h=GH):
    return colunas_eixo(c, t, t0, [("A", 50), ("B", 55)], x, y, w, h, 45, 55, [45, 50, 55], tv=tv, quebra=quebra)


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a1, ps("o anúncio:", "i", 56, TINTA2), GX, 200, "left")
        anuncio(c, t, a1 + 0.2, tv=c1)
        X = 1420
        E.frase(c, t, a1 + 1.2, ps("a coluna de B é", "i", 60) + [("o dobro", "g", 66, COR)], X, 330, "center", 0.1)
        E.frase(c, t, b1, ps("B vende", "i", 62) + [("2 vezes mais?", "g", 68, ERRADO)], X, 450, "center", 0.1)
        E.frase(c, t, c1, ps("leia os números:", "i", 56) + [("50 contra 55", "g", 62)], X, 600, "center", 0.1)
        bola_txt(c, t, d1, "10%", X, 800, 110, 76)
        E.frase(c, t, d1 + 0.4, ps("a diferença real", "i", 46, TINTA2), X, 970, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, [("3 truques", "g", 96, COR)] + ps("de gráfico", "i", 84), XE, 440, passo=0.12)
        E.frase(c, t, ta + 3.4, ps("e o", "i", 80) + [("crescimento real", "g", 90, COR)], XE, 590, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "ler um gráfico:", "título, eixos e unidade"), ("s03.c", "a variação percentual:", "diferença ÷ valor de antes"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 50), x + 40, y + 74, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 40, y + 180, 62, "g", COR)
    alvo = [250 + i * 290 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.6), ps("faltou?", "i", 50, COR) + ps("procure no canal", "i", 50), x, 900, "left", 0.1)


# ---------------- truque 1: eixo cortado ----------------
EX, EY, EW, EH = 260, 380, 560, 440      # o anúncio, à esquerda
HX = 1160                                # o gráfico honesto, à direita


def b_eixo(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7 = C["s07.a"], C["s07.b"]

    def graficos():
        E.frase(c, t, a4, [("1º truque:", "g", 70, COR)] + ps("o eixo que não começa no zero", "i", 64), W / 2, 170, "center", 0.1)
        vy, cs = colunas_eixo(c, t, C["s04"], [("A", 50), ("B", 55)], EX, EY, EW, EH, 45, 55, [45, 50, 55], tv=C["s04"] + 0.5, quebra=a5)
        circula(c, t, b4, EX - 50, vy(45) - 14, 48)
        bw = EW / 2 * 0.56
        pedaco(c, t, c4, cs[0] + bw / 2 + 20, vy(45), vy(50), "5", ERRADO)
        pedaco(c, t, d4, cs[1] + bw / 2 + 20, vy(45), vy(55), "10", ERRADO)
        E.foco(c, t, C["s04"], 0.4, lambda a: centro(c, "o anúncio", EX + EW / 2, EY - 60, 46, "i", TINTA2, a))
        if t >= c5 - 0.1:
            colunas_eixo(c, t, c5, [("A", 50), ("B", 55)], HX, EY, EW, EH, 0, 60, [0, 20, 40, 60], tv=c5 + 0.8)
            E.foco(c, t, c5, 0.4, lambda a: centro(c, "eixo no zero", HX + EW / 2, EY - 60, 46, "g", CERTO, a))
    fase(c, t, C["s04"], C["s07"] - 0.1, graficos)

    def contas4():
        X = 1440
        E.frase(c, t, b4, ps("o eixo começa em", "i", 54) + [("45", "g", 60, ERRADO)], X, 460, "center", 0.08)
        fcen(c, t, c4, "50 − 45 = 5", X, 600, 72)
        fcen(c, t, d4, "55 − 45 = 10", X, 740, 72)
        E.frase(c, t, d4 + 1.0, ps("5 e 10: parece o dobro", "i", 48, TINTA2), X, 830, "center", 0.08)
    fase(c, t, C["s04"], C["s05"] - 0.1, contas4)

    def textos5():
        E.frase(c, t, a5, ps("cortar o eixo", "i", 50) + [("come o mesmo pedaço", "g", 54, ERRADO)] + ps("de baixo de todas", "i", 50), W / 2, 270, "center", 0.08)
        E.frase(c, t, b5, ps("o que sobra", "i", 54) + [("exagera a diferença", "g", 58, ERRADO)], 1440, 600, "center", 0.08)
    fase(c, t, C["s05"], c5 - 0.1, textos5)
    if C["s05"] <= t < C["s07"]:
        E.frase(c, t, d5, ps("quase do", "i", 52) + [("mesmo tamanho", "g", 56, CERTO)], HX + EW / 2, 250, "center", 0.08)
        fcen(c, t, a6, "55 − 50 = 5", 540, 1010, 64)
        fcen(c, t, b6, "5 ÷ 50 = 0,1 = 10%", 1440, 1010, 64, COR)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, a7, ps("em", "i", 60) + [("gráfico de linhas,", "g", 66, COR)] + ps("o eixo cortado é comum", "i", 60), W / 2, 200, "center", 0.08)
    E.frase(c, t, a7 + 2.0, ps("lá importa a subida e a descida", "i", 50, TINTA2), W / 2, 280, "center", 0.08)
    dados = [("seg", 102), ("ter", 104), ("qua", 103), ("qui", 106), ("sex", 108)]
    E.serie(c, t, a7 + 0.3, dados, 420, 400, 1100, 420, vmin=100, vmax=110, marcas=[100, 105, 110], valores=False, size=42)
    circula(c, t, b7, 420 - 50, 400 + 420 - 14, 52)
    E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "confira onde o eixo começa", W / 2, 990, 54, "g", a=a, cor=E.SOBRE))


# ---------------- truque 2: escala irregular ----------------
VENDAS_ENG = [("jan", 100), ("fev", 110), ("mar", 120), ("dez", 210)]
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def b_escala(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0 = C["s10.a"], C["s10.b"]
    E.frase(c, t, a8, [("2º truque:", "g", 70, COR)] + ps("a escala irregular", "i", 64), W / 2, 170, "center", 0.1)
    x, y, w, h = 200, 330, 760, 460
    pts = E.serie(c, t, b8, VENDAS_ENG, x, y, w, h, vmin=0, vmax=240, marcas=[0, 60, 120, 180, 240], size=40)
    if c8 <= t < a0:   # o mesmo espaço entre as marcas
        for i in range(3):
            x0, x1 = x + w * (i + 0.5) / 4, x + w * (i + 1.5) / 4
            E.chave(c, x0 + 8, x1 - 8, y + h + 90, TINTA2 if i < 2 else ERRADO, ep(t, c8 + 0.2 * i, 0.4), h=18)
        E.foco(c, t, c8 + 0.6, 0.4, lambda a: centro(c, "mesmo espaço", x + w / 2, y + h + 160, 44, "i", TINTA2, a))
    if t >= d8:
        p = ep(t, d8, 0.6)
        M.line(c, *pts[2], lerp(pts[2][0], pts[3][0], p), lerp(pts[2][1], pts[3][1], p), ERRADO, 1, 14)
        E.foco(c, t, d8 + 0.5, 0.4, lambda a: centro(c, "disparou?", (pts[2][0] + pts[3][0]) / 2 - 120, (pts[2][1] + pts[3][1]) / 2 - 10, 50, "g", ERRADO, a))
    if a9 <= t < a0:
        E.foco(c, t, a9, 0.4, lambda a: centro(c, "9 meses!", x + w * 3 / 4, y + h + 160 + 60, 50, "g", ERRADO, a))
    X = 1440

    def contas():
        E.frase(c, t, a9, ps("de março a dezembro:", "i", 54) + [("9 meses", "g", 58, ERRADO)], X, 330, "center", 0.08)
        fcen(c, t, b9, "210 − 120 = 90", X, 470, 72)
        fcen(c, t, c9, "90 ÷ 9 = 10 por mês", X, 600, 68, COR)
        E.frase(c, t, d9, ps("começo do ano:", "i", 52) + [("+10 por mês", "g", 56, COR)], X, 740, "center", 0.08)
        E.frase(c, t, d9 + 1.0, ps("o mesmo ritmo", "i", 50, TINTA2), X, 820, "center", 0.08)
    fase(c, t, C["s09"], e9 - 0.1, contas)
    if t >= e9 - 0.1:
        dados = [(m if m in ("jan", "mar", "jun", "set", "dez") else "", 100 + 10 * i) for i, m in enumerate(MESES)]
        E.serie(c, t, e9, dados, 1060, y, 760, h, vmin=0, vmax=240, marcas=[0, 60, 120, 180, 240], size=36, valores=False, d=1.6)
        E.foco(c, t, e9 + 0.2, 0.4, lambda a: centro(c, "os meses no lugar certo", 1440, 290, 46, "g", CERTO, a))
    E.foco(c, t, a0, 0.5, lambda a: E.pilula(c, "mesmo espaço = mesmo passo", 700, 1000, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, b0, ps("no eixo de baixo", "i", 48, TINTA2) + [("e no do lado", "g", 50)], 1180, 1016, "left", 0.08)


# ---------------- truque 3: figura fora de proporção ----------------
FB = 900               # base das figuras
PX1, PX2 = 520, 1180   # a garrafa de antes e a de depois
PW, PH = 130, 260


def b_figura(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, a1, [("3º truque:", "g", 70, COR)] + ps("a figura fora de proporção", "i", 64), W / 2, 170, "center", 0.1)
    E.frase(c, t, b1, ps("leite da fazenda:", "i", 54) + [("dobrou", "g", 58, COR)], W / 2, 260, "center", 0.08)
    E.foco(c, t, b1 + 0.5, 0.5, lambda a: garrafa(c, PX1, FB, PW, PH, a))
    E.foco(c, t, b1 + 0.7, 0.4, lambda a: centro(c, "3.000 L", PX1, FB + 70, 54, "g", TINTA, a))
    kh = ease_io(prog(t, c1, 0.8))
    kw = ease_io(prog(t, d1, 0.8))
    if t >= c1:
        garrafa(c, PX2, FB, PW * (1 + kw), PH * (1 + kh))
        E.foco(c, t, c1 + 0.2, 0.4, lambda a: centro(c, "6.000 L", PX2, FB + 70, 54, "g", COR, a))
        E.frase(c, t, c1, [("altura × 2", "g", 50, COR)], PX2 + 230, FB - 360, "left")
    if t >= d1:
        E.frase(c, t, d1, [("largura × 2", "g", 50, ERRADO)], PX2 + 230, FB - 280, "left")
    if t >= a2:
        E.frase(c, t, a2, ps("o olho mede", "i", 50) + [("a área:", "g", 54, COR)] + ps("largura × altura", "i", 50), W / 2, 340, "center", 0.08)
        grade_area(c, t, b2, PX2, FB, PW, PH)
        E.frase(c, t, b2 + 0.4, [("2 × 2 = 4", "g", 56, ERRADO)], PX2 + 230, FB - 180, "left")
    E.frase(c, t, c2, ps("parece", "i", 56) + [("4 vezes maior", "g", 60, ERRADO)], 560, 480, "center", 0.08)
    E.frase(c, t, d2, ps("o real:", "i", 56) + [("o dobro, +100%", "g", 60, CERTO)], 560, 560, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 160, "center", 0.1)
    E.frase(c, t, a3, ps("medir o crescimento", "i", 60) + [("pelo desenho", "g", 66, ERRADO)], W / 2, 250, "center", 0.08)
    vy, cs = colunas_eixo(c, t, C["s13"], [("A", 50), ("B", 55)], 230, 380, 520, 420, 45, 55, [45, 50, 55], tv=d3)
    bw = 520 / 2 * 0.56
    pedaco(c, t, a3 + 2.0, cs[0] + bw / 2 + 20, vy(45), vy(50), "5", ERRADO)
    pedaco(c, t, a3 + 2.6, cs[1] + bw / 2 + 20, vy(45), vy(55), "10", ERRADO)
    X = 1380
    fcen(c, t, b3, "10 − 5 = 5", X, 420, 66, ERRADO)
    fcen(c, t, b3 + 2.0, "5 ÷ 5 = 1 = 100%", X, 530, 66, ERRADO)
    if t >= c3:
        E.risco(c, X - 300, 560, X + 300, 380, t, c3, largura=12)
    E.frase(c, t, c3 + 0.3, ps("os pedaços", "i", 52) + [("não são os valores", "g", 56)], X, 660, "center", 0.08)
    fcen(c, t, d3, "55 − 50 = 5", X, 790, 66, CERTO)
    fcen(c, t, d3 + 1.0, "5 ÷ 50 = 10%", X, 900, 66, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 60, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a4, [("3 olhares", "g", 80, BR)] + ps("antes de acreditar", "i", 66, CLARO), W / 2, 270, "center", 0.1)
        for i, (ti, s) in enumerate(((b4, "o eixo começa no zero?"), (c4, "mesmo espaço tem o mesmo passo?"), (d4, "a figura cresceu numa direção só?"))):
            y = 430 + i * 140
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 22, 46, a=a), centro(c, str(i + 1), 330, y - 2, 54, "g", E.SOBRE, a)))
            E.frase(c, t, ti + 0.1, ps(s, "i", 62, BR), 410, y, "left", 0.08)
        E.frase(c, t, e4, ps("algum não?", "i", 60, CLARO) + [("ignore o desenho, faça a conta", "g", 62, BR)], W / 2, 900, "center", 0.08)
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, a5, ps("gráfico honesto:", "i", 60, CLARO) + [("tamanho proporcional ao valor", "g", 64, BR)], W / 2, 260, "center", 0.08)
    E.frase(c, t, a5 + 1.6, ps("cada truque quebra essa proporção", "i", 54, CLARO), W / 2, 360, "center", 0.08)
    E.foco(c, t, b5, 0.5, lambda a: E.selo(c, 430, 560, 44, False, a))
    E.frase(c, t, b5 + 0.1, ps("não compensa:", "i", 60, CLARO) + [("gráfico sem números", "g", 64, BR)], 510, 582, "left", 0.08)
    E.frase(c, t, c5, ps("aí, compare tamanhos só se", "i", 58, CLARO) + [("os 3 olhares passarem", "g", 62, BR)], W / 2, 760, "center", 0.08)


# ---------------- questão ----------------
QX1, QX2 = 120, 980


def matriculas(c, t, t0, tv=None, x=QX1 + 150, y=330, w=520, h=320, cv=None):
    return colunas_eixo(c, t, t0, [("1º ano", 400), ("2º ano", 420)], x, y, w, h, 390, 420, [390, 400, 410, 420], tv=tv, size=40, rot_t=cv)


def caixotes(c, t, t0, tg, x=QX2 + 120, base=650, w=90, h=80):
    E.foco(c, t, t0, 0.5, lambda a: caixote(c, x, base, w, h, a))
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, "2.000 kg", x, base + 60, 42, "g", TINTA, a))
    k = ease_io(prog(t, tg, 0.8))
    if t >= tg:
        caixote(c, x + 300, base, w * (1 + k), h * (1 + k))
        E.foco(c, t, tg + 0.2, 0.4, lambda a: centro(c, "4.000 kg", x + 300, base + 60, 42, "g", COR, a))


def b_questao(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 150, passo=0.12)
    E.frase(c, t, a6, [("1)", "g", 56, COR)] + ps("matrículas de uma escola", "i", 50), QX1, 250, passo=0.08)
    matriculas(c, t, a6 + 0.4, tv=c6)
    circula(c, t, b6, QX1 + 150 - 50, 330 + 320 - 12, 46)
    E.frase(c, t, b6, ps("o eixo começa em", "i", 46, TINTA2) + [("390", "g", 50, ERRADO)], QX1, 790, passo=0.08)
    E.frase(c, t, d6, ps("parece quantas vezes maior?", "i", 48), QX1, 870, passo=0.08)
    E.frase(c, t, e6, ps("crescimento real?", "i", 48), QX1, 950, passo=0.08)
    E.frase(c, t, a7, [("2)", "g", 56, COR)] + ps("produção da horta", "i", 50), QX2, 250, passo=0.08)
    caixotes(c, t, a7 + 0.4, b7)
    E.frase(c, t, b7 + 0.4, ps("altura e largura", "i", 46, TINTA2) + [("× 2", "g", 50, ERRADO)], QX2, 790, passo=0.08)
    E.frase(c, t, c7, ps("parece quantas vezes maior?", "i", 48), QX2, 870, passo=0.08)
    E.frase(c, t, d7, ps("cresceu quantas vezes?", "i", 48), QX2, 950, passo=0.08)
    E.relogio(c, t, C["s18.a"], cx=1720, cy=480, r=120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9, e9, f9 = (C[f"s19.{k}"] for k in "abcdef")
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    X = 1400

    def um():
        E.frase(c, t, C["s19"] + 0.1, [("1)", "g", 60, COR)] + ps("matrículas", "i", 56), XE, 200, passo=0.08)
        vy, cs = matriculas(c, t, C["s19"], tv=C["s19"], x=280, y=330, w=560, h=440)
        bw = 560 / 2 * 0.56
        pedaco(c, t, a9, cs[0] + bw / 2 + 20, vy(390), vy(400), "10", ERRADO)
        pedaco(c, t, b9, cs[1] + bw / 2 + 20, vy(390), vy(420), "30", ERRADO)
        fcen(c, t, a9, "400 − 390 = 10", X, 260, 60)
        fcen(c, t, b9, "420 − 390 = 30", X, 360, 60)
        fcen(c, t, c9, "30 ÷ 10 = 3", X, 470, 62, ERRADO)
        E.frase(c, t, c9 + 0.6, ps("parece 3 vezes maior", "i", 46, ERRADO), X, 530, "center", 0.06)
        fcen(c, t, d9, "420 − 400 = 20", X, 650, 60)
        fcen(c, t, e9, "20 ÷ 400 = 0,05", X, 760, 60)
        bola_txt(c, t, f9, "5%", X, 920, 95, 70)
        E.frase(c, t, f9 + 0.3, ps("crescimento real", "i", 44, TINTA2), X - 330, 935, "center", 0.06)
    fase(c, t, C["s19"], C["s20"] - 0.1, um)
    if t < C["s20"] - 0.1:
        return
    E.frase(c, t, C["s20"] + 0.1, [("2)", "g", 60, COR)] + ps("o caixote", "i", 56), XE, 200, passo=0.08)
    caixotes(c, t, C["s20"], C["s20"], x=420, base=820, w=160, h=140)
    grade_area(c, t, a0 + 0.3, 720, 820, 160, 140)
    fcen(c, t, a0, "2 × 2 = 4", X, 340, 72)
    E.frase(c, t, b0, ps("parece", "i", 56) + [("4 vezes maior", "g", 60, ERRADO)], X, 450, "center", 0.08)
    fcen(c, t, c0, "4.000 ÷ 2.000 = 2", X, 600, 66)
    bola_txt(c, t, d0, "× 2", X, 790, 100, 76)
    E.frase(c, t, d0 + 0.4, ps("a produção só dobrou", "i", 46, TINTA2), X, 950, "center", 0.06)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", ps("confira o", "i", 58) + [("começo do eixo,", "g", 62, COR)] + [("o passo", "g", 62, COR)] + ps("e", "i", 58) + [("a figura", "g", 62, COR)]),
                 ("s21.b", ps("calcule com", "i", 58) + [("os números,", "g", 62, COR)] + ps("nunca com o desenho", "i", 58)))
        for i, (k, partes) in enumerate(itens):
            y = 440 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a0, b0, c0, d0, e0, f0 = (C[f"s22.{k}"] for k in "abcdef")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("números", "g", 100, COR)] + ps("que enganam", "i", 80), XE, 410)
    for i, (ti, s) in enumerate(((b0, "amostra ruim"), (c0, "porcentagem sobre base pequena"), (d0, "correlação que não é causa"))):
        E.frase(c, t, ti, [(f"{i + 1}.", "g", 52, COR)] + ps(s, "i", 52), XE, 540 + i * 90, passo=0.08)
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, e0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, e0 + 0.2, 0.4))
    E.frase(c, t, f0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, eixo=b_eixo, escala=b_escala, figura=b_figura, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
