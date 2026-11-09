"""Visual — Estudativo · FIS-EGF-004: pressão: força por área.

Segue a linguagem visual da Física (visual.py da FIS-CIN-001) e a da trilha Equilíbrio, Gravitação e Fluidos (cabeçalho do
visual.py da FIS-EGF-001): eixo e braço em cota, giro horário laranja e anti-horário azul, astros (Sol âmbar, Terra azul),
fluidos em azul translúcido, pressão em setinhas laranja, empuxo azul. O kit da trilha vem copiado logo abaixo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Equilíbrio, Gravitação e Fluidos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-EGF-004_pressao_forca_por_area.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pressao", "atmosfera", "atalho", "questao", "fim"))

# todas as contas da aula
assert 600 / 2 == 300 and 600 / 0.5 == 1200 and abs(600 / 0.002 - 300_000) < 1e-6 and 600 / 20 == 30 and 30 * 10_000 == 300_000
assert 60 * 10 == 600 and 600 / 300 == 2 and 2 * 10_000 == 20_000 and 20_000 / 100_000 == 0.2 and 2 * 20_000 == 40_000
assert 100 * 100 == 10_000 and 1e5 / 10 / 1000 == 10  # 1 m² = 10.000 cm²; 10⁵ N = peso de 10 toneladas


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha (o mesmo em todas as aulas FIS-EGF) ----------------
BR = "#FFFFFF"
MADEIRA, MADEIRA2 = "#B07A4A", "#7E5432"
AGUA, AGUA2, OLEO = "#5AB4E6", "#2C86C2", "#E9B44C"
SOL, TERRA, LUA = "#FFB020", "#2F6FB0", "#A9A9B4"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def linhas(c, t, itens, x, y0, dy, size=72, align="left", est="g"):
    """passo a passo: itens = [(instante, "fórmula", cor)], uma linha por etapa, de cima para baixo"""
    for i, it in enumerate(itens):
        t0, s, cor = it[0], it[1], (it[2] if len(it) > 2 else TINTA)
        E.formula_em(c, t, t0, s, x, y0 + i * dy, size, est, cor, align)


def cota(c, t, t0, A, B, rot, cor=TINTA2, size=46, lado=-1, d=0.5, cor_txt=None):
    """linha de medida de A até B, com tracinhos nas pontas e o rótulo no meio, do lado `lado` (−1 = acima/esquerda)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    ux, uy = E._uni(*A, *B)
    nx, ny = -uy, ux
    M.line(c, *A, lerp(A[0], B[0], q), lerp(A[1], B[1], q), cor, 1.0, 4)
    for P_ in (A, B):
        M.line(c, P_[0] - nx * 16, P_[1] - ny * 16, P_[0] + nx * 16, P_[1] + ny * 16, cor, q, 4)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    E.foco(c, t, t0 + d * 0.6, 0.4, lambda a: E._meio(c, rot, mx + nx * lado * (size * 0.8), my + ny * lado * (size * 0.8), size, "b", cor_txt or E.COR_TEXTO, a))


def seta_giro(c, cx, cy, r, ini, varre, cor, a=1.0, largura=9, p=1.0):
    """arco com ponta de seta: o sentido do giro. ini e varre em graus de tela (varre > 0 = horário)"""
    if a <= 0 or p <= 0:
        return
    v = varre * p
    E.arco(c, cx, cy, r, ini, v, cor, largura, a)
    g = math.radians(ini + v)
    x, y = cx + r * math.cos(g), cy + r * math.sin(g)
    s = 1 if v > 0 else -1
    ux, uy = -math.sin(g) * s, math.cos(g) * s
    F._cabeca(c, x + ux * largura * 1.6, y + uy * largura * 1.6, ux, uy, largura * 3.2, cor, a)


def apoio(c, x, y, s=70, a=1.0, escuro=False):
    """apoio triangular com o vértice (o eixo) em (x, y)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x - s * 0.7, y + s); p.lineTo(x + s * 0.7, y + s); p.close()
    c.drawPath(p, M.paint(BR if escuro else TINTA, a))
    c.drawCircle(x, y, s * 0.13, M.paint(E.COR, a))


def lembrete(c, t, C, cena, itens, numero, palavra="coisas"):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)], uma caixa por item"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de" if palavra == "coisas" else "você vai usar", "i", 80), XE, 410, passo=0.14)
    t1 = C.get(cena + ".a", C[cena] + 0.6) if hasattr(C, "get") else C[cena] + 0.6
    E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, str(numero), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, palavra, XE + 215, 700, 110 if palavra == "coisas" else 84, "i", TINTA, a))
    x, w = 820, 1000
    h = {2: 230, 3: 190, 4: 150}[n]
    gap = {2: 290, 3: 230, 4: 180}[n]
    y0 = {2: 230, 3: 150, 4: 140}[n]
    s1, s2 = {2: (58, 58), 3: (50, 52), 4: (44, 46)}[n]
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s2, COR)], x + 44, y + h * 0.4 + s2 * 1.3)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 50, COR) + ps("procure no canal", "i", 50), 820, 1010, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """até o fim da aula: itens = [(cue, texto)] numerados, com a órbita à direita"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.2 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, cena, itens):
    """itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 26, 52, a=a), centro(c, str(i + 1), 230, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.1)


def proxima(c, t, C, cena, l1, l2, desenho=None, k=("a", "c", "d")):
    """próxima aula + inscreva-se + bons estudos; desenho(a) ilustra a próxima aula na metade de baixo"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[f"{cena}.{k[0]}"], l1, XE, 400)
    if l2:
        E.frase(c, t, C[f"{cena}.{k[0]}"] + 0.5, l2, XE, 540)
    if desenho:
        desenho()
    E.foco(c, t, C[f"{cena}.{k[1]}"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[f"{cena}.{k[1]}"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[f"{cena}.{k[1]}"] + 0.2, 0.4))
    E.frase(c, t, C[f"{cena}.{k[2]}"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def hora_testar(c, t, C, cena):
    E.frase(c, t, C[cena], ps("hora de testar", "i", 72, COR), XE, 180)




def empurra(c, t, t0, P, ang, comp, rot=None, modulo=None, cor=None):
    """força que CHEGA ao ponto P vindo da direção oposta a ang (graus da Física): a ponta encosta no corpo"""
    dx, dy = F._dir(ang)
    F.vetor(c, t, t0, (P[0] - dx * comp, P[1] - dy * comp), P, rot, modulo, cor, 10, em=0.4)


# ---------------- peças desta aula ----------------
TOMATE = "#D8342C"
LAMINA = "#B9BCC4"


def setas_pressao(c, t, t0, x0, x1, y, comp, n, cor=None, d=0.5, sobe=False):
    """n setinhas de pressão lado a lado, de x0 a x1, apertando a linha y (para baixo; sobe=True aponta para cima)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    for i in range(n):
        x = lerp(x0, x1, (i + 0.5) / n)
        if sobe:
            F.seta(c, x, y + comp, x, y, cor or E.COR, q, 6, cabeca=18, p=q)
        else:
            F.seta(c, x, y, x, y + comp, cor or E.COR, q, 6, cabeca=18, p=q)


def faca(c, x, y, w, afiada, a=1.0):
    """faca de lado, lâmina para baixo; (x, y) = ponta do fio, à esquerda"""
    if a <= 0:
        return
    p = skia.Path()
    esp = 4 if afiada else 34
    p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w, y - 110); p.lineTo(x + 40, y - 110)
    p.lineTo(x, y - esp); p.close()
    c.drawPath(p, M.paint(LAMINA, a))
    c.drawPath(p, M.paint(TINTA2, a, stroke=3))
    M.rrect(c, x + w, y - 110, 200, 70, 18, TINTA, a)
    if not afiada:
        M.rrect(c, x, y - 34, w, 34, 6, "#9A9DA6", a)


def tomate(c, cx, cy, r, amassado=0.0, cortado=0.0, a=1.0):
    if a <= 0:
        return
    if cortado > 0:
        for d in (-1, 1):
            c.save(); c.translate(cx + d * 30 * cortado, cy); c.rotate(d * 8 * cortado)
            c.clipRect(skia.Rect.MakeLTRB(-r * 1.2 if d < 0 else 0, -r * 1.2, 0 if d < 0 else r * 1.2, r * 1.2))
            E.bola(c, 0, 0, r, TOMATE, a)
            c.restore()
        return
    c.save(); c.translate(cx, cy + r * 0.3 * amassado); c.scale(1 + 0.35 * amassado, 1 - 0.3 * amassado)
    E.bola(c, 0, 0, r, TOMATE, a)
    c.restore()
    M.line(c, cx, cy - r * (1 - 0.3 * amassado) + 4, cx + 10, cy - r - 22, "#3E9B3E", a, 6)


def caixa(c, cx, chao_y, w, h, rot, a=1.0):
    F.bloco(c, cx, chao_y - h / 2, w, h, rot, a=a, size=44)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            for i, (k_, afiada, txt, cor) in enumerate((("s01.a", False, "faca cega: amassa", ERRADO), ("s01.b", True, "faca afiada: corta", CERTO))):
                x0 = 260 + i * 820
                q = ep(t, C[k_], 0.5)
                if q <= 0:
                    continue
                desce = ease_io(prog(t, C[k_] + 0.6, 1.0))
                F.chao(c, x0 - 40, x0 + 600, 820, q)
                if afiada:
                    tomate(c, x0 + 280, 720, 100, cortado=ease_io(prog(t, C[k_] + 1.4, 0.6)), a=q)
                    faca(c, x0 + 140, lerp(520, 720 if desce < 1 else 820, desce), 300, True, q)
                else:
                    tomate(c, x0 + 280, 720, 100, amassado=desce, a=q)
                    faca(c, x0 + 140, lerp(520, 620 + 30 * desce, desce), 300, False, q)
                E.foco(c, t, C[k_] + 0.4, 0.4, lambda a, x0=x0, txt=txt, cor=cor: E.escreve(c, txt, x0, 960, 54, "g", cor, a))
            E.frase(c, t, lerp(C["s01.b"], C["s01.c"], 0.5), ps("a mesma força. muda a", "i", 66), XE, 200, passo=0.1)
            E.frase(c, t, C["s01.c"], [("área", "g", 76, COR)], XE + 680, 200)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "calcular a pressão"), ("s02.b", "pascal e atmosfera"), ("s02.c", "a faca afiada")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o peso:", "massa × 10, em newtons"), ("s03.c", "converter área:", "1 m² = 10.000 cm²")), 2)


# ---------------- pressão ----------------
def b_pressao(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("pressão", "g", 80, COR)] + ps("= força em cada pedaço de área", "i", 64), XE, 190, passo=0.1)
            F.formula_legenda(c, t, C["s04.b"], "p = f{F}{A}", [("F", "força que aperta, em ângulo reto", "N"), ("A", "área", "m^2"), ("p", "pressão", "Pa")],
                              XE, 420, 140, tl=[C["s04.c"], C["s04.d"], C["s04.e"]], size_l=48)
            pilula_em(c, t, C["s04.f"], "1 Pa = 1 N/m²", XE + 350, 900, 50, E.COR)
            y = 760
            q = ep(t, C["s04.b"], 0.5)
            if q > 0:
                F.chao(c, 1150, 1750, y, q)
                caixa(c, 1450, y, 420, 200, "F", q)
            setas_pressao(c, t, C["s04.c"], 1250, 1650, y + 10, 60, 7)
            E.foco(c, t, C["s04.d"], 0.4, lambda a: (M.line(c, 1240, y - 210, 1660, y - 210, E.COR, a, 6), centro(c, "área A", 1450, y - 240, 46, "b", COR, a)))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            y = 520
            q1, q2 = ep(t, C["s05.a"], 0.5), ep(t, C["s05.e"], 0.5)
            if q1 > 0:
                F.chao(c, 160, 900, y, q1)
                caixa(c, 520, y, 560, 160, "600 N", q1)
            setas_pressao(c, t, C["s05.b"], 260, 780, y + 10, 40, 8)
            E.foco(c, t, C["s05.b"], 0.4, lambda a: centro(c, "2 m²", 520, y + 110, 46, "b", TINTA2, a))
            if q2 > 0:
                F.chao(c, 1060, 1760, y, q2)
                caixa(c, 1400, y, 160, 360, "600 N", q2)
            setas_pressao(c, t, C["s05.f"], 1330, 1470, y + 10, 160, 3)
            E.foco(c, t, C["s05.f"], 0.4, lambda a: centro(c, "0,5 m²", 1520, y + 110, 46, "b", TINTA2, a))
            E.formula_em(c, t, C["s05.c"], "600 ÷ 2 = 300 Pa", 520, 800, 72, "g", TINTA, "center")
            E.formula_em(c, t, C["s05.f"] + 0.4, "600 ÷ 0,5 = 1.200 Pa", 1400, 800, 72, "g", COR, "center")
            E.frase(c, t, C["s05.h"] - 1.4, [("área ÷ 4", "g", 70), ("→", "g", 66, TINTA2), ("pressão × 4", "g", 70, COR)], W / 2, 950, "center", 0.2)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], ps("a faca é a", "i", 70) + [("mesma ideia", "g", 70, COR)], XE, 190, passo=0.12)
            # o fio visto de perto: cega (largo) e afiada (finíssimo)
            E.foco(c, t, C["s06.b"], 0.5, lambda a: (M.rrect(c, 300, 400, 380, 40, 6, LAMINA, a), centro(c, "cega: fio largo", 490, 500, 44, "b", TINTA2, a),
                                                      M.rrect(c, 300, 600, 380, 6, 2, TINTA, a), centro(c, "afiada: fio finíssimo", 490, 680, 44, "b", COR, a)))
            E.frase(c, t, C["s06.c"], [("área mínima", "g", 60), ("→", "g", 58, TINTA2), ("pressão enorme", "g", 60, COR)], XE, 830, passo=0.15)
            for i, (k_, s, cor) in enumerate((("s06.e", "prego: ponta fina", E.COR), ("s06.f", "trator: pneu largo", F.NEG))):
                E.foco(c, t, C[k_], 0.5, lambda a, s=s, cor=cor, i=i: E.pilula(c, s, 1400, 420 + 200 * i, 52, "g", fundo=cor, a=a))
            E.foco(c, t, C["s06.f"] + 0.8, 0.4, lambda a: centro(c, "área grande: pressão pequena", 1400, 740, 46, "i", TINTA2, a))
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    # s07: a cama de pregos
    E.frase(c, t, C["s07.a"], ps("a cama de", "i", 70) + [("pregos", "g", 70, COR)], XE, 190, passo=0.12)
    y = 760
    q = ep(t, C["s07.a"], 0.5)
    if q > 0:
        M.rrect(c, 520, y, 900, 40, 8, MADEIRA, q)
        n = int(lerp(1, 36, ease_io(prog(t, C["s07.c"], 1.0)))) if t >= C["s07.c"] else 1
        for i in range(n):
            x = 560 + (i + 0.5) * 820 / max(n, 1) if n > 1 else 970
            M.line(c, x, y, x, y - 70, TINTA2, q, 5)
        F.bloco(c, 970, y - 120, 760, 100, None, a=q, cor=E.mix(E.COR, BR, 0.3))
    E.frase(c, t, C["s07.b"], [("1 prego:", "g", 58), ("fura", "g", 58, ERRADO)], XE, 330, passo=0.12)
    E.frase(c, t, C["s07.c"], [("centenas:", "g", 58)] + ps("o peso se espalha", "i", 60), XE, 430, passo=0.12)
    E.frase(c, t, C["s07.d"], [("pressão pequena", "g", 58, CERTO)] + ps("em cada ponta", "i", 60), XE, 530, passo=0.12)


# ---------------- atmosfera ----------------
def b_atmosfera(c, t, C, b):
    if t < C["s09"]:
        def s08():
            q = ep(t, C["s08.b"], 0.8)
            if q > 0:
                p = skia.Paint(AntiAlias=True)
                p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, 120), skia.Point(0, 780)], [M.hexc("#8FC8EE", 0.0), M.hexc("#8FC8EE", 0.6 * q)]))
                c.drawRect(skia.Rect.MakeXYWH(1250, 120, 300, 660), p)
                F.chao(c, 1150, 1650, 860, q)
                F.bloco(c, 1400, 820, 70, 80, None, a=q)
            setas_pressao(c, t, C["s08.b"] + 0.4, 1260, 1540, 760, 60, 5)
            E.frase(c, t, C["s08.a"], ps("o ar também faz", "i", 70) + [("pressão", "g", 70, COR)], XE, 200, passo=0.12)
            E.frase(c, t, C["s08.b"], ps("a camada de ar em cima pesa", "i", 58, TINTA2), XE, 300, passo=0.08)
            E.formula_em(c, t, C["s08.c"], "1 atm", XE, 500, 110, "g", COR)
            E.formula_em(c, t, C["s08.d"], "≈ 100.000 Pa", XE, 650, 96, "g", TINTA)
            E.formula_em(c, t, C["s08.e"], "= 1 × 10^5 Pa", XE, 800, 96, "g", TINTA)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("100.000 Pa", "g", 70, COR)] + ps("é muito:", "i", 70), XE, 200, passo=0.12)
            E.frase(c, t, C["s09.b"], ps("como", "i", 64) + [("10 toneladas", "g", 64)] + ps("em cada metro quadrado", "i", 64), XE, 320, passo=0.1)
            cx, cy = 1350, 700
            E.foco(c, t, C["s09.c"] - 0.5, 0.5, lambda a: E.bola(c, cx, cy, 120, E.mix(E.COR, BR, 0.3), a))
            for k in range(12):
                g = 2 * math.pi * k / 12
                ux, uy = math.cos(g), math.sin(g)
                F.seta(c, cx + ux * 260, cy + uy * 260, cx + ux * 135, cy + uy * 135, E.COR, ep(t, C["s09.c"], 0.5), 6, cabeca=18)
                F.seta(c, cx + ux * 30, cy + uy * 30, cx + ux * 105, cy + uy * 105, BR, ep(t, C["s09.d"], 0.5), 5, cabeca=14)
            E.frase(c, t, C["s09.c"], ps("o ar empurra", "i", 58) + [("de todos os lados", "g", 58, COR)], XE, 560, passo=0.1)
            E.frase(c, t, C["s09.d"], ps("o corpo empurra", "i", 58) + [("de volta", "g", 58)], XE, 680, passo=0.1)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    E.frase(c, t, C["s10"], ps("para converter", "i", 70, COR), XE, 200)
    linhas(c, t, [(C["s10.a"], "1 atm = 10^5 Pa", COR), (C["s10.b"], "2 atm = 2 × 10^5 Pa", TINTA), (C["s10.c"], "50.000 Pa = 0,5 atm", TINTA)], XE, 380, 170, 92)
    E.frase(c, t, C["s10.d"], [("Pa → atm:", "g", 60)] + ps("divida por", "i", 62) + [("100.000", "g", 60, COR)], XE, 920, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("área em", "i", 66) + [("cm²", "g", 62)] + ps("na fórmula", "i", 66), XE + 480, 190, passo=0.1)
    E.formula_em(c, t, C["s11.b"], "F = 600 N,   A = 20 cm^2", XE, 360, 80, "g", TINTA2)
    E.formula_em(c, t, C["s11.c"], "600 ÷ 20 =", XE, 520, 96, "g", TINTA)
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.formula(c, "30 Pa", XE + 560, 520, 96, "g", ERRADO, a))
    if t >= C["s11.d"] + 0.6:
        E.risco(c, XE + 540, 540, XE + 880, 450, t, C["s11.d"] + 0.6, largura=12)
    E.formula_em(c, t, C["s11.e"], "20 cm^2 = 0,002 m^2", XE, 700, 84, "g", TINTA)
    E.formula_em(c, t, C["s11.f"], "600 ÷ 0,002 =", XE, 870, 96, "g", TINTA)
    bola_txt(c, t, C["s11.f"] + 0.8, "300.000 Pa", 1420, 840, 175, 54, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s12.a"], ps("conta em", "i", 70, CLARO) + [("N/cm²", "g", 70, BR)], W / 2 - 300, 330, "center", 0.12)
            E.frase(c, t, C["s12.b"], [("× 10.000", "g", 76, BR)] + ps("no final", "i", 70, CLARO), W / 2 + 420, 330, "center", 0.12)
            E.formula_em(c, t, C["s12.c"], "600 ÷ 20 = 30 N/cm^2", W / 2, 540, 96, "g", CLARO, "center")
            E.formula_em(c, t, C["s12.d"], "30 × 10.000 = 300.000 Pa", W / 2, 700, 96, "g", BR, "center")
            E.frase(c, t, C["s12.e"], ps("porque", "i", 60, CLARO) + [("1 m² = 10.000 cm²", "g", 60, BR)], W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("para comparar,", "i", 72, CLARO) + [("nem converta", "g", 72, BR)], W / 2, 300, "center", 0.12)
    E.formula_em(c, t, C["s13.b"], "área ÷ 10  →  pressão × 10", W / 2, 520, 96, "g", BR, "center")
    E.frase(c, t, C["s13.c"], ps("resposta em pascal:", "i", 62, CLARO) + [("converta", "g", 62, BR)], W / 2, 760, "center", 0.12)


# ---------------- questão ----------------
def pessoa(c, cx, chao_y, a=1.0, um_pe=False):
    if a <= 0:
        return
    M.rrect(c, cx - 50, chao_y - 330, 100, 170, 30, E.COR, a)
    E.bola(c, cx, chao_y - 380, 44, E.mix(E.COR, BR, 0.2), a)
    M.rrect(c, cx - 40, chao_y - 170, 30, 170 if True else 0, 10, TINTA, a)
    if um_pe:
        M.rrect(c, cx + 10, chao_y - 170, 30, 120, 10, TINTA, a)
    else:
        M.rrect(c, cx + 10, chao_y - 170, 30, 170, 10, TINTA, a)


def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], [("pessoa de", "i", 66), ("60 kg", "g", 66, COR), ("em pé", "i", 66)], XE, 330, passo=0.12)
    E.frase(c, t, C["s14.b"], [("os dois pés:", "i", 66), ("300 cm²", "g", 66, COR)], XE, 440, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("pressão em", "i", 72) + [("Pa?", "g", 72, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("quanto de", "i", 72) + [("1 atm?", "g", 72, COR)], XE, 760, passo=0.12)
    if t < C["s15"]:
        q = ep(t, C["s14.a"], 0.5)
        if q > 0:
            F.chao(c, 1250, 1650, 900, q)
            pessoa(c, 1450, 900, q)
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "300 cm²", 1450, 960, 40, "g", fundo=E.COR, a=a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s17"]:
        def s16():
            linhas(c, t, [(C["s16.a"], "P = 60 · 10 = 600 N", TINTA), (C["s16.b"], "600 ÷ 300 =", TINTA), (C["s16.d"], "2 × 10.000", TINTA)], XE, 260, 170, 84)
            E.foco(c, t, C["s16.c"], 0.4, lambda a: E.formula(c, "2 N/cm^2", XE + E.formula(None, "600 ÷ 300 = ", 0, 0, 84, a=0), 430, 84, "g", COR, a))
            bola_txt(c, t, C["s16.e"], "20.000 Pa", 1450, 420, 165, 56, CERTO)
            E.formula_em(c, t, C["s16.f"], "1 atm = 100.000 Pa", XE, 800, 76, "g", TINTA2)
            bola_txt(c, t, C["s16.g"], "0,2 atm", 1450, 790, 120, 50, CERTO)
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    E.frase(c, t, C["s17.a"], ps("num pé só?", "i", 80), XE, 300, passo=0.12)
    E.frase(c, t, C["s17.a"] + 1.0, [("área ÷ 2", "g", 72), ("→", "g", 68, TINTA2), ("pressão × 2", "g", 72, COR)], XE, 470, passo=0.15)
    bola_txt(c, t, C["s17.b"], "40.000 Pa", 520, 720, 160, 54, CERTO)
    q = ep(t, C["s17"], 0.5)
    if q > 0:
        F.chao(c, 1250, 1650, 900, q)
        pessoa(c, 1450, 900, q, um_pe=True)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s19"]:
        E.saida(c, t, C["s19"] - 0.1, lambda: resumo(c, t, C, "s18", (
            ("s18.a", [("pressão", "g", 66, COR), ("=", "g", 66, TINTA2), ("força ÷ área", "i", 70)]),
            ("s18.b", [("área em m²", "g", 66), ("→", "g", 62, TINTA2), ("pressão em Pa", "g", 66, COR)]),
            ("s18.c", [("1 atm", "g", 66, COR), ("≈ 10⁵ Pa", "g", 66)]))))
        return

    def desenho():
        q = ep(t, C["s19.a"], 0.6)
        if q <= 0:
            return
        x, y, w, h = 300, 640, 900, 340
        c.drawRect(skia.Rect.MakeXYWH(x, y + 40, w, h - 40), M.paint(AGUA, 0.45 * q))
        M.line(c, x, y + 40, x + w, y + 40, AGUA2, q, 5)
        for X in (x, x + w):
            M.line(c, X, y, X, y + h, TINTA, q, 6)
        M.line(c, x, y + h, x + w, y + h, TINTA, q, 6)
        E.bola(c, x + 600, y + 240, 30, E.COR, q)
        cota(c, t, C["s19.b"], (x + 680, y + 40), (x + 680, y + 240), "h", lado=1, size=50)
    proxima(c, t, C, "s19", [("Lei", "g", 120, COR), ("de", "i", 110), ("Stevin", "g", 120, COR)], None, desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pressao=b_pressao, atmosfera=b_atmosfera, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
