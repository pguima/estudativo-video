"""Visual — Estudativo · FIS-EGF-012: praticando: vazão e Bernoulli.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-012_praticando_vazao_e_bernoulli.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))

# todas as contas da aula
assert 4 * 250 == 1000 and 1000 / 1 == 1000 == 16 * 60 + 40 and 30 * 2 == 60 and 10 * 3 == 30 and 60 * 1 / 30 == 2
assert 1000 / 2 * (6 ** 2 - 2 ** 2) == 16000 and (6 + 2) * (6 - 2) == 32 and (70 + 60) * (70 - 60) == 70 ** 2 - 60 ** 2 == 1300
assert abs(1.2 / 2 * 1300 - 780) < 1e-9 and 780 * 20 == 15600 and math.isqrt(20 * 5) == 10 and abs((20 * 1.25) ** 0.5 - 5) < 1e-9


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


# ---------------- peças desta aula (cano, fluxo, asa e tanque copiados das FIS-EGF-010 e 011) ----------------
def cano(c, x0, x1, xm, y, h1, h2, a=1.0, cor=AGUA, trans=60):
    def meia(x):
        if x <= xm - trans / 2:
            return h1 / 2
        if x >= xm + trans / 2:
            return h2 / 2
        return lerp(h1 / 2, h2 / 2, ease_io((x - xm + trans / 2) / trans))
    if a <= 0:
        return meia
    n = 60
    xs = [lerp(x0, x1, i / n) for i in range(n + 1)]
    top = [(x, y - meia(x)) for x in xs]
    bot = [(x, y + meia(x)) for x in reversed(xs)]
    p = skia.Path(); p.addPoly(top + bot, True)
    c.drawPath(p, M.paint(cor, 0.5 * a))
    for pts in (top, bot):
        pp = skia.Path(); pp.addPoly(pts, False)
        c.drawPath(pp, M.paint(TINTA, a, stroke=6))
    return meia


def fluxo(c, t, t0, x0, x1, xm, y, h1, h2, v1, a=1.0, n_lin=3, esp=150):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    v2 = v1 * h1 / h2
    for j in range(n_lin):
        fy = (j + 0.5) / n_lin - 0.5
        for xa, xb, v, hh in ((x0, xm, v1, h1), (xm, x1, v2, h2)):
            passo = esp * (v / v1)
            off = ((t - t0) * v) % passo
            x = xa + off - passo
            while x < xb:
                if x >= xa + 10 and x + 40 <= xb:
                    yy = y + fy * hh * 0.8
                    F.seta(c, x, yy, x + 22 + 18 * (v / v1), yy, F.VEL, q, 5, cabeca=14)
                x += passo


def asa(c, cx, cy, s, a=1.0, ang=-6):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    p = skia.Path()
    p.moveTo(-s, 0); p.cubicTo(-s * 0.7, -s * 0.32, s * 0.3, -s * 0.3, s, 0)
    p.cubicTo(s * 0.3, s * 0.06, -s * 0.7, s * 0.12, -s, 0); p.close()
    c.drawPath(p, M.paint("#B9BCC4", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))
    c.restore()


def tanque_furo(c, t, t0, x, y, w, h, nivel, furo_y, jato=0.0, a=1.0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    ys = y + h - nivel
    c.drawRect(skia.Rect.MakeLTRB(x, ys, x + w, y + h), M.paint(AGUA, 0.5 * q))
    M.line(c, x, ys, x + w, ys, AGUA2, q, 5)
    M.line(c, x, y, x, y + h, TINTA, q, 6)
    M.line(c, x, y + h, x + w, y + h, TINTA, q, 6)
    M.line(c, x + w, y, x + w, furo_y - 12, TINTA, q, 6)
    M.line(c, x + w, furo_y + 12, x + w, y + h, TINTA, q, 6)
    if jato > 0:
        alc = 340 * jato
        pts = [(x + w + alc * s, furo_y + 300 * s * s) for s in [i / 30 for i in range(31)]]
        F.poli(c, pts, 1.0, AGUA2, q, 16)


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


def caixa_dagua(c, x, y, w, h, nivel, a=1.0):
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - nivel, w, nivel), M.paint(AGUA, 0.5 * a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=6))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 110)], XE, 380, passo=0.2)
    E.frase(c, t, C["s01.a"] + 1.0, ps("com fluidos em movimento", "i", 60, TINTA2), XE, 480, passo=0.1)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: (caixa_dagua(c, 1050, 260, 220, 200, 120, a), centro(c, "caixa d'água", 1160, 540, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s01.c"], 0.5, lambda a: (asa(c, 1600, 360, 170, a), centro(c, "asa", 1600, 540, 46, "i", TINTA2, a)))
    E.frase(c, t, C["s01.d"], ps("pause o vídeo e", "i", 70) + [("resolva antes", "g", 70, COR)], XE, 780, passo=0.12)


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s02", (("s02.a", "vazão:", "Q = A · v"), ("s02.b", "continuidade:", "A₁ · v₁ = A₂ · v₂"),
                              ("s02.c", "Bernoulli:", "mais rápido, menos pressão; v = √(2gh)")), 3, "ferramentas")


# ---------------- situação 1: a caixa d'água ----------------
def b_questao1(c, t, C, b):
    def desenho():
        q = ep(t, C["s03.b"], 0.5)
        cano(c, 1050, 1500, 1500, 360, 90, 90, q)
        fluxo(c, t, C["s03.c"], 1050, 1500, 1499, 360, 90, 90, 140, n_lin=2)
        E.foco(c, t, C["s03.d"], 0.5, lambda a: (caixa_dagua(c, 1500, 460, 300, 420, 200, a), centro(c, "1.000 L", 1650, 940, 46, "b", TINTA, a)))
        E.foco(c, t, C["s03.b"] + 0.3, 0.4, lambda a: E.pilula(c, "4 cm²", 1270, 270, 40, "g", fundo=TINTA, a=a))
    enunciado(c, t, C, "s03", 1, "a caixa d'água", [
        (C["s03.b"], [("cano de", "i", 60), ("4 cm²", "g", 60, COR)], 330),
        (C["s03.c"], [("água a", "i", 60), ("2,5 m/s", "g", 60, F.VEL)], 440),
        (C["s03.d"], [("tempo para", "i", 64), ("1.000 L?", "g", 64, COR)], 620)], desenho)


def b_resposta1(c, t, C, b):
    linhas(c, t, [(C["s05.a"], "2,5 m/s = 250 cm/s", TINTA2), (C["s05.b"], "Q = 4 · 250", TINTA), (C["s05.c"], "= 1.000 cm^3/s", TINTA)], XE, 240, 150, 76)
    bola_txt(c, t, C["s05.d"], "1 L/s", 1450, 340, 120, 60)
    E.formula_em(c, t, C["s05.e"], "t = 1.000 L ÷ 1 L/s", XE, 760, 76, "g", TINTA)
    bola_txt(c, t, C["s05.f"], "1.000 s", 1450, 730, 130, 54, CERTO)
    E.foco(c, t, C["s05.f"] + 0.8, 0.4, lambda a: E.pilula(c, "16 min 40 s", 1450, 920, 44, "g", fundo=TINTA, a=a))


# ---------------- situação 2: o rio ----------------
def secao(c, x, y, w, h, rot, a=1.0):
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(AGUA, 0.55 * a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(AGUA2, a, stroke=4))
    centro(c, rot, x + w / 2, y + h + 56, 42, "b", TINTA, a)


def b_questao2(c, t, C, b):
    k = 16

    def desenho():
        secao(c, 1080, 380, 30 * k, 2 * k * 4, "30 m × 2 m", ep(t, C["s06.b"], 0.5))
        secao(c, 1660, 380, 10 * k, 3 * k * 4, "10 m × 3 m", ep(t, C["s06.d"], 0.5))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "1 m/s", 1320, 320, 40, "g", fundo=F.VEL, a=a))
        E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "v = ?", 1740, 320, 40, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s06.b"] + 0.3, 0.4, lambda a: centro(c, "seções do rio (fora de escala)", 1400, 760, 38, "i", TINTA2, a))
    enunciado(c, t, C, "s06", 2, "o rio", [
        (C["s06.b"], [("30 m", "g", 60), ("de largura,", "i", 60), ("2 m", "g", 60), ("de fundo", "i", 60)], 330),
        (C["s06.c"], [("a", "i", 60), ("1 m/s", "g", 60, F.VEL)], 440),
        (C["s06.d"], [("estreito:", "i", 60), ("10 m", "g", 60), ("e", "i", 60), ("3 m", "g", 60)], 550),
        (C["s06.e"], [("velocidade ali?", "g", 66, COR)], 710)], desenho)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08"], ps("a seção é um", "i", 60) + [("retângulo", "g", 60, COR)], XE, 200, passo=0.12)
    linhas(c, t, [(C["s08.a"], "A₁ = 30 · 2 = 60 m^2", TINTA), (C["s08.b"], "A₂ = 10 · 3 = 30 m^2", TINTA), (C["s08.c"], "60 · 1 = 30 · v", TINTA)], XE, 360, 150, 76)
    bola_txt(c, t, C["s08.d"], "2 m/s", 1450, 480, 130, 60, CERTO)
    E.frase(c, t, C["s08.e"], [("área ÷ 2", "g", 62), ("→", "g", 58, TINTA2), ("velocidade × 2", "g", 62, F.VEL)], XE, 900, passo=0.15)


# ---------------- situação 3: o cano que afina ----------------
def b_questao3(c, t, C, b):
    def desenho():
        q = ep(t, C["s09.b"], 0.5)
        cano(c, 1000, 1800, 1400, 520, 210, 70, q)
        fluxo(c, t, C["s09.b"], 1000, 1800, 1400, 520, 210, 70, 60, n_lin=2)
        E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: (E.pilula(c, "2 m/s", 1200, 360, 40, "g", fundo=F.VEL, a=a), E.pilula(c, "6 m/s", 1600, 430, 40, "g", fundo=F.VEL, a=a)))
    enunciado(c, t, C, "s09", 3, "o cano que afina", [
        (C["s09.b"], [("de", "i", 60), ("2", "g", 60), ("para", "i", 60), ("6 m/s", "g", 60, F.VEL)], 330),
        (C["s09.c"], [("quanto a pressão", "i", 64), ("cai?", "g", 64, COR)], 500)], desenho)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("cano deitado:", "g", 56)] + ps("a altura não muda", "i", 58), XE, 200, passo=0.1)
    E.formula_em(c, t, C["s11.b"], "queda = f{d}{2} · (v₂^2 − v₁^2)", XE, 360, 80, "g", TINTA)
    E.formula_em(c, t, C["s11.c"], "= 500 ·", XE, 540, 80, "g", TINTA)
    E.formula_em(c, t, C["s11.d"], "(36 − 4) = 500 · 32", XE + 300, 540, 80, "g", TINTA)
    bola_txt(c, t, C["s11.f"], "16.000 Pa", 1450, 800, 160, 52, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("um atalho de conta", "i", 76, CLARO), W / 2, 170, "center")
    E.formula_em(c, t, C["s12.a"], "a^2 − b^2 = (a + b) · (a − b)", W / 2, 360, 100, "g", BR, "center")
    E.formula_em(c, t, C["s12.b"], "6^2 − 2^2", W / 2 - 300, 560, 90, "g", CLARO, "center")
    E.formula_em(c, t, C["s12.c"], "= 8 · 4", W / 2 + 100, 560, 90, "g", CLARO, "center")
    E.formula_em(c, t, C["s12.d"], "= 32", W / 2 + 420, 560, 90, "g", BR, "center")
    E.formula_em(c, t, C["s12.e"], "70^2 − 60^2 = 130 · 10", W / 2, 760, 90, "g", BR, "center")
    E.frase(c, t, C["s12.f"], ps("com números pequenos,", "i", 58, CLARO) + [("tanto faz", "g", 58, BR)], W / 2, 920, "center", 0.1)


# ---------------- situação 4: a asa ----------------
def b_questao4(c, t, C, b):
    def desenho():
        q = ep(t, C["s13.b"], 0.5)
        asa(c, 1400, 600, 330, q)
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.pilula(c, "70 m/s", 1400, 380, 44, "g", fundo=F.VEL, a=a))
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "60 m/s", 1400, 820, 44, "g", fundo=F.VEL, a=a))
        E.foco(c, t, C["s13.e"], 0.4, lambda a: centro(c, "A = 20 m²", 1400, 960, 46, "b", TINTA, a))
    enunciado(c, t, C, "s13", 4, "a asa", [
        (C["s13.b"], [("por cima:", "i", 58), ("70 m/s", "g", 58, F.VEL)], 320),
        (C["s13.c"], [("por baixo:", "i", 58), ("60 m/s", "g", 58, F.VEL)], 420),
        (C["s13.d"], [("ar:", "i", 58), ("1,2 kg/m³", "g", 58)], 520),
        (C["s13.e"], [("asa:", "i", 58), ("20 m²", "g", 58)], 620),
        (C["s13.f"], [("sustentação?", "g", 66, COR)], 770)], desenho)


def b_resposta4(c, t, C, b):
    if t < C["s16"]:
        def s15():
            E.formula_em(c, t, C["s15.a"], "f{1,2}{2} = 0,6", XE, 240, 80, "g", TINTA)
            E.formula_em(c, t, C["s15.b"], "× (70^2 − 60^2)", XE + 420, 240, 80, "g", TINTA)
            E.formula_em(c, t, C["s15.c"], "atalho: 130 · 10", XE, 450, 80, "g", TINTA2)
            E.formula_em(c, t, C["s15.d"], "= 1.300", XE + 620, 450, 80, "g", TINTA)
            E.formula_em(c, t, C["s15.e"], "0,6 · 1.300", XE, 650, 80, "g", TINTA)
            bola_txt(c, t, C["s15.f"], "780 Pa", 1300, 620, 130, 56)
        E.saida(c, t, C["s16"] - 0.1, s15)
        return
    E.frase(c, t, C["s16.a"], [("F = p · A", "g", 76, COR)] + ps("(pressão vezes área)", "i", 60, TINTA2), XE, 280, passo=0.12)
    E.formula_em(c, t, C["s16.b"], "780 · 20", XE, 480, 90, "g", TINTA)
    bola_txt(c, t, C["s16.c"], "15.600 N", 1350, 460, 160, 52, CERTO)
    q = ep(t, C["s16.c"], 0.5)
    asa(c, 1350, 840, 260, q)
    F.forca(c, t, C["s16.c"] + 0.3, (1350, 800), 90, 150, None, lado=1)


# ---------------- situação 5: o tanque que esvazia ----------------
def b_questao5(c, t, C, b):
    def desenho():
        furo_y = 320 + 600 - 60
        nivel = lerp(560, 560 / 4 + 60 * 0.75, ease_io(prog(t, C["s17.d"], 1.4)))
        tanque_furo(c, t, C["s17.b"], 1350, 320, 320, 600, nivel, furo_y, 1.0 if t < C["s17.d"] else lerp(1.0, 0.5, ease_io(prog(t, C["s17.d"], 1.4))))
        E.foco(c, t, C["s17.b"] + 0.3, 0.4, lambda a: E.escreve(c, "5 m" if t < C["s17.d"] else "1,25 m", 1330 - E.larg("1,25 m", "b", 46), 600, 46, "b", COR, a))
    enunciado(c, t, C, "s17", 5, "o tanque", [
        (C["s17.b"], [("furo", "i", 60), ("5 m", "g", 60, COR), ("abaixo do nível", "i", 60)], 330),
        (C["s17.c"], [("velocidade?", "g", 66, COR)], 470),
        (C["s17.d"], [("e com o nível a", "i", 60), ("1,25 m?", "g", 60, COR)], 600)], desenho)


def b_resposta5(c, t, C, b):
    E.formula_em(c, t, C["s19.a"], "v^2 = 20 · h", XE, 230, 84, "g", COR)
    E.formula_em(c, t, C["s19.b"], "h = 5:  v^2 = 100", XE, 400, 76, "g", TINTA)
    bola_txt(c, t, C["s19.c"], "10 m/s", 1300, 370, 95, 46, CERTO)
    E.formula_em(c, t, C["s19.d"], "h = 1,25:  v^2 = 25", XE, 600, 76, "g", TINTA)
    bola_txt(c, t, C["s19.e"], "5 m/s", 1300, 600, 95, 46, CERTO)
    E.frase(c, t, C["s19.f"], [("altura ÷ 4", "g", 60), ("→", "g", 56, TINTA2), ("velocidade ÷ 2", "g", 60, F.VEL)], XE, 820, passo=0.15)
    E.frase(c, t, C["s19.g"], ps("a velocidade acompanha a", "i", 58) + [("raiz da altura", "g", 58, COR)], XE, 940, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s21"]:
        E.saida(c, t, C["s21"] - 0.1, lambda: resumo(c, t, C, "s20", (
            ("s20.a", [("Q = A · v,", "g", 64, COR), ("igual em todo o cano", "i", 70)]),
            ("s20.b", [("corre mais,", "i", 70), ("a pressão cai", "g", 64, COR)]),
            ("s20.c", [("furo:", "i", 70), ("v = √(2 · g · h)", "g", 64, COR)]))))
        return
    E.frase(c, t, C["s21"], ps("e com isso,", "i", 76), XE, 230, passo=0.12)
    E.frase(c, t, C["s21.a"], [("trilha completa", "g", 100, COR)], XE, 380)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: (
        E.bola(c, 470, 720, 0, a=0),
        M.rrect(c, 270, 690, 400, 24, 8, MADEIRA, a), apoio(c, 470, 714, 60, a), centro(c, "a gangorra", 470, 860, 46, "i", TINTA2, a)))
    if t >= C["s21.b"] + 0.4:
        F.seta(c, 720, 720, 900, 720, E.COR, ep(t, C["s21.b"] + 0.4, 0.5), 10)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: (asa(c, 1120, 720, 170, a), centro(c, "a asa do avião", 1120, 860, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
