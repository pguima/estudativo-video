"""Visual — Estudativo · FIS-MAG-010: vento e sol, rendimento e intermitência. Linguagem visual do Magnetismo e das usinas: veja
o visual.py da FIS-MAG-001 e da FIS-MAG-009. Rendimento em colunas (E.colunas); controlável = selo verde, intermitente = selo
vermelho. Sol amarelo, painel azul-escuro, água azul clara. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-010_vento_e_sol_rendimento_e_intermitencia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("eolica", "solar", "rendimento", "intermitencia", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
AGUA = "#7FC8E8"
SOL = "#FFB020"
PAINEL = "#22416E"

# todas as contas da aula (valores típicos, aproximados)
assert 0.20 * 1000 == 200 and 10 * 1000 == 10_000 and 0.20 * 10_000 == 2000
RENDIMENTO = [("hídrica", 90), ("térmica", 40), ("nuclear", 33), ("eólica", 45), ("solar", 20)]  # % aproximado
assert max(RENDIMENTO, key=lambda r: r[1])[0] == "hídrica" and min(RENDIMENTO, key=lambda r: r[1])[0] == "solar"


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


def sol(c, cx, cy, r, a=1.0, t=0.0):
    if a <= 0:
        return
    for k in range(10):
        g = math.radians(36 * k + t * 20)
        M.line(c, cx + r * 1.2 * math.cos(g), cy + r * 1.2 * math.sin(g), cx + r * 1.55 * math.cos(g), cy + r * 1.55 * math.sin(g), SOL, a, 8)
    E.bola(c, cx, cy, r, SOL, a)


def lua(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#C9C5BC", a))
    c.drawCircle(cx + r * 0.45, cy - r * 0.2, r * 0.9, M.paint(E.PAPEL, a))


def painel(c, cx, cy, w, h, a=1.0):
    """painel solar em perspectiva leve"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - w / 2, cy + h / 2); p.lineTo(cx + w / 2, cy + h / 2); p.lineTo(cx + w / 2 - w * 0.12, cy - h / 2); p.lineTo(cx - w / 2 + w * 0.12, cy - h / 2); p.close()
    c.drawPath(p, M.paint(PAINEL, a))
    for k in range(1, 4):
        f = k / 4
        M.line(c, lerp(cx - w / 2, cx - w / 2 + w * 0.12, 0) + w * f, cy + h / 2, cx - w / 2 + w * 0.12 + (w - w * 0.24) * f, cy - h / 2, "#6F8DB8", a, 3)
    for k in range(1, 3):
        f = k / 3
        y = lerp(cy + h / 2, cy - h / 2, f)
        M.line(c, cx - w / 2 + w * 0.12 * f, y, cx + w / 2 - w * 0.12 * f, y, "#6F8DB8", a, 3)
    M.line(c, cx, cy + h / 2, cx, cy + h / 2 + h * 0.5, TINTA2, a, 8)


def eolica(c, cx, cy, s, ang, a=1.0):
    """aerogerador: torre e três pás girando"""
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(cx - s * 0.06, cy + s * 1.6); p.lineTo(cx + s * 0.06, cy + s * 1.6); p.lineTo(cx + s * 0.03, cy); p.lineTo(cx - s * 0.03, cy); p.close()
    c.drawPath(p, M.paint("#D9D6CF", a)); c.drawPath(p, M.paint(TINTA2, a, stroke=3))
    for k in range(3):
        g = math.radians(ang + 120 * k)
        c.save(); c.translate(cx, cy); c.rotate(math.degrees(g))
        pp = skia.Path(); pp.moveTo(0, -s * 0.05); pp.quadTo(s * 0.5, -s * 0.12, s, 0); pp.quadTo(s * 0.5, s * 0.04, 0, s * 0.05); pp.close()
        c.drawPath(pp, M.paint(BR, a)); c.drawPath(pp, M.paint(TINTA, a, stroke=4))
        c.restore()
    c.drawCircle(cx, cy, s * 0.07, M.paint(E.COR, a))


def represa(c, x, y, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y, 220, 240, 6, AGUA, a)
    p = skia.Path(); p.moveTo(x + 220, y - 20); p.lineTo(x + 280, y - 20); p.lineTo(x + 340, y + 240); p.lineTo(x + 220, y + 240); p.close()
    c.drawPath(p, M.paint("#B9B3A6", a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        E.foco(c, t, C["s01.a"], 0.5, lambda a: (sol(c, 520, 330, 80, a, t), painel(c, 520, 600, 380, 160, a)))
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: E.pilula(c, "meio-dia: gera", 520, 860, 50, "g", fundo=CERTO, a=a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (lua(c, 1060, 330, 70, a), painel(c, 1060, 600, 380, 160, a)))
        E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.pilula(c, "meia-noite: zero", 1060, 860, 50, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (lua(c, 1600, 330, 70, a), represa(c, 1440, 520, a)))
        E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: E.pilula(c, "3 da manhã: gera", 1600, 860, 50, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s01.d"], ps("essa diferença", "i", 64) + [("cai na prova", "g", 64, COR)], W / 2, 1000, "center", 0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("cinco fontes, duas coisas", "i", 80), XE, 280, passo=0.14)
    for i, (k, s) in enumerate((("s02.b", "rendimento"), ("s02.c", "intermitência"))):
        y = 470 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def ren(a, x, y):
        E.formula(c, "η = f{útil}{entrou}", x - 10, y + 30, 54, "g", TINTA, a, "center")

    def tur(a, x, y):
        for k in range(8):
            g = math.radians(45 * k)
            M.line(c, x - 60, y, x - 60 + 60 * math.cos(g), y + 60 * math.sin(g), TINTA, a, 5)
        M.line(c, x, y, x + 60, y, TINTA, a, 6)
        c.drawCircle(x + 110, y, 50, M.paint(TINTA, a, stroke=5))
    lembrete2(c, t, C, "s03", (("s03.b", "rendimento:", "útil dividido pelo total"), ("s03.c", "usinas:", "turbina e gerador")), (ren, tur))


# ---------------- eólica ----------------
def b_eolica(c, t, C, b):
    ang = (t - C["s04"]) * 90
    E.foco(c, t, C["s04"], 0.5, lambda a: eolica(c, 1400, 380, 300, ang, a))
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("usina", "i", 90), ("eólica", "g", 90, COR)], XE, 220)
        for k in range(4):
            x = 700 + ((t - C["s04.a"]) * 260 + k * 160) % 500
            if t >= C["s04.a"]:
                F.seta(c, x, 300 + k * 60, x + 90, 300 + k * 60, "#7FB7D6", 0.8, 5, 18)
        E.frase(c, t, C["s04.a"], ps("o vento empurra as pás", "i", 56), XE, 380, passo=0.1)
        E.frase(c, t, C["s04.b"], ps("as pás giram o eixo", "i", 56), XE, 470, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("o eixo gira o", "i", 56) + [("gerador", "g", 56, COR)], XE, 560, passo=0.1)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "entra: energia cinética do ar", XE + 330, 720, 50, "g", fundo=TINTA, a=a))
        return
    E.frase(c, t, C["s05.a"], ps("não tira", "i", 76) + [("toda", "g", 76, COR)] + ps("a energia", "i", 76), XE, 220, passo=0.12)
    E.frase(c, t, C["s05.b"], ps("se tirasse, o ar", "i", 56) + [("pararia", "g", 56)] + ps("atrás das pás", "i", 56), XE, 380, passo=0.1)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "no máximo, cerca de metade", XE + 330, 560, 56, "g", fundo=E.COR, a=a))


# ---------------- solar ----------------
def b_solar(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("painel solar:", "g", 76, COR), ("diferente", "i", 80)], XE, 220, passo=0.12)
        E.foco(c, t, C["s06.a"], 0.5, lambda a: (sol(c, 1550, 280, 80, a, t), painel(c, 1400, 620, 500, 220, a)))
        if t >= C["s06.b"]:
            for k in range(4):
                f = ((t - C["s06.b"]) * 0.8 + k / 4) % 1
                M.line(c, lerp(1500, 1380, f), lerp(380, 560, f), lerp(1500, 1380, f) - 20, lerp(380, 560, f) + 30, SOL, 0.9, 6)
        E.frase(c, t, C["s06.b"], ps("luz vira eletricidade", "i", 60) + [("direto", "g", 60, COR)], XE, 380, passo=0.12)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "sem turbina, sem gerador", XE + 300, 520, 52, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: E.pilula(c, "rendimento: cerca de 20%", XE + 300, 660, 56, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s07"], ps("um exemplo", "i", 76), XE, 220, passo=0.12)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.formula(c, "sol forte: 1.000 W por m^2", XE, 420, 76, "g", TINTA, a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "1 m^2 de painel,  20%", XE, 580, 76, "g", TINTA, a))
    E.foco(c, t, C["s07.b"] + 1.0, 0.5, lambda a: E.formula(c, "0,20 × 1.000", XE, 740, 76, "g", TINTA2, a))
    bola_txt(c, t, C["s07.c"], "200 W", 1500, 620, 170, 80)


# ---------------- rendimento ----------------
def b_rendimento(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], ps("compare o", "i", 76) + [("rendimento", "g", 76, COR)], XE, 200, passo=0.12)
        rot = [("hídrica", "≈ 90%"), ("térmica", "⅓ a ½"), ("nuclear", "≈ ⅓"), ("eólica", "até ≈ ½"), ("solar", "≈ 20%")]
        vals = [90, 45, 33, 45, 20]
        ks = ("s08.a", "s08.b", "s08.c", "s08.d", "s08.e")
        x0, yb, wcol, hmax = 300, 900, 200, 560
        M.line(c, x0 - 40, yb, x0 + 5 * 280, yb, TINTA, 1, 4)
        for i in range(5):
            x = x0 + i * 280
            q = ease_out(prog(t, C[ks[i]], 0.6))
            if q > 0:
                h = hmax * vals[i] / 100 * q
                M.rrect(c, x, yb - h, wcol, h, 8, E.COR if i == 0 else (SOL if i == 4 else TINTA2), 1)
                E.foco(c, t, C[ks[i]] + 0.3, 0.4, lambda a, i=i, x=x, h=h: (centro(c, rot[i][1], x + wcol / 2, yb - h - 24, 52, "g", TINTA, a)))
            E.foco(c, t, C[ks[i]], 0.4, lambda a, i=i, x=x: centro(c, rot[i][0], x + wcol / 2, yb + 60, 50, "g", TINTA, a))
        return
    E.frase(c, t, C["s09.a"], [("rendimento baixo", "g", 76), ("≠", "g", 76, ERRADO), ("fonte ruim", "g", 76)], XE, 260, passo=0.14)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (sol(c, 500, 560, 90, a, t), eolica(c, 900, 470, 160, (t - C["s09.b"]) * 90, a)))
    E.frase(c, t, C["s09.b"], ps("sol e vento chegam", "i", 60) + [("de graça", "g", 60, CERTO)], 1100, 520, passo=0.12)
    E.frase(c, t, C["s09.c"], ps("e", "i", 60) + [("não queimam nada", "g", 60, CERTO)], 1100, 640, passo=0.12)
    E.frase(c, t, C["s09.d"], ps("o problema", "i", 70) + [("é outro", "g", 70, COR)], XE, 920, passo=0.12)


# ---------------- intermitência ----------------
def b_intermitencia(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("intermitência:", "g", 80, COR)], XE, 220)
        E.frase(c, t, C["s10.a"] + 0.6, ps("liga e desliga sozinha", "i", 64), XE, 320, passo=0.12)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: (lua(c, 600, 520, 60, a), painel(c, 600, 720, 300, 130, a), E.pilula(c, "noite: zero", 600, 930, 48, "g", fundo=ERRADO, a=a)))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: (eolica(c, 1200, 560, 170, 0, a), E.pilula(c, "sem vento: para", 1200, 930, 48, "g", fundo=ERRADO, a=a)))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "ninguém escolhe a hora", 1600, 420, 50, "g", fundo=TINTA, a=a))
        return
    E.frase(c, t, C["s11"], ps("e as", "i", 76) + [("controláveis", "g", 76, COR)], XE, 200, passo=0.12)
    linhas = (("s11.a", "térmica e nuclear", "geram dia e noite"), ("s11.b", "hidrelétrica", "depende da chuva, mas"),
              ("s11.c", "a represa guarda água", "gera quando precisar"))
    for i, (k, l1, l2) in enumerate(linhas):
        y = 380 + i * 150
        E.foco(c, t, C[k], 0.4, lambda a, y=y: E.selo(c, XE + 40, y - 20, 36, True, a))
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 60), (l2, "i", 62, TINTA2)], XE + 110, y, passo=0.12)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "hidrelétrica: parceira do sol e do vento", W / 2, 900, 56, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], [("renovável", "g", 64), ("=", "g", 64, ERRADO), ("gera o tempo todo?", "i", 66)], XE, 330, passo=0.12)
    E.frase(c, t, C["s12.b"], [("renovável:", "g", 60, COR), ("não acaba", "i", 64)], XE, 480, passo=0.12)
    E.frase(c, t, C["s12.c"], [("intermitente:", "g", 60, COR), ("não dá para controlar", "i", 64)], XE, 590, passo=0.12)
    for i, (k, nome, s2) in enumerate((("s12.d", "hidrelétrica", "renovável e controlável"), ("s12.e", "solar", "renovável e intermitente"))):
        y = 760 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y, nome=nome, s2=s2: (E.pilula(c, nome, XE + 170, y - 20, 50, "g", fundo=TINTA, a=a),
                                                                         E.escreve(c, s2, XE + 400, y, 56, "b", CERTO if i == 0 else ERRADO, a)))


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("agora, o atalho:", "i", 76, CLARO) + [("duas perguntas", "g", 76, BR)], W / 2, 170, "center", 0.12)
        cols = ("gira gerador?", "liga quando quero?")
        fontes = (("hídrica", True, True), ("térmica", True, True), ("nuclear", True, True), ("eólica", True, False), ("solar", False, False))
        E.foco(c, t, C["s13.b"], 0.4, lambda a: centro(c, cols[0], 1050, 330, 50, "g", BR, a))
        E.foco(c, t, C["s13.c"], 0.4, lambda a: centro(c, cols[1], 1500, 330, 50, "g", BR, a))
        for i, (nome, g, ctrl) in enumerate(fontes):
            y = 440 + i * 115
            E.foco(c, t, C["s13.a"] + 0.15 * i, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, 420, y + 14, 56, "g", E.CLARO, a))
            E.foco(c, t, C["s13.b"] + 0.3 + 0.1 * i, 0.4, lambda a, g=g, y=y: E.selo(c, 1050, y, 36, g, a))
            E.foco(c, t, C["s13.c"] + 0.3 + 0.1 * i, 0.4, lambda a, ctrl=ctrl, y=y: E.selo(c, 1500, y, 36, ctrl, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "intermitentes: eólica e solar", W / 2, 1010, 50, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s14.a"], ps("a questão pede a noite ou o pico?", "i", 64, CLARO), W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "procure uma controlável", W / 2, 400, 64, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s14.c"], ps("pede menos gás carbônico?", "i", 64, CLARO), W / 2, 620, "center", 0.1)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "sem queima: hídrica, eólica, solar, nuclear", W / 2, 760, 54, "g", fundo="#3A3A48", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "10 m^2 de painel,  20%", XE, 330, 70, "g", TINTA, a))
        E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "1.000 W por m^2", XE, 450, 70, "g", TINTA, a))
        E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "ao meio-dia: P = ?", XE, 600, 70, "g", COR, a))
        E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "à meia-noite: P = ?", XE, 710, 70, "g", COR, a))
        E.frase(c, t, C["s15.e"], ps("noite:", "i", 60) + [("eólica ou hidrelétrica?", "g", 60, COR)], XE, 860, passo=0.12)
        E.foco(c, t, C["s15.a"], 0.5, lambda a: (sol(c, 1600, 300, 70, a, t), painel(c, 1500, 600, 420, 180, a)))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=500, r=200)
        E.foco(c, t, C["s16"], 0.4, lambda a: E.formula(c, "10 m^2,  20%,  1.000 W/m^2", XE, 400, 56, "g", TINTA, a))
        E.frase(c, t, C["s16"] + 0.3, [("meio-dia?", "g", 60, COR), ("meia-noite?", "g", 60, COR)], XE, 520, passo=0.12)
        E.frase(c, t, C["s16"] + 0.6, [("a noite com quem?", "g", 60)], XE, 640)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "10 × 1.000", XE, 300, 90, "g", TINTA, a))
        E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "= 10.000 W de luz", XE + 500, 300, 80, "g", TINTA2, a))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "0,20 × 10.000", XE, 500, 90, "g", TINTA, a))
        bola_txt(c, t, C["s17.d"], "2.000 W", 1450, 560, 180, 76)
        E.foco(c, t, C["s17.e"], 0.5, lambda a: (lua(c, XE + 80, 760, 50, a), E.formula(c, "meia-noite:  0 W", XE + 180, 790, 80, "g", ERRADO, a)))
        return
    E.frase(c, t, C["s18.a"], ps("a noite fica com a", "i", 76) + [("hidrelétrica", "g", 76, COR)], XE, 240, passo=0.12)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: (represa(c, 600, 460, a), lua(c, 1000, 400, 60, a)))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.pilula(c, "a represa guarda a água", 760, 820, 52, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: (eolica(c, 1450, 460, 170, 0, a), E.pilula(c, "eólica: só se ventar", 1450, 820, 52, "g", fundo=TINTA, a=a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("hidrelétrica:", "g", 70), ("maior rendimento", "i", 74)]),
                 ("s19.b", [("sol:", "g", 70), ("o menor, mas de graça", "i", 74)]),
                 ("s19.c", [("vento e sol:", "g", 70), ("intermitentes", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
        E.frase(c, t, C["s19.d"], ps("próxima aula:", "i", 60, TINTA2) + [("questões de usinas", "g", 60, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s20.a"] + 0.2, 0.4))
    E.frase(c, t, C["s20.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, eolica=b_eolica, solar=b_solar, rendimento=b_rendimento, intermitencia=b_intermitencia,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
