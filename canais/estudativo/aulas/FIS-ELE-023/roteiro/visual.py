"""Visual — Estudativo · FIS-ELE-023: praticando potência, geradores e receptores (aula de prática, seis questões).

Segue a LINGUAGEM VISUAL DA FÍSICA (FIS-CIN-001), a da ELETRICIDADE (FIS-ELE-001) e a do módulo GERADORES E RECEPTORES
(FIS-ELE-020). As peças vêm das aulas do módulo: `chuveiro`, `bulbo` e `etiqueta` (FIS-ELE-019), `gerador_real` e `circuito`
(FIS-ELE-020/021), `receptor` (FIS-ELE-022). Padrão da prática (copie nas próximas práticas da trilha):
- `enunciado`: pílula "questão N" no alto, os dados à esquerda entrando no tempo da fala e o desenho à direita; no "pause e
  tente", o desenho dá lugar ao relógio de pausa. Na cena da resposta, a pílula fica e os passos descem um por cue, com a
  resposta final na esfera (verde = conferida).
- Método no começo: uma linha por peça (resistor, gerador, receptor, conta), com a fórmula em laranja.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-023_praticando_potencia_geradores_receptores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "q6", "fim"))
BR = "#FFFFFF"
CALOR = "#D9480F"
AMAR = "#FFC400"

# todas as contas da aula
assert 4400 / 1000 == 4.4 and 0.5 * 30 == 15 and abs(4.4 * 15 - 66) < 1e-9 and abs(66 * 0.80 - 52.80) < 1e-9
assert 220 ** 2 == 48400 and 48400 / 4840 == 10 and 48400 / 2420 == 20 and 4840 == 2 * 2420
assert 48400 / 50 == 2 * (48400 / 100) and 100 / 50 == 2
assert 20 / (18 + 2) == 1 and 20 - 2 * 1 == 18 and 18 / 20 == 0.9
assert (12 - 6) / (1 + 2) == 2 and 6 + 2 * 2 == 10 == 12 - 1 * 2 and 6 / 10 == 0.6
assert 20 ** 2 / (4 * 4) == 25 and 20 / (4 + 4) == 2.5 and 4 * 2.5 ** 2 == 25


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-CIN-001 / FIS-ELE-001 / FIS-ELE-019) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for k, (ti, s) in enumerate(itens):
        fim = itens[k + 1][0] - 0.1 if k + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def bola_txt(c, t, t0, s, cx, cy, r_, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r_ * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def lembrete(c, t, C, cena, itens):
    """lembrete de n coisas: itens = [(cue, linha fina, linha forte)]; a linha forte aceita fórmula"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hb, gap = (230, 290) if n == 2 else (200, 225)
    y0 = 230 if n == 2 else 170
    for k, (cue, l1, l2) in enumerate(itens):
        y = y0 + k * gap
        p = ep(t, C[cue], 0.5)
        E.caixa_pontilhada(c, x, y, w, hb, p, prog_=p)
        E.frase(c, t, C[cue] + 0.1, [(l1, "i", 56)], x + 44, y + hb * 0.4)
        E.formula_em(c, t, C[cue] + 0.3, l2, x + 44, y + hb * 0.8, 62, "g", COR)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            820, 1000 if n == 3 else 920, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """promessa do gancho: a órbita da Física à direita e os itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for k, (cue, s, dt) in enumerate(itens):
        y = 460 + k * 170
        E.foco(c, t, C[cue] + dt, 0.5, lambda a, k=k, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(k + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[cue] + dt + 0.1, [(s, "g", 76, COR if k == 0 else TINTA)], XE + 110, y)


def inscreva(c, t, tc, td, x=1520, y=420):
    E.foco(c, t, tc, 0.5, lambda a: E.pilula(c, "Inscreva-se", x, y, 76, estilo="g", a=a))
    p = ease_io(prog(t, tc + 0.3, 0.8))
    E.cursor(c, lerp(x + 300, x + 130, p), lerp(y + 300, y + 25, p), ep(t, tc + 0.2, 0.4))
    E.frase(c, t, td, [("bons", "i", 104), ("estudos!", "i", 104, COR)], x + 50, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for k, (cue, partes) in enumerate(itens):
        y = 360 + k * 190
        E.foco(c, t, C[cue], 0.5, lambda a, k=k, y=y: (E.bola(c, 300, y - 24, 50, a=a), centro(c, str(k + 1), 300, y - 2, 58, "g", BR, a)))
        E.frase(c, t, C[cue] + 0.1, partes, 400, y, passo=0.12)


def caixa_tracejada(c, x, y, w, h, a, cor=TINTA2):
    if a <= 0:
        return
    pt = M.paint(cor, a, stroke=4)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), pt)


def gerador_real(c, t, t0, A, B, rot_e="ε", rot_r="r", tr=None, calor=None, polos=True):
    """gerador real na horizontal, de A (polo −) a B (polo +): pilha (fem) e resistência interna numa caixa tracejada.
    tr = instante da resistência interna (senão, junto); calor = instante em que r acende (perda que vira calor)"""
    tr = t0 if tr is None else tr
    xm = lerp(A[0], B[0], 0.45)
    y = A[1]
    E.foco(c, t, t0, 0.5, lambda a: caixa_tracejada(c, A[0] + 40, y - 120, B[0] - A[0] - 80, 240, a))
    F.pilha(c, t, t0, A, (xm, y), rot_e)
    if calor is not None and t >= calor:
        q = ep(t, calor, 0.6)
        g = skia.Paint(AntiAlias=True)
        cx = (xm + B[0]) / 2
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, y), 150, [M.hexc(CALOR, 0.55 * q), M.hexc(CALOR, 0)], [0, 1]))
        c.drawCircle(cx, y, 150, g)
    F.resistor(c, t, tr, (xm, y), B, rot_r, cor=CALOR if calor is not None and t >= calor else None)
    if polos:
        for P, s in ((A, "−"), (B, "+")):
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, P=P, s=s: (F.no(c, P, a), centro(c, s, P[0], P[1] + 80, 60, "g", F.NEG if s == "−" else E.COR, a)))


def paralelo2(c, t, t0, A, B, rot1, rot2, dy=95):
    """dois resistores em paralelo entre A (direita) e B (esquerda), na horizontal"""
    xa, xb, y = A[0], B[0], A[1]
    xi, xf = xa - 90, xb + 90
    F.fio(c, t, t0, [A, (xi, y), (xi, y - dy)])
    F.fio(c, t, t0, [(xi, y), (xi, y + dy)])
    F.fio(c, t, t0, [B, (xf, y), (xf, y - dy)])
    F.fio(c, t, t0, [(xf, y), (xf, y + dy)])
    F.resistor(c, t, t0 + 0.3, (xi, y - dy), (xf, y - dy), rot1, lado=-1)
    F.resistor(c, t, t0 + 0.4, (xi, y + dy), (xf, y + dy), rot2)
    if t >= t0 + 0.3:
        F.no(c, (xi, y)); F.no(c, (xf, y))


def circuito(c, t, t0, x0, x1, yt, yb, rot_e="ε", rot_r="r", carga="R", tc=None, calor=None, corrente=None, tr=None):
    """a volta padrão: gerador real em cima (− à esquerda, + à direita) e a carga embaixo. carga = rótulo de um resistor ou
    função fn(A, B) que desenha a carga entre A (direita) e B (esquerda). corrente = instante das setinhas (sentido horário)"""
    A, B = (x0 + 110, yt), (x1 - 110, yt)
    F.fio(c, t, t0, [(x0, yb), (x0, yt), A])
    F.fio(c, t, t0, [B, (x1, yt), (x1, yb)])
    gerador_real(c, t, t0, A, B, rot_e, rot_r, tr=tr, calor=calor)
    tc = t0 + 0.3 if tc is None else tc
    if callable(carga):
        carga((x1, yb), (x0, yb))
    else:
        F.resistor(c, t, tc, (x1, yb), (x0, yb), carga)
    if corrente is not None:
        k = 60
        F.corrente(c, t, corrente, [(B[0], yt + k), (x1 - k, yt + k), (x1 - k, yb - k), (x0 + k, yb - k), (x0 + k, yt + k), (A[0], yt + k)],
                   fecha=False, espaco=170)


def tabela(c, t, cols, linhas, x, y, wc, dy=110, size=64, destaque=None, td=None):
    """tabela: cols = cabeçalhos; linhas = [(instante, [células])]; destaque = índice da linha que acende em td"""
    E.foco(c, t, linhas[0][0] - 0.4, 0.4, lambda a: [E.formula(c, s, x + k * wc, y, 50, "b", TINTA2, a) for k, s in enumerate(cols)])
    if t >= linhas[0][0] - 0.4:
        M.line(c, x - 20, y + 26, x + wc * len(cols) - 40, y + 26, TINTA2, ep(t, linhas[0][0] - 0.4, 0.4), 3)
    for j, (ti, cel) in enumerate(linhas):
        yy = y + (j + 1) * dy
        if destaque == j and td is not None and t >= td:
            q = ep(t, td, 0.4)
            M.rrect(c, x - 30, yy - size * 0.95, wc * len(cols) - 10, size * 1.35, 20, E.COR, 0.16 * q)
        for k, s in enumerate(cel):
            E.foco(c, t, ti + 0.25 * k, 0.4, lambda a, s=s, k=k, yy=yy, j=j: E.formula(
                c, s, x + k * wc, yy, size, "g", COR if (destaque == j and td is not None and t >= td) else TINTA, a))


def motor_simb(c, cx, cy, r_, a=1.0):
    """motor: círculo com M"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r_, M.paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r_, M.paint(TINTA, a, stroke=6))
    centro(c, "M", cx, cy + r_ * 0.36, r_, "g", E.COR, a)


def _brilho(c, cx, cy, r, b, a):
    if b <= 0 or a <= 0:
        return
    g = skia.Paint(AntiAlias=True)
    R = r * (1.5 + 1.9 * b)
    g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), R, [M.hexc(AMAR, 0.7 * b * a), M.hexc(AMAR, 0)], [0, 1]))
    c.drawCircle(cx, cy, R, g)


def bulbo(c, cx, cy, r, b=0.0, a=1.0):
    """lâmpada desenhada: vidro com centro em (cx, cy), filamento e rosca embaixo"""
    if a <= 0:
        return
    _brilho(c, cx, cy, r * 1.1, b, a)
    vidro = skia.Path()
    vidro.addCircle(cx, cy, r)
    vidro.addRect(skia.Rect.MakeXYWH(cx - r * 0.42, cy + r * 0.6, r * 0.84, r * 0.6))
    c.drawPath(vidro, M.paint(E.mix("#F4F4F0", AMAR, b * 0.8), a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=6))
    M.line(c, cx - r * 0.42, cy + r * 0.75, cx - r * 0.42, cy + r * 1.2, TINTA, a, 6)
    M.line(c, cx + r * 0.42, cy + r * 0.75, cx + r * 0.42, cy + r * 1.2, TINTA, a, 6)
    for k in range(4):
        M.rrect(c, cx - r * 0.46, cy + r * (1.2 + 0.17 * k), r * 0.92, r * 0.13, 5, "#8C8C96", a)
    pts = [(cx - r * 0.3, cy + r * 0.7), (cx - r * 0.3, cy)] + [(cx - r * 0.3 + r * 0.6 * j / 6, cy - r * 0.18 * (1 if j % 2 else -1)) for j in range(1, 6)] + \
          [(cx + r * 0.3, cy), (cx + r * 0.3, cy + r * 0.7)]
    F.poli(c, pts, 1.0, E.mix(TINTA2, "#FF8A00", b), a, 5)


def etiqueta(c, cx, cy, l1, l2, a=1.0, cor=None, size=58):
    """cartão de etiqueta: duas linhas pesadas"""
    if a <= 0:
        return
    w = max(E.larg(l1, "g", size), E.larg(l2, "g", size * 0.8)) + size * 1.2
    h = size * 2.7
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), M.paint(cor or TINTA, a, stroke=4))
    centro(c, l1, cx, cy - size * 0.05, size, "g", cor or TINTA, a)
    centro(c, l2, cx, cy + size * 0.95, size * 0.8, "b", TINTA2, a)


def chuveiro(c, cx, cy, s, giro=0.0, a=1.0, agua=0.0, t=0.0):
    """chuveiro: cano no alto, crivo em (cx, cy) e a chave à direita; giro de 0 (verão) a 1 (inverno)"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.08, cy - s * 1.25, s * 0.16, s * 0.9, 6, "#9AA0A8", a)
    p = skia.Path()
    p.moveTo(cx - s * 0.25, cy - s * 0.35); p.lineTo(cx + s * 0.25, cy - s * 0.35)
    p.lineTo(cx + s * 0.62, cy + s * 0.12); p.lineTo(cx - s * 0.62, cy + s * 0.12); p.close()
    c.drawPath(p, M.paint("#E9EBEE", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    for k in range(-4, 5):
        c.drawCircle(cx + k * s * 0.12, cy + s * 0.05, s * 0.025, M.paint(TINTA2, a))
    # água
    if agua > 0:
        for k in range(-4, 5):
            for j in range(4):
                fase = (t * 1.6 + j * 0.25 + (k % 3) * 0.11) % 1.0
                x = cx + k * s * 0.12 * (1 + fase * 0.5)
                y = cy + s * 0.2 + fase * s * 1.2
                M.line(c, x, y, x + k * 2, y + s * 0.09, "#4BA3E3", a * agua * (1 - fase), 4)
    # chave
    kx, ky, kr = cx + s * 0.95, cy - s * 0.85, s * 0.22
    c.drawCircle(kx, ky, kr, M.paint("#FFFFFF", a))
    c.drawCircle(kx, ky, kr, M.paint(TINTA, a, stroke=5))
    g = math.radians(-150 + 120 * giro)
    M.line(c, kx, ky, kx + math.cos(g) * kr * 0.8, ky + math.sin(g) * kr * 0.8, E.COR, a, 7)
    E.escreve(c, "verão", kx - kr * 2.9, ky - kr * 0.9, s * 0.13, "i", TINTA2, a)
    E.escreve(c, "inverno", kx + kr * 0.25, ky - kr * 1.25, s * 0.13, "i", COR if giro > 0.5 else TINTA2, a)


def receptor(c, t, t0, A, B, rot_e="ε′", rot_r="r′", calor=None, tr=None, polos=True):
    """receptor na horizontal, a corrente entrando por A (polo +) e saindo por B (polo −): motor (ε′) e r′ numa caixa tracejada"""
    tr = t0 if tr is None else tr
    y = A[1]
    xm = lerp(A[0], B[0], 0.42)
    xc = lerp(A[0], B[0], 0.25)
    E.foco(c, t, t0, 0.5, lambda a: caixa_tracejada(c, min(A[0], B[0]) + 40, y - 120, abs(B[0] - A[0]) - 80, 240, a))

    def mot(a):
        M.line(c, *A, xc - 56, y, TINTA, a, 6)
        M.line(c, xc + 56, y, xm, y, TINTA, a, 6)
        motor_simb(c, xc, y, 56, a)
        if rot_e:
            E._meio(c, rot_e, xc, y - 80, 44, "b", TINTA, a)
    E.foco(c, t, t0, 0.5, mot)
    if calor is not None and t >= calor:
        q = ep(t, calor, 0.6)
        g = skia.Paint(AntiAlias=True)
        cx = (xm + B[0]) / 2
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, y), 150, [M.hexc(CALOR, 0.55 * q), M.hexc(CALOR, 0)], [0, 1]))
        c.drawCircle(cx, y, 150, g)
    F.resistor(c, t, tr, (xm, y), B, rot_r, cor=CALOR if calor is not None and t >= calor else None)
    if polos:
        for P, s in ((A, "+"), (B, "−")):
            E.foco(c, t, t0 + 0.3, 0.4, lambda a, P=P, s=s: (F.no(c, P, a), centro(c, s, P[0], P[1] + 80, 60, "g", F.NEG if s == "−" else E.COR, a)))




# ---------------- prática ----------------
NOMES = ("um", "dois", "três", "quatro", "cinco", "seis")


def enunciado(c, t, C, cena, n, linhas, desenho, tp, resp):
    """questão n: linhas = [(instante, partes)] à esquerda; desenho(a) à direita até tp (pause), depois o relógio; some em resp"""
    E.foco(c, t, C[cena], 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 120, 150, 46, "g", fundo=E.COR, a=a))
    if t >= resp:
        return

    def tudo():
        for k, (ti, partes) in enumerate(linhas):
            E.frase(c, t, ti, partes, XE, 320 + k * 120, passo=0.1)
        if t < tp:
            E.foco(c, t, C[cena] + 0.3, 0.6, desenho)
        else:
            E.relogio(c, t, tp, cx=1500, cy=440, r=190)
    E.saida(c, t, resp - 0.1, tudo)


def passos(c, t, itens, x=XE, y0=320, dy=125):
    """passos da resposta: itens = [(instante, fórmula, cor)]"""
    for k, (ti, s, cor) in enumerate(itens):
        E.foco(c, t, ti, 0.5, lambda a, s=s, k=k, cor=cor: E.formula(c, s, x, y0 + k * dy, 70, "g", cor or TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    for k, (cue, s) in enumerate((("s01.a", "conta de luz"), ("s01.a", "chuveiro"), ("s01.a", "bateria"), ("s01.a", "motor"))):
        E.foco(c, t, C[cue] + 0.5 * k, 0.4, lambda a, k=k, s=s: E.pilula(c, s, 1150 + (k % 2) * 420, 300 + (k // 2) * 150, 58, "g",
                                                                     fundo=E.COR if k % 2 == 0 else TINTA, a=a))
    E.frase(c, t, C["s01.b"], ps("na prova,", "i", 84) + [("misturados", "g", 84, COR)], XE, 300, passo=0.14)
    E.frase(c, t, C["s01.c"], ps("até o fim da aula:", "i", 72), XE, 620, passo=0.12)
    E.foco(c, t, C["s01.c"] + 0.8, 0.5, lambda a: E.escreve(c, "6", XE, 860, 260, "g", COR, a))
    E.frase(c, t, C["s01.c"] + 1.2, ps("questões", "g", 90), XE + 190, 840)
    E.frase(c, t, C["s01.d"], ps("qual fórmula", "i", 64) + [("chamar", "g", 62, COR)], XE + 190, 950, passo=0.12)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s02"], ps("antes, o", "i", 80) + [("método", "g", 80, COR)], XE, 190, passo=0.14)
    E.frase(c, t, C["s02.a"], ps("o que cada peça faz com a energia?", "i", 66), XE, 320, passo=0.1)
    itens = (("s02.b", "resistor", "esquenta: escolha a fórmula pelo que não muda"), ("s02.c", "gerador", "U = ε − r · i"),
             ("s02.d", "receptor", "U = ε′ + r′ · i"), ("s02.e", "conta de luz", "E = P · Δt, em kWh"))
    for k, (cue, nome, f) in enumerate(itens):
        y = 470 + k * 140
        E.foco(c, t, C[cue], 0.5, lambda a, k=k, y=y: (E.bola(c, XE + 36, y - 22, 36, a=a), centro(c, str(k + 1), XE + 36, y - 2, 44, "g", BR, a)))
        E.frase(c, t, C[cue] + 0.1, [(nome, "g", 64)], XE + 100, y)
        E.foco(c, t, C[cue] + 0.5, 0.5, lambda a, f=f, y=y, k=k: (E.formula(c, f, 760, y, 60, "g", COR, a) if k else
                                                                  E.escreve(c, f, 760, y, 54, "i", TINTA, a)))


# ---------------- questão 1: conta de luz ----------------
def b_q1(c, t, C, b):
    enunciado(c, t, C, "s03", 1, [(C["s03.a"], [("chuveiro:", "i", 64), ("4.400", "g", 64), ("W", "b", 48, F.UNID)]),
                                  (C["s03.a"] + 1.5, [("meia", "g", 64), ("hora", "g", 64)] + ps("por dia", "i", 64)),
                                  (C["s03.b"], [("30", "g", 64)] + ps("dias", "i", 64)),
                                  (C["s03.c"], [("1", "g", 64), ("kWh", "b", 48, F.UNID), ("=", "g", 64, TINTA2), ("R$", "b", 52, TINTA2), ("0,80", "g", 64)]),
                                  (C["s03.d"], ps("quanto custa no mês?", "g", 66, COR))],
              lambda a: chuveiro(c, 1450, 520, 300, 1.0, a, ep(t, C["s03"] + 0.6, 0.6), t), C["s03.e"], C["s04"])
    if t < C["s04"]:
        return
    passos(c, t, [(C["s04.a"], "4.400 W ÷ 1.000 = 4,4 kW", None), (C["s04.b"], "0,5 h × 30 = 15 h", None),
                  (C["s04.c"], "E = 4,4 × 15 = 66 kWh", COR), (C["s04.d"], "66 × 0,80 =", None)])
    E.foco(c, t, C["s04.e"], 0.5, lambda a: (E.bola(c, 1150, 670, 150 * ease_back(prog(t, C["s04.e"], 0.5)), CERTO, a),
                                             centro(c, "R$ 52,80", 1150, 690, 56, "g", BR, a)))


# ---------------- questão 2: chuveiro ----------------
def b_q2(c, t, C, b):
    enunciado(c, t, C, "s05", 2, [(C["s05.a"], [("chuveiro", "i", 64), ("de", "i", 64), ("220", "g", 64), ("V", "b", 48, F.UNID)]),
                                  (C["s05.b"], [("4.840", "g", 64), ("W", "b", 48, F.UNID)] + ps("ou", "i", 64)),
                                  (C["s05.c"], [("2.420", "g", 64), ("W", "b", 48, F.UNID)]),
                                  (C["s05.d"], ps("resistência no inverno?", "g", 66, COR))],
              lambda a: chuveiro(c, 1450, 520, 300, 0.5 + 0.5 * math.sin(t * 1.5), a, 1.0, t), C["s05.e"], C["s06"])
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"], [("inverno", "g", 64, COR), ("=", "g", 64, TINTA2)] + ps("maior potência:", "i", 64) + [("4.840", "g", 64), ("W", "b", 48, F.UNID)],
            XE, 300, passo=0.1)
    passos(c, t, [(C["s06.b"], "P = f{U^2}{R}  →  R = f{U^2}{P}", None), (C["s06.c"], "R = f{48.400}{4.840}", None)], y0=460, dy=170)
    bola_txt(c, t, C["s06.d"], "10 Ω", 1150, 610, 110, 64, CERTO)
    E.frase(c, t, C["s06.e"], ps("verão: metade da potência", "i", 60) + [("→", "g", 58, TINTA2), ("20", "g", 62, COR), ("Ω", "b", 48, F.UNID)], XE, 900, passo=0.1)


# ---------------- questão 3: lâmpadas ----------------
def b_q3(c, t, C, b):
    def lampadas(a):
        for x, P in ((1320, "100 W"), (1680, "50 W")):
            bulbo(c, x, 420, 100, 0.0, a)
            etiqueta(c, x, 700, P, "220 V", a, size=50)
    enunciado(c, t, C, "s07", 3, [(C["s07.a"], [("100", "g", 64), ("W", "b", 48, F.UNID), ("e", "i", 64), ("50", "g", 64), ("W", "b", 48, F.UNID)]),
                                  (C["s07.a"] + 1.0, ps("etiquetas de", "i", 64) + [("220", "g", 64), ("V", "b", 48, F.UNID)]),
                                  (C["s07.c"], ps("qual brilha mais em", "i", 64) + [("série?", "g", 64, COR)]),
                                  (C["s07.d"], ps("e em", "i", 64) + [("paralelo?", "g", 64, COR)] + ps("quantas vezes?", "i", 64))],
              lampadas, C["s07.e"], C["s08"])
    if t < C["s08"]:
        return
    for k, (cue, lig, xa, xb, ba, bb) in enumerate((("s08.a", "paralelo", 1180, 1500, 1.0, 0.5), ("s08.c", "série", 1180, 1500, 0.35, 0.7))):
        y = 400 + k * 380
        E.frase(c, t, C[cue], [(lig + ":", "g", 66, COR)] + ps("mesma", "i", 66) + [("tensão" if k == 0 else "corrente", "g", 62)], XE, y, passo=0.12)
        E.foco(c, t, C[cue] + 0.3, 0.5, lambda a, y=y, ba=ba, bb=bb, xa=xa, xb=xb: (bulbo(c, xa, y - 60, 75, ba, a), bulbo(c, xb, y - 60, 75, bb, a),
                                                                                   centro(c, "100 W", xa, y + 120, 44, "g", TINTA, a),
                                                                                   centro(c, "50 W", xb, y + 120, 44, "g", TINTA, a)))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.pilula(c, "100 W brilha mais: o dobro", XE + 380, 500, 44, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "50 W brilha mais", XE + 250, 880, 44, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "f{100}{50} = 2", XE + 520, 1010, 64, "g", COR, a))


# ---------------- questão 4: bateria ----------------
def b_q4(c, t, C, b):
    enunciado(c, t, C, "s09", 4, [(C["s09.a"], [("bateria:", "i", 64), ("20", "g", 64), ("V", "b", 48, F.UNID), ("e", "i", 64), ("2", "g", 64), ("Ω", "b", 48, F.UNID)]),
                                  (C["s09.b"], [("resistor:", "i", 64), ("18", "g", 64), ("Ω", "b", 48, F.UNID)]),
                                  (C["s09.c"], ps("tensão nos polos?", "g", 66, COR)),
                                  (C["s09.d"], ps("rendimento?", "g", 66, COR))],
              lambda a: circuito(c, 0, -9, 1120, 1790, 330, 760, "20 V", "2 Ω", "18 Ω"), C["s09.e"], C["s10"])
    if t < C["s10"]:
        return
    passos(c, t, [(C["s10.a"], "i = f{20}{18 + 2}", None)], y0=360)
    bola_txt(c, t, C["s10.b"], "1 A", 900, 330, 85, 62)
    passos(c, t, [(C["s10.c"], "U = 20 − 2 × 1", None)], y0=600)
    bola_txt(c, t, C["s10.d"], "18 V", 900, 575, 85, 58)
    passos(c, t, [(C["s10.e"], "rendimento = f{18}{20} = 90 %", CERTO)], y0=850)


# ---------------- questão 5: motor ----------------
def b_q5(c, t, C, b):
    def desenho(a):
        circuito(c, 0, -9, 1120, 1790, 330, 760, "12 V", "1 Ω",
                 lambda A, B: receptor(c, 0, -9, A, B, "6 V", "2 Ω"))
    enunciado(c, t, C, "s11", 5, [(C["s11.a"], [("bateria:", "i", 64), ("12", "g", 64), ("V", "b", 48, F.UNID), ("e", "i", 64), ("1", "g", 64), ("Ω", "b", 48, F.UNID)]),
                                  (C["s11.b"], [("motor:", "i", 64), ("ε′", "g", 64, COR), ("=", "g", 64, TINTA2), ("6", "g", 64), ("V", "b", 48, F.UNID),
                                                ("e", "i", 64), ("2", "g", 64), ("Ω", "b", 48, F.UNID)]),
                                  (C["s11.c"], ps("corrente?", "g", 66, COR)),
                                  (C["s11.d"], ps("rendimento do motor?", "g", 66, COR))],
              desenho, C["s11.e"], C["s12"])
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("ε′", "g", 66, COR)] + ps("subtrai:", "i", 66), XE, 300, passo=0.12)
    passos(c, t, [(C["s12.b"], "i = f{12 − 6}{1 + 2} = f{6}{3}", None)], y0=470)
    bola_txt(c, t, C["s12.c"], "2 A", 1080, 440, 85, 62)
    passos(c, t, [(C["s12.d"], "U do motor = 6 + 2 × 2 = 10 V", None), (C["s12.e"], "rendimento = f{6}{10}", None)], y0=690, dy=170)
    bola_txt(c, t, C["s12.f"], "60 %", 1080, 830, 95, 60, CERTO)


# ---------------- questão 6: potência máxima ----------------
def b_q6(c, t, C, b):
    enunciado(c, t, C, "s13", 6, [(C["s13.a"], [("gerador:", "i", 64), ("20", "g", 64), ("V", "b", 48, F.UNID), ("e", "i", 64), ("4", "g", 64), ("Ω", "b", 48, F.UNID)]),
                                  (C["s13.b"], ps("que resistor de fora recebe", "i", 64)),
                                  (C["s13.b"] + 1.2, ps("a maior potência?", "g", 64, COR)),
                                  (C["s13.c"], ps("de quantos watts?", "g", 66, COR))],
              lambda a: circuito(c, 0, -9, 1120, 1790, 330, 760, "20 V", "4 Ω", "R = ?"), C["s13.d"], C["s14"])
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("potência máxima:", "i", 66) + [("R", "g", 66, COR), ("=", "g", 66, TINTA2), ("r", "g", 66, COR)], XE, 300, passo=0.12)
    bola_txt(c, t, C["s14.b"], "4 Ω", 1050, 275, 85, 62)
    passos(c, t, [(C["s14.c"], "P máx = f{20^2}{4 · 4} = f{400}{16}", None)], y0=520)
    bola_txt(c, t, C["s14.d"], "25 W", 1250, 490, 95, 60, CERTO)
    passos(c, t, [(C["s14.e"], "confira: i = f{20}{8} = 2,5 A;  4 × 2,5^2 = 25", TINTA2)], y0=780)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r_():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        E.frase(c, t, C["s15.a"], ps("o que cada peça faz", "i", 80) + ps("com a energia?", "g", 74), W / 2, 450, "center", 0.12)
        E.frase(c, t, C["s15.b"], ps("a fórmula", "i", 90) + [("aparece", "g", 90, COR)], W / 2, 620, "center", 0.14)
    E.saida(c, t, C["s15.c"] - 0.6, r_)
    if t < C["s15.c"] - 0.6:
        return
    E.frase(c, t, C["s15.c"] - 0.5, [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s15.c"], ps("leis de", "i", 96) + [("Kirchhoff", "g", 100, COR)], XE, 420, passo=0.14)
    E.frase(c, t, C["s15.d"], ps("nós, malhas e a", "i", 66) + [("regra", "g", 64), ("de", "g", 64), ("sinais", "g", 64)], XE, 560, passo=0.1)
    inscreva(c, t, C["s15.e"], C["s15.f"])


BLOCKS = dict(gancho=b_gancho, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, q6=b_q6, fim=b_fim)
