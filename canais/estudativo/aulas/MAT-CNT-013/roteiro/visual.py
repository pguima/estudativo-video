"""Visual — Estudativo · MAT-CNT-013: evento complementar, o que não pode acontecer.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 012): casinhas() com × e igual_bola() com o resultado na esfera,
bloco() em volta de um grupo, espaco() para o espaço amostral (Ω), dado()/tabela66() da MAT-CNT-011/012, E.arvore da MAT-CNT-001.
Peças desta aula:
- moeda_gira(): moeda do kit (E.moeda) girando até parar numa face; Ca = cara (cor da matéria), Co = coroa (cinza).
- chip(): um resultado das três moedas ("Ca Co Co") numa pílula de contorno.
- linha(): conta numa linha com texto e frações de verdade (P(A) = 1 − 1/8), cada parte no seu instante.
- fora(): universo com o conjunto A e o lado de fora pintado (o complementar Ā), como na MAT-CON-002.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
from itertools import product
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-013_evento_complementar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("moedas", "regra", "chute", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
VERM = "#D94B3D"
RES = list(product(("Ca", "Co"), repeat=3))
PELO_MENOS = [r for r in RES if "Ca" in r]
EXATA = [r for r in RES if r.count("Ca") == 1]
assert len(RES) == 2 * 2 * 2 == 8 and [r for r in RES if "Ca" not in r] == [("Co", "Co", "Co")] and len(PELO_MENOS) == 8 - 1 == 7
assert Fr(1) - Fr(1, 8) == Fr(7, 8) and Fr(7, 8) * 100 == Fr(175, 2) and Fr(7, 8) + Fr(1, 8) == 1
assert EXATA == [("Ca", "Co", "Co"), ("Co", "Ca", "Co"), ("Co", "Co", "Ca")] and Fr(len(EXATA), 8) == Fr(3, 8)
assert 5 * 5 == 25 and 4 * 4 == 16 and 25 - 16 == 9 and Fr(9, 25) * 100 == 36 and Fr(1) - Fr(16, 25) == Fr(9, 25)
D2 = list(product(range(1, 7), repeat=2))
assert len(D2) == 36 and sum(1 for b, v in D2 if 6 not in (b, v)) == 25 and sum(1 for b, v in D2 if 6 in (b, v)) == 11 == 36 - 25
assert Fr(11, 36) < Fr(1, 3) and Fr(36 - 1, 36) == Fr(35, 36)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (iguais às da MAT-CNT-002) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def casinhas(c, t, cx, y, itens, s=180, gap=None, tx=None, escuro=False, size=None, tnomes=None):
    """as casinhas do princípio multiplicativo, centradas em cx; y = centro das caixas.
    itens = [(nome embaixo, valor, t_caixa, t_valor[, cor do valor])]. Devolve o centro de cada caixa."""
    n = len(itens)
    gap = s * 0.62 if gap is None else gap
    if size is None:
        vals = [len(str(it[1])) for it in itens if it[1] is not None]
        maior = max(vals) if vals else 1
        size = s * (0.56 if maior <= 1 else 0.46 if maior == 2 else 0.36)
    x0 = cx - (n * s + (n - 1) * gap) / 2
    xs = [x0 + s / 2 + i * (s + gap) for i in range(n)]
    borda = BR if escuro else TINTA
    for i, it in enumerate(itens):
        nome, val, tb, tv = it[:4]
        cor_v = it[4] if len(it) > 4 else (BR if escuro else (CINZA if val == "?" else COR))
        x = xs[i]

        def caixa(a, x=x):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s / 2, s, s), s * 0.12, s * 0.12)
            if escuro:
                c.drawRRect(r, M.paint(BR, 0.08 * a))
            else:
                sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
                sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
                c.save(); c.translate(0, 8); c.drawRRect(r, sh); c.restore()
                c.drawRRect(r, M.paint(BR, a))
            c.drawRRect(r, M.paint(borda, a, stroke=5))
        E.foco(c, t, tb, 0.45, caixa)
        if nome:
            tn = tnomes[i] if tnomes else tb + 0.15
            E.foco(c, t, tn, 0.45, lambda a, x=x, nome=nome: centro(c, nome, x, y + s / 2 + max(52, s * 0.34), max(42, s * 0.27), "i",
                                                                  CLARO if escuro else TINTA2, a))
        if val is not None and tv is not None:
            E.foco(c, t, tv, 0.45, lambda a, x=x, val=str(val), cv=cor_v: E.formula(c, val, x, y + size * 0.36, size, "g", cv, a, "center"))
        if i:
            ti = tx[i - 1] if tx else tb
            if ti is not None:
                E.sinal(c, t, ti, "×", (xs[i - 1] + x) / 2, y, s * 0.42, BR if escuro else TINTA)
    return xs


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do grupo: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


# ---------------- peças da MAT-CNT-011 e da MAT-CNT-012 ----------------
PINTAS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
          5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, a=1.0, cor=None, fundo=BR, borda=None, sombra=True):
    """face de dado com as pintas; dado vermelho = fundo VERM, pintas brancas"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    if sombra:
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda or (TINTA if fundo == BR else M.mix(fundo, "#000000", 0.35)), a, stroke=max(3, s * 0.035)))
    k = s * 0.27
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * k, cy + dy * k, s * 0.085, M.paint(cor or (TINTA if fundo == BR else BR), a))


def branco(c, cx, cy, s, n, a=1.0):
    dado(c, cx, cy, s, n, a)


def vermelho(c, cx, cy, s, n, a=1.0):
    dado(c, cx, cy, s, n, a, fundo=VERM)


def espaco(c, x, y, w, h, a=1.0, rotulo="Ω", cor=None):
    """retângulo do espaço amostral, com o nome no canto"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30)
    c.drawRRect(r, M.paint(BR, 0.55 * a))
    c.drawRRect(r, M.paint(cor or TINTA2, a, stroke=5))
    E.escreve(c, rotulo, x + 26, y + 70, 60, "g", cor or TINTA2, a)


def tabela66(c, t, t0, x, y, cel, tl=None, tc=None, pinta=None):
    """tabela dos dois dados: (x, y) = canto de cima à esquerda da grade; linhas = dado branco, colunas = dado vermelho.
    pinta = {(b, v): (t0, cor, texto)}. Devolve a função (b, v) → centro do quadradinho"""
    centro_ = lambda b, v: (x + (v - 0.5) * cel, y + (b - 0.5) * cel)

    def grade(a):
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 6 * cel, 6 * cel), 16, 16), M.paint(BR, 0.85 * a))
        for i in range(7):
            M.line(c, x + i * cel, y, x + i * cel, y + 6 * cel, TINTA2, a * 0.5, 2.5)
            M.line(c, x, y + i * cel, x + 6 * cel, y + i * cel, TINTA2, a * 0.5, 2.5)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 6 * cel, 6 * cel), 16, 16), M.paint(TINTA, a, stroke=4))
    E.foco(c, t, t0, 0.5, grade)
    for i in range(1, 7):
        E.foco(c, t, (tl if tl is not None else t0) + 0.08 * i, 0.4, lambda a, i=i: branco(c, x - cel * 0.62, y + (i - 0.5) * cel, cel * 0.72, i, a))
        E.foco(c, t, (tc if tc is not None else t0) + 0.08 * i, 0.4, lambda a, i=i: vermelho(c, x + (i - 0.5) * cel, y - cel * 0.62, cel * 0.72, i, a))
    for (b, v), (tp, cor, txt) in (pinta or {}).items():
        cx, cy = centro_(b, v)

        def cheia(a, cx=cx, cy=cy, cor=cor, txt=txt):
            m = cel * 0.08
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - cel / 2 + m, cy - cel / 2 + m, cel - 2 * m, cel - 2 * m), 10, 10), M.paint(cor, a))
            if txt:
                centro(c, txt, cx, cy + cel * 0.13, cel * 0.36, "g", BR, a)
        E.foco(c, t, tp, 0.35, cheia, sobe=4)
    return centro_


# ---------------- peças desta aula ----------------
def moeda_gira(c, t, t0, cx, cy, r, final, tpara, escuro=False):
    """moeda que gira (a face troca a cada meia volta) e para na face final em tpara"""
    def f(a):
        if t < tpara:
            fase = (t - t0) * 2.4
            k = max(0.08, abs(math.cos(fase * math.pi)))
            face = "Ca" if int(fase + 0.5) % 2 == 0 else "Co"
        else:
            k, face = 1.0, final
        c.save(); c.translate(cx, cy); c.scale(k, 1)
        E.moeda(c, 0, 0, r, face, a, E.COR if face == "Ca" else (CINZA if escuro else TINTA2))
        c.restore()
    E.foco(c, t, t0, 0.5, f)


def moeda(c, cx, cy, r, face, a=1.0):
    E.moeda(c, cx, cy, r, face, a, E.COR if face == "Ca" else TINTA2)


def chip(c, cx, cy, txt, a=1.0, cor=None, size=44, cheio=False):
    """um resultado ("Ca Co Co") numa pílula de contorno; cheio = pílula pintada"""
    if a <= 0:
        return
    cor = cor or COR
    w, h = E.larg(txt, "b", size) + size * 1.1, size * 1.7
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(r, M.paint(cor if cheio else BR, a))
    c.drawRRect(r, M.paint(cor, a, stroke=4))
    centro(c, txt, cx, cy + size * 0.35, size, "b", BR if cheio else cor, a)


def larg_parte(p, size):
    return E.larg(p, "g", size) if isinstance(p, str) else max(E.larg(str(p[0]), "g", size), E.larg(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: E.escreve(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def fora(c, x, y, w, h, cx, cy, r, a=1.0, pinta=1.0, nome="A", size=60):
    """universo (x, y, w, h) com o conjunto A (círculo em cx, cy) e o lado de fora pintado: o complementar Ā"""
    if a <= 0:
        return
    rect = skia.Rect.MakeXYWH(x, y, w, h)
    if pinta > 0:
        p = skia.Path(); p.addRect(rect); p.addCircle(cx, cy, r); p.setFillType(skia.PathFillType.kEvenOdd)
        c.drawPath(p, M.paint(E.COR, 0.3 * a * pinta))
    c.drawRect(rect, M.paint(TINTA, a, stroke=4))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=6))
    E.escreve(c, "U", x + 8, y - 16, 56, "i", TINTA2, a)
    centro(c, nome, cx, cy + size * 0.36, size, "g", COR, a)


def pil_esq(c, t, t0, x, y, txt, size=46, fundo=None, cor=BR):
    """pílula com a borda esquerda em x"""
    w = E.larg(txt, "g", size) + size * 1.1
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x + w / 2, y, size, estilo="g", fundo=fundo or TINTA2, cor=cor, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        for i, (x, f) in enumerate(((300, "Ca"), (480, "Co"), (660, "Ca"))):
            moeda_gira(c, t, C["s01.a"] - 0.2 + 0.12 * i, x, 340, 82, f, C["s01.b"] - 0.3 + 0.15 * i)
        E.frase(c, t, C["s01.a"] + 0.2, [("você", "i", 80), ("lança", "i", 80), ("3", "g", 88, COR), ("moedas", "g", 84)], 840, 320)
        E.frase(c, t, C["s01.b"], [("pelo", "i", 80), ("menos", "i", 80), ("uma", "g", 88, COR), ("cara?", "g", 88, COR)], 840, 450)
        # o único resultado sem cara
        for i, x in enumerate((300, 440, 580)):
            E.foco(c, t, C["s01.c"] + 0.1 * i, 0.45, lambda a, x=x: moeda(c, x, 740, 62, "Co", a))
        nota(c, t, C["s01.c"] + 0.5, 440, 880, "o único sem cara", 50, TINTA2, "i")
        y = 740
        xs, xf = linha(c, t, 820, y, 110, [("1 −", lerp(C["s01.c"], C["s01.d"], 0.55)), ((1, 8), lerp(C["s01.c"], C["s01.d"], 0.55) + 0.2)])
        E.sinal(c, t, C["s01.d"] - 0.1, "=", xf + 80, y, 100)
        E.resultado(c, t, C["s01.d"], 7, 8, xf + 290, y, 110, 130)
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 300)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 100), ("chance", "g", 120, COR), ("pelo", "i", 100)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.3, [("lado", "i", 100), ("contrário", "g", 116)], XE, 600)
        pil_esq(c, t, C["s02.b"], XE, 760, "quando economiza tempo", 50)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1480, 490, 88, "g", BR, a),
                                                      E.centro(c, "de prova", 1480, 600, 88, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84), ("duas", "g", 88, COR), ("coisas", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 200, "probabilidade"), ("s03.c", 1000, "complementar")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 620, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 64, COR)], x + 360, 400, "center")
    E.foco(c, t, C["s03.b"] + 0.4, 0.45, lambda a: E.escreve(c, "P =", 250, 640, 96, "g", TINTA, a))
    E.fr(c, t, C["s03.b"] + 0.7, "favoráveis", "possíveis", 640, 610, 66, COR)
    E.foco(c, t, C["s03.c"] + 0.4, 0.5, lambda a: fora(c, 1130, 510, 460, 280, 1300, 650, 110, a, ep(t, C["s03.c"] + 1.6, 0.6)))
    E.foco(c, t, C["s03.c"] + 1.8, 0.45, lambda a: E.escreve(c, "Ā", 1475, 610, 76, "g", COR, a))
    nota(c, t, C["s03.c"] + 2.0, 1360, 870, "o que fica fora de A", 48, TINTA2, "i")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.75), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- espaço amostral e árvore ----------------
def folha(cam):
    n = cam.count("Ca")
    return "nenhuma" if n == 0 else f"{n} cara" + ("s" if n > 1 else "")


def b_moedas(c, t, C, b):
    def casas():
        E.frase(c, t, C["s04.a"], [("todos", "g", 76, COR), ("os", "i", 72), ("resultados", "i", 72), ("possíveis", "i", 72)], W / 2, 180, "center")
        E.foco(c, t, C["s04.b"], 0.45, lambda a: moeda(c, 320, 470, 95, "Ca", a))
        E.foco(c, t, C["s04.b"] + 0.3, 0.45, lambda a: moeda(c, 560, 470, 95, "Co", a))
        nota(c, t, C["s04.b"] + 0.2, 320, 640, "cara", 52, COR, "g")
        nota(c, t, C["s04.b"] + 0.5, 560, 640, "coroa", 52, TINTA2, "g")
        nota(c, t, C["s04.b"] + 0.8, 440, 740, "2 faces", 52, TINTA2, "i")
        tc = C["s04.c"]
        casinhas(c, t, 1180, 470, [(f"moeda {i + 1}", 2, tc + 0.2 * i, tc + 0.6 + 0.2 * i) for i in range(3)], s=150)
        igual_bola(c, t, C["s04.d"] + 1.2, 1560, 470, "8", r=100)
        E.foco(c, t, C["s04.d"] + 1.6, 0.45, lambda a: E.centro(c, "8 resultados", 1180, 800, 64, "g", TINTA, a))
    E.saida(c, t, C["s05"] - 0.1, casas)
    if t < C["s05"]:
        return
    ta = C["s05.a"]
    tb = [C["s05.b"], lerp(C["s05.b"], C["s05.c"], 0.2), lerp(C["s05.b"], C["s05.c"], 0.42)]
    dest = tuple(r for r in RES if r.count("Ca") and t >= tb[r.count("Ca") - 1])
    pos = E.arvore(c, t, ta, [("Ca", "Co")] * 3, 90, 150, 1000, 860, folha=folha, tn=[ta, ta + 0.5, ta + 1.0], tf=ta + 1.6,
                   destaque=dest, size=48)
    # a ponta que fica de fora
    px, py = pos[("Co", "Co", "Co")]
    if t >= C["s05.c"]:
        E.caixa_pontilhada(c, px - 60, py - 46, 400, 92, ep(t, C["s05.c"], 0.4), ERRADO, ep(t, C["s05.c"], 0.4))

    def painel5():
        E.frase(c, t, ta + 1.6, [("8", "g", 96, COR), ("pontas", "i", 84)], 1220, 270)
        E.frase(c, t, C["s05.b"] - 0.3, ps("pelo menos 1 cara:", "i", 58), 1220, 420, passo=0.08)
        E.foco(c, t, tb[0], 0.4, lambda a: E.escreve(c, "1,", 1220, 520, 72, "g", COR, a))
        E.foco(c, t, tb[1], 0.4, lambda a: E.escreve(c, "2", 1300, 520, 72, "g", COR, a))
        E.foco(c, t, tb[2], 0.4, lambda a: E.escreve(c, "ou 3 caras", 1370, 520, 72, "g", COR, a))
        E.frase(c, t, C["s05.c"], ps("fica de fora:", "i", 58), 1220, 690, passo=0.08)
        E.foco(c, t, C["s05.d"], 0.45, lambda a: chip(c, 1400, 790, "Co Co Co", a, ERRADO, 52))
    E.saida(c, t, C["s06"] - 0.1, painel5)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"] - 0.2, 0.4, lambda a: E.escreve(c, "favoráveis", 1220, 260, 58, "i", TINTA2, a))
    E.formula_em(c, t, C["s06.a"], "8 − 1 = 7", 1220, 370, 96, "g", TINTA)
    xs, xf = linha(c, t, 1220, 530, 110, [("P =", C["s06.b"]), ((7, 8), C["s06.b"] + 0.2, COR)])
    E.frase(c, t, C["s06.c"], [("não", "g", 58, ERRADO), ("contou", "i", 56), ("o", "i", 56), ("que", "i", 56), ("pode", "i", 56)], 1220, 760, passo=0.1)
    E.frase(c, t, C["s06.d"], [("contou", "i", 56), ("o", "i", 56), ("que", "i", 56), ("não", "g", 58, COR), ("pode", "g", 58, COR)], 1220, 860, passo=0.1)
    E.frase(c, t, C["s06.d"] + 1.2, ps("e tirou do total", "i", 54, TINTA2), 1220, 950, passo=0.1)


# ---------------- regra ----------------
POS_A = [(380, 430), (640, 430), (900, 430), (1160, 430), (510, 570), (770, 570), (1030, 570)]


def b_regra(c, t, C, b):
    def universo():
        E.frase(c, t, C["s07.a"], [("evento", "i", 84), ("complementar", "g", 90, COR)], W / 2, 170, "center")
        E.foco(c, t, C["s07.b"], 0.5, lambda a: espaco(c, 160, 260, 1600, 500, a))
        E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: E.pilula(c, "universo = espaço amostral", W / 2, 260, 44, estilo="g", fundo=TINTA2, a=a))
        if t >= C["s07.c"] - 0.2:
            E.foco(c, t, C["s07.c"] - 0.2, 0.5, lambda a: bloco(c, 380 - 125, 1160 + 125, 500, 230, a))
            E.foco(c, t, C["s07.c"], 0.45, lambda a: E.pilula(c, "A: pelo menos 1 cara", 710, 705, 42, estilo="g", a=a))
        for i, (r, (x, y)) in enumerate(zip(PELO_MENOS, POS_A)):
            E.foco(c, t, C["s07.b"] + 0.5 + 0.06 * i, 0.4, lambda a, r=r, x=x, y=y: chip(c, x, y, " ".join(r), a, COR, 40))
        E.foco(c, t, C["s07.b"] + 0.95, 0.4, lambda a: chip(c, 1530, 500, "Co Co Co", a, TINTA2, 40, cheio=t >= C["s07.d"] + 0.3))
        if t >= C["s07.d"]:
            E.caixa_pontilhada(c, 1390, 420, 280, 160, ep(t, C["s07.d"], 0.4), TINTA2, ep(t, C["s07.d"], 0.4))
        E.foco(c, t, C["s07.d"] + 0.3, 0.45, lambda a: E.pilula(c, "Ā: nenhuma cara", 1530, 705, 42, estilo="g", fundo=TINTA2, a=a))
        # as duas chances somam 1
        y = 900
        linha(c, t, W / 2, y, 80, [("P(A) + P(Ā)", C["s08.a"]), ("=", C["s08.b"]), ((7, 8), C["s08.b"] + 0.2, COR), ("+", C["s08.b"] + 0.4),
                                   ((1, 8), C["s08.b"] + 0.6, TINTA2), ("=", C["s08.b"] + 1.0), ((8, 8), C["s08.b"] + 1.2), ("= 1", C["s08.b"] + 2.0),
                                   ("= 100%", C["s08.c"], CERTO)], "center")
    E.saida(c, t, C["s09"] - 0.1, universo)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"] + 0.1, ps("daí sai a regra", "i", 64, TINTA2), W / 2, 150, "center")
    y = 300
    xs, xf = linha(c, t, W / 2, y, 130, [("P(A)", C["s09.a"], COR), ("= 1 −", C["s09.a"] + 0.3), ("P(Ā)", C["s09.a"] + 0.6)], "center")
    wa, wb = E.larg("P(A)", "g", 130), E.larg("P(Ā)", "g", 130)
    nota(c, t, C["s09.b"], xs[0] + wa / 2, y + 140, "chance do evento A", 46, COR)
    if t >= C["s09.c"]:
        E.caixa_pontilhada(c, xs[2] - 20, y - 120, wb + 40, 200, ep(t, C["s09.c"], 0.4), TINTA2, ep(t, C["s09.c"], 0.4))
    nota(c, t, C["s09.c"] + 0.2, xs[2] + wb / 2, y + 140, "traço em cima: complementar", 46, TINTA2)
    if t < C["s10"]:
        return
    y = 640
    xs, xf = linha(c, t, 230, y, 100, [("1 −", C["s10.a"]), ((1, 8), C["s10.a"] + 0.2), ("=", C["s10.b"]), ((8, 8), C["s10.b"] + 0.3, COR),
                                        ("−", C["s10.b"] + 0.6), ((1, 8), C["s10.b"] + 0.8), ("=", C["s10.c"]), ((7, 8), C["s10.c"] + 0.2, COR)])
    igual_bola(c, t, C["s10.d"], xf + 70, y, "87,5%", r=125)
    # o inteiro em 8 pedaços: um sai
    bx, by, bw, bh = 480, 860, 960, 100
    sai = ep(t, C["s10.c"], 0.7)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.barra_fatias(c, bx, by, bw, bh, 8, 7 if t >= C["s10.c"] else 8, E.COR, a))
    if t >= C["s10.c"]:
        lp = bw / 8
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx + 7 * lp, by - 90 * sai, lp, bh), 8, 8), M.paint(E.COR, 1 - sai))
    nota(c, t, C["s10.b"] + 0.5, bx + bw / 2, by + bh + 70, "1 inteiro = 8 pedaços iguais", 46, TINTA2, "i")
    nota(c, t, C["s10.c"] + 0.4, bx + bw + 160, by + 68, "sobram 7", 52, COR)
    nota(c, t, C["s10.d"] + 1.2, xf + 263, 830, "quase certeza", 50, TINTA2, "i")


# ---------------- chute ----------------
LETRAS = "ABCDE"
CERTA = 2


def cartao(c, t, t0, x, y, nome, terr=None):
    """questão com 5 alternativas, só uma certa (a do meio); terr = instante em que as 4 erradas ficam vermelhas"""
    def f(a):
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 640, 200), 24, 24)
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(TINTA, a, stroke=4))
        E.escreve(c, nome, x + 30, y + 60, 44, "b", TINTA2, a)
    E.foco(c, t, t0, 0.45, f)
    for i, L in enumerate(LETRAS):
        cx, cy = x + 80 + i * 120, y + 130
        q = ep(t, terr, 0.4) if terr is not None else 0

        def letra(a, cx=cx, cy=cy, L=L, i=i, q=q):
            cor = CERTO if i == CERTA else ERRADO
            c.drawCircle(cx, cy, 40, M.paint(M.mix(BR, cor, 0.85 * q) if q > 0 else BR, a))
            c.drawCircle(cx, cy, 40, M.paint(M.mix(TINTA, cor, q), a, stroke=4))
            centro(c, L, cx, cy + 16, 44, "g", BR if q > 0.5 else TINTA, a)
        E.foco(c, t, t0 + 0.2 + 0.06 * i, 0.4, letra)


def b_chute(c, t, C, b):
    def montar():
        E.foco(c, t, C["s11.a"], 0.45, lambda a: E.pilula(c, "quando o nenhum tem muitos resultados", W / 2, 150, 44, estilo="g", fundo=TINTA2, a=a))
        cartao(c, t, C["s11.b"], 150, 260, "questão 1", C["s12.c"])
        cartao(c, t, C["s11.b"] + 0.5, 150, 520, "questão 2", C["s12.c"] + 0.3)
        E.frase(c, t, C["s11.c"], [("acertar", "i", 66), ("pelo", "i", 66), ("menos", "i", 66), ("uma?", "g", 74, COR)], 150, 840, passo=0.12)
        nota(c, t, C["s12.c"] + 0.6, 470, 960, "cada uma: 4 erradas", 50, ERRADO)
        nota(c, t, C["s12.a"] - 0.3, 1230, 250, "possíveis", 50, TINTA2, "i")
        casinhas(c, t, 1180, 380, [("questão 1", 5, C["s12.a"], C["s12.a"] + 0.3), ("questão 2", 5, C["s12.a"] + 0.2, C["s12.a"] + 0.5)], s=140)
        igual_bola(c, t, C["s12.a"] + 1.4, 1430, 380, "25", r=95)
        E.foco(c, t, C["s12.b"], 0.45, lambda a: E.pilula(c, "complementar: errar as duas", 1380, 610, 42, estilo="g", fundo=TINTA2, a=a))
        casinhas(c, t, 1180, 800, [("questão 1", 4, C["s12.d"], C["s12.d"] + 0.3, ERRADO), ("questão 2", 4, C["s12.d"] + 0.2, C["s12.d"] + 0.5, ERRADO)], s=140)
        igual_bola(c, t, C["s12.d"] + 1.4, 1430, 800, "16", r=95, cor=ERRADO)
    E.saida(c, t, C["s13"] - 0.1, montar)
    if t < C["s13"]:
        return
    linha(c, t, 200, 280, 96, [("P(errar as duas) =", C["s13.a"]), ((16, 25), C["s13.a"] + 0.3, ERRADO)])
    E.foco(c, t, C["s13.b"] - 0.3, 0.4, lambda a: E.escreve(c, "tire do inteiro:", 200, 540, 60, "i", TINTA2, a))
    E.formula_em(c, t, C["s13.b"], "25 − 16 = 9", 700, 545, 96, "g", TINTA)
    xs, xf = linha(c, t, 200, 780, 96, [("P(pelo menos 1) =", C["s13.c"]), ((9, 25), C["s13.c"] + 0.3, COR)])
    igual_bola(c, t, C["s13.d"], xf + 60, 780, "36%", r=110, cor=CERTO)


# ---------------- erro ----------------
DUAS = [r for r in RES if r.count("Ca") == 2]


def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"] + 0.1, [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], W / 2, 160, "center")
    E.frase(c, t, C["s14.a"], [("pelo", "i", 62), ("menos", "i", 62), ("uma", "g", 66, CERTO), ("≠", "g", 66), ("exatamente", "i", 62), ("uma", "g", 66, ERRADO)],
            W / 2, 270, "center", passo=0.1)
    xs = (330, 640, 950)
    tb = [lerp(C["s14.b"], C["s14.c"], k) for k in (0, 0.33, 0.66)]
    for i, (r, x) in enumerate(zip(EXATA, xs)):
        E.foco(c, t, tb[i], 0.4, lambda a, r=r, x=x: chip(c, x, 420, " ".join(r), a, COR, 44))
    nota(c, t, tb[0] + 0.3, 1200, 436, "1 cara", 48, TINTA2, "i")
    td = [C["s14.d"], C["s14.d"] + 0.3, C["s14.d"] + 0.6, lerp(C["s14.d"], C["s14.e"], 0.5)]
    for i, (r, x) in enumerate(zip(DUAS, xs)):
        E.foco(c, t, td[i], 0.4, lambda a, r=r, x=x: chip(c, x, 580, " ".join(r), a, COR, 44))
    nota(c, t, td[0] + 0.3, 1200, 596, "2 caras", 48, TINTA2, "i")
    E.foco(c, t, td[3], 0.4, lambda a: chip(c, 640, 740, "Ca Ca Ca", a, COR, 44))
    nota(c, t, td[3] + 0.3, 1200, 756, "3 caras", 48, TINTA2, "i")
    if t >= C["s14.e"]:
        E.foco(c, t, C["s14.e"], 0.5, lambda a: bloco(c, 330 - 140, 950 + 140, 580, 360, a, CERTO, 5))
    E.fr(c, t, C["s14.c"], 3, 8, 1560, 430, 120, ERRADO)
    if t >= C["s14.d"]:
        E.risco(c, 1470, 520, 1650, 330, t, C["s14.d"], largura=12)
    E.fr(c, t, C["s14.e"], 7, 8, 1560, 740, 120, CERTO)
    E.foco(c, t, C["s14.e"] + 0.3, 0.4, lambda a: E.selo(c, 1740, 740, 50, True, a))
    nota(c, t, lerp(C["s14.d"], C["s14.e"], 0.75), 640, 960, "pelo menos uma: 1, 2 ou 3 caras", 50, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def palavras():
        E.frase(c, t, C["s15"] + 0.1, [("viu", "i", 76, CLARO), ("na", "i", 76, CLARO), ("questão?", "i", 76, CLARO)], 480, 230, "center")
        for k, y, txt in (("s15.a", 400, "pelo menos um"), ("s15.b", 560, "no mínimo um"), ("s15.c", 720, "algum")):
            E.foco(c, t, C[k], 0.45, lambda a, y=y, txt=txt: E.pilula(c, txt, 480, y, 58, estilo="g", fundo=E.COR, a=a))
        if t >= C["s15.d"]:
            p = ep(t, C["s15.d"], 0.5)
            M.arrow(c, 860, 560, 1040, 560, BR, p, 6, 22, p)
        E.frase(c, t, C["s15.d"] + 0.3, [("calcule", "i", 72, CLARO), ("o", "i", 72, CLARO), ("nenhum", "g", 80, BR)], 1100, 450, passo=0.12)
        E.frase(c, t, C["s15.d"] + 0.9, [("e", "i", 72, CLARO), ("tire", "i", 72, CLARO), ("de", "i", 72, CLARO), ("1", "g", 80, BR)], 1100, 560, passo=0.12)
        E.foco(c, t, C["s15.d"] + 1.6, 0.5, lambda a: E.escreve(c, "1 − P(nenhum)", 1100, 730, 104, "g", BR, a))
    E.saida(c, t, C["s16"] - 0.1, palavras)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("nenhum:", "g", 70, BR), ("um", "i", 66, CLARO), ("grupo", "i", 66, CLARO), ("pequeno", "g", 70, BR)], W / 2, 220, "center", passo=0.12)
    E.frase(c, t, lerp(C["s16.a"], C["s16.b"], 0.5), [("pelo", "i", 66, CLARO), ("menos", "i", 66, CLARO), ("um:", "g", 70, BR), ("vários", "g", 70, BR),
                                                      ("casos", "i", 66, CLARO)], W / 2, 330, "center", passo=0.12)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "não compensa: o evento já é pequeno", W / 2, 500, 50, estilo="g", fundo=ERRADO, a=a))
    for i, x in enumerate((380, 560, 740)):
        E.foco(c, t, C["s16.c"] + 0.1 * i, 0.45, lambda a, x=x: E.moeda(c, x, 740, 80, "Ca", a, E.COR))
    nota(c, t, C["s16.c"] + 0.5, 560, 890, "3 caras: uma ponta só", 50, CLARO, "i")
    xs, xf = linha(c, t, 1060, 740, 120, [("P =", C["s16.d"], BR), ((1, 8), C["s16.d"] + 0.2, BR)])
    E.foco(c, t, C["s16.d"] + 0.6, 0.45, lambda a: E.escreve(c, "direto", xf + 50, 770, 72, "i", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.foco(c, t, C["s17.a"], 0.45, lambda a: branco(c, XE + 110, 400, 190, 3, a))
    E.foco(c, t, C["s17.a"] + 0.2, 0.45, lambda a: vermelho(c, XE + 350, 400, 190, 5, a))
    E.frase(c, t, C["s17.a"] + 0.5, [("2", "g", 68, COR), ("dados", "i", 64), ("comuns,", "i", 64), ("de", "i", 64), ("6", "g", 68, COR), ("faces", "i", 64)],
            XE, 620, passo=0.1)
    E.frase(c, t, C["s17.b"], [("chance", "i", 72), ("de", "i", 72), ("pelo", "i", 72), ("menos", "i", 72), ("um", "g", 80, COR), ("6?", "g", 80, COR)],
            XE, 790, passo=0.12)
    E.relogio(c, t, C["s18.a"], 1500, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cel = 112
    tx, ty = 250, 230
    pinta = {}
    td = C["s19.d"]
    for bb in range(1, 6):
        for vv in range(1, 6):
            pinta[(bb, vv)] = (td + 0.03 * (bb + vv), CINZA, None)
    ta = C["s20.a"]
    seis = [(6, v) for v in range(1, 7)] + [(b_, 6) for b_ in range(1, 6)]
    for i, k in enumerate(seis):
        pinta[k] = (ta + 0.05 * i, E.COR, None)
    tabela66(c, t, C["s19.a"], tx, ty, cel, pinta=pinta)
    X = 1060

    def contas():
        E.formula_em(c, t, C["s19.a"] + 0.3, "6 × 6 = 36", X, 300, 84, "g", TINTA)
        nota(c, t, C["s19.a"] + 0.8, X + 200, 380, "possíveis", 48, TINTA2, "i")
        E.foco(c, t, C["s19.b"], 0.45, lambda a: E.pilula(c, "complementar: nenhum 6", X + 330, 500, 46, estilo="g", fundo=TINTA2, a=a))
        nota(c, t, C["s19.c"], X + 330, 640, "cada dado: 5 faces sem 6", 50, TINTA2, "i")
        E.formula_em(c, t, C["s19.d"], "5 × 5 = 25", X, 790, 84, "g", TINTA2)
        nota(c, t, C["s19.d"] + 0.6, X + 200, 870, "nenhum 6", 48, TINTA2, "i")
    E.saida(c, t, C["s20"] - 0.1, contas)
    if t < C["s20"]:
        return
    E.formula_em(c, t, C["s20.a"], "36 − 25 = 11", X, 300, 84, "g", COR)
    nota(c, t, C["s20.a"] + 0.6, X + 250, 380, "têm pelo menos um 6", 48, COR, "i")
    xs, xf = linha(c, t, X, 520, 110, [("P =", C["s20.b"]), ((11, 36), C["s20.b"] + 0.2, CERTO)])
    E.foco(c, t, C["s20.b"] + 0.7, 0.4, lambda a: E.selo(c, xf + 80, 520, 46, True, a))
    nota(c, t, C["s20.b"] + 1.4, X + 330, 690, "um pouco menos que 1/3", 46, TINTA2, "i")
    E.fr(c, t, C["s20.c"], 35, 36, X + 100, 860, 96, ERRADO)
    if t >= C["s20.c"] + 0.8:
        E.risco(c, X + 10, 950, X + 190, 780, t, C["s20.c"] + 0.8, largura=11)
    nota(c, t, C["s20.c"] + 0.5, X + 470, 880, "nenhum 6 não é 1 caso", 46, ERRADO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s21.a"], 0.5, lambda a: fora(c, 220, 320, 620, 400, 470, 520, 150, a, ep(t, C["s21.a"] + 0.6, 0.6)))
        E.foco(c, t, C["s21.a"] + 1.0, 0.45, lambda a: E.escreve(c, "Ā", 700, 680, 80, "g", COR, a))
        linha(c, t, 1000, 520, 104, [("P(A) = 1 − P(Ā)", C["s21.a"] + 1.4)])
        E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "pelo menos um?  1 − P(nenhum)", W / 2, 880, 58, estilo="g", a=a))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22"] + 0.6, [("a", "i", 76), ("palavra", "i", 76), ("ou", "g", 96, COR), ("na", "i", 76), ("probabilidade", "g", 80, COR)], XE, 440)

    def carta(cx, cy, txt, cor, a, destaque=False):
        w = max(140, E.larg(txt, "g", 70) + 50)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - 98, w, 196), 16, 16)
        c.drawRRect(r, M.paint(BR, a))
        c.drawRRect(r, M.paint(E.COR if destaque else TINTA, a, stroke=7 if destaque else 4))
        centro(c, txt, cx, cy + 26, 70, "g", cor, a)
    E.foco(c, t, C["s22.a"], 0.45, lambda a: carta(XE + 80, 650, "K", TINTA, a))
    E.foco(c, t, C["s22.a"] + 0.3, 0.45, lambda a: E.escreve(c, "ou", XE + 190, 672, 60, "i", TINTA2, a))
    E.foco(c, t, C["s22.a"] + 0.6, 0.45, lambda a: carta(XE + 340, 650, "♥", VERM, a))
    E.foco(c, t, C["s22.b"], 0.45, lambda a: carta(XE + 580, 650, "K♥", VERM, a, True))
    nota(c, t, C["s22.b"] + 0.4, XE + 580, 820, "não conte 2 vezes", 44, COR)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 650, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1610, p), lerp(900, 675, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, moedas=b_moedas, regra=b_regra, chute=b_chute, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
