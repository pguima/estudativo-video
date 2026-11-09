"""Visual — Estudativo · FIS-ELE-022: receptores e associação de pilhas.

Segue a LINGUAGEM VISUAL DA FÍSICA (docstring do visual.py da FIS-CIN-001), a da ELETRICIDADE (FIS-ELE-001) e a do módulo
GERADORES E RECEPTORES (docstring do visual.py da FIS-ELE-020): gerador real = pilha + r numa caixa tracejada, perda em cor de
calor, a volta padrão `circuito` (FIS-ELE-021). Peças novas desta aula (copie quando precisar):
- RECEPTOR = `receptor`: motor (círculo com M, o ε′) e a resistência interna r′ numa caixa tracejada; o polo + do receptor
  fica do lado por onde a corrente ENTRA. ε′ e r′ escritos com o apóstrofo tipográfico (′), na fonte pesada.
- `ventilador`: o ventilador do gancho, girando ou travado (com o calor no motor).
- `pilha_desenho`: pilha comum deitada (corpo escuro, faixa laranja, polo + à direita; `vira=True` inverte a pilha).
- Pilhas em série = uma fila encostada; em paralelo = pilhas empilhadas com os polos iguais ligados por fios.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-022_receptores_associacao_de_pilhas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("receptor", "motor", "pilhas", "paralelo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CALOR = "#D9480F"

# todas as contas da aula
e_, r_, i_ = 9, 1.5, 2
assert r_ * i_ == 3 and e_ + r_ * i_ == 12 and e_ / 12 == 0.75
assert 12 / r_ == 8 and 8 / i_ == 4 and (r_ * 8 ** 2) / (r_ * i_ ** 2) == 16 and r_ * 64 == 96 and r_ * 4 == 6
assert 2 * 1.5 == 3 and 3 * 1.5 == 4.5 and 4.5 - 1.5 == 3 and 4 * 1.5 == 6
assert (24 - 12) / (1 + 2) == 4 and 24 - 1 * 4 == 20 == 12 + 2 * 4
assert abs(4 * 0.1 - 0.4) < 1e-12 and abs(6 / (2.6 + 0.4) - 2) < 1e-12


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


def receptor(c, t, t0, A, B, rot_e="ε′", rot_r="r′", calor=None, tr=None, polos=True):
    """receptor na horizontal, a corrente entrando por A (polo +) e saindo por B (polo −): motor (ε′) e r′ numa caixa tracejada"""
    tr = t0 if tr is None else tr
    y = A[1]
    xm = lerp(A[0], B[0], 0.42)
    xc = lerp(A[0], B[0], 0.25)
    E.foco(c, t, t0, 0.5, lambda a: caixa_tracejada(c, A[0] + 40, y - 120, B[0] - A[0] - 80, 240, a))

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


def pilha_desenho(c, cx, cy, w, h, a=1.0, rot="1,5 V", vira=False, cor_corpo="#2A2A33"):
    """pilha comum deitada: corpo escuro, faixa laranja, polo + à direita (vira=True: polo + à esquerda)"""
    if a <= 0:
        return
    c.save()
    if vira:
        c.translate(2 * cx, 0); c.scale(-1, 1)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h * 0.18, cor_corpo, a, shadow=True)
    M.rrect(c, cx + w * 0.12, cy - h / 2, w * 0.38, h, h * 0.18, E.COR, a)
    M.rrect(c, cx + w / 2 - 6, cy - h * 0.17, h * 0.22, h * 0.34, 6, "#B9BCC4", a)
    c.restore()
    s = -1 if vira else 1
    centro(c, rot, cx - s * w * 0.15, cy + h * 0.16, h * 0.4, "g", BR, a)
    centro(c, "+", cx + s * w * 0.31, cy + h * 0.17, h * 0.45, "g", BR, a)


def ventilador(c, cx, cy, r, giro, a=1.0, calor=0.0):
    """ventilador de mesa: grade, três pás girando (giro em graus), haste e base"""
    if a <= 0:
        return
    M.rrect(c, cx - 14, cy, 28, r * 1.5, 10, "#8C8C96", a)
    M.rrect(c, cx - r * 0.75, cy + r * 1.45, r * 1.5, 34, 16, "#5E5E68", a)
    if calor > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 0.9, [M.hexc(CALOR, 0.75 * calor * a), M.hexc(CALOR, 0)], [0, 1]))
        c.drawCircle(cx, cy, r * 0.9, g)
    for k in range(3):
        g_ = math.radians(giro + 120 * k)
        p = skia.Path()
        p.moveTo(cx, cy)
        p.quadTo(cx + math.cos(g_ - 0.55) * r * 0.75, cy + math.sin(g_ - 0.55) * r * 0.75, cx + math.cos(g_) * r * 0.88, cy + math.sin(g_) * r * 0.88)
        p.quadTo(cx + math.cos(g_ + 0.35) * r * 0.55, cy + math.sin(g_ + 0.35) * r * 0.55, cx, cy)
        c.drawPath(p, M.paint(E.COR, a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=5))
    for k in range(8):
        g_ = math.radians(22.5 * k)
        M.line(c, cx + math.cos(g_) * r * 0.2, cy + math.sin(g_) * r * 0.2, cx + math.cos(g_) * r, cy + math.sin(g_) * r, TINTA2, a * 0.5, 2)
    c.drawCircle(cx, cy, r * 0.16, M.paint(TINTA, a))


def celular(c, cx, cy, h, carga, a=1.0):
    """celular com a bateria enchendo (carga de 0 a 1)"""
    if a <= 0:
        return
    w = h * 0.52
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#2A2A33", a, shadow=True)
    M.rrect(c, cx - w / 2 + 14, cy - h / 2 + 30, w - 28, h - 60, 12, "#F4F4F0", a)
    bw, bh = w * 0.5, h * 0.18
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - bw / 2, cy - bh / 2, bw, bh), 8, 8), M.paint(TINTA, a, stroke=5))
    M.rrect(c, cx - bw / 2 + 6, cy - bh / 2 + 6, (bw - 12) * carga, bh - 12, 4, CERTO, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        trava = C["s01.a"] + 0.4
        vol = C["s01.d"]
        if t < trava:
            giro = t * 900
        elif t < vol:
            giro = trava * 900 + 200 * (1 - math.exp(-(t - trava) * 4))
        else:
            giro = trava * 900 + 200 + (t - vol) * 900 * min(1, (t - vol) / 0.8)
        cal = ep(t, C["s01.b"], 0.8) * (1 - ep(t, vol, 0.6))
        E.foco(c, t, C["s01"], 0.6, lambda a: ventilador(c, 1440, 420, 250, giro, a, cal))
        E.frase(c, t, C["s01.a"], ps("hélice", "i", 84) + [("travada", "g", 84, ERRADO)], XE, 280, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("o motor", "i", 76) + [("esquenta", "g", 76, CALOR)], XE, 430, passo=0.14)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "pode queimar", XE + 230, 560, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s01.d"], [("girando,", "g", 76, COR)] + ps("o motor", "i", 76), XE, 760, passo=0.14)
        E.frase(c, t, C["s01.d"] + 1.0, ps("segura a corrente", "g", 76), XE, 870, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "o motor", 1.4), ("s02.b", "várias pilhas juntas", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "no gerador real", "U = ε − r · i"),
                              ("s03.c", "lei de Pouillet", "i = f{ε}{soma das resistências}")))


# ---------------- receptor ----------------
def b_receptor(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("o gerador", "i", 74) + [("entrega", "g", 70)], XE, 230, passo=0.12)
        E.frase(c, t, C["s04.a"], ps("o", "i", 100) + [("receptor", "g", 100, COR)] + ps("recebe", "i", 100), XE, 400, passo=0.14)
        E.frase(c, t, C["s04.b"], ps("e transforma em outra:", "i", 64) + [("não", "g", 62), ("só", "g", 62), ("calor", "g", 62)], XE, 520, passo=0.1)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: ventilador(c, 620, 750, 130, t * 500, a))
        E.foco(c, t, C["s04.c"] + 0.3, 0.4, lambda a: centro(c, "movimento", 620, 1010, 52, "g", TINTA, a))
        E.foco(c, t, C["s04.d"], 0.5, lambda a: celular(c, 1280, 800, 300, ep(t, C["s04.d"] + 0.3, 2.5), a))
        E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: centro(c, "energia química", 1280, 1010, 52, "g", TINTA, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    A, B = (560, 300), (1360, 300)
    F.fio(c, t, C["s05"], [(A[0] - 200, A[1]), A])
    F.fio(c, t, C["s05"], [B, (B[0] + 200, B[1])])
    receptor(c, t, C["s05"], A, B, "ε′", "r′", tr=C["s05.c"], calor=C["s05.d"])
    F.corrente(c, t, C["s05"] + 0.4, [(A[0] - 200, A[1] - 150), (B[0] + 200, B[1] - 150)], fecha=False, espaco=170)

    def s05():
        E.frase(c, t, C["s05.a"], [("ε′", "g", 70, COR)] + ps("força contraeletromotriz", "g", 60), XE, 560, passo=0.12)
        E.frase(c, t, C["s05.a"] + 1.4, ps("a parte que vira trabalho útil", "i", 56, TINTA2), XE, 640, passo=0.1)
        E.frase(c, t, C["s05.c"], [("r′", "g", 70, CALOR)] + ps("resistência interna:", "i", 62) + [("calor", "g", 60, CALOR)], XE, 790, passo=0.12)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"], ps("precisa receber", "i", 64) + [("mais", "g", 62, COR)] + ps("que", "i", 64) + [("ε′", "g", 62, COR)], XE, 560, passo=0.1)
    E.formula_em(c, t, C["s06.b"], "U = ε′ + r′ · i", XE, 720, 110, "g", TINTA)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (E.escreve(c, "gerador:", XE, 890, 52, "i", TINTA2, a), E.formula(c, "U = ε − r · i", XE + 230, 890, 56, "g", TINTA, a),
                                             E.escreve(c, "sai menos", XE + 640, 890, 52, "i", TINTA2, a)))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: (E.escreve(c, "receptor:", XE, 990, 52, "i", TINTA2, a), E.formula(c, "U = ε′ + r′ · i", XE + 230, 990, 56, "g", COR, a),
                                             E.escreve(c, "precisa entrar mais", XE + 690, 990, 52, "i", TINTA2, a)))


# ---------------- o motor ----------------
def b_motor(c, t, C, b):
    A, B = (560, 290), (1360, 290)
    if t < C["s09"]:
        F.fio(c, t, C["s07.a"], [(A[0] - 200, A[1]), A])
        F.fio(c, t, C["s07.a"], [B, (B[0] + 200, B[1])])
        receptor(c, t, C["s07.a"], A, B, "9 V", "1,5 Ω", calor=C["s07.c"])
        F.corrente(c, t, C["s07.b"], [(A[0] - 200, A[1] - 150), (B[0] + 200, B[1] - 150)], fecha=False, espaco=170)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: F.medida(c, 2, "A", B[0] + 230, A[1] - 130, 70, TINTA, a))

        def s07():
            E.frase(c, t, C["s07"], [("exemplo", "i", 74, COR)], XE, 150)
            E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "perda: 1,5 × 2 = 3 V", XE, 600, 76, "g", CALOR, a))
            E.foco(c, t, C["s07.d"], 0.5, lambda a: E.formula(c, "U = 9 + 3", XE, 760, 90, "g", TINTA, a))
            bola_txt(c, t, C["s07.e"], "12 V", 900, 730, 110, 66)
        E.saida(c, t, C["s08"] - 0.1, s07)
        if t >= C["s08"]:
            E.foco(c, t, C["s08.a"], 0.5, lambda a: E.formula(c, "rendimento =", XE, 700, 84, "g", TINTA, a))
            E.formula_em(c, t, C["s08.b"], "f{ε′}{U} = f{9}{12} =", XE + 560, 700, 96, "g", TINTA)
            bola_txt(c, t, C["s08.c"], "75 %", XE + 1300, 670, 110, 68)
        return
    # s09: o ventilador travado
    E.frase(c, t, C["s09"], ps("e o ventilador", "i", 74) + [("travado?", "g", 72, ERRADO)], XE, 200, passo=0.12)
    E.foco(c, t, C["s09"] + 0.4, 0.6, lambda a: ventilador(c, 1520, 420, 210, 30, a, ep(t, C["s09.c"], 1.0)))
    E.frase(c, t, C["s09.a"], ps("sem girar:", "i", 66), XE, 360)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "ε′ = 0", XE + 330, 360, 80, "g", ERRADO, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "i = f{12}{1,5} =", XE, 580, 90, "g", TINTA, a))
    bola_txt(c, t, C["s09.d"], "8 A", XE + 600, 550, 100, 68, ERRADO)
    E.foco(c, t, C["s09.d"] + 0.8, 0.4, lambda a: E.pilula(c, "4 × a corrente", XE + 950, 550, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "calor: r′ · i^2", XE, 850, 80, "g", CALOR, a))
    E.foco(c, t, C["s09.e"] + 1.0, 0.5, lambda a: E.pilula(c, "16 × mais calor", XE + 820, 825, 54, "g", fundo=ERRADO, a=a))


# ---------------- pilhas em série ----------------
def b_pilhas(c, t, C, b):
    E.frase(c, t, C["s10"], ps("agora, as", "i", 80) + [("pilhas", "g", 80, COR)], XE, 200, passo=0.14)
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], [("em", "i", 70), ("série:", "g", 70, COR)] + ps("o + encosta no −", "g", 60, TINTA2), XE, 340, passo=0.12)
            for k in range(2):
                E.foco(c, t, C["s10.a"] + 0.4 * k, 0.5, lambda a, k=k: pilha_desenho(c, 760 + k * 470, 520, 460, 150, a))
            if t >= C["s10.a"] + 0.8:
                q = ep(t, C["s10.a"] + 0.8, 0.4)
                c.drawCircle(995, 520, 50 + 6 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
            E.frase(c, t, C["s10.b"], [("ε", "g", 74, COR)] + ps("somam:", "i", 74), XE, 760, passo=0.12)
            E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "1,5 + 1,5 =", XE + 400, 760, 80, "g", TINTA, a))
            bola_txt(c, t, C["s10.c"] + 0.8, "3 V", XE + 1010, 735, 90, 64)
            E.frase(c, t, C["s10.d"], [("r", "g", 70, CALOR)] + ps("também somam: estão em série", "i", 64), XE, 930, passo=0.12)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], ps("uma pilha", "i", 70) + [("invertida", "g", 70, ERRADO)] + [("subtrai", "g", 70)], XE, 340, passo=0.12)
    for k in range(4):
        vira = k == 2
        E.foco(c, t, C["s11.a"] + 0.2 * k, 0.5, lambda a, k=k, vira=vira: pilha_desenho(c, 480 + k * 330, 540, 320, 120, a, vira=vira,
                                                                                    cor_corpo="#6B1F22" if vira and t >= C["s11.b"] else "#2A2A33"))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "1,5 + 1,5 − 1,5 + 1,5 = 3 V", XE, 760, 76, "g", TINTA, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.escreve(c, "6 V", XE + 1180, 760, 76, "g", ERRADO, a))
    if t >= C["s11.c"] + 0.4:
        E.risco(c, XE + 1170, 780, XE + 1320, 700, t, C["s11.c"] + 0.4, largura=10)
    E.frase(c, t, C["s11.c"], ps("três volts,", "g", 66, COR) + ps("em vez de seis", "i", 66), XE, 900, passo=0.12)


# ---------------- pilhas em paralelo ----------------
def b_paralelo(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("em", "i", 74), ("paralelo:", "g", 74, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s12.a"] + 0.8, ps("+ com +, − com −", "g", 60, TINTA2), XE, 320, passo=0.12)
    xs, w = 1340, 340
    for k in range(3):
        y = 330 + k * 200
        E.foco(c, t, C["s12.a"] + 0.3 * k, 0.5, lambda a, y=y: pilha_desenho(c, xs, y, w, 120, a))
    F.fio(c, t, C["s12.a"] + 1.0, [(xs - w / 2, 330), (xs - w / 2 - 110, 330), (xs - w / 2 - 110, 730), (xs - w / 2, 730)])
    F.fio(c, t, C["s12.a"] + 1.0, [(xs - w / 2 - 110, 530), (xs - w / 2, 530)])
    F.fio(c, t, C["s12.a"] + 1.0, [(xs + w / 2 + 10, 330), (xs + w / 2 + 120, 330), (xs + w / 2 + 120, 730), (xs + w / 2 + 10, 730)])
    F.fio(c, t, C["s12.a"] + 1.0, [(xs + w / 2 + 120, 530), (xs + w / 2 + 10, 530)])
    E.frase(c, t, C["s12.b"], [("ε", "g", 70, COR)] + ps("não soma:", "i", 70), XE, 470, passo=0.12)
    bola_txt(c, t, C["s12.c"], "1,5 V", XE + 560, 445, 95, 54)
    E.frase(c, t, C["s12.d"], ps("muda a", "i", 64) + [("r", "g", 64, CALOR)] + ps("interna:", "i", 64), XE, 650, passo=0.12)
    E.formula_em(c, t, C["s12.e"], "r do conjunto = f{r}{n}", XE, 790, 70, "g", TINTA)
    E.frase(c, t, C["s12.f"], ps("cada uma dá uma parte da corrente:", "i", 52) + [("dura", "g", 50, COR), ("mais", "g", 50, COR)], XE, 960, passo=0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s13.a"], ps("somar", "i", 76) + [("ε", "g", 76, COR)] + ps("em paralelo", "i", 76), XE, 360, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "3 pilhas em paralelo = 4,5 V ?", XE, 540, 76, "g", ERRADO, a))
    if t >= C["s13.c"]:
        E.risco(c, XE - 10, 550, XE + 1150, 470, t, C["s13.c"], largura=12)
    bola_txt(c, t, C["s13.c"], "1,5 V", XE + 200, 740, 105, 56, CERTO)
    E.frase(c, t, C["s13.d"], ps("só a", "i", 80) + [("série", "g", 80, COR), ("soma", "g", 80)], XE + 420, 770, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("o atalho:", "i", 72, CLARO) + ps("gerador e motor", "g", 68, BR), W / 2, 200, "center", 0.12)
        E.frase(c, t, C["s14.a"], ps("bateria mais forte:", "i", 62, CLARO) + [("ε′", "g", 62, BR)] + ps("entra subtraindo", "i", 62, CLARO),
                W / 2, 380, "center", 0.1)
        E.formula_em(c, t, C["s14.b"], "i = f{ε − ε′}{soma de todas as resistências}", W / 2, 640, 96, "g", BR, "center")
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "bateria:", 260, 240, 56, "i", CLARO, a), E.formula(c, "24 V, 1 Ω", 520, 240, 64, "g", BR, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "motor:", 1020, 240, 56, "i", CLARO, a), E.formula(c, "12 V, 2 Ω", 1230, 240, 64, "g", BR, a)))
    E.formula_em(c, t, C["s15.c"], "i = f{24 − 12}{1 + 2} = f{12}{3} =", 260, 480, 96, "g", BR)
    bola_txt(c, t, C["s15.d"], "4 A", 1380, 450, 100, 68)
    E.frase(c, t, C["s15.e"], ps("o motor empurra", "i", 60, CLARO) + [("contra", "g", 60, BR)], W / 2, 720, "center", 0.12)
    E.frase(c, t, C["s15.f"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("ramos em paralelo, Kirchhoff (outra aula)", "i", 60, CLARO),
            W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("4", "g", 64)] + ps("pilhas de", "i", 64) + [("1,5", "g", 64), ("V", "b", 48, F.UNID), ("e", "i", 64), ("0,1", "g", 64), ("Ω", "b", 48, F.UNID)],
            XE, 340, passo=0.1)
    E.frase(c, t, C["s16.b"], [("em", "i", 64), ("série", "g", 64, COR)] + ps("com uma lâmpada de", "i", 64) + [("2,6", "g", 64), ("Ω", "b", 48, F.UNID)],
            XE, 440, passo=0.1)
    E.frase(c, t, C["s16.d"], [("ε", "g", 66, COR)] + ps("do conjunto?", "i", 66), XE, 600, passo=0.12)
    E.frase(c, t, C["s16.e"], ps("corrente?", "g", 66), XE + 560, 600, passo=0.12)
    E.frase(c, t, C["s16.f"], ps("e se fossem em", "i", 66) + [("paralelo?", "g", 66, COR)], XE, 720, passo=0.12)
    if t < C["s17"]:
        for k in range(4):
            E.foco(c, t, C["s16.a"] + 0.2 * k, 0.5, lambda a, k=k: pilha_desenho(c, 520 + k * 290, 900, 280, 100, a))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18.a"], [("em", "i", 72), ("série,", "g", 72, COR)] + ps("tudo soma", "i", 72), XE, 200, passo=0.12)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "ε = 4 × 1,5 = 6 V", XE, 340, 76, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "r = 4 × 0,1 = 0,4 Ω", XE, 460, 76, "g", TINTA, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "i = f{6}{2,6 + 0,4}", XE, 650, 90, "g", TINTA, a))
    E.formula_em(c, t, C["s18.e"], "= f{6}{3} =", XE + 470, 650, 90, "g", TINTA)
    bola_txt(c, t, C["s18.f"], "2 A", XE + 900, 620, 95, 66, CERTO)
    E.frase(c, t, C["s18.g"], [("em", "i", 66), ("paralelo:", "g", 66, COR), ("ε", "g", 66, COR)] + ps("não soma", "i", 66), XE, 900, passo=0.12)
    bola_txt(c, t, C["s18.h"], "1,5 V", XE + 900, 875, 95, 54, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r_():
        resumo(c, t, C, "s19", (("s19.a", [("receptor:", "g", 66), ("U = ε′ + r′ · i", "g", 70, COR)]),
                               ("s19.b", [("série:", "g", 66), ("soma", "i", 70), ("tudo", "g", 66, COR)]),
                               ("s19.c", [("paralelo:", "g", 66), ("ε", "g", 66, COR), ("fica,", "i", 70), ("r", "g", 66, CALOR), ("se", "i", 70), ("divide", "i", 70)])))
    E.saida(c, t, C["s20"] - 0.1, r_)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("praticar", "g", 100, COR)], XE, 400)
    for k, s in enumerate(("conta de luz", "chuveiro", "baterias", "motores")):
        E.foco(c, t, C["s20.a"] + 0.6 + 0.3 * k, 0.4, lambda a, k=k, s=s: E.pilula(c, s, XE + 160 + (k % 2) * 440, 560 + (k // 2) * 130, 50, "g",
                                                                                 fundo=TINTA if k % 2 else E.COR, a=a))
    inscreva(c, t, C["s20.b"], C["s20.c"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, receptor=b_receptor, motor=b_motor, pilhas=b_pilhas, paralelo=b_paralelo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
