"""Visual — Estudativo · MAT-CNT-006: permutação com repetição e em círculo.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 005): casinhas(), igual_bola(), letra(), fila() e bloco().
Peças desta aula:
- ficha_ana(): os dois A de ANA pintados de vermelho e azul (fingindo que são diferentes); a cor some quando vira a mesma letra.
- mesa(): mesa redonda com cadeiras paradas e pessoas que giram juntas; giros() soma os giros animados; seta_giro() mostra o giro.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-006_permutacao_repeticao_circular.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ana", "arara", "erro", "mesa", "atalho", "questao", "fim"))
BR = "#FFFFFF"
F = math.factorial
from itertools import permutations
assert len(set(permutations("ANA"))) == 3 == F(3) // F(2) and len(set(permutations("ARARA"))) == 10 == F(5) // (F(3) * F(2))
assert F(5) // F(3) == 20 == 5 * 4 and F(5) // 5 == 24 == F(4) and len(set(permutations("BANANA"))) == 60 == F(6) // F(3) // 2
assert F(6) // F(3) == 120 == 6 * 5 * 4 and F(5) == 120 and F(6) == 720 and F(7) == 5040


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
    itens = [(nome embaixo, valor, t_caixa, t_valor[, cor do valor])]; valor None = caixa vazia; "?" sai em cinza;
    cor "fixo" = algarismo já decidido: caixa cheia, valor em branco, sem × ao lado.
    tx = instante de cada × (None = sem ×; senão, junto com a caixa da direita); tnomes = instante de cada nome.
    Devolve o centro de cada caixa."""
    n = len(itens)
    gap = s * 0.62 if gap is None else gap
    if size is None:
        vals = [len(str(it[1])) for it in itens if it[1] is not None]
        maior = max(vals) if vals else 1
        size = s * (0.56 if maior <= 1 else 0.46 if maior == 2 else 0.36)
    x0 = cx - (n * s + (n - 1) * gap) / 2
    xs = [x0 + s / 2 + i * (s + gap) for i in range(n)]
    borda = BR if escuro else TINTA
    fixo = [len(it) > 4 and it[4] == "fixo" for it in itens]
    for i, it in enumerate(itens):
        nome, val, tb, tv = it[:4]
        cor_v = it[4] if len(it) > 4 else (BR if escuro else (CINZA if val == "?" else COR))
        x = xs[i]

        def caixa(a, x=x, cheia=fixo[i]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s / 2, s, s), s * 0.12, s * 0.12)
            if escuro:
                c.drawRRect(r, M.paint(BR, (0.3 if cheia else 0.08) * a))
            else:
                sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.10 * a))
                sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
                c.save(); c.translate(0, 8); c.drawRRect(r, sh); c.restore()
                c.drawRRect(r, M.paint(TINTA if cheia else BR, a))
            c.drawRRect(r, M.paint(borda, a, stroke=5))
        E.foco(c, t, tb, 0.45, caixa)
        if nome:
            tn = tnomes[i] if tnomes else tb + 0.15
            E.foco(c, t, tn, 0.45, lambda a, x=x, nome=nome: centro(c, nome, x, y + s / 2 + max(52, s * 0.34), max(42, s * 0.27), "i",
                                                                  CLARO if escuro else TINTA2, a))
        if val is not None and tv is not None:
            cv = BR if cor_v == "fixo" else cor_v
            E.foco(c, t, tv, 0.45, lambda a, x=x, val=str(val), cv=cv: E.formula(c, val, x, y + size * 0.36, size, "g", cv, a, "center"))
        if i and not fixo[i] and not fixo[i - 1]:
            ti = tx[i - 1] if tx else tb
            if ti is not None:
                E.sinal(c, t, ti, "×", (xs[i - 1] + x) / 2, y, s * 0.42, BR if escuro else TINTA)
    return xs


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


# ---------------- peças desta aula ----------------
def letra(c, cx, cy, s, ch, a=1.0, fundo=BR, tinta=TINTA, borda=TINTA):
    """ficha de letra, como as de jogo de palavras"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.16, s * 0.16)
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda, a, stroke=4))
    centro(c, ch, cx, cy + s * 0.22, s * 0.6, "g", tinta, a)


def pessoa(c, cx, cy, h, cor, nome=None, a=1.0, cor_nome=None):
    """boneco simples: cabeça e tronco; (cx, cy) = centro do tronco"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2)
    c.drawRRect(r, M.paint(cor, a))
    if nome:
        centro(c, nome, cx, cy + h * 0.38 + 56, 48, "b", cor_nome or TINTA, a)


def fila(c, t, estados, cx, cy, passo, desenha, d=0.6, alto=None):
    """itens em fila que trocam de lugar. estados = [(instante, [ids na ordem])]; desenha(id, x, y).
    Quem muda de lugar desliza em arco (os que vão para a direita por cima, os outros por baixo). Devolve {id: x}"""
    cur, ant, q = estados[0][1], estados[0][1], 1.0
    for ti, ordem in estados:
        if t >= ti:
            ant, cur = cur, ordem
            q = ease_io(prog(t, ti, d))
    n = len(cur)
    alto = passo * 0.6 if alto is None else alto
    xs = {}
    for k in cur:
        i0, i1 = ant.index(k), cur.index(k)
        x = cx + (lerp(i0, i1, q) - (n - 1) / 2) * passo
        y = cy - math.sin(math.pi * q) * alto * (1 if i1 > i0 else -1 if i1 < i0 else 0)
        xs[k] = x
        desenha(k, x, y)
    return xs


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do bloco: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


VERMELHO, AZUL = "#D9483B", "#3E6FD9"
CORES_MESA = ("#E08A3C", "#8E5BD9", "#5B8DB8", "#55895A", "#C2463A", "#D8A53C")


def giros(t, tg, d=0.7):
    """quantos giros (com fração) já aconteceram: tg = instante de cada giro"""
    return sum(ease_io(prog(t, ti, d)) for ti in tg)


def mesa(c, t, cx, cy, R, n, giro=0.0, a=1.0, escuro=False, fixa=None, nomes="ABCDEF"):
    """mesa redonda com n cadeiras (paradas) e n pessoas (que giram juntas). giro = quantas cadeiras andaram, no sentido horário.
    fixa = índice da pessoa marcada como referência"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, R * 0.55, M.paint("#FFFFFF", (0.1 if escuro else 1.0) * a))
    c.drawCircle(cx, cy, R * 0.55, M.paint(BR if escuro else TINTA, a, stroke=5))
    for k in range(n):
        ang = math.radians(-90 + k * 360 / n)
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 52, y - 52, 104, 104), 22, 22)
        c.drawRRect(r, M.paint(CLARO if escuro else FIO, 0.5 * a if escuro else a))
    for k in range(n):
        ang = math.radians(-90 + (k + giro) * 360 / n)
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        c.drawCircle(x, y, 44, M.paint(CORES_MESA[k], a))
        centro(c, nomes[k], x, y + 18, 50, "g", BR, a)
        if fixa == k:
            c.drawCircle(x, y, 60, M.paint("#FFD500" if escuro else E.COR, a, stroke=8))


def seta_giro(c, t, t0, cx, cy, R, cor=None):
    """seta curva por fora da mesa: o giro de uma cadeira"""
    p = ease_io(prog(t, t0, 0.6))
    if p <= 0:
        return
    rr = R + 95
    path = skia.Path()
    path.addArc(skia.Rect.MakeXYWH(cx - rr, cy - rr, 2 * rr, 2 * rr), -80, 60 * p)
    c.drawPath(path, M.paint(cor or E.COR, 1, stroke=7))
    if p > 0.95:
        ang = math.radians(-20)
        x, y = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
        tx, ty = -math.sin(ang), math.cos(ang)
        nx, ny = math.cos(ang), math.sin(ang)
        tri = skia.Path()
        tri.moveTo(x + tx * 26, y + ty * 26); tri.lineTo(x - tx * 6 + nx * 18, y - ty * 6 + ny * 18); tri.lineTo(x - tx * 6 - nx * 18, y - ty * 6 - ny * 18); tri.close()
        c.drawPath(tri, M.paint(cor or E.COR))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        for i, ch in enumerate("ARARA"):
            E.foco(c, t, C["s01.a"] + 0.1 * i, 0.4, lambda a, i=i, ch=ch: letra(c, W / 2 + (i - 2) * 190, 300, 160, ch, a))
        E.frase(c, t, C["s01.a"] + 0.7, [("quantos", "i", 76), ("anagramas?", "g", 76, COR)], W / 2, 520, "center")
        E.formula_em(c, t, C["s01.b"], "5! = 120?", 760, 720, 120, "g", ERRADO if t >= C["s01.c"] else TINTA, "center")
        if t >= C["s01.c"]:
            E.risco(c, 500, 680, 1020, 680, t, C["s01.c"], largura=14)
            E.foco(c, t, C["s01.c"] + 0.1, 0.4, lambda a: E.centro(c, "não", 760, 850, 72, "g", ERRADO, a))
        E.foco(c, t, C["s01.d"] - 0.2, 0.4, lambda a: E.escreve(c, "só", 1200, 745, 84, "i", TINTA, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (E.bola(c, 1450, 700, 120, a=a), centro(c, "10", 1450, 700 + 32, 90, "g", BR, a)))
    E.saida(c, t, C["s02"] - 0.1, pergunta)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("letras", "g", 132)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("repetidas", "g", 132, COR)], XE, 630)
        E.frase(c, t, C["s02.b"], [("e", "i", 96), ("mesa", "g", 96), ("redonda", "g", 96, COR)], XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 210, "center")
    for k, x, titulo in (("s03.a", 220, "permutação"), ("s03.c", 1000, "cortar fatoriais")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 330, 700, 560, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 72, COR)], x + 350, 440, "center")
    for i, ch in enumerate("AMOR"):
        E.foco(c, t, C["s03.a"] + 0.3 + 0.1 * i, 0.4, lambda a, i=i, ch=ch: letra(c, 570 + (i - 1.5) * 110, 580, 90, ch, a))
    E.formula_em(c, t, C["s03.b"], "4! = 24", 570, 790, 96, "g", TINTA, "center")
    E.foco(c, t, C["s03.b"] + 0.4, 0.4, lambda a: E.centro(c, "todas diferentes, em fila", 570, 860, 42, "i", TINTA2, a))
    E.formula_em(c, t, C["s03.c"] + 0.3, "f{5!}{3!} = 5 × 4", 1350, 700, 96, "g", TINTA, "center")


# ---------------- ANA: o exemplo pequeno ----------------
PERMS = ((("Av", "N", "Aa"), ("Aa", "N", "Av")), (("Av", "Aa", "N"), ("Aa", "Av", "N")), (("N", "Av", "Aa"), ("N", "Aa", "Av")))
PALAVRAS = ("ANA", "AAN", "NAA")


def ficha_ana(c, k, x, y, s, a, cor_on):
    """letra de ANA; os dois A podem ter cor (vermelho e azul) que some em cor_on 1 → 0"""
    if k == "N":
        letra(c, x, y, s, "N", a)
        return
    cor = VERMELHO if k == "Av" else AZUL
    fundo = E.mix(BR, cor, cor_on) if cor_on > 0 else BR
    letra(c, x, y, s, "A", a, fundo, BR if cor_on > 0.5 else TINTA)


def b_ana(c, t, C, b):
    cor_on = ep(t, C["s04.b"], 0.5) * (1 - ep(t, C["s05.a"], 0.6))
    E.frase(c, t, C["s04"] + 0.2, [("comece", "i", 72), ("pequeno:", "i", 72)], XE, 190)
    for i, k in enumerate(("Av", "N", "Aa")):
        E.foco(c, t, C["s04.a"] + 0.1 * i, 0.4, lambda a, i=i, k=k: ficha_ana(c, k, 860 + i * 125, 170, 110, a, cor_on))
    if t >= C["s04.b"]:
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.escreve(c, "finja que são diferentes", 1300, 190, 46, "i", TINTA2, a) if t < C["s05.a"] else None)
    # as seis ordens
    xs, ys, s = (560, 1010), (400, 600, 800), 110
    for r, par in enumerate(PERMS):
        for col, perm in enumerate(par):
            t0 = C["s04.c"] + 0.15 * (r * 2 + col)
            destaque = (C["s05.b"] <= t < C["s06"] and r == 0)
            for j, k in enumerate(perm):
                x = xs[col] + (j - 1) * 125
                E.foco(c, t, t0, 0.4, lambda a, k=k, x=x, y=ys[r]: ficha_ana(c, k, x, y, s, a, cor_on))
            if destaque:
                E.foco(c, t, C["s05.b"] if col == 0 else C["s05.b"] + 0.6, 0.4, lambda a, col=col, r=r: E.caixa_pontilhada(
                    c, xs[col] - 200, ys[r] - 75, 400, 150, a, E.COR, a))
    E.foco(c, t, C["s04.c"], 0.5, lambda a: E.formula(c, "3! = 6", XE, 1000, 84, "g", TINTA, a))
    E.foco(c, t, C["s04.c"] + 0.3, 0.5, lambda a: E.escreve(c, "ordens", XE + 260, 1000, 56, "i", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "a mesma palavra", 785, ys[0] - 120, 44, estilo="b", a=a) if t < C["s06"] else None)
    # cada palavra contada duas vezes: chaves nas linhas
    if t >= C["s05.d"]:
        for r in range(3):
            p = ep(t, C["s05.d"] + 0.2 * r, 0.4)
            M.line(c, 1240, ys[r] - 60, 1240, ys[r] + 60, E.COR, p, 6)
            E.foco(c, t, C["s05.d"] + 0.2 * r, 0.4, lambda a, r=r: E.escreve(c, "2 vezes", 1270, ys[r] + 18, 50, "b", COR, a) if t < C["s06.b"] else None)
    for r, k in enumerate(("s06.b", "s06.c", "s06.d")):
        E.foco(c, t, C[k], 0.45, lambda a, r=r: E.escreve(c, PALAVRAS[r], 1270, ys[r] + 22, 72, "g", COR, a))
    E.formula_em(c, t, C["s06.a"], "6 ÷ 2 = 3", 1250, 1000, 84, "g", COR)


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s07"] + 0.1, [("a", "i", 96), ("regra", "g", 96, COR)], W / 2, 190, "center")
    E.passo(c, t, C["s07.a"], 1, "conte como se tudo fosse", "diferente: n!", 360)
    E.passo(c, t, C["s07.b"], 2, "divida pelo fatorial de", "cada repetição", 560)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "letra 3 vezes: ÷ 3!", 1150, 520, 60, "b", TINTA, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.escreve(c, "letra 2 vezes: ÷ 2!", 1150, 620, 60, "b", TINTA, a))
    # por que fatorial: os três A coloridos trocam de 3! jeitos
    t0 = C["s07.d"] + 2.0
    for i, cor in enumerate((VERMELHO, AZUL, "#2FA84F")):
        E.foco(c, t, t0 + 0.15 * i, 0.4, lambda a, i=i, cor=cor: letra(c, 420 + i * 130, 850, 110, "A", a, cor, BR))
    E.foco(c, t, t0 + 0.6, 0.5, lambda a: E.escreve(c, "trocam de 3! jeitos e dão a mesma palavra", 790, 870, 52, "i", TINTA2, a))


# ---------------- ARARA ----------------
def b_arara(c, t, C, b):
    for i, ch in enumerate("ARARA"):
        forte = (ch == "A" and t >= C["s08.a"]) or (ch == "R" and t >= C["s08.b"])
        cor = E.COR if ch == "A" else TINTA2
        E.foco(c, t, C["s08"] + 0.1 * i, 0.4, lambda a, i=i, ch=ch, forte=forte, cor=cor: letra(c, 420 + i * 140, 220, 120, ch, a,
                                                                                               cor if forte else BR, BR if forte else TINTA))
    E.foco(c, t, C["s08.a"] + 0.3, 0.4, lambda a: E.escreve(c, "A: 3 vezes", 1180, 205, 56, "b", COR, a))
    E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: E.escreve(c, "R: 2 vezes", 1180, 275, 56, "b", TINTA2, a))
    E.formula_em(c, t, C["s08.c"], "f{5!}{3! · 2!}", 420, 560, 130, "g", TINTA, "center")
    E.formula_em(c, t, C["s09.a"], "f{5!}{3!} = 5 × 4", 800, 560, 96, "g", TINTA)
    E.formula_em(c, t, C["s09.b"], "= 20", 800 + E.formula(None, "f{5!}{3!} = 5 × 4", 0, 0, 96, a=0) + 30, 560, 96, "g", COR)
    E.formula_em(c, t, C["s09.c"], "f{20}{2!} = f{20}{2}", 800, 800, 96, "g", TINTA)
    bx = igual_bola(c, t, C["s09.d"], 1290, 770, "10", r=105)
    E.foco(c, t, C["s09.d"] + 0.3, 0.5, lambda a: E.centro(c, "anagramas", bx, 960, 56, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s10.a"], ps("dividiu só por uma repetição", "i", 64, TINTA2), W / 2, 280, "center", passo=0.12)
    E.formula_em(c, t, C["s10.b"], "f{5!}{3!}", 400, 500, 120, "g", TINTA, "center")
    E.formula_em(c, t, C["s10.c"], "= 20", 520, 500, 120, "g", ERRADO)
    if t >= C["s10.c"] + 1.0:
        E.risco(c, 300, 470, 840, 470, t, C["s10.c"] + 1.0, largura=12)
    # os R trocam de lugar e a palavra não muda
    est = [(C["s10.d"], ["A1", "R1", "A2", "R2", "A3"]), (C["s10.d"] + 1.0, ["A1", "R2", "A2", "R1", "A3"])]

    def desenha(k, x, y):
        if k[0] == "R":
            letra(c, x, y, 120, "R", 1.0, VERMELHO if k == "R1" else AZUL, BR)
        else:
            letra(c, x, y, 120, "A", 1.0)
    if t >= C["s10.d"]:
        E.foco(c, t, C["s10.d"], 0.4, lambda a: fila(c, t, est, 1350, 470, 145, desenha, alto=110))
        E.foco(c, t, C["s10.d"] + 1.4, 0.5, lambda a: E.centro(c, "trocou os R: mesma palavra", 1350, 640, 52, "i", TINTA, a))
    E.frase(c, t, C["s10.e"], [("toda", "i", 84), ("letra", "i", 84), ("repetida", "g", 84, COR), ("divide", "g", 84, COR)], W / 2, 860, "center")
    E.foco(c, t, C["s10.e"] + 1.2, 0.5, lambda a: E.centro(c, "sem dividir pelo R, cada palavra aparece 2 vezes", W / 2, 960, 50, "i", TINTA2, a))


# ---------------- mesa redonda ----------------
MX, MY, MR = 620, 590, 300


def b_mesa(c, t, C, b):
    end = C["s12.end"]
    tg = [C["s12.a"]] + [lerp(C["s12.c"] + 0.8, end, k / 4) for k in range(4)]
    g = giros(t, tg)
    E.foco(c, t, C["s11.a"], 0.6, lambda a: mesa(c, t, MX, MY, MR, 5, g, a))
    E.frase(c, t, C["s11.a"], [("5", "g", 80, COR), ("pessoas,", "i", 80), ("mesa", "g", 80), ("redonda", "g", 80, COR)], W / 2, 150, "center")

    def vizinhos():
        E.frase(c, t, C["s11.b"], ps("o que importa:", "i", 64, TINTA2), 1100, 420)
        E.frase(c, t, C["s11.b"] + 0.5, [("quem", "i", 72), ("está", "i", 72), ("à", "i", 72), ("direita", "g", 72, COR)], 1100, 520)
        E.frase(c, t, C["s11.b"] + 1.2, [("e", "i", 72), ("à", "i", 72), ("esquerda", "g", 72, COR)], 1100, 610)
    E.saida(c, t, C["s12"] - 0.1, vizinhos)
    if C["s12.a"] <= t < C["s13"]:
        seta_giro(c, t, C["s12.a"], MX, MY, MR)
        E.frase(c, t, C["s12.a"], ps("todos andam 1 cadeira", "i", 64), 1100, 400)
        E.frase(c, t, C["s12.b"], [("mesmos", "g", 64), ("vizinhos", "g", 64, COR)], 1100, 500)
        E.frase(c, t, C["s12.c"], [("mesma", "g", 72), ("arrumação", "g", 72, COR)], 1100, 620)
        k = min(5, int(g + 0.001))
        if t >= C["s12.c"] + 0.8:
            E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: E.escreve(c, f"giro {max(k, 1)} de 5", 1100, 760, 60, "b", TINTA2, a))
        if g >= 4.99:
            E.foco(c, t, tg[-1] + 0.7, 0.4, lambda a: E.escreve(c, "todo mundo volta ao lugar", 1100, 850, 54, "i", COR, a))
    if t >= C["s13"]:
        E.formula_em(c, t, C["s13.a"], "em fila: 5! = 120", 1080, 420, 80, "g", TINTA)
        E.frase(c, t, C["s13.b"], ps("cada arrumação aparece", "i", 60, TINTA2), 1080, 560)
        E.frase(c, t, C["s13.b"] + 0.6, [("5", "g", 66, COR), ("vezes,", "i", 60, TINTA2), ("uma", "i", 60, TINTA2), ("por", "i", 60, TINTA2),
                                         ("giro", "i", 60, TINTA2)], 1080, 640)
        E.formula_em(c, t, C["s13.c"], "120 ÷ 5", 1080, 830, 96, "g", TINTA)
        igual_bola(c, t, C["s13.c"] + 0.4, 1460, 796, "24", r=100)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def fixa():
        E.frase(c, t, C["s14.a"], [("fixe", "g", 96, BR), ("uma", "i", 96, CLARO), ("pessoa", "g", 96, BR)], W / 2, 170, "center")
        E.foco(c, t, C["s14.a"] + 0.2, 0.5, lambda a: mesa(c, t, MX, MY, MR, 5, 0, a, escuro=True, fixa=0 if t >= C["s14.a"] + 0.6 else None))
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "a referência", MX, MY, 44, estilo="g", fundo=E.COR, a=a))
        E.frase(c, t, C["s14.c"] - 1.6, ps("as outras 4 fazem fila", "i", 64, CLARO), 1080, 450)
        E.formula_em(c, t, C["s14.c"], "4!", 1080, 640, 120, "g", BR)
        igual_bola(c, t, C["s14.c"] + 0.4, 1260, 600, "24", r=100, cor=E.COR, escuro=True)
        E.foco(c, t, C["s14.c"] + 1.2, 0.5, lambda a: E.escreve(c, "mesma resposta, sem dividir", 1080, 820, 52, "i", CLARO, a))
    E.saida(c, t, C["s15"] - 0.1, fixa)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("fixar uma pessoa elimina os giros", "i", 72, CLARO), W / 2, 190, "center", passo=0.12)
    E.frase(c, t, C["s15.b"], [("mesa", "g", 84, BR), ("redonda:", "g", 84, BR)], 520, 400, "center")
    E.formula_em(c, t, C["s15.b"] + 0.4, "(n − 1)!", 520, 540, 120, "g", "#FFD500", "center")
    E.foco(c, t, C["s15.b"] + 1.6, 0.5, lambda a: E.centro(c, "8 pessoas: 7!", 520, 660, 60, "b", CLARO, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "cadeiras numeradas", 1360, 400, 54, estilo="g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s15.c"] + 0.6, 0.5, lambda a: E.centro(c, "girar muda a arrumação", 1360, 520, 56, "i", CLARO, a))
    E.frase(c, t, C["s15.d"], [("conta", "i", 72, CLARO), ("de", "i", 72, CLARO), ("fila:", "i", 72, CLARO), ("n!", "g", 84, BR)], 1360, 660, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.foco(c, t, C["s16.a"] - 0.3, 0.5, lambda a: (E.bola(c, XE + 36, 330, 36, a=a), centro(c, "1", XE + 36, 346, 44, "g", BR, a)))
    for i, ch in enumerate("BANANA"):
        E.foco(c, t, C["s16.a"] + 0.08 * i, 0.4, lambda a, i=i, ch=ch: letra(c, XE + 170 + i * 130, 330, 110, ch, a))
    E.frase(c, t, C["s16.a"] + 0.6, [("quantos", "i", 72), ("anagramas?", "g", 72, COR)], XE + 110, 500)
    E.foco(c, t, C["s16.b"] - 0.3, 0.5, lambda a: (E.bola(c, XE + 36, 680, 36, a=a), centro(c, "2", XE + 36, 696, 44, "g", BR, a)))
    E.frase(c, t, C["s16.b"], [("6", "g", 72, COR), ("amigos", "i", 72), ("em", "i", 72), ("volta", "i", 72), ("da", "i", 72)], XE + 110, 700)
    E.frase(c, t, C["s16.b"] + 0.8, [("mesa", "g", 72), ("redonda?", "g", 72, COR)], XE + 110, 800)
    E.relogio(c, t, C["s17.a"], 1500, 520, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def banana():
        for i, ch in enumerate("BANANA"):
            cor = E.COR if ch == "A" else TINTA2 if ch == "N" else None
            E.foco(c, t, C["s18"] + 0.08 * i, 0.4, lambda a, i=i, ch=ch, cor=cor: letra(c, 360 + i * 130, 200, 110, ch, a,
                                                                                       cor if cor and t >= C["s18.a"] + 0.6 else BR,
                                                                                       BR if cor and t >= C["s18.a"] + 0.6 else TINTA))
        E.foco(c, t, C["s18.a"], 0.4, lambda a: E.escreve(c, "6 letras: A 3 vezes, N 2, B 1", 1180, 215, 48, "b", TINTA, a))
        E.formula_em(c, t, C["s18.b"], "f{6!}{3!} = 6 × 5 × 4", 300, 520, 100, "g", TINTA)
        E.formula_em(c, t, C["s18.c"], "= 120", 300 + E.formula(None, "f{6!}{3!} = 6 × 5 × 4", 0, 0, 100, a=0) + 30, 520, 100, "g", COR)
        E.formula_em(c, t, C["s18.d"], "120 ÷ 2!", 300, 780, 100, "g", TINTA)
        bx = igual_bola(c, t, C["s18.d"] + 0.4, 760, 745, "60", r=105, cor=CERTO)
        E.foco(c, t, C["s18.d"] + 0.7, 0.5, lambda a: E.escreve(c, "anagramas", bx + 130, 765, 56, "g", CERTO, a))
    E.saida(c, t, C["s19"] - 0.1, banana)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19"] + 0.2, 0.6, lambda a: mesa(c, t, MX, MY, 280, 6, 0, a, fixa=0 if t >= C["s19.a"] else None))
    E.frase(c, t, C["s19.a"], [("fixe", "g", 76), ("um", "i", 76), ("amigo", "i", 76)], 1080, 380)
    E.formula_em(c, t, C["s19.b"], "5!", 1080, 560, 120, "g", TINTA)
    igual_bola(c, t, C["s19.b"] + 0.4, 1240, 520, "120", r=105, cor=CERTO)
    E.foco(c, t, C["s19.b"] + 1.4, 0.5, lambda a: E.escreve(c, "em fila: 6! = 720", 1080, 760, 60, "b", TINTA2, a))
    E.foco(c, t, C["s19.b"] + 2.4, 0.5, lambda a: E.escreve(c, "6 vezes mais", 1080, 850, 56, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, l1, l2) in enumerate((("s20.a", "letra repetida?", "÷ fatorial da repetição"), ("s20.b", "mesa redonda?", "fixe uma: (n − 1)!"))):
            y = 430 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y + 10, 56, a=a), centro(c, str(i + 1), 300, y + 33, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72), 400, y - 10)
            E.formula_em(c, t, C[k] + 0.6, l2, 400, y + 95, 96, "g", COR)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], ps("até aqui, todo mundo entrava na fila", "i", 64, TINTA2), XE, 250, passo=0.12)
    E.frase(c, t, C["s21.b"] - 0.4, ps("próxima aula", "i", 84), XE, 380)
    E.frase(c, t, C["s21.b"], [("escolher", "g", 130, COR)], XE, 520)
    E.frase(c, t, C["s21.b"] + 0.3, [("só", "i", 120), ("alguns", "g", 130, COR)], XE, 660)
    E.frase(c, t, C["s21.b"] + 1.0, ps("o pódio: 3 entre 8", "i", 64, TINTA2), XE, 760)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.escreve(c, "a ordem muda?", XE, 850, 64, "g", TINTA, a))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ana=b_ana, regra=b_regra, arara=b_arara, erro=b_erro, mesa=b_mesa, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
