"""Visual — Estudativo · FIS-ELE-001: carga elétrica e eletrização. Primeira aula da trilha Eletricidade.

Segue a LINGUAGEM VISUAL DA FÍSICA (docstring do visual.py da FIS-CIN-001: grandeza em itálico + letra pesada laranja,
medida = número + unidade cinza, fórmula nova com F.formula_legenda, atalho no palco, texto à esquerda e desenho à direita).

LINGUAGEM VISUAL DA ELETRICIDADE (todas as aulas FIS-ELE-* copiam daqui; peças em _ferramentas/fisica.py, importado como F,
e as peças locais abaixo, que cada visual.py copia quando precisar):
- CARGA: + é laranja (E.COR), − é azul (F.NEG), sempre com o sinal desenhado em branco. Carga grande e sozinha = F.carga;
  carga pequena dentro de um corpo = `q()` (bolinha chapada com sinal). Elétron = `q(..., "−")`; próton = `q(..., "+")`.
  Corpo NEUTRO mostra pares + e − lado a lado; corpo carregado mostra só o EXCESSO (bolinhas de um sinal).
  Só os elétrons (azuis) se mexem na tela: os + ficam parados no lugar. É a regra da aula 001 e vale para toda a trilha.
- METAL (condutor): esfera cinza com volume (`esfera_metal`, E.bola em METAL). ISOLANTE: plástico escuro (pente, bastão) ou
  papel claro. TERRA: o símbolo de três traços (`terra`), ligado por F.fio.
- ATRAÇÃO E REPULSÃO: setas laranja (F.seta, cor COR) saindo das cargas: para fora = repelem, para dentro = atraem.
  FORÇA ELÉTRICA (a partir da FIS-ELE-002) é vetor laranja como toda força (F.vetor / F.forca).
- CAMPO ELÉTRICO (FIS-ELE-003 em diante): linhas de força em cinza-tinta (TINTA2) com setas (F.campo_carga); o vetor E
  em tinta (TINTA), para não se confundir com a força (laranja). Campo uniforme = linhas paralelas igualmente espaçadas.
- POTENCIAL (escalar): número com sinal numa pílula, nunca seta; superfícies equipotenciais tracejadas (E.TRACO).
- CIRCUITO (FIS-ELE-008 em diante): F.fio em tinta, F.pilha, F.resistor, F.lampada, F.chave. Corrente convencional =
  setinhas laranja (F.corrente) do + para o − por fora da pilha; elétrons = bolinhas azuis andando ao contrário.
- UNIDADES da trilha em cinza-tinta (F.UNID), escritas como no SI: C, µC, N, N/C, V, J, A, mAh, Ω, F (farad).
  Potência de dez sempre com E.formula ("1,6 × 10^{−19}"), nunca com algarismo sobrescrito solto. Símbolo grego (µ, Ω, Δ)
  e os sinais = e → só na fonte pesada ("g"/"b"): a itálica não tem esses caracteres.
- Os três jeitos de eletrizar ficam numa barra de pílulas no alto (`jeitos`), com o da vez em laranja.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-001_carga_eletrica_eletrizacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("carga", "quantidade", "atrito", "inducao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"
PLAST = "#2E2E36"

# todas as contas da aula
assert abs(5 * 1.6 - 8) < 1e-12 and 12 + (-19) == -7 and abs(5e12 * 1.6e-19 - 8e-7) < 1e-20
assert 8 + (-2) == 6 and 6 / 2 == 3 and 3 + 3 == 6
assert abs(3.2 / 1.6 - 2) < 1e-12 and -6 - (-19) == 13 and abs(3.2e-6 / 1.6e-19 - 2e13) / 2e13 < 1e-9
assert abs((-3.2 + 0) / 2 - (-1.6)) < 1e-12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copie para as outras aulas) ----------------
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


def terra(c, x, y, a=1.0, cor=TINTA):
    """símbolo de terra: três traços, o de cima em y"""
    for i, w in enumerate((90, 60, 30)):
        M.line(c, x - w / 2, y + i * 18, x + w / 2, y + i * 18, cor, a, 6)


def pente(c, x, y, w, h, a=1.0, cor=PLAST):
    """pente de plástico: costas em cima (x, y), dentes para baixo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h * 0.34, 10, cor, a)
    n = max(6, int(w / 26))
    for i in range(n):
        tx = x + 12 + i * (w - 32) / (n - 1)
        M.rrect(c, tx, y + h * 0.28, 9, h * 0.72, 4, cor, a)


def cabeca(c, cx, cy, r, a=1.0):
    """cabeça de perfil simples, com cabelo em cima"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#E7B58C", a))
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - r * 1.06, cy - r * 1.12, r * 2.12, r * 1.9), 180, 180)
    p.close()
    c.drawPath(p, M.paint("#3B2A20", a))
    for dx in (-0.55, -0.15, 0.25, 0.6):
        M.line(c, cx + dx * r, cy - r * 0.95, cx + dx * r + r * 0.18, cy - r * 0.25, "#5A4232", a, 4)
    for dx in (-0.35, 0.35):
        c.drawCircle(cx + dx * r, cy + r * 0.25, r * 0.07, M.paint(TINTA, a))
    M.line(c, cx - r * 0.25, cy + r * 0.6, cx + r * 0.25, cy + r * 0.6, "#9C5B3E", a, 5)


def papel(c, x, y, w, h, giro=0.0, a=1.0):
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(giro)
    M.rrect(c, -w / 2, -h / 2, w, h, 3, "#FFFFFF", a)
    c.drawRect(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), M.paint(TINTA2, a, stroke=2))
    c.restore()


def jeitos(c, t, t0, k):
    """barra com os três jeitos de eletrizar; o da vez em laranja"""
    for i, s in enumerate(("atrito", "contato", "indução")):
        x = 640 + 320 * i
        E.foco(c, t, t0 + 0.12 * i, 0.4, lambda a, i=i, s=s, x=x: E.pilula(
            c, s, x, 110, 40, "g", fundo=E.COR if i == k else FIO, cor=BR if i == k else TINTA2, a=a))


def bastao(c, x0, x1, y, h, a=1.0):
    """bastão de plástico negativo, de x0 a x1"""
    if a <= 0:
        return
    M.rrect(c, x0, y - h / 2, x1 - x0, h, h / 2, PLAST, a)
    for i in range(4):
        q(c, x1 - 50 - i * 80, y, 20, "−", a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        hx, hy, hr = 1560, 680, 170
        E.foco(c, t, C["s01.a"], 0.5, lambda a: cabeca(c, hx, hy, hr, a))
        # o pente esfrega o cabelo e vai até os papéis
        if t < C["s01.b"]:
            px = 1395 + 60 * math.sin(max(0, t - C["s01.a"]) * 9)
            py = hy - hr * 1.12 - 70
        else:
            k = ease_io(prog(t, C["s01.b"], 0.9))
            px, py = lerp(1395, 1010, k), lerp(hy - hr * 1.12 - 70, 560, k)
        E.foco(c, t, C["s01.a"] + 0.2, 0.4, lambda a: pente(c, px, py, 330, 100, a))
        # papéis na mesa; pulam no s01.c
        if t >= C["s01.b"] - 0.2:
            F.chao(c, 960, 1420, 900, ep(t, C["s01.b"] - 0.2, 0.4))
        for i, (dx, g) in enumerate(((0, 12), (90, -18), (170, 25), (250, -8))):
            u = ease_back(prog(t, C["s01.c"] + 0.08 * i, 0.5))
            x, y = 1040 + dx, lerp(880, 680 + 10 * (i % 2), min(1, u))
            E.foco(c, t, C["s01.b"] + 0.1 * i, 0.3, lambda a, x=x, y=y, g=g, u=u: papel(c, x, y, 54, 34, g * (1 - min(1, u)), a))
        # os elétrons no pente
        for i in range(5):
            E.foco(c, t, C["s01.d"] + 0.1 * i, 0.3, lambda a, i=i: q(c, px + 45 + i * 60, py + 17, 15, "−", a), blur=0)
        E.frase(c, t, C["s01.a"], [("pente", "g", 90), ("no", "i", 92), ("cabelo", "i", 92)], XE, 300)
        E.frase(c, t, C["s01.b"], [("perto", "i", 92), ("do", "i", 92), ("papel", "g", 90)], XE, 440)
        E.frase(c, t, C["s01.c"], [("o", "i", 104), ("papel", "i", 104), ("pula!", "g", 104, COR)], XE, 600)
        E.frase(c, t, C["s01.c"] + 1.2, ps("sem cola, sem ímã", "i", 64, TINTA2), XE, 720, passo=0.12)
        E.frase(c, t, C["s01.d"], [("elétrons", "g", 130, COR)], XE, 890)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.a", "a carga de um corpo", 1.4, 74), ("s02.b", "contando elétrons", 0, 74), ("s02.c", "atrito · contato · indução", 0, 62))
    for i, (k, s, dt, sz) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", sz, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    itens = (("s03.b", "o átomo:", "prótons e elétrons"), ("s03.c", "potências de 10:", "some ou subtraia"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 170)
    E.foco(c, t, C["s03.b"] + 0.6, 0.5, lambda a: E.orbita(c, 1670, 345, 105, a=a, giro=8 * math.sin(t * 0.6)))
    E.foco(c, t, C["s03.c"] + 0.8, 0.5, lambda a: (E.formula(c, "10^2 · 10^3 = 10^5", 1630, 610, 44, "g", TINTA, a, "center"),
                                                  E.formula(c, "10^5 ÷ 10^3 = 10^2", 1630, 700, 44, "g", TINTA2, a, "center")))
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.7), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


# ---------------- carga elétrica ----------------
def corpo(c, x, y, w, h, a=1.0):
    """corpo genérico (bloco claro) onde ficam as cargas"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 28, "#E4E4E0", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 28, 28), M.paint(TINTA2, a, stroke=3))


def b_carga(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("carga", "i", 100), ("elétrica", "g", 100, COR)], XE, 230)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: q(c, XE + 34, 384, 30, "+", a))
        E.frase(c, t, C["s04.b"], [("próton:", "g", 68), ("positiva", "i", 72, TINTA2)], XE + 90, 408)
        E.foco(c, t, C["s04.c"], 0.4, lambda a: q(c, XE + 34, 504, 30, "−", a))
        E.frase(c, t, C["s04.c"], [("elétron:", "g", 68), ("negativa", "i", 72, TINTA2)], XE + 90, 528)
        E.frase(c, t, C["s04.d"], [("mesmo", "i", 72), ("tamanho", "g", 68, COR)], XE, 660)
        E.frase(c, t, C["s04.e"], [("4", "g", 84, COR), ("prótons,", "i", 72), ("4", "g", 84, NEG), ("elétrons", "i", 72)], XE, 820, passo=0.15)
        E.frase(c, t, C["s04.f"], [("=", "g", 84, TINTA2), ("neutro", "g", 96)], XE, 950)
        # o átomo: núcleo com 4 prótons e 4 elétrons girando
        ax, ay, R = 1420, 560, 270
        pe = ep(t, C["s04.a"] + 0.4, 0.6)
        if pe > 0:
            pt = M.paint(TINTA2, 0.5 * pe, stroke=3)
            pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
            c.drawCircle(ax, ay, R, pt)
            for i, (dx, dy) in enumerate(((-26, -24), (26, -24), (-26, 26), (26, 26))):
                c.drawCircle(ax + dx * 0.6, ay - dy * 0.6, 34, M.paint(CINZA, pe))
            for i, (dx, dy) in enumerate(((-30, -28), (30, 24), (28, -30), (-28, 28))):
                q(c, ax + dx, ay + dy, 30, "+", ep(t, C["s04.b"] + 0.2 + 0.1 * i, 0.4))
            for i in range(4):
                g = math.radians(45 + 90 * i) + max(0, t - C["s04.a"]) * 0.35
                q(c, ax + R * math.cos(g), ay + R * math.sin(g), 30, "−", ep(t, C["s04.c"] + 0.2 + 0.1 * i, 0.4))
        E.foco(c, t, C["s04.f"] + 0.3, 0.4, lambda a: E.pilula(c, "neutro: as cargas se cancelam", ax, ay + R + 90, 40, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("quem se mexe:", "i", 80) + [("os", "g", 80, NEG), ("elétrons", "g", 80, NEG)], W / 2, 200, "center", 0.12)
            E.frase(c, t, C["s05.a"] + 1.3, ps("os prótons ficam no núcleo", "i", 54, TINTA2), W / 2, 290, "center", 0.1)
            for j, (x0, k_in, k_lbl, cor, sinal, txt) in enumerate(((240, "s05.b", "s05.c", E.COR, "POSITIVO", "perdeu elétrons"),
                                                                    (1040, "s05.d", "s05.e", NEG, "NEGATIVO", "ganhou elétrons"))):
                y0, w, h = 380, 640, 330
                ta = C["s05.a"] + 0.3 if j == 0 else C["s05.d"] - 0.4
                E.foco(c, t, ta, 0.5, lambda a, x0=x0: corpo(c, x0, y0, w, h, a))
                al = ep(t, ta + 0.2, 0.4)
                for i in range(6):
                    cx, cy = x0 + 110 + (i % 3) * 210, y0 + 100 + (i // 3) * 130
                    q(c, cx, cy, 26, "+", al)
                    if j == 0 and i in (1, 5):   # estes dois saem
                        u = ease_io(prog(t, C[k_in] + 0.15 * (i == 5), 0.9))
                        q(c, lerp(cx + 58, cx + 58 + 160, u), lerp(cy, cy - 260, u), 26, "−", al * (1 - u))
                    else:
                        q(c, cx + 58, cy, 26, "−", al)
                if j == 1:  # dois elétrons chegam de fora
                    for i, (ex, ey) in enumerate(((x0 + 215, y0 + 165), (x0 + 425, y0 + 165))):
                        u = ease_io(prog(t, C[k_in] + 0.15 * i, 0.9))
                        if u > 0:
                            q(c, lerp(ex + 120, ex, u), lerp(ey + 240, ey, u), 26, "−", min(1, u * 2))
                E.foco(c, t, C[k_in] + 0.6, 0.4, lambda a, x0=x0, txt=txt: centro(c, txt, x0 + w / 2, y0 + h + 90, 54, "i", TINTA, a))
                E.foco(c, t, C[k_lbl], 0.5, lambda a, x0=x0, cor=cor, sinal=sinal: E.pilula(c, sinal, x0 + w / 2, y0 + h + 200, 64, "g", fundo=cor, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("carregados se empurram ou se puxam", "i", 70), W / 2, 200, "center", 0.1)
    for k, sinais, y, l1, l2 in (("s06.a", ("+", "+"), 450, "mesmo sinal", "se repelem"), ("s06.b", ("+", "−"), 800, "sinais opostos", "se atraem")):
        repele = sinais[0] == sinais[1]
        u = ease_io(prog(t, C[k] + 0.6, 0.8))
        if repele:
            x1, x2 = 1180 - 90 * u, 1500 + 90 * u
        else:
            x1, x2 = 1060 + 60 * u, 1620 - 60 * u
        E.foco(c, t, C[k], 0.5, lambda a, x1=x1, x2=x2, sinais=sinais, y=y: (q(c, x1, y, 56, sinais[0], a), q(c, x2, y, 56, sinais[1], a)))
        a_, p_ = ep(t, C[k] + 0.6, 0.3), ease_out(prog(t, C[k] + 0.6, 0.5))
        if t >= C[k] + 0.6:
            for xc, d in ((x1, -1), (x2, 1)):
                s_ = d if repele else -d
                F.seta(c, xc + s_ * 72, y, xc + s_ * 72 + s_ * (130 if repele else 100), y, E.COR, a_, 9, None, p_)
        E.frase(c, t, C[k], [(l1, "i", 76)], XE, y - 20)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 80, COR)], XE, y + 80)


# ---------------- Q = n · e ----------------
def b_quantidade(c, t, C, b):
    def s07():
        E.foco(c, t, C["s07.a"], 0.5, lambda a: E.escreve(c, "C", XE, 420, 280, "g", COR, a))
        E.frase(c, t, C["s07.a"] + 0.3, [("coulomb", "g", 96)], XE + 240, 330)
        E.frase(c, t, C["s07.a"] + 0.8, ps("a unidade de carga", "i", 64, TINTA2), XE + 240, 420, passo=0.1)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: q(c, XE + 40, 630, 40, "−", a))
        E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: (E.formula(c, "e = 1,6 × 10^{−19}", XE + 120, 670, 110, "g", TINTA, a),
                                                      E.formula(c, "C", XE + 140 + E.formula(None, "e = 1,6 × 10^{−19}", 0, 0, 110, a=0), 670, 80, "b", F.UNID, a)))
        E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: E.escreve(c, "um elétron", XE + 120, 560, 50, "i", TINTA2, a))
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.pilula(c, "carga elementar", XE + 330, 850, 60, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s07.c"] + 1.0, ps("a menor carga solta na natureza", "i", 54, TINTA2), XE + 700, 870, passo=0.1)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s09"]:
        E.saida(c, t, C["s09"] - 0.1, lambda: F.formula_legenda(
            c, t, C["s08.a"], "Q = n · e", [("Q", "carga", "C"), ("n", "elétrons ganhos ou perdidos", None), ("e", "carga elementar", "1,6 × 10^{−19} C")],
            560, 380, 180, tl=[C["s08.b"], C["s08.c"], C["s08.d"]], size_l=58))
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], [("perdeu", "g", 80, COR)], XE, 220)
    E.foco(c, t, C["s09.a"] + 0.3, 0.5, lambda a: (E.formula(c, "5 × 10^{12}", XE + 330, 220, 80, "g", TINTA, a),
                                                  E.escreve(c, "elétrons", XE + 380 + E.formula(None, "5 × 10^{12}", 0, 0, 80, a=0), 220, 76, "i", TINTA, a)))
    E.formula_em(c, t, C["s09.a"] + 1.2, "Q = 5 × 10^{12} · 1,6 × 10^{−19}", W / 2, 420, 96, "g", TINTA, "center")
    E.formula_em(c, t, C["s09.b"], "5 · 1,6 = 8", W / 2 - 420, 610, 84, "g", COR, "center")
    E.formula_em(c, t, C["s09.c"], "10^{12} · 10^{−19} = 10^{−7}", W / 2 + 330, 610, 84, "g", COR, "center")
    E.foco(c, t, C["s09.c"] + 0.8, 0.4, lambda a: centro(c, "12 + (−19) = −7", W / 2 + 330, 700, 50, "b", TINTA2, a))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: pilula_f(c, "Q = 8 × 10^{−7} C", W / 2, 840, 84, a=a))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: (q(c, W / 2 - 280, 990, 30, "+", a), E.escreve(c, "positiva: perdeu elétrons", W / 2 - 230, 1008, 52, "i", TINTA, a)))


# ---------------- atrito ----------------
def b_atrito(c, t, C, b):
    jeitos(c, t, C["s10"], 0)
    hx, hy, hr = 1520, 690, 170
    E.foco(c, t, C["s10.a"], 0.5, lambda a: cabeca(c, hx, hy, hr, a))
    py = hy - hr * 1.12 - 72
    px = 1355 + (60 * math.sin((t - C["s10.a"]) * 9) * (1 - ep(t, C["s10.b"], 0.4)) if t >= C["s10.a"] else 0)
    E.foco(c, t, C["s10.a"] + 0.2, 0.4, lambda a: pente(c, px, py, 330, 100, a))
    # três elétrons passam do cabelo para o pente; no cabelo ficam três +
    for i in range(3):
        sx, sy = hx - 90 + i * 90, hy - hr * 0.6
        u = ease_io(prog(t, C["s10.b"] + 0.25 * i, 0.9))
        if t >= C["s10.b"] - 0.3:
            q(c, lerp(sx, px + 70 + i * 95, u), lerp(sy, py + 17, u) - 70 * math.sin(u * math.pi), 17, "−", ep(t, C["s10.b"] - 0.3, 0.3))
            q(c, sx, sy, 17, "+", ep(t, C["s10.b"] + 0.25 * i + 0.6, 0.3))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "pente −", px + 165, py - 60, 44, "g", fundo=NEG, a=a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "cabelo +", hx, hy + hr + 70, 44, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s10.a"], [("atrito", "g", 120, COR)], XE, 330)
    E.frase(c, t, C["s10.a"] + 0.6, ps("esfregar um no outro", "i", 64, TINTA2), XE, 430, passo=0.1)
    E.frase(c, t, C["s10.b"], [("elétrons:", "g", 60, NEG), ("cabelo", "i", 66), ("→", "g", 60, TINTA2), ("pente", "i", 66)], XE, 570, passo=0.15)
    E.frase(c, t, C["s10.c"], [("pente", "i", 76), ("negativo", "g", 72, NEG)], XE, 700)
    E.frase(c, t, C["s10.d"], [("cabelo", "i", 76), ("positivo", "g", 72, COR)], XE, 810)
    E.frase(c, t, C["s10.e"], [("sinais", "i", 64), ("opostos,", "g", 60), ("mesmo", "i", 64), ("tamanho", "g", 60)], XE, 950, passo=0.12)


# ---------------- condutor, isolante e contato ----------------
def b_contato(c, t, C, b):
    def s11():
        E.frase(c, t, C["s11"], ps("uma ideia antes", "i", 70, TINTA2), W / 2, 190, "center", 0.12)
        for i, (x, k1, k2, nome, mat) in enumerate(((170, "s11.a", "s11.b", "CONDUTORES", "metais"),
                                                    (1010, "s11.c", "s11.d", "ISOLANTES", "plástico, vidro, borracha"))):
            p = ep(t, C[k1], 0.5)
            E.caixa_pontilhada(c, x, 270, 740, 560, p, prog_=p)
            E.frase(c, t, C[k1], [(mat, "i", 62)], x + 50, 370)
            # barra do material com elétrons
            bx, by, bw = x + 60, 520, 620
            al = ep(t, C[k1] + 0.3, 0.4)
            M.rrect(c, bx, by, bw, 90, 45, METAL if i == 0 else PLAST, al)
            for j in range(5):
                if i == 0:
                    ex = bx + 40 + ((j * (bw - 80) / 5 + (t - C[k1]) * 160) % (bw - 80))
                else:
                    ex = bx + 70 + j * 120 + 8 * math.sin(t * 6 + j)
                q(c, ex, by + 45, 22, "−", al)
            E.foco(c, t, C[k1] + 0.6, 0.4, lambda a, x=x, i=i: centro(c, "elétrons andam" if i == 0 else "elétrons quase parados", x + 370, 700, 50, "i", TINTA2, a))
            E.foco(c, t, C[k2], 0.5, lambda a, x=x, nome=nome, i=i: E.pilula(c, nome, x + 370, 780, 58, "g", fundo=E.COR if i == 0 else TINTA, a=a))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if C["s12"] <= t < C["s13"]:
        def s12():
            jeitos(c, t, C["s12"], 1)
            E.frase(c, t, C["s12.a"], [("contato", "g", 110, COR)], XE, 300)
            R, y = 140, 600
            u = ease_io(prog(t, C["s12.b"] + 0.8, 0.8)) * (1 - ease_io(prog(t, C["s12.d"] + 0.3, 0.8)))
            xa, xb = lerp(640, 820, u), lerp(1300, 1100, u)
            E.foco(c, t, C["s12.a"] + 0.3, 0.5, lambda a: esfera_metal(c, xa, y, R, a))
            E.foco(c, t, C["s12.b"], 0.5, lambda a: esfera_metal(c, xb, y, R, a))
            al = ep(t, C["s12.a"] + 0.5, 0.4)
            pa = [(-60, -50), (20, -70), (70, -5), (-75, 25), (0, 30), (40, 75)]
            for dx, dy in pa:
                q(c, xa + dx, y + dy, 24, "+", al)
            # B neutra: três pares; no contato, os três − de B vão para A
            ab = ep(t, C["s12.b"] + 0.2, 0.4)
            pb = [(-55, -40), (35, -45), (0, 55)]
            for i, (dx, dy) in enumerate(pb):
                q(c, xb + dx, y + dy, 24, "+", ab)
                v = ease_io(prog(t, C["s12.c"] + 0.15 * i, 0.8))
                alvo = pa[(0, 2, 4)[i]]
                ex, ey = lerp(xb + dx + 46, xa + alvo[0] + 44, v), lerp(y + dy, y + alvo[1] + 6, v)
                q(c, ex, ey, 24, "−", ab)
            E.foco(c, t, C["s12.a"] + 0.6, 0.4, lambda a: centro(c, "carregada", 640, y + R + 80, 50, "i", TINTA2, a) if t < C["s12.c"] else None)
            E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: centro(c, "neutra", 1300, y + R + 80, 50, "i", TINTA2, a) if t < C["s12.c"] else None)
            E.foco(c, t, C["s12.c"] + 0.2, 0.4, lambda a: E.pilula(c, "elétrons passam", W / 2 + 10, 380, 44, "b", fundo=TINTA, a=a) if t < C["s12.d"] else None)
            E.foco(c, t, C["s12.d"] + 0.4, 0.4, lambda a: (E.pilula(c, "+", 640, y - R - 60, 50, "g", fundo=E.COR, a=a),
                                                          E.pilula(c, "+", 1300, y - R - 60, 50, "g", fundo=E.COR, a=a)))
            troca(c, t, [(C["s12.d"], [("as", "i", 70), ("duas:", "i", 70), ("mesmo", "g", 66), ("sinal", "g", 66, COR)]),
                         (C["s12.e"], [("esferas", "i", 70), ("iguais:", "g", 66), ("metade", "g", 66, COR), ("para", "i", 70), ("cada", "i", 70)])],
                  lambda s, a: _linha(c, s, W / 2, 940, a))
        E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    jeitos(c, t, C["s13"] - 1, 1)
    R, y = 115, 400
    u = ease_io(prog(t, C["s13.d"] - 1.4, 0.7)) * (1 - ease_io(prog(t, C["s13.f"] - 0.2, 0.7)))
    xa, xb = lerp(620, 845, u), lerp(1300, 1075, u)
    E.foco(c, t, C["s13"], 0.5, lambda a: esfera_metal(c, xa, y, R, a))
    E.foco(c, t, C["s13.c"] - 0.3, 0.5, lambda a: esfera_metal(c, xb, y, R, a))
    E.foco(c, t, C["s13"] + 0.2, 0.4, lambda a: centro(c, "1", xa, y + 22, 64, "g", BR, a))
    E.foco(c, t, C["s13.c"] - 0.1, 0.4, lambda a: centro(c, "2", xb, y + 22, 64, "g", BR, a))
    troca(c, t, [(C["s13.a"], ("+8", "µC")), (C["s13.f"], ("+3", "µC"))], lambda s, a: F.medida(c, s[0], s[1], 620, y + R + 100, 80, E.COR, a, "center"))
    troca(c, t, [(C["s13.c"], ("−2", "µC")), (C["s13.f"], ("+3", "µC"))], lambda s, a: F.medida(c, s[0], s[1], 1300, y + R + 100, 80, NEG if s[0][0] == "−" else E.COR, a, "center"))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: pilula_f(c, "1 µC = 10^{−6} C", 1640, 240, 48, fundo=TINTA, a=a))
    E.formula_em(c, t, C["s13.d"], "(+8) + (−2) = +6", W / 2 - 330, 800, 86, "g", TINTA, "center")
    E.formula_em(c, t, C["s13.e"], "6 ÷ 2 = 3", W / 2 + 430, 800, 86, "g", COR, "center")
    E.frase(c, t, C["s13.g"], [("soma:", "i", 64), ("6", "g", 66, COR), ("antes,", "i", 64), ("3 + 3 = 6", "g", 62, COR), ("depois", "i", 64)], W / 2, 960, "center", 0.12)
    E.foco(c, t, C["s13.g"] + 2.2, 0.4, lambda a: E.pilula(c, "a carga se conserva", 1660, 950, 42, "b", fundo=CERTO, a=a))


def _linha(c, partes, x, y, a, align="center"):
    """linha de tipografia mista parada (para a troca)"""
    w, xs = E._arranjo(partes, x, align)
    for p, xx in zip(partes, xs):
        E.escreve(c, p[0], xx, y, p[2], p[1], p[3] if len(p) > 3 else TINTA, a)


# ---------------- indução ----------------
def b_inducao(c, t, C, b):
    sx, sy, R = 1180, 560, 170
    pos = [(-95, -70), (-10, -110), (80, -60), (-60, 40), (40, 30), (-10, 115)]

    def s14_15():
        jeitos(c, t, C["s14"], 2)
        E.frase(c, t, C["s14.a"], [("indução", "g", 110, COR)], XE, 300)
        E.frase(c, t, C["s14.a"] + 0.6, ps("sem encostar", "i", 70, TINTA2), XE, 400, passo=0.12)
        # bastão chega pela esquerda e vai embora no s15.d
        u_in = ease_io(prog(t, C["s14.b"], 0.9))
        u_out = ease_io(prog(t, C["s15.d"], 0.9))
        xt = lerp(-80, sx - R - 60, u_in) - 1400 * u_out
        bastao(c, xt - 520, xt, sy, 74, ep(t, C["s14.b"], 0.3))
        E.foco(c, t, C["s14.a"] + 0.4, 0.5, lambda a: esfera_metal(c, sx, sy, R, a))
        al = ep(t, C["s14.a"] + 0.6, 0.4)
        sep = ease_io(prog(t, C["s14.c"], 1.0))
        terra_on = t >= C["s15"]
        # fio para a terra; no s15.c, o fio é cortado
        if terra_on:
            cortado = t >= C["s15.c"]
            F.fio(c, t, C["s15.a"], [(sx + R * 0.7, sy + R * 0.7), (1560, sy + R * 0.7 + 90), (1560, 800)])
            if not cortado:
                F.fio(c, t, C["s15.a"] + 0.6, [(1560, 800), (1560, 930)], d=0.3)
            else:
                M.line(c, 1560, 870, 1560, 930, TINTA, 1.0, 6)
                E.foco(c, t, C["s15.c"], 0.3, lambda a: (M.line(c, 1530, 810, 1590, 860, ERRADO, a, 7), M.line(c, 1530, 860, 1590, 810, ERRADO, a, 7)))
            E.foco(c, t, C["s15.a"] + 0.6, 0.4, lambda a: (terra(c, 1560, 940, a), E.escreve(c, "terra", 1630, 975, 50, "i", TINTA2, a)))
        for i, (dx, dy) in enumerate(pos):
            q(c, sx + dx, sy + dy, 24, "+", al)
            # elétrons: perto do +, depois no lado de longe; três descem pela terra no s15.b; os outros voltam quando o bastão sai
            far = (sx + 110 + 30 * ((i % 2) - 0.5), sy - 100 + i * 40)
            ex, ey = lerp(sx + dx + 46, far[0], sep), lerp(sy + dy, far[1], sep)
            volta = ease_io(prog(t, C["s15.d"] + 0.5, 0.8)) if terra_on else 0
            if i < 3 and terra_on:
                v = ease_io(prog(t, C["s15.b"] + 0.25 * i, 1.2))
                pts = [(ex, ey), (sx + R * 0.7, sy + R * 0.7), (1560, sy + R * 0.7 + 90), (1560, 930)]
                if v > 0:
                    ex, ey = _ao_longo(pts, v)
                q(c, ex, ey, 24, "−", al * (1 - ep(t, C["s15.b"] + 0.25 * i + 1.1, 0.2)))
            else:
                ex, ey = lerp(ex, sx + dx + 46, volta), lerp(ey, sy + dy, volta)
                q(c, ex, ey, 24, "−", al)
        if not terra_on:
            E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: E.pilula(c, "perto: +", sx - R + 10, sy - R - 40, 40, "g", fundo=E.COR, a=a))
            E.foco(c, t, C["s14.c"] + 0.5, 0.4, lambda a: E.pilula(c, "longe: −", sx + R - 10, sy + R + 40, 40, "g", fundo=NEG, a=a))
        troca(c, t, [(C["s14.c"], [("elétrons", "g", 64, NEG), ("fogem", "i", 70), ("para", "i", 70), ("longe", "i", 70)]),
                     (C["s14.e"], [("continua", "i", 70), ("neutra:", "g", 66), ("só", "i", 70), ("separou", "g", 66, COR)]),
                     (C["s15.a"], [("ligue", "i", 70), ("à", "i", 70), ("terra", "g", 66, COR)]),
                     (C["s15.b"], [("elétrons", "g", 64, NEG), ("descem", "i", 70), ("pelo", "i", 70), ("fio", "i", 70)]),
                     (C["s15.c"], [("corte", "i", 70), ("o", "i", 70), ("fio", "g", 66, ERRADO)]),
                     (C["s15.d"], [("afaste", "i", 70), ("o", "i", 70), ("bastão", "g", 66)])],
              lambda s, a: _linha(c, s, XE, 960, a, "left"))
        E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "POSITIVA", sx, sy - R - 70, 60, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s15.f"], 0.5, lambda a: E.pilula(c, "sinal oposto ao do bastão", sx, sy + R + 90, 42, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s16"] - 0.1, s14_15)
    if t < C["s16"]:
        return
    # o papel do começo
    E.frase(c, t, C["s16"], ps("o papel do começo", "i", 80, TINTA2), XE, 250, passo=0.12)
    E.frase(c, t, C["s16.a"], [("pente", "i", 76), ("negativo", "g", 72, NEG)], XE, 430)
    E.frase(c, t, C["s16.b"], [("perto", "i", 76), ("fica", "i", 76), ("+", "g", 90, COR)], XE, 580)
    E.frase(c, t, C["s16.c"], [("papel", "i", 76), ("puxado", "g", 72, COR)], XE, 730)
    px, py = 1060, 330
    E.foco(c, t, C["s16"] + 0.3, 0.5, lambda a: pente(c, px, py, 420, 120, a))
    for i in range(5):
        E.foco(c, t, C["s16.a"] + 0.08 * i, 0.3, lambda a, i=i: q(c, px + 60 + i * 76, py + 20, 17, "−", a), blur=0)
    E.foco(c, t, C["s16.b"] - 1.2, 0.4, lambda a: E.pilula(c, "isolante: deslocam um pouquinho", px + 210, 960, 38, "b", fundo=TINTA2, a=a))
    u = ease_io(prog(t, C["s16.c"], 0.6))
    yy = lerp(760, 560, u)
    E.foco(c, t, C["s16"] + 0.5, 0.5, lambda a: papel(c, px + 210, yy, 380, 170, -4 * (1 - u), a))
    sep = ep(t, C["s16.b"], 0.6)
    for i in range(4):
        x = px + 70 + i * 92
        q(c, x, yy - 52 + 4 * (1 - u) * (i - 1.5), 18, "+", sep)
        q(c, x, yy + 52 + 4 * (1 - u) * (i - 1.5), 18, "−", sep)
    if t >= C["s16.c"]:
        F.seta(c, px + 470, 760, px + 470, 600, E.COR, ep(t, C["s16.c"], 0.3), 9, None, ease_out(prog(t, C["s16.c"], 0.5)))


def _ao_longo(pts, v):
    comp = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    alvo = sum(comp) * max(0, min(1, v))
    for (x0, y0), (x1, y1), L in zip(pts, pts[1:], comp):
        if alvo <= L:
            f = alvo / L if L else 0
            return lerp(x0, x1, f), lerp(y0, y1, f)
        alvo -= L
    return pts[-1]


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s17"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s17.a"], [("ganhou", "i", 96), ("prótons?", "g", 92, ERRADO)], XE, 360)
    if t >= C["s17.b"]:
        E.risco(c, XE - 10, 380, XE + 860, 290, t, C["s17.b"], largura=12)
    E.foco(c, t, C["s17.b"] + 0.2, 0.5, lambda a: E.orbita(c, 1560, 300, 150, a=a, giro=8 * math.sin(t * 0.6)))
    E.frase(c, t, C["s17.b"] + 0.5, ps("prótons ficam no núcleo", "i", 56, TINTA2), 1560, 470, "center", 0.1)
    for i, (k, x, s, cor, l1, l2) in enumerate((("s17.c", 170, "+", E.COR, "positivo =", "falta de elétrons"),
                                                ("s17.d", 1000, "−", NEG, "negativo =", "excesso de elétrons"))):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 560, 750, 250, p, prog_=p)
        E.foco(c, t, C[k] + 0.1, 0.4, lambda a, x=x, s=s: q(c, x + 90, 685, 46, s, a))
        E.frase(c, t, C[k] + 0.2, [(l1, "i", 62)], x + 170, 660)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 58, cor if s == "+" else NEG)], x + 170, 750)
    E.frase(c, t, C["s17.e"], [("indução:", "i", 60), ("perdeu", "g", 58), ("elétrons", "g", 58, NEG), ("para", "i", 60), ("a", "i", 60), ("terra", "i", 60)],
            W / 2, 940, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s18():
        E.frase(c, t, C["s18"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s18.a"], [("o", "i", 70, CLARO), ("sinal", "g", 70, BR), ("de", "i", 70, CLARO), ("cada", "i", 70, CLARO), ("jeito", "i", 70, CLARO)], W / 2, 280, "center", 0.12)
        linhas = (("s18.b", "atrito", "sinais opostos", ("+", "−")), ("s18.c", "contato", "mesmo sinal", ("+", "+")),
                  ("s18.d", "indução", "com terra: oposto", ("−", "+")))
        for i, (k, nome, regra, ss) in enumerate(linhas):
            y = 430 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 24, 46, a=a), centro(c, str(i + 1), 330, y - 2, 54, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(nome, "g", 70, BR)], 420, y)
            E.frase(c, t, C[k] + 0.4, [(regra, "i", 70, CLARO)], 820, y)
            E.foco(c, t, C[k] + 0.7, 0.4, lambda a, y=y, ss=ss, i=i: (q(c, 1470, y - 24, 34, ss[0], a), q(c, 1570, y - 24, 34, ss[1], a)))
        E.formula_em(c, t, C["s18.e"], "cada uma = f{Q₁ + Q₂}{2}", W / 2, 950, 80, "g", BR, "center")
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19.a"], ps("a carga total", "i", 76, CLARO) + [("não", "g", 76, BR), ("muda", "g", 76, BR)], W / 2, 230, "center", 0.12)
    E.frase(c, t, C["s19.a"] + 1.4, ps("o que um perde, o outro ganha", "i", 60, CLARO), W / 2, 330, "center", 0.1)
    E.frase(c, t, C["s19.b"], [("não", "g", 66, ERRADO), ("vale", "g", 66, ERRADO), ("meio", "i", 70, CLARO), ("a", "i", 70, CLARO), ("meio:", "i", 70, CLARO)], W / 2, 500, "center", 0.12)
    E.foco(c, t, C["s19.b"] + 0.8, 0.5, lambda a: (E.bola(c, 760, 720, 150, METAL, a), E.bola(c, 1180, 760, 80, METAL, a)))
    E.foco(c, t, C["s19.b"] + 1.6, 0.4, lambda a: (E.pilula(c, "mais carga", 760, 930, 40, "b", fundo=E.COR, a=a),
                                                  E.pilula(c, "menos", 1180, 930, 40, "b", fundo=TINTA2, a=a)))
    E.frase(c, t, C["s19.b"] + 2.2, ps("tamanhos diferentes", "i", 60, CLARO), 1600, 760, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s20.a"] - 0.4, [("esfera", "i", 78), ("de", "i", 78), ("metal:", "i", 78)], XE, 330)
    E.formula_em(c, t, C["s20.a"], "Q = −3,2 × 10^{−6} C", XE, 450, 92, "g", COR)
    E.frase(c, t, C["s20.b"], [("ganhou", "g", 70), ("ou", "i", 76), ("perdeu?", "g", 70)], XE, 590, passo=0.15)
    E.frase(c, t, C["s20.b"] + 1.0, [("quantos", "i", 76), ("elétrons?", "g", 70, COR)], XE, 690, passo=0.15)
    E.frase(c, t, C["s20.c"], ps("encosta em outra igual, neutra", "i", 66), XE, 830, passo=0.1)
    E.frase(c, t, C["s20.d"], [("carga", "i", 72), ("de", "i", 72), ("cada", "i", 72), ("uma?", "g", 68, COR)], XE, 940, passo=0.15)
    if t < C["s21"]:
        E.foco(c, t, C["s20.a"], 0.5, lambda a: esfera_metal(c, 1450, 450, 125, a))
        for i, (dx, dy) in enumerate(((-60, -50), (30, -70), (70, 10), (-40, 40), (20, 70))):
            E.foco(c, t, C["s20.a"] + 0.4 + 0.08 * i, 0.3, lambda a, dx=dx, dy=dy: q(c, 1450 + dx * 0.85, 450 + dy * 0.85, 22, "−", a))
        E.foco(c, t, C["s20.c"], 0.5, lambda a: (esfera_metal(c, 1640, 800, 125, a), centro(c, "igual, neutra", 1640, 990, 44, "i", TINTA2, a)))
    else:
        E.relogio(c, t, C["s21.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s22():
        E.frase(c, t, C["s22.a"], [("negativa", "g", 70, NEG), ("→", "g", 70, TINTA2), ("ganhou", "i", 76), ("elétrons", "g", 70)], XE, 210, passo=0.15)
        E.formula_em(c, t, C["s22.b"], "n = f{Q}{e} = f{3,2 × 10^{−6}}{1,6 × 10^{−19}}", W / 2, 430, 92, "g", TINTA, "center")
        E.formula_em(c, t, C["s22.c"], "f{3,2}{1,6} = 2", W / 2 - 430, 670, 84, "g", COR, "center")
        E.formula_em(c, t, C["s22.d"], "f{10^{−6}}{10^{−19}} = 10^{13}", W / 2 + 330, 670, 84, "g", COR, "center")
        E.foco(c, t, C["s22.d"] + 1.4, 0.4, lambda a: centro(c, "−6 + 19 = 13", W / 2 + 330, 800, 50, "b", TINTA2, a))
        E.foco(c, t, C["s22.e"], 0.5, lambda a: pilula_f(c, "n = 2 × 10^{13} elétrons", W / 2, 940, 72, a=a))
    E.saida(c, t, C["s23"] - 0.1, s22)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], ps("no contato com a neutra", "i", 72, TINTA2), XE, 210, passo=0.12)
    E.formula_em(c, t, C["s23.a"], "f{−3,2 × 10^{−6} + 0}{2}", W / 2, 420, 100, "g", TINTA, "center")
    E.foco(c, t, C["s23.b"], 0.4, lambda a: centro(c, "÷ 2: as esferas são iguais", W / 2, 560, 50, "i", TINTA2, a))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: pilula_f(c, "−1,6 × 10^{−6} C cada", W / 2, 700, 76, fundo=NEG, a=a))
    for x in (W / 2 - 200, W / 2 + 200):
        E.foco(c, t, C["s23.d"], 0.5, lambda a, x=x: (esfera_metal(c, x, 910, 85, a), q(c, x - 25, 900, 20, "−", a), q(c, x + 28, 925, 20, "−", a)))
    E.foco(c, t, C["s23.d"] + 0.3, 0.4, lambda a: E.pilula(c, "mesmo sinal", 1560, 910, 44, "g", fundo=E.COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s24.a", [("quem", "i", 70), ("se", "i", 70), ("mexe:", "i", 70), ("elétrons", "g", 70, NEG)]),
                 ("s24.b", [("Q = n · e", "g", 76)]),
                 ("s24.c", [("atrito:", "g", 62), ("opostos", "i", 66), ("·", "g", 62, COR), ("contato:", "g", 62), ("mesmo", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
        E.frase(c, t, C["s24.c"] + 1.6, [("indução", "g", 62), ("com", "i", 66), ("terra:", "i", 66), ("oposto", "i", 66)], 360, 850, passo=0.12)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s25.a"], [("lei", "i", 120), ("de", "i", 120), ("Coulomb", "g", 120, COR)], XE, 410)
    # duas cargas e a força; depois a distância dobra e a força cai para um quarto
    y = 720
    u = ease_io(prog(t, C["s25.b"] + 0.4, 0.9))
    x1, x2 = 400, lerp(760, 1120, u)
    F.carga(c, t, C["s25.a"] + 0.4, x1, y, 56, "+")
    F.carga(c, t, C["s25.a"] + 0.6, x2, y, 56, "+")
    k = lerp(1, 0.25, u)
    if t >= C["s25.a"] + 1.0:
        a_ = ep(t, C["s25.a"] + 1.0, 0.3)
        F.seta(c, x1 - 70, y, x1 - 70 - 220 * k, y, E.COR, a_, 9)
        F.seta(c, x2 + 70, y, x2 + 70 + 220 * k, y, E.COR, a_, 9)
    E.foco(c, t, C["s25.b"] + 0.4, 0.4, lambda a: E.formula(c, "2d → f{F}{4}", 760, 900, 70, "g", TINTA, a, "center"))
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, carga=b_carga, quantidade=b_quantidade, atrito=b_atrito, contato=b_contato,
              inducao=b_inducao, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
