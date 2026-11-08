"""Visual — Estudativo · MAT-EST-001: população, amostra e tipos de variáveis. Primeira aula de Estatística.

LINGUAGEM VISUAL DA ESTATÍSTICA (as próximas aulas da trilha copiam daqui; as peças estão neste arquivo, prontas para copiar):
- CORES DAS CATEGORIAS: CATS = E._paleta(n), na ordem em que a categoria aparece na tabela (1ª = cor da matéria, 2ª = cinza
  escuro, 3ª = índigo claro, 4ª = índigo escuro...). A mesma categoria tem a mesma cor em toda a aula: na bolinha da
  população, na linha da tabela, na fatia da barra de 100%, na coluna do gráfico (E.colunas com a cor em cada dado) e no
  setor da pizza (E.pizza(cores=CATS)). Vermelho e verde continuam só para erro e acerto.
- PESSOAS = BOLINHAS (pessoas()): a população é uma grade de bolinhas que entram em onda; a amostra é a parte das bolinhas
  que fica forte com um anel, o resto desbota para cinza claro. Censo = todas fortes.
- TABELA (quadro()): cabeçalho em itálico fino com um fio embaixo; ENTRA COLUNA A COLUNA, cada célula no marcador em que a
  fala diz o número; a 1ª coluna traz a bolinha da cor da categoria; a linha "total" vem depois de um fio grosso.
  Números na grotesca; a coluna da vez (a que está sendo calculada) fica na cor da matéria, as prontas em preto.
- FREQUÊNCIA RELATIVA = BARRA DE 100% (barra100()): uma barra deitada dividida nas fatias das categorias, com a % dentro
  de cada fatia. Duas barras iguais, uma em cima da outra, mostram que a amostra tem as mesmas fatias que a população.
- LISTA DE DADOS NA TELA = FICHAS (fichas()): pílulas brancas com borda fina, em grade; a ficha contada acende na cor da
  categoria e pode voar para a coluna da tabela ou para a caixa do tipo de variável.
- TIPOS DE VARIÁVEL = DUAS CAIXAS PONTILHADAS (qualitativa à esquerda, quantitativa à direita), com as fichas caindo dentro.
- Conta da vez à direita, resposta final na esfera (bola), como no resto do curso; atalho no palco escuro.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-001_populacao_amostra_e_tipos_de_variaveis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("populacao", "variaveis", "erro", "proporcional", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
APAGADO = E.mix(CINZA, PAPEL, 0.6)   # bolinha fora da amostra
CATS = E._paleta(3)                  # manhã, tarde, noite (e produção, escritório, vendas)
assert 500 + 300 + 200 == 1000 and 500 * 80 // 1000 == 40 and 300 * 80 // 1000 == 24 and 200 * 80 // 1000 == 16 and 40 + 24 + 16 == 80
assert 80 / 1000 == 0.08 and 1200 * 0.075 == 90 and 90 // 2 == 45 and 90 // 3 == 30 and 45 + 30 + 15 == 90
assert 240 + 100 + 60 == 400 and 40 / 400 == 0.1 and 24 + 10 + 6 == 40


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


# ================= peças da Estatística (copiar nas próximas aulas) =================
def pessoas(c, t, t0, x, y, cols, lins, passo, r, estado=None, d=0.9):
    """a população em bolinhas: grade cols x lins a partir de (x, y), em onda da esquerda para a direita.
    estado(i, j) -> (cor, anel) muda a bolinha (cor None = cor da matéria; anel True = da amostra). Devolve os centros"""
    pts = []
    for j in range(lins):
        for i in range(cols):
            cx, cy = x + i * passo, y + j * passo
            k = ease_back(prog(t, t0 + d * (i / max(1, cols - 1)) * 0.8 + 0.02 * j, 0.35))
            cor, anel = (estado(i, j) if estado else (None, False))
            if k > 0:
                c.drawCircle(cx, cy, r * k, M.paint(cor or E.COR))
                if anel:
                    c.drawCircle(cx, cy, (r + 7) * k, M.paint(TINTA, 1, stroke=4))
            pts.append((cx, cy))
    return pts


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados que entra coluna a coluna. colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...];
    total = [(texto, t0[, cor]), ...] depois de um fio grosso; cores = cor de cada linha (bolinha antes da 1ª coluna).
    (x, y) = canto de cima à esquerda; devolve o y da linha de base de cada linha"""
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


def barra100(c, t, t0, x, y, w, h, partes, cores=None, rotulos=None, size=46, d=1.0, a=1.0):
    """frequência relativa: barra deitada de 100% dividida nas fatias das categorias (partes em %), cada fatia entra no seu
    tempo (t0 número = em fila; lista = um instante por fatia) e ganha a % (ou o rótulo) dentro"""
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


def fichas(c, t, t0, itens, x, y, w, size=44, gap=22, passo=0.06, voa=None):
    """lista de dados em grade de fichas, da esquerda para a direita. itens = [(texto[, cor acesa, t_acende])].
    voa = {índice: (x, y, t)} faz a ficha voar até (x, y) a partir de t. Devolve os centros"""
    cx, cy, centros = x, y, []
    h = size * 1.55
    for i, it in enumerate(itens):
        s = it[0]
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px, py = cx + wi / 2, cy
        if voa and i in voa:
            vx, vy, tv = voa[i]
            q = ease_io(prog(t, tv, 0.7))
            px, py = lerp(px, vx, q), lerp(py, vy, q)
        cor = it[1] if len(it) > 1 and t >= it[2] else None
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, py=py, cor=cor: ficha(c, s, px, py, size, a, cor), sobe=8)
        centros.append((px, py))
        cx += wi + gap
    return centros


def caixa_tipo(c, t, t0, x, y, w, h, titulo, sub, cor=None):
    """a caixa de um tipo de variável: pontilhada, com o nome em cima"""
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: (centro(c, titulo, x + w / 2, y - 70, 70, "g", cor or COR, a),
                                          centro(c, sub, x + w / 2, y - 18, 44, "i", TINTA2, a)))


# ---------------- peças desta aula ----------------
def panela(c, t, t0, cx, cy, r, mexe=0.0, colher=0.0):
    """a panela de sopa (E.cilindro largo) com a sopa, o redemoinho de mexer e a colher"""
    E.cilindro(c, t, t0, cx, cy, r, 0.62 * r, preenche=0.15)
    ct = cy - 0.62 * r * math.cos(math.radians(22))
    q = ep(t, t0 + 0.6, 0.5)
    if q > 0:
        ry = r * math.sin(math.radians(22))
        c.drawOval(skia.Rect.MakeXYWH(cx - r * 0.96, ct - ry * 0.96 + 10, 2 * r * 0.96, 2 * ry * 0.96), M.paint("#E8A33D", 0.9 * q))
        for dx in (-1, 1):   # alças
            M.line(c, cx + dx * r, ct + 40, cx + dx * (r + 50), ct + 30, TINTA, q, 10)
    if mexe > 0:
        ry = r * math.sin(math.radians(22)) * 0.6
        E._elipse(c, cx, ct + 10, r * 0.6, ry, 200, 300 * mexe, TINTA, 1, 6)
        E._elipse(c, cx, ct + 10, r * 0.35, ry * 0.6, 20, 300 * mexe, TINTA, 0.7, 5)
    if colher > 0:
        k = ease_io(colher)
        bx, by = lerp(cx + r * 1.5, cx + r * 0.35, k), lerp(ct - 260, ct - 4, k)
        M.line(c, bx + 30, by - 20, bx + 230, by - 190, TINTA, 1, 14)
        c.drawOval(skia.Rect.MakeXYWH(bx - 50, by - 30, 100, 60), M.paint("#C8C8CE"))
        c.drawOval(skia.Rect.MakeXYWH(bx - 50, by - 30, 100, 60), M.paint(TINTA, 1, stroke=6))
        if k > 0.95:
            c.drawOval(skia.Rect.MakeXYWH(bx - 38, by - 20, 76, 40), M.paint("#E8A33D"))


def lampada(c, cx, cy, s, a=1.0, acesa=0.0, queimada=False):
    if a <= 0:
        return
    if acesa > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), s * 2.4, [M.hexc("#FFD500", 0.7 * acesa * a), M.hexc("#FFD500", 0.0)], [0, 1]))
        c.drawCircle(cx, cy, s * 2.4, g)
    vidro = "#FFE680" if acesa > 0.5 else (E.mix(TINTA2, BR, 0.3) if queimada else BR)
    c.drawCircle(cx, cy, s, M.paint(vidro, a))
    c.drawCircle(cx, cy, s, M.paint(TINTA, a, stroke=max(3, s * 0.12)))
    M.rrect(c, cx - s * 0.45, cy + s * 0.85, s * 0.9, s * 0.7, s * 0.12, TINTA2, a)


def camisa(c, cx, cy, s, num, a=1.0, cor=None):
    """camisa de futebol com o número"""
    if a <= 0:
        return
    k = s / 100
    p = skia.Path()
    pts = [(-40, -60), (-15, -70), (0, -58), (15, -70), (40, -60), (75, -30), (55, -5), (40, -18), (40, 70), (-40, 70), (-40, -18), (-55, -5), (-75, -30)]
    p.moveTo(cx + pts[0][0] * k, cy + pts[0][1] * k)
    for px, py in pts[1:]:
        p.lineTo(cx + px * k, cy + py * k)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, a))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    centro(c, num, cx, cy + 34 * k, 72 * k, "g", BR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        panela(c, t, a1, 560, 840, 330, mexe=ease_io(prog(t, c1, 1.6)), colher=prog(t, b1, 0.9))
        X = 1440
        E.frase(c, t, a1 + 0.3, ps("a sopa está", "i", 72) + [("salgada?", "g", 76, COR)], X, 240, "center", 0.1)
        E.frase(c, t, a1 + 1.6, ps("não precisa tomar a panela", "i", 52, TINTA2), X, 330, "center", 0.08)
        E.frase(c, t, b1, [("uma colher", "g", 90, COR)] + ps("basta", "i", 90), X, 520, "center", 0.12)
        E.frase(c, t, c1, ps("se você", "i", 66) + [("mexer antes", "g", 72, COR)], X, 680, "center", 0.1)
        E.foco(c, t, c1 + 1.6, 0.5, lambda q: E.pilula(c, "a ideia da estatística", X, 880, 56, "g", a=q, cor=E.SOBRE))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, [("todos", "g", 100, COR)] + ps("ou só", "i", 88) + [("uma parte", "g", 100, COR)], XE, 430, passo=0.14)
        E.frase(c, t, ta + 4.2, ps("e os", "i", 88) + [("tipos de dado", "g", 100, COR)], XE, 580, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa:", XE + 175, 700, 120, "i", TINTA, a))
    E.frase(c, t, C["s03.a"] + 0.6, [("porcentagem", "g", 90, COR)], XE, 860)
    x, w = 980, 820
    itens = (("s03.b", "quantos % a parte é do total:", "parte ÷ total"), ("s03.c", "a porcentagem de um número:", "20% de 80 = 16"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 54), x + 44, y + 84, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 44, y + 170, 68, "g", COR)
    alvo = [260 + i * 280 + 180 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.75), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- população e censo ----------------
PX, PY, PC, PL, PP, PR = 150, 330, 12, 7, 74, 24   # a grade da população: 12 x 7 = 84 bolinhas


def amostra_espalhada(i, j):
    return (i * 5 + j * 3) % 7 == 0      # 12 bolinhas espalhadas


def b_populacao(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    lamp = ep(t, d4, 0.6) * (1 - ep(t, C["s05"], 0.5))
    vira = ep(t, C["s05"], 0.5)

    def est(i, j):
        if t >= a5:   # censo: todas fortes, com anel
            return None, ep(t, a5 + 0.02 * (i + j), 0.3) > 0.5
        return E.mix(APAGADO, E.COR, vira) if t < b4 or t >= C["s05"] else None, False
    if lamp < 0.99:
        c.save()
        if lamp > 0:
            pa = skia.Paint(); pa.setAlphaf(1 - lamp); c.saveLayer(None, pa)
        pessoas(c, t, C["s04"], PX, PY, PC, PL, PP, PR, est)
        if lamp > 0:
            c.restore()
        c.restore()
    if lamp > 0:
        for j in range(PL):
            for i in range(PC):
                lampada(c, PX + i * PP, PY + j * PP - 6, 20, lamp)
    gx0, gy0, gx1, gy1 = PX - 50, PY - 50, PX + (PC - 1) * PP + 50, PY + (PL - 1) * PP + 50
    if t >= b4:
        p = ep(t, b4, 0.6)
        E.caixa_pontilhada(c, gx0, gy0, gx1 - gx0, gy1 - gy0, p, None, prog_=p)
        E.foco(c, t, b4 + 0.2, 0.4, lambda a: E.escreve(c, "população", gx0, gy0 - 30, 64, "g", COR, a))
    X = 1480

    def um():
        E.frase(c, t, a4, ps("quem me", "i", 70) + [("interessa?", "g", 76, COR)], X, 260, "center", 0.1)
        E.frase(c, t, b4, ps("o grupo inteiro:", "i", 58), X, 400, "center", 0.1)
        E.frase(c, t, b4 + 0.6, [("população", "g", 84, COR)], X, 500, "center", 0.1)
        E.frase(c, t, c4, ps("todos os alunos", "i", 56), X, 650, "center", 0.1)
        E.frase(c, t, c4 + 0.8, ps("da escola", "i", 56), X, 720, "center", 0.1)
        E.frase(c, t, d4, ps("ou as lâmpadas", "i", 56, TINTA2), X, 860, "center", 0.1)
        E.frase(c, t, d4 + 0.8, ps("de uma fábrica", "i", 56, TINTA2), X, 930, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, a5, ps("ouve", "i", 64) + [("todos", "g", 70, COR)], X, 260, "center", 0.1)
    E.frase(c, t, b5, [("censo", "g", 120, COR)], X, 420, "center", 0.1)
    E.frase(c, t, c5, ps("IBGE: visita", "i", 52) + [("todos", "g", 56)], X, 580, "center", 0.1)
    E.frase(c, t, c5 + 0.8, ps("os domicílios do país", "i", 52), X, 650, "center", 0.1)
    E.foco(c, t, d5, 0.5, lambda q: E.pilula(c, "completo, mas caro e demorado", X, 820, 46, "g", fundo=TINTA2, a=q))


# ---------------- amostra ----------------
def b_amostra(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    canto = t >= b7

    def est(i, j):
        if t < a6:
            return None, False
        if canto:   # amostra de um canto só
            dentro = i >= 9 and j <= 3
            q = ep(t, b7 + 0.04 * (i + j), 0.3)
            return (E.mix(APAGADO, ERRADO, q) if dentro else APAGADO), dentro and q > 0.5
        dentro = amostra_espalhada(i, j)
        q = ep(t, a6, 0.5)
        return (E.COR if dentro else E.mix(E.COR, APAGADO, q)), dentro and q > 0.5
    pessoas(c, t, C["s06"] - 3, PX, PY, PC, PL, PP, PR, est)
    gx0, gy0, gx1, gy1 = PX - 50, PY - 50, PX + (PC - 1) * PP + 50, PY + (PL - 1) * PP + 50
    E.caixa_pontilhada(c, gx0, gy0, gx1 - gx0, gy1 - gy0, 1.0, None)
    E.escreve(c, "população", gx0, gy0 - 30, 64, "g", COR)
    if canto:
        p = ep(t, c7, 0.5)
        E.caixa_pontilhada(c, PX + 9 * PP - 40, PY - 40, 3 * PP + 80 - 80 + 80, 4 * PP - 74 + 80, p, ERRADO, prog_=p)
    X = 1480

    def um():
        E.frase(c, t, a6, ps("só uma", "i", 66) + [("parte:", "g", 72)], X, 260, "center", 0.1)
        E.frase(c, t, b6, [("amostra", "g", 120, COR)], X, 420, "center", 0.1)
        E.foco(c, t, c6, 0.5, lambda q: lampada(c, X - 120, 640, 52, q, acesa=1 - ep(t, c6 + 1.8, 0.4), queimada=t > c6 + 2))
        E.frase(c, t, c6 + 0.4, ps("acesa até", "i", 52), X + 90, 630, "center", 0.1)
        E.frase(c, t, c6 + 1.0, [("queimar", "g", 56, COR)], X + 90, 700, "center", 0.1)
        E.frase(c, t, d6, ps("testar todas =", "i", 52) + [("sem estoque", "g", 56, ERRADO)], X, 880, "center", 0.1)
    fase(c, t, C["s06"], C["s07"] - 0.1, um)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, a7, ps("precisa", "i", 62) + [("parecer", "g", 66, COR)], X, 260, "center", 0.1)
    E.frase(c, t, a7 + 0.8, ps("com a população", "i", 62), X, 340, "center", 0.1)
    E.frase(c, t, a7 + 1.6, ps("a colher da sopa mexida", "i", 50, TINTA2), X, 420, "center", 0.08)
    E.frase(c, t, b7, ps("futebol só na", "i", 56) + [("porta do estádio", "g", 58, ERRADO)], X, 640, "center", 0.1)
    E.foco(c, t, c7, 0.5, lambda a: E.selo(c, X - 250, 820, 46, False, a))
    E.frase(c, t, c7 + 0.1, ps("um canto só", "i", 60), X - 180, 845, "left", 0.1)


# ---------------- tipos de variável ----------------
QX, QW, QY, QH = 160, 760, 420, 520   # caixa qualitativa; a quantitativa espelhada à direita
NX = W - QX - QW


def b_variaveis(c, t, C, b):
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    E.frase(c, t, a8, ps("o que a pesquisa pergunta:", "i", 60) + [("variável", "g", 70, COR)], W / 2, 170, "center", 0.1)
    E.frase(c, t, b8, [("2 tipos", "g", 60)], W / 2, 250, "center", 0.1)
    caixa_tipo(c, t, c8, QX, QY, QW, QH, "qualitativa", "categoria, qualidade")
    caixa_tipo(c, t, e8, NX, QY, QW, QH, "quantitativa", "número que se conta ou mede", TINTA2)
    for i, (s, t0) in enumerate((("cor preferida", c8 + 1.6), ("time", c8 + 2.2), ("turno de estudo", d8))):
        y = QY + 110 + i * 140
        E.foco(c, t, t0, 0.5, lambda a, s=s, y=y: ficha(c, s, QX + QW / 2, y, 52, a, E.COR), sobe=40)
    for i, (s, t0) in enumerate((("idade", f8), ("altura", f8 + 0.5), ("número de filhos", f8 + 1.0))):
        y = QY + 110 + i * 140
        E.foco(c, t, t0, 0.5, lambda a, s=s, y=y: ficha(c, s, NX + QW / 2, y, 52, a, TINTA2), sobe=40)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    E.frase(c, t, C["s09"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 170, "center", 0.1)
    E.frase(c, t, a9, ps("tem número, então é", "i", 58) + [("quantitativa?", "g", 62, ERRADO)], W / 2, 260, "center", 0.1)

    def camisas():
        E.foco(c, t, b9, 0.5, lambda a: camisa(c, 430, 560, 190, "10", a))
        E.foco(c, t, b9 + 0.4, 0.5, lambda a: camisa(c, 860, 560, 190, "5", a, TINTA2))
        fcen(c, t, c9, "10 = 2 × 5 ?", 1440, 520, 96, ERRADO)
        if t >= c9 + 1.0:
            E.risco(c, 1160, 560, 1720, 440, t, c9 + 1.0, largura=12)
        E.frase(c, t, c9 + 1.8, ps("a camisa 10 não vale o dobro", "i", 52), 1440, 640, "center", 0.1)
        E.frase(c, t, c9 + 3.2, ps("o número só", "i", 52) + [("dá nome", "g", 56, COR)], 1440, 720, "center", 0.1)
    fase(c, t, b9, d9 - 0.1, camisas)
    if t < d9 - 0.1:
        return
    caixa_tipo(c, t, d9, QX, 420, QW, 420, "qualitativa", "só dá nome")
    for i, s in enumerate(("número da camisa", "CEP", "telefone")):
        E.foco(c, t, d9 + 0.3 + 0.4 * i, 0.5, lambda a, s=s, i=i: ficha(c, s, QX + QW / 2, 530 + i * 120, 50, a, E.COR), sobe=40)
    X = 1400
    E.foco(c, t, e9, 0.5, lambda a: E.pilula(c, "o teste: faz sentido somar?", X, 470, 52, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, e9 + 1.8, 0.5, lambda a: E.selo(c, X - 170, 640, 44, True, a))
    E.frase(c, t, e9 + 1.9, ps("idade:", "i", 60) + [("sim", "g", 64, CERTO)], X - 100, 662, "left", 0.1)
    E.foco(c, t, e9 + 2.6, 0.5, lambda a: E.selo(c, X - 170, 780, 44, False, a))
    E.frase(c, t, e9 + 2.7, ps("camisa:", "i", 60) + [("não", "g", 64, ERRADO)], X - 100, 802, "left", 0.1)


# ---------------- amostra proporcional ----------------
TX, TY = 170, 330
COLS_T = [("turno", 300, 0), ("alunos", 260, 0), ("%", 220, 0), ("amostra", 280, 0)]


def b_proporcional(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, a0, ps("amostra", "i", 70) + [("proporcional", "g", 76, COR)], XE, 190, "left", 0.1)
    vez = lambda ti, prox: COR if ti <= t < prox else TINTA
    cols = [("turno", 270, b0), ("alunos", 230, b0 + 0.3), ("%", 200, b1 - 0.4), ("amostra", 240, a2 - 0.3)]
    linhas = [[("manhã", b0 + 0.6), ("500", b0 + 0.9), ("50%", b1, vez(b1, C["s12"])), ("40", a2, vez(a2, d2))],
              [("tarde", b0 + 1.6), ("300", b0 + 1.9), ("30%", c1, vez(c1, C["s12"])), ("24", b2, vez(b2, d2))],
              [("noite", b0 + 2.6), ("200", b0 + 2.9), ("20%", d1, vez(d1, C["s12"])), ("16", c2, vez(c2, d2))]]
    total = [("total", b0 + 3.4), ("1.000", b0 + 3.6), ("100%", d1 + 1.4), ("80", c0 if t < d2 else d2, COR if t < a2 else TINTA)]
    quadro(c, t, TX, TY, cols, linhas, total, size=58, cores=CATS)
    X = 1510

    def conta10():
        E.frase(c, t, c0, ps("a pesquisa vai ouvir", "i", 56), X, 380, "center", 0.1)
        bola_txt(c, t, c0 + 0.6, "80", X, 560, 110, 84)
        E.frase(c, t, c0 + 1.6, ps("quantos de cada turno?", "i", 56), X, 760, "center", 0.1)
    fase(c, t, C["s10"], C["s11"] - 0.1, conta10)

    def conta11():
        E.frase(c, t, a1, ps("cada turno pesa", "i", 52), X, 330, "center", 0.1)
        E.frase(c, t, a1 + 0.9, ps("na amostra o", "i", 52) + [("mesmo", "g", 56, COR)] + ps("que na escola", "i", 52), X, 400, "center", 0.1)
        fcen(c, t, b1, "500 ÷ 1.000 = 0,5 = 50%", X, 560, 56, COR)
        fcen(c, t, c1, "300 ÷ 1.000 = 30%", X, 680, 56)
        fcen(c, t, d1, "200 ÷ 1.000 = 20%", X, 800, 56)
    fase(c, t, C["s11"], C["s12"] - 0.1, conta11)
    if t >= C["s12"] - 0.1:
        fcen(c, t, a2, "50% de 80 = 40", X, 360, 60)
        fcen(c, t, b2, "30% de 80 = 24", X, 480, 60)
        fcen(c, t, c2, "20% de 80 = 16", X, 600, 60)
        fcen(c, t, d2, "40 + 24 + 16 = 80", X, 760, 66, COR)
        E.foco(c, t, d2 + 1.0, 0.5, lambda a: E.selo(c, X - 120, 880, 44, True, a))
        E.frase(c, t, d2 + 1.1, [("bateu", "g", 62, CERTO)], X - 50, 902, "left", 0.1)
    # a barra de 100%: a escola e a amostra com as mesmas fatias
    barra100(c, t, [b1, c1, d1], TX, 830, 940, 80, [50, 30, 20], CATS, size=40)
    E.foco(c, t, b1, 0.4, lambda a: E.escreve(c, "escola", TX, 815, 38, "i", TINTA2, a))
    if t >= C["s12"]:
        barra100(c, t, [a2, b2, c2], TX, 960, 940, 80, [50, 30, 20], CATS, ["40", "24", "16"], size=40)
        E.foco(c, t, a2, 0.4, lambda a: E.escreve(c, "amostra", TX, 945, 38, "i", TINTA2, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4, e4, f4 = (C[f"s14.{k}"] for k in "abcdef")

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
        E.frase(c, t, a3, ps("amostra é quantos % da", "i", 66, CLARO) + [("população?", "g", 70, BR)], W / 2, 270, "center", 0.1)
        fcen(c, t, b3, "80 ÷ 1.000 = 0,08 = 8%", W / 2, 440, 90, BR)
        E.frase(c, t, c3, ps("tire", "i", 62, CLARO) + [("8%", "g", 68, BR)] + ps("de cada turno", "i", 62, CLARO), W / 2, 580, "center", 0.1)
        for i, (s, ti) in enumerate((("8% de 500 = 40", d3), ("8% de 300 = 24", d3 + 2.0), ("8% de 200 = 16", d3 + 3.4))):
            x = 400 + i * 560
            E.foco(c, t, ti, 0.5, lambda a, x=x, i=i: c.drawCircle(x - 215, 742, 16, M.paint(E.mix(CATS[i], BR, 0.25), a)))
            fcen(c, t, ti, s, x + 20, 760, 54, BR)
    fase(c, t, C["s13"], C["s14"] - 0.1, um)
    if t < C["s14"] - 0.1:
        return
    E.frase(c, t, C["s14"] + 0.2, ps("funciona porque é", "i", 62, CLARO) + [("a mesma fatia", "g", 66, BR)] + ps("de cada turno", "i", 62, CLARO),
            W / 2, 190, "center", 0.1)
    E.foco(c, t, b4, 0.5, lambda a: E.selo(c, 330, 340, 46, False, a))
    E.frase(c, t, b4 + 0.1, ps("não compensa: % quebrada", "i", 60, CLARO), 410, 362, "left", 0.1)
    fcen(c, t, c4, "90 ÷ 1.200 = 7,5%", W / 2, 520, 80, CLARO)
    E.frase(c, t, d4, ps("manhã =", "i", 58, CLARO) + [("metade", "g", 62, BR)], 560, 700, "center", 0.1)
    fcen(c, t, e4, "90 ÷ 2 = 45", 560, 820, 76, BR)
    E.frase(c, t, f4 - 1.6, ps("tarde =", "i", 58, CLARO) + [("um terço", "g", 62, BR)], 1360, 700, "center", 0.1)
    fcen(c, t, f4, "90 ÷ 3 = 30", 1360, 820, 76, BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, ps("empresa:", "i", 60) + [("400", "g", 64, COR)] + ps("funcionários", "i", 60), XE, 300, passo=0.1)
    E.frase(c, t, b5, ps("pesquisa ouve", "i", 60) + [("40,", "g", 64, COR)] + ps("proporcional ao setor", "i", 56), XE, 400, passo=0.1)
    E.frase(c, t, c5, [("1)", "g", 60, COR)] + ps("censo ou amostra?", "i", 60), XE, 540, passo=0.1)
    E.frase(c, t, d5, [("2)", "g", 60, COR)] + ps("quantos de cada setor?", "i", 60), XE, 640, passo=0.1)
    E.frase(c, t, e5, [("3)", "g", 60, COR)] + ps("tipo de variável:", "i", 60), XE, 740, passo=0.1)
    E.foco(c, t, e5 + 1.2, 0.4, lambda a: (ficha(c, "setor", XE + 110, 840, 46, a), ficha(c, "salário", XE + 330, 840, 46, a),
                                          ficha(c, "nº do crachá", XE + 610, 840, 46, a)))

    def tab():
        cols = [("setor", 320, a5 + 0.3), ("funcionários", 340, a5 + 0.5)]
        linhas = [[("produção", a5 + 1.0), ("240", a5 + 1.2)], [("escritório", a5 + 1.8), ("100", a5 + 2.0)], [("vendas", a5 + 2.6), ("60", a5 + 2.8)]]
        quadro(c, t, 1180, 330, cols, linhas, [("total", a5 + 3.3), ("400", a5 + 3.5)], size=54, cores=CATS)
    E.saida(c, t, C["s16.a"] - 0.1, tab)
    E.relogio(c, t, C["s16.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    X = 1440

    def um():
        cols = [("setor", 320, C["s17"]), ("funcionários", 340, C["s17"]), ("amostra", 280, c7 - 0.3)]
        linhas = [[("produção", C["s17"]), ("240", C["s17"]), ("24", c7, COR)],
                  [("escritório", C["s17"]), ("100", C["s17"]), ("10", d7, COR)],
                  [("vendas", C["s17"]), ("60", C["s17"]), ("6", e7, COR)]]
        quadro(c, t, 140, 380, cols, linhas, [("total", C["s17"]), ("400", C["s17"]), ("40", e7 + 1.6)], size=54, cores=CATS)
        E.foco(c, t, a7, 0.5, lambda q: E.pilula(c, "1) amostra", X, 240, 60, "g", a=q, cor=E.SOBRE))
        fcen(c, t, b7, "40 ÷ 400 = 0,1 = 10%", X, 420, 64)
        fcen(c, t, c7, "10% de 240 = 24", X, 560, 58)
        fcen(c, t, d7, "10% de 100 = 10", X, 670, 58)
        fcen(c, t, e7, "10% de 60 = 6", X, 780, 58)
        fcen(c, t, e7 + 1.6, "24 + 10 + 6 = 40", X, 920, 62, COR)
        E.foco(c, t, e7 + 2.6, 0.5, lambda a: E.selo(c, X + 330, 900, 40, True, a))
    fase(c, t, C["s17"], C["s18"] - 0.1, um)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.1, [("3)", "g", 62, COR)] + ps("tipo de variável", "i", 62), W / 2, 200, "center", 0.1)
    caixa_tipo(c, t, C["s18"], QX, 420, QW, 460, "qualitativa", "categoria")
    caixa_tipo(c, t, C["s18"] + 0.2, NX, 420, QW, 460, "quantitativa", "dá para somar e comparar", TINTA2)
    E.foco(c, t, a8, 0.5, lambda a: ficha(c, "setor", QX + QW / 2, 560, 56, a, E.COR), sobe=40)
    E.foco(c, t, b8, 0.5, lambda a: ficha(c, "salário", NX + QW / 2, 560, 56, a, TINTA2), sobe=40)
    E.foco(c, t, c8, 0.5, lambda a: ficha(c, "nº do crachá", QX + QW / 2, 720, 56, a, E.COR), sobe=40)
    E.frase(c, t, c8 + 1.0, ps("só identifica a pessoa", "i", 48, TINTA2), QX + QW / 2, 830, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("censo", "g", 70, COR)] + ps("ouve todos,", "i", 64) + [("amostra", "g", 70, COR)] + ps("uma parte", "i", 64)),
                 ("s19.b", [("qualitativa", "g", 70, COR)] + ps("é categoria,", "i", 64) + [("quantitativa", "g", 70, TINTA2)] + ps("é quantidade", "i", 64)),
                 ("s19.c", ps("proporcional:", "i", 64) + [("a mesma %", "g", 70, COR)] + ps("de cada grupo", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("tabela", "g", 120, COR)] + ps("de frequência", "i", 96), XE, 410)
    E.frase(c, t, b0, ps("quantas vezes cada resposta aparece", "i", 52), XE, 540, passo=0.08)
    E.frase(c, t, c0, ps("idades de", "i", 52) + [("10 em 10", "g", 56, COR)] + ps("anos", "i", 52), XE, 630, passo=0.1)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, populacao=b_populacao, amostra=b_amostra, variaveis=b_variaveis, erro=b_erro,
              proporcional=b_proporcional, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
