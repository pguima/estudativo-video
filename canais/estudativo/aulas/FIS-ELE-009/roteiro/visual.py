"""Visual — Estudativo · FIS-ELE-009: resistência e primeira lei de Ohm.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
circuito em tinta com F.resistor/F.pilha, corrente em setinhas laranja; gráfico U × i com F.grafico (U no eixo vertical);
ôhmico = reta pela origem em laranja; não ôhmico = curva em azul (F.NEG); Ω sempre na fonte pesada. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-009_resistencia_primeira_lei_de_ohm.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("resistencia", "ohm", "grafico", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"

# todas as contas da aula
assert 220 / 11 == 20 and 11 * 20 == 220
assert 10 / 2 == 5 and 20 / 4 == 5
assert 12 / 0.5 == 24 and 36 / 12 == 3 and 0.5 * 3 == 1.5 and 36 / 24 == 1.5


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



def chuveiro(c, cx, cy, s, a=1.0, agua=0.0, quente=True):
    """chuveiro de lado: cano em cima, crivo, gotas"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.1, cy - s * 1.2, s * 0.2, s * 0.8, 8, METAL, a)
    p = skia.Path()
    p.moveTo(cx - s * 0.6, cy - s * 0.1); p.lineTo(cx + s * 0.6, cy - s * 0.1); p.lineTo(cx + s * 0.35, cy - s * 0.5); p.lineTo(cx - s * 0.35, cy - s * 0.5); p.close()
    c.drawPath(p, M.paint("#E4E4E0", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))
    if agua > 0:
        cor = "#5AA9E6" if not quente else "#FF9A6A"
        for i in range(7):
            x = cx - s * 0.5 + i * s / 6
            for k in range(3):
                y = cy + ((agua * 2 + k / 3 + i * 0.13) % 1) * s * 1.2
                c.drawCircle(x, y, 7, M.paint(cor, a * 0.9))


def cano(c, t, t0, x0, y0, x1, y1, h=60, tagua=None):
    """cano inclinado (de y0 alto para y1 baixo) com água correndo"""
    q_ = ep(t, t0, 0.5)
    if q_ <= 0:
        return
    M.line(c, x0, y0, x1, y1, "#B9C6D2", q_, h)
    if tagua is not None and t >= tagua:
        ux, uy = E._uni(x0, y0, x1, y1)
        L = math.dist((x0, y0), (x1, y1))
        for k in range(6):
            s = ((t - tagua) * 160 + k * L / 6) % L
            c.drawCircle(x0 + ux * s, y0 + uy * s, 12, M.paint("#2F7FC1", ep(t, tagua, 0.4)))


def triangulo_uri(c, cx, cy, s, a=1.0, tampa=None, cor=BR, fundo=None):
    """triângulo U / R × i; tampa = "U", "R" ou "i" desenha a tampa (pílula) sobre a letra"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy - s); p.lineTo(cx + s * 1.1, cy + s * 0.7); p.lineTo(cx - s * 1.1, cy + s * 0.7); p.close()
    c.drawPath(p, M.paint(cor, a, stroke=6))
    M.line(c, cx - s * 0.7, cy + s * 0.05, cx + s * 0.7, cy + s * 0.05, cor, a, 6)
    M.line(c, cx, cy + s * 0.05, cx, cy + s * 0.7, cor, a, 6)
    pos = {"U": (cx, cy - s * 0.18), "R": (cx - s * 0.38, cy + s * 0.5), "i": (cx + s * 0.38, cy + s * 0.5)}
    for k, (x, y) in pos.items():
        E.centro(c, k, x, y + s * 0.12, s * 0.38, "g", cor, a)
    if tampa:
        x, y = pos[tampa]
        c.drawCircle(x, y, s * 0.27, M.paint(fundo or E.COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: chuveiro(c, 1400, 480, 300, a, max(0, t - C["s01.a"]) * 0.8, quente=t < C["s01.b"]))
        E.frase(c, t, C["s01.a"], [("o", "i", 80), ("chuveiro", "i", 80), ("tem", "i", 80), ("uma", "i", 80)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.a"] + 0.8, [("resistência", "g", 90, COR)], XE, 380)
        E.frase(c, t, C["s01.b"], ps("queimou:", "i", 70) + [("água", "g", 66, NEG), ("fria", "g", 66, NEG)], XE, 540, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("o que é", "i", 76) + [("resistência?", "g", 72, COR)], XE, 760, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "U = R · i", 0.4), ("s02.c", "o resistor ôhmico", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "corrente, em ampère:", "carga por segundo"), ("s03.c", "tensão U, em volt:", "a ddp")),
             (lambda a, x, y: E.formula(c, "i = f{Q}{Δt}", x - 10, y + 20, 56, "g", TINTA, a, "center"),
              lambda a, x, y: E.formula(c, "1 V = 1 J/C", x - 30, y + 20, 48, "g", TINTA, a, "center")))


# ---------------- tensão e resistência ----------------
def b_resistencia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("a tensão", "i", 80) + [("empurra", "g", 76, COR)] + ps("a corrente", "i", 80), XE, 230, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("sem tensão,", "i", 66) + [("sem", "g", 62), ("corrente", "g", 62)], XE, 350, passo=0.12)
        cano(c, t, C["s04.b"] + 0.6, 700, 520, 1500, 820, tagua=C["s04.d"])
        if t >= C["s04.c"]:
            a = ep(t, C["s04.c"], 0.4)
            M.line(c, 1600, 520, 1600, 820, COR, a, 6, dash=E.TRACO)
            M.line(c, 1560, 520, 1640, 520, COR, a, 6)
            M.line(c, 1560, 820, 1640, 820, COR, a, 6)
            E.escreve(c, "desnível = tensão", 1300, 470, 54, "g", COR, a)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.escreve(c, "água por segundo = corrente", 700, 940, 56, "g", "#2F7FC1", a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    x, y, w = 760, 520, 1000
    M.rrect(c, x, y - 60, w, 120, 60, METAL, ep(t, C["s05"], 0.4))
    for i in range(10):
        for j in range(2):
            ax_, ay_ = x + 70 + i * 95, y - 25 + j * 50
            c.drawCircle(ax_, ay_, 14, M.paint("#6E7682", ep(t, C["s05"] + 0.2, 0.4)))
    if t >= C["s05.a"]:
        for k in range(5):
            s = ((t - C["s05.a"]) * 140 + k * 200) % (w - 60)
            q(c, x + 30 + s, y + 10 * math.sin(s / 30), 16, "−", ep(t, C["s05.a"], 0.4))
    hot = ep(t, C["s05.b"], 0.8)
    if hot > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(x + w / 2, y), w * 0.6, [M.hexc("#FF5A1F", 0.35 * hot), M.hexc("#FF5A1F", 0)], [0, 1]))
        c.drawCircle(x + w / 2, y, w * 0.6, g)
    E.frase(c, t, C["s05.a"], ps("os elétrons", "i", 66) + [("esbarram", "g", 62)], XE, 230, passo=0.12)
    E.frase(c, t, C["s05.b"], ps("a peça", "i", 66) + [("esquenta", "g", 62, COR)], XE, 340, passo=0.12)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "resistência elétrica: R", W / 2, 780, 64, "g", fundo=E.COR, a=a))
    F.fio(c, t, C["s05.d"], [(560, 940), (760, 940)])
    F.fio(c, t, C["s05.d"], [(1000, 940), (1200, 940)])
    F.resistor(c, t, C["s05.d"] + 0.2, (760, 940), (1000, 940))
    E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: E.escreve(c, "resistor", 1260, 960, 60, "g", TINTA, a))


# ---------------- lei de Ohm ----------------
def b_ohm(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], ps("primeira lei de", "i", 72) + [("Ohm", "g", 72, COR)], XE, 200, passo=0.12)
        F.formula_legenda(c, t, C["s06.b"], "U = R · i", [("U", "tensão", "V"), ("R", "resistência", "Ω, ohm"), ("i", "corrente", "A")],
                          XE + 40, 440, 160, tl=[C["s06.c"], C["s06.d"], C["s06.e"]], size_l=58)
        E.foco(c, t, C["s06.f"], 0.5, lambda a: pilula_f(c, "1 Ω = 1 V/A", 1440, 420, 90, a=a))
        E.foco(c, t, C["s06.f"] + 1.2, 0.4, lambda a: E.escreve(c, "Ω: a letra grega ômega", 1180, 580, 52, "b", TINTA2, a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.foco(c, t, C["s07"] + 0.2, 0.5, lambda a: chuveiro(c, 1560, 470, 220, a))
            E.foco(c, t, C["s07.a"], 0.5, lambda a: (E.escreve(c, "U =", XE, 290, 90, "g", TINTA, a), F.medida(c, 220, "V", XE + 190, 290, 90, COR, a)))
            E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.escreve(c, "R =", XE, 420, 90, "g", TINTA, a), F.medida(c, 11, "Ω", XE + 190, 420, 90, COR, a)))
            E.formula_em(c, t, C["s07.c"], "220 = 11 · i", XE, 620, 96, "g", TINTA)
            E.formula_em(c, t, C["s07.d"], "i = f{220}{11}", XE, 820, 96, "g", TINTA)
            E.foco(c, t, C["s07.e"], 0.5, lambda a: pilula_f(c, "i = 20 A", 1000, 790, 96, a=a))
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], [("R", "g", 76, COR), ("fixo:", "i", 80), ("U", "g", 76), ("e", "i", 80), ("i", "g", 76), ("proporcionais", "g", 72, COR)], XE, 250, passo=0.12)
    linhas = (("U × 2", "i × 2", C["s08.b"]), ("U × 3", "i × 3", C["s08.b"] + 1.6))
    for k, (u, i_, t0) in enumerate(linhas):
        y = 470 + k * 170
        E.formula_em(c, t, t0, u, XE + 60, y, 100, "g", TINTA)
        E.foco(c, t, t0 + 0.4, 0.4, lambda a, y=y: F.seta(c, XE + 440, y - 34, XE + 640, y - 34, TINTA2, a, 8))
        E.formula_em(c, t, t0 + 0.6, i_, XE + 720, y, 100, "g", COR)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "RESISTOR ÔHMICO", W / 2, 900, 70, "g", fundo=E.COR, a=a))


# ---------------- gráfico ----------------
def b_grafico(c, t, C, b):
    def s09():
        P = F.grafico(c, t, C["s09"], 1000, 260, 760, 600, 0, 5, 0, 25, eixo_x="i (A)", eixo_y="U (V)", passo=1, passo_y=5, marcas_x=(2, 4), marcas_y=(10, 20))
        E.curva(c, t, C["s09.a"], P, lambda v: 5 * v, 0, 4.8, d=1.0)
        E.ponto(c, t, C["s09.c"], P, 2, 10, guias=True)
        E.ponto(c, t, C["s09.d"], P, 4, 20, guias=True)
        E.frase(c, t, C["s09"], ps("gráfico da tensão pela corrente", "i", 56, TINTA2), XE, 230, passo=0.1)
        E.frase(c, t, C["s09.a"], [("reta", "g", 70, COR), ("pela", "i", 72), ("origem", "g", 70)], XE, 360, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("função linear:", "i", 62) + [("U = R · i", "g", 62)], XE, 470, passo=0.1)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "2 A → 10 V", XE, 610, 64, "g", TINTA, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "4 A → 20 V", XE, 710, 64, "g", TINTA, a))
        E.foco(c, t, C["s09.e"], 0.5, lambda a: pilula_f(c, "R = f{10}{2} = f{20}{4} = 5 Ω", XE + 360, 870, 64, a=a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    P = F.grafico(c, t, C["s10"], 1000, 260, 760, 600, 0, 5, 0, 25, eixo_x="i (A)", eixo_y="U (V)", passo=1, passo_y=5, marcas_x=(), marcas_y=())
    E.curva(c, t, C["s10"] + 0.3, P, lambda v: 5 * v, 0, 4.8, d=0.6, tracejada=True)
    E.curva(c, t, C["s10.c"], P, lambda v: 1.5 * v + 0.3 * v ** 3, 0, 4.3, d=1.2, cor=NEG)
    E.foco(c, t, C["s10.c"] + 1.0, 0.4, lambda a: E.escreve(c, "ôhmico", 1745, 320, 44, "i", TINTA2, a))
    E.foco(c, t, C["s10.c"] + 1.2, 0.4, lambda a: E.escreve(c, "filamento", 1500, 190, 48, "g", NEG, a))
    E.ponto(c, t, C["s10.e"], P, 3, 1.5 * 3 + 0.3 * 27, cor=NEG, guias=True)
    E.frase(c, t, C["s10.a"], [("filamento", "g", 70), ("esquenta", "i", 74)], XE, 260, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("a resistência muda:", "i", 62) + [("cresce", "g", 60, COR)], XE, 380, passo=0.1)
    E.frase(c, t, C["s10.c"], [("curva", "g", 66, NEG)] + ps("cada vez mais inclinada", "i", 58), XE, 500, passo=0.1)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "NÃO ÔHMICO", XE + 240, 650, 60, "g", fundo=NEG, a=a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: pilula_f(c, "R = f{U}{i} daquele ponto", XE + 380, 840, 60, fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("R cresce com U?", "i", 80), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s11.b"], "R = f{U}{i}", XE, 450, 120, "g", TINTA)
    E.formula_em(c, t, C["s11.b"] + 1.6, "U × 2  →  R × 2 ?", XE + 520, 420, 90, "g", ERRADO)
    if t >= C["s11.c"]:
        E.risco(c, XE + 500, 440, XE + 1350, 360, t, C["s11.c"], largura=10)
    E.formula_em(c, t, C["s11.c"], "R = f{2U}{2i} = f{U}{i}", XE, 720, 110, "g", CERTO)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "R fica igual", 1400, 690, 60, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s11.e"], ps("ôhmico: R depende da", "i", 64) + [("peça", "g", 62, COR)], XE, 950, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s12.a"], ps("o triângulo do", "i", 72, CLARO) + [("U R i", "g", 72, BR)], W / 2, 280, "center", 0.12)
        tampa = None
        for k, v in (("s12.d", "U"), ("s12.e", "R"), ("s12.f", "i")):
            if t >= C[k]:
                tampa = v
        E.foco(c, t, C["s12.b"], 0.5, lambda a: triangulo_uri(c, 560, 640, 260, a, tampa))
        E.frase(c, t, C["s12.c"], ps("tampe o que quer achar", "i", 62, CLARO), 1320, 450, "center", 0.1)
        troca(c, t, [(C["s12.d"], "U = R · i"), (C["s12.e"], "R = f{U}{i}"), (C["s12.f"], "i = f{U}{R}")],
              lambda s, a: E.formula(c, s, 1320, 720, 130, "g", BR, a, "center"))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("a mesma fórmula, isolada de 3 jeitos", "i", 66, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s13.b"], [("não", "g", 64, ERRADO), ("ôhmico:", "g", 64, BR)] + ps("não leve o R de um ponto a outro", "i", 64, CLARO), W / 2, 560, "center", 0.1)
    E.frase(c, t, C["s13.b"] + 2.0, ps("o triângulo vale ponto a ponto", "i", 64, CLARO), W / 2, 680, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"] - 0.6, [("resistor", "i", 76), ("ôhmico", "g", 72)], XE, 330, passo=0.12)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: (E.escreve(c, "U =", XE, 460, 84, "g", TINTA, a), F.medida(c, 12, "V", XE + 170, 460, 84, COR, a)))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "i =", XE + 500, 460, 84, "g", TINTA, a), F.medida(c, "0,5", "A", XE + 650, 460, 84, COR, a)))
    E.frase(c, t, C["s14.c"], [("R?", "g", 84, COR)], XE, 630)
    E.frase(c, t, C["s14.d"], [("com", "i", 76), ("36", "g", 76, COR), ("V,", "g", 76), ("qual", "i", 76), ("é", "i", 76), ("a", "i", 76), ("corrente?", "g", 72, COR)], XE, 790, passo=0.12)

    def desenho():
        x0, x1, y0, y1 = 1180, 1720, 380, 760
        F.fio(c, t, C["s14.a"], [(x0, (y0 + y1) / 2 - 60), (x0, y0), (1370, y0)])
        F.fio(c, t, C["s14.a"], [(1530, y0), (x1, y0), (x1, y1), (x0, y1), (x0, (y0 + y1) / 2 + 60)])
        F.pilha(c, t, C["s14.a"] + 0.2, (x0, (y0 + y1) / 2 + 60), (x0, (y0 + y1) / 2 - 60), "12 V", lado=-1)
        F.resistor(c, t, C["s14.a"] + 0.3, (1370, y0), (1530, y0), "R")
        if t >= C["s14.b"]:
            F.corrente(c, t, C["s14.b"], [(x0, (y0 + y1) / 2 - 60), (x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, (y0 + y1) / 2 + 60)], fecha=False)
    questao_relogio(c, t, C, "s15", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s16.a"], "R = f{U}{i}", XE, 280, 100, "g", TINTA)
    E.formula_em(c, t, C["s16.b"], "= f{12}{0,5}", XE + 400, 280, 100, "g", TINTA2)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: pilula_f(c, "R = 24 Ω", 1360, 245, 90, a=a))
    E.foco(c, t, C["s16.c"] + 1.2, 0.4, lambda a: E.escreve(c, "dividir por meio é dobrar", XE, 430, 54, "i", TINTA2, a))
    E.formula_em(c, t, C["s17.a"], "12 V → 36 V:  U × 3", XE, 600, 84, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "i × 3 = 0,5 × 3", XE, 760, 84, "g", TINTA)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: pilula_f(c, "i = 1,5 A", 1360, 730, 90, fundo=CERTO, a=a))
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.formula(c, "confira: f{36}{24} = 1,5", XE, 950, 70, "g", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s18", (("s18.a", [("U = R · i", "g", 76)]),
                                ("s18.b", [("resistência", "i", 72), ("em", "i", 72), ("ohm,", "g", 68, COR), ("Ω", "g", 68, COR)]),
                                ("s18.c", [("ôhmico:", "g", 68), ("reta", "g", 68, COR), ("pela", "i", 72), ("origem", "i", 72)])))
    E.saida(c, t, C["s19"] - 0.1, tela)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("segunda", "g", 110, COR), ("lei", "i", 110), ("de", "i", 110), ("Ohm", "g", 110, COR)], XE, 400, passo=0.15)
    for i, (w, h, cor, nome) in enumerate(((560, 26, METAL, "comprimento"), (300, 52, METAL, "espessura"), (420, 26, "#C9A227", "material"))):
        y = 600 + i * 130
        E.foco(c, t, C["s19.b"] + 0.5 * i, 0.4, lambda a, w=w, h=h, cor=cor, y=y, nome=nome: (M.rrect(c, XE, y - h / 2, w, h, h / 2, cor, a),
                                                                                         E.escreve(c, nome, XE + 620, y + 18, 54, "i", TINTA, a)))
    cta(c, t, C, "s19")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, resistencia=b_resistencia, ohm=b_ohm, grafico=b_grafico, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
