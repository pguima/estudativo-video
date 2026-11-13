"""Visual — Estudativo · QUI-SOL-011: praticando propriedades coligativas (aula de prática, cinco questões).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a das propriedades coligativas (cabeçalho de
QUI-SOL-008/roteiro/visual.py). Usa as peças das aulas irmãs (panela, montanha e duelo da 008; unidade e íons da 009; tubo_u,
hemacia e setas_agua da 010), carregadas de lá para o desenho ficar idêntico. Cada questão: número na esfera, enunciado à
esquerda, desenho à direita; na pausa, o relógio. Todo instante vem de C[...]."""
import importlib.util
import math
from pathlib import Path

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia


def _irma(aid):
    """visual.py de outra aula do grupo, para reaproveitar as peças"""
    p = Path(__file__).resolve().parents[2] / aid / "roteiro" / "visual.py"
    s = importlib.util.spec_from_file_location(f"v_{aid.replace('-', '_')}", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


V8, V9, V10 = _irma("QUI-SOL-008"), _irma("QUI-SOL-009"), _irma("QUI-SOL-010")
E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-011_praticando_coligativas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
SETA_AGUA = V10.SETA_AGUA

# as contas da aula
Q2 = dict(A=0.2 * 1, B=0.1 * 2, C=0.1 * 3)
assert max(Q2, key=Q2.get) == "C" and abs(Q2["A"] - Q2["B"]) < 1e-12
assert sum(Q.contar("KCl").values()) == 2 and Q.contar("MgCl2") == {"Mg": 1, "Cl": 2}
assert 0.1 * 2 > 0.15  # questão cinco: o lado do sal tem mais partículas


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, est, cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def cabecalho(c, t, t0, n, tema):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 150, 56, a=a), centro(c, str(n), XE + 50, 176, 70, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 70, TINTA2), (tema, "g", 64, COR)], XE + 130, 175, passo=0.12)


def figura_ou_relogio(c, t, C, cena_pausa, fn):
    if t < C[cena_pausa]:
        fn()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1470, cy=540, r=220)


def linha(c, t, ti, partes, y, x=XE, passo=0.08):
    E.frase(c, t, ti, partes, x, y, passo=passo)


def uva(c, cx, cy, r, incha=0.0, a=1.0):
    """uva-passa: enrugada e escura; incha = 0..1 fica lisa e redonda"""
    if a <= 0:
        return
    rr = r * (1 + 0.4 * incha)
    pth = skia.Path()
    for k in range(61):
        ang = 2 * math.pi * k / 60
        rug = 1 - 0.12 * (1 - incha) * (0.5 + 0.5 * math.sin(ang * 9))
        px, py = cx + rr * math.cos(ang) * rug, cy + rr * 0.85 * math.sin(ang) * rug
        (pth.moveTo if k == 0 else pth.lineTo)(px, py)
    pth.close()
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx - rr * 0.3, cy - rr * 0.3), rr * 1.4,
                                               [M.hexc(M.mix("#7B3F61", "#B0679A", incha), a), M.hexc(M.mix("#3E1F33", "#6E2E58", incha), a)], [0, 1]))
    c.drawPath(pth, p)


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 150, COR), ("questões", "i", 120)], XE, 330, passo=0.15)
    for k, (ti, s) in enumerate(((C["s01.b"], "cozinha"), (C["s01.b"] + 0.6, "lista de soluções"), (C["s01.b"] + 1.4, "uva-passa"),
                                 (C["s01.b"] + 2.0, "estrada com neve"), (C["s01.b"] + 2.8, "membrana"))):
        E.foco(c, t, ti, 0.4, lambda a, k=k: (E.bola(c, XE + 40, 474 + 100 * k, 34, a=a), centro(c, str(k + 1), XE + 40, 492 + 100 * k, 44, "g", BR, a)))
        E.frase(c, t, ti + 0.1, [(s, "g", 60)], XE + 100, 500 + 100 * k)
    E.foco(c, t, C["s01.c"], 0.8, lambda a: E.simbolo(c, 1500, 600, 260 * a, giro=8 * math.sin(t * 0.4)), blur=0)
    pilula_em(c, t, C["s01.c"] + 0.4, "pause, tente, confira", 1500, 950, 50, E.COR)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("suas ferramentas", "i", 70, TINTA2), XE, 170, passo=0.12)
    E.frase(c, t, C["s02.a"], [("soluto", "g", 64, COR), ("→", "g", 64, TINTA2)], XE, 320, passo=0.1)
    E.frase(c, t, C["s02.b"], ps("ferve", "i", 66) + [("mais quente", "g", 62, ERRADO)], XE + 300, 320, passo=0.1)
    E.frase(c, t, C["s02.c"], ps("congela", "i", 66) + [("mais frio", "g", 62, SETA_AGUA)], XE + 300, 420, passo=0.1)
    E.frase(c, t, C["s02.d"], [("coligativo:", "g", 60, COR)] + ps("depende só de quantas partículas", "i", 60), XE, 560, passo=0.08)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "concentração × partículas", XE, 740, 76, "g", TINTA, a))
    E.frase(c, t, C["s03.b"], ps("osmose: a água corre atrás do", "i", 60) + [("soluto", "g", 58, COR)], XE, 880, passo=0.08)
    rotulo(c, t, C["s03.c"], "do menos para o mais concentrado", XE + 520, 960, 44, TINTA, "b")


# ---------------- questão 1: cozinha ----------------
def b_q1(c, t, C, b):
    cabecalho(c, t, C["s04"], 1, "cozinha")
    linha(c, t, C["s04.a"], [("1", "g", 56, COR)] + ps("na serra, o feijão demora mais", "i", 58), 320)
    linha(c, t, C["s04.b"], [("2", "g", 56, COR)] + ps("panela de pressão: cozinha mais rápido", "i", 58), 420)
    linha(c, t, C["s04.c"], [("3", "g", 56, COR)] + ps("macarrão com sal: ferve pouco acima de 100 °C", "i", 52), 520)
    linha(c, t, C["s04.d"], ps("em quais o efeito é", "i", 62) + [("coligativo?", "g", 58, COR)], 680)

    def fig():
        E.foco(c, t, C["s04.a"], 0.5, lambda a: V8.montanha(c, 1260, 520, 300, 260, a))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: V8.panela(c, t, 1720, 470, 220, 120, a, pressao=True))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: V8.panela(c, t, 1500, 900, 300, 150, a, ferve=C["s04.c"] + 0.5, sal=8))
    figura_ou_relogio(c, t, C, "s05", fig)


def b_r1(c, t, C, b):
    cabecalho(c, t, C["s06"] - 0.3, 1, "resolvendo")
    E.frase(c, t, C["s06"], ps("pergunte:", "i", 60, TINTA2) + [("o que mudou?", "g", 58, COR)], XE, 290, passo=0.1)
    linhas = ((C["s06.a"], "1", "serra: pressão do ar menor", False), (C["s06.b"], "2", "panela: pressão maior", False), (C["s06.c"], "3", "sal: mudou o que está dissolvido", True))
    for k, (ti, n, s, col) in enumerate(linhas):
        y = 420 + k * 130
        linha(c, t, ti, [(n, "g", 56, COR)] + ps(s, "i", 56), y)
        pilula_em(c, t, ti + 1.4, "coligativo" if col else "não é coligativo", 1500, y - 18, 46, E.COR if col else TINTA)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: E.formula(c, "o sal: + menos de 0,5 °C", XE, 900, 64, "g", TINTA, a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.escreve(c, "não é ele que acelera o macarrão", XE, 990, 48, "b", TINTA2, a))


# ---------------- questão 2: lista ----------------
def b_q2(c, t, C, b):
    cabecalho(c, t, C["s08"], 2, "lista de soluções")
    itens = ((C["s08.b"], "A", "sacarose (açúcar)", "0,2 mol/L"), (C["s08.c"], "B", "cloreto de potássio", "0,1 mol/L"), (C["s08.d"], "C", "cloreto de magnésio", "0,1 mol/L"))
    for k, (ti, l, nome, conc) in enumerate(itens):
        y = 340 + k * 120
        E.foco(c, t, ti, 0.4, lambda a, l=l, y=y: (E.bola(c, XE + 40, y - 22, 40, a=a), centro(c, l, XE + 40, y - 2, 50, "g", BR, a)))
        linha(c, t, ti + 0.1, ps(nome, "i", 58) + [(conc, "g", 54, COR)], y, XE + 100)
    linha(c, t, C["s08.e"], ps("qual ferve", "i", 60) + [("mais quente?", "g", 56, COR)], 760)
    linha(c, t, C["s08.f"], ps("alguma", "i", 60) + [("empata?", "g", 56, COR)], 860)

    def fig():
        for k, (f, ti) in enumerate((("KCl", C["s08.c"]), ("MgCl2", C["s08.d"]))):
            E.foco(c, t, ti, 0.4, lambda a, f=f, k=k: Q.formula(c, f, 1500, 420 + 200 * k, 90, TINTA, a, "center"))
    figura_ou_relogio(c, t, C, "s09", fig)


def b_r2(c, t, C, b):
    cabecalho(c, t, C["s10"] - 0.3, 2, "resolvendo")
    itens = ((C["s10.a"], "A", "0,2 × 1 = 0,2", "açúcar"), (C["s10.b"], "B", "0,1 × 2 = 0,2", "KCl"), (C["s10.c"], "C", "0,1 × 3 = 0,3", "MgCl2"))
    for k, (ti, l, conta, f) in enumerate(itens):
        y = 340 + k * 170
        E.foco(c, t, ti, 0.4, lambda a, l=l, y=y: (E.bola(c, XE + 40, y - 22, 44, a=a), centro(c, l, XE + 40, y - 2, 54, "g", BR, a)))
        E.formula_em(c, t, ti + 0.3, conta, XE + 120, y, 70, "g", TINTA)
        if f == "açúcar":
            V9.unidade(c, t, ti + 0.2, f, 1000, y - 24, 26)
        else:
            _unidade_k(c, t, ti + 0.2, f, 1000, y - 24, 26, ti + 0.8)
    pilula_em(c, t, C["s11.a"], "C ferve mais quente", 1560, 660, 54, E.COR)
    pilula_em(c, t, C["s11.b"], "A e B empatam", 1560, 440, 54, TINTA)
    rotulo(c, t, C["s11.c"], "mesmo com concentrações diferentes", 1560, 530, 40, TINTA2, "b")


def _unidade_k(c, t, t0, f, cx, cy, r, abre):
    """KCl e MgCl₂ no mesmo desenho dos íons da QUI-SOL-009"""
    if t < t0:
        return
    q = ep(t, t0, 0.4)
    s = ease_io(prog(t, abre, 0.8))
    d = lerp(r * 1.6, r * 3.4, s)
    if f == "KCl":
        pts = [((cx - d / 2, cy), "K", "+"), ((cx + d / 2, cy), "Cl", "−")]
    else:
        pts = [((cx, cy), "Mg", "2+"), ((cx - d, cy + lerp(0, 30, s)), "Cl", "−"), ((cx + d, cy + lerp(0, 30, s)), "Cl", "−")]
    for (x, y), el, cg in pts:
        V9.ion(c, x, y, r, el, cg if s > 0.5 else "", q)


# ---------------- questão 3: uva-passa e náufrago ----------------
def b_q3(c, t, C, b):
    cabecalho(c, t, C["s12"], 3, "uva-passa e náufrago")
    linha(c, t, C["s12.a"], ps("uva-passa, cheia de açúcar,", "i", 58), 330)
    linha(c, t, C["s12.a"] + 1.4, ps("de molho em", "i", 58) + [("água pura", "g", 56, COR)], 410)
    linha(c, t, C["s12.b"], ps("náufrago bebe", "i", 58) + [("água do mar", "g", 56, COR)], 540)
    linha(c, t, C["s12.c"], [("A", "g", 56, COR)] + ps("o que acontece com a uva-passa?", "i", 56), 700)
    linha(c, t, C["s12.d"], [("B", "g", 56, COR)] + ps("e com as células do náufrago?", "i", 56), 800)

    def fig():
        Q.bequer(c, t, C["s12.a"], 1450, 900, 420, 460, 0.75, Q.AGUA, graduacao=False)
        E.foco(c, t, C["s12.a"] + 0.3, 0.5, lambda a: uva(c, 1450, 760, 70, 0, a))
    figura_ou_relogio(c, t, C, "s13", fig)


def b_r3(c, t, C, b):
    cabecalho(c, t, C["s14"] - 0.3, 3, "resolvendo")
    if t < C["s15"]:
        Q.bequer(c, t, C["s14"] - 0.3, 1450, 900, 420, 460, 0.75, Q.AGUA, graduacao=False)
        inc = ease_io(prog(t, C["s14.c"], 1.6))
        E.foco(c, t, C["s14"], 0.4, lambda a: uva(c, 1450, 740, 80, inc, a))
        V10.setas_agua(c, t, C["s14.c"], 1300, 1360, 750, 2)
        V10.setas_agua(c, t, C["s14.c"], 1600, 1540, 750, 2)
        linha(c, t, C["s14.a"], [("A", "g", 56, COR)] + ps("dentro da uva: mais concentrado", "i", 58), 330)
        linha(c, t, C["s14.b"], ps("a água corre atrás do soluto", "i", 58), 450)
        linha(c, t, C["s14.c"], ps("entra na uva, e ela", "i", 60) + [("incha", "g", 58, COR)], 570)
        return
    m = -ease_io(prog(t, C["s15.c"], 1.4))
    E.foco(c, t, C["s15"], 0.4, lambda a: (c.drawCircle(1450, 620, 300, M.paint("#BFE3D8", 0.6 * a)), V10.hemacia(c, 1450, 620, 140, m, a)))
    V10.setas_agua(c, t, C["s15.c"], 1600, 1720, 630, 3)
    linha(c, t, C["s15.a"], [("B", "g", 56, COR)] + ps("com o náufrago, o contrário", "i", 58), 330)
    linha(c, t, C["s15.b"], ps("o sangue fica mais concentrado", "i", 56), 450)
    linha(c, t, C["s15.b"] + 1.6, ps("que as células", "i", 56), 530)
    linha(c, t, C["s15.c"], ps("a água", "i", 58) + [("sai", "g", 56, SETA_AGUA)] + ps("das células", "i", 58), 660)
    linha(c, t, C["s15.d"], ps("a sede", "i", 58) + [("piora", "g", 56, ERRADO)], 770)
    pilula_em(c, t, C["s15.e"], "água do mar desidrata", XE + 330, 900, 50, E.COR)


# ---------------- questão 4: estrada com neve ----------------
def b_q4(c, t, C, b):
    cabecalho(c, t, C["s16"], 4, "estrada com neve")
    linha(c, t, C["s16.a"], ps("estradas com neve recebem", "i", 58), 330)
    linha(c, t, C["s16.a"] + 1.4, [("sal de cozinha", "g", 56, COR)] + ps("ou", "i", 58) + [("cloreto de cálcio", "g", 56, COR)], 410)
    linha(c, t, C["s16.b"], [("A", "g", 56, COR)] + ps("qual efeito derrete o gelo?", "i", 56), 560)
    linha(c, t, C["s16.c"], [("B", "g", 56, COR)] + ps("mol por mol, por que o cloreto", "i", 56), 660)
    linha(c, t, C["s16.c"] + 2.0, ps("de cálcio funciona melhor?", "i", 56), 740, XE + 50)

    def fig():
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (M.rrect(c, 1180, 760, 620, 120, 20, "#3A3B42", a), M.rrect(c, 1200, 730, 580, 50, 22, V9.GELO, a)))
        V9.unidade(c, t, C["s16.a"] + 1.0, "NaCl", 1330, 560, 34, abre=C["s16.a"] + 1.4)
        V9.unidade(c, t, C["s16.a"] + 1.6, "CaCl2", 1650, 560, 30, abre=C["s16.a"] + 2.0)
    figura_ou_relogio(c, t, C, "s17", fig)


def b_r4(c, t, C, b):
    cabecalho(c, t, C["s18"] - 0.3, 4, "resolvendo")
    linha(c, t, C["s18.a"], [("A", "g", 56, COR)] + ps("congela abaixo de 0 °C:", "i", 58) + [("crioscopia", "g", 56, COR)], 320)
    linha(c, t, C["s18.b"], ps("o gelo derrete mesmo no frio", "i", 56), 420)
    linha(c, t, C["s18.c"], [("B", "g", 56, COR), ("NaCl:", "g", 56)] + ps("2 partículas", "i", 58), 580)
    linha(c, t, C["s18.d"], [("CaCl₂:", "g", 56)] + ps("3 partículas", "i", 58), 680, XE + 50)
    V9.unidade(c, t, C["s18.c"], "NaCl", 1350, 560, 40, abre=C["s18.c"] + 0.5, num=C["s18.c"] + 1.0)
    V9.unidade(c, t, C["s18.d"], "CaCl2", 1350, 800, 40, abre=C["s18.d"] + 0.5, num=C["s18.d"] + 1.0)
    pilula_em(c, t, C["s18.e"], "mais partículas por mol, maior efeito", XE + 470, 860, 46, E.COR)


# ---------------- questão 5: membrana ----------------
def b_q5(c, t, C, b):
    cabecalho(c, t, C["s19"], 5, "membrana")
    linha(c, t, C["s19.a"], ps("membrana semipermeável entre duas soluções", "i", 52), 320)
    linha(c, t, C["s19.b"], [("A:", "g", 58, COR)] + ps("sal de cozinha", "i", 60) + [("0,1 mol/L", "g", 56, COR)], 450)
    linha(c, t, C["s19.c"], [("B:", "g", 58, COR)] + ps("glicose", "i", 60) + [("0,15 mol/L", "g", 56, COR)], 560)
    linha(c, t, C["s19.d"], ps("para que lado vai a", "i", 62) + [("água?", "g", 58, SETA_AGUA)], 720)

    def fig():
        E.foco(c, t, C["s19.a"], 0.5, lambda a: V10.tubo_u(c, t, 1260, 330, 520, 520, 0.55, 0.55, 6, 5, a, rot=("A", "B")))
    figura_ou_relogio(c, t, C, "s20", fig)


def b_r5(c, t, C, b):
    cabecalho(c, t, C["s21"] - 0.3, 5, "resolvendo")
    sobe = ease_io(prog(t, C["s21.d"], 1.6))
    E.foco(c, t, C["s21"] - 0.3, 0.5, lambda a: V10.tubo_u(c, t, 1260, 330, 520, 520, lerp(0.55, 0.75, sobe), lerp(0.55, 0.35, sobe), 6, 5, a, rot=("A", "B")))
    V10.setas_agua(c, t, C["s21.d"], 1520 + 80, 1520 - 80, 800, 2)
    E.frase(c, t, C["s21"], ps("conte as partículas", "i", 60, TINTA2), XE, 290, passo=0.1)
    E.formula_em(c, t, C["s21.a"], "A: 0,1 × 2 = 0,2", XE, 420, 72, "g", TINTA)
    E.formula_em(c, t, C["s21.b"], "B: 0,15 × 1 = 0,15", XE, 530, 72, "g", TINTA)
    E.formula_em(c, t, C["s21.c"], "A tem mais partículas", XE, 660, 60, "g", COR)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.formula(c, "B → A", XE, 790, 90, "g", SETA_AGUA, a))
    E.foco(c, t, C["s21.d"] + 0.5, 0.4, lambda a: E.selo(c, XE + 380, 760, 46, True, a))
    E.foco(c, t, C["s22.a"], 0.5, lambda a: E.formula(c, "0,1 < 0,15: A → B", XE, 940, 60, "g", ERRADO, a))
    if t >= C["s22.b"]:
        E.risco(c, XE - 10, 960, XE + 560, 890, t, C["s22.b"], largura=10)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s23.a", [("o", "i", 70), ("que", "i", 70), ("mudou:", "i", 70), ("pressão", "g", 66), ("ou", "i", 70), ("solução?", "g", 66, COR)]),
                 ("s23.b", [("conte", "i", 70), ("as", "i", 70), ("partículas", "g", 66, COR)]),
                 ("s23.c", [("osmose:", "g", 66), ("a", "i", 70), ("água", "g", 66, SETA_AGUA), ("corre", "i", 70), ("atrás", "i", 70), ("do", "i", 70), ("soluto", "g", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], ps("trilha de", "i", 80) + [("soluções", "g", 80, COR)], XE, 250, passo=0.12)
    E.frase(c, t, C["s24"] + 1.2, [("concluída", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s24.a"], ps("do copo de mistura à água atravessando a membrana", "i", 50), XE, 530, passo=0.06)
    E.foco(c, t, C["s24"] + 1.6, 0.6, lambda a: E.simbolo(c, 1520, 820, 160 * a, giro=6 * math.sin(t * 0.5)), blur=0)
    E.foco(c, t, C["s24.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s24.b"] + 0.2, 0.4))
    E.frase(c, t, C["s24.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 760)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
