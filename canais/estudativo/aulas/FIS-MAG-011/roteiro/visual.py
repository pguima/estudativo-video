"""Visual — Estudativo · FIS-MAG-011: praticando usinas e matriz elétrica. Linguagem visual do Magnetismo e das usinas: veja o
visual.py da FIS-MAG-001 e da FIS-MAG-009 (cadeia de energia em pílulas, a última laranja). Prática no modelo da FIS-MAG-008:
enunciado à esquerda, desenho à direita, relógio na pausa, um passo por linha na resolução. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-011_praticando_usinas_e_matriz_eletrica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
AGUA = "#7FC8E8"
SOL = "#FFB020"

# todas as contas da aula
assert 50 * 80 == 4000 and 10_000 * 4000 == 40_000_000 and math.isclose(0.85 * 40, 34)
assert math.isclose(210 / 600, 0.35) and 21 / 60 == 0.35 and 600 - 210 == 390
assert 0.20 * 1000 == 200 and 1_000_000 / 200 == 5000
assert 5000 / (105 * 68) < 0.75  # 5.000 m² ≈ dois terços de um campo de futebol (≈ 7.000 m²)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


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


def enunciado(c, t, C, cena, n, linhas, desenho, pausa):
    E.frase(c, t, C[cena], [("questão", "i", 70, COR), (str(n), "g", 70, COR)], XE, 180, passo=0.12)
    for i, (ti, s) in enumerate(linhas):
        E.foco(c, t, ti, 0.5, lambda a, i=i, s=s: E.formula(c, s, XE, 330 + 110 * i, 58, "g", TINTA, a))
    if t < pausa:
        E.foco(c, t, linhas[0][0], 0.5, desenho)
    else:
        E.relogio(c, t, pausa, cx=1500, cy=480, r=190)


def passos(c, t, itens, x=XE, y0=260, dy=130, size=72):
    for i, it in enumerate(itens):
        ti, s = it[0], it[1]
        cor = it[2] if len(it) > 2 else TINTA
        E.foco(c, t, ti, 0.5, lambda a, i=i, s=s, cor=cor: E.formula(c, s, x, y0 + dy * i, size, "g", cor, a))


def represa(c, x, y, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y, 220, 240, 6, AGUA, a)
    p = skia.Path(); p.moveTo(x + 220, y - 20); p.lineTo(x + 280, y - 20); p.lineTo(x + 340, y + 240); p.lineTo(x + 220, y + 240); p.close()
    c.drawPath(p, M.paint("#B9B3A6", a))
    M.line(c, x + 200, y + 180, x + 420, y + 320, "#3B8DB5", a, 22)


def chama(c, cx, cy, s, a, t):
    for k in range(3):
        h = s * (1 + 0.15 * math.sin(t * 9 + k))
        p = skia.Path(); x = cx + (k - 1) * s * 0.5
        p.moveTo(x - s * 0.3, cy); p.quadTo(x - s * 0.3, cy - h * 0.6, x, cy - h); p.quadTo(x + s * 0.3, cy - h * 0.6, x + s * 0.3, cy); p.close()
        c.drawPath(p, M.paint(E.COR if k != 1 else SOL, a))


def painel(c, cx, cy, w, h, a=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - w / 2, cy + h / 2); p.lineTo(cx + w / 2, cy + h / 2); p.lineTo(cx + w / 2 - w * 0.12, cy - h / 2); p.lineTo(cx - w / 2 + w * 0.12, cy - h / 2); p.close()
    c.drawPath(p, M.paint("#22416E", a))
    M.line(c, cx, cy + h / 2, cx, cy + h, TINTA2, a, 8)


# ---------------- gancho, lembrete e método ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], ps("questão de usina:", "i", 76) + [("conta fácil", "g", 76, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s01.b"], ps("o que ela pede:", "i", 64) + [("o caminho da energia", "g", 64)], XE, 420, passo=0.12)
    E.frase(c, t, C["s01.c"], ps("e", "i", 64) + [("a fonte certa", "g", 64, COR)], XE + 420, 520, passo=0.12)
    E.frase(c, t, C["s01.d"], [("5 questões,", "g", 70), ("do começo ao fim", "i", 74)], XE, 720, passo=0.12)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as duas últimas aulas", "i", 80), XE, 220, passo=0.12)
    for i, (k, s) in enumerate((("s02.a", "a cadeia de energia"), ("s02.b", "a potência da queda d'água"), ("s02.c", "o rendimento"), ("s02.d", "a intermitência"))):
        y = 400 + i * 130
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 36, a=a), centro(c, str(i + 1), XE + 40, y - 6, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 66)], XE + 110, y)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.5), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54), XE, 960, passo=0.1)


def b_metodo(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s03"], ps("primeiro,", "i", 76, CLARO) + [("o método", "g", 76, BR)], W / 2, 180, "center", 0.12)
    E.frase(c, t, C["s03.a"], ps("toda cadeia termina igual:", "i", 60, CLARO), W / 2, 340, "center", 0.1)
    cadeia(c, t, [(C["s03.a"] + 0.6, "movimento"), (C["s03.a"] + 1.0, "gerador"), (C["s03.a"] + 1.4, "eletricidade")], 560, 460, size=50)
    E.frase(c, t, C["s03.b"], ps("comece do fim:", "i", 60, CLARO) + [("o que gira a turbina?", "g", 60, BR)], W / 2, 640, "center", 0.1)
    E.frase(c, t, C["s03.c"], [("água,", "g", 66, E.CLARO), ("vapor", "g", 66, E.CLARO), ("ou", "i", 66, CLARO), ("vento", "g", 66, E.CLARO)], W / 2, 780, "center", 0.15)
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.pilula(c, "exceção: painel solar, luz direto em eletricidade", W / 2, 930, 46, "g", fundo=E.COR, a=a))


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    if t < C["s05"]:
        enunciado(c, t, C, "s04", 1, [(C["s04.a"], "hidrelétrica: a sequência"), (C["s04.a"] + 1.4, "da represa até a rede?"),
                                      (C["s04.b"], "e na nuclear, o que muda?")], lambda a: represa(c, 1300, 400, a), C["s04.c"])
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05"], [("hidrelétrica", "g", 76, COR)], XE, 220)
        E.foco(c, t, C["s05.a"], 0.5, lambda a: represa(c, 1300, 360, a))
        cadeia(c, t, [(C["s05.a"], "potencial"), (C["s05.b"], "cinética da água"), (C["s05.c"], "cinética da turbina"), (C["s05.d"], "elétrica")],
               XE, 800, gap=50, size=46)
        E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "4 etapas, do alto da represa à rede", W / 2, 960, 46, "g", fundo=CERTO, a=a))
        return
    E.frase(c, t, C["s06.a"], [("nuclear:", "g", 76, COR), ("o começo é outro", "i", 80)], XE, 220, passo=0.12)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (M.rrect(c, 1250, 330, 260, 220, 30, "#D9D6CF", a), E.formula(c, "reator", 1380, 460, 54, "g", TINTA, a, "center")))
    E.foco(c, t, C["s06.b"] + 0.5, 0.4, lambda a: E.escreve(c, "só produz calor", XE, 400, 60, "b", TINTA2, a))
    cadeia(c, t, [(C["s06.b"], "calor"), (C["s06.c"], "vapor"), (C["s06.d"], "giro da turbina"), (C["s06.e"], "eletricidade")], XE, 700, gap=50, size=50)
    E.foco(c, t, C["s06.f"], 0.5, lambda a: E.pilula(c, "como o núcleo dá calor: aula de fissão", W / 2, 920, 46, "g", fundo=TINTA2, a=a))


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    if t < C["s08"]:
        enunciado(c, t, C, "s07", 2, [(C["s07.a"], "Z = 50 m^3/s,   h = 80 m"), (C["s07.b"], "rendimento: 85%"), (C["s07.c"], "potência elétrica = ?")],
                  lambda a: represa(c, 1300, 400, a), C["s07.d"])
        return
    passos(c, t, [(C["s08.a"], "P = 10.000 · Z · h"), (C["s08.b"], "50 · 80 = 4.000"), (C["s08.c"], "10.000 · 4.000 = 40.000.000 W = 40 MW"),
                  (C["s08.d"], "0,85 × 40")], y0=280, dy=150, size=66)
    bola_txt(c, t, C["s08.e"], "34 MW", 1500, 820, 170, 80)


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    if t < C["s10"]:
        enunciado(c, t, C, "s09", 3, [(C["s09.a"], "recebe 600 MW de calor"), (C["s09.a"] + 1.6, "entrega 210 MW elétricos"),
                                      (C["s09.b"], "rendimento = ?"), (C["s09.c"], "calor para o ambiente = ?")],
                  lambda a: (chama(c, 1450, 700, 130, a, t), M.rrect(c, 1330, 430, 240, 160, 20, "#D9D6CF", a)), C["s09.d"])
        return
    passos(c, t, [(C["s10.a"], "η = f{210}{600}"), (C["s10.b"], "= f{21}{60}"), (C["s10.c"], "= 0,35 = 35%", COR)], y0=300, dy=170, size=80)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "600 − 210", 1150, 470, 80, "g", TINTA, a))
    bola_txt(c, t, C["s10.e"], "390 MW", 1450, 760, 170, 72)
    E.foco(c, t, C["s10.e"] + 0.8, 0.4, lambda a: centro(c, "390 milhões de J/s: segunda lei", 1450, 990, 46, "i", TINTA2, a))


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    if t < C["s12"]:
        enunciado(c, t, C, "s11", 4, [(C["s11.a"], "quer 1 MW ao meio-dia"), (C["s11.b"], "1.000 W por m^2,  20%"), (C["s11.c"], "quantos m^2 de painel?")],
                  lambda a: painel(c, 1450, 560, 520, 220, a), C["s11.d"])
        return
    passos(c, t, [(C["s12.a"], "0,20 × 1.000"), (C["s12.b"], "= 200 W por m^2"), (C["s12.c"], "1 MW = 1.000.000 W"),
                  (C["s12.d"], "f{1.000.000}{200}")], y0=260, dy=150, size=72)
    bola_txt(c, t, C["s12.e"], "5.000 m^2", 1450, 600, 190, 66)
    E.foco(c, t, C["s12.e"] + 0.6, 0.4, lambda a: centro(c, "uns dois terços de um campo de futebol", 1450, 860, 44, "i", TINTA2, a))
    E.foco(c, t, C["s12.f"], 0.5, lambda a: E.pilula(c, "à noite: zero", 1450, 960, 56, "g", fundo=ERRADO, a=a))


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    opcoes = (("solar", "intermitente"), ("eólica", "intermitente"), ("térmica a gás", "queima"), ("hidrelétrica", "fica"))
    if t < C["s14"]:
        enunciado(c, t, C, "s13", 5, [(C["s13.a"], "precisa de energia à noite"), (C["s13.b"], "não pode queimar combustível")],
                  lambda a: None, C["s13.e"])
        if t < C["s13.e"]:
            for i, (nome, _) in enumerate(opcoes):
                E.foco(c, t, C["s13.c"] + 0.3 * i, 0.4, lambda a, i=i, nome=nome: E.pilula(c, nome, 1450, 330 + i * 130, 54, "g", fundo=TINTA, a=a))
            E.frase(c, t, C["s13.d"], [("qual escolher?", "g", 64, COR)], XE, 700)
        return
    E.frase(c, t, C["s14"], ps("elimine", "i", 76) + [("uma por uma", "g", 76, COR)], XE, 220, passo=0.12)
    tempos = (C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"])
    for i, (nome, motivo) in enumerate(opcoes):
        y = 380 + i * 150
        E.pilula(c, nome, 560, y, 56, "g", fundo=TINTA)
        ok = i == 3
        E.foco(c, t, tempos[i], 0.4, lambda a, i=i, y=y, ok=ok, motivo=motivo: (E.selo(c, 900, y - 18, 40, ok, a),
                                                                                E.escreve(c, "a represa guarda água" if ok else motivo, 980, y, 54, "b", CERTO if ok else ERRADO, a)))
        if not ok and t >= tempos[i] + 0.3:
            E.risco(c, 400, y - 10, 720, y - 30, t, tempos[i] + 0.3, largura=8)
    E.foco(c, t, C["s14.a"], 0.4, lambda a: E.escreve(c, "intermitência e queima", 1100, 230, 50, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s15.a", [("cadeia:", "g", 66), ("comece pelo que gira a turbina", "i", 70)]),
                 ("s15.b", None),
                 ("s15.c", [("fonte:", "g", 66), ("gera quando quero? queima?", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            if partes:
                E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
            else:
                E.formula_em(c, t, C[k] + 0.1, "água:  P = 10.000 · Z · h", 400, y, 66, "g", TINTA)
        E.frase(c, t, C["s15.d"], ps("fim da trilha de", "i", 58, TINTA2) + [("eletromagnetismo e usinas", "g", 58, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s16.a"] + 0.2, 0.4))
    E.frase(c, t, C["s16.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
