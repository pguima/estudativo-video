"""Visual — Estudativo · FIS-MAG-009: como uma usina gera eletricidade. Linguagem visual do Magnetismo: veja o visual.py da
FIS-MAG-001. Usinas: cadeia de energia = pílulas em fila ligadas por setas (cadeia()), a última, "elétrica", em laranja;
água em azul claro; o gerador = ímã girando dentro de duas bobinas (gerador()); a turbina = roda de pás girando (turbina()).
Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-009_como_uma_usina_gera_eletricidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("gerador", "hidro", "termo", "nuclear", "queda", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
AGUA = "#7FC8E8"
AGUA2 = "#3B8DB5"

# todas as contas da aula (densidade da água 1.000 kg/m³, g = 10 m/s²)
assert 1000 * 100 * 10 * 50 == 50_000_000 and 0.9 * 50e6 == 45e6
assert 1000 * 10 == 10_000 and 10_000 * 100 * 50 == 50_000_000 and 100 * 50 == 5000
assert 20 * 30 == 600 and 10_000 * 600 == 6_000_000 and math.isclose(0.9 * 6e6, 5.4e6)
# unidade: kg/m³ · m³/s · m/s² · m = kg·m²/s³ = W


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas (o mesmo da FIS-CIN-001)"""
    E.frase(c, t, C[cena] + 0.2, ps("lembre", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def cadeia(c, t, itens, x0, y, gap=60, size=46, ultima=True):
    """cadeia de energia: itens = [(instante, texto)], pílulas em fila com setas; a última em laranja"""
    x = x0
    for i, (ti, s) in enumerate(itens):
        w = E.larg(s, "g", size) + size
        cx = x + w / 2
        fim = i == len(itens) - 1 and ultima
        E.foco(c, t, ti, 0.45, lambda a, s=s, cx=cx, fim=fim: E.pilula(c, s, cx, y, size, "g", fundo=E.COR if fim else TINTA, a=a))
        if i:
            E.foco(c, t, ti, 0.4, lambda a, x=x: F.seta(c, x - gap + 8, y - size * 0.35, x - 8, y - size * 0.35, TINTA2, a, 6, 18))
        x += w + gap
    return x


def turbina(c, cx, cy, r, ang, a=1.0, cor=None):
    """roda de pás girando (ang em graus)"""
    if a <= 0:
        return
    cor = cor or TINTA
    for k in range(8):
        g = math.radians(ang + 45 * k)
        x1, y1 = cx + r * math.cos(g), cy + r * math.sin(g)
        M.line(c, cx, cy, x1, y1, cor, a, 8)
        M.line(c, x1, y1, x1 + r * 0.3 * math.cos(g + 1.3), y1 + r * 0.3 * math.sin(g + 1.3), cor, a, 8)
    c.drawCircle(cx, cy, r * 0.18, M.paint(E.COR, a))


def gerador(c, cx, cy, r, ang, a=1.0):
    """gerador: carcaça com duas bobinas e um ímã girando no meio (ang em graus)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=10))
    for lado in (-1, 1):
        x = cx + lado * r * 0.78
        M.rrect(c, x - r * 0.14, cy - r * 0.4, r * 0.28, r * 0.8, 10, "#C27A44", a)
        for k in range(5):
            y = cy - r * 0.32 + k * r * 0.16
            M.line(c, x - r * 0.16, y, x + r * 0.16, y, "#7A4520", a, 4)
    c.save(); c.translate(cx, cy); c.rotate(-ang)
    for lado, cor in ((1, E.COR), (-1, NEG)):
        x0 = 0 if lado > 0 else -r * 0.5
        M.rrect(c, x0, -r * 0.14, r * 0.5, r * 0.28, 8, cor, a)
    c.restore()
    c.drawCircle(cx, cy, r * 0.06, M.paint(TINTA, a))


def represa(c, x, y, a=1.0):
    """represa: água alta à esquerda, muro, tubo descendo"""
    if a <= 0:
        return
    M.rrect(c, x, y, 260, 300, 6, AGUA, a)
    p = skia.Path(); p.moveTo(x + 260, y - 20); p.lineTo(x + 330, y - 20); p.lineTo(x + 400, y + 300); p.lineTo(x + 260, y + 300); p.close()
    c.drawPath(p, M.paint("#B9B3A6", a))
    M.line(c, x + 230, y + 220, x + 520, y + 400, AGUA2, a, 26)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        xs = (360, 960, 1560)
        nomes = (("s01.a", "hidrelétrica"), ("s01.b", "termelétrica"), ("s01.c", "nuclear"))
        for i, (k, s) in enumerate(nomes):
            x = xs[i]
            def icone(a, i=i, x=x):
                if i == 0:
                    M.rrect(c, x - 160, 360, 180, 200, 6, AGUA, a)
                    p = skia.Path(); p.moveTo(x + 20, 340); p.lineTo(x + 70, 340); p.lineTo(x + 130, 560); p.lineTo(x + 20, 560); p.close()
                    c.drawPath(p, M.paint("#B9B3A6", a))
                elif i == 1:
                    M.rrect(c, x - 150, 430, 300, 130, 8, "#B9B3A6", a)
                    M.rrect(c, x + 60, 300, 50, 140, 4, TINTA2, a)
                    for k in range(3):
                        c.drawCircle(x + 90 + 30 * k, 270 - 30 * k, 26 + 6 * k, M.paint("#D9D6CF", a))
                else:
                    p = skia.Path(); p.moveTo(x - 120, 560); p.quadTo(x - 50, 430, x - 90, 320); p.lineTo(x + 90, 320); p.quadTo(x + 50, 430, x + 120, 560); p.close()
                    c.drawPath(p, M.paint("#C9C5BC", a))
                    for k in range(3):
                        c.drawCircle(x - 30 + 30 * k, 290 - 20 * k, 30, M.paint("#E4E1DA", a))
            E.foco(c, t, C[k], 0.5, icone)
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, x=x, s=s: centro(c, s, x, 640, 56, "g", TINTA, a))
        if t >= C["s01.d"]:
            for x in xs:
                F.seta(c, x, 680, 960 + (x - 960) * 0.3, 760, TINTA2, ep(t, C["s01.d"], 0.4), 6)
        E.foco(c, t, C["s01.e"], 0.5, lambda a: (turbina(c, 860, 900, 80, (t - C["s01.e"]) * 160, a), F.seta(c, 960, 900, 1040, 900, TINTA2, a, 6),
                                                 gerador(c, 1150, 900, 90, (t - C["s01.e"]) * 160, a)))
        E.frase(c, t, C["s01.e"], ps("um eixo girando", "i", 56, TINTA2), 1300, 920, passo=0.1)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate((("s02.a", "o caminho da energia", 1.2), ("s02.b", "a potência da queda", 0))):
        y = 470 + i * 170
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def far(a, x, y):
        E.formula(c, "ε = f{ΔΦ}{Δt}", x + 10, y + 30, 56, "g", TINTA, a, "center")

    def pot(a, x, y):
        E.formula(c, "P = f{E}{Δt}", x - 10, y + 10, 50, "g", TINTA, a, "center")
        E.formula(c, "η = f{útil}{total}", x - 10, y + 80, 40, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "Faraday:", "fluxo muda: corrente"), ("s03.c", "potência e rendimento:", "watt e útil/total")), (far, pot))


# ---------------- o gerador ----------------
def b_gerador(c, t, C, b):
    cx, cy, r = 1350, 560, 270
    ang = (t - C["s04"]) * 120 if t >= C["s04.a"] else 0
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("o", "i", 90), ("gerador", "g", 90, COR)], XE, 220)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: gerador(c, cx, cy, r, ang, a))
        E.frase(c, t, C["s04.a"], ps("ímã girando em", "i", 60) + [("bobinas", "g", 60, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("o fluxo muda", "i", 60) + [("o tempo todo", "g", 60)], XE, 500, passo=0.12)
        E.frase(c, t, C["s04.c"], [("Faraday:", "g", 60, COR), ("corrente", "i", 64)], XE, 620, passo=0.12)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "corrente alternada", XE + 250, 780, 54, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s05.a"], ps("o motor", "i", 80) + [("ao contrário", "g", 80, COR)], XE, 220, passo=0.12)
    gerador(c, cx + 150, cy, 200, ang)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.pilula(c, "motor", XE + 120, 420, 50, "g", fundo=TINTA, a=a), E.escreve(c, "corrente → giro", XE + 270, 435, 54, "b", TINTA, a)))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: (E.pilula(c, "gerador", XE + 140, 540, 50, "g", fundo=E.COR, a=a), E.escreve(c, "giro → corrente", XE + 300, 555, 54, "b", TINTA, a)))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: (turbina(c, 1060, 560, 120, ang * 1.0, a), M.line(c, 1180, 560, 1300, 560, TINTA, a, 10)))
    E.frase(c, t, C["s05.d"], ps("toda usina dessas precisa de", "i", 56), XE, 800, passo=0.1)
    E.frase(c, t, C["s05.e"], [("uma turbina:", "g", 60, COR), ("roda com pás", "i", 64)], XE, 900, passo=0.12)


# ---------------- hidrelétrica ----------------
def b_hidro(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("hidrelétrica:", "g", 76, COR), ("a água empurra", "i", 80)], XE, 200, passo=0.12)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: represa(c, 300, 360, a))
    if t >= C["s06.c"]:
        q = ((t - C["s06.c"]) * 1.2) % 1
        for k in range(3):
            f = (q + k / 3) % 1
            c.drawCircle(lerp(540, 800, f), lerp(590, 750, f), 12, M.paint(BR, 0.9))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: turbina(c, 880, 790, 90, (t - C["s06.d"]) * 200, a))
    E.foco(c, t, C["s06.e"], 0.5, lambda a: (M.line(c, 970, 790, 1060, 790, TINTA, a, 10), gerador(c, 1160, 790, 100, (t - C["s06.d"]) * 200, a)))
    cadeia(c, t, [(C["s06.b"], "potencial"), (C["s06.c"], "cinética"), (C["s06.d"], "giro da turbina"), (C["s06.e"], "elétrica")], 300, 1000, gap=50, size=44)


# ---------------- termelétrica ----------------
def chama(c, cx, cy, s, a, t):
    for k in range(3):
        h = s * (1 + 0.15 * math.sin(t * 9 + k))
        p = skia.Path(); x = cx + (k - 1) * s * 0.5
        p.moveTo(x - s * 0.3, cy); p.quadTo(x - s * 0.3, cy - h * 0.6, x, cy - h); p.quadTo(x + s * 0.3, cy - h * 0.6, x + s * 0.3, cy); p.close()
        c.drawPath(p, M.paint(E.COR if k != 1 else "#FFB020", a))


def b_termo(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("termelétrica:", "g", 76, COR), ("o vapor empurra", "i", 80)], XE, 200, passo=0.12)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: chama(c, 400, 780, 110, a, t))
        E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: centro(c, "carvão, gás, bagaço", 400, 850, 44, "i", TINTA2, a))
        E.foco(c, t, C["s07.c"], 0.5, lambda a: (M.rrect(c, 300, 500, 200, 170, 20, "#D9D6CF", a), c.drawRect(skia.Rect.MakeXYWH(300, 580, 200, 90), M.paint(AGUA, a))))
        if t >= C["s07.d"]:
            q = ((t - C["s07.d"]) * 1.4) % 1
            for k in range(4):
                f = (q + k / 4) % 1
                c.drawCircle(lerp(500, 820, f), lerp(540, 560, f), 16, M.paint("#CFCBC2", 0.9))
            turbina(c, 900, 560, 90, (t - C["s07.d"]) * 200, 1)
            M.line(c, 990, 560, 1090, 560, TINTA, 1, 10)
            gerador(c, 1190, 560, 100, (t - C["s07.d"]) * 200, 1)
        E.foco(c, t, C["s07.e"], 0.5, lambda a: E.pilula(c, "o vapor esfria e volta", 900, 760, 46, "g", fundo=TINTA, a=a))
        cadeia(c, t, [(C["s07.b"], "química"), (C["s07.b"] + 1.0, "calor"), (C["s07.d"], "giro da turbina"), (C["s07.d"] + 1.0, "elétrica")], 300, 1000, size=44)
        return
    E.frase(c, t, C["s08.a"], ps("uma", "i", 80) + [("máquina térmica", "g", 80, COR)], XE, 240, passo=0.12)
    E.frase(c, t, C["s08.b"], ps("segunda lei: nem todo calor vira", "i", 60) + [("trabalho", "g", 60)], XE, 400, passo=0.1)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: (E.pilula(c, "calor", 480, 620, 56, "g", fundo=E.COR, a=a), F.seta(c, 600, 600, 860, 600, TINTA2, a, 8),
                                             E.pilula(c, "trabalho", 1000, 620, 56, "g", fundo=TINTA, a=a), F.seta(c, 720, 620, 860, 760, TINTA2, a, 8),
                                             E.pilula(c, "sai para o ambiente", 1060, 800, 50, "g", fundo="#B9B3A6", a=a)))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "rendimento bem abaixo de 100%", W / 2, 960, 56, "g", fundo=TINTA, a=a))


# ---------------- nuclear ----------------
def b_nuclear(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("e a", "i", 84) + [("nuclear?", "g", 84, COR)], XE, 220, passo=0.12)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "é uma termelétrica", XE + 280, 360, 60, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: (M.rrect(c, 300, 500, 220, 200, 30, "#D9D6CF", a), E.formula(c, "reator", 410, 620, 50, "g", TINTA, a, "center")))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.escreve(c, "só aquece a água", 280, 760, 52, "i", TINTA2, a))
    if t >= C["s09.e"]:
        turbina(c, 900, 600, 90, (t - C["s09.e"]) * 200, ep(t, C["s09.e"], 0.4))
        M.line(c, 990, 600, 1090, 600, TINTA, ep(t, C["s09.e"], 0.4), 10)
        gerador(c, 1190, 600, 100, (t - C["s09.e"]) * 200, ep(t, C["s09.e"], 0.4))
    cadeia(c, t, [(C["s09.c"], "calor do reator"), (C["s09.e"], "vapor"), (C["s09.e"] + 0.6, "turbina"), (C["s09.e"] + 1.2, "elétrica")], 300, 900, size=44)
    E.foco(c, t, C["s09.f"], 0.5, lambda a: E.pilula(c, "como o reator faz calor: aula de fissão", W / 2, 1010, 44, "g", fundo=TINTA2, a=a))


# ---------------- potência da queda ----------------
def b_queda(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("potência", "g", 80, COR), ("da queda d'água", "i", 84)], XE, 220, passo=0.12)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "E = m · g · h", XE, 420, 100, "g", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "massa por segundo = d · Z", XE, 600, 80, "g", TINTA, a))
        E.foco(c, t, C["s10.c"] + 1.0, 0.4, lambda a: E.escreve(c, "Z: vazão, o volume por segundo", XE, 700, 52, "b", TINTA2, a))
        E.foco(c, t, C["s10.a"], 0.5, lambda a: represa(c, 1400, 360, a))
        E.foco(c, t, C["s10.b"], 0.4, lambda a: (M.line(c, 1370, 360, 1370, 760, TINTA2, a, 4, dash=E.TRACO), E.escreve(c, "h", 1320, 580, 60, "g", COR, a)))
        return
    if t < C["s12"]:
        F.formula_legenda(c, t, C["s11.a"], "P = d · Z · g · h", [("d", "densidade da água", "kg/m^3"), ("Z", "vazão", "m^3/s"),
                                                                  ("g", "gravidade", "m/s^2"), ("h", "altura da queda", "m")],
                          XE, 320, 140, tl=[C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]])
        E.foco(c, t, C["s11.f"], 0.5, lambda a: E.pilula(c, "P em watt (W)", 1450, 360, 60, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s11.b"] + 0.6, 0.4, lambda a: E.escreve(c, "água: 1.000 kg/m³", 1250, 560, 52, "b", TINTA, a))
        E.foco(c, t, C["s11.d"] + 0.6, 0.4, lambda a: E.escreve(c, "g = 10 m/s²", 1250, 650, 52, "b", TINTA, a))
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "Z = 100 m^3/s,   h = 50 m", XE, 230, 66, "g", TINTA, a))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "P = 1.000 · 100 · 10 · 50", XE, 400, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "= 50.000.000 W = 50 MW", XE, 540, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "rendimento 90%:  0,9 × 50", XE, 720, 70, "g", TINTA2, a))
    bola_txt(c, t, C["s12.e"], "45 MW", 1500, 760, 170, 80)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("eletricidade", "i", 64) + [("direto do átomo?", "g", 64, ERRADO)], XE, 330, passo=0.12)
    if t >= C["s13.a"] + 1.0:
        E.risco(c, XE + 330, 350, XE + 900, 290, t, C["s13.a"] + 1.0, largura=10)
    E.frase(c, t, C["s13.b"], ps("o núcleo do átomo só dá", "i", 64) + [("calor", "g", 64, COR)], XE, 480, passo=0.12)
    cadeia(c, t, [(C["s13.c"], "calor"), (C["s13.d"], "vapor"), (C["s13.d"] + 0.4, "turbina"), (C["s13.d"] + 0.8, "gerador")], XE, 680, size=52)
    E.frase(c, t, C["s13.e"], ps("quase igual à", "i", 60) + [("termelétrica a carvão", "g", 60, COR)], XE, 880, passo=0.12)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        E.formula_em(c, t, C["s14.a"], "d · g = 1.000 · 10", W / 2, 360, 100, "g", BR, "center")
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "10.000", W / 2, 480, 70, "g", fundo=E.COR, a=a))
        E.formula_em(c, t, C["s14.c"], "P = 10.000 · Z · h", W / 2, 680, 120, "g", E.CLARO, "center")
        E.formula_em(c, t, C["s14.d"], "10.000 · 100 · 50 = 50.000.000 W", W / 2, 880, 70, "g", BR, "center")
        return
    E.frase(c, t, C["s15.a"], [("d · g", "g", 70, BR), ("é sempre o mesmo para a", "i", 70, CLARO), ("água", "g", 70, BR)], W / 2, 330, "center", 0.12)
    E.frase(c, t, C["s15.b"], [("não serve:", "g", 64, ERRADO), ("g = 9,8", "g", 64, BR)], W / 2, 560, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("ou", "i", 64, CLARO) + [("outro líquido", "g", 64, BR)], W / 2, 700, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "Z = 20 m^3/s,   h = 30 m", XE, 380, 76, "g", TINTA, a))
        E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "rendimento: 90%", XE, 520, 76, "g", TINTA, a))
        E.frase(c, t, C["s16.c"], [("potência elétrica = ?", "g", 76, COR)], XE, 700)
        E.foco(c, t, C["s16.a"], 0.5, lambda a: represa(c, 1300, 380, a))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=500, r=200)
        E.foco(c, t, C["s17"], 0.4, lambda a: E.formula(c, "Z = 20 m^3/s,  h = 30 m", XE, 420, 60, "g", TINTA, a))
        E.foco(c, t, C["s17"] + 0.2, 0.4, lambda a: E.formula(c, "90%:  P = ?", XE, 540, 60, "g", COR, a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "20 · 30 = 600", XE, 280, 90, "g", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "10.000 · 600", XE, 460, 90, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "= 6.000.000 W = 6 MW", XE, 620, 80, "g", TINTA, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "0,9 × 6", XE, 800, 80, "g", TINTA2, a))
    bola_txt(c, t, C["s18.e"], "5,4 MW", 1480, 640, 190, 80)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("turbina", "g", 70), ("presa a um gerador", "i", 74)]),
                 ("s19.b", [("nuclear:", "g", 70), ("uma termelétrica", "i", 74)]),
                 ("s19.c", None))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            if partes:
                E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
            else:
                E.formula_em(c, t, C[k] + 0.1, "P = d · Z · g · h", 400, y, 74, "g", TINTA)
        E.frase(c, t, C["s19.d"], ps("próxima aula:", "i", 60, TINTA2) + [("o vento e o sol", "g", 60, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s20.a"] + 0.2, 0.4))
    E.frase(c, t, C["s20.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, gerador=b_gerador, hidro=b_hidro, termo=b_termo, nuclear=b_nuclear, queda=b_queda,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
