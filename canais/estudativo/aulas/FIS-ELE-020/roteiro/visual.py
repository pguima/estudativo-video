"""Visual — Estudativo · FIS-ELE-020: gerador real e força eletromotriz. Primeira aula do módulo Geradores e receptores.

Segue a LINGUAGEM VISUAL DA FÍSICA (docstring do visual.py da FIS-CIN-001) e a da ELETRICIDADE (docstring do visual.py da
FIS-ELE-001). Acrescenta, para o módulo GERADORES E RECEPTORES (as aulas FIS-ELE-021 a 026 copiam daqui):
- GERADOR REAL = `gerador_real`: F.pilha (a fem ε, placa longa = +) e F.resistor (a resistência interna r) dentro de uma
  caixa tracejada em cinza; os polos (bolinhas) ficam na borda da caixa, com "−" e "+". A perda r·i acende em laranja
  (calor) quando a fala chega nela.
- Letras: ε (épsilon), r (interna, minúscula), R (de fora, maiúscula), U (tensão nos polos), i (corrente). Grego só na fonte
  pesada. Tensão útil U em tinta; ε em laranja (é a grandeza do módulo); a perda r·i em vermelho-calor (ERRADO só no erro).
- GRÁFICO U × i: F.grafico com "i (A)" e "U (V)"; a reta do gerador em laranja, ε marcado no eixo da tensão e a corrente de
  curto no eixo da corrente.
- POTÊNCIAS: barra `barras_pot` — total em tinta, útil em laranja, perdida em cinza-calor, sempre com o valor em watt.
- Rendimento como porcentagem na esfera (bola_txt).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-020_gerador_real_forca_eletromotriz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fem", "interna", "grafico", "rendimento", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CALOR = "#D9480F"

# todas as contas da aula
eps, r, i = 12, 0.5, 6
U = eps - r * i
assert r * i == 3 and U == 9 and eps / r == 24
assert eps * i == 72 and U * i == 54 and r * i ** 2 == 18 and 72 == 54 + 18
assert U * i / (eps * i) == 0.75 and U / eps == 0.75 and 54 / 72 == 0.75
assert abs(12 / 24 - 0.5) < 1e-12
assert 10 / 5 == 2 and 10 - 2 * 1 == 8 and 8 / 10 == 0.8


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


def pilha_desenho(c, cx, cy, w, h, a=1.0, rot="1,5 V"):
    """pilha comum deitada: corpo escuro, faixa laranja, polo + à direita"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h * 0.18, "#2A2A33", a, shadow=True)
    M.rrect(c, cx + w * 0.12, cy - h / 2, w * 0.38, h, h * 0.18, E.COR, a)
    M.rrect(c, cx + w / 2 - 6, cy - h * 0.17, h * 0.22, h * 0.34, 6, "#B9BCC4", a)
    centro(c, rot, cx - w * 0.15, cy + h * 0.16, h * 0.42, "g", BR, a)
    centro(c, "+", cx + w * 0.31, cy + h * 0.17, h * 0.45, "g", BR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        px, py = 1380, 330
        E.foco(c, t, C["s01.a"], 0.5, lambda a: pilha_desenho(c, px, py, 460, 170, a))
        E.frase(c, t, C["s01.a"], ps("pilha nova:", "i", 84), XE, 300)
        E.foco(c, t, C["s01.a"] + 0.6, 0.5, lambda a: F.medida(c, "1,5", "V", XE, 440, 130, COR, a))
        # o brinquedo puxa corrente: a tensão nos polos cai
        if t >= C["s01.b"]:
            F.fio(c, t, C["s01.b"], [(px - 240, py), (px - 330, py), (px - 330, 760), (1240, 760)])
            F.fio(c, t, C["s01.b"], [(px + 240, py), (1800, py), (1800, 760), (1640, 760)])
            E.foco(c, t, C["s01.b"] + 0.5, 0.5, lambda a: F.carrinho(c, 1440, 800, 300, a=a))
            F.corrente(c, t, C["s01.b"] + 0.9, [(px + 260, py - 50), (1750, py - 50), (1750, 700)], fecha=False, espaco=160)
        E.frase(c, t, C["s01.b"], ps("brinquedo que puxa", "i", 66) + [("muita", "g", 62), ("corrente", "g", 62)], XE, 600, passo=0.12)
        q = ease_io(prog(t, C["s01.c"], 1.2))
        if t >= C["s01.c"] - 0.2:
            E.foco(c, t, C["s01.c"] - 0.2, 0.4, lambda a: (E.escreve(c, "tensão nos polos", XE, 760, 56, "i", TINTA2, a),
                                                           M.rrect(c, XE, 800, 560, 50, 14, FIO, a),
                                                           M.rrect(c, XE, 800, 560 * (1 - 0.3 * q), 50, 14, E.COR, a)))
            E.foco(c, t, C["s01.c"] + 0.6, 0.4, lambda a: E.escreve(c, "cai", XE + 600, 845, 64, "g", ERRADO, a))
        E.frase(c, t, C["s01.d"], ps("parte se perde", "i", 72) + [("dentro", "g", 70, COR)], XE, 980, passo=0.12)
        if t >= C["s01.e"]:
            q2 = ep(t, C["s01.e"], 0.6)
            g = skia.Paint(AntiAlias=True)
            g.setShader(skia.GradientShader.MakeRadial(skia.Point(px, py), 330, [M.hexc(CALOR, 0.5 * q2), M.hexc(CALOR, 0)], [0, 1]))
            c.drawCircle(px, py, 330, g)
            pilha_desenho(c, px, py, 460, 170)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a perda dentro da pilha", 1.4), ("s02.b", "o gráfico do gerador", 0), ("s02.c", "o rendimento", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "tensão no resistor", "U = R · i"),
                              ("s03.c", "potência elétrica", "P = U · i"),
                              ("s03.d", "rendimento", "f{potência útil}{potência total}")))


def rot_eps(c, t, t0, P, v, s):
    """rótulo do ponto em que a reta corta o eixo da tensão, à direita do eixo e acima da reta"""
    E.foco(c, t, t0, 0.4, lambda a: E.formula(c, s, P.ox + 30, P.y(v) - 22, 48, "g", COR, a))


# ---------------- gerador e fem ----------------
def turbina(c, cx, cy, r_, giro, a=1.0):
    if a <= 0:
        return
    for k in range(3):
        g = math.radians(giro + 120 * k)
        p = skia.Path()
        p.moveTo(cx, cy)
        p.quadTo(cx + math.cos(g - 0.5) * r_ * 0.7, cy + math.sin(g - 0.5) * r_ * 0.7, cx + math.cos(g) * r_, cy + math.sin(g) * r_)
        p.quadTo(cx + math.cos(g + 0.3) * r_ * 0.5, cy + math.sin(g + 0.3) * r_ * 0.5, cx, cy)
        c.drawPath(p, M.paint(TINTA2, a))
    c.drawCircle(cx, cy, r_ * 0.16, M.paint(TINTA, a))


def b_fem(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("gerador", "g", 100, COR)], XE, 240)
        E.frase(c, t, C["s04.a"] + 0.7, ps("outra energia", "i", 64) + [("→", "g", 60, TINTA2), ("elétrica", "g", 62)], XE, 340, passo=0.12)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: pilha_desenho(c, 1180, 300, 330, 120, a, ""))
        E.foco(c, t, C["s04.b"] + 0.3, 0.4, lambda a: centro(c, "reação química", 1180, 430, 46, "i", TINTA2, a))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: turbina(c, 1620, 300, 120, t * 140, a))
        E.foco(c, t, C["s04.c"] + 0.3, 0.4, lambda a: centro(c, "giro da turbina", 1620, 480, 46, "i", TINTA2, a))
        E.frase(c, t, C["s04.d"], ps("a tensão que ele cria:", "i", 66), XE, 600, passo=0.12)
        E.frase(c, t, C["s04.d"] + 1.2, [("força", "g", 96), ("eletromotriz", "g", 96, COR)], XE, 740, passo=0.3)
        E.foco(c, t, C["s04.e"], 0.5, lambda a: E.escreve(c, "ε", XE, 960, 170, "g", COR, a))
        E.frase(c, t, C["s04.e"] + 0.6, ps("épsilon, em", "i", 64) + [("volt", "g", 60)], XE + 140, 930, passo=0.12)
        E.foco(c, t, C["s04.e"] + 1.2, 0.4, lambda a: E.formula(c, "(V)", XE + 640, 930, 60, "b", F.UNID, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], ps("não é uma", "i", 90) + [("força", "g", 86)], XE, 260, passo=0.14)
    if t >= C["s05.a"] + 1.2:
        x0 = XE + E.larg("não é uma", "i", 90) + 20
        E.risco(c, x0, 280, x0 + E.larg("força", "g", 86) + 20, 200, t, C["s05.a"] + 1.2, largura=12)
    E.frase(c, t, C["s05.b"], ps("energia por", "i", 72) + [("coulomb", "g", 70, COR)], XE, 430, passo=0.12)
    E.formula_em(c, t, C["s05.b"] + 1.0, "ε = f{energia}{carga}", XE, 640, 100, "g", TINTA)
    E.formula_em(c, t, C["s05.b"] + 2.0, "f{J}{C} = V", XE + 900, 640, 90, "b", F.UNID)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: pilha_desenho(c, 560, 880, 400, 140, a))
    E.foco(c, t, C["s05.c"] + 0.6, 0.5, lambda a: (F.medida(c, "1,5", "J", 960, 900, 90, COR, a), E.escreve(c, "a cada coulomb", 1200, 900, 64, "i", TINTA, a)))


# ---------------- resistência interna ----------------
def b_interna(c, t, C, b):
    A, B = (560, 380), (1360, 380)
    if t < C["s08"]:
        def s0607():
            E.frase(c, t, C["s06"] + 0.2, [("dentro", "i", 74), ("do", "i", 74), ("gerador", "g", 70, COR)], XE, 140)
            F.fio(c, t, C["s06.a"], [(A[0] - 200, A[1]), A])
            F.fio(c, t, C["s06.a"], [B, (B[0] + 200, B[1])])
            gerador_real(c, t, C["s06.a"], A, B, "ε", "r", tr=C["s06.b"], calor=C["s06.e"])
            F.corrente(c, t, C["s06.a"] + 0.4, [(A[0] - 200, A[1] - 150), (B[0] + 200, B[1] - 150)], fecha=False, espaco=170)
            E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "resistência interna", 1140, 560, 42, "g", fundo=TINTA, a=a))
            E.foco(c, t, C["s06.d"], 0.5, lambda a: (E.formula(c, "perde r · i", 1000, 680, 62, "g", CALOR, a)))
            E.foco(c, t, C["s06.e"] + 0.3, 0.4, lambda a: E.escreve(c, "vira calor", 1340, 680, 56, "i", CALOR, a))
            F.formula_legenda(c, t, C["s07.a"], "U = ε − r · i", [("U", "tensão útil, nos polos", "V"), ("ε", "força eletromotriz", "V"),
                                                                  ("r", "resistência interna", "Ω"), ("i", "corrente", "A")],
                              XE, 720, 120, tl=[C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]], size_l=44, dy=60)
        E.saida(c, t, C["s08"] - 0.1, s0607)
        return
    # s08 e s09: o exemplo
    def s08():
        E.frase(c, t, C["s08"], [("exemplo", "i", 74, COR)], XE, 160)
        F.fio(c, t, C["s08.a"], [(A[0] - 200, A[1]), A])
        F.fio(c, t, C["s08.a"], [B, (B[0] + 200, B[1])])
        gerador_real(c, t, C["s08.a"], A, B, "12 V", "0,5 Ω", calor=C["s08.c"])
        F.corrente(c, t, C["s08.b"], [(A[0] - 200, A[1] - 150), (B[0] + 200, B[1] - 150)], fecha=False, espaco=170)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: F.medida(c, 6, "A", B[0] + 230, A[1] - 130, 70, TINTA, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "perda: 0,5 × 6 = 3 V", XE, 620, 80, "g", CALOR, a))
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.formula(c, "U = 12 − 3", XE, 790, 90, "g", TINTA, a))
        bola_txt(c, t, C["s08.e"], "9 V", 1000, 760, 110, 74)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], ps("e sem", "i", 84) + [("corrente", "g", 80, COR)] + ps("nenhuma?", "i", 84), XE, 220, passo=0.12)
    E.foco(c, t, C["s09.a"] + 0.4, 0.5, lambda a: gerador_real(c, 0, -9, A, B, "ε", "r"))
    E.formula_em(c, t, C["s09.b"], "i = 0", XE, 600, 110, "g", TINTA)
    E.formula_em(c, t, C["s09.b"] + 1.4, "→  U = ε", XE + 400, 600, 110, "g", COR)
    E.frase(c, t, C["s09.c"], ps("a força eletromotriz é a tensão", "i", 62) + ps("sem nada ligado", "g", 60), XE, 820, passo=0.1)


# ---------------- gráfico U × i ----------------
def b_grafico(c, t, C, b):
    P = F.grafico(c, t, C["s10.a"], 1000, 200, 760, 620, 0, 26, 0, 14, "i (A)", "U (V)", passo=4, passo_y=2,
                  marcas_x=[4, 8, 12, 16, 20, 24], marcas_y=[2, 4, 6, 8, 10, 12])
    E.frase(c, t, C["s10.a"], ps("tensão pela corrente", "i", 70), XE, 230, passo=0.12)
    E.formula_em(c, t, C["s10.b"], "U = 12 − 0,5 · i", XE, 380, 80, "g", TINTA)
    E.frase(c, t, C["s10.b"] + 1.6, ps("função afim:", "i", 60) + [("reta", "g", 58, COR)], XE, 480, passo=0.12)
    E.curva(c, t, C["s10.c"], P, lambda x: 12 - 0.5 * x, 0, 24, d=1.0)
    E.ponto(c, t, C["s10.d"], P, 0, 12, None)
    rot_eps(c, t, C["s10.d"] + 0.2, P, 12, "ε = 12 V")
    if t >= C["s10.e"]:  # degrau: 4 A a mais, 2 V a menos (a cada 1 A, meio volt)
        q = ep(t, C["s10.e"], 0.5)
        M.line(c, P.x(4), P.y(10), P.x(8), P.y(10), TINTA2, q, 4, dash=E.TRACO)
        M.line(c, P.x(8), P.y(10), P.x(8), P.y(8), TINTA2, q, 4, dash=E.TRACO)
    E.frase(c, t, C["s10.e"], ps("cada 1 A a mais:", "i", 56) + [("−0,5", "g", 54, COR), ("V", "b", 42, F.UNID)], XE, 600, passo=0.1)
    E.frase(c, t, C["s11.a"], [("U", "g", 60, COR), ("=", "g", 60, TINTA2), ("0", "g", 60)] + ps("no eixo da corrente", "i", 60), XE, 720, passo=0.12)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "12 ÷ 0,5 = 12 × 2 = 24 A", XE, 820, 52, "b", TINTA, a))
    E.ponto(c, t, C["s11.b"] + 1.0, P, 24, 0, None)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "curto-circuito: 24 A", P.x(15), P.oy + 120, 40, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s11.d"], ps("polos ligados por um fio", "i", 50, TINTA2), XE, 920, passo=0.1)
    E.frase(c, t, C["s11.e"], ps("toda a tensão se perde", "g", 48, CALOR) + [("dentro", "g", 48, CALOR)], XE, 1000, passo=0.1)


# ---------------- rendimento ----------------
def barras_pot(c, t, itens, x, y0, escala, dy=150):
    """barras horizontais de potência: itens = [(instante, rótulo, watts, cor)]"""
    for k, (ti, rot, wt, cor) in enumerate(itens):
        y = y0 + k * dy
        q = ease_io(prog(t, ti, 0.7))
        if q <= 0:
            continue
        E.foco(c, t, ti, 0.4, lambda a, rot=rot, y=y: E.formula(c, rot, x, y - 20, 48, "b", TINTA2, a))
        M.rrect(c, x, y, wt * escala * q, 70, 16, cor, 1.0)
        E.foco(c, t, ti + 0.5, 0.4, lambda a, wt=wt, y=y: F.medida(c, wt, "W", x + wt * escala + 30, y + 54, 66, TINTA, a))


def b_rendimento(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("e o", "i", 84) + [("rendimento?", "g", 80, COR)], XE, 200, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "total = ε · i = 12 × 6", XE, 330, 56, "b", TINTA2, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "útil = U · i = 9 × 6", XE + 860, 330, 56, "b", TINTA2, a))
    barras_pot(c, t, [(C["s12.b"] + 0.4, "total", 72, TINTA), (C["s12.c"] + 0.4, "útil", 54, E.COR),
                      (C["s12.d"], "vira calor dentro: r · i^2 = 0,5 × 36", 18, CALOR)], XE, 470, 15)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "rendimento = f{54}{72} =", 820, 930, 80, "g", TINTA, a))
    bola_txt(c, t, C["s13.b"], "75 %", 1640, 900, 120, 76)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s14.a"], ps("usar", "i", 74) + [("ε", "g", 74, COR)] + ps("como a tensão nos polos", "i", 74), XE, 350, passo=0.12)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "útil = 12 × 6 = 72 W ?", XE, 520, 84, "g", ERRADO, a))
    if t >= C["s14.c"]:
        E.risco(c, XE - 10, 530, XE + 980, 450, t, C["s14.c"], largura=12)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.escreve(c, "polos:", XE, 680, 70, "i", TINTA, a), F.medida(c, 9, "V", XE + 220, 680, 84, TINTA, a)))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "útil = 9 × 6", XE, 820, 84, "g", TINTA, a))
    bola_txt(c, t, C["s14.d"] + 0.6, "54 W", 1140, 790, 110, 64, CERTO)
    E.foco(c, t, C["s14.e"], 0.5, lambda a: E.pilula(c, "ε nos polos só com i = 0", 1500, 600, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s14.a"] + 0.6, 0.5, lambda a: gerador_real(c, 0, -9, (1180, 230), (1780, 230), "ε", "r", polos=False))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, os", "i", 76, CLARO) + [("atalhos", "g", 76, BR)], W / 2, 180, "center")
        E.formula_em(c, t, C["s15.a"], "rendimento = f{U}{ε}", 380, 420, 110, "g", BR)
        E.formula_em(c, t, C["s15.b"], "= f{U · i}{ε · i}", 1180, 420, 110, "g", CLARO)
        if t >= C["s15.b"] + 0.8:
            wx = 1180 + E.formula(None, "= ", 0, 0, 110, "g", a=0)
            wf = E.formula(None, "f{U · i}{ε · i}", 0, 0, 110, "g", a=0)
            for k, yy in enumerate((330, 470)):
                xx = wx + wf * 0.78
                E.risco(c, xx - 30, yy + 30, xx + 40, yy - 40, t, C["s15.b"] + 0.8 + 0.2 * k, cor=E.COR, largura=8)
        E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "f{9}{12} = 75 %", 380, 760, 100, "g", BR, a))
        E.frase(c, t, C["s15.c"] + 1.6, ps("sem calcular", "i", 64, CLARO) + ps("nenhuma potência", "g", 60, BR), 380, 940, "left", 0.12)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    P = F.grafico(c, t, C["s16"], 1080, 220, 660, 560, 0, 26, 0, 14, "i (A)", "U (V)", passo=4, passo_y=2,
                  marcas_x=[24], marcas_y=[12], escuro=True)
    E.curva(c, t, C["s16"] + 0.3, P, lambda x: 12 - 0.5 * x, 0, 24, d=0.8)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: c.drawCircle(P.x(0), P.y(12), 16, M.paint(E.COR, a)))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: c.drawCircle(P.x(24), P.y(0), 16, M.paint(E.COR, a)))
    E.frase(c, t, C["s16.a"], [("ε:", "g", 70, BR)] + ps("onde a reta corta o eixo", "i", 60, CLARO) + [("U", "g", 60, BR)], XE, 300, passo=0.1)
    E.formula_em(c, t, C["s16.b"], "r = f{ε}{corrente de curto}", XE, 500, 76, "g", BR)
    E.formula_em(c, t, C["s16.c"], "r = f{12}{24} = 0,5 Ω", XE, 720, 84, "g", CLARO)
    E.frase(c, t, C["s16.d"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("pediu potência em watt", "i", 60, CLARO),
            XE, 960, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], ps("o gráfico começa em", "i", 62) + [("10", "g", 62), ("V", "b", 46, F.UNID)], XE, 360, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("toca a corrente em", "i", 62) + [("5", "g", 62), ("A", "b", 46, F.UNID)], XE, 460, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("resistência interna?", "g", 66), XE, 640, passo=0.12)
    E.frase(c, t, C["s17.d"], ps("rendimento com", "i", 66) + [("1", "g", 64, COR), ("A?", "g", 64, COR)], XE, 760, passo=0.12)
    if t < C["s18"]:
        P = F.grafico(c, t, C["s17.a"], 1150, 250, 620, 560, 0, 6, 0, 12, "i (A)", "U (V)", passo=1, passo_y=2,
                      marcas_x=[1, 2, 3, 4, 5], marcas_y=[2, 4, 6, 8, 10])
        E.curva(c, t, C["s17.a"] + 0.5, P, lambda x: 10 - 2 * x, 0, 5, d=1.0)
        E.ponto(c, t, C["s17.a"] + 0.5, P, 0, 10, None)
        E.ponto(c, t, C["s17.b"], P, 5, 0, None)
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = F.grafico(c, t, C["s19"], 1150, 250, 620, 560, 0, 6, 0, 12, "i (A)", "U (V)", passo=1, passo_y=2,
                  marcas_x=[1, 2, 3, 4, 5], marcas_y=[2, 4, 6, 8, 10])
    E.curva(c, t, C["s19"] + 0.3, P, lambda x: 10 - 2 * x, 0, 5, d=0.8)
    E.ponto(c, t, C["s19.a"], P, 0, 10, None)
    rot_eps(c, t, C["s19.a"] + 0.2, P, 10, "ε = 10 V")
    E.ponto(c, t, C["s19.d"], P, 1, 8, "8 V", guias=True)
    E.frase(c, t, C["s19.a"], [("ε", "g", 80, COR), ("=", "g", 80, TINTA2), ("10", "g", 80), ("V", "b", 60, F.UNID)], XE, 240, passo=0.12)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "r = f{10}{5} =", XE, 420, 84, "g", TINTA, a))
    bola_txt(c, t, C["s19.c"], "2 Ω", XE + 560, 400, 95, 64)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.formula(c, "perda: 2 × 1 = 2 V", XE, 620, 66, "g", CALOR, a))
    E.foco(c, t, C["s19.e"], 0.5, lambda a: E.formula(c, "U = 10 − 2 = 8 V", XE, 730, 66, "g", TINTA, a))
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "rendimento = f{8}{10} =", XE, 920, 70, "g", TINTA, a))
    bola_txt(c, t, C["s20.b"], "80 %", XE + 820, 890, 100, 66, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r_():
        resumo(c, t, C, "s21", (("s21.a", [("U = ε − r · i", "g", 72, COR)]),
                               ("s21.b", [("gráfico:", "g", 64), ("começa", "i", 66), ("em", "i", 66), ("ε,", "g", 64, COR), ("acaba", "i", 66),
                                          ("no", "i", 66), ("curto", "g", 64, COR)]),
                               ("s21.c", [("rendimento", "g", 64), ("=", "g", 64, TINTA2), ("U", "g", 64, COR), ("÷", "g", 64, TINTA2), ("ε", "g", 64, COR)])))
    E.saida(c, t, C["s22"] - 0.1, r_)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], ps("a corrente numa fração", "i", 70), XE, 380, passo=0.12)
    E.frase(c, t, C["s22.b"], ps("lei de", "i", 100) + [("Pouillet", "g", 104, COR)], XE, 530, passo=0.14)
    y, yb = 720, 940
    gerador_real(c, t, C["s22"] + 0.6, (300, y), (900, y), "ε", "r", polos=False)
    F.fio(c, t, C["s22"] + 0.8, [(900, y), (1060, y), (1060, yb), (900, yb)])
    F.resistor(c, t, C["s22.a"], (900, yb), (460, yb), "R")
    F.fio(c, t, C["s22"] + 0.8, [(460, yb), (200, yb), (200, y), (300, y)])
    inscreva(c, t, C["s22.c"], C["s22.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fem=b_fem, interna=b_interna, grafico=b_grafico, rendimento=b_rendimento,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
