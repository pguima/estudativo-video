"""Visual — Estudativo · FIS-EGF-008: flutuar ou afundar.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-008_flutuar_ou_afundar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("disputa", "fracao", "aparente", "atalho", "questao", "fim"))

# todas as contas da aula
assert 30 - 10 == 20 and 0.75 * 2 == 1.5 and 2 - 1.5 == 0.5 and 1.5 * 10 == 15 and 0.75 * 2 * 10 == 15
assert 0.9 / 1 == 0.9 and 0.6 / 1 == 0.6 and 0.2 / 1 == 0.2 and 7 < 7.8 < 8  # gelo, madeira, cortiça; aço quase 8 vezes


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
ACO, GELO = "#7A808C", "#EAF6FF"


def agua(c, x, y, w, h, a=1.0):
    """água aberta: retângulo com a superfície em y"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(AGUA, 0.45 * a))
    M.line(c, x, y, x + w, y, AGUA2, a, 5)


def boiando(c, cx, ys, w, h, frac, cor, a=1.0, rot=None, size=40):
    """bloco que boia com `frac` da altura abaixo da superfície ys; a parte submersa ganha um véu azul"""
    if a <= 0:
        return
    cy = ys + h * frac - h / 2
    F.bloco(c, cx, cy, w, h, rot, cor=cor, a=a, size=size)
    c.save(); c.clipRect(skia.Rect.MakeLTRB(cx - w, ys, cx + w, ys + h * 2))
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint(AGUA2, 0.3 * a))
    c.restore()


def iceberg(c, cx, ys, k, a=1.0):
    """iceberg com 9/10 do volume abaixo da superfície (forma simples, altura total 10k)"""
    if a <= 0:
        return
    p = skia.Path()
    top = ys - 1.0 * k
    p.moveTo(cx - 0.6 * k, ys); p.lineTo(cx - 0.2 * k, top); p.lineTo(cx + 0.5 * k, ys - 0.4 * k); p.lineTo(cx + 0.9 * k, ys)
    p.lineTo(cx + 2.4 * k, ys + 3 * k); p.lineTo(cx + 1.6 * k, ys + 8 * k); p.lineTo(cx - 1.2 * k, ys + 9 * k)
    p.lineTo(cx - 2.6 * k, ys + 4 * k); p.close()
    c.drawPath(p, M.paint(GELO, a))
    c.drawPath(p, M.paint(AGUA2, a, stroke=4))


def balanca_gancho(c, x, y_top, leitura, a=1.0):
    """balança de gancho: caixa com o visor e o gancho embaixo; devolve o ponto do gancho"""
    if a <= 0:
        return x, y_top + 260
    M.line(c, x, y_top - 60, x, y_top, TINTA, a, 5)
    M.rrect(c, x - 90, y_top, 180, 200, 24, "#2A2A30", a)
    M.rrect(c, x - 70, y_top + 30, 140, 70, 10, "#DDEFE3", a)
    centro(c, leitura, x, y_top + 82, 44, "g", TINTA, a)
    M.line(c, x, y_top + 200, x, y_top + 260, TINTA, a, 5)
    return x, y_top + 260


def disputa_setas(c, t, tp, te, cx, cy, kp, ke, rot=True):
    F.forca(c, t, tp, (cx - 26, cy), -90, kp, "P" if rot else None, lado=-1)
    F.forca(c, t, te, (cx + 26, cy), 90, ke, "E" if rot else None, cor=F.NEG, lado=1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            ys = 700
            q = ep(t, C["s01.a"], 0.5)
            agua(c, 820, ys, 1000, 330, q)
            if q > 0:
                p = skia.Path(); p.moveTo(1000, ys - 120); p.lineTo(1500, ys - 120); p.lineTo(1440, ys + 70); p.lineTo(1060, ys + 70); p.close()
                c.drawPath(p, M.paint(ACO, q))
                M.rrect(c, 1180, ys - 220, 160, 100, 10, ACO, q)
            prego_y = lerp(ys - 40, ys + 280, ease_io(prog(t, C["s01.b"] + 0.4, 1.2)))
            E.foco(c, t, C["s01.b"], 0.4, lambda a: (M.line(c, 1680, prego_y - 70, 1680, prego_y + 30, ACO, a, 10), M.line(c, 1660, prego_y - 70, 1700, prego_y - 70, ACO, a, 10)))
            E.foco(c, t, C["s01.a"] + 0.5, 0.4, lambda a: E.pilula(c, "boia", 1250, ys - 280, 46, "g", fundo=CERTO, a=a))
            E.foco(c, t, C["s01.b"] + 1.0, 0.4, lambda a: E.pilula(c, "afunda", 1680, ys - 140, 46, "g", fundo=ERRADO, a=a))
            E.frase(c, t, C["s01.a"], ps("navio de aço:", "i", 64) + [("boia", "g", 64, CERTO)], XE, 230, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("prego de aço:", "i", 64) + [("afunda", "g", 64, ERRADO)], XE, 340, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("o mesmo material", "i", 60, TINTA2), XE, 450, passo=0.1)
            E.frase(c, t, C["s01.d"], ps("não decide o", "i", 64) + [("peso", "g", 64)], XE, 640, passo=0.12)
            E.frase(c, t, C["s01.e"], ps("decide a", "i", 70) + [("densidade", "g", 76, COR)], XE, 780, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "boia ou afunda?"), ("s02.b", "quanto fica dentro"), ("s02.c", "o peso aparente")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o empuxo:", "E = d · V · g, d do líquido"), ("s03.c", "razão:", "uma grandeza ÷ a outra")), 2)


# ---------------- a disputa ----------------
def b_disputa(c, t, C, b):
    if t < C["s05"]:
        def s04():
            ys = 300
            q = ep(t, C["s04.a"], 0.5)
            agua(c, 1050, ys, 700, 720, q)
            E.foco(c, t, C["s04.a"] + 0.2, 0.4, lambda a: F.bloco(c, 1400, 640, 200, 200, None, a=a, cor=TINTA2))
            disputa_setas(c, t, C["s04.b"], C["s04.c"], 1400, 640, 230, 230)
            E.frase(c, t, C["s04.b"], [("peso", "g", 62, COR)] + ps("para baixo,", "i", 62), XE, 230, passo=0.12)
            E.frase(c, t, C["s04.c"], [("empuxo", "g", 62, F.NEG)] + ps("para cima", "i", 62), XE + 470, 230, passo=0.12)
            E.formula_em(c, t, C["s04.d"], "P = d (corpo) · V · g", XE, 450, 72, "g", COR)
            E.formula_em(c, t, C["s04.e"], "E = d (líquido) · V · g", XE, 600, 72, "g", F.NEG)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("V", "g", 64), ("e", "i", 66), ("g", "g", 64)] + ps("iguais: decide a", "i", 66) + [("densidade", "g", 66, COR)], XE, 200, passo=0.1)
            ys = 420
            q = ep(t, C["s05.c"] - 0.3, 0.5)
            agua(c, 160, ys, 1600, 540, q)
            for k_, x, txt, cor, cy_fim in (("s05.c", 400, "mais denso: afunda", ERRADO, 900), ("s05.d", 960, "menos denso: sobe", CERTO, ys - 40),
                                             ("s05.e", 1520, "igual: fica parado", TINTA, 680)):
                y = lerp(680, cy_fim, ease_io(prog(t, C[k_] + 0.3, 1.2)))
                E.foco(c, t, C[k_], 0.4, lambda a, x=x, y=y, cor=cor: F.bloco(c, x, y, 140, 140, None, a=a, cor=cor))
                E.foco(c, t, C[k_] + 0.2, 0.4, lambda a, x=x, txt=txt, cor=cor: centro(c, txt, x, 1040, 46, "b", cor, a))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.frase(c, t, C["s06.a"], ps("e o", "i", 70) + [("navio?", "g", 70, COR)], XE, 200, passo=0.12)
    ys = 640
    q = ep(t, C["s06.a"], 0.5)
    agua(c, 860, ys, 1000, 380, q)
    if q > 0:
        p = skia.Path(); p.moveTo(980, ys - 160); p.lineTo(1560, ys - 160); p.lineTo(1500, ys + 90); p.lineTo(1040, ys + 90); p.close()
        c.drawPath(p, M.paint(ACO, q))
        qq = ep(t, C["s06.b"], 0.5)
        if qq > 0:
            p2 = skia.Path(); p2.moveTo(1010, ys - 140); p2.lineTo(1530, ys - 140); p2.lineTo(1478, ys + 70); p2.lineTo(1062, ys + 70); p2.close()
            c.drawPath(p2, M.paint("#EEF6FB", qq))
            centro(c, "ar", 1270, ys - 20, 56, "i", TINTA2, qq)
    E.frase(c, t, C["s06.b"], ps("é oco:", "i", 62) + [("muito ar", "g", 60)], XE, 320, passo=0.12)
    E.frase(c, t, C["s06.c"], [("densidade média", "g", 58, COR)], XE, 440)
    E.frase(c, t, C["s06.c"] + 0.6, ps("massa de tudo ÷ volume todo", "i", 52, TINTA2), XE, 520, passo=0.08)
    E.frase(c, t, C["s06.d"], [("menor que a da água", "g", 56, CERTO)], XE, 640)
    E.frase(c, t, C["s06.e"], [("prego maciço:", "g", 56)] + ps("quase 8 vezes mais denso", "i", 56, ERRADO), XE, 900, passo=0.1)


# ---------------- fração submersa ----------------
def b_fracao(c, t, C, b):
    if t < C["s08"]:
        def s07():
            ys = 600
            q = ep(t, C["s07.a"], 0.5)
            agua(c, 1050, ys, 700, 420, q)
            frac = lerp(1.0, 0.6, ease_io(prog(t, C["s07.a"] + 0.3, 1.4)))
            E.foco(c, t, C["s07.a"], 0.4, lambda a: boiando(c, 1400, ys, 260, 260, frac, MADEIRA, a))
            disputa_setas(c, t, C["s07.b"], C["s07.b"] + 0.3, 1400, ys + 260 * frac - 130, 150, 150)
            E.frase(c, t, C["s07.a"], ps("quem boia sobe até ficar", "i", 58) + [("só uma parte dentro", "g", 56)], XE, 200, passo=0.1)
            E.frase(c, t, C["s07.b"], [("empuxo = peso", "g", 60, COR)], XE, 310)
            E.frase(c, t, C["s07.c"], ps("resultante zero:", "i", 56) + [("parado", "g", 56)], XE, 400, passo=0.1)
            E.formula_em(c, t, C["s07.d"], "d (corpo) · V = d (líquido) · V (dentro)", XE, 560, 52, "g", TINTA)
            E.frase(c, t, C["s07.e"], [("fração submersa", "g", 60, COR)], XE, 720)
            E.formula_em(c, t, C["s07.f"], "f{V dentro}{V} = f{d corpo}{d líquido}", XE, 900, 76, "g", COR)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    ys, k = 420, 60
    q = ep(t, C["s08"], 0.5)
    agua(c, 900, ys, 920, 620, q)
    iceberg(c, 1350, ys, k, q)
    E.formula_em(c, t, C["s08.a"], "gelo: 0,9    água: 1", XE, 260, 70, "g", TINTA)
    E.formula_em(c, t, C["s08.b"], "f{0,9}{1} =", XE, 470, 96, "g", TINTA)
    bola_txt(c, t, C["s08.c"], "9/10 dentro", 560, 450, 120, 40)
    pilula_em(c, t, C["s08.d"], "1/10 aparece", 1350, ys - 120, 44, TINTA)
    E.frase(c, t, C["s08.e"], ps("a ponta do iceberg é", "i", 56) + [("só a ponta", "g", 56, COR)], XE, 800, passo=0.1)


# ---------------- peso aparente ----------------
def b_aparente(c, t, C, b):
    ys = 640
    q = ep(t, C["s09.c"] - 0.4, 0.5)
    leitura = "30 N" if t < C["s09.d"] else "20 N"
    desce = ease_io(prog(t, C["s09.d"] - 0.8, 0.8))
    gx, gy = 1450, 160
    if q > 0:
        agua(c, 1150, ys, 600, 400, q)
        hx, hy = balanca_gancho(c, gx, gy + desce * 0, leitura, q)
        M.line(c, hx, hy, hx, hy + 60 + 160 * desce, TINTA2, q, 3)
        F.bloco(c, hx, hy + 140 + 160 * desce, 150, 150, None, a=q, cor=TINTA2)
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("e o corpo que", "i", 64) + [("afunda?", "g", 64, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("o empuxo", "i", 60) + [("alivia o peso", "g", 60, F.NEG)], XE, 310, passo=0.12)
        E.frase(c, t, C["s09.c"], ps("balança de gancho:", "i", 58), XE, 470, passo=0.1)
        E.frase(c, t, C["s09.d"], [("marca menos", "g", 58, COR)], XE + 520, 470)
        E.frase(c, t, C["s09.e"], [("peso aparente", "g", 66, COR)], XE, 680)
        E.formula_em(c, t, C["s09.f"], "= P − E", XE + 480, 680, 66, "g", TINTA)
        return
    E.frase(c, t, C["s10.a"], [("pedra:", "g", 60), ("30 N,", "g", 60), ("1 litro", "g", 60, COR)], XE, 220, passo=0.12)
    E.formula_em(c, t, C["s10.b"], "1 L de água  →  E = 10 N", XE, 400, 70, "g", F.NEG)
    E.formula_em(c, t, C["s10.c"], "30 − 10 =", XE, 580, 90, "g", TINTA)
    bola_txt(c, t, C["s10.d"], "20 N", 760, 555, 100, 56)
    E.frase(c, t, C["s10.e"], ps("na piscina, você levanta", "i", 54) + [("um amigo", "g", 54)], XE, 860, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("pesado afunda, leve boia?", "i", 64), XE + 480, 190, passo=0.1)
    if t >= C["s11.b"] + 1.0:
        E.risco(c, XE + 470, 205, XE + 1230, 150, t, C["s11.b"] + 1.0, largura=10)
    ys = 560
    q = ep(t, C["s11.b"], 0.5)
    agua(c, 300, ys, 1320, 440, q)
    if q > 0:
        boiando(c, 650, ys, 520, 110, 0.55, MADEIRA, q, "100 kg", 40)
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: E.pilula(c, "tronco de 100 kg: boia", 650, ys - 120, 42, "g", fundo=CERTO, a=a))
    yy = lerp(ys + 20, ys + 400, ease_io(prog(t, C["s11.c"] + 0.3, 1.2)))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: (c.drawOval(skia.Rect.MakeXYWH(1330, yy - 10, 60, 20), M.paint("#C9A227", a))))
    E.foco(c, t, C["s11.c"] + 0.2, 0.4, lambda a: E.pilula(c, "moeda de 5 g: afunda", 1360, ys - 120, 42, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s11.d"], ps("não importa o peso:", "i", 58) + [("importa a densidade", "g", 58, COR)], W / 2, 1050, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
    E.frase(c, t, C["s12.a"], ps("na água, com", "i", 66, CLARO) + [("g/cm³:", "g", 64, BR)] + ps("a fração sai direto", "i", 66, CLARO), W / 2, 320, "center", 0.1)
    E.formula_em(c, t, C["s12.b"], "madeira 0,6  →", W / 2 - 380, 500, 84, "g", CLARO, "center")
    E.formula_em(c, t, C["s12.c"], "6/10 dentro", W / 2 + 330, 500, 84, "g", BR, "center")
    E.formula_em(c, t, C["s12.d"], "cortiça 0,2  →  2/10 dentro", W / 2, 650, 84, "g", CLARO, "center")
    E.frase(c, t, C["s12.e"], ps("porque a água vale", "i", 62, CLARO) + [("1", "g", 66, BR)], W / 2, 800, "center", 0.12)
    E.frase(c, t, C["s13.a"], [("óleo, mar:", "g", 60, BR)] + ps("a densidade não é 1:", "i", 62, CLARO) + [("divida", "g", 60, BR)], W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], [("bloco de", "i", 64), ("2 L", "g", 64, COR)], XE, 320, passo=0.12)
    E.frase(c, t, C["s14.b"], [("d =", "g", 60), ("0,75 g/cm³", "g", 60, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("boia na água", "i", 60), XE, 520, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("fração", "i", 70) + [("submersa?", "g", 70, COR)], XE, 680, passo=0.12)
    E.frase(c, t, C["s14.e"], ps("litros", "i", 70) + [("fora da água?", "g", 70, COR)], XE, 800, passo=0.12)
    if t < C["s15"]:
        ys = 600
        q = ep(t, C["s14.a"], 0.5)
        agua(c, 1150, ys, 600, 420, q)
        if q > 0:
            boiando(c, 1450, ys, 260, 220, 0.5, MADEIRA, q, "2 L")
        E.foco(c, t, C["s14.c"] + 0.3, 0.4, lambda a: centro(c, "?", 1450, ys - 140, 80, "g", COR, a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ys = 600
    if t < C["s17"]:
        def s16():
            E.formula_em(c, t, C["s16.a"], "f{0,75}{1} =", XE, 300, 96, "g", TINTA)
            bola_txt(c, t, C["s16.b"], "3/4", 600, 270, 95, 70, CERTO)
            E.formula_em(c, t, C["s16.c"], "f{3}{4} · 2 L = 1,5 L dentro", XE, 560, 80, "g", TINTA)
            E.formula_em(c, t, C["s16.d"], "fora: 2 − 1,5 = 0,5 L", XE, 760, 80, "g", CERTO)
            q = ep(t, C["s16.a"], 0.5)
            agua(c, 1150, ys, 600, 420, q)
            fr = lerp(0.5, 0.75, ease_io(prog(t, C["s16.b"], 1.0)))
            if q > 0:
                boiando(c, 1450, ys, 260, 220, fr, MADEIRA, q, "2 L")
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    q = ep(t, C["s17"], 0.5)
    agua(c, 1150, ys, 600, 420, q)
    if q > 0:
        boiando(c, 1450, ys, 260, 220, 0.75, MADEIRA, q, "2 L")
    disputa_setas(c, t, C["s17.c"], C["s17.a"], 1450, ys + 220 * 0.75 - 110, 170, 170)
    E.formula_em(c, t, C["s17.a"], "E: 1,5 L × 10 N = 15 N", XE, 300, 76, "g", F.NEG)
    E.formula_em(c, t, C["s17.b"], "massa: 0,75 kg/L × 2 L = 1,5 kg", XE, 480, 64, "g", TINTA2)
    E.formula_em(c, t, C["s17.c"], "P = 15 N", XE, 640, 76, "g", COR)
    pilula_em(c, t, C["s17.d"], "empatou: boia parado", 560, 820, 50, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s19"]:
        E.saida(c, t, C["s19"] - 0.1, lambda: resumo(c, t, C, "s18", (
            ("s18.a", [("mais denso", "g", 64), ("afunda,", "i", 68), ("menos denso", "g", 64), ("boia", "i", 68)]),
            ("s18.b", [("fração submersa", "g", 64, COR), ("=", "g", 64, TINTA2), ("razão das densidades", "i", 66)]),
            ("s18.c", [("peso aparente", "g", 64, COR), ("=", "g", 64, TINTA2), ("P − E", "g", 64)]))))
        return

    def desenho():
        q = ep(t, C["s19.b"], 0.6)
        if q <= 0:
            return
        for i, (rot, cor) in enumerate((("p = F/A", E.COR), ("prensa", TINTA), ("empuxo", F.NEG))):
            E.foco(c, t, C["s19.b"] + 0.3 * i, 0.4, lambda a, i=i, rot=rot, cor=cor: E.pilula(c, rot, 380 + i * 330, 800, 50, "g", fundo=cor, a=a))
    proxima(c, t, C, "s19", [("Praticando:", "g", 110, COR)], [("hidrostática", "i", 100)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, disputa=b_disputa, fracao=b_fracao, aparente=b_aparente, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
