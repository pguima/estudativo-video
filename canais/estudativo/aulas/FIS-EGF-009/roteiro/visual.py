"""Visual — Estudativo · FIS-EGF-009: praticando: hidrostática.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-009_praticando_hidrostatica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "atalho", "questao5", "fim"))

# todas as contas da aula
assert 50 * 10 == 500 and 500 / 1 * 10_000 == 5_000_000 and 5_000_000 / 100_000 == 50 and 500 / 250 * 10_000 == 20_000
assert abs(12 / 0.8 - 15) < 1e-9 and abs(0.8 * 15 - 12) < 1e-9 and (10 / 2) ** 2 == 25 and 5000 / 25 == 200 and 5000 / 5 == 1000
assert 50 - 30 == 20 and 20 / 10 == 2 and 50 / 10 / 2 == 2.5 and 50 / 20 == 2.5 and 0.9 < 1 and 0.9 > 0.8


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


# ---------------- peças desta aula (tubo em U, prensa, balança e gelo copiados das FIS-EGF-005, 006 e 008) ----------------
GELO = "#EAF6FF"


def situacao(c, t, t0, n, titulo):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, 160, 44, a=a), centro(c, str(n), XE + 40, 180, 54, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("situação", "i", 66), (titulo, "g", 62, COR)], XE + 110, 180, passo=0.12)


def enunciado(c, t, C, cena, n, titulo, linhas, desenho):
    situacao(c, t, C[cena], n, titulo)
    for t0, partes, y in linhas:
        E.frase(c, t, t0, partes, XE, y, passo=0.1)
    pausa = f"s{int(cena[1:]) + 1:02d}"
    if t < C[pausa]:
        desenho()
    else:
        E.relogio(c, t, C[pausa + ".a"], cx=1480, cy=480, r=200)


def tubo_u(c, t, t0, cx, yb, k, h_oleo, h_agua, a=1.0):
    """tubo em U: água embaixo e à esquerda; óleo à direita sobre a água. Alturas em cm, k = px por cm"""
    q = ep(t, t0, 0.6) * a
    w, gap = 120, 300
    xL, xR = cx - gap / 2 - w, cx + gap / 2
    y_sep = yb - 120
    y_ag, y_ol = y_sep - h_agua * k, y_sep - h_oleo * k
    if q <= 0:
        return y_sep, y_ag, y_ol, xL, xR
    agua, oleo = M.paint(AGUA, 0.55 * q), M.paint(OLEO, 0.65 * q)
    c.drawRect(skia.Rect.MakeLTRB(xL, y_ag, xL + w, yb), agua)
    c.drawRect(skia.Rect.MakeLTRB(xL, yb - 120, xR + w, yb), agua)
    c.drawRect(skia.Rect.MakeLTRB(xR, y_sep, xR + w, yb), agua)
    c.drawRect(skia.Rect.MakeLTRB(xR, y_ol, xR + w, y_sep), oleo)
    top = min(y_ag, y_ol) - 100
    p = skia.Path()
    p.moveTo(xL, top); p.lineTo(xL, yb); p.lineTo(xR + w, yb); p.lineTo(xR + w, top)
    p.moveTo(xL + w, top); p.lineTo(xL + w, yb - 120); p.lineTo(xR, yb - 120); p.lineTo(xR, top)
    c.drawPath(p, M.paint(TINTA, q, stroke=6))
    return y_sep, y_ag, y_ol, xL, xR


def prensa(c, x1, w1, x2, w2, yb, n1, n2, a=1.0, carro=None, canal=70):
    if a <= 0:
        return
    oleo = M.paint(OLEO, 0.6 * a)
    y1, y2 = yb - n1, yb - n2
    c.drawRect(skia.Rect.MakeLTRB(x1 - w1 / 2, y1, x1 + w1 / 2, yb), oleo)
    c.drawRect(skia.Rect.MakeLTRB(x2 - w2 / 2, y2, x2 + w2 / 2, yb), oleo)
    c.drawRect(skia.Rect.MakeLTRB(x1 + w1 / 2, yb - canal, x2 - w2 / 2, yb), oleo)
    top = yb - 520
    p = skia.Path()
    p.moveTo(x1 - w1 / 2, top); p.lineTo(x1 - w1 / 2, yb); p.lineTo(x2 + w2 / 2, yb); p.lineTo(x2 + w2 / 2, top)
    p.moveTo(x1 + w1 / 2, top); p.lineTo(x1 + w1 / 2, yb - canal); p.lineTo(x2 - w2 / 2, yb - canal); p.lineTo(x2 - w2 / 2, top)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    M.rrect(c, x1 - w1 / 2 + 4, y1 - 22, w1 - 8, 22, 4, "#2A2A30", a)
    M.rrect(c, x2 - w2 / 2 + 4, y2 - 26, w2 - 8, 26, 4, "#2A2A30", a)
    if carro:
        F.bloco(c, x2, y2 - 26 - 70, w2 * 0.8, 140, carro, a=a, size=38)


def balanca_gancho(c, x, y_top, leitura, a=1.0):
    if a <= 0:
        return x, y_top + 260
    M.line(c, x, y_top - 60, x, y_top, TINTA, a, 5)
    M.rrect(c, x - 90, y_top, 180, 200, 24, "#2A2A30", a)
    M.rrect(c, x - 70, y_top + 30, 140, 70, 10, "#DDEFE3", a)
    centro(c, leitura, x, y_top + 82, 44, "g", TINTA, a)
    M.line(c, x, y_top + 200, x, y_top + 260, TINTA, a, 5)
    return x, y_top + 260


def copo(c, x, y, w, h, nivel, cor, a=1.0):
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - nivel, w, nivel), M.paint(cor, 0.5 * a))
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x, y + h); p.lineTo(x + w, y + h); p.lineTo(x + w, y)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))


def cubo_gelo(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s / 2, cy - s / 2, s, s, 14, GELO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), 14, 14), M.paint(AGUA2, a, stroke=4))


def salto(c, cx, chao_y, a=1.0):
    """sapato de salto fino, de lado; o salto toca o chão em cx"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 6, chao_y); p.lineTo(cx + 6, chao_y); p.lineTo(cx + 18, chao_y - 120); p.lineTo(cx + 40, chao_y - 150)
    p.lineTo(cx + 260, chao_y - 20); p.lineTo(cx + 270, chao_y); p.lineTo(cx + 170, chao_y); p.lineTo(cx + 40, chao_y - 100)
    p.lineTo(cx + 10, chao_y - 110); p.close()
    c.drawPath(p, M.paint(E.COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 110)], XE, 380, passo=0.2)
    E.frase(c, t, C["s01.a"] + 1.0, ps("com líquidos e pressão", "i", 60, TINTA2), XE, 480, passo=0.1)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: (salto(c, 1060, 480, a), centro(c, "salto alto", 1180, 560, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s01.c"], 0.5, lambda a: (copo(c, 1500, 260, 220, 240, 200, OLEO, a), cubo_gelo(c, 1610, 440, 80, a),
                                              centro(c, "gelo que afunda", 1610, 560, 46, "i", TINTA2, a)))
    E.frase(c, t, C["s01.d"], ps("pause o vídeo e", "i", 70) + [("resolva antes", "g", 70, COR)], XE, 780, passo=0.12)


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s02", (("s02.a", "pressão:", "p = F / A"), ("s02.b", "Stevin:", "p = p₀ + d · g · h"),
                              ("s02.c", "Pascal:", "F₁ / A₁ = F₂ / A₂"), ("s02.d", "empuxo:", "E = d · V · g")), 4, "ferramentas")


# ---------------- situação 1: o salto ----------------
def b_questao1(c, t, C, b):
    def desenho():
        q = ep(t, C["s03.b"], 0.5)
        if q > 0:
            F.chao(c, 1150, 1750, 760, q)
            salto(c, 1300, 760, q)
        E.foco(c, t, C["s03.c"], 0.4, lambda a: E.pilula(c, "1 cm²", 1300, 830, 44, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s03.e"], 0.4, lambda a: (M.rrect(c, 1400, 860, 320, 60, 28, TINTA2, a), centro(c, "tênis: 250 cm²", 1560, 970, 44, "b", TINTA, a)))
    enunciado(c, t, C, "s03", 1, "o salto fino", [
        (C["s03.b"], [("pessoa de", "i", 60), ("50 kg", "g", 60, COR)], 320),
        (C["s03.c"], [("salto de", "i", 60), ("1 cm²", "g", 60, COR)], 430),
        (C["s03.d"], [("pressão em", "i", 64), ("Pa", "g", 64, COR), ("e", "i", 64), ("atm?", "g", 64, COR)], 600),
        (C["s03.e"], [("e com tênis de", "i", 64), ("250 cm²?", "g", 64, COR)], 720)], desenho)


def b_resposta1(c, t, C, b):
    linhas(c, t, [(C["s05.a"], "P = 500 N", TINTA), (C["s05.b"], "500 ÷ 1 = 500 N/cm^2", TINTA), (C["s05.c"], "× 10.000", TINTA)], XE, 220, 140, 72)
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.formula(c, "= 5.000.000 Pa", XE + E.formula(None, "× 10.000 ", 0, 0, 72, a=0), 500, 72, "g", COR, a))
    E.formula_em(c, t, C["s05.e"], "÷ 100.000  =", XE, 640, 72, "g", TINTA)
    bola_txt(c, t, C["s05.e"] + 0.5, "50 atm", 1450, 400, 150, 60, CERTO)
    E.frase(c, t, C["s05.f"], [("tênis:", "g", 58), ("área × 250", "g", 58), ("→", "g", 56, TINTA2), ("pressão ÷ 250", "g", 58, COR)], XE, 820, passo=0.12)
    E.formula_em(c, t, C["s05.g"] + 1.2, "= 20.000 Pa = 0,2 atm", XE, 950, 64, "g", CERTO)


# ---------------- situação 2: tubo em U ----------------
def b_questao2(c, t, C, b):
    def desenho():
        k = 18
        ys, ya, yo, xL, xR = tubo_u(c, t, C["s06.b"], 1450, 960, k, 15, 12)
        if t >= C["s06.c"]:
            M.line(c, xL - 60, ys, xR + 180, ys, E.COR, ep(t, C["s06.c"], 0.5), 4, dash=E.TRACO)
        cota(c, t, C["s06.c"], (xL - 40, ys), (xL - 40, ya), "12 cm", lado=-1, size=42)
        E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "h = ?", xR + 150, (ys + yo) / 2 + 16, 50, "g", COR, a))
        E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: (centro(c, "água", xL + 60, 1010, 44, "b", AGUA2, a), centro(c, "óleo", xR + 60, yo - 30, 44, "b", "#9A6B10", a)))
    enunciado(c, t, C, "s06", 2, "o tubo em U", [
        (C["s06.b"], ps("água e óleo", "i", 60), 320),
        (C["s06.c"], [("água:", "i", 60), ("12 cm", "g", 60, AGUA2), ("acima da separação", "i", 56)], 430),
        (C["s06.d"], [("óleo:", "i", 60), ("0,8 g/cm³", "g", 60, "#9A6B10")], 540),
        (C["s06.e"], [("altura do óleo?", "g", 66, COR)], 700)], desenho)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08.a"], ps("na separação:", "i", 60) + [("mesma pressão", "g", 60, COR)], XE, 220, passo=0.12)
    linhas(c, t, [(C["s08.b"], "d · h (óleo) = d · h (água)", TINTA), (C["s08.c"], "0,8 · h = 1 · 12", TINTA), (C["s08.d"], "h = 12 ÷ 0,8", TINTA)], XE, 380, 150, 72)
    bola_txt(c, t, C["s08.e"], "15 cm", 1450, 520, 150, 64, CERTO)
    E.frase(c, t, C["s08.f"], ps("menos denso:", "i", 56) + [("mais alto", "g", 56, COR)], XE, 900, passo=0.1)
    E.formula_em(c, t, C["s08.f"] + 1.4, "confira: 0,8 · 15 = 12", XE + 700, 900, 56, "g", TINTA2)


# ---------------- situação 3: prensa com diâmetros ----------------
def b_questao3(c, t, C, b):
    def desenho():
        q = ep(t, C["s09.b"], 0.5)
        prensa(c, 1250, 60, 1620, 300, 920, 330, 230, q, carro="5.000 N")
        E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.pilula(c, "2 cm", 1250, 980, 40, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "10 cm", 1620, 980, 40, "g", fundo=TINTA, a=a))
    enunciado(c, t, C, "s09", 3, "a prensa", [
        (C["s09.b"], [("diâmetro pequeno:", "i", 60), ("2 cm", "g", 60, COR)], 320),
        (C["s09.c"], [("grande:", "i", 60), ("10 cm", "g", 60, COR)], 430),
        (C["s09.d"], [("força para", "i", 64), ("5.000 N?", "g", 64, COR)], 600)], desenho)


def b_resposta3(c, t, C, b):
    linhas(c, t, [(C["s11.a"], "diâmetros: 10 ÷ 2 = 5", TINTA), (C["s11.b"], "áreas: 5^2 = 25", COR), (C["s11.c"], "5.000 ÷ 25", TINTA)], XE, 240, 160, 76)
    bola_txt(c, t, C["s11.d"], "200 N", 1450, 400, 140, 64, CERTO)
    E.formula_em(c, t, C["s11.e"], "5.000 ÷ 5 = 1.000 N", XE, 820, 72, "g", ERRADO)
    if t >= C["s11.e"] + 1.0:
        E.risco(c, XE - 10, 840, XE + 760, 760, t, C["s11.e"] + 1.0, largura=10)
    E.frase(c, t, C["s11.e"] + 1.6, ps("cinco vezes mais força do que precisa", "i", 52, TINTA2), XE, 940, passo=0.08)


# ---------------- situação 4: peso aparente ----------------
def balanca_cena(c, t, t0, leitura, dentro, a=1.0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    ys = 680
    c.drawRect(skia.Rect.MakeXYWH(1250, ys, 460, 340), M.paint(AGUA, 0.45 * q))
    M.line(c, 1250, ys, 1710, ys, AGUA2, q, 5)
    hx, hy = balanca_gancho(c, 1480, 200, leitura, q)
    M.line(c, hx, hy, hx, hy + 50 + 200 * dentro, TINTA2, q, 3)
    F.bloco(c, hx, hy + 130 + 200 * dentro, 150, 150, None, a=q, cor=TINTA2)


def b_questao4(c, t, C, b):
    dentro = ease_io(prog(t, C["s12.c"], 1.0))
    enunciado(c, t, C, "s12", 4, "a balança de gancho", [
        (C["s12.b"], [("no ar:", "i", 60), ("50 N", "g", 60, COR)], 320),
        (C["s12.c"], [("na água:", "i", 60), ("30 N", "g", 60, F.NEG)], 430),
        (C["s12.d"], [("volume?", "g", 66, COR)], 600),
        (C["s12.e"], [("densidade?", "g", 66, COR)], 710)],
        lambda: balanca_cena(c, t, C["s12.b"], "50 N" if t < C["s12.c"] + 0.6 else "30 N", dentro))


def b_resposta4(c, t, C, b):
    E.formula_em(c, t, C["s14.a"], "E = 50 − 30 = 20 N", XE, 230, 76, "g", F.NEG)
    E.formula_em(c, t, C["s14.c"], "1 L → 10 N:", XE, 380, 68, "g", TINTA2)
    bola_txt(c, t, C["s14.d"], "V = 2 L", 1000, 360, 110, 46, CERTO)
    E.formula_em(c, t, C["s14.e"], "m = 50 N ÷ 10 = 5 kg", XE, 560, 72, "g", TINTA)
    E.formula_em(c, t, C["s14.f"], "d = 5 kg ÷ 2 L", XE, 720, 72, "g", TINTA)
    bola_txt(c, t, C["s14.g"], "2,5 g/cm³", 1450, 700, 165, 46, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], ps("guarde o atalho", "i", 76, CLARO), W / 2, 170, "center")
    E.frase(c, t, C["s15.a"], [("N que somem", "g", 66, BR), ("÷ 10", "g", 66, CLARO), ("=", "g", 62, CLARO), ("litros", "g", 66, BR)], W / 2, 340, "center", 0.12)
    E.frase(c, t, C["s15.b"], [("peso no ar", "g", 66, BR), ("÷", "g", 62, CLARO), ("o que sumiu", "g", 66, BR)], W / 2, 500, "center", 0.12)
    E.formula_em(c, t, C["s15.c"], "50 ÷ 20 = 2,5 g/cm^3", W / 2, 670, 92, "g", CLARO, "center")
    E.frase(c, t, C["s15.d"], ps("o peso tem a densidade do corpo; o empuxo, a da água:", "i", 50, CLARO) + [("1", "g", 54, BR)], W / 2, 840, "center", 0.06)
    E.frase(c, t, C["s15.e"], ps("outro líquido:", "i", 58, CLARO) + [("× a densidade dele", "g", 56, BR)], W / 2, 960, "center", 0.1)


# ---------------- situação 5: gelo na água e no óleo ----------------
def dois_copos(c, t, t0, tagua, toleo, resolvido=False):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    for x, cor, k_, nome in ((1150, AGUA, tagua, "água"), (1520, OLEO, toleo, "óleo 0,8")):
        copo(c, x, 360, 280, 560, 460, cor, q)
        centro(c, nome, x + 140, 990, 44, "b", TINTA2, q)
        if t >= k_:
            fundo = x != 1150
            fim = (920 - 52) if fundo else (920 - 460 + 40)  # no óleo, no fundo; na água, 9/10 abaixo da superfície
            cy = fim if resolvido else lerp(300, fim, ease_io(prog(t, k_, 1.2)))
            cubo_gelo(c, x + 140, cy, 100, ep(t, k_, 0.3))


def b_questao5(c, t, C, b):
    enunciado(c, t, C, "s16", 5, "o gelo", [
        (C["s16.b"], [("gelo:", "i", 60), ("0,9 g/cm³", "g", 60, COR)], 320),
        (C["s16.c"], [("um na", "i", 60), ("água", "g", 60, AGUA2)], 430),
        (C["s16.d"], [("outro no", "i", 60), ("óleo, 0,8", "g", 60, "#9A6B10")], 540),
        (C["s16.e"], [("o que acontece?", "g", 66, COR)], 700)],
        lambda: dois_copos(c, t, C["s16.b"], C["s16.c"] + 99, C["s16.d"] + 99))


def b_resposta5(c, t, C, b):
    dois_copos(c, t, C["s18"], C["s18.b"], C["s18.f"])
    E.formula_em(c, t, C["s18.a"], "água: 0,9 < 1", XE, 260, 72, "g", TINTA)
    E.frase(c, t, C["s18.b"], [("boia,", "g", 60, CERTO)], XE, 380)
    E.frase(c, t, C["s18.c"], [("9/10", "g", 60, AGUA2)] + ps("dentro", "i", 62), XE + 200, 380, passo=0.12)
    E.formula_em(c, t, C["s18.d"], "óleo: 0,9 > 0,8", XE, 580, 72, "g", TINTA)
    E.frase(c, t, C["s18.e"], ps("mais denso que o óleo:", "i", 56), XE, 700, passo=0.1)
    E.frase(c, t, C["s18.f"], [("afunda", "g", 66, ERRADO)], XE, 800)
    E.frase(c, t, C["s18.f"] + 1.4, ps("não é truque: é densidade", "i", 54, TINTA2), XE, 920, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s20"]:
        E.saida(c, t, C["s20"] - 0.1, lambda: resumo(c, t, C, "s19", (
            ("s19.a", [("área em m² → Pa;", "g", 56), ("prensa:", "i", 60), ("mesma unidade", "g", 56, COR)]),
            ("s19.b", [("mesma altura, mesmo líquido:", "i", 60), ("mesma pressão", "g", 56, COR)]),
            ("s19.c", [("prensa:", "i", 60), ("diâmetros ao quadrado", "g", 56, COR)]),
            ("s19.d", [("densidade", "g", 58, COR), ("decide quem boia", "i", 60)]))))
        return

    def desenho():
        q = ep(t, C["s20.b"], 0.6)
        if q <= 0:
            return
        c.drawRect(skia.Rect.MakeLTRB(250, 760, 700, 900), M.paint(AGUA, 0.5 * q))
        c.drawRect(skia.Rect.MakeLTRB(700, 800, 1150, 860), M.paint(AGUA, 0.5 * q))
        M.line(c, 250, 760, 700, 760, TINTA, q, 5); M.line(c, 250, 900, 700, 900, TINTA, q, 5)
        M.line(c, 700, 760, 700, 800, TINTA, q, 5); M.line(c, 700, 860, 700, 900, TINTA, q, 5)
        M.line(c, 700, 800, 1150, 800, TINTA, q, 5); M.line(c, 700, 860, 1150, 860, TINTA, q, 5)
        for i in range(3):
            x = 320 + i * 120
            F.seta(c, x, 830, x + 60, 830, F.VEL, q, 6, cabeca=16)
        for i in range(3):
            x = 760 + ((t * 300 + i * 130) % 380)
            F.seta(c, x, 830, x + 90, 830, F.VEL, q, 6, cabeca=16)
    proxima(c, t, C, "s20", [("Vazão", "g", 120, COR), ("e", "i", 110)], [("continuidade", "g", 110, COR)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              atalho=b_atalho, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
