"""Visual — Estudativo · MAT-FAT-006: praticando produtos notáveis e fatoração (cinco questões inéditas).
Cada questão: etiqueta "questão n", o enunciado e o relógio de pausa; depois a resposta com a conta que a voz faz e o teste
com 10. (2x − 3)² em três termos; x³ − 4x com o x em evidência e a diferença de quadrados; (x² + 10x + 25)/(x + 5) com o
trinômio reconhecido e o corte; no palco, simplificar antes de trocar o x; 6/(√5 − √2) pelo conjugado; 1.002 · 998 na reta.

Convenções da trilha (as de MAT-FAT-004 e 005): fração em dois andares (fra, andar); CORTAR FATOR = realce da cor da
matéria em cima e embaixo, depois o traço (corta_f); VALOR PROIBIDO = pílula vermelha (proibido); EVIDÊNCIA = o fator
comum na cor da matéria e o parêntese depois (evid); MULTIPLICAR EM CIMA E EMBAIXO = "×" e a fração na cor da matéria
(vezes_um). Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Fatoração e Equação do 2º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FAT-006_praticando_produtos_notaveis_fatoracao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
AM = "#FFD500"

# as contas da aula
x = 10
assert (2 * x - 3) ** 2 == 4 * x * x - 12 * x + 9 == 289 == 17 ** 2 and 400 - 120 + 9 == 289
assert x ** 3 - 4 * x == x * (x + 2) * (x - 2) == 960 == 1000 - 40 == 10 * 12 * 8
x = 95
assert (x * x + 10 * x + 25) // (x + 5) == x + 5 == 100 and (x * x + 10 * x + 25) % (x + 5) == 0 and 2 * 5 == 10
del x
r5, r2 = math.sqrt(5), math.sqrt(2)
assert abs(6 / (r5 - r2) - 2 * (r5 + r2)) < 1e-12 and abs((r5 - r2) * (r5 + r2) - 3) < 1e-12
del r5, r2
assert 1002 * 998 == 1000 ** 2 - 2 ** 2 == 1_000_000 - 4 == 999_996


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def entre(t0, t1, f):
    """instante na fração f do trecho entre dois marcadores: fala sem marcador própria"""
    return t0 + (t1 - t0) * f


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fw(s, size):
    return E.formula(None, s, 0, 0, size, a=0) if s else 0.0


def trecho_x(s, trecho, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s"""
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    return xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, trecho, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
    total = fw("".join(p[0] for p in pecas), size)
    x0 = x - total / 2 if align == "center" else x
    acc = ""
    for p in pecas:
        s, t0, cp = p[0], p[1], (p[2] if len(p) > 2 else cor)
        xo = x0 + fw(acc, size)
        E.foco(c, t, t0, 0.4, lambda a, s=s, xo=xo, cp=cp: E.formula(c, s, xo, y, size, cor=cp, a=a))
        acc += s
    return x0


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def flecha(c, t, t0, x0, y0, x1, y1, alto, cor, d=0.6, largura=6):
    """arco de (x0, y0) a (x1, y1) com ponta de seta; alto > 0 sobe, alto < 0 desce"""
    p = ep(t, t0, d)
    if p <= 0:
        return
    cx = (x0 + x1) / 2
    cy = (min(y0, y1) - alto) if alto > 0 else (max(y0, y1) - alto)
    pt = lambda u: ((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1)
    n = max(2, int(30 * p))
    path = skia.Path()
    path.moveTo(*pt(0))
    for i in range(1, n + 1):
        path.lineTo(*pt(p * i / n))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.97:
        ang = math.atan2(y1 - cy, x1 - cx)
        for da in (2.6, -2.6):
            M.line(c, x1, y1, x1 + 24 * math.cos(ang + da), y1 + 24 * math.sin(ang + da), cor, 1.0, largura)


def chuveiro(c, t, ts, s, y, size, cor, align="center", x=W / 2, alto=90):
    """as quatro setas do chuveirinho, em ts = (1º·1º, 1º·2º, 2º·1º, 2º·2º); s = fórmula com dois parênteses"""
    i2 = s.index(")(") + 1
    p1, p2 = s[1:i2 - 1], s[i2 + 1:-1]
    a1, b1 = p1.split(" ", 1)[0], p1.split(" ", 2)[2]
    a2, b2 = p2.split(" ", 1)[0], p2.split(" ", 2)[2]
    pos = lambda tr, n=0: trecho_x(s, tr, x, size, align, n)
    xa1, wa1 = pos(a1)
    xb1, wb1 = pos(b1)
    xa2, wa2 = pos(a2, 1 if a2 == a1 else 0)
    xb2, wb2 = pos(b2, 1 if b2 == b1 else 0)
    topo, base = y - size * 0.95, y + size * 0.2
    flecha(c, t, ts[0], xa1 + wa1 / 2, topo, xa2 + wa2 / 2, topo, alto * 1.4, cor)
    flecha(c, t, ts[1], xa1 + wa1 / 2, topo, xb2 + wb2 / 2, topo, alto * 2.2, cor)
    flecha(c, t, ts[2], xb1 + wb1 / 2, base, xa2 + wa2 / 2, base, -alto * 1.4, cor)
    flecha(c, t, ts[3], xb1 + wb1 / 2, base, xb2 + wb2 / 2, base, -alto * 2.2, cor)


TONS = (E.COR, M.mix(E.COR, BR, 0.45), M.mix(E.COR, BR, 0.45), M.mix(E.COR, BR, 0.72))


def piso(c, x0, y0, A, B, a=1.0, nomes=("x^2", "3x", "3x", "9"), rot=(0, 0, 0, 0), pinta=(1, 1, 1, 1), falta=(0, 0, 0, 0),
         sizes=(96, 64, 64, 64), escuro=False):
    """piso de lado A + B (em pixels; B = (Bw, Bh) faz o piso retangular A + Bw por A + Bh): quadrado grande A×A, faixa A×B à direita, faixa B×A embaixo, quadradinho B×B.
    rot = alfa do nome de cada pedaço; pinta = quanto cada pedaço já tem a sua cor; falta = pedaço que sumiu (contorno vermelho tracejado)"""
    if a <= 0:
        return
    Bw, Bh = B if isinstance(B, tuple) else (B, B)
    vazio = M.mix(E.COR, BR, 0.88) if not escuro else M.mix(E.COR, "#07070F", 0.5)
    pedacos = ((0, 0, A, A), (A, 0, Bw, A), (0, A, A, Bh), (A, A, Bw, Bh))
    for i, (dx, dy, w, h) in enumerate(pedacos):
        f = falta[i]
        q = a * (1 - 0.85 * f)
        r = skia.Rect.MakeXYWH(x0 + dx, y0 + dy, w, h)
        M.rrect(c, x0 + dx, y0 + dy, w, h, 8, M.mix(vazio, TONS[i], pinta[i]), q)
        c.drawRRect(skia.RRect.MakeRectXY(r, 8, 8), M.paint(E.COR, q, stroke=3))
        if f > 0:
            p = M.paint(ERRADO, a * f, stroke=5)
            p.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
            c.drawRRect(skia.RRect.MakeRectXY(r.makeInset(6, 6), 6, 6), p)
        if rot[i] > 0:
            tinta = BR if (i == 0 and pinta[0] > 0.5) else TINTA
            E.formula(c, nomes[i], x0 + dx + w / 2, y0 + dy + h / 2 + sizes[i] * 0.36, sizes[i], cor=tinta, a=rot[i] * q, align="center")


def lados(c, t, ta, x0, y0, A, B, la="x", lb="3", cor=None, size=64, lb2=None):
    """rótulos dos lados do piso: la + lb à esquerda, la + lb2 em cima (lb2 = lb no quadrado; B = (Bw, Bh) no retangular)"""
    cor = cor or COR
    Bw, Bh = B if isinstance(B, tuple) else (B, B)
    lb2 = lb2 or lb
    E.foco(c, t, ta, 0.45, lambda p: (E.formula(c, la, x0 - 46, y0 + A / 2 + size * 0.36, size, cor=cor, a=p, align="center"),
                                     E.formula(c, lb, x0 - 46, y0 + A + Bh / 2 + size * 0.36, size, cor=cor, a=p, align="center"),
                                     E.formula(c, la, x0 + A / 2, y0 - 28, size, cor=cor, a=p, align="center"),
                                     E.formula(c, lb2, x0 + A + Bw / 2, y0 - 28, size, cor=cor, a=p, align="center")))


def evid(c, t, t0, fator, dentro, x, y, size, align="left", t1=None, cor=None):
    """colocar em evidência (convenção da trilha): o fator comum na cor da matéria, na frente; o parêntese com o que
    sobrou de cada termo entra depois (t1). Devolve o x inicial"""
    s = fator + "(" + dentro + ")"
    x0 = x - fw(s, size) / 2 if align == "center" else x
    form(c, t, t0, fator, x0, y, size, COR)
    form(c, t, t1 if t1 is not None else t0 + 0.4, "(" + dentro + ")", x0 + fw(fator, size), y, size, cor)
    return x0


def arco_d(c, t, t0, s, de, ate_, x, y, size, alto, cor=None, align="left", n=0, rotulo=None):
    """arco com seta do fator de fora até um termo de dentro (distributiva, como em MAT-EQU-004)"""
    x0, w0 = trecho_x(s, de, x, size, align)
    x1, w1 = trecho_x(s, ate_, x, size, align, n)
    E.salto(c, t, t0, x0 + w0 / 2, x1 + w1 / 2, y - size * 0.95, alto, cor or COR, rotulo, size=46)


def fra(c, cima, baixo, cx, y, size, a=1.0, cor=None, cor_c=None, cor_b=None, so_cima=False):
    """fração armada em dois andares, centrada em cx; y = altura da barra. Cada andar é uma fórmula (aceita x^2, r{2})"""
    if a <= 0:
        return
    w = max(fw(cima, size), fw(baixo, size)) + size * 0.3
    tinta = cor or TINTA
    E.formula(c, cima, cx, y - size * 0.32, size, cor=cor_c or tinta, a=a, align="center")
    if not so_cima:
        b = max(5, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(tinta, a))
        E.formula(c, baixo, cx, y + size * 0.98, size, cor=cor_b or tinta, a=a, align="center")


def fra_w(cima, baixo, size):
    return max(fw(cima, size), fw(baixo, size)) + size * 0.3


def fra_em(c, t, t0, cima, baixo, cx, y, size, cor=None, cor_c=None, cor_b=None):
    E.foco(c, t, t0, 0.5, lambda p: fra(c, cima, baixo, cx, y, size, p, cor, cor_c, cor_b))


def andar(c, t, t0, s, cx, y, size, cima=True, cor=None, t1=None):
    """um andar da fração que troca no lugar (fatorado entra em t0 e sai em t1)"""
    yy = y - size * 0.32 if cima else y + size * 0.98
    fn = lambda p: E.formula(c, s, cx, yy, size, cor=cor or TINTA, a=p, align="center")
    if t1 is not None:
        if t0 - 0.01 <= t < t1 + 0.4:
            E.saida(c, t, t1, lambda: E.foco(c, t, t0, 0.45, fn))
    else:
        E.foco(c, t, t0, 0.45, fn)


def barra_f(c, t, t0, cx, y, w, size, cor=None):
    b = max(5, size * 0.07)
    p = ep(t, t0, 0.4)
    if p > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 * p, y - b / 2, w * p, b), b / 2, b / 2), M.paint(cor or TINTA, 1.0))


def yb(y, size, cima):
    """linha de base de um andar"""
    return y - size * 0.32 if cima else y + size * 0.98


def realce_f(c, t, t0, s, trecho, cx, y, size, cima, cor=None, n=0, t1=None):
    realce(c, t, t0, s, trecho, cx, yb(y, size, cima), size, cor, "center", n, t1)


def corta_f(c, t, t0, s, trecho, cx, y, size, cima, cor=None, n=0):
    """corte de um fator: traço inclinado sobre o trecho (na cor da matéria: corte permitido; vermelho: proibido)"""
    if t < t0:
        return
    x0, w = trecho_x(s, trecho, cx, size, "center", n)
    yy = yb(y, size, cima)
    E.risco(c, x0 - 10, yy + size * 0.12, x0 + w + 10, yy - size * 0.8, t, t0, cor or COR, max(6, size * 0.07))


def proibido(c, t, t0, s, cx, cy, size=60):
    """valor proibido (convenção da trilha): pílula vermelha com o x que zera o de baixo da fração original"""
    E.foco(c, t, t0, 0.45, lambda p: E.pilula(c, s, cx, cy, size, estilo="g", fundo=ERRADO, cor=BR, a=p))


def vezes_um(c, t, t0, s, x, y, size, um=True, cor=None):
    """multiplicar em cima e embaixo (convenção da trilha): "× " e a fração s/s na cor da matéria, com "= 1" embaixo.
    x = borda esquerda do "×"; devolve a largura total"""
    wx = fw("× ", size)
    w = fra_w(s, s, size)
    form(c, t, t0, "×", x, y + size * 0.3, size, cor or COR)
    fra_em(c, t, t0, s, s, x + wx + w / 2, y, size, cor or COR)
    if um:
        E.foco(c, t, t0 + 0.5, 0.4, lambda p: centro(c, "= 1", x + wx + w / 2, y + size * 1.75, size * 0.45, "i", cor or COR, p))
    return wx + w

def questao(c, t, t0, n, rot=None):
    """etiqueta da questão (convenção das práticas): pílula "questão n" e o assunto em itálico ao lado"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 150, 150, 52, estilo="g", a=a), sobe=8)
    if rot:
        E.frase(c, t, t0 + 0.3, ps(rot, "i", 64, TINTA2), XE + 340, 168, passo=0.08)


def selo_em(c, t, t0, cx, cy, r, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


def nota(c, t, t0, s, x, y, size=52, cor=None, est="i", align="left"):
    """texto de apoio parado que entra com foco"""
    if align == "center":
        E.foco(c, t, t0, 0.45, lambda p: centro(c, s, x, y, size, est, cor or TINTA2, p))
    else:
        E.foco(c, t, t0, 0.45, lambda p: E.escreve(c, s, x, y, size, est, cor or TINTA2, p))


def fim_padrao(c, t, C, resumo_id, prox_id, itens, prox_l1, prox_big, extra=None, k_ins="d", k_bons="e"):
    """resumo numerado (itens = [(cue, partes)]) e a ponte para a próxima aula com Inscreva-se"""
    def resumo():
        E.frase(c, t, C[resumo_id] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        for k, (tk, partes) in enumerate(itens):
            yy = 430 + k * 200
            E.foco(c, t, tk, 0.5, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), 230, yy - 30, 58, 66, p))
            E.frase(c, t, tk + 0.1, partes, 320, yy, passo=0.12)
    E.saida(c, t, C[prox_id] - 0.1, resumo)
    if t < C[prox_id]:
        return
    E.frase(c, t, C[prox_id] + 0.2, ps(prox_l1, "i", 80), XE, 230, passo=0.1)
    E.frase(c, t, C[prox_id + ".a"], ps(prox_big, "g", 100, COR), XE, 390, passo=0.12)
    if extra:
        extra()
    ci = C[prox_id + "." + k_ins]
    E.foco(c, t, ci, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 600, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, ci + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(890, 645, p), ep(t, ci + 0.2, 0.4), TINTA)
    E.frase(c, t, C[prox_id + "." + k_bons], ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), 1450, 950, "center")


def mil(v):
    return f"{v:,}".replace(",", ".")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]
    E.frase(c, t, ka, [("5", "g", 220, COR)] + ps("questões", "i", 130), XE, 360, passo=0.15)
    E.frase(c, t, ka + 0.8, ps("criadas para esta aula", "i", 70, TINTA2), XE, 470, passo=0.1)
    tf = entre(ka, kb, 0.4)
    for i in range(5):
        E.foco(c, t, tf + i * 0.15, 0.5, lambda a, i=i: num_bola(c, str(i + 1), 1130 + i * 150, 300, 58, 70, a))
    E.frase(c, t, tf + 0.5, ps("uma para cada ferramenta", "i", 56, TINTA2), 1130 - 58, 440, passo=0.08)
    E.foco(c, t, kb, 0.5, lambda a: E.bola(c, XE + 70, 700, 70 * ease_back(prog(t, kb, 0.5)), a=a), blur=0)
    E.foco(c, t, kb + 0.1, 0.4, lambda a: [M.rrect(c, XE + 70 + dx - 11, 670, 22, 60, 6, BR, a) for dx in (-17, 17)])
    E.frase(c, t, kb + 0.2, [("pause", "g", 84, COR)] + ps("e resolva antes da resposta", "i", 84), XE + 170, 730, passo=0.12)
    E.frase(c, t, entre(kb, C["s01.end"], 0.55), ps("errar aqui", "i", 70) + [("não custa nada", "g", 66, CERTO)] + ps("e ensina mais", "i", 70),
            XE + 170, 880, passo=0.1)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("as", "i", 84) + ps("ferramentas", "g", 84, COR), XE, 180)
    itens = (("a", "produtos notáveis", "(a − b)^2 = a^2 − 2ab + b^2"),
             ("b", "evidência", "6x^2 + 9x = 3x(2x + 3)"),
             ("c", "frações com letra", "f{x^2 − 9}{x − 3} = x + 3"),
             ("d", "racionalizar", "f{1}{r{2}} = f{r{2}}{2}"))
    for i, (k, nome, f) in enumerate(itens):
        tk, yy = C[f"s02.{k}"], 330 + i * 145
        E.foco(c, t, tk, 0.45, lambda p, i=i, yy=yy: num_bola(c, str(i + 1), XE + 40, yy - 22, 38, 48, p))
        E.frase(c, t, tk, ps(nome, "g", 58, COR), XE + 110, yy, passo=0.08)
        form(c, t, tk + 0.3, f, 900, yy, 64)
    E.foco(c, t, C["s02.e"], 0.5, lambda a: E.pilula(c, "confira: troque o x por 10 antes e depois", W / 2, 900, 52, estilo="g", fundo=CERTO, a=a), sobe=8)
    E.frase(c, t, entre(C["s02.e"], C["s02.end"], 0.6), ps("travou? procure a aula no canal", "i", 50, TINTA2), XE, 1010, passo=0.08)


# ---------------- questões: enunciado e pausa ----------------
def enunciado(c, t, C, sid, pid, n, rot, verbo, desenha):
    ka, kb = C[f"{sid}.a"], C[f"{sid}.b"]
    questao(c, t, ka, n, rot)
    E.frase(c, t, entre(ka, kb, 0.55), ps(verbo, "i", 84), XE, 380, passo=0.1)
    desenha(kb)
    E.relogio(c, t, C[f"{pid}.a"], 1520, 520, 170)


def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03", "s04", 1, "abrir o produto notável", "escreva sem parênteses",
              lambda kb: (form(c, t, kb, "(2x − 3)^2", XE + 40, 640, 180, COR),
                          E.frase(c, t, entre(kb, C["s03.end"], 0.7), ps("sem multiplicar tudo", "i", 64, TINTA2), XE + 40, 830, passo=0.1)))


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")

    def s05():
        form(c, t, C["s05"] + 0.1, "(2x − 3)^2", XE, 220, 110)
        E.foco(c, t, C["s05"] + 0.4, 0.45, lambda p: (centro(c, "1º", XE + fw("(", 110) + fw("2x", 110) / 2, 300, 44, "b", COR, p),
                                                       centro(c, "2º", XE + fw("(2x ", 110) + fw("− 3", 110) / 2, 300, 44, "b", COR, p)))
        linhas = ((a5, b5, "quadrado do 1º", "2x · 2x", " = 4x^2", 0.55),
                  (b5, c5, "2 · 1º · 2º", "2 · 2x · (−3)", " = −12x", 0.7),
                  (c5, d5, "quadrado do 2º", "(−3)^2", " = +9", 0.45))
        for k, (t0, t1, rot, conta, res, f) in enumerate(linhas):
            yy = 450 + k * 150
            nota(c, t, t0, rot, XE, yy, 50)
            monta(c, t, [(conta, t0 + 0.2), (res, entre(t0, t1, f), COR)], XE + 430, yy, 90)
        form(c, t, d5, "= 4x^2 − 12x + 9", XE, 940, 120, CERTO)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)

    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")

    def s06():
        nota(c, t, C["s06"] + 0.2, "teste com 10", XE, 190, 60)
        monta(c, t, [("(20 − 3)^2 = 17^2", a6), (" = 289", entre(a6, b6, 0.65), COR)], XE, 340, 92)
        monta(c, t, [("400 − 120 + 9", b6), (" = 289", b6 + 1.2, COR)], XE, 480, 92)
        selo_em(c, t, entre(b6, c6, 0.6), 1260, 450, 46)
        form(c, t, c6, "2x^2 − ...", XE, 720, 110, ERRADO)
        if t >= c6 + 0.8:
            E.risco(c, XE - 10, 740, XE + fw("2x^2 − ...", 110) + 10, 640, t, c6 + 0.8, largura=11)
        nota(c, t, c6 + 0.5, "esqueceu de elevar o 2", XE, 810, 50, ERRADO)
        form(c, t, entre(c6, d6, 0.7), "(2x)^2 = 4x^2", 1000, 720, 110, CERTO)
        E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "o quadrado vale para o termo inteiro: número e letra", W / 2, 940, 50, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    fase(c, t, C["s06"], 1e9, s06)


def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s07", "s08", 2, "fatorar", "fatore até o fim",
              lambda kb: form(c, t, kb, "x^3 − 4x", XE + 40, 660, 190, COR))


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    F1 = "x^3 − 4x"

    def s09():
        E.frase(c, t, a9, ps("antes de tudo:", "i", 66, TINTA2) + ps("fator comum", "g", 66, COR), XE, 190, passo=0.1)
        form(c, t, C["s09"] + 0.1, F1, XE, 380, 120)
        realce(c, t, a9 + 0.6, F1, "x", XE, 380, 120)
        realce(c, t, a9 + 0.9, F1, "x", XE, 380, 120, n=1)
        form(c, t, b9, "=", XE, 560, 120)
        x0 = XE + fw("= ", 120)
        evid(c, t, b9, "x", "x^2 − 4", x0, 560, 120, t1=b9 + 0.6)
        realce(c, t, c9, "x(x^2 − 4)", "x^2 − 4", x0, 560, 120)
        form(c, t, c9 + 0.3, "4 = 2^2", 1080, 540, 80, TINTA2)
        nota(c, t, c9 + 0.6, "diferença de dois quadrados", 1080, 630, 54, COR)
        form(c, t, d9, "= x(x + 2)(x − 2)", XE, 820, 130, CERTO)
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)

    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]

    def s10():
        nota(c, t, C["s10"] + 0.2, "teste com 10", XE, 190, 60)
        monta(c, t, [("1.000 − 40", a0), (" = 960", a0 + 1.2, COR)], XE, 360, 96)
        monta(c, t, [("10 · 12 · 8", b0), (" = 960", b0 + 1.3, COR)], XE, 510, 96)
        selo_em(c, t, b0 + 1.8, 1000, 480, 46)
        form(c, t, c0 - 0.3, "x(x^2 − 4)", XE, 770, 110, TINTA2)
        E.foco(c, t, c0, 0.45, lambda p: E.pilula(c, "não errou, mas não terminou", 1250, 735, 56, estilo="g", fundo=TINTA2, cor=BR, a=p))
        E.frase(c, t, entre(c0, C["s10.end"], 0.55), ps("a questão pedia", "i", 66) + ps("até o fim", "g", 66, COR), XE, 940, passo=0.1)
    fase(c, t, C["s10"], 1e9, s10)


def b_questao3(c, t, C, b):
    ka, kb, kc = C["s11.a"], C["s11.b"], C["s11.c"]
    questao(c, t, ka, 3, "simplificar antes da conta")
    E.frase(c, t, entre(ka, kb, 0.5), ps("calcule", "i", 84), XE, 360, passo=0.1)
    fra_em(c, t, kb, "x^2 + 10x + 25", "x + 5", 660, 560, 120, COR)
    form(c, t, kc, "para x = 95", XE + 40, 900, 100)
    E.relogio(c, t, C["s12.a"], 1520, 520, 170)


def b_resposta3(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    TRI, s, y = "x^2 + 10x + 25", 130, 600

    def s13():
        nota(c, t, C["s13"] + 0.2, "trocar o x direto:", XE, 200, 60)
        form(c, t, a3, "95^2 = ?", XE + 560, 210, 100, ERRADO)
        E.frase(c, t, entre(a3, b3, 0.6), ps("simplifique", "g", 70, COR) + ps("antes", "i", 70), 1200, 210, passo=0.1)
        form(c, t, C["s13"] + 0.3, TRI, W / 2, y, s, align="center")
        xs = {k: trecho_x(TRI, k, W / 2, s, "center") for k in ("x^2", "10x", "25")}
        realce(c, t, b3, TRI, "x^2", W / 2, y, s, align="center")
        nota(c, t, b3 + 0.2, "quadrado de x", xs["x^2"][0] + xs["x^2"][1] / 2, y + 100, 46, COR, align="center")
        realce(c, t, entre(b3, c3, 0.5), TRI, "25", W / 2, y, s, align="center")
        nota(c, t, entre(b3, c3, 0.5) + 0.2, "quadrado de 5", xs["25"][0] + xs["25"][1] / 2, y + 100, 46, COR, align="center")
        realce(c, t, c3, TRI, "10x", W / 2, y, s, align="center", cor=CERTO)
        E.foco(c, t, c3 + 0.3, 0.45, lambda p: E.formula(c, "2 · x · 5", xs["10x"][0] + xs["10x"][1] / 2, y - 175, 60, cor=CERTO, a=p, align="center"))
        selo_em(c, t, entre(c3, d3, 0.75), xs["10x"][0] + xs["10x"][1] / 2 + 190, y - 195, 32)
        form(c, t, d3, "= (x + 5)^2", W / 2, 900, 130, CERTO, align="center")
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    TOP, BOT, s2, y2, cx = "(x + 5)(x + 5)", "x + 5", 120, 440, 620

    def s14():
        barra_f(c, t, C["s14"] + 0.1, cx, y2, fra_w(TOP, BOT, s2), s2)
        andar(c, t, C["s14"] + 0.1, TOP, cx, y2, s2, True)
        andar(c, t, C["s14"] + 0.1, BOT, cx, y2, s2, False)
        realce_f(c, t, a4 + 0.2, TOP, "(x + 5)", cx, y2, s2, True)
        realce_f(c, t, a4 + 0.2, BOT, "x + 5", cx, y2, s2, False)
        corta_f(c, t, a4 + 0.9, TOP, "(x + 5)", cx, y2, s2, True)
        corta_f(c, t, a4 + 1.1, BOT, "x + 5", cx, y2, s2, False)
        form(c, t, b4, "= x + 5", cx + 460, y2 + 45, 130, CERTO)
        proibido(c, t, entre(b4, c4, 0.55), "x ≠ −5", 1640, 300, 60)
        nota(c, t, c4 - 0.4, "com 95:", XE, 750, 60)
        monta(c, t, [("95 + 5 = ", c4), ("100", c4 + 0.4, CERTO)], XE, 910, 130)
        E.frase(c, t, entre(c4, C["s14.end"], 0.45), ps("sem calculadora,", "i", 56, TINTA2) + ps("sem conta armada", "i", 56, TINTA2), 1000, 890, passo=0.08)
    fase(c, t, C["s14"], 1e9, s14)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_ = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.2, ps("o atalho desta prática", "i", 72, CLARO), XE, 180, passo=0.1)
    E.frase(c, t, a_, ps("simplifique", "g", 120, BR), XE, 350)
    E.frase(c, t, a_ + 0.5, ps("antes de trocar o x", "i", 96, CLARO), XE, 470, passo=0.12)
    E.frase(c, t, b_, ps("a simplificada vale o mesmo em todo valor permitido", "i", 54, CLARO), XE, 600, passo=0.07)
    fra(c, "x^2 + 10x + 25", "x + 5", 420, 740, 70, ep(t, b_ + 0.8, 0.45), BR)
    form(c, t, b_ + 1.2, "→", 760, 770, 80, AM)
    form(c, t, b_ + 1.4, "x + 5", 860, 770, 90, AM)
    E.frase(c, t, entre(b_, c_, 0.75), ps("a conta", "i", 70, CLARO) + ps("encolhe", "g", 70, AM), 1250, 770, passo=0.1)
    selo_em(c, t, c_, XE + 40, 935, 38, False)
    E.frase(c, t, c_, ps("nada se corta?", "g", 62, BR) + ps("troque o x direto", "i", 62, CLARO), XE + 110, 958, passo=0.08)


def b_questao4(c, t, C, b):
    enunciado(c, t, C, "s16", "s17", 4, "racionalizar", "racionalize",
              lambda kb: fra_em(c, t, kb, "6", "r{5} − r{2}", 560, 600, 150, COR))


def b_resposta4(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    s, y = 100, 470
    K = "r{5} + r{2}"

    def s18():
        E.frase(c, t, C["s18"] + 0.2, ps("subtração embaixo:", "i", 62, TINTA2) + ps("conjugado", "g", 62, COR), XE, 180, passo=0.1)
        fra(c, "6", "r{5} − r{2}", 290, y, s, ep(t, C["s18"] + 0.1, 0.4))
        w = vezes_um(c, t, a8, K, 490, y, s, um=False)
        xm = 490 + fw("× ", s) + fra_w(K, K, s) / 2
        realce_f(c, t, a8 + 0.4, K, "+", xm, y, s, False)
        E.foco(c, t, a8 + 0.5, 0.45, lambda p: E.pilula(c, "conjugado", xm, 300, 50, estilo="g", a=p))
        form(c, t, b8 - 0.3, "=", 490 + w + 30, y + 40, s)
        TOP = "6(r{5} + r{2})"
        cx = 490 + w + 110 + fra_w(TOP, "3", s) / 2
        barra_f(c, t, b8, cx, y, fra_w(TOP, "3", s), s)
        andar(c, t, b8, "3", cx, y, s, False)
        form(c, t, b8 + 0.3, "embaixo: 5 − 2 = 3", XE, 800, 70, TINTA2)
        andar(c, t, c8, TOP, cx, y, s, True)
        form(c, t, c8 + 0.3, "em cima: 6(r{5} + r{2})", XE, 920, 70, TINTA2)
    fase(c, t, C["s18"], C["s19"] - 0.1, s18)

    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")

    def s19():
        TOP, s2, y2, cx = "6(r{5} + r{2})", 100, 380, 450
        fra(c, TOP, "3", cx, y2, s2, ep(t, C["s19"] + 0.1, 0.4))
        realce_f(c, t, a9, TOP, "6", cx, y2, s2, True)
        realce_f(c, t, a9, "3", "3", cx, y2, s2, False)
        nota(c, t, a9 + 0.3, "÷ 3 em cima e embaixo: 6 ÷ 3 = 2", XE, 190, 54)
        x1 = 800
        form(c, t, b9, "= 2(r{5} + r{2})", x1, y2 + 40, 110, CERTO)
        E.foco(c, t, c9, 0.45, lambda p: E.escreve(c, "ou", x1 - 80, y2 + 230, 60, "i", TINTA2, p))
        form(c, t, c9 + 0.1, "2r{5} + 2r{2}", x1 + fw("= ", 110), y2 + 230, 110, CERTO)
        E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "multiplicou só embaixo? mudou o valor", W / 2, 820, 56, estilo="g", fundo=ERRADO, cor=BR, a=a))
        E.frase(c, t, entre(d9, C["s19.end"], 0.55), ps("o de cima", "i", 70) + ps("tem que acompanhar", "g", 70, COR), W / 2, 960, "center", passo=0.1)
    fase(c, t, C["s19"], 1e9, s19)


def b_questao5(c, t, C, b):
    enunciado(c, t, C, "s20", "s21", 5, "cálculo de cabeça", "calcule de cabeça",
              lambda kb: form(c, t, kb, "1.002 · 998", XE + 40, 660, 170, COR))


def b_resposta5(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s22.{k}"] for k in "abcde")
    y = 330
    vx = E.reta(c, t, C["s22"] + 0.1, 420, 1500, y, 997, 1003, [998, 1000, 1002], mil, size=50)
    E.salto(c, t, a_, vx(1000), vx(1002), y, 90, COR, "+2")
    E.salto(c, t, a_ + 0.4, vx(1000), vx(998), y, 90, COR, "−2")
    nota(c, t, a_ + 0.8, "a mesma distância de 1.000", W / 2, 490, 52, COR, align="center")
    form(c, t, b_, "(1.000 + 2)(1.000 − 2)", XE, 640, 96)
    nota(c, t, c_ - 0.4, "soma × diferença", 1350, 630, 52)
    form(c, t, c_, "= 1.000^2 − 2^2", XE, 790, 96)
    form(c, t, d_, "= 1.000.000 − 4", XE, 940, 96)
    form(c, t, e_, "= 999.996", XE + fw("= 1.000.000 − 4 ", 96) + 20, 940, 110, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s23.a"], ps("abra com o", "i", 72) + ps("produto notável certo", "g", 72, COR)),
             (C["s23.b"], ps("procure", "i", 72) + ps("fator comum", "g", 72, COR) + ps("antes de tudo", "i", 72)),
             (C["s23.c"], ps("simplifique", "g", 72, COR) + ps("antes da conta", "i", 72)))
    fim_padrao(c, t, C, "s23", "s24", itens, "próxima aula: a fatoração resolve", "equações do 2º grau",
               extra=lambda: (form(c, t, C["s24.b"], "x^2 − 49 = 0", XE, 580, 96), form(c, t, C["s24.c"], "x^2 − 5x = 0", XE, 740, 96)))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
