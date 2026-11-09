"""Visual — Estudativo · FIS-MAG-008: praticando magnetismo e indução. Linguagem visual do Magnetismo: veja o visual.py da
FIS-MAG-001. Cada questão: enunciado à esquerda com um desenho pequeno à direita; na pausa, o relógio ocupa o desenho; na
resolução, uma linha por passo e a resposta na esfera. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-008_praticando_magnetismo_e_inducao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
VEL = F.VEL

# todas as contas da aula
assert math.isclose(2e-7 * 5 / 0.1, 1e-5) and math.isclose(2e-7 * 20 / 0.2, 2e-5) and 20 / 5 == 4 and 4 / 2 == 2
assert math.isclose(5e-6 * 2e3, 1e-2) and math.isclose(5e-6 * 2e3 * 0.6, 6e-3)
assert math.isclose(0.4 * 5, 2) and math.isclose(2 * 0.5, 1) and math.isclose(0.4 * 5 * 0.5 * math.sin(math.radians(30)), 0.5)
assert math.isclose(0.03 - 0.01, 0.02) and math.isclose(0.02 / 0.5, 0.04) and math.isclose(50 * 0.04, 2)
assert 220 / 11 == 20 and 400 / 20 == 20 and math.isclose(2 / 20, 0.1)
cruz = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
assert cruz((1, 0, 0), (0, 0, 1)) == (0, -1, 0)  # questão 2: v para a direita, B saindo → força para baixo
CASOS = {("N", False): "S"}
assert CASOS[("N", False)] == "S"  # questão 4: norte saindo → atrai → face sul → horário


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def simbolo_campo(c, cx, cy, r, sai=True, a=1.0, cor=None):
    if a <= 0:
        return
    cor = cor or TINTA
    c.drawCircle(cx, cy, r, M.paint(cor, a, stroke=max(3, r * 0.14)))
    if sai:
        c.drawCircle(cx, cy, r * 0.28, M.paint(cor, a))
    else:
        k = r * 0.62
        M.line(c, cx - k, cy - k, cx + k, cy + k, cor, a, max(3, r * 0.14))
        M.line(c, cx - k, cy + k, cx + k, cy - k, cor, a, max(3, r * 0.14))


def folha(c, x0, y0, cols, lins, passo, sai, r, a, cor=TINTA2):
    for i in range(lins):
        for j in range(cols):
            simbolo_campo(c, x0 + j * passo, y0 + i * passo, r, sai, a, cor)


def barra(c, cx, cy, w=360, h=110, a=1.0, ang=0.0):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-ang)
    for lado, cor in ((1, E.COR), (-1, NEG)):
        x0 = 0 if lado > 0 else -w / 2
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, -h / 2, w / 2, h), 10, 10), M.paint(cor, a))
    c.restore()
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    sz = min(h, w / 2) * 0.55
    E._meio(c, "N", cx + ux * w / 4, cy + uy * w / 4, sz, "g", BR, a)
    E._meio(c, "S", cx - ux * w / 4, cy - uy * w / 4, sz, "g", BR, a)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def enunciado(c, t, C, cena, n, linhas, desenho, pausa):
    """enunciado da questão n: linhas = [(instante, texto em fórmula)]; desenho(a) à direita até a pausa, depois o relógio"""
    E.frase(c, t, C[cena], [("questão", "i", 70, COR), (str(n), "g", 70, COR)], XE, 180, passo=0.12)
    for i, (ti, s) in enumerate(linhas):
        E.foco(c, t, ti, 0.5, lambda a, i=i, s=s: E.formula(c, s, XE, 330 + 110 * i, 60, "g", TINTA, a))
    if t < pausa:
        E.foco(c, t, linhas[0][0], 0.5, desenho)
    else:
        E.relogio(c, t, pausa, cx=1500, cy=480, r=190)


def passos(c, t, itens, x=XE, y0=260, dy=130, size=72):
    """resolução: uma linha por passo, [(instante, fórmula, cor)]"""
    for i, it in enumerate(itens):
        ti, s = it[0], it[1]
        cor = it[2] if len(it) > 2 else TINTA
        E.foco(c, t, ti, 0.5, lambda a, i=i, s=s, cor=cor: E.formula(c, s, x, y0 + dy * i, size, "g", cor, a))


def lembrete_itens(c, t, C):
    E.frase(c, t, C["s02"], ps("as aulas do módulo", "i", 80), XE, 220, passo=0.12)
    for i, (k, s) in enumerate((("s02.a", "campo da corrente"), ("s02.b", "força magnética"), ("s02.c", "Faraday e Lenz"), ("s02.d", "transformador"))):
        y = 400 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 36, a=a), centro(c, str(i + 1), XE + 40, y - 6, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 66)], XE + 110, y)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.5), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54), XE, 960, passo=0.1)


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], ps("fórmulas", "i", 80) + [("parecidas", "g", 80, COR)], XE, 260, passo=0.12)
    for i, s in enumerate(("B = 2·10^{−7}·f{i}{d}", "F = q·v·B·sen θ", "F = B·i·L·sen θ", "ε = f{ΔΦ}{Δt}", "f{U₁}{U₂} = f{N₁}{N₂}")):
        x, y = 1150 + (i % 2) * 380, 300 + i * 120
        E.foco(c, t, C["s01.a"] + 0.3 * i, 0.4, lambda a, s=s, x=x, y=y: E.formula(c, s, x, y, 56, "g", TINTA2, a))
    E.frase(c, t, C["s01.b"], ps("o difícil:", "i", 70) + [("qual usar", "g", 70, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s01.c"], [("5 questões", "g", 70), ("de tudo", "i", 74)], XE, 620, passo=0.12)
    E.frase(c, t, C["s01.d"], ps("reconhecer em", "i", 64) + [("segundos", "g", 64, COR)], XE, 760, passo=0.12)


def b_lembrete(c, t, C, b):
    lembrete_itens(c, t, C)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s03"], ps("o método:", "i", 76, CLARO) + [("três perguntas", "g", 76, BR)], W / 2, 170, "center", 0.12)
    linhas = (("s03.a", "corrente criando campo?", "fio, espira, bobina: mão que segura"),
              ("s03.b", "alguém sente força?", "carga: q·v·B   fio: B·i·L   mão do tapa"),
              ("s04.a", "o fluxo está mudando?", "Faraday, com o sentido de Lenz"),
              ("s04.b", "duas bobinas num ferro?", "transformador"))
    for i, (k, q, r) in enumerate(linhas):
        y = 340 + i * 175
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 22, 40, a=a), centro(c, str(i + 1) if i < 3 else "+", 230, y - 2, 46, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(q, "g", 58, BR)], 300, y)
        E.frase(c, t, C[k] + 0.6, [(r, "b", 46, CLARO)], 300, y + 66)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    def fio(a):
        M.line(c, 1450, 260, 1450, 900, TINTA, a, 8)
        F.corrente(c, t, C["s05.a"], [(1450, 900), (1450, 260)], fecha=False, a=a)
        M.line(c, 1450, 520, 1650, 520, TINTA2, a, 4, dash=E.TRACO)
        c.drawCircle(1650, 520, 12, M.paint(TINTA, a))
        centro(c, "10 cm", 1550, 490, 44, "g", TINTA, a)
    if t < C["s06"]:
        enunciado(c, t, C, "s05", 1, [(C["s05.a"], "i = 5 A,  d = 10 cm"), (C["s05.a"] + 1.2, "B = 1 · 10^{−5} T"),
                                      (C["s05.b"], "d = 20 cm,  i = 20 A:  B = ?")], fio, C["s05.c"])
        return
    E.frase(c, t, C["s06"], [("fio:", "g", 64, COR), ("B proporcional a i/d", "i", 66)], XE, 200, passo=0.12)
    passos(c, t, [(C["s06.a"], "B = 2 · 10^{−7} · f{i}{d}"), (C["s06.b"], "i: 5 → 20   (× 4, em cima)"), (C["s06.c"], "d: 10 → 20   (× 2, embaixo)"),
                  (C["s06.d"], "f{4}{2} = 2:  o campo dobra", COR)], y0=360)
    bola_txt(c, t, C["s06.e"], "2 · 10^{−5} T", 1500, 820, 190, 60)


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    def cena(a, forca=False):
        folha(c, 1150, 330, 5, 4, 140, True, 22, a)
        F.carga(c, 99, 0, 1330, 540, 44, "+") if a > 0.99 else None
        F.seta(c, 1380, 540, 1580, 540, VEL, a, 10)
        E.escreve(c, "v", 1590, 510, 56, "g", VEL, a)
    if t < C["s08"]:
        enunciado(c, t, C, "s07", 2, [(C["s07.a"], "q = 5 · 10^{−6} C  (positiva)"), (C["s07.a"] + 1.5, "v = 2 · 10^{3} m/s,  para a direita"),
                                      (C["s07.b"], "B = 0,6 T,  saindo da folha"), (C["s07.c"], "F = ?  E o sentido?")], cena, C["s07.d"])
        return
    if t < C["s09"]:
        E.frase(c, t, C["s08"], [("carga andando:", "g", 64, COR)], XE, 200)
        passos(c, t, [(C["s08.a"], "F = q · v · B · sen θ"), (C["s08.b"], "θ = 90°,  sen θ = 1"),
                      (C["s08.c"], "5 · 10^{−6} · 2 · 10^{3} = 10^{−2}"), (C["s08.d"], "10^{−2} · 0,6")], y0=340)
        bola_txt(c, t, C["s08.d"] + 0.6, "6 · 10^{−3} N", 1500, 820, 200, 56)
        return
    E.frase(c, t, C["s09"], [("o sentido:", "g", 64, COR), ("a mão do tapa", "i", 66)], XE, 200, passo=0.12)
    folha(c, 1000, 330, 6, 4, 140, True, 22, 1)
    F.carga(c, 99, 0, 1300, 540, 44, "+")
    F.seta(c, 1350, 540, 1560, 540, VEL, ep(t, C["s09.a"], 0.4), 10)
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "polegar: v", XE + 160, 400, 46, "g", fundo=VEL, a=a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "dedos: B saindo", XE + 200, 520, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "palma: para baixo", XE + 210, 640, 46, "g", fundo=E.COR, a=a))
    F.vetor(c, t, C["s09.d"], (1300, 590), (1300, 860), "F", None, E.COR, 11, size=60)
    E.foco(c, t, C["s09.d"] + 0.4, 0.5, lambda a: E.pilula(c, "força para baixo", XE + 220, 820, 60, "g", fundo=CERTO, a=a))


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    def cena(a):
        for k in range(4):
            F.seta(c, 1150, 320 + k * 130, 1800, 320 + k * 130, TINTA2, a * 0.7, 4, 20)
        g = math.radians(30)
        M.line(c, 1470 - 260 * math.cos(g), 520 + 260 * math.sin(g), 1470 + 260 * math.cos(g), 520 - 260 * math.sin(g), TINTA, a, 10)
        E.escreve(c, "30°", 1600, 600, 52, "g", COR, a)
        E.escreve(c, "B", 1810, 300, 56, "g", TINTA, a)
    if t < C["s11"]:
        enunciado(c, t, C, "s10", 3, [(C["s10.a"], "L = 50 cm,  B = 0,4 T"), (C["s10.a"] + 1.8, "i = 5 A"),
                                      (C["s10.b"], "fio a 30° do campo"), (C["s10.c"], "F = ?")], cena, C["s10.d"])
        return
    E.frase(c, t, C["s11"], [("fio com corrente:", "g", 64, COR)], XE, 200)
    passos(c, t, [(C["s11.a"], "F = B · i · L · sen θ"), (C["s11.b"], "L = 0,5 m"), (C["s11.c"], "0,4 · 5 · 0,5 = 1"),
                  (C["s11.d"], "× sen 30° = × f{1}{2}")], y0=340)
    bola_txt(c, t, C["s11.e"], "0,5 N", 1500, 760, 170, 80)


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    def cena(a):
        q = min(1.0, max(0.0, t - C["s12.a"]) / 3)
        barra(c, lerp(1350, 1150, q), 540, 300, 90, a)
        for k in range(6):
            x = 1560 + k * 40
            c.drawOval(skia.Rect.MakeXYWH(x - 14, 400, 28, 280), M.paint(TINTA, a, stroke=6))
        E.escreve(c, "50 espiras", 1560, 760, 44, "i", TINTA2, a)
    if t < C["s13"]:
        enunciado(c, t, C, "s12", 4, [(C["s12.a"], "N do ímã se afasta;  50 espiras"), (C["s12.b"], "Φ: 0,03 → 0,01 Wb,  em 0,5 s"),
                                      (C["s12.c"], "ε = ?"), (C["s12.d"], "face do lado do ímã?")], cena, C["s12.e"])
        return
    E.frase(c, t, C["s13"], [("fluxo mudando:", "g", 64, COR), ("Faraday", "i", 66)], XE, 200, passo=0.12)
    passos(c, t, [(C["s13.a"], "ΔΦ = 0,02 Wb"), (C["s13.b"], "f{0,02}{0,5} = 0,04"), (C["s13.c"], "× 50 = 2 V", COR)], y0=340)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "Lenz: saiu, atrai", 1450, 360, 56, "g", fundo=TINTA, a=a))
    if t >= C["s13.e"]:
        q = ep(t, C["s13.e"], 0.4)
        c.drawCircle(1450, 640, 160, M.paint(TINTA, q, stroke=8))
        pts = [(1450 + 160 * math.cos(2 * math.pi * k / 36), 640 + 160 * math.sin(2 * math.pi * k / 36)) for k in range(36)]  # horário
        F.corrente(c, t, C["s13.e"] + 0.2, pts, espaco=140)
        E._meio(c, "S", 1450, 640, 120, "g", NEG, q)
        E.foco(c, t, C["s13.e"] + 0.4, 0.4, lambda a: centro(c, "face sul: horário", 1450, 880, 52, "g", CERTO, a))


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    def cena(a):
        e = 60
        M.rrect(c, 1250, 330, 440, 420, 18, "#9AA0A8", a)
        M.rrect(c, 1250 + e, 330 + e, 440 - 2 * e, 420 - 2 * e, 10, E.PAPEL, a)
        for k in range(8):
            M.line(c, 1250 - 10, 400 + k * 36, 1250 + e + 10, 392 + k * 36, TINTA, a, 6)
        for k in range(2):
            M.line(c, 1690 - e - 10, 480 + k * 80, 1700, 472 + k * 80, TINTA, a, 6)
        centro(c, "400", 1280, 800, 48, "g", TINTA, a)
        centro(c, "?", 1660, 800, 56, "g", COR, a)
    if t < C["s15"]:
        enunciado(c, t, C, "s14", 5, [(C["s14.a"], "U₁ = 220 V,  N₁ = 400"), (C["s14.b"], "U₂ = 11 V"), (C["s14.c"], "N₂ = ?"),
                                      (C["s14.d"], "i₂ = 2 A:  i₁ = ?")], cena, C["s14.e"])
        return
    passos(c, t, [(C["s15.a"], "f{220}{11} = 20:  a tensão cai 20 vezes"), (C["s15.b"], "N₂ = f{400}{20} = 20 espiras", COR),
                  (C["s15.c"], "a corrente vai ao contrário"), (C["s15.d"], "i₁ = f{2}{20}")], y0=260, dy=150)
    bola_txt(c, t, C["s15.e"], "0,1 A", 1500, 820, 170, 80)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate((("s16.a", [("corrente", "g", 70), ("cria campo", "i", 74)]),
                                     ("s16.b", [("campo", "g", 70), ("empurra carga e fio", "i", 74)]),
                                     ("s16.c", [("fluxo mudando", "g", 70), ("cria corrente", "i", 74)]))):
        y = 340 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 48, a=a), centro(c, str(i + 1), 300, y - 4, 56, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.frase(c, t, C["s16.d"], ps("próxima aula:", "i", 56, TINTA2) + [("como uma usina gera eletricidade", "g", 56, COR)], W / 2, 820, "center", 0.1)
    E.foco(c, t, C["s16.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 700, 960, 64, estilo="g", a=a))
    E.frase(c, t, C["s16.f"], [("bons", "i", 80), ("estudos!", "i", 80, COR)], 1350, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
