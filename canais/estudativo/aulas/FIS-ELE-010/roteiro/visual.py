"""Visual — Estudativo · FIS-ELE-010: segunda lei de Ohm.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: F.fio, F.resistor, unidades em cinza-tinta, Ω e = só na fonte pesada).
Nesta aula: o FIO de verdade é a peça `fio_cobre` (barra cor de cobre com o corte, a "bolinha", na ponta direita): o
comprimento e a espessura mudam na tela no instante da fala. Material diferente = outra cor (nicromo em cinza).
Fator de cada mudança numa pílula: × em laranja (aumenta R), ÷ em azul (diminui R).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-010_segunda_lei_de_ohm.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "formula", "efeitos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
COBRE = "#C8743A"
NICROMO = "#8C8F99"

# todas as contas da aula
assert 4 * 3 / 2 == 6 and 4 * 3 == 12 and 12 / 2 == 6
assert 2 * 2 == 4 and 3 ** 2 == 9
assert 12 * 3 == 36 and 36 / 4 == 9 and 12 * 3 / 2 == 18


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "6 Ω" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (70 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: E.formula(c, l3, x + 44, y + 240, 46, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


def fator(c, t, t0, s, cx, cy, size=48, menos=False):
    """pílula do fator: × aumenta R (laranja), ÷ diminui R (azul)"""
    pilula_em(c, t, t0, s, cx, cy, size, F.NEG if menos else E.COR)


# ---------------- o fio ----------------
def fio_cobre(c, x, cy, L, d, a=1.0, cor=COBRE, corte=True):
    """fio de comprimento L e espessura d, da esquerda (x) para a direita, com o corte (a bolinha) na ponta direita"""
    if a <= 0 or L <= 0:
        return
    rx = max(5, d * 0.22)
    escuro, claro = E.mix(cor, "#000000", 0.3), E.mix(cor, BR, 0.4)
    c.drawOval(skia.Rect.MakeXYWH(x - rx, cy - d / 2, 2 * rx, d), M.paint(escuro, a))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, cy - d / 2), skia.Point(0, cy + d / 2)],
                                               [M.hexc(claro, a), M.hexc(cor, a), M.hexc(escuro, a)], [0.0, 0.45, 1.0]))
    c.drawRect(skia.Rect.MakeXYWH(x, cy - d / 2, L, d), p)
    if corte:
        c.drawOval(skia.Rect.MakeXYWH(x + L - rx, cy - d / 2, 2 * rx, d), M.paint(E.mix(cor, BR, 0.55), a))
        c.drawOval(skia.Rect.MakeXYWH(x + L - rx, cy - d / 2, 2 * rx, d), M.paint(escuro, a, stroke=3))


def cota(c, x0, x1, y, rot, a=1.0, cor=TINTA2, size=52):
    """linha de cota com tracinhos nas pontas e o rótulo em cima"""
    if a <= 0:
        return
    M.line(c, x0, y, x1, y, cor, a, 4)
    for x in (x0, x1):
        M.line(c, x, y - 16, x, y + 16, cor, a, 4)
    E._meio(c, rot, (x0 + x1) / 2, y - size * 0.75, size, "g", cor, a)


def corte_zoom(c, cx, cy, r, a=1.0, cor=COBRE, rot="A"):
    """o corte do fio visto de frente: círculo cor de cobre com o rótulo"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, E.mix(cor, BR, 0.25), a)
    c.drawCircle(cx, cy, r, M.paint(E.mix(cor, "#000000", 0.3), a, stroke=4))
    if rot:
        E._meio(c, rot, cx, cy, r * 0.8, "g", BR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("estique o", "i", 90) + [("fio", "g", 90, COR)], XE, 230, passo=0.14)
        q = ease_io(prog(t, C["s01.a"] + 1.2, 1.6))
        L, d = lerp(560, 1120, q), lerp(120, 60, q)
        x0 = 400
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: fio_cobre(c, x0, 480, L, d, a), blur=0)
        E.foco(c, t, C["s01.a"] + 0.7, 0.4, lambda a: cota(c, x0, x0 + L, 480 - d / 2 - 50, "L" if q < 0.5 else "2L", a))
        E.frase(c, t, C["s01.b"], [("R", "g", 120, TINTA), ("dobra?", "i", 120)], XE, 760, passo=0.2)
        if t >= C["s01.c"]:
            E.risco(c, XE + 120, 790, XE + 520, 690, t, C["s01.c"] + 0.1, largura=12)
        E.frase(c, t, C["s01.c"] + 0.3, [("não:", "i", 80), ("fica", "i", 80)], XE + 640, 760, passo=0.14)
        bola_txt(c, t, C["s01.c"] + 0.8, "×4", 1560, 730, 130, 110)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("o que muda o", "i", 88) + [("R", "g", 88, COR)], XE, 280, passo=0.14)
    for i, (k, s) in enumerate((("s02.b", "comprimento"), ("s02.c", "espessura"), ("s02.d", "material"))):
        y = 450 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84, TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def resistor(a, x, y):
        F.resistor(c, t, C["s03.b"] + 0.6, (x - 130, y + 10), (x + 110, y + 10))

    lembrete(c, t, C, "s03", (("s03.b", "a resistência, em ohm:", "R  (Ω)", None),
                              ("s03.c", "ler uma fórmula:", "em cima direto, embaixo inverso", None)), (resistor, None))


# ---------------- a ideia: o corredor ----------------
def corredor(c, x, cy, L, w, a=1.0, piso=None):
    """corredor visto de cima: piso, duas paredes e pessoas (bolinhas) espalhadas"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, cy - w / 2, L, w), M.paint(piso or "#E6E2DA", a))
    for y in (cy - w / 2, cy + w / 2):
        M.line(c, x, y, x + L, y, TINTA, a, 8)
    k = 0
    for i in range(int(L // 58)):
        for j in range(max(1, int(w // 62))):
            k += 1
            dx = (math.sin(k * 12.9898) * 43758.5453) % 1
            dy = (math.sin(k * 78.233) * 12345.678) % 1
            px = x + 30 + i * 58 + dx * 18
            py = cy - w / 2 + 31 + j * 62 + dy * 14
            if px < x + L - 18 and py < cy + w / 2 - 16:
                c.drawCircle(px, py, 14, M.paint(TINTA2, a * 0.85))


def b_ideia(c, t, C, b):
    E.frase(c, t, C["s04"], ps("do que depende o", "i", 80) + [("R", "g", 80, COR), ("de", "i", 80), ("um", "i", 80), ("fio?", "i", 80)],
            XE, 200, passo=0.12)
    qL = ease_io(prog(t, C["s04.b"], 0.9))
    qw = ease_io(prog(t, C["s04.c"], 0.9))
    qp = ease_io(prog(t, C["s04.d"], 0.7))
    L, w = lerp(560, 860, qL), lerp(130, 270, qw)
    piso = E.mix("#E6E2DA", "#C9A27A", qp)
    E.foco(c, t, C["s04.a"], 0.6, lambda a: corredor(c, 930, 520, L, w, a, piso))
    E.frase(c, t, C["s04.a"], [("corredor", "g", 70, TINTA)], XE, 400)
    E.frase(c, t, C["s04.b"], [("mais", "i", 60), ("comprido", "g", 60), ("→", "g", 60, TINTA2), ("difícil", "g", 60, ERRADO)], XE, 760, passo=0.12)
    E.frase(c, t, C["s04.c"], [("mais", "i", 60), ("largo", "g", 60), ("→", "g", 60, TINTA2), ("fácil", "g", 60, CERTO)], XE, 870, passo=0.12)
    E.frase(c, t, C["s04.d"], [("o", "i", 60), ("piso", "g", 60), ("=", "g", 60, TINTA2), ("o", "i", 60), ("material", "g", 60, COR)], XE, 980, passo=0.12)
    if t >= C["s04.b"]:
        E.foco(c, t, C["s04.b"] + 0.5, 0.4, lambda a: cota(c, 930, 930 + L, 520 - w / 2 - 50, "comprimento", a, size=44))
    if t >= C["s04.c"]:
        E.foco(c, t, C["s04.c"] + 0.5, 0.4, lambda a: (M.line(c, 880, 520 - w / 2, 880, 520 + w / 2, TINTA2, a, 4),
                                                       E.escreve(c, "largura", 650, 535, 44, "i", TINTA2, a)))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s05():
        F.formula_legenda(c, t, C["s05.a"], "R = ρ · f{L}{A}", [("R", "resistência", "Ω"), ("L", "comprimento", "m"),
                                                               ("A", "área do corte", "m^2"), ("ρ", "resistividade", "Ω · m")],
                          XE, 330, size=140, tl=[C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]], size_l=56, dy=96)
        E.frase(c, t, C["s05"], ps("segunda lei de Ohm", "i", 64, TINTA2), XE, 150, passo=0.12)
        x0, L, d = 1060, 600, 120
        E.foco(c, t, C["s05.a"] + 0.6, 0.5, lambda a: fio_cobre(c, x0, 380, L, d, a), blur=0)
        E.foco(c, t, C["s05.c"], 0.4, lambda a: cota(c, x0, x0 + L, 260, "L", a, cor=COR, size=60))
        if t >= C["s05.d"]:
            q = ep(t, C["s05.d"], 0.5)
            M.line(c, x0 + L, 380, 1560, 620, TINTA2, q, 3, dash=E.TRACO)
            corte_zoom(c, 1560, 700, 110 * ease_back(prog(t, C["s05.d"], 0.6)), q)
            E.foco(c, t, C["s05.d"] + 0.5, 0.4, lambda a: E.escreve(c, "o corte", 1700, 720, 46, "i", TINTA2, a))
        E.foco(c, t, C["s05.e"] + 0.4, 0.4, lambda a: E.pilula(c, "depende do material", 1330, 940, 44, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("a unidade de", "i", 80) + [("ρ", "g", 80, COR)], XE, 230, passo=0.12)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: E.formula(c, "Ω · m", XE + 580, 230, 84, "g", F.UNID, a))
    # Ω·m · m / m² = Ω, com os metros riscados
    x, y, s = 420, 560, 110
    w1 = E.formula(None, "Ω · m · ", 0, 0, s, "g", a=0)
    wf = E.formula(None, "f{m}{m^2}", 0, 0, s, "g", a=0)
    E.formula_em(c, t, C["s06.b"], "Ω · m · f{m}{m^2}", x, y, s, "g", TINTA)
    wom = E.formula(None, "Ω · ", 0, 0, s, "g", a=0)
    wm = E.formula(None, "m", 0, 0, s, "g", a=0)
    if t >= C["s06.c"]:
        M.line(c, x + wom - 4, y + 10, x + wom + wm + 4, y - s * 0.7, E.COR, 1.0, 9, progress=ep(t, C["s06.c"], 0.35))
        M.line(c, x + w1 - 4, y + s * 0.95, x + w1 + wf + 4, y - s * 0.75, E.COR, 1.0, 9, progress=ep(t, C["s06.c"] + 0.25, 0.4))
    E.foco(c, t, C["s06.c"] + 0.7, 0.5, lambda a: E.formula(c, "= Ω", x + w1 + wf + 50, y, s, "g", COR, a))
    E.foco(c, t, C["s06.c"] + 0.4, 0.4, lambda a: E.escreve(c, "os metros cortam", x + 40, y + 200, 52, "i", TINTA2, a))
    E.foco(c, t, C["s06.d"], 0.6, lambda a: fio_cobre(c, 1100, 850, 640, 80, a), blur=0)
    E.frase(c, t, C["s06.d"] + 0.2, [("cobre:", "g", 60, COBRE), ("ρ", "g", 60, COR), ("baixa", "i", 64)], 1100, 760, passo=0.12)
    E.frase(c, t, lerp(C["s06.d"], C["s06.end"], 0.55), ps("vai nos fios da casa", "i", 56, TINTA2), 1100, 970, passo=0.1)


# ---------------- uma mudança de cada vez ----------------
def b_efeitos(c, t, C, b):
    def s07():
        linhas = ((300, "s07.a", "s07.b", [("L", "g", 66, COR), ("em", "i", 66), ("cima:", "i", 66), ("direto", "g", 62)], "R × 2", False),
                  (580, "s07.c", "s07.d", [("A", "g", 66, COR), ("embaixo:", "i", 66), ("inverso", "g", 62)], "R ÷ 2", True),
                  (860, "s07.e", "s07.f", [("ρ", "g", 66, COR), ("o", "i", 66), ("material", "g", 62)], "R × 3", False))
        for y, k1, k2, partes, res, menos in linhas:
            E.frase(c, t, C[k1], partes, XE, y + 20, passo=0.12)
            E.foco(c, t, C[k2], 0.4, lambda a, y=y, res=res, menos=menos: E.pilula(c, res, 1740, y, 50, "g", fundo=F.NEG if menos else E.COR, a=a))
        # comprimento
        q = ease_io(prog(t, C["s07.b"] + 0.2, 0.8))
        E.foco(c, t, C["s07.a"] + 0.3, 0.5, lambda a: fio_cobre(c, 900, 300, lerp(300, 600, q), 60, a), blur=0)
        E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.escreve(c, "L × 2", 900, 240, 44, "b", TINTA2, a))
        # área
        q = ease_io(prog(t, C["s07.d"] + 0.2, 0.8))
        E.foco(c, t, C["s07.c"] + 0.3, 0.5, lambda a: fio_cobre(c, 900, 580, 450, lerp(60, 85, q), a), blur=0)
        E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: E.escreve(c, "A × 2", 900, 500, 44, "b", TINTA2, a))
        # material
        q = ease_io(prog(t, C["s07.f"], 0.8))
        E.foco(c, t, C["s07.e"] + 0.3, 0.5, lambda a: fio_cobre(c, 900, 860, 450, 60, a, E.mix(COBRE, NICROMO, q)), blur=0)
        E.foco(c, t, C["s07.f"] + 0.6, 0.4, lambda a: E.escreve(c, "ρ × 3", 900, 800, 44, "b", TINTA2, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], ps("um exemplo", "i", 76, TINTA2), XE, 200)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: F.medida(c, 4, "Ω", XE, 360, 130, TINTA, a))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: fio_cobre(c, 640, 320, 300, 60, a), blur=0)
    E.foco(c, t, C["s08.b"], 0.6, lambda a: fio_cobre(c, 1000, 320, 820, lerp(60, 85, ep(t, C["s08.c"], 0.6)), a), blur=0)
    fator(c, t, C["s08.b"] + 0.3, "L × 3", 1200, 440, 46)
    fator(c, t, C["s08.c"] + 0.3, "A × 2", 1560, 440, 46)
    estados = [(C["s08.d"], "4 × 3"), (C["s08.e"], "4 × 3 ÷ 2"), (C["s08.f"], "12 ÷ 2")]
    troca(c, t, estados, lambda s, a: E.formula(c, s, 640, 720, 120, "g", TINTA, a))
    E.saida(c, t, C["s08.f"] - 0.1, lambda: (E.foco(c, t, C["s08.d"] + 0.3, 0.4, lambda a: E.escreve(c, "comprimento", 700, 820, 48, "i", TINTA2, a)),
                                             E.foco(c, t, C["s08.e"] + 0.3, 0.4, lambda a: E.escreve(c, "área", 1010, 820, 48, "i", TINTA2, a))))
    bola_txt(c, t, C["s08.g"], "6 Ω", 1500, 730, 130, 84)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    def s09():
        E.frase(c, t, C["s09.a"], [("espessura", "g", 70), ("=", "g", 70, TINTA2), ("diâmetro", "g", 70, COR)], XE, 370, passo=0.15)
        E.foco(c, t, C["s09.a"] + 1.0, 0.5, lambda a: E.formula(c, "≠ área", XE + 830, 370, 70, "g", ERRADO, a))
        E.foco(c, t, C["s09.b"], 0.5, lambda a: corte_zoom(c, 520, 640, 70, a, rot=None))
        E.foco(c, t, C["s09.b"] + 0.6, 0.5, lambda a: corte_zoom(c, 900, 640, 140, a, rot=None))
        E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: cota(c, 450, 590, 520, "d", a, size=48))
        E.foco(c, t, C["s09.b"] + 0.9, 0.4, lambda a: cota(c, 760, 1040, 460, "2d", a, size=48))
        E.frase(c, t, C["s09.c"], [("R", "g", 90), ("÷ 2", "g", 90, ERRADO), ("?", "g", 90, ERRADO)], 1300, 680, passo=0.15)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], ps("a área vai com o", "i", 66) + [("quadrado", "g", 62, COR)] + ps("do diâmetro", "i", 66), XE, 330, passo=0.1)
    # quadrado: lado dobrou, área vezes quatro
    x0, y0, l = 260, 470, 130
    E.foco(c, t, C["s10.b"], 0.5, lambda a: M.rrect(c, x0, y0, l, l, 4, E.COR, a))
    q = ep(t, C["s10.b"] + 0.8, 0.5)
    if q > 0:
        for i in range(2):
            for j in range(2):
                if i or j:
                    M.rrect(c, x0 + 220 + i * l, y0 + j * l - l / 2, l - 6, l - 6, 4, E.mix(E.COR, BR, 0.3), q)
        M.rrect(c, x0 + 220, y0 - l / 2, l - 6, l - 6, 4, E.COR, q)
        E.escreve(c, "lado × 2 → área × 4", x0, y0 + 280, 48, "b", TINTA2, q)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: corte_zoom(c, 1050, 620, 60, a, rot=None))
    E.foco(c, t, C["s10.c"] + 0.3, 0.5, lambda a: corte_zoom(c, 1330, 620, 120, a, rot=None))
    fator(c, t, C["s10.c"] + 0.8, "d × 2  →  A × 4", 1220, 810, 46)
    E.frase(c, t, C["s10.d"], [("R", "g", 90), ("÷ 4", "g", 90, CERTO)], 1560, 970, passo=0.15)
    E.foco(c, t, C["s10.d"] + 0.6, 0.4, lambda a: E.formula(c, "÷ 2", 1200, 970, 80, "g", ERRADO, a))
    if t >= C["s10.d"] + 1.0:
        E.risco(c, 1185, 990, 1330, 910, t, C["s10.d"] + 1.0, largura=10)
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "a área do círculo: outra aula", 520, 970, 40, "b", fundo=TINTA2, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s11():
        E.frase(c, t, C["s11"], ps("o atalho do fio", "i", 80, CLARO) + [("esticado", "g", 80, BR)], W / 2, 180, "center", 0.12)
        E.frase(c, t, C["s11.a"], ps("esticar não cria cobre novo", "i", 60, CLARO), W / 2, 300, "center", 0.1)
        q = ease_io(prog(t, C["s11.b"], 1.4))
        L, d = lerp(500, 1000, q), lerp(120, 60, q)
        E.foco(c, t, C["s11.a"] + 0.4, 0.5, lambda a: fio_cobre(c, W / 2 - L / 2, 500, L, d, a), blur=0)
        fator(c, t, C["s11.b"] + 0.4, "L × 2", W / 2 - 300, 650, 50)
        fator(c, t, C["s11.c"], "A ÷ 2", W / 2 + 300, 650, 50)
        E.frase(c, t, C["s11.d"], [("R", "g", 84, BR), ("×", "g", 84, CLARO), ("2", "g", 84, BR), ("×", "g", 84, CLARO), ("2", "g", 84, BR)],
                W / 2 - 120, 860, "center", 0.25)
        bola_txt(c, t, C["s11.e"], "×4", W / 2 + 330, 830, 110, 90)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], ps("esticou", "i", 84, CLARO) + [("n", "g", 84, BR)] + ps("vezes:", "i", 84, CLARO), W / 2 - 200, 260, "center", 0.12)
    E.foco(c, t, C["s12.a"] + 1.0, 0.5, lambda a: (E.bola(c, W / 2 + 420, 230, 120, a=a), E.formula(c, "R × n^2", W / 2 + 420, 262, 70, "g", BR, a, "center")))
    E.frase(c, t, C["s12.b"], [("3", "g", 76, BR), ("vezes", "i", 76, CLARO), ("→", "g", 76, CLARO), ("× 9", "g", 76, BR)], W / 2, 480, "center", 0.15)
    E.frase(c, t, C["s12.c"], ps("mesma quantidade de cobre:", "i", 58, CLARO), W / 2, 640, "center", 0.1)
    E.frase(c, t, C["s12.c"] + 1.4, [("L", "g", 60, BR), ("multiplica,", "i", 60, CLARO), ("A", "g", 60, BR), ("divide", "i", 60, CLARO)], W / 2, 740, "center", 0.12)
    E.frase(c, t, C["s12.d"], [("não", "g", 58, ERRADO), ("vale:", "i", 60, CLARO)] + ps("fio trocado por outro", "i", 60, CLARO), W / 2, 920, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s13.a"], [("fio", "i", 76)], XE, 360)
    E.foco(c, t, C["s13.a"] + 0.3, 0.5, lambda a: F.medida(c, 12, "Ω", XE + 160, 360, 100, COR, a))
    E.frase(c, t, C["s13.a"] + 1.0, ps("mesmo material", "i", 60, TINTA2), XE, 450)
    E.frase(c, t, C["s13.b"], [("comprimento", "g", 66), ("× 3", "g", 66, COR)], XE, 590, passo=0.15)
    E.frase(c, t, C["s13.c"], [("diâmetro", "g", 66), ("× 2", "g", 66, COR)], XE, 700, passo=0.15)
    E.frase(c, t, C["s13.d"], [("R", "g", 80), ("novo", "i", 84), ("=", "g", 80, TINTA2), ("?", "g", 84, COR)], XE, 860, passo=0.15)
    if t < C["s14"]:
        E.foco(c, t, C["s13.a"], 0.6, lambda a: fio_cobre(c, 1080, 400, 300, 50, a), blur=0)
        E.foco(c, t, C["s13.b"], 0.6, lambda a: fio_cobre(c, 1080, 620, 760, lerp(50, 100, ep(t, C["s13.c"], 0.6)), a), blur=0)
    else:
        E.relogio(c, t, C["s14.a"], cx=1460, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15.a"], [("L", "g", 70, COR), ("× 3", "g", 70), ("→", "g", 70, TINTA2), ("R", "g", 70), ("× 3", "g", 70, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s15.b"], [("d", "g", 70, COR), ("× 2", "g", 70), ("→", "g", 70, TINTA2), ("A", "g", 70), ("× 4", "g", 70), ("→", "g", 70, TINTA2),
                               ("R", "g", 70), ("÷ 4", "g", 70, F.NEG)], XE, 400, passo=0.12)
    troca(c, t, [(C["s15.c"], "12 × 3 = 36"), (C["s15.d"] - 0.6, "36 ÷ 4")], lambda s, a: E.formula(c, s, XE, 620, 110, "g", TINTA, a))
    bola_txt(c, t, C["s15.d"], "9 Ω", 1250, 600, 130, 84, CERTO)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: F.medida(c, 18, "Ω", XE, 900, 90, ERRADO, a))
    if t >= C["s15.e"] + 0.5:
        E.risco(c, XE - 10, 920, XE + 230, 830, t, C["s15.e"] + 0.5, largura=10)
    E.frase(c, t, C["s15.e"] + 0.8, ps("dividiu só por 2: a pegadinha", "i", 56, TINTA2), XE + 300, 900, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        E.formula_em(c, t, C["s16.a"], "R = ρ · f{L}{A}", W / 2, 360, 110, "g", TINTA, "center")
        itens = (("s16.b", [("L", "g", 64, COR), ("maior", "i", 66), ("→", "g", 64, TINTA2), ("R", "g", 64), ("maior", "i", 66)]),
                 ("s16.c", [("fio", "i", 66), ("mais", "i", 66), ("grosso", "g", 64, COR), ("→", "g", 64, TINTA2), ("R", "g", 64), ("menor", "i", 66)]),
                 ("s16.d", [("material", "g", 64, COR), ("→", "g", 64, TINTA2), ("ρ", "g", 64)]),
                 ("s16.e", [("d", "g", 64, COR), ("× 2", "g", 64), ("→", "g", 64, TINTA2), ("A", "g", 64), ("× 4", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            x, y = (330, 1050)[i % 2], 580 + (i // 2) * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, x=x, y=y: (E.bola(c, x - 70, y - 24, 46, a=a), centro(c, str(i + 1), x - 70, y - 2, 54, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, x, y, passo=0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s17.a"], [("resistores", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s17.a"] + 0.5, [("em", "i", 110), ("série", "g", 110, COR)], XE, 540)
    # três resistores um atrás do outro
    y, x0 = 760, 260
    F.fio(c, t, C["s17.a"] + 0.6, [(x0, y), (x0 + 60, y)])
    for i in range(3):
        F.resistor(c, t, C["s17.a"] + 0.7 + 0.25 * i, (x0 + 60 + 230 * i, y), (x0 + 290 + 230 * i, y))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "R total = R₁ + R₂ + R₃", x0, y + 160, 64, "b", TINTA2, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, formula=b_formula, efeitos=b_efeitos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
