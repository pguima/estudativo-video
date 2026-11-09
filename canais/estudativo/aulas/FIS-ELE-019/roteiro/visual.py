"""Visual — Estudativo · FIS-ELE-019: chuveiro, lâmpadas e tomada.

Segue a LINGUAGEM VISUAL DA FÍSICA (docstring do visual.py da FIS-CIN-001) e a da ELETRICIDADE (docstring do visual.py da
FIS-ELE-001): circuito com F.fio em tinta, corrente convencional em setinhas laranja (F.corrente), unidades em cinza-tinta,
grego, "=" e "→" só na fonte pesada. Peças desta aula (copie quando precisar):
- `lamp_entre`: lâmpada de circuito (círculo com X, como F.lampada) com BRILHO contínuo de 0 a 1, para comparar lâmpadas.
  O brilho na tela segue a raiz da potência recebida (100 W = 1), para a mais fraca continuar visível.
- `bulbo`: lâmpada desenhada (vidro, filamento, rosca) para a ilustração; `etiqueta`: cartão "100 W · 220 V".
- `tomada`: tomada de parede como fonte de tensão fixa, ligada por F.fio como qualquer componente.
- `chuveiro`: chuveiro com a chave verão/inverno; `fio_chuveiro`: o fio que esquenta, com a derivação do meio.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-019_chuveiro_lampadas_tomada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("chuveiro", "etiqueta", "ligacoes", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMAR = "#FFC400"

# todas as contas da aula
assert 220 ** 2 == 48400 and 48400 / 22 == 2200 and 48400 / 11 == 4400 and 4400 == 2 * 2200
R100, R25, R40 = 48400 / 100, 48400 / 25, 48400 / 40
assert R100 == 484 and R25 == 1936 and R25 == 4 * R100 and R40 == 1210
i_s = 220 / (R100 + R25)
assert R100 + R25 == 2420 and abs(i_s - 1 / 11) < 1e-12
assert abs(R25 * i_s ** 2 - 16) < 1e-9 and abs(R100 * i_s ** 2 - 4) < 1e-9
assert abs(R100 * i_s - 44) < 1e-9 and abs(R25 * i_s - 176) < 1e-9 and abs(44 ** 2 / R100 - 4) < 1e-9
assert 100 / 25 == 4 and 100 / 40 == 2.5 and R40 / R100 == 2.5
i_q = 220 / (R40 + R100)
assert abs((R40 * i_q ** 2) / (R100 * i_q ** 2) - 2.5) < 1e-9


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-CIN-001 / FIS-ELE-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita "=", "→", fração e potência)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def lembrete(c, t, C, cena, itens):
    """lembrete de n coisas: itens = [(cue, linha fina, linha forte)]; a linha forte aceita fórmula"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hb, gap = (230, 290) if n == 2 else (200, 225)
    y0 = 230 if n == 2 else 170
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hb, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + hb * 0.4)
        E.formula_em(c, t, C[k] + 0.3, l2, x + 44, y + hb * 0.8, 62, "g", COR)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            820, 1000 if n == 3 else 920, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """promessa do gancho: a órbita da Física à direita e os itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 460 + i * 170
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


def inscreva(c, t, tc, td, x=1520, y=420):
    E.foco(c, t, tc, 0.5, lambda a: E.pilula(c, "Inscreva-se", x, y, 76, estilo="g", a=a))
    p = ease_io(prog(t, tc + 0.3, 0.8))
    E.cursor(c, lerp(x + 300, x + 130, p), lerp(y + 300, y + 25, p), ep(t, tc + 0.2, 0.4))
    E.frase(c, t, td, [("bons", "i", 104), ("estudos!", "i", 104, COR)], x + 50, 990, "center")


# ---------------- peças desta aula ----------------
def _brilho(c, cx, cy, r, b, a):
    if b <= 0 or a <= 0:
        return
    g = skia.Paint(AntiAlias=True)
    R = r * (1.5 + 1.9 * b)
    g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), R, [M.hexc(AMAR, 0.7 * b * a), M.hexc(AMAR, 0)], [0, 1]))
    c.drawCircle(cx, cy, R, g)


def lamp_entre(c, t, t0, A, B, brilho=0.0, rotulo=None, lado=1, r=46):
    """lâmpada de circuito entre A e B com brilho de 0 a 1 (pode variar com t)"""
    def fn(a):
        ux, uy = E._uni(*A, *B)
        cx, cy = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        M.line(c, *A, cx - ux * r, cy - uy * r, TINTA, a, 6)
        M.line(c, cx + ux * r, cy + uy * r, *B, TINTA, a, 6)
        _brilho(c, cx, cy, r, brilho, a)
        c.drawCircle(cx, cy, r, M.paint(E.mix("#FFFFFF", AMAR, min(1, brilho * 1.3)), a))
        c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=5))
        k = r * 0.68
        M.line(c, cx - k, cy - k, cx + k, cy + k, TINTA, a, 5)
        M.line(c, cx - k, cy + k, cx + k, cy - k, TINTA, a, 5)
        if rotulo:
            nx, ny = uy * lado, -ux * lado
            E._cola(c, rotulo, cx, cy, nx, ny, r + 26, 50, "b", TINTA, a)
    E.foco(c, t, t0, 0.5, fn)


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


def tomada(c, cx, cy, s, a=1.0, rotulo=None):
    """tomada de parede (padrão brasileiro, três furos) com centro em (cx, cy) e lado s"""
    if a <= 0:
        return
    M.rrect(c, cx - s / 2, cy - s / 2, s, s, s * 0.18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.18, s * 0.18), M.paint(TINTA, a, stroke=5))
    c.drawCircle(cx, cy, s * 0.33, M.paint("#ECECEC", a))
    c.drawCircle(cx, cy, s * 0.33, M.paint(TINTA2, a, stroke=3))
    for dx, dy in ((-0.13, 0.05), (0.13, 0.05), (0, -0.15)):
        c.drawCircle(cx + dx * s, cy + dy * s, s * 0.05, M.paint(TINTA, a))
    if rotulo:
        F.medida(c, rotulo.split()[0], rotulo.split()[1], cx, cy + s * 0.5 + 76, 64, COR, a, "center")


def tomada_entre(c, t, t0, A, B, rotulo="220 V", esq=False):
    """tomada como fonte de um circuito vertical: A em cima, B embaixo"""
    def fn(a):
        cx, cy = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        M.line(c, *A, cx, cy - 70, TINTA, a, 6)
        M.line(c, cx, cy + 70, *B, TINTA, a, 6)
        tomada(c, cx, cy, 140, a)
        F.medida(c, rotulo.split()[0], rotulo.split()[1], cx - 100 if esq else cx + 100, cy + 22, 56, COR, a, "right" if esq else "left")
    E.foco(c, t, t0, 0.5, fn)


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        gi = ease_io(prog(t, C["s01.a"] + 0.6, 0.8))
        E.foco(c, t, C["s01"], 0.6, lambda a: chuveiro(c, 1380, 560, 300, gi, a, ep(t, C["s01.a"] + 0.3, 0.6), t))
        E.frase(c, t, C["s01.a"], [("inverno", "g", 120, COR)], XE, 300)
        E.frase(c, t, C["s01.a"] + 0.8, ps("chave no quente", "i", 66, TINTA2), XE, 400, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("mais", "i", 84) + [("resistência?", "g", 80)], XE, 560, passo=0.14)
        if t >= C["s01.c"]:
            E.risco(c, XE - 10, 580, XE + 680, 500, t, C["s01.c"], largura=12)
            E.foco(c, t, C["s01.c"] + 0.2, 0.4, lambda a: E.pilula(c, "é o contrário", XE + 900, 535, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s01.d"], [("resistência", "g", 104), ("menor", "g", 104, COR)], XE, 820, passo=0.25)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "o chuveiro", 1.4), ("s02.b", "qual lâmpada brilha", 0)))
        E.frase(c, t, C["s02.b"] + 1.3, ps("em série e em paralelo", "i", 60, TINTA2), XE + 110, 730, passo=0.12)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a potência num resistor", "P = R · i^2      P = f{U^2}{R}"),
                              ("s03.c", "série: a mesma corrente", "paralelo: a mesma tensão")))


# ---------------- tomada e chuveiro ----------------
def b_chuveiro(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("na", "i", 90) + [("tomada", "g", 90, COR)], XE, 230)
        E.frase(c, t, C["s04.a"], ps("a mesma tensão,", "i", 70) + [("sempre", "g", 66)], XE, 350, passo=0.12)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: tomada(c, 1540, 330, 230, a))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: F.medida(c, 220, "V", 1540, 560, 120, COR, a, "center"))
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.pilula(c, "fixa", 1540, 640, 44, "g", fundo=TINTA, a=a))
        x0, y0, s = XE, 640, 150
        E.formula_em(c, t, C["s04.c"], "P = f{U^2}{R}", x0, y0, s, "g", TINTA)
        wp = E.formula(None, "P = ", 0, 0, s, "g", a=0)
        wf = E.formula(None, "f{U^2}{R}", 0, 0, s, "g", a=0)
        cxR = x0 + wp + wf / 2
        if t >= C["s04.d"]:
            p = ep(t, C["s04.d"], 0.5)
            E.caixa_pontilhada(c, cxR - 70, y0 - 50, 140, 140, p, cor=E.COR, prog_=p)
            E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: E.escreve(c, "embaixo", cxR + 100, y0 + 60, 54, "i", COR, a))
        E.frase(c, t, C["s04.e"], [("menos", "i", 72), ("R", "g", 72, COR), ("→", "g", 72, TINTA2), ("mais", "i", 72), ("P", "g", 72, COR)],
                XE, 960, passo=0.15)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s07"]:
        def s0506():
            E.frase(c, t, C["s05.a"], ps("mais potência =", "i", 66) + [("mais calor", "g", 64, COR)], W / 2, 170, "center", 0.12)
            cols = ((170, "s05.b", "verão", "22", "s05.c", "48.400 ÷ 22", "s05.d", "2.200 W"),
                    (1000, "s06.a", "inverno", "11", "s06.b", "48.400 ÷ 11", "s06.c", "4.400 W"))
            for x, k1, nome, R, k2, conta, k3, res in cols:
                w = 750
                p = ep(t, C[k1], 0.5)
                E.caixa_pontilhada(c, x, 250, w, 620, p, prog_=p)
                E.frase(c, t, C[k1], [(nome, "g", 72, COR if nome == "inverno" else TINTA)], x + 50, 350)
                E.foco(c, t, C[k1] + 0.3, 0.5, lambda a, x=x, R=R: (E.formula(c, "R = ", x + 50, 480, 90, "g", TINTA, a),
                                                                    F.medida(c, R, "Ω", x + 50 + E.formula(None, "R = ", 0, 0, 90, a=0), 480, 90, TINTA, a)))
                E.foco(c, t, C[k2], 0.5, lambda a, x=x, conta=conta: E.escreve(c, conta, x + 50, 600, 60, "b", TINTA2, a))
                bola_txt(c, t, C[k3], res, x + w / 2, 740, 125, 52, E.COR if nome == "inverno" else TINTA)
            E.foco(c, t, C["s06.a"] + 0.6, 0.4, lambda a: E.pilula(c, "metade", 1560, 450, 42, "g", fundo=TINTA, a=a))
            E.foco(c, t, C["s06.c"] + 0.6, 0.4, lambda a: E.pilula(c, "o dobro", 1640, 640, 42, "g", fundo=E.COR, a=a))
            E.frase(c, t, C["s06.d"], ps("tensão fixa:", "i", 60) + [("P", "g", 60, COR), ("e", "i", 60), ("R", "g", 60, COR)] +
                    ps("inversamente proporcionais", "i", 60), W / 2, 980, "center", 0.1)
        E.saida(c, t, C["s07"] - 0.1, s0506)
    if t < C["s07"]:
        return
    # s07: o fio que esquenta, com a derivação do meio
    E.frase(c, t, C["s07"], ps("como a chave", "i", 76) + [("muda", "g", 76, COR)] + ps("a resistência?", "i", 76), XE, 220, passo=0.12)
    x0, x1, y = 360, 1560, 520
    xm = (x0 + x1) / 2
    n = 16
    pts = [(x0, y)] + [(x0 + (x1 - x0) * k / n, y + 34 * (1 if k % 2 else -1)) for k in range(1, n)] + [(x1, y)]
    q = ease_io(prog(t, C["s07"] + 0.4, 0.9))
    F.poli(c, pts, q, TINTA, 1.0, 7)
    for x, s in ((x0, "comum"), (xm, "inverno"), (x1, "verão")):
        if q >= 0.99:
            M.line(c, x, y, x, y + 180, TINTA, 1.0, 6)
            F.no(c, (x, y))
            E.foco(c, t, C["s07"] + 1.3, 0.4, lambda a, x=x, s=s: centro(c, s, x, y + 250, 48, "i", COR if s == "inverno" else TINTA2, a))
    if t >= C["s07.a"]:
        meio = [p for p in pts if p[0] <= xm + 1]
        F.poli(c, meio, ease_io(prog(t, C["s07.a"], 0.8)), E.COR, 1.0, 9)
        F.corrente(c, t, C["s07.a"] + 0.6, [(x0, y - 70), (xm, y - 70)], fecha=False, espaco=150)
        E.foco(c, t, C["s07.a"] + 0.8, 0.4, lambda a: E.pilula(c, "pedaço menor", (x0 + xm) / 2, y - 140, 46, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s07.b"], ps("fio mais curto →", "g", 64) + [("R", "g", 64, COR), ("menor", "g", 64, COR)], XE, 880, passo=0.12)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "o porquê: segunda lei de Ohm, outra aula", W / 2, 990, 42, "b", fundo=TINTA2, a=a))


# ---------------- lâmpadas: a etiqueta ----------------
def b_etiqueta(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], ps("agora, as", "i", 84) + [("lâmpadas", "g", 84, COR)], XE, 230, passo=0.14)
        acende = ep(t, C["s08.a"], 0.8)
        E.foco(c, t, C["s08"] + 0.5, 0.6, lambda a: bulbo(c, 1460, 420, 170, acende, a))
        E.frase(c, t, C["s08.a"], [("brilho", "g", 76, COR), ("=", "g", 76, TINTA2)] + ps("potência", "i", 80), XE, 420, passo=0.12)
        E.frase(c, t, C["s08.a"] + 0.7, ps("recebida de verdade", "i", 66, TINTA2), XE, 520, passo=0.12)
        E.frase(c, t, lerp(C["s08.a"], C["s08.b"], 0.55), ps("resistência da lâmpada:", "i", 54, TINTA2) + [("fixa", "g", 54)], XE, 640, passo=0.1)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: etiqueta(c, 1460, 870, "100 W", "220 V", a))
        E.frase(c, t, C["s08.c"], ps("só vale", "i", 76) + [("em", "i", 76), ("220", "g", 76, COR), ("V", "b", 60, F.UNID)], XE, 840, passo=0.14)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("da etiqueta sai a", "i", 72) + [("resistência", "g", 70, COR)], XE, 200, passo=0.12)
    E.formula_em(c, t, C["s09"] + 1.0, "R = f{U^2}{P}", XE, 400, 110, "g", TINTA)
    for x, k, P, w, rot in ((1300, "s09.a", "100 W", 90, "R"), (1680, "s09.b", "25 W", 360, "4R")):
        bb = 1.0 if P == "100 W" else 0.5
        E.foco(c, t, C[k], 0.5, lambda a, x=x, bb=bb: bulbo(c, x, 360, 110, bb, a))
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x, P=P: etiqueta(c, x, 640, P, "220 V", a, size=54))
        if t >= C["s09.d"]:
            q = ease_io(prog(t, C["s09.d"] + (0.3 if rot == "4R" else 0), 0.7))
            M.rrect(c, x - w / 2, 800, w * q, 46, 12, E.COR if rot == "4R" else TINTA2, 1.0)
            E.foco(c, t, C["s09.d"] + 0.5, 0.4, lambda a, x=x, rot=rot: centro(c, rot, x, 910, 60, "g", COR if rot == "4R" else TINTA2, a))
    E.frase(c, t, C["s09.c"], ps("menor potência", "i", 58) + [("→", "g", 56, TINTA2), ("maior", "g", 56, COR), ("R", "g", 56, COR)], XE, 560, passo=0.1)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "f{1}{4} da potência", XE, 760, 64, "g", TINTA, a))
    E.foco(c, t, C["s09.d"] + 0.6, 0.5, lambda a: E.formula(c, "4 × a resistência", XE, 900, 64, "g", COR, a))


# ---------------- em paralelo e em série ----------------
def b_ligacoes(c, t, C, b):
    xs, yt, yb = 960, 330, 860
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], ps("em", "i", 96) + [("paralelo", "g", 96, COR)], XE, 260)
            F.fio(c, t, C["s10.a"], [(xs, yt), (1630, yt)])
            F.fio(c, t, C["s10.a"], [(xs, yb), (1630, yb)])
            tomada_entre(c, t, C["s10.a"], (xs, yt), (xs, yb))
            for x, P, bb in ((1330, "100 W", 1.0), (1630, "25 W", 0.5)):
                br = bb * ep(t, C["s10.b"], 0.6)
                lamp_entre(c, t, C["s10.a"] + 0.4, (x, yt), (x, yb), br, P, lado=1)
                F.no(c, (x, yt)) if x < 1600 and t >= C["s10.a"] + 0.4 else None
                F.no(c, (x, yb)) if x < 1600 and t >= C["s10.a"] + 0.4 else None
            E.frase(c, t, C["s10.b"], ps("cada uma:", "i", 66), XE, 420)
            E.foco(c, t, C["s10.b"] + 0.4, 0.5, lambda a: F.medida(c, 220, "V", XE, 530, 96, COR, a))
            E.frase(c, t, C["s10.c"], ps("brilha mais:", "i", 66), XE, 680)
            E.foco(c, t, C["s10.c"] + 0.4, 0.5, lambda a: F.medida(c, 100, "W", XE, 800, 110, COR, a))
            E.frase(c, t, C["s10.d"], [("100", "g", 60), ("contra", "i", 62), ("25", "g", 60)], XE, 930, passo=0.15)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    # s11 e s12: em série
    xs, xd, xl1, xl2 = 1080, 1800, 1340, 1610
    F.fio(c, t, C["s11"], [(xs, yt), (xl1 - 120, yt)])
    F.fio(c, t, C["s11"], [(xl1 + 120, yt), (xl2 - 120, yt)])
    F.fio(c, t, C["s11"], [(xl2 + 120, yt), (xd, yt), (xd, yb), (xs, yb)])
    tomada_entre(c, t, C["s11"], (xs, yt), (xs, yb), esq=True)
    b25, b100 = 0.4 * ep(t, C["s11.b"], 0.6), 0.2 * ep(t, C["s11.b"], 0.6)
    lamp_entre(c, t, C["s11"] + 0.3, (xl1 - 120, yt), (xl1 + 120, yt), b100, "100 W")
    lamp_entre(c, t, C["s11"] + 0.5, (xl2 - 120, yt), (xl2 + 120, yt), b25, "25 W")
    F.corrente(c, t, C["s11.b"], [(xs, yt + 70), (xd - 70, yt + 70), (xd - 70, yb - 70), (xs, yb - 70)], fecha=False, espaco=170)
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: E.pilula(c, "a mesma i", 1470, 720, 46, "g", fundo=E.COR, a=a))

    def s11():
        E.frase(c, t, C["s11.a"], ps("em", "i", 96) + [("série", "g", 96, COR)], XE, 260)
        E.formula_em(c, t, C["s11.b"], "P = R · i^2", XE, 420, 90, "g", TINTA)
        E.frase(c, t, C["s11.c"], ps("mais", "i", 66) + [("R,", "g", 64, COR)] + ps("mais potência", "i", 66), XE, 560, passo=0.12)
        E.frase(c, t, C["s11.d"], ps("brilha mais:", "i", 66), XE, 700)
        E.foco(c, t, C["s11.d"] + 0.4, 0.5, lambda a: F.medida(c, 25, "W", XE, 830, 110, COR, a))
        E.foco(c, t, C["s11.e"], 0.5, lambda a: E.pilula(c, "4 vezes mais", XE + 520, 800, 50, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], ps("a conta inteira", "i", 72), XE, 230)
    E.foco(c, t, C["s12"] + 1.4, 0.5, lambda a: (E.formula(c, "R = 484 + 1.936", XE, 360, 56, "b", TINTA2, a),
                                                 F.medida(c, "= 2.420", "Ω", XE, 440, 56, TINTA2, a)))
    E.foco(c, t, C["s12"] + 3.2, 0.5, lambda a: E.formula(c, "i = f{1}{11} A", XE, 580, 64, "g", TINTA, a))
    E.foco(c, t, C["s12.a"], 0.5, lambda a: (E.bola(c, xl2, 520, 72, E.COR, a), F.medida(c, 16, "W", xl2, 538, 50, BR, a, "center", cor_u=BR)))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.bola(c, xl1, 520, 72, TINTA2, a), F.medida(c, 4, "W", xl1, 538, 50, BR, a, "center", cor_u=BR)))
    E.frase(c, t, C["s12.c"], ps("as duas abaixo da etiqueta:", "i", 54) + [("dividem", "g", 52)] + [("os", "i", 54), ("220", "g", 52), ("V", "b", 40, F.UNID)],
            W / 2, 1000, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s13.a"], ps("a de maior potência", "i", 70), XE, 380, passo=0.12)
    E.frase(c, t, C["s13.a"] + 1.2, ps("sempre brilha mais?", "g", 66), XE, 480, passo=0.12)
    if t >= C["s13.b"] - 0.4:
        E.risco(c, XE - 10, 500, XE + 720, 440, t, C["s13.b"] - 0.4, largura=12)
    E.foco(c, t, C["s13.a"] + 0.4, 0.5, lambda a: etiqueta(c, 1500, 260, "100 W", "220 V", a))
    E.frase(c, t, C["s13.b"], [("100", "g", 66), ("W", "b", 50, F.UNID)] + ps("só com", "i", 70) + [("220", "g", 66, COR), ("V", "b", 50, F.UNID)],
            XE, 660, passo=0.12)
    br = 0.2 * ep(t, C["s13.c"], 0.6)
    E.foco(c, t, C["s13.c"] - 0.3, 0.5, lambda a: bulbo(c, 1500, 560, 120, br, a))
    E.frase(c, t, C["s13.c"], ps("em série:", "i", 70) + [("44", "g", 70, ERRADO), ("V", "b", 54, F.UNID)], XE, 820, passo=0.12)
    bola_txt(c, t, C["s13.d"], "4 W", 1500, 935, 100, 60, ERRADO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("o atalho:", "i", 76, CLARO) + ps("etiquetas da mesma tensão", "g", 60, BR), W / 2, 170, "center", 0.12)
        for i, (k, lig, mm) in enumerate((("s14.a", "paralelo", "maior"), ("s14.b", "série", "menor"))):
            y = 380 + 200 * i
            E.foco(c, t, C[k], 0.5, lambda a, lig=lig, y=y: E.pilula(c, lig, 420, y - 26, 58, "g", fundo=E.COR, a=a))
            E.frase(c, t, C[k] + 0.3, ps("brilha a de", "i", 70, CLARO) + [(mm, "g", 70, BR)] + ps("potência", "i", 70, CLARO), 700, y, passo=0.12)
        E.frase(c, t, C["s14.c"], ps("quantas vezes mais?", "i", 66, CLARO), XE + 120, 840)
        E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "f{100}{25} = 4", 1150, 830, 84, "g", BR, a))
        E.foco(c, t, C["s14.d"] + 0.4, 0.5, lambda a: E.escreve(c, "a razão das etiquetas", 1150, 990, 48, "i", CLARO, a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("mais watts na etiqueta =", "i", 68, CLARO) + [("menos", "g", 66, BR), ("R", "g", 66, BR)], W / 2, 230, "center", 0.12)
    E.frase(c, t, C["s15.b"], ps("tensão fixa:", "i", 66, CLARO) + ps("ganha a menor R", "g", 64, BR), W / 2, 420, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("corrente fixa:", "i", 66, CLARO) + ps("ganha a maior R", "g", 64, BR), W / 2, 560, "center", 0.12)
    E.frase(c, t, C["s15.d"], [("não", "g", 60, ERRADO), ("vale:", "i", 64, CLARO)] + ps("etiquetas com tensões diferentes", "i", 64, CLARO), W / 2, 780, "center", 0.1)
    E.frase(c, t, C["s15.d"] + 2.0, ps("calcule", "i", 60, CLARO) + [("R", "g", 58, BR)] + ps("de cada uma", "i", 60, CLARO), W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16"] + 0.8, ps("duas lâmpadas de", "i", 66) + [("220", "g", 64), ("V", "b", 48, F.UNID)], XE, 320, passo=0.12)
    E.frase(c, t, C["s16.c"], [("em", "i", 76), ("série,", "g", 76, COR)] + ps("na tomada", "i", 76), XE, 520, passo=0.14)
    E.frase(c, t, C["s16.c"] + 1.2, ps("qual brilha mais?", "g", 76), XE, 660, passo=0.14)
    E.frase(c, t, C["s16.d"], ps("quantas vezes mais?", "i", 76, COR), XE, 800, passo=0.14)
    if t < C["s17"]:
        for x, k, P in ((1250, "s16.a", "40 W"), (1650, "s16.b", "100 W")):
            E.foco(c, t, C[k], 0.5, lambda a, x=x: bulbo(c, x, 420, 110, 0, a))
            E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x, P=P: etiqueta(c, x, 720, P, "220 V", a, size=54))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18.a"], [("série:", "g", 80, COR)] + ps("a mesma corrente", "i", 80), XE, 230, passo=0.12)
        E.frase(c, t, C["s18.b"], ps("brilha a de", "i", 70) + [("maior", "g", 66), ("R", "g", 66, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s18.b"] + 1.6, ps("= a de", "g", 66, TINTA2) + [("menor", "g", 66)] + ps("potência na etiqueta", "i", 70), XE, 480, passo=0.12)
        for x, P, bb in ((1250, "40 W", 0.62), (1650, "100 W", 0.25)):
            br = bb * ep(t, C["s18.c"], 0.7)
            E.foco(c, t, C["s18.a"], 0.5, lambda a, x=x, br=br: bulbo(c, x, 680, 100, br, a))
            E.foco(c, t, C["s18.a"] + 0.2, 0.5, lambda a, x=x, P=P: etiqueta(c, x, 940, P, "220 V", a, size=46))
        E.foco(c, t, C["s18.c"] + 0.4, 0.5, lambda a: E.selo(c, 1390, 600, 50, True, a))
        E.frase(c, t, C["s18.c"], [("40", "g", 96, CERTO), ("W", "b", 70, F.UNID)] + ps("brilha mais", "g", 90, CERTO), XE, 720, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19.a"], ps("quantas vezes?", "i", 80), XE, 230)
    E.foco(c, t, C["s19.a"] + 0.8, 0.5, lambda a: E.formula(c, "f{100}{40} =", XE, 430, 100, "g", TINTA, a))
    bola_txt(c, t, C["s19.b"], "2,5 ×", XE + 470, 400, 120, 70)
    E.frase(c, t, C["s19.c"], ps("confira pelas resistências", "i", 66, TINTA2), XE, 640, passo=0.12)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: (E.escreve(c, "40 W:", XE, 760, 64, "b", TINTA2, a), F.medida(c, "1.210", "Ω", XE + 210, 760, 70, TINTA, a)))
    E.foco(c, t, C["s19.e"], 0.5, lambda a: (E.escreve(c, "100 W:", XE, 880, 64, "b", TINTA2, a), F.medida(c, 484, "Ω", XE + 240, 880, 70, TINTA, a)))
    E.foco(c, t, C["s19.f"], 0.5, lambda a: E.formula(c, "f{1.210}{484} = 2,5", 1100, 820, 90, "g", CERTO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", [("tomada:", "g", 64), ("menos", "i", 66), ("R,", "g", 64, COR), ("mais", "i", 66), ("P", "g", 64, COR)]),
                 ("s20.a", [("inverno:", "g", 64), ("a", "i", 66), ("menor", "i", 66), ("resistência", "g", 64, COR)]),
                 ("s20.b", [("paralelo:", "g", 64), ("brilha", "i", 66), ("a", "i", 66), ("de", "i", 66), ("maior", "g", 64, COR), ("potência", "i", 66)]),
                 ("s20.c", [("série:", "g", 64), ("brilha", "i", 66), ("a", "i", 66), ("de", "i", 66), ("menor", "g", 64, COR), ("potência", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 165
            tk = C[k] + (3.2 if i == 1 else 0)
            E.foco(c, t, tk, 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 24, 50, a=a), centro(c, str(i + 1), 300, y - 2, 58, "g", BR, a)))
            E.frase(c, t, tk + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("força", "g", 110, COR), ("eletromotriz", "g", 110, COR)], XE, 400, passo=0.3)
    E.frase(c, t, C["s21.b"], ps("a tensão que se perde", "i", 70) + [("dentro", "g", 66)], XE, 530, passo=0.12)
    # a pilha por dentro: a fem e a resistência interna numa caixa tracejada
    y = 760
    if t >= C["s21.b"]:
        q = ep(t, C["s21.b"], 0.5)
        pt = M.paint(TINTA2, q, stroke=4)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(330, y - 110, 760, 220), 30, 30), pt)
    F.pilha(c, t, C["s21.a"] + 0.6, (230, y), (560, y), "ε")
    F.resistor(c, t, C["s21.b"] + 0.3, (560, y), (900, y), "r")
    F.fio(c, t, C["s21.b"] + 0.3, [(900, y), (1190, y)])
    inscreva(c, t, C["s21.c"], C["s21.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, chuveiro=b_chuveiro, etiqueta=b_etiqueta, ligacoes=b_ligacoes,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
