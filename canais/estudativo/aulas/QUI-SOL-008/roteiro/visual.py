"""Visual — Estudativo · QUI-SOL-008: pressão de vapor e ponto de ebulição. Primeira aula do módulo de propriedades coligativas.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py).

LINGUAGEM VISUAL DAS PROPRIEDADES COLIGATIVAS (QUI-SOL-008 a 011 copiam daqui):
- PARTÍCULA DE ÁGUA = bolinha azul-clara (AGUA_P) com contorno; SOLUTO = bolinha turquesa (E.COR), maior. Íons de um sal que se
  separa: bolinhas turquesa e cinza (cátion e ânion) com um tracinho de carga; molécula de açúcar = bolinha âmbar, inteira.
- POTE FECHADO (pote): líquido embaixo, partículas de vapor voando em cima e batendo na tampa. Mais vapor = mais pressão de vapor.
- O EMPATE (duelo): duas colunas lado a lado, "pressão de vapor" em turquesa e "pressão de fora" em cinza-tinta, com a linha
  tracejada do topo da de fora. Quando a turquesa alcança a cinza, o líquido ferve (bolhas no fundo). É a figura que explica
  montanha, panela de pressão e soluto, sempre igual.
- TERMÔMETRO (termometro) ao lado do recipiente, com o valor em °C numa pílula.
- SETAS DE PRESSÃO DE FORA: setas cinza para baixo sobre a superfície; menos setas = menos pressão (montanha), mais = panela.
- Coligativo × não coligativo: pílula turquesa "coligativo" e pílula tinta "não é coligativo", nunca só cor.
Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-008_pressao_de_vapor_ebulicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vapor", "ferver", "lugares", "sal", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AGUA_P = "#7CC4EA"
PANELA = "#5B6470"

# ordem da questão (temperaturas aproximadas de ebulição)
EBUL = dict(A=100.0, B=100.3, C=95.0)
assert sorted(EBUL, key=EBUL.get, reverse=True) == ["B", "A", "C"]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças (candidatas ao kit: pote, duelo, termometro, setas_fora, bolhas) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, est, cor, a))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def particula(c, x, y, r, cor, a=1.0):
    c.drawCircle(x, y, r, M.paint(cor, a))
    c.drawCircle(x, y, r, M.paint(M.mix(cor, "#000000", 0.35), 0.6 * a, stroke=2))


def pote(c, t, x, y, w, h, n_liq=40, n_sol=0, n_vap=8, agita=1.0, a=1.0, semente=3, tampa=True, nivel=0.5):
    """recipiente fechado: líquido com partículas embaixo, vapor voando em cima"""
    if a <= 0:
        return
    rnd = random.Random(semente)
    yl = y + h * (1 - nivel)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint("#FFFFFF", 0.5 * a))
    c.save(); c.clipRect(skia.Rect.MakeLTRB(x, yl, x + w, y + h))
    c.drawRect(skia.Rect.MakeLTRB(x, yl, x + w, y + h), M.paint(Q.AGUA, 0.8 * a))
    c.restore()
    r = 11
    cols = max(1, int((w - 20) / (2.3 * r)))
    tot = n_liq + n_sol
    sol_idx = set(rnd.sample(range(tot), n_sol)) if n_sol else set()
    for i in range(tot):
        cx = x + 14 + r + (i % cols) * (w - 28 - 2 * r) / max(1, cols - 1)
        cy = yl + 14 + r + (i // cols) * 2.2 * r
        if cy > y + h - r - 6:
            continue
        ph = rnd.random() * 6.3
        dx, dy = 3 * agita * math.sin(t * 4 + ph), 3 * agita * math.cos(t * 3.4 + ph)
        if i in sol_idx:
            particula(c, cx + dx, cy + dy, r * 1.25, E.COR, a)
        else:
            particula(c, cx + dx, cy + dy, r, AGUA_P, a)
    # vapor: partículas voando no espaço de cima, rebatendo
    for k in range(n_vap):
        vx, vy = 90 + rnd.random() * 80, 70 + rnd.random() * 60
        fx, fy = rnd.random(), rnd.random()
        px = (fx * (w - 2 * r) + vx * t) % (2 * (w - 2 * r))
        py = (fy * (yl - y - 2 * r - 6) + vy * t) % (2 * max(1, yl - y - 2 * r - 6))
        px = px if px < w - 2 * r else 2 * (w - 2 * r) - px
        py = py if py < yl - y - 2 * r - 6 else 2 * (yl - y - 2 * r - 6) - py
        particula(c, x + r + px, y + r + 4 + py, r * 0.9, AGUA_P, 0.9 * a)
    vidro = M.paint(Q.VIDRO, a, stroke=5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), vidro)
    if tampa:
        M.rrect(c, x - 14, y - 22, w + 28, 26, 10, TINTA2, a)


def duelo(c, t, t0, x, ybase, h, pv, pf, a=1.0, size=36, escuro=False, rot=True):
    """o empate: coluna da pressão de vapor (turquesa) e coluna da pressão de fora (cinza), alturas 0..1 de h"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    tinta = BR if escuro else TINTA
    wcol, gap = 90, 90
    for k, (v, cor, nome) in enumerate(((pv, E.COR, "vapor"), (pf, "#6E6E76" if not escuro else "#9AA0A8", "de fora"))):
        xx = x + k * (wcol + gap)
        hh = h * max(0.0, v)
        M.rrect(c, xx, ybase - h, wcol, h, 14, "#FFFFFF" if not escuro else "#1C1E28", 0.6 * q)
        M.rrect(c, xx, ybase - hh, wcol, hh, 14, cor, q)
        if rot:
            centro(c, nome, xx + wcol / 2, ybase + size * 1.2, size, "b", tinta, q)
    M.line(c, x - 20, ybase - h * pf, x + 2 * wcol + gap + 20, ybase - h * pf, tinta, 0.8 * q, 3, dash=[12, 9])
    if rot:
        centro(c, "pressão", x + wcol + gap / 2, ybase - h - size * 0.6, size * 1.2, "i", tinta if not escuro else CLARO, q)


def termometro(c, x, y, h, nivel, cor=ERRADO, a=1.0, valor=None, escuro=False):
    if a <= 0:
        return
    M.rrect(c, x - 14, y - h, 28, h, 14, "#FFFFFF", a, stroke=3, stroke_color=TINTA2)
    M.rrect(c, x - 7, y - 10 - (h - 30) * nivel, 14, (h - 30) * nivel + 10, 7, cor, a)
    c.drawCircle(x, y + 6, 24, M.paint(cor, a))
    c.drawCircle(x, y + 6, 24, M.paint(TINTA2, a, stroke=3))
    if valor:
        E.pilula(c, valor, x, y - h - 40, 40, "g", fundo=TINTA if not escuro else "#3A3B42", a=a)


def setas_fora(c, t, t0, x0, x1, y, n, cor=TINTA2, a=1.0, comp=70):
    """setas para baixo: a pressão de fora apertando a superfície"""
    q = ep(t, t0, 0.5) * a
    if q <= 0 or n <= 0:
        return
    for k in range(n):
        xx = lerp(x0, x1, (k + 0.5) / n)
        dy = 6 * math.sin(t * 3 + k)
        M.arrow(c, xx, y - comp - 30 + dy, xx, y - 12 + dy, cor, q, 5, 18)


def bolhas(c, t, t0, x, y0, y1, w, n=10, a=1.0, semente=4):
    """bolhas de vapor subindo no líquido: ferveu"""
    if t < t0:
        return
    rnd = random.Random(semente)
    q = ep(t, t0, 0.5) * a
    for i in range(n):
        xx = x + 20 + rnd.random() * (w - 40)
        per = 1.0 + rnd.random() * 0.8
        u = (((t - t0) + rnd.random() * per) % per) / per
        yy = lerp(y0, y1, u)
        r = 6 + 10 * u
        c.drawCircle(xx + 4 * math.sin(u * 8 + i), yy, r, M.paint("#FFFFFF", 0.6 * q))
        c.drawCircle(xx + 4 * math.sin(u * 8 + i), yy, r, M.paint(TINTA2, 0.7 * q, stroke=2))


def panela(c, t, cx, yb, w, h, a=1.0, pressao=False, ferve=None, sal=0):
    """panela no fogo; pressao=True põe a tampa travada com válvula"""
    if a <= 0:
        return
    for k in range(5):
        fx = cx - w * 0.35 + k * w * 0.175
        fh = 50 + 14 * math.sin(t * 9 + k * 1.7)
        pth = skia.Path(); pth.moveTo(fx - 18, yb + 70); pth.quadTo(fx, yb + 70 - fh * 1.6, fx + 18, yb + 70); pth.close()
        c.drawPath(pth, M.paint("#F2994A", 0.85 * a))
    M.rrect(c, cx - w / 2, yb - h, w, h, 24, PANELA, a)
    M.rrect(c, cx - w / 2 + 16, yb - h + 20, w - 32, h - 40, 18, Q.AGUA, a)
    if sal:
        rnd = random.Random(5)
        for i in range(sal):
            c.drawCircle(cx - w / 2 + 40 + rnd.random() * (w - 80), yb - h + 50 + rnd.random() * (h - 100), 9, M.paint(E.COR, a))
    if ferve is not None and t >= ferve:
        bolhas(c, t, ferve, cx - w / 2 + 16, yb - 30, yb - h + 30, w - 32, 12, a)
    M.rrect(c, cx - w / 2 - 50, yb - h + 20, 50, 22, 10, TINTA, a)
    M.rrect(c, cx + w / 2, yb - h + 20, 50, 22, 10, TINTA, a)
    if pressao:
        M.rrect(c, cx - w / 2 - 10, yb - h - 30, w + 20, 34, 14, TINTA, a)
        M.rrect(c, cx - 16, yb - h - 80, 32, 54, 8, "#9AA0A8", a)
        for k in range(3):
            u = ((t * 1.3 + k * 0.33) % 1.0)
            c.drawCircle(cx + 10 * math.sin(u * 6), yb - h - 90 - 90 * u, 10 + 14 * u, M.paint("#FFFFFF", 0.5 * (1 - u) * a))


def montanha(c, x, y, w, h, a=1.0):
    if a <= 0:
        return
    pth = skia.Path(); pth.moveTo(x, y); pth.lineTo(x + w * 0.42, y - h); pth.lineTo(x + w * 0.58, y - h * 0.82); pth.lineTo(x + w, y); pth.close()
    c.drawPath(pth, M.paint("#8FA3AD", a))
    neve = skia.Path(); neve.moveTo(x + w * 0.32, y - h * 0.76); neve.lineTo(x + w * 0.42, y - h); neve.lineTo(x + w * 0.52, y - h * 0.86)
    neve.lineTo(x + w * 0.46, y - h * 0.8); neve.lineTo(x + w * 0.4, y - h * 0.84); neve.close()
    c.drawPath(neve, M.paint("#FFFFFF", a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cols = ((C["s01.a"], 380, "La Paz", "88 °C", 0.45), (C["s01.b"], 960, "panela de pressão", "120 °C", 0.8), (C["s01.c"], 1540, "água com sal", "> 100 °C", 0.62))
        for k, (ti, cx, nome, val, nv) in enumerate(cols):
            if k == 0:
                E.foco(c, t, ti, 0.5, lambda a: montanha(c, cx - 230, 760, 460, 360, a))
                E.foco(c, t, ti + 0.4, 0.5, lambda a: panela(c, t, cx, 830, 220, 110, a, ferve=ti + 0.5))
            elif k == 1:
                E.foco(c, t, ti, 0.5, lambda a: panela(c, t, cx, 830, 300, 170, a, pressao=True))
            else:
                E.foco(c, t, ti, 0.5, lambda a: panela(c, t, cx, 830, 300, 170, a, ferve=ti + 0.6, sal=14))
            E.foco(c, t, ti + 0.3, 0.4, lambda a, cx=cx, val=val, nv=nv: termometro(c, cx + 200, 640, 260, nv, ERRADO, a, val))
            rotulo(c, t, ti + 0.2, nome, cx, 980, 50, TINTA, "b")
        E.frase(c, t, C["s01.d"], ps("três fatos,", "i", 70) + [("uma ideia só", "g", 66, COR)], W / 2, 200, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("pressão", "g", 70, COR), ("de", "i", 74), ("vapor", "g", 70, COR)]),
                 (C["s02.c"], [("os", "i", 74), ("três", "g", 70), ("casos", "i", 74)]),
                 (C["s02.d"], [("uma", "i", 74), ("pergunta", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], ps("esquentou: partículas", "i", 62) + [("mais agitadas", "g", 58, COR)], XE, 300, passo=0.1)
    E.foco(c, t, C["s03.a"] + 0.3, 0.5, lambda a: pote(c, t, 1300, 200, 460, 240, 26, 0, 0, 1 + 3 * ep(t, C["s03.a"] + 1.0, 1.0), a, tampa=False, nivel=0.8))
    E.frase(c, t, C["s03.b"], [("pressão", "g", 62, COR)] + ps("de um gás = choque das partículas", "i", 62), XE, 560, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("nível do mar:", "i", 62) + [("1 atm", "g", 62, COR)], XE, 780, passo=0.1)
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "= 760 mmHg", XE + 560, 780, 62, "g", TINTA, a))
    setas_fora(c, t, C["s03.c"] + 0.3, 1300, 1760, 900, 5)
    E.foco(c, t, C["s03.c"] + 0.3, 0.5, lambda a: M.rrect(c, 1280, 900, 500, 100, 16, Q.AGUA, a))
    rotulo(c, t, C["s03.c"] + 0.6, "o ar aperta a superfície", 1530, 1050, 44, TINTA, "b")


# ---------------- pressão de vapor ----------------
PX, PY, PW, PH = 1150, 260, 520, 640


def b_vapor(c, t, C, b):
    quente = ep(t, C["s05.c"], 1.2)
    nvap = int(lerp(2, 8, ep(t, C["s04.b"], 1.5)) + 8 * quente)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: pote(c, t, PX, PY, PW, PH, 44, 0, nvap, 1 + 2 * quente, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: termometro(c, PX + PW + 90, PY + PH - 20, 360, lerp(0.35, 0.8, quente), ERRADO, a))
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("água num pote", "i", 66) + [("fechado", "g", 62, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("as mais agitadas", "i", 62) + [("escapam", "g", 58, COR)], XE, 420, passo=0.1)
        E.frase(c, t, C["s04.b"] + 1.6, ps("e viram vapor", "i", 62), XE, 510, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("o vapor fica preso em cima", "i", 62), XE, 680, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("batendo nas paredes", "i", 62, TINTA2), XE, 780, passo=0.1)
        return
    E.frase(c, t, C["s05.a"], [("pressão", "g", 100, COR)], XE, 300)
    E.frase(c, t, C["s05.a"] + 0.4, [("de", "i", 100), ("vapor", "g", 100, COR)], XE, 430, passo=0.12)
    E.frase(c, t, C["s05.b"], ps("a vontade do líquido de evaporar", "i", 58), XE, 560, passo=0.1)
    E.frase(c, t, C["s05.c"], [("esquentou", "g", 62, ERRADO), ("→", "g", 62, TINTA2)] + ps("mais partículas escapam", "i", 60), XE, 740, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("a pressão de vapor", "i", 62) + [("sobe", "g", 60, COR)], XE, 840, passo=0.1)


# ---------------- ferver: o empate ----------------
def b_ferver(c, t, C, b):
    # béquer aberto aquecendo e a dupla de colunas
    if t < C["s07"]:
        t_ini, dur = C["s06.c"] - 0.6, 3.0
    else:
        t_ini, dur = C["s07.b"], 2.0
    temp = lerp(25, 100, ease_io(prog(t, t_ini, dur)))
    pv = (temp - 20) / 80
    cx, yb = 1080, 900
    Q.bequer(c, t, C["s06"], cx, yb, 380, 420, 0.7, Q.AGUA, graduacao=False)
    setas_fora(c, t, C["s06.b"], cx - 160, cx + 160, yb - 420 * 0.7, 4)
    bolhas(c, t, t_ini + dur, cx - 190, yb - 20, yb - 420 * 0.7 + 10, 380, 12)
    E.foco(c, t, C["s06"], 0.5, lambda a: termometro(c, cx + 260, yb - 40, 360, (temp - 20) / 90, ERRADO, a, f"{round(temp)} °C"))
    duelo(c, t, C["s06.c"] - 0.6, 1520, 900, 520, pv, 1.0)
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("ferver", "g", 80, COR)], XE, 260)
        E.frase(c, t, C["s06.a"] + 0.6, ps("formar bolhas de vapor dentro do líquido", "i", 46), XE, 340, passo=0.08)
        E.frase(c, t, C["s06.b"], ps("o ar de fora", "i", 56) + [("aperta", "g", 54, TINTA)], XE, 480, passo=0.1)
        E.frase(c, t, C["s06.c"], ps("a bolha só nasce quando", "i", 52), XE, 600, passo=0.08)
        E.frase(c, t, C["s06.c"] + 1.4, [("vapor", "g", 52, COR), ("=", "g", 52, TINTA2), ("de fora", "g", 52)], XE, 680, passo=0.1)
        E.frase(c, t, C["s06.d"], [("ponto", "g", 60, COR), ("de", "i", 64), ("ebulição", "g", 60, COR)], XE, 830, passo=0.12)
        rotulo(c, t, C["s06.d"] + 1.2, "a temperatura do empate", XE + 270, 900, 42)
        return
    E.frase(c, t, C["s07.a"], [("praia:", "i", 64), ("1 atm", "g", 62, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("a pressão de vapor da água", "i", 52), XE, 440, passo=0.08)
    E.frase(c, t, C["s07.b"] + 1.6, ps("chega a 1 atm a", "i", 52) + [("100 °C", "g", 52, COR)], XE, 520, passo=0.08)
    E.frase(c, t, C["s07.c"], ps("ferve a", "i", 66) + [("100 °C", "g", 66, COR)], XE, 720, passo=0.12)


# ---------------- montanha e panela ----------------
def b_lugares(c, t, C, b):
    if t < C["s09"]:
        E.foco(c, t, C["s08.a"], 0.6, lambda a: montanha(c, 760, 920, 700, 560, a))
        cx, yb = 1110, 900
        ferve = C["s08.d"]
        E.foco(c, t, C["s08.a"] + 0.6, 0.5, lambda a: panela(c, t, cx, yb, 220, 110, a, ferve=ferve))
        setas_fora(c, t, C["s08.b"], cx - 80, cx + 80, yb - 120, 2, comp=50)
        temp = lerp(25, 88, ease_io(prog(t, C["s08.c"], 2.0)))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: termometro(c, cx + 200, yb - 30, 280, (temp - 20) / 90, ERRADO, a, f"{round(temp)} °C"))
        pf = 0.68
        duelo(c, t, C["s08.b"], 1520, 900, 520, min(pf, (temp - 20) / 80 * 1.0), pf)
        E.frase(c, t, C["s08.a"], ps("no alto:", "i", 62) + [("menos ar", "g", 58, COR)], XE, 250, passo=0.12)
        E.frase(c, t, C["s08.b"], ps("pressão de fora", "i", 58) + [("menor", "g", 56, COR)], XE, 360, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("o empate vem", "i", 58) + [("mais cedo", "g", 56, COR)], XE, 470, passo=0.1)
        E.frase(c, t, C["s08.d"], [("La Paz:", "g", 58), ("≈ 88 °C", "g", 62, COR)], XE, 600, passo=0.12)
        rotulo(c, t, C["s08.e"], "o feijão demora mais", XE + 220, 690, 46, TINTA, "b")
        return
    cx, yb = 1060, 900
    E.foco(c, t, C["s09"], 0.5, lambda a: panela(c, t, cx, yb, 340, 190, a, pressao=True, ferve=C["s09.d"]))
    setas_fora(c, t, C["s09.b"], cx - 150, cx + 150, yb - 200, 6, comp=60)
    temp = lerp(25, 120, ease_io(prog(t, C["s09.c"], 2.2)))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: termometro(c, cx + 260, yb - 30, 300, min(1, (temp - 20) / 105), ERRADO, a, f"{round(temp)} °C"))
    pf = 1.0
    duelo(c, t, C["s09.b"], 1520, 900, 420, min(pf, (temp - 20) / 100), pf)
    E.frase(c, t, C["s09.a"], [("panela", "g", 62), ("de", "i", 66), ("pressão:", "g", 62)] + ps("o contrário", "i", 66), XE, 250, passo=0.12)
    E.frase(c, t, C["s09.b"], ps("a tampa prende o vapor:", "i", 54), XE, 360, passo=0.1)
    E.frase(c, t, C["s09.b"] + 1.6, [("≈ 2 atm", "g", 58, COR)] + ps("lá dentro", "i", 58), XE, 440, passo=0.1)
    E.frase(c, t, C["s09.c"], ps("o empate pede", "i", 56) + [("temperatura maior", "g", 54, COR)], XE, 560, passo=0.1)
    E.frase(c, t, C["s09.d"], [("≈ 120 °C", "g", 66, COR)], XE, 680)
    E.frase(c, t, C["s09.e"], [("mais", "b", 40), ("quente:", "b", 40), ("cozinha", "b", 40), ("mais", "b", 40), ("rápido", "b", 40)], XE, 770, passo=0.08)


# ---------------- o sal ----------------
def b_sal(c, t, C, b):
    xs = (110, 540)
    nv_pura, nv_sal = 10, 4
    E.foco(c, t, C["s10"], 0.5, lambda a: pote(c, t, xs[0], 300, 390, 500, 36, 0, nv_pura, 1.5, a, semente=3))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: pote(c, t, xs[1], 300, 390, 500, 24, 12, nv_sal if t >= C["s10.b"] else nv_pura, 1.5, a, semente=5))
    rotulo(c, t, C["s10"] + 0.3, "água pura", xs[0] + 195, 880, 48, TINTA, "b")
    rotulo(c, t, C["s10.a"] + 0.3, "água com sal", xs[1] + 195, 880, 48, COR, "b")
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("o sal ocupa lugar", "i", 56), 1060, 300, passo=0.08)
        E.frase(c, t, C["s10.a"] + 1.0, ps("na superfície", "i", 56), 1060, 380, passo=0.08)
        E.frase(c, t, C["s10.b"], ps("menos água escapa", "i", 56), 1060, 500, passo=0.1)
        E.frase(c, t, C["s10.c"], ps("pressão de vapor", "i", 56) + [("menor", "g", 54, COR)], 1060, 620, passo=0.1)
        duelo(c, t, C["s10.c"], 1540, 1000, 270, lerp(0.95, 0.6, ep(t, C["s10.c"] + 0.4, 0.8)), 1.0)
        E.frase(c, t, C["s10.d"], [("tonoscopia", "g", 76, COR)], 1060, 800)
        return
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("demora mais para o empate", "i", 56), 1060, 300, passo=0.08)
        E.frase(c, t, C["s11.b"], ps("precisa", "i", 58) + [("esquentar mais", "g", 56, COR)], 1060, 420, passo=0.1)
        E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "ferve acima de 100 °C", 1060, 560, 66, "g", ERRADO, a))
        E.frase(c, t, C["s11.d"], [("ebulioscopia", "g", 80, COR)], 1060, 740)
        rotulo(c, t, C["s11.d"] + 0.8, "a subida do ponto de ebulição", 1380, 830, 44)
        return
    E.frase(c, t, C["s12.a"], ps("importa", "i", 58) + [("quantas", "g", 56, COR)] + ps("partículas,", "i", 58), 1060, 300, passo=0.08)
    E.frase(c, t, C["s12.a"] + 1.4, ps("não qual soluto", "i", 58), 1060, 380, passo=0.08)
    E.frase(c, t, C["s12.b"], ps("depende só da quantidade:", "i", 56), 1060, 500, passo=0.08)
    E.frase(c, t, C["s12.c"], [("efeito", "g", 80), ("coligativo", "g", 80, COR)], 1060, 630, passo=0.12)
    E.frase(c, t, C["s12.d"], ps("soluto que", "i", 56) + [("não evapora:", "g", 54)], 1060, 780, passo=0.1)
    pilula_em(c, t, C["s12.d"] + 1.2, "sal", 1160, 880, 50, E.COR)
    pilula_em(c, t, C["s12.d"] + 1.5, "açúcar", 1360, 880, 50, TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)

    def errado():
        E.frase(c, t, C["s13.a"], ps("o sal faz a água ferver", "i", 66, ERRADO) + [("mais rápido", "g", 62, ERRADO)], XE, 380, passo=0.1)
        if t >= C["s13.a"] + 2.2:
            E.risco(c, XE - 10, 400, XE + 1200, 320, t, C["s13.a"] + 2.2, largura=12)
    errado()
    E.frase(c, t, C["s13.b"], ps("é o contrário: sobe o", "i", 62) + [("ponto de ebulição", "g", 58, COR)], XE, 560, passo=0.1)
    E.frase(c, t, C["s13.b"] + 2.0, ps("e a água demora um pouco mais", "i", 58, TINTA2), XE, 650, passo=0.1)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.formula(c, "1 colher de sal: + menos de 0,5 °C", XE, 820, 66, "g", TINTA, a)))
    pilula_em(c, t, C["s13.d"], "na cozinha, quase nada", XE + 420, 930, 50, E.COR)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: panela(c, t, 1600, 600, 300, 160, a, sal=5))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("o atalho é uma pergunta", "i", 70, CLARO), W / 2, 170, "center", 0.12)
            E.frase(c, t, C["s14.a"], [("o", "i", 140, BR), ("que", "i", 140, BR), ("mudou?", "g", 130, E.CLARO)], W / 2, 400, "center", 0.15)
            E.frase(c, t, C["s14.b"], [("a", "i", 56, CLARO), ("pressão", "g", 54, BR), ("de", "i", 56, CLARO), ("fora", "g", 54, BR)], 520, 600, "center", 0.1)
            rotulo(c, t, C["s14.b"] + 1.2, "montanha, panela", 520, 680, 44, CLARO)
            pilula_em(c, t, C["s14.c"], "não é coligativo", 520, 800, 54, "#3A3B42")
            E.frase(c, t, C["s14.d"], [("o", "i", 56, CLARO), ("que", "i", 56, CLARO), ("está", "i", 56, CLARO), ("dissolvido", "g", 54, BR)], 1400, 600, "center", 0.1)
            rotulo(c, t, C["s14.d"] + 1.2, "sal, açúcar", 1400, 680, 44, CLARO)
            pilula_em(c, t, C["s14.e"], "coligativo", 1400, 800, 54, E.COR)
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15"], ps("a regra das setas", "i", 70, CLARO), W / 2, 160, "center", 0.12)
    linhas = ((C["s15.a"], "pressão de fora ↑", "ferve mais quente"), (C["s15.b"], "pressão de fora ↓", "ferve mais frio"), (C["s15.c"], "soluto ↑", "ferve mais quente"))
    for k, (ti, l, r) in enumerate(linhas):
        y = 320 + k * 120
        E.foco(c, t, ti, 0.5, lambda a, l=l, r=r, y=y: (E.formula(c, l, 900, y, 64, "g", BR, a, "right"),
                                                        E.formula(c, "→", 960, y, 64, "g", CLARO, a, "center"),
                                                        E.formula(c, r, 1020, y, 64, "g", E.CLARO, a)))
    E.frase(c, t, C["s15.d"], ps("tudo é um empate:", "i", 58, CLARO) + [("vapor", "g", 56, BR), ("contra", "i", 58, CLARO), ("de fora", "g", 56, BR)], W / 2, 750, "center", 0.1)
    E.frase(c, t, C["s15.e"], [("não", "g", 54, ERRADO), ("compensa:", "i", 58, CLARO)] + ps("soluto que evapora, como álcool", "i", 58, CLARO), W / 2, 880, "center", 0.1)
    rotulo(c, t, C["s15.e"] + 2.2, "aí a mistura pode ferver abaixo de 100 °C", W / 2, 960, 44, BR, "b")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s16"] + 1.0, ps("três panelas com 1 litro de água", "i", 56, TINTA2), XE, 260, passo=0.1)
    for k, (ti, l, s) in enumerate(((C["s16.a"], "A", "água pura, na praia"), (C["s16.b"], "B", "água com açúcar, na praia"), (C["s16.c"], "C", "água pura, no alto da serra"))):
        y = 400 + k * 110
        E.foco(c, t, ti, 0.4, lambda a, l=l, y=y: (E.bola(c, XE + 40, y - 22, 40, a=a), centro(c, l, XE + 40, y - 2, 50, "g", BR, a)))
        E.frase(c, t, ti + 0.1, ps(s, "i", 60), XE + 100, y, passo=0.08)
    E.frase(c, t, C["s16.d"], [("1", "g", 56, COR)] + ps("ordem: da mais quente para a mais fria", "i", 56), XE, 800, passo=0.08)
    E.frase(c, t, C["s16.e"], [("2", "g", 56, COR)] + ps("qual é efeito coligativo?", "i", 56), XE, 900, passo=0.08)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: panela(c, t, 1480, 640, 300, 160, a))
        E.foco(c, t, C["s16.c"], 0.5, lambda a: montanha(c, 1260, 960, 440, 260, a))
    else:
        E.relogio(c, t, C["s17.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    dados = ((C["s18.a"], "A", "100 °C", 0.6, "referência"), (C["s18.b"], "B", "> 100 °C", 0.8, "soluto: pressão de vapor cai"), (C["s18.c"], "C", "< 100 °C", 0.4, "menos pressão de fora"))
    for k, (ti, l, v, nv, sub) in enumerate(dados):
        y = 300 + k * 200
        E.foco(c, t, ti, 0.4, lambda a, l=l, y=y: (E.bola(c, XE + 40, y - 22, 44, a=a), centro(c, l, XE + 40, y - 2, 54, "g", BR, a)))
        E.foco(c, t, ti + 0.3, 0.4, lambda a, v=v, y=y: E.formula(c, v, XE + 120, y, 72, "g", ERRADO if l != "C" else "#2E86AB", a))
        E.foco(c, t, ti + 0.6, 0.4, lambda a, sub=sub, y=y: E.escreve(c, sub, XE + 480, y - 8, 42, "b", TINTA, a))
    E.frase(c, t, C["s18.d"], ps("ordem:", "i", 66), 1260, 300, passo=0.1)
    E.foco(c, t, C["s18.d"] + 0.6, 0.5, lambda a: E.formula(c, "B > A > C", 1260, 420, 110, "g", COR, a))
    pilula_em(c, t, C["s18.e"], "só B é coligativo", 1480, 620, 56, E.COR)
    rotulo(c, t, C["s18.e"] + 1.0, "em C, mudou a pressão do ar", 1480, 720, 46, TINTA, "b")
    E.foco(c, t, C["s18.e"] + 0.4, 0.5, lambda a: E.selo(c, 1780, 410, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("ferve", "g", 66), ("no", "i", 70), ("empate:", "i", 70), ("vapor", "g", 66, COR), ("=", "g", 66, TINTA2), ("de fora", "g", 66)]),
                 ("s19.b", [("pressão", "g", 66), ("de", "i", 70), ("fora", "g", 66), ("muda", "i", 70), ("a", "i", 70), ("fervura", "i", 70)]),
                 ("s19.c", [("soluto", "g", 66, COR), ("baixa", "i", 70), ("a", "i", 70), ("pressão", "i", 70), ("de", "i", 70), ("vapor", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula:", "i", 80), ("o", "i", 80), ("frio", "g", 76, COR)], XE, 250, passo=0.12)
    E.frase(c, t, C["s20.a"], [("anticongelante", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s20.b"], ps("contar as", "i", 66) + [("partículas", "g", 62, COR)], XE, 560, passo=0.12)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, vapor=b_vapor, ferver=b_ferver, lugares=b_lugares, sal=b_sal, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
