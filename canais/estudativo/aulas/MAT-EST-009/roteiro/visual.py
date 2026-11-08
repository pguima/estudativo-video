"""Visual — Estudativo · MAT-EST-009: média ponderada.
Mesma linguagem da Estatística de MAT-EST-001 a 008: cada valor com a sua cor de E._paleta (o 6 e o R$ 20 na 1ª cor, o 8 e
o R$ 40 na 2ª), lista de dados em fichas (fichas(), MAT-EST-001), cartões de prova (prova(), MAT-EST-008), tabela que entra
célula a célula (quadro(), MAT-EST-001), colunas do kit (E.colunas), conta da vez à direita, resposta na esfera, atalho no
palco escuro.
Novo nesta aula (para copiar nas próximas):
- PESO = a ficha do valor repetida tantas vezes quanto o peso (o 6 duas vezes, o 8 três vezes).
- MÉDIA NA RETA = E.reta entre os valores, com um pino para cada média (pino()): a ponderada fica perto do valor de maior
  peso; a média sem peso, no meio, em cinza ou vermelho quando é o erro.
- ATALHO DE DOIS VALORES = o trecho da reta dividido em partes iguais (tantas quanto a soma dos pesos), com as partes
  andadas acesas (trilho()).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-009_media_ponderada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("peso", "regra", "loja", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
CATS = E._paleta(3)
assert 6 * 2 + 8 * 3 == 36 and 36 / 5 == 7.2 and 6 + 6 + 8 + 8 + 8 == 36 and (6 + 8) / 2 == 7
assert 30 * 20 + 10 * 40 == 1000 and 1000 / 40 == 25 and (20 + 40) / 2 == 30
assert 6 + 3 / 5 * 2 == 7.2 and 20 + 10 / 40 * 20 == 25
assert 6 * 3 + 7 * 2 + 9 * 5 == 77 and 3 + 2 + 5 == 10 and 77 / 10 == 7.7


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ² ou → vai na grotesca)"""
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
    """um dado da lista (MAT-EST-001): pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


def prova(c, cx, cy, w, h, titulo, valor, a=1.0, cor=None, borda=None):
    """o cartão de uma prova (MAT-EST-008): nome em cima, nota grande"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, BR, a)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22)
    c.drawRRect(rr, M.paint(borda or FIO, a, stroke=4 if borda is None else 7))
    centro(c, titulo, cx, cy - h / 2 + 52, 36, "i", TINTA2, a)
    centro(c, valor, cx, cy + h * 0.32, h * 0.45, "g", cor or TINTA, a)


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados (MAT-EST-001). colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...]"""
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
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            if k == 0 and cores:
                E.foco(c, t, ti, 0.4, lambda a, yy=yy, j=j: c.drawCircle(xs[0] + 22, yy - size * 0.34, size * 0.24, M.paint(cores[j], a)))
                cx += 22
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: centro(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else TINTA, a))
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
            cx = xs[k] + colunas[k][1] / 2 + (22 if k == 0 and cores else 0)
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else TINTA, a))
    return bases


# ================= peças da média ponderada (copiar nas próximas aulas) =================
def pino(c, t, t0, vx, y, v, rotulo, cor=None, alto=90, size=44, t1=None):
    """um pino na reta no valor v, com a pílula em cima"""
    q = ease_back(prog(t, t0, 0.45)) * (1 - ep(t, t1, 0.4) if t1 is not None else 1)
    if q <= 0:
        return
    k = cor or E.COR
    x = vx(v)
    M.line(c, x, y, x, y - alto * q, k, min(1, q), 6)
    c.drawCircle(x, y, 14 * q, M.paint(k, min(1, q)))
    E.pilula(c, rotulo, x, y - alto - 30, size, "g", fundo=k, cor=M.on(k), a=min(1, q))


def trilho(c, t, vx, y, v0, v1, n, acesas, ta, cor=None, tinta=TINTA, lw=14):
    """o trecho de v0 a v1 dividido em n partes iguais (risquinhos), com 'acesas' partes andadas a partir de ta"""
    k = cor or E.COR
    x0, x1 = vx(v0), vx(v1)
    for i in range(1, n):
        x = lerp(x0, x1, i / n)
        M.line(c, x, y - 14, x, y + 14, tinta, ep(t, ta - 0.6, 0.4), 4)
    p = ease_io(prog(t, ta, 0.4 * max(1, acesas)))
    if p > 0:
        M.line(c, x0, y, lerp(x0, lerp(x0, x1, acesas / n), p), y, k, 1, lw)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, a1, 0.5, lambda a: prova(c, 400, 420, 300, 320, "prova 1", "6", a, CATS[0]))
        E.foco(c, t, a1 + 0.6, 0.4, lambda a: E.pilula(c, "peso 2", 400, 640, 50, "g", fundo=CATS[0], a=a))
        E.foco(c, t, b1, 0.5, lambda a: prova(c, 800, 420, 300, 320, "prova 2", "8", a, CATS[1]))
        E.foco(c, t, b1 + 0.6, 0.4, lambda a: E.pilula(c, "peso 3", 800, 640, 50, "g", fundo=CATS[1], cor=TINTA, a=a))
        X = 1460
        E.frase(c, t, lerp(b1, c1, 0.5), ps("a média não é", "i", 60), X, 330, "center", 0.1)
        E.foco(c, t, lerp(b1, c1, 0.5) + 0.5, 0.5, lambda a: E.escreve(c, "7", X - 40, 520, 160, "g", ERRADO, a))
        if t >= lerp(b1, c1, 0.5) + 1.2:
            E.risco(c, X - 90, 520, X + 90, 380, t, lerp(b1, c1, 0.5) + 1.2, largura=12)
        bola_txt(c, t, c1, "7,2", X, 760, 130, 92)
        E.frase(c, t, c1 + 1.2, ps("o peso explica", "i", 50, TINTA2), X, 960, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 300, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("qualquer média", "i", 88), XE, 450, passo=0.14)
        E.frase(c, t, ta + 2.6, [("com pesos", "g", 104, COR)], XE, 600, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa:", XE + 175, 700, 120, "i", TINTA, a))
    E.frase(c, t, C["s03.a"] + 0.6, [("média aritmética", "g", 80, COR)], XE, 860)
    x, w = 980, 820
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 360, w, 260, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, ps("a soma dividida", "i", 56), x + 44, 450, "left", 0.1)
    E.frase(c, t, C["s03.b"] + 0.6, ps("pela quantidade", "i", 56), x + 44, 520, "left", 0.1)
    E.formula_em(c, t, C["s03.b"] + 1.2, "f{6 + 7 + 8}{3} = 7", x + w - 60, 590, 52, "g", COR, "right")
    E.cursor(c, x + w - 30, 600, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.b"], C["s03.end"], 0.6), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 760, "left", 0.1)


# ---------------- o que é peso ----------------
FY = 560


def fichas_peso(c, t, t6, t8, x0=260, y=FY, size=70, gap=60, cor6=None, cor8=None):
    """o 6 duas vezes e o 8 três vezes; devolve os centros"""
    pts = []
    w = E.larg("6", "b", size) + size * 1.1
    for i in range(5):
        cx = x0 + w / 2 + i * (w + gap) + (40 if i >= 2 else 0)
        s, ti, cor = ("6", t6 + 0.4 * i, cor6 or CATS[0]) if i < 2 else ("8", t8 + 0.4 * (i - 2), cor8 or CATS[1])
        E.foco(c, t, ti, 0.45, lambda a, s=s, cx=cx, cor=cor: ficha(c, s, cx, y, size, a, cor), sobe=30)
        pts.append(cx)
    return pts


def b_peso(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    pts = fichas_peso(c, t, b4, c4)
    E.frase(c, t, C["s04"] + 0.2, ps("o que é", "i", 66) + [("peso?", "g", 72, COR)], XE, 220, passo=0.12)
    E.frase(c, t, a4, ps("quantas vezes o valor", "i", 60) + [("conta", "g", 66, COR)], XE, 340, passo=0.1)
    E.foco(c, t, b4 + 0.6, 0.4, lambda a: centro(c, "peso 2", (pts[0] + pts[1]) / 2, FY + 130, 46, "g", COR, a))
    E.foco(c, t, c4 + 1.0, 0.4, lambda a: centro(c, "peso 3", pts[3], FY + 130, 46, "g", COR, a))
    p = ep(t, a5, 0.5)
    if p > 0:
        E.chave(c, pts[0] - 70, pts[4] + 70, FY - 90, E.COR, p, -26, 6)
        E.foco(c, t, a5 + 0.3, 0.4, lambda a: centro(c, "5 notas", (pts[0] + pts[4]) / 2, FY - 140, 56, "g", COR, a))
    X = 1500
    fcen(c, t, b5, "6 + 6 + 8 + 8 + 8 = 36", W / 2, 800, 70)
    fcen(c, t, c5, "36 ÷ 5", X - 100, 940, 70)
    bola_txt(c, t, c5 + 0.6, "7,2", X + 200, 915, 85, 64)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9 = C["s09.a"], C["s09.b"]
    s8 = C["s08"]

    def um():
        for i, (ti, l1, l2) in enumerate(((a6, "multiplique", "cada valor pelo peso"), (b6, "some", "os resultados"),
                                          (c6, "divida", "pela soma dos pesos"))):
            y = 300 + i * 200
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 42, y - 22, 42, a=a), centro(c, str(i + 1), XE + 42, y - 2, 50, "g", E.SOBRE, a)))
            E.frase(c, t, ti + 0.1, [(l1, "g", 62, COR)], XE + 108, y, "left", 0.1)
            E.frase(c, t, ti + 0.4, ps(l2, "i", 50, TINTA2), XE + 108, y + 62, "left", 0.1)
        X = 1400
        fcen(c, t, a7, "6 · 2 = 12", X, 310, 66)
        fcen(c, t, b7, "8 · 3 = 24", X, 420, 66)
        fcen(c, t, c7, "12 + 24 = 36", X, 560, 66)
        fcen(c, t, d7, "pesos: 2 + 3 = 5", X, 700, 60, TINTA2)
        fcen(c, t, e7, "36 ÷ 5", X - 120, 880, 70)
        bola_txt(c, t, e7 + 0.6, "7,2", X + 180, 855, 95, 66)
    fase(c, t, C["s06"], s8 - 0.1, um)
    if t < s8 - 0.1:
        return
    y = 620
    vx = E.reta(c, t, s8, 300, 1620, y, 6, 8, [6, 7, 8], E._num, size=56)
    for v, cor in ((6, CATS[0]), (8, CATS[1])):
        E.foco(c, t, s8 + 0.3, 0.4, lambda a, v=v, cor=cor: c.drawCircle(vx(v), y, 22, M.paint(cor, a)))
    pino(c, t, a8, vx, y, 7.2, "7,2", alto=120, size=50)
    p = ep(t, a8 + 0.8, 0.5)
    if p > 0:
        M.arrow(c, vx(7.2) + 30, y + 150, vx(8) - 20, y + 150, E.COR, p, 6, 20, ease_io(prog(t, a8 + 0.8, 0.6)))
    E.frase(c, t, a8 + 1.0, ps("mais perto do", "i", 50) + [("8", "g", 56, COR)], vx(7.6), y + 230, "center", 0.1)
    E.frase(c, t, s8 + 0.2, ps("onde fica o", "i", 60) + [("7,2?", "g", 66, COR)], W / 2, 220, "center", 0.1)
    if t < a9 + 0.4:
        E.saida(c, t, a9 - 0.1, lambda: E.foco(c, t, b8, 0.5, lambda q: E.pilula(c, "puxada para o valor de maior peso", W / 2, 340, 50, "g", a=q, cor=E.SOBRE)))
    pino(c, t, a9, vx, y, 7, "7", TINTA2, alto=160, size=50)
    if t >= a9:
        E.foco(c, t, a9 + 0.3, 0.4, lambda q: E.pilula(c, "pesos iguais: (6 + 8) ÷ 2 = 7", W / 2, 330, 48, "g", fundo=TINTA2, a=q))
    E.foco(c, t, b9, 0.5, lambda q: E.selo(c, 360, 960, 44, False, q))
    E.frase(c, t, b9 + 0.1, ps("quem responde 7", "i", 50) + [("esquece o peso", "g", 54, ERRADO)], 430, 982, "left", 0.1)


# ---------------- a loja ----------------
GL = (200, 340, 620, 500)
CAMISAS = [("R$ 20", 30, CATS[0]), ("R$ 40", 10, CATS[1])]


def loja(c, t, ta, tb, x=GL[0], y=GL[1], w=GL[2], h=GL[3], size=44):
    E.colunas(c, t, ta - 0.3, CAMISAS, x, y, w, h, vmax=34, passo=max(0.1, tb - ta), size=size)
    E.foco(c, t, ta, 0.4, lambda a: E.escreve(c, "camisas vendidas", x - 10, y - 60, 40, "i", TINTA2, a))


def b_loja(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    loja(c, t, a0, b0)
    X = 1400

    def um():
        E.frase(c, t, C["s10"] + 0.2, ps("o peso nem sempre vem", "i", 54), X, 260, "center", 0.1)
        E.frase(c, t, C["s10"] + 1.4, ps("escrito como peso", "i", 54), X, 330, "center", 0.1)
        E.frase(c, t, a0, [("30 camisas", "g", 60, COR)] + ps("a R$ 20", "i", 56), X, 480, "center", 0.1)
        E.frase(c, t, b0, [("10 camisas", "g", 60, COR)] + ps("a R$ 40", "i", 56), X, 580, "center", 0.1)
        E.frase(c, t, lerp(b0, c0, 0.5), [("preço médio?", "g", 62)], X, 700, "center", 0.1)
        E.foco(c, t, c0, 0.5, lambda q: E.pilula(c, "peso = quantas camisas", X, 850, 52, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s10"], C["s11"] - 0.1, um)
    if t < C["s11"] - 0.1:
        return
    fcen(c, t, a1, "30 · 20 = 600", X, 270, 64)
    fcen(c, t, b1, "10 · 40 = 400", X, 380, 64)
    fcen(c, t, c1, "600 + 400 = 1.000", X, 510, 64)
    fcen(c, t, d1, "pesos: 30 + 10 = 40", X, 640, 58, TINTA2)
    fcen(c, t, e1, "1.000 ÷ 40 = 25", X, 790, 64, COR)
    bola_txt(c, t, e1 + 0.7, "R$ 25", X, 940, 95, 52)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    loja(c, t, -9, -9, 160, 300, 520, 400, 40)
    y = 950
    vx = E.reta(c, t, C["s12"], 860, 1720, y, 20, 40, [20, 25, 30, 40], lambda v: "R$ " + E._num(v), size=44)
    pino(c, t, b2 + 0.8, vx, y, 30, "R$ 30?", ERRADO, alto=110, size=44)
    pino(c, t, d2, vx, y, 25, "R$ 25", alto=190, size=44)
    X = 1300
    E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 62, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a2, ps("esquecer os pesos", "i", 56), X, 285, "center", 0.1)
    fcen(c, t, b2, "(20 + 40) ÷ 2 = 30", X, 400, 64, ERRADO)
    E.frase(c, t, c2, ps("saíram muito mais", "i", 52) + [("camisas de 20", "g", 56, COR)], X, 510, "center", 0.1)
    E.frase(c, t, d2, ps("o preço médio fica", "i", 50) + [("perto de 20", "g", 54, COR)], X, 600, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    s4 = C["s14"]
    y = 560

    def um():
        vx = E.reta(c, t, C["s13"] + 0.2, 300, 1620, y, 6, 8, [6, 8], E._num, escuro=True, size=60)
        p = ep(t, b3, 0.5)
        if p > 0:
            E.chave(c, vx(6), vx(8), y + 120, CLARO, p, 22, 6)
            E.foco(c, t, b3 + 0.3, 0.4, lambda a: centro(c, "distância 2", (vx(6) + vx(8)) / 2, y + 200, 50, "g", BR, a))
        trilho(c, t, vx, y, 6, 8, 5, 3, c3 + 0.6, E.mix(E.COR, BR, 0.35), CLARO)
        pino(c, t, e3, vx, y, 7.2, "7,2", BR, alto=110, size=54)
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho, para dois valores:", "i", 58, CLARO), W / 2, 200, "center", 0.1)
        E.frase(c, t, a3, ps("ande do menor para o maior,", "i", 56, CLARO) + [("na fração do peso", "g", 60, BR)], W / 2, 290, "center", 0.08)
        E.frase(c, t, c3, ps("o 8 tem", "i", 54, CLARO) + [("3 dos 5 pesos", "g", 58, BR)], 500, 880, "center", 0.1)
        fcen(c, t, d3, "f{3}{5} de 2 = 1,2", 1100, 890, 60, BR)
        fcen(c, t, e3, "6 + 1,2 = 7,2", 1600, 890, 60, BR)
    fase(c, t, C["s13"], s4 - 0.1, um)
    if t < s4 - 0.1:
        return
    E.frase(c, t, s4 + 0.2, ps("funciona porque", "i", 58, CLARO), W / 2, 190, "center", 0.1)
    E.frase(c, t, a4, [("3 das 5 notas", "g", 60, BR)] + ps("subiram de 6 para 8", "i", 56, CLARO), W / 2, 280, "center", 0.1)
    y2 = 560
    vx = E.reta(c, t, b4 - 1.6, 300, 1500, y2, 20, 40, [20, 40], lambda v: "R$ " + E._num(v), escuro=True, size=50)
    trilho(c, t, vx, y2, 20, 40, 4, 1, b4 + 0.4, E.mix(E.COR, BR, 0.35), CLARO)
    E.frase(c, t, b4 - 1.6, ps("na loja:", "i", 54, CLARO), 300, 430, "left", 0.1)
    E.frase(c, t, b4, ps("o 40 tem", "i", 52, CLARO) + [("10 das 40: um quarto", "g", 56, BR)], 1000, 430, "left", 0.1)
    fcen(c, t, c4, "f{1}{4} de 20 = 5", 700, 760, 60, BR)
    fcen(c, t, c4 + 1.4, "20 + 5 = 25", 1250, 760, 60, BR)
    pino(c, t, c4 + 1.4, vx, y2, 25, "R$ 25", BR, alto=100, size=44)
    E.foco(c, t, d4, 0.5, lambda q: E.selo(c, 520, 920, 44, False, q))
    E.frase(c, t, d4 + 0.1, ps("3 valores ou mais:", "i", 52, CLARO) + [("multiplique, some e divida", "g", 54, BR)], 590, 942, "left", 0.08)


# ---------------- questão ----------------
MAT = [("matemática", 3, 6), ("português", 2, 7), ("redação", 5, 9)]


def selecao(c, t, x, y, tp, tn, size=54, prod=None, cores=None):
    cols = [("matéria", 360, tp - 0.4), ("peso", 180, tp - 0.2), ("nota", 180, tn)] + ([("nota × peso", 320, prod[0] - 0.3)] if prod else [])
    linhas = []
    for j, (m, p, n) in enumerate(MAT):
        lin = [(m, tp - 0.4 + 0.2 * j), (str(p), tp + 0.4 * j), (str(n), tn + 0.4 * j, COR)]
        if prod:
            lin.append((str(p * n), prod[j], COR))
        linhas.append(lin)
    return quadro(c, t, x, y, cols, linhas, None, size, size * 1.7, cores=cores or CATS)


def b_questao(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, ps("nota final com", "i", 58) + [("pesos", "g", 64, COR)], XE, 300, passo=0.1)
    E.frase(c, t, c5, ps("qual é a", "i", 60) + [("nota final?", "g", 66, COR)], XE, 900, passo=0.1)
    E.saida(c, t, C["s16.a"] - 0.1, lambda: selecao(c, t, XE, 470, a5 + 1.0, b5))
    E.relogio(c, t, C["s16.a"], 1440, 540, 200)


def b_resposta(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    if t >= d8:
        p = ep(t, d8, 0.4)
        M.rrect(c, 120 - 15, 300 + 20 + 54 * 1.7 * 3 - 54 * 1.7 * 0.3 - 54 * 0.98, 1060 + 30, 54 * 1.36, 14, E.mix(E.COR, PAPEL, 0.86), p)
    selecao(c, t, 120, 300, -9, -9, prod=[a7, b7, c7])
    X = 1500
    fcen(c, t, d7, "18 + 14 + 45 = 77", 650, 760, 66)
    if t < C["s18"] - 0.1:
        return
    fcen(c, t, a8, "pesos: 3 + 2 + 5 = 10", 650, 880, 58, TINTA2)
    E.frase(c, t, b8, ps("÷ 10: a vírgula anda", "i", 50) + [("1 casa", "g", 54, COR)], X, 320, "center", 0.1)
    fcen(c, t, c8, "77 ÷ 10 = 7,7", X, 520, 72)
    bola_txt(c, t, c8 + 0.6, "7,7", X, 720, 110, 80)
    E.frase(c, t, d8, ps("a redação, de maior peso,", "i", 46, TINTA2), X, 900, "center", 0.08)
    E.frase(c, t, d8 + 1.0, [("puxou para cima", "g", 52, COR)], X, 970, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s19.a", ps("multiplique cada valor pelo", "i", 60) + [("peso", "g", 66, COR)]),
                 ("s19.b", [("some", "g", 66, COR)]),
                 ("s19.c", ps("divida pela", "i", 60) + [("soma dos pesos", "g", 66, COR)]),
                 ("s19.d", ps("a média é puxada para o", "i", 60) + [("maior peso", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 370 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 50, a=a), centro(c, str(i + 1), 200, y - 4, 58, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula, mais duas médias", "i", 76), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("geométrica:", "g", 80, COR)] + ps("4 e 9 dão 6", "i", 70), XE, 420, passo=0.12)
    E.frase(c, t, b0, [("harmônica:", "g", 80, COR)] + ps("40 e 60 km/h dão 48", "i", 70), XE, 560, passo=0.12)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(960, 785, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, peso=b_peso, regra=b_regra, loja=b_loja, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
