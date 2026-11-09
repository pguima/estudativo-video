"""Visual — Estudativo · FIS-ELE-006: capacitores.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
placas de metal com +Q (laranja) e −Q (azul), isolante claro entre elas, fios e pilha em tinta (F.fio, F.pilha); a energia
é a ÁREA do triângulo no gráfico U × Q (F.grafico + F.area_graf); a energia é escrita por extenso ("energia"), para não
confundir com o E do campo. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-006_capacitores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("capacitor", "energia", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"
AMAR = "#FFC400"

# todas as contas da aula
assert abs(100e-6 * 300 - 3e-2) < 1e-12 and abs(3e-2 * 300 - 9) < 1e-9 and abs(9 / 2 - 4.5) < 1e-12
assert abs(20e-6 * 100 - 2e-3) < 1e-12 and abs(2e-3 * 100 - 0.2) < 1e-12 and abs(0.2 / 2 - 0.1) < 1e-12
assert abs(100e-6 * 300 ** 2 / 2 - 4.5) < 1e-9 and abs((3e-2) ** 2 / (2 * 100e-6) - 4.5) < 1e-9 and 2 ** 2 == 4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Eletricidade (cópia das da FIS-ELE-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def q(c, x, y, r, s, a=1.0):
    """carga pequena: + laranja, − azul, com o sinal em branco"""
    if a <= 0:
        return
    cor = E.COR if s == "+" else NEG
    c.drawCircle(x + r * 0.08, y + r * 0.16, r, M.paint("#000000", 0.16 * a))
    c.drawCircle(x, y, r, M.paint(cor, a))
    k, lw = r * 0.52, max(3, r * 0.24)
    M.line(c, x - k, y, x + k, y, BR, a, lw)
    if s == "+":
        M.line(c, x, y - k, x, y + k, BR, a, lw)


def esfera_metal(c, cx, cy, R, a=1.0):
    E.bola(c, cx, cy, R, METAL, a)


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita potência de dez)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def _linha(c, partes, x, y, a, align="center"):
    """linha de tipografia mista parada (para a troca)"""
    w, xs = E._arranjo(partes, x, align)
    for p, xx in zip(partes, xs):
        E.escreve(c, p[0], xx, y, p[2], p[1], p[3] if len(p) > 3 else TINTA, a)


def terra(c, x, y, a=1.0, cor=TINTA):
    """símbolo de terra: três traços, o de cima em y"""
    for i, w in enumerate((90, 60, 30)):
        M.line(c, x - w / 2, y + i * 18, x + w / 2, y + i * 18, cor, a, 6)


def promessa(c, t, C, cena, itens, sz=74):
    """tela "até o fim da aula": órbita à direita e itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", sz, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, desenhos):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, cx, cy) desenha à direita da caixa"""
    if len(itens) == 2:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
        E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
        E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    else:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa", "i", 84), XE, 470, passo=0.14)
        E.frase(c, t, C[cena] + 0.6, ps("de uma coisa", "i", 84), XE, 580, passo=0.14)
    x, w = 820, 1000
    y0 = 230 if len(itens) == 2 else 340
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    if len(itens) == 2:
        q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
        E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    else:
        E.cursor(c, x + w - 30, 560, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, dy=190):
    """tela "resumindo": itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 380 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)


def cta(c, t, C, cena):
    """inscreva-se (cue c) e bons estudos (cue d), à direita"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


def questao_relogio(c, t, C, cena_pausa, desenho):
    """lado direito da questão: o desenho até a pausa, depois o relógio"""
    if t < C[cena_pausa]:
        desenho()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1460, cy=440, r=200)



def capacitor(c, t, x1, x2, y0, y1, ta, ti=None, tq=None, tn=None, n=4, a=1.0):
    """placas em x1 e x2 (de y0 a y1); ti = isolante; tq = +Q na esquerda; tn = −Q na direita"""
    q_ = ep(t, ta, 0.5) * a
    if q_ <= 0:
        return
    if ti is not None and t >= ti:
        c.drawRect(skia.Rect.MakeLTRB(x1 + 18, y0, x2 - 18, y1), M.paint("#FFE9A8", 0.7 * ep(t, ti, 0.4) * a))
    M.rrect(c, x1 - 18, y0, 36, y1 - y0, 8, METAL, q_)
    M.rrect(c, x2 - 18, y0, 36, y1 - y0, 8, METAL, q_)
    for i in range(n):
        yy = lerp(y0 + 40, y1 - 40, i / (n - 1))
        if tq is not None:
            q(c, x1 + 2, yy, 20, "+", ep(t, tq + 0.06 * i, 0.3) * a)
        if tn is not None:
            q(c, x2 - 2, yy, 20, "−", ep(t, tn + 0.06 * i, 0.3) * a)


def camera(c, cx, cy, s, a=1.0, flash=0.0):
    if a <= 0:
        return
    M.rrect(c, cx - s, cy - s * 0.6, 2 * s, 1.25 * s, s * 0.15, TINTA, a)
    M.rrect(c, cx - s * 0.6, cy - s * 0.78, s * 0.5, s * 0.22, 6, TINTA, a)
    c.drawCircle(cx, cy, s * 0.42, M.paint("#3A3A44", a))
    c.drawCircle(cx, cy, s * 0.3, M.paint("#1B1B22", a))
    M.rrect(c, cx + s * 0.45, cy - s * 0.5, s * 0.4, s * 0.22, 6, "#EDEDED", a)
    if flash > 0:
        g = skia.Paint(AntiAlias=True)
        fx, fy = cx + s * 0.65, cy - s * 0.4
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(fx, fy), s * 1.6, [M.hexc("#FFF6C8", 0.95 * flash * a), M.hexc("#FFF6C8", 0)], [0, 1]))
        c.drawCircle(fx, fy, s * 1.6, g)


def grafico_uq(c, t, t0, x, y, w, h, tarea=None, tret=None, tri_cor=None):
    """gráfico U × Q com a reta saindo do zero; tarea = triângulo pintado; tret = retângulo tracejado (o erro)"""
    P = F.grafico(c, t, t0, x, y, w, h, 0, 4, 0, 4, eixo_x="", eixo_y="", marcas_x=(), marcas_y=(), grade=False)
    E.curva(c, t, t0 + 0.6, P, lambda v: v * 0.9, 0, 3.6, d=0.8)
    if t >= t0 + 1.2:
        ag = ep(t, t0 + 1.2, 0.4)
        M.line(c, P.x(3.6), P.oy, P.x(3.6), P.y(3.24), TINTA2, ag, 3, dash=E.TRACO)
        M.line(c, P.ox, P.y(3.24), P.x(3.6), P.y(3.24), TINTA2, ag, 3, dash=E.TRACO)
        centro(c, "Q", P.x(3.6), P.oy + 64, 56, "g", COR, ag)
        E.escreve(c, "U", P.ox - 64, P.y(3.24) + 20, 56, "g", COR, ag)
    if tret is not None and t >= tret:
        a = ep(t, tret, 0.4)
        M.line(c, P.x(0), P.y(3.24), P.x(3.6), P.y(3.24), ERRADO, a, 5, dash=E.TRACO)
        M.line(c, P.x(3.6), P.y(0), P.x(3.6), P.y(3.24), ERRADO, a, 5, dash=E.TRACO)
    if tarea is not None:
        F.area_graf(c, t, tarea, P, lambda v: v * 0.9, 0, 3.6, cor=tri_cor)
    return P


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        fl = ep(t, C["s01.a"] + 0.6, 0.15) * (1 - ep(t, C["s01.a"] + 1.0, 0.6))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: camera(c, 1400, 520, 230, a, fl))
        E.frase(c, t, C["s01.a"], ps("o flash acende por", "i", 72), XE, 260, passo=0.12)
        E.foco(c, t, C["s01.a"] + 1.0, 0.5, lambda a: E.formula(c, "< 0,001 s", XE, 420, 110, "g", COR, a))
        E.frase(c, t, C["s01.b"], ps("as pilhas sozinhas:", "i", 66) + [("lentas", "g", 62, ERRADO)], XE, 600, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("quem solta tudo:", "i", 66) + [("o", "i", 66), ("capacitor", "g", 72, COR)], XE, 800, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "C = Q ÷ U", 0.4), ("s02.c", "a energia guardada", 0), ("s02.d", "o flash", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def area(a, x, y):
        M.line(c, x - 130, y + 60, x + 110, y + 60, TINTA, a, 4)
        M.line(c, x - 130, y + 60, x - 130, y - 80, TINTA, a, 4)
        c.drawRect(skia.Rect.MakeLTRB(x - 128, y - 30, x + 60, y + 58), M.paint(E.COR, 0.35 * a))
        M.line(c, x - 130, y - 30, x + 60, y - 30, E.COR, a, 5)
    lembrete(c, t, C, "s03", (("s03.b", "a tensão U, em volt:", "joule por coulomb"), ("s03.c", "gráfico força × deslocamento:", "a área é o trabalho")),
             (lambda a, x, y: E.formula(c, "1 V = 1 J/C", x - 40, y + 20, 52, "g", TINTA, a, "center"), area))


# ---------------- o capacitor ----------------
def b_capacitor(c, t, C, b):
    x1, x2, y0, y1 = 1180, 1520, 260, 700

    def s04():
        E.frase(c, t, C["s04.a"], [("capacitor:", "g", 90, COR)], XE, 250)
        E.frase(c, t, C["s04.a"] + 0.5, ps("duas placas de metal", "i", 66), XE, 360, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("com um isolante no meio", "i", 66), XE, 460, passo=0.12)
        capacitor(c, t, x1, x2, y0, y1, C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"])
        tp = lerp(C["s04.b"], C["s04.c"], 0.5)
        F.fio(c, t, tp, [(x1, y1), (x1, 880), (1290, 880)])
        F.fio(c, t, tp, [(x2, y1), (x2, 880), (1410, 880)])
        F.pilha(c, t, tp + 0.3, (1290, 880), (1410, 880))
        E.frase(c, t, C["s04.c"], [("+Q", "g", 76, COR), ("e", "i", 76), ("−Q", "g", 76, NEG)], XE, 640, passo=0.3)
        if t >= C["s04.e"]:
            for i in range(4):
                yy = lerp(y0 + 70, y1 - 70, i / 3)
                p = ease_io(prog(t, C["s04.e"] + 0.05 * i, 0.6))
                M.line(c, x1 + 40, yy, lerp(x1 + 40, x2 - 40, p), yy, TINTA2, 1.0, 4)
                if p > 0.6:
                    F._cabeca(c, (x1 + x2) / 2 + 11, yy, 1, 0, 20, TINTA2, 1.0)
            E.foco(c, t, C["s04.e"] + 0.6, 0.4, lambda a: E.pilula(c, "tensão U", (x1 + x2) / 2, y0 - 60, 46, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s04.e"], ps("campo uniforme e tensão", "i", 60) + [("U", "g", 64, COR)], XE, 800, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.formula_em(c, t, C["s05.a"], "U × 2  →  Q × 2", XE, 230, 90, "g", TINTA2)
            E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "capacitância", 1460, 200, 56, "g", fundo=E.COR, a=a))
            F.formula_legenda(c, t, C["s05.c"], "C = f{Q}{U}", [("C", "capacitância", "F, farad"), ("Q", "carga de uma placa", "C"), ("U", "tensão", "V")],
                              XE + 40, 500, 150, tl=[C["s05.d"], C["s05.e"], C["s05.f"]], size_l=58)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], [("1", "g", 96, COR), ("farad", "g", 90), ("é", "i", 96), ("muito", "i", 96)], XE, 260, passo=0.12)
            E.foco(c, t, C["s06.b"], 0.5, lambda a: pilula_f(c, "1 µF = 10^{−6} F", XE + 360, 420, 70, fundo=TINTA, a=a))
            E.frase(c, t, C["s06.c"], [("cuidado", "g", 70, ERRADO), ("com", "i", 74), ("as", "i", 74), ("letras", "i", 74)], XE, 620, passo=0.12)
            E.frase(c, t, C["s06.c"] + 1.2, [("C", "g", 70, COR), ("na", "i", 66), ("fórmula:", "i", 66), ("capacitância", "g", 62), ("·", "g", 62, TINTA2),
                                             ("carga", "i", 66), ("em", "i", 66), ("coulomb", "g", 62)], XE, 760, passo=0.1)
            E.frase(c, t, C["s06.c"] + 3.4, [("F", "g", 70, COR), ("do", "i", 66), ("farad", "g", 62), ("≠", "g", 70, ERRADO), ("F", "g", 70, COR),
                                             ("da", "i", 66), ("força", "g", 62)], XE, 900, passo=0.12)
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.foco(c, t, C["s07.a"], 0.5, lambda a: (E.escreve(c, "C =", XE, 240, 76, "g", TINTA, a), F.medida(c, 100, "µF", XE + 160, 240, 76, COR, a)))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.escreve(c, "U =", XE + 700, 240, 76, "g", TINTA, a), F.medida(c, 300, "V", XE + 860, 240, 76, COR, a)))
    E.formula_em(c, t, C["s07.c"], "Q = C · U", XE, 460, 100, "g", TINTA)
    E.formula_em(c, t, C["s07.d"], "= 100 × 10^{−6} · 300", XE + 520, 460, 84, "g", TINTA2)
    E.foco(c, t, C["s07.e"], 0.5, lambda a: pilula_f(c, "Q = 3 × 10^{−2} C", W / 2, 720, 90, a=a))
    capacitor(c, t, 1500, 1720, 760, 1000, C["s07.e"] + 0.3, None, C["s07.e"] + 0.5, C["s07.e"] + 0.5, n=3)


# ---------------- energia ----------------
def b_energia(c, t, C, b):
    def s08_09():
        E.frase(c, t, C["s08.a"], ps("o trabalho fica guardado:", "i", 64) + [("energia", "g", 64, COR)], XE, 200, passo=0.1)
        P = grafico_uq(c, t, C["s08.b"], 1040, 300, 640, 520, tarea=C["s08.c"])
        E.frase(c, t, C["s08.b"], ps("tensão pela carga: reta", "i", 60), XE, 330, passo=0.1)
        E.frase(c, t, C["s08.c"] - 1.6, [("V", "g", 56), ("×", "g", 56, TINTA2), ("C", "g", 56), ("=", "g", 56, TINTA2), ("J/C", "g", 56), ("×", "g", 56, TINTA2),
                                          ("C", "g", 56), ("=", "g", 56, TINTA2), ("J", "g", 56, COR)], XE, 440, passo=0.08)
        E.frase(c, t, C["s08.c"], ps("área =", "i", 64) + [("energia", "g", 62, COR)], XE, 560, passo=0.1)
        E.frase(c, t, C["s08.d"], ps("triângulo: base × altura ÷ 2", "i", 58, TINTA2), XE, 660, passo=0.1)
        E.foco(c, t, C["s08.e"], 0.5, lambda a: pilula_f(c, "energia = f{Q · U}{2}", XE + 380, 830, 72, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08_09)
    if C["s09"] <= t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09"], ps("no capacitor de antes", "i", 70, TINTA2), XE, 220, passo=0.12)
            E.formula_em(c, t, C["s09.a"], "energia = f{3 × 10^{−2} · 300}{2}", XE, 470, 96, "g", TINTA)
            E.formula_em(c, t, C["s09.b"], "= f{9}{2}", XE + 1060, 470, 96, "g", TINTA2)
            E.foco(c, t, C["s09.d"], 0.5, lambda a: pilula_f(c, "energia = 4,5 J", W / 2, 760, 96, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], [("e", "i", 84), ("o", "i", 84), ("flash?", "g", 84, COR)], XE, 220, passo=0.12)
            # barra de carga: enche devagar; no clique, esvazia de uma vez
            x, y, w, h = XE, 400, 760, 90
            enche = ease_io(prog(t, C["s10.a"], max(0.8, C["s10.b"] - C["s10.a"] - 0.2)))
            vazio = ep(t, C["s10.b"] + 0.2, 0.12)
            nivel = enche * (1 - vazio)
            M.rrect(c, x, y, w, h, 20, "#E4E4E0", ep(t, C["s10.a"], 0.3))
            if nivel > 0:
                M.rrect(c, x, y, w * nivel, h, 20, E.COR, 1.0)
            E.foco(c, t, C["s10.a"], 0.4, lambda a: E.escreve(c, "carrega devagar: segundos", x, y + 160, 56, "i", TINTA, a))
            E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "solta tudo: < 0,001 s", x, y + 260, 60, "g", COR, a))
            fl = ep(t, C["s10.b"] + 0.2, 0.1) * (1 - ep(t, C["s10.b"] + 0.5, 0.8))
            E.foco(c, t, C["s10"] + 0.3, 0.5, lambda a: camera(c, 1460, 520, 220, a, fl))
            E.frase(c, t, C["s10.c"], ps("pouca energia, muito rápido", "i", 60), XE, 840, passo=0.1)
            E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "luz forte", 1460, 860, 60, "g", fundo=AMAR, cor=TINTA, a=a))
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.formula_em(c, t, C["s11"], "Q = C · U", XE, 280, 90, "g", TINTA2)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: pilula_f(c, "energia = f{C · U^2}{2}", W / 2, 470, 96, a=a))
    E.formula_em(c, t, C["s11.b"], "U × 2", 560, 800, 110, "g", TINTA, "center")
    E.foco(c, t, C["s11.c"], 0.5, lambda a: (F.seta(c, 800, 765, 1040, 765, TINTA2, a, 8), pilula_f(c, "energia × 4", 1360, 765, 90, fundo=CERTO, a=a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("esquecer o", "i", 76) + [("÷ 2", "g", 76, ERRADO)], XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: pilula_f(c, "Q · U = 9 J", XE + 300, 420, 84, fundo=ERRADO, a=a))
    if t >= C["s12.b"] + 0.8:
        E.risco(c, XE + 20, 460, XE + 580, 380, t, C["s12.b"] + 0.8, largura=10)
    grafico_uq(c, t, C["s12.c"] - 0.6, 1060, 330, 600, 480, tarea=C["s12.c"] + 0.3, tret=C["s12.c"], tri_cor=CERTO)
    E.frase(c, t, C["s12.c"], [("triângulo,", "g", 64, CERTO), ("não", "i", 70), ("retângulo", "g", 64, ERRADO)], XE, 640, passo=0.12)
    E.frase(c, t, C["s12.d"], ps("a tensão começou em zero", "i", 60, TINTA2), XE, 760, passo=0.1)
    E.foco(c, t, C["s12.d"] + 1.0, 0.5, lambda a: pilula_f(c, "certo: 4,5 J", XE + 300, 910, 76, fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("três formas, a mesma energia", "i", 68, CLARO), W / 2, 280, "center", 0.12)
        for k, s, x in (("s13.b", "f{Q · U}{2}", 480), ("s13.c", "f{C · U^2}{2}", 960), ("s13.d", "f{Q^2}{2 · C}", 1440)):
            E.formula_em(c, t, C[k], s, x, 520, 110, "g", BR, "center")
        E.frase(c, t, C["s13.e"], ps("escolha a que usa os dados", "g", 60, BR), W / 2, 820, "center", 0.12)
        E.frase(c, t, C["s13.e"] + 1.6, ps("e pule uma etapa", "i", 64, CLARO), W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("todas vêm de", "i", 76, CLARO), W / 2, 300, "center", 0.12)
    E.foco(c, t, C["s14.a"] + 1.0, 0.5, lambda a: pilula_f(c, "Q = C · U", W / 2, 420, 84, a=a))
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO), ("compensa", "i", 70, CLARO), ("decorar", "i", 70, CLARO), ("se", "i", 70, CLARO), ("confunde:", "i", 70, CLARO)],
            W / 2, 640, "center", 0.12)
    E.frase(c, t, C["s14.b"] + 1.8, ps("ache Q e use Q · U ÷ 2", "g", 64, BR), W / 2, 780, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "C =", XE, 360, 84, "g", TINTA, a), F.medida(c, 20, "µF", XE + 170, 360, 84, COR, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "U =", XE, 500, 84, "g", TINTA, a), F.medida(c, 100, "V", XE + 170, 500, 84, COR, a)))
    E.frase(c, t, C["s15.c"], [("carga", "i", 80), ("em", "i", 80), ("cada", "i", 80), ("placa?", "g", 76, COR)], XE, 680, passo=0.15)
    E.frase(c, t, C["s15.d"], [("energia", "i", 80), ("guardada?", "g", 76, COR)], XE, 820, passo=0.15)
    questao_relogio(c, t, C, "s16", lambda: capacitor(c, t, 1320, 1600, 300, 760, C["s15.a"], C["s15.a"] + 0.2, C["s15.b"], C["s15.b"]))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "Q = C · U", XE, 240, 90, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "= 20 × 10^{−6} · 100", XE + 470, 240, 84, "g", TINTA2)
    E.formula_em(c, t, C["s17.c"], "= 2.000 × 10^{−6}", XE + 470, 380, 84, "g", TINTA2)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: pilula_f(c, "Q = 2 × 10^{−3} C", W / 2, 520, 72, a=a))
    E.formula_em(c, t, C["s18.a"], "energia = f{Q · U}{2}", XE, 740, 90, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= f{2 × 10^{−3} · 100}{2} = f{0,2}{2}", XE + 760, 740, 84, "g", TINTA2)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: pilula_f(c, "energia = 0,1 J", W / 2, 960, 80, fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s19", (("s19.a", [("C = Q ÷ U,", "g", 70), ("em", "i", 72), ("farad", "g", 68, COR)]),
                                ("s19.b", [("energia = Q · U ÷ 2:", "g", 66), ("o", "i", 70), ("triângulo", "i", 70)]),
                                ("s19.c", [("carrega", "i", 72), ("devagar,", "i", 72), ("solta", "g", 68), ("de", "i", 72), ("uma", "i", 72), ("vez", "g", 68, COR)])))
    E.saida(c, t, C["s20"] - 0.1, tela)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("praticando", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.5, [("eletrostática", "g", 90)], XE, 520)
    for i, s in enumerate(("eletrização", "força", "campo", "potencial", "capacitores")):
        x = XE + (i % 3) * 360
        y = 680 + (i // 3) * 120
        E.foco(c, t, C["s20.b"] + 0.25 * i, 0.4, lambda a, s=s, x=x, y=y: E.pilula(c, s, x + (E.larg(s, "g", 44) + 48) / 2, y, 44, "g", fundo=TINTA, a=a))
    cta(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, capacitor=b_capacitor, energia=b_energia, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
