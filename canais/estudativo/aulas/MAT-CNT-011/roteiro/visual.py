"""Visual — Estudativo · MAT-CNT-011: probabilidade, favoráveis sobre possíveis.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 010): pílulas, igual_bola() com o resultado na esfera, bloco() em volta
de um grupo, fila() para itens que trocam de lugar em arco (MAT-CNT-005). Frações com E.fracao / E.fr / E.ponte do kit.
Peças desta aula:
- dado(): face de dado com as pintas; a cor das pintas marca o resultado favorável.
- espaco(): o retângulo do espaço amostral (Ω), com o evento como bloco dentro dele.
- saco(): saco de bolas coloridas; bolas() as bolas dentro, que acendem por cor.
- prob(): "P(...) =" com a fração de favoráveis sobre possíveis.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-011_probabilidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dado", "regra", "limites", "bolas", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, VERM, VERDE = "#3D7DD8", "#D94B3D", "#2FA84F"
PAR = [n for n in range(1, 7) if n % 2 == 0]
PRIMO = [n for n in range(1, 7) if n > 1 and all(n % d for d in range(2, n))]
assert PAR == [2, 4, 6] and Fr(3, 6) == Fr(1, 2) and Fr(1, 2) * 100 == 50
assert Fr(0, 6) == 0 and Fr(6, 6) == 1 and 3 + 5 + 2 == 10 and Fr(5, 10) == Fr(1, 2)
assert Fr(3, 10) * 100 == 30 and 3 * 10 == 30 and Fr(7, 20) * 100 == 35 and 7 * 5 == 35
assert PRIMO == [2, 3, 5] and 5 + 8 + 12 == 25 and Fr(8, 25).denominator == 25 and Fr(8, 25) * 100 == 32 and 8 * 4 == 32


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


def marca(c, t, t0, x, y, s, t1=None, cor=None):
    """caixa pontilhada em volta da casinha da vez (some em t1)"""
    def f():
        p = ep(t, t0, 0.4)
        m = s * 0.16
        E.caixa_pontilhada(c, x - s / 2 - m, y - s / 2 - m, s + 2 * m, s + 2 * m, p, cor, p)
    if t >= t0:
        E.saida(c, t, t1, f) if t1 is not None else f()


def regra(c, t, t0, x, y, txt, fundo=None, size=40, t1=None):
    """pílula com a restrição, centrada em (x, y)"""
    f = lambda: E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x, y, size, estilo="b", fundo=fundo or TINTA2, a=a))
    E.saida(c, t, t1, f) if t1 is not None else f()


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


# ---------------- peças da MAT-CNT-005 e da MAT-CNT-004 ----------------
def pessoa(c, cx, cy, h, cor, nome=None, a=1.0, cor_nome=None, nome_y=None):
    """boneco simples: cabeça e tronco; (cx, cy) = centro do tronco. nome_y = linha de base do nome (senão, embaixo)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2)
    c.drawRRect(r, M.paint(cor, a))
    if nome:
        centro(c, nome, cx, nome_y if nome_y is not None else cy + h * 0.38 + 56, max(40, h * 0.24), "b", cor_nome or TINTA, a)


def bloco(c, x0, x1, cy, h, a=1.0, cor=None, largura=7):
    """contorno do grupo: quem está dentro anda junto"""
    if a <= 0:
        return
    m = 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 - m, cy - h / 2 - m, x1 + m, cy + h / 2 + m), 34, 34)
    c.drawRRect(r, M.paint(cor or E.COR, 0.08 * a))
    c.drawRRect(r, M.paint(cor or E.COR, a, stroke=largura))


def fracao_corte(c, t, t0, cx, cy, size, cima, baixo, tcima=None, tc=None, cortar=(), cor=None, escuro=False):
    """fração de fatoriais: cima = lista de partes ("8", "×", "7", "×", "6!"), baixo = texto de baixo.
    tcima = instante de cada parte de cima (senão, junto); tc = instante do corte; cortar = índices de cima que somem com o de baixo."""
    tinta = cor or (BR if escuro else TINTA)
    esp = size * 0.22
    ws = [E.larg(p, "g", size) for p in cima]
    wc = sum(ws) + esp * (len(cima) - 1)
    wb = E.larg(baixo, "g", size)
    w = max(wc, wb) + size * 0.3
    y_cima, y_baixo = cy - size * 0.22, cy + size * 0.95
    E.foco(c, t, t0, 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.05, w, size * 0.09), 4, 4),
                                                 M.paint(tinta, a)))
    x = cx - wc / 2
    pos = []
    for i, (p, wp) in enumerate(zip(cima, ws)):
        ti = tcima[i] if tcima else t0
        E.foco(c, t, ti, 0.45, lambda a, p=p, x=x: E.escreve(c, p, x, y_cima, size, "g", tinta, a))
        pos.append((x, wp))
        x += wp + esp
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, baixo, cx - wb / 2, y_baixo, size, "g", tinta, a))
    if tc is not None and t >= tc:
        risca = E.COR if not escuro else CLARO
        for i in cortar:
            xx, wp = pos[i]
            E.risco(c, xx - 8, y_cima + 8, xx + wp + 8, y_cima - size * 0.78, t, tc, risca, size * 0.09)
        E.risco(c, cx - wb / 2 - 8, y_baixo + 8, cx + wb / 2 + 8, y_baixo - size * 0.78, t, tc + 0.2, risca, size * 0.09)
    return w



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


# ---------------- peças desta aula ----------------
PINTAS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
          5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, a=1.0, cor=None, fundo=BR, borda=None, escuro=False):
    """face de dado com as pintas; cor = cor das pintas (TINTA por padrão)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2)
    if not escuro:
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
        c.save(); c.translate(0, 6); c.drawRRect(r, sh); c.restore()
    c.drawRRect(r, M.paint(fundo, a))
    c.drawRRect(r, M.paint(borda or TINTA, a, stroke=max(3, s * 0.035)))
    k = s * 0.27
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * k, cy + dy * k, s * 0.085, M.paint(cor or TINTA, a))


def espaco(c, x, y, w, h, a=1.0, rotulo="Ω", cor=None):
    """retângulo do espaço amostral, com o nome no canto"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30)
    c.drawRRect(r, M.paint(BR, 0.55 * a))
    c.drawRRect(r, M.paint(cor or TINTA2, a, stroke=5))
    E.escreve(c, rotulo, x + 26, y + 70, 60, "g", cor or TINTA2, a)


def saco(c, cx, cy, w, h, a=1.0):
    """saco de pano visto de frente, com a boca amarrada; (cx, cy) = centro do corpo"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - w * 0.22, cy - h * 0.5)
    p.cubicTo(cx - w * 0.62, cy - h * 0.3, cx - w * 0.58, cy + h * 0.5, cx, cy + h * 0.5)
    p.cubicTo(cx + w * 0.58, cy + h * 0.5, cx + w * 0.62, cy - h * 0.3, cx + w * 0.22, cy - h * 0.5)
    p.close()
    c.drawPath(p, M.paint("#E9DCC4", a))
    c.drawPath(p, M.paint("#8C7A5B", a, stroke=6))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w * 0.26, cy - h * 0.56, w * 0.52, h * 0.08), 12, 12), M.paint("#8C7A5B", a))


def bolas(c, t, cx, cy, grupos, r=34, apaga=None):
    """bolas dentro do saco. grupos = [(cor, n, t0)], na ordem; apaga = função cor → alfa (0..1). Devolve as posições"""
    pos = [(-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), (-1.5, 0), (-0.5, 0), (0.5, 0), (1.5, 0), (-1, 1), (0, 1), (1, 1)]
    k = 0
    for cor, n, t0 in grupos:
        for j in range(n):
            px, py = pos[k]
            x, y = cx + px * r * 2.3, cy + py * r * 2.1
            al = apaga(cor) if apaga else 1.0
            E.foco(c, t, t0 + 0.08 * j, 0.4, lambda a, x=x, y=y, cor=cor, al=al: E.bola(c, x, y, r, cor, a * al))
            k += 1


def prob(c, t, t0, x, y, nome, n, d, size=96, cor=None, tf=None):
    """'P(nome) =' com a fração n/d à direita; y = linha da barra. Devolve o x do fim da fração"""
    txt = f"P({nome}) =" if nome else "="
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, txt, x, y + size * 0.34, size, "g", TINTA, a))
    xf = x + E.larg(txt, "g", size) + size * 0.25
    lw = max(E.larg(str(n), "g", size), E.larg(str(d), "g", size)) + size * 0.2
    E.fr(c, t, t0 if tf is None else tf, n, d, xf + lw / 2, y, size, cor)
    return xf + lw


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        giro = 0 if t >= C["s01.b"] else int((t - C["s01.a"]) * 6) % 6
        face = 4 if t >= C["s01.b"] else (giro + 1)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: dado(c, 420, 400, 260, face, a, COR if t >= C["s01.b"] else TINTA))
        E.frase(c, t, C["s01.a"] + 0.3, [("você", "i", 80), ("joga", "i", 80), ("um", "i", 80), ("dado", "g", 84)], 680, 330)
        E.frase(c, t, C["s01.b"], [("chance", "i", 80), ("de", "i", 80), ("sair", "i", 80), ("par?", "g", 88, COR)], 680, 470)
        y = 820
        E.fr(c, t, C["s01.c"], 3, 6, 520, y, 120, COR)
        E.sinal(c, t, C["s01.d"] - 0.1, "=", 720, y, 100)
        E.fr(c, t, C["s01.d"], 1, 2, 900, y, 120, COR)
        E.sinal(c, t, C["s01.e"] - 0.1, "=", 1090, y, 100)
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.escreve(c, "50%", 1170, y + 44, 140, "g", COR, a))
        E.foco(c, t, C["s01.e"] + 0.6, 0.5, lambda a: E.pilula(c, "as três estão certas", 900, 1010, 48, estilo="g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 110), ("chance", "g", 130, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.2, [("de", "i", 110), ("um", "i", 110), ("resultado", "g", 120)], XE, 630)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 470, 84, "g", BR, a),
                                                      E.escreve(c, "para %", 1330, 580, 96, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 110, "conjunto"), ("s03.c", 680, "simplificar"), ("s03.d", 1250, "porcentagem")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 560, 600, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 60, COR)], x + 280, 390, "center")
    E.foco(c, t, C["s03.b"] + 0.4, 0.5, lambda a: E.centro(c, "{1, 2, 3}", 390, 640, 84, "g", TINTA, a))
    E.foco(c, t, C["s03.b"] + 0.8, 0.4, lambda a: E.centro(c, "entre chaves", 390, 790, 46, "i", TINTA2, a))
    E.fr(c, t, C["s03.c"] + 0.3, 3, 6, 860, 600, 90)
    E.sinal(c, t, C["s03.c"] + 0.6, "=", 960, 600, 80)
    E.fr(c, t, C["s03.c"] + 0.8, 1, 2, 1060, 600, 90, COR)
    E.foco(c, t, C["s03.c"] + 1.0, 0.4, lambda a: E.centro(c, "÷ 3 em cima e embaixo", 960, 790, 42, "i", TINTA2, a))
    E.foco(c, t, C["s03.d"] + 0.3, 0.5, lambda a: E.escreve(c, "50%", 1290, 632, 84, "g", COR, a))
    E.sinal(c, t, C["s03.d"] + 0.6, "=", 1540, 600, 80)
    E.fr(c, t, C["s03.d"] + 0.8, 50, 100, 1680, 600, 80)
    E.foco(c, t, C["s03.d"] + 1.2, 0.4, lambda a: E.centro(c, "100 embaixo", 1530, 790, 46, "i", TINTA2, a))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.7), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- espaço amostral e evento ----------------
def b_dado(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("tudo", "g", 76, COR), ("o", "i", 72), ("que", "i", 72), ("pode", "i", 72), ("acontecer", "i", 72)], W / 2, 170, "center")
    y, s, passo_ = 470, 150, 205
    tb = [C["s04.b"] + 0.56 * i for i in range(6)]
    est = [(C["s04"], [1, 2, 3, 4, 5, 6]), (C["s05.b"] + 1.4, [1, 3, 5, 2, 4, 6])]
    par = t >= C["s05.b"]

    def desenha(k, x, yy):
        cor = COR if (par and k % 2 == 0) else TINTA
        E.foco(c, t, tb[k - 1], 0.4, lambda a: dado(c, x, yy, s, k, a, cor))
    # o espaço amostral (embaixo dos dados)
    x0, x1 = W / 2 - 2.5 * passo_ - s / 2 - 50, W / 2 + 2.5 * passo_ + s / 2 + 50
    E.foco(c, t, C["s04.c"], 0.5, lambda a: espaco(c, x0, y - 210, x1 - x0, 380, a))
    xs = fila(c, t, est, W / 2, y, passo_, desenha, d=0.9, alto=120)
    E.foco(c, t, C["s04.c"] + 0.3, 0.5, lambda a: E.pilula(c, "espaço amostral", W / 2, y - 210, 46, estilo="g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s04.c"] + 0.8, 0.5, lambda a: E.centro(c, "Ω = {1, 2, 3, 4, 5, 6}", W / 2, 790, 72, "g", TINTA, a) if t < C["s05.c"] else None)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "6 elementos", W / 2, 900, 54, estilo="g", a=a) if t < C["s05"] + 0.2 else None)
    # o evento
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.centro(c, "o que você quer: número par", W / 2, 900, 56, "i", COR, a) if t >= C["s05"] + 0.2 else None)
    if t >= C["s05.c"] - 0.3:
        e0, e1 = W / 2 + 0.5 * passo_ - s / 2 - 10, W / 2 + 2.5 * passo_ + s / 2 + 10
        E.foco(c, t, C["s05.c"] - 0.3, 0.5, lambda a: bloco(c, e0, e1, y, s + 10, a))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "evento", (e0 + e1) / 2, y + s / 2 + 70, 44, estilo="g", a=a))
        E.foco(c, t, C["s05.c"] + 0.3, 0.5, lambda a: E.centro(c, "E = {2, 4, 6}", W / 2, 790, 72, "g", COR, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.centro(c, "o evento está contido no espaço amostral: é um pedaço dele", W / 2, 990, 46, "b", TINTA2, a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    def fracao():
        E.frase(c, t, C["s06.a"], [("probabilidade", "g", 80, COR), ("é", "i", 76), ("uma", "i", 76), ("fração", "g", 80)], W / 2, 180, "center")
        y = 460
        E.foco(c, t, C["s06.a"] + 0.6, 0.45, lambda a: E.escreve(c, "P =", 330, y + 40, 120, "g", TINTA, a))
        E.foco(c, t, C["s06.b"], 0.45, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(590, y - 6, 640, 12), 6, 6), M.paint(TINTA, a)))
        E.foco(c, t, C["s06.b"], 0.45, lambda a: E.centro(c, "favoráveis", 910, y - 40, 96, "g", CERTO, a))
        E.foco(c, t, C["s06.c"], 0.45, lambda a: E.centro(c, "possíveis", 910, y + 120, 96, "g", TINTA, a))
        E.foco(c, t, C["s06.b"] + 0.5, 0.4, lambda a: E.escreve(c, "quantos servem", 1290, y - 60, 50, "i", CERTO, a))
        E.foco(c, t, C["s06.c"] + 0.5, 0.4, lambda a: E.escreve(c, "quantos podem acontecer", 1290, y + 100, 50, "i", TINTA2, a))
        for i in range(6):
            n = i + 1
            E.foco(c, t, C["s06.d"] + 0.05 * i, 0.4, lambda a, n=n, i=i: dado(c, 330 + i * 110, 820, 90, n, a, COR if n % 2 == 0 else TINTA))
        prob(c, t, C["s06.d"] + 0.5, 1050, 820, "par", 3, 6, size=96, cor=COR)
    E.saida(c, t, C["s07"] - 0.1, fracao)
    if C["s07"] <= t < C["s08"] + 0.5:
        def simplifica():
            E.frase(c, t, C["s07"] + 0.1, ps("três respostas, a mesma chance", "i", 72), W / 2, 200, "center", passo=0.12)
            y = 560
            E.fr(c, t, C["s07.a"], 3, 6, 360, y, 130, COR)
            E.pontes(c, t, 450, 650, y, 130, "÷ 3", C["s07.a"] + 0.6, C["s07.a"] + 1.0, size=40)
            E.fr(c, t, C["s07.b"], 1, 2, 740, y, 130, COR)
            E.sinal(c, t, C["s07.c"] - 0.2, "=", 880, y, 110)
            E.fr(c, t, C["s07.c"], 50, 100, 1060, y, 120)
            igual_bola(c, t, C["s07.d"], 1250, y, "50%", r=120)
            E.foco(c, t, C["s07.d"] + 1.6, 0.5, lambda a: E.centro(c, "metade dos resultados serve", W / 2, 880, 60, "i", TINTA2, a))
        E.saida(c, t, C["s08"] - 0.1, simplifica)
    if t < C["s08"]:
        return
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.pilula(c, "só vale se todos têm a mesma chance", W / 2, 200, 54, estilo="g", a=a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: (dado(c, 560, 540, 220, 5, a), E.selo(c, 690, 410, 50, True, a)))
    E.foco(c, t, C["s08.b"] + 0.3, 0.5, lambda a: E.centro(c, "dado honesto", 560, 760, 60, "g", CERTO, a))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: (dado(c, 1360, 540, 220, 6, a, ERRADO), E.selo(c, 1490, 410, 50, False, a)))
    E.foco(c, t, C["s08.c"] + 0.3, 0.5, lambda a: E.centro(c, "dado viciado: cai mais no 6", 1360, 760, 56, "g", ERRADO, a))
    E.foco(c, t, C["s08.c"] + 1.4, 0.5, lambda a: E.centro(c, "a conta não vale", 1360, 850, 50, "i", ERRADO, a))


# ---------------- limites ----------------
def b_limites(c, t, C, b):
    E.frase(c, t, C["s09"] + 0.1, [("a", "i", 76), ("chance", "i", 76), ("vai", "i", 76), ("de", "i", 76), ("0", "g", 84, COR), ("a", "i", 76), ("1", "g", 84, COR)],
            W / 2, 170, "center")
    yr = 380
    vx = E.reta(c, t, C["s09.a"], 360, 1560, yr, 0, 1, [0, 0.5, 1], fmt=lambda v: {0: "0", 0.5: "½", 1: "1"}[v])
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "impossível", vx(0), yr - 90, 44, estilo="g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "certo", vx(1), yr - 90, 44, estilo="g", fundo=CERTO, a=a))
    # sair 7
    E.foco(c, t, C["s09.a"] + 1.2, 0.5, lambda a: E.escreve(c, "sair 7:", 240, 650, 64, "i", TINTA, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.escreve(c, "E = { }", 480, 650, 72, "g", TINTA2, a))
    E.foco(c, t, C["s09.b"] + 0.6, 0.4, lambda a: E.escreve(c, "vazio", 520, 720, 44, "i", TINTA2, a))
    E.fr(c, t, C["s09.c"], 0, 6, 860, 625, 90)
    E.foco(c, t, C["s09.c"] + 0.5, 0.45, lambda a: E.escreve(c, "= 0", 930, 655, 90, "g", ERRADO, a))
    # sair de 1 a 6
    E.foco(c, t, C["s10"] + 0.1, 0.5, lambda a: E.escreve(c, "de 1 a 6:", 240, 880, 64, "i", TINTA, a))
    E.fr(c, t, C["s10.a"], 6, 6, 860, 855, 90)
    E.foco(c, t, C["s10.a"] + 0.5, 0.45, lambda a: E.escreve(c, "= 1", 930, 885, 90, "g", CERTO, a))
    E.foco(c, t, C["s10.b"], 0.45, lambda a: E.escreve(c, "= 100%", 1130, 885, 90, "g", CERTO, a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "passou de 1? tem erro na conta", W / 2, 1010, 44, estilo="g", fundo=ERRADO, a=a))


# ---------------- saco de bolas ----------------
def b_bolas(c, t, C, b):
    SX, SY = 560, 560
    E.foco(c, t, C["s11"] + 0.1, 0.5, lambda a: saco(c, SX, SY, 620, 560, a))
    foco_cor = None
    if C["s12.a"] <= t < C["s12.b"]:
        foco_cor = AZUL
    elif t >= C["s12.b"]:
        foco_cor = VERM
    apaga = (lambda cor: 1.0 if cor == foco_cor else 0.3) if foco_cor else None
    bolas(c, t, SX, SY + 20, [(AZUL, 3, C["s11.a"]), (VERM, 5, C["s11.b"]), (VERDE, 2, C["s11.c"])], r=44, apaga=apaga)

    def lista():
        for i, (k, n, nome, cor) in enumerate((("s11.a", 3, "azuis", AZUL), ("s11.b", 5, "vermelhas", VERM), ("s11.c", 2, "verdes", VERDE))):
            y = 360 + i * 110
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, y=y, n=n, nome=nome, cor=cor: (E.escreve(c, str(n), 1050, y, 84, "g", cor, a),
                                                                                E.escreve(c, nome, 1130, y, 60, "i", TINTA, a)))
        E.formula_em(c, t, C["s11.d"], "3 + 5 + 2 = 10", 1050, 720, 76, "g", TINTA)
        E.foco(c, t, C["s11.d"] + 1.0, 0.4, lambda a: E.escreve(c, "possíveis", 1100, 820, 56, "i", TINTA2, a))
    E.saida(c, t, C["s12"] - 0.1, lista)
    if t < C["s12"]:
        return
    prob(c, t, C["s12.a"], 960, 420, "azul", 3, 10, size=76, cor=AZUL)
    xf = prob(c, t, C["s12.b"], 960, 720, "vermelha", 5, 10, size=76, cor=VERM)
    E.sinal(c, t, C["s12.c"] - 0.1, "=", xf + 60, 720, 76)
    E.fr(c, t, C["s12.c"], 1, 2, xf + 150, 720, 76, VERM)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"] + 0.1, [("cuidado", "g", 96, ERRADO), ("com", "i", 90), ("isto", "i", 90)], W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], ps("trocar o de baixo", "i", 64, TINTA2), W / 2, 270, "center")
    y = 450
    for i in range(10):
        cor = AZUL if i < 3 else (VERM if i < 8 else VERDE)
        x = 360 + i * 120 + (80 if i >= 3 and t >= C["s13.b"] and t < C["s13.d"] else 0)
        E.foco(c, t, C["s13.a"] + 0.05 * i, 0.4, lambda a, x=x, cor=cor: E.bola(c, x, y, 44, cor, a))
    if C["s13.b"] <= t < C["s13.d"] + 0.4:
        E.saida(c, t, C["s13.d"], lambda: E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: (E.centro(c, "3 azuis", 480, y + 110, 50, "b", AZUL, a),
                                                                                      E.centro(c, "7 não azuis", 1150, y + 110, 50, "b", TINTA2, a))))
    if t >= C["s13.d"]:
        E.foco(c, t, C["s13.d"], 0.5, lambda a: bloco(c, 360 - 50, 360 + 9 * 120 + 50, y, 100, a))
        E.foco(c, t, C["s13.d"] + 0.3, 0.4, lambda a: E.centro(c, "embaixo, o total: 10", 360 + 4.5 * 120, y + 130, 52, "b", COR, a))
    E.fr(c, t, C["s13.c"], 3, 7, 620, 790, 120, ERRADO)
    if t >= C["s13.d"]:
        E.risco(c, 540, 860, 700, 720, t, C["s13.d"], largura=12)
    E.fr(c, t, C["s13.e"], 3, 10, 1200, 790, 120, CERTO)
    E.foco(c, t, C["s13.e"] + 0.4, 0.5, lambda a: E.selo(c, 1400, 790, 50, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def cem():
        E.frase(c, t, C["s14.a"], [("leve", "i", 84, CLARO), ("o", "i", 84, CLARO), ("de", "i", 84, CLARO), ("baixo", "g", 90, BR), ("até", "i", 84, CLARO),
                                   ("100", "g", 96, BR)], W / 2, 200, "center", passo=0.12)
        for y, (n, d, k, nn, dd, tb, tc, te, pct) in ((470, (3, 10, 10, 30, 100, "s14.b", "s14.c", None, "30%")),
                                                      (820, (7, 20, 5, 35, 100, "s14.d", "s14.e", None, "35%"))):
            E.fr(c, t, C[tb], n, d, 420, y, 110, BR)
            E.pontes(c, t, 520, 760, y, 110, f"× {k}", C[tb] + 0.5, C[tb] + 0.9, cor=E.COR, size=40)
            E.fr(c, t, C[tc], nn, dd, 900, y, 110, BR)
            igual_bola(c, t, C[tc] + 0.5, 1080, y, pct, r=95, cor=E.COR, escuro=True)
    E.saida(c, t, C["s15"] - 0.1, cem)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("porcentagem = fração com 100 embaixo", "i", 68, BR), W / 2, 200, "center", passo=0.1)
    E.frase(c, t, C["s15.a"] + 2.6, ps("× o mesmo número em cima e embaixo: a fração não muda", "i", 50, CLARO), W / 2, 300, "center", passo=0.08)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.pilula(c, "não compensa: o de baixo não chega em 100", W / 2, 470, 50, estilo="g", fundo=ERRADO, a=a))
    E.fr(c, t, C["s15.b"] + 1.6, 1, 3, W / 2, 640, 110, BR)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.escreve(c, "1 ÷ 3", 520, 930, 96, "g", BR, a))
    E.foco(c, t, C["s15.c"] + 1.6, 0.5, lambda a: E.escreve(c, "ou deixe em fração", 1000, 925, 64, "i", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, C["s16.a"], [("dado", "i", 68), ("honesto:", "i", 68), ("chance", "i", 68), ("de", "i", 68), ("um", "i", 68), ("primo?", "g", 76, COR)],
            XE, 350, passo=0.12)
    for i, (n, nome, cor) in enumerate(((5, "morango", "#E86A92"), (8, "coco", "#B9A27A"), (12, "chocolate", "#6B4428"))):
        y = 500 + i * 95
        E.foco(c, t, C["s16.b"] + 0.6 * i, 0.4, lambda a, y=y, n=n, nome=nome, cor=cor: (E.bola(c, XE + 30, y - 22, 30, cor, a),
                                                                                     E.escreve(c, f"{n} de {nome}", XE + 90, y, 60, "b", TINTA, a)))
    E.frase(c, t, C["s16.c"], [("chance", "i", 68), ("de", "i", 68), ("pegar", "i", 68), ("um", "i", 68), ("de", "i", 68), ("coco?", "g", 76, COR)],
            XE, 860, passo=0.12)
    E.foco(c, t, C["s16.c"] + 2.4, 0.5, lambda a: E.pilula(c, "fração e porcentagem", XE + 260, 980, 44, estilo="b", fundo=TINTA2, a=a))
    E.relogio(c, t, C["s17.a"], 1500, 560, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def primo():
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.pilula(c, "primo: exatamente 2 divisores, o 1 e ele mesmo", W / 2, 180, 46, estilo="b", fundo=TINTA2, a=a))
        tb = {2: C["s18.b"], 3: C["s18.b"] + 0.56, 5: C["s18.b"] + 1.12}
        for i in range(6):
            n = i + 1
            cor = COR if (n in tb and t >= tb[n]) else TINTA
            E.foco(c, t, C["s18.b"] - 0.6 + 0.05 * i, 0.4, lambda a, n=n, i=i, cor=cor: dado(c, 460 + i * 200, 420, 150, n, a, cor))
        E.foco(c, t, C["s18.b"] + 1.6, 0.4, lambda a: E.centro(c, "1 não é primo", 460, 560, 44, "b", ERRADO, a))
        y = 790
        prob(c, t, C["s18.c"], 300, y, "primo", 3, 6, size=110, cor=COR)
        E.sinal(c, t, C["s18.d"] - 0.1, "=", 1040, y, 100)
        E.fr(c, t, C["s18.d"], 1, 2, 1170, y, 120, COR)
        igual_bola(c, t, C["s18.e"], 1290, y, "50%", r=100, cor=CERTO)
    E.saida(c, t, C["s19"] - 0.1, primo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.1, [("caixa", "i", 72), ("de", "i", 72), ("bombons", "g", 76)], W / 2, 180, "center")
    E.formula_em(c, t, C["s19.a"], "possíveis: 5 + 8 + 12 = 25", 260, 340, 72, "g", TINTA)
    E.formula_em(c, t, C["s19.b"], "favoráveis: 8", 260, 460, 72, "g", CERTO)
    y = 760
    prob(c, t, C["s19.c"], 260, y, "coco", 8, 25, size=110, cor=COR)
    E.foco(c, t, C["s19.c"] + 0.8, 0.4, lambda a: E.centro(c, "não simplifica", 760, y + 190, 44, "i", TINTA2, a))
    E.pontes(c, t, 960, 1130, y, 110, "× 4", C["s19.d"] - 0.6, C["s19.d"] - 0.3, size=40)
    E.fr(c, t, C["s19.d"], 32, 100, 1280, y, 110)
    igual_bola(c, t, C["s19.d"] + 0.6, 1430, y, "32%", r=100, cor=CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.escreve(c, "P =", 420, 520, 120, "g", TINTA, a))
        E.fr(c, t, C["s20.a"] + 0.3, "favoráveis", "possíveis", 980, 480, 96, COR)
        E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "todos os resultados com a mesma chance", W / 2, 820, 54, estilo="g", fundo=TINTA2, a=a))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21"] + 0.6, [("probabilidade", "g", 80, COR), ("com", "i", 72), ("contagem", "g", 80, COR)], XE, 440)
    E.foco(c, t, C["s21.a"], 0.5, lambda a: (dado(c, XE + 60, 600, 100, 3, a), dado(c, XE + 180, 600, 100, 4, a)))
    E.frase(c, t, C["s21.a"] + 0.3, [("soma", "i", 64), ("7?", "g", 70, COR)], XE + 270, 620)
    E.frase(c, t, C["s21.b"], [("sorteio", "i", 64), ("de", "i", 64), ("comissão", "g", 70, COR)], XE, 760)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1480, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1810, 1610, p), lerp(650, 355, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dado=b_dado, regra=b_regra, limites=b_limites, bolas=b_bolas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
