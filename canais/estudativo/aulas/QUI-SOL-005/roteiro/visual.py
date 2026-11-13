"""Visual — Estudativo · QUI-SOL-005: diluição e mistura de soluções.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py). Diluir = o mesmo número de bolinhas de soluto num béquer que enche: elas se espalham.
C₁V₁ = C₂V₂ com "antes" e "depois" embaixo de cada lado. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-005_diluicao_mistura.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("diluir", "preparar", "mistura", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula
assert 0.5 * 100 == 50 and 50 / 500 == 0.1 and 500 - 100 == 400
assert 0.5 * 500 == 250 and 250 / 2 == 125 and 500 - 125 == 375
assert round(0.5 * 0.2 + 1.0 * 0.3, 9) == 0.4 and round(0.4 / 0.5, 9) == 0.8 and 0.5 + 1.0 == 1.5
assert 0.5 / 5 == 0.1 and 0.8 / 4 == 0.2 and round(0.2 * 1 + 0.6 * 3, 9) == 2.0 and 2.0 / 4 == 0.5 and (0.2 + 0.6) / 2 == 0.4


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


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def copo(c, t, t0, cx, yb, w, h, nivel, n, te=None, semente=3, rot=None, sub=None):
    """béquer com n bolinhas de soluto que se espalham pelo líquido (n fixo = o soluto não muda)"""
    Q.bequer(c, t, t0, cx, yb, w, h, nivel, Q.AGUA, te=te, graduacao=False,
             particulas=dict(n=n, estado="gas", tipos=[(E.COR, 1.0)], r=8, semente=semente))
    if rot:
        rotulo(c, t, t0 + 0.3, rot, cx, yb + 70, 50, TINTA, "b")
    if sub:
        rotulo(c, t, t0 + 0.5, sub, cx, yb + 130, 46, COR, "b")


def equacao(c, t, t0, cx, y, size=120, escuro=False, antes=None, depois=None):
    """C₁·V₁ = C₂·V₂ com 'antes' e 'depois' embaixo"""
    tinta = BR if escuro else TINTA
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, "C₁·V₁ = C₂·V₂", cx, y, size, "g", tinta, a, "center"))
    w = E.formula(None, "C₁·V₁ = C₂·V₂", 0, 0, size, a=0)
    for ti, s, dx, f in ((antes, "antes", -w * 0.3, TINTA if not escuro else "#3A3B42"), (depois, "depois", w * 0.3, E.COR)):
        if ti is not None:
            pilula_em(c, t, ti, s, cx + dx, y + size * 0.75, size * 0.36, f)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cx, yb, w, h = 1360, 900, 420, 600
        nivel = lerp(0.18, 0.88, ease_io(prog(t, C["s01.b"], 2.4)))
        Q.bequer(c, t, C["s01.a"], cx, yb, w, h, nivel, Q.AGUA, particulas=dict(n=16, estado="gas", tipos=[(E.COR, 1.0)], r=9, semente=5))
        E.frase(c, t, C["s01.a"], [("100 mL", "g", 70, COR)] + ps("com", "i", 74) + [("0,5 mol/L", "g", 70, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("complete com água até", "i", 64) + [("500 mL", "g", 62, COR)], XE, 380, passo=0.1)
        # água entrando
        if C["s01.b"] <= t < C["s01.b"] + 2.4:
            M.line(c, cx + 60, yb - h - 80, cx + 60, yb - h * nivel, "#7FC2E2", 0.8, 14)
        E.frase(c, t, C["s01.c"], ps("nenhum grão de sal entrou ou saiu", "i", 58, TINTA2), XE, 500, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("a concentração cai para", "i", 64) + [("quanto?", "g", 60, COR)], XE, 660, passo=0.1)
        bola_txt(c, t, C["s01.e"], "0,1 mol/L", XE + 140, 820, 130, 46)
        E.frase(c, t, C["s01.e"] + 1.2, ps("numa linha", "i", 60, TINTA2), XE + 320, 840, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("diluir", "g", 70, COR), ("com", "i", 74), ("uma", "i", 74), ("fórmula", "i", 74)]),
                 (C["s02.c"], [("misturar", "g", 70, COR), ("duas", "i", 74), ("soluções", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.formula_em(c, t, C["s03.a"], "M = f{mols}{V}", XE, 380, 100, "g", TINTA)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.formula(c, "mols = M · V", XE, 620, 100, "g", COR, a))
    p = ep(t, C["s03.b"] - 0.2, 0.5)
    if p > 0:
        M.arrow(c, XE + 120, 460, XE + 120, 540, E.COR, p, 6, 22, ease_io(p))
    E.frase(c, t, C["s03.c"], ps("isolar a letra: a mesma conta", "i", 60) + [("dos dois lados", "g", 56, COR)], XE, 830, passo=0.1)
    E.foco(c, t, C["s03.c"] + 1.6, 0.5, lambda a: E.formula(c, "2x = 10 → x = 5", 1300, 620, 80, "g", TINTA2, a))


# ---------------- diluição ----------------
def b_diluir(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("diluir", "g", 110, COR)], XE, 300)
            E.frase(c, t, C["s04.a"] + 0.6, ps("é acrescentar solvente", "i", 70), XE, 410, passo=0.12)
            nivel = lerp(0.3, 0.85, ease_io(prog(t, C["s04.b"], 2.0)))
            Q.bequer(c, t, C["s04"], 1360, 920, 420, 600, nivel, Q.AGUA, particulas=dict(n=16, estado="gas", tipos=[(E.COR, 1.0)], r=9, semente=5))
            E.frase(c, t, C["s04.b"], [("volume", "i", 66), ("cresce", "g", 62, COR)], XE, 580, passo=0.12)
            E.frase(c, t, C["s04.c"], [("soluto:", "i", 66), ("o", "i", 66), ("mesmo", "g", 62, COR)], XE, 680, passo=0.12)
            rotulo(c, t, C["s04.d"], "16 bolinhas antes, 16 depois", 1360, 1010, 46, TINTA)
            E.frase(c, t, C["s04.e"], ps("a concentração", "i", 66) + [("cai", "g", 62, ERRADO)], XE, 820, passo=0.12)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("soluto antes:", "i", 60, TINTA2), 260, 250)
            E.formula_em(c, t, C["s05.a"] + 0.6, "C₁ · V₁", 260, 380, 110, "g", TINTA)
            E.frase(c, t, C["s05.b"], ps("soluto depois:", "i", 60, TINTA2), 1100, 250)
            E.formula_em(c, t, C["s05.b"] + 0.6, "C₂ · V₂", 1100, 380, 110, "g", COR)
            rotulo(c, t, C["s05.a"] + 1.0, "concentração e volume iniciais", 470, 470, 40)
            rotulo(c, t, C["s05.b"] + 1.0, "concentração e volume finais", 1310, 470, 40)
            pilula_em(c, t, C["s05.c"], "o soluto não mudou: as duas contas são iguais", W / 2, 620, 46, TINTA, "b")
            equacao(c, t, C["s05.d"], W / 2, 860, 150, antes=C["s05.d"] + 0.5, depois=C["s05.d"] + 0.7)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            equacao(c, t, C["s06"], W / 2, 230, 100)
            E.formula_em(c, t, C["s06.a"], "0,5 × 100 = 50", 260, 450, 90, "g", TINTA)
            E.formula_em(c, t, C["s06.b"], "= C₂ × 500", 1000, 450, 90, "g", COR)
            E.formula_em(c, t, C["s06.c"], "C₂ = f{50}{500}", 260, 690, 90, "g", TINTA2)
            rotulo(c, t, C["s06.c"] + 0.4, "÷ 500 dos dois lados", 1040, 680, 46)
            bola_txt(c, t, C["s06.d"], "0,1 mol/L", 1500, 840, 130, 46)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    E.frase(c, t, C["s07.a"], ps("os volumes podem ficar em", "i", 66) + [("mL", "g", 62, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s07.a"] + 1.6, ps("desde que os dois estejam na mesma unidade", "i", 58, TINTA2), XE, 400, passo=0.1)
    E.frase(c, t, C["s07.b"], ps("a concentração: em", "i", 64) + [("mol/L", "g", 60, COR), ("ou", "i", 64), ("g/L", "g", 60, COR)], XE, 600, passo=0.12)
    E.frase(c, t, C["s07.b"] + 2.0, [("só", "i", 64), ("não", "g", 60, ERRADO), ("misture", "i", 64), ("as", "i", 64), ("duas", "i", 64)], XE, 700, passo=0.12)
    equacao(c, t, C["s07"], 1400, 920, 90)


# ---------------- preparar ----------------
def b_preparar(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("a fórmula ensina a", "i", 66) + [("preparar", "g", 62, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s08.b"], ps("estoque:", "i", 60, TINTA2) + [("2 mol/L", "g", 60)], XE, 320, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("quero:", "i", 60, TINTA2) + [("500 mL", "g", 60, COR), ("de", "i", 60), ("0,5 mol/L", "g", 60, COR)], XE, 420, passo=0.1)
        E.formula_em(c, t, C["s08.d"], "2 × V₁ = 0,5 × 500 = 250", XE, 620, 84, "g", TINTA)
        E.formula_em(c, t, C["s08.e"], "V₁ = f{250}{2} =", XE, 830, 84, "g", TINTA2)
        bola_txt(c, t, C["s08.e"] + 0.8, "125 mL", XE + 720, 805, 110, 50)
        return
    copo(c, t, C["s09"], 560, 860, 300, 420, 0.7, 24, rot="estoque 2 mol/L")
    copo(c, t, C["s09.a"], 1300, 860, 380, 520, 0.25, 12, te=None, rot="125 mL do estoque", semente=7) if t < C["s09.b"] else None
    if t >= C["s09.b"]:
        nivel = lerp(0.25, 1.0 * 0.8, ease_io(prog(t, C["s09.b"], 1.8)))
        Q.bequer(c, t, C["s09.a"], 1300, 860, 380, 520, nivel, Q.AGUA, graduacao=False,
                 particulas=dict(n=12, estado="gas", tipos=[(E.COR, 1.0)], r=8, semente=7))
        rotulo(c, t, C["s09.b"] + 1.0, "completo até 500 mL", 1300, 930, 50, TINTA, "b")
        M.line(c, 1080, 860 - 520 * 0.8, 1520, 860 - 520 * 0.8, E.COR, ep(t, C["s09.b"], 0.4), 4, dash=[14, 10])
        E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: E.escreve(c, "500 mL", 1540, 860 - 520 * 0.8 + 14, 44, "b", COR, a))
    p = ep(t, C["s09.a"] + 0.3, 0.5)
    if p > 0:
        M.arrow(c, 740, 600, 1080, 600, E.COR, p, 6, 24, ease_io(p))
    E.formula_em(c, t, C["s09.c"], "500 − 125 = 375 mL de água", W / 2, 1040, 64, "g", COR, "center")


# ---------------- mistura ----------------
def b_mistura(c, t, C, b):
    xa, xb, xc = 320, 820, 1520
    copo(c, t, C["s10.a"], xa, 720, 260, 320, 0.45, 10, rot="200 mL", sub="0,5 mol/L", semente=2)
    E.foco(c, t, C["s10.b"] - 0.2, 0.4, lambda a: centro(c, "+", (xa + xb) / 2, 640, 110, "g", TINTA2, a))
    copo(c, t, C["s10.b"], xb, 720, 260, 320, 0.65, 30, rot="300 mL", sub="1 mol/L", semente=4)
    E.frase(c, t, C["s10"], ps("mesmo soluto, sem reação", "i", 60, TINTA2), XE, 180, passo=0.1)
    E.frase(c, t, C["s10.c"], ps("os", "i", 60) + [("mols", "g", 56, COR)] + ps("se somam, os", "i", 60) + [("volumes", "g", 56, COR)] + ps("também", "i", 60), XE, 280, passo=0.1)
    p = ep(t, C["s10.c"] + 1.6, 0.5)
    if p > 0:
        M.arrow(c, 1000, 600, 1290, 600, E.COR, p, 6, 24, ease_io(p))
    copo(c, t, C["s10.c"] + 1.8, xc, 720, 340, 440, 0.8, 40, rot="500 mL", semente=6)
    if t >= C["s11"]:
        E.formula_em(c, t, C["s11.a"], "0,5 × 0,2 = 0,1 mol", 100, 930, 52, "g", TINTA)
        E.formula_em(c, t, C["s11.b"], "1 × 0,3 = 0,3 mol", 640, 930, 52, "g", TINTA)
        E.formula_em(c, t, C["s11.c"], "0,1 + 0,3 = 0,4 mol", 100, 1030, 52, "g", COR)
        E.formula_em(c, t, C["s11.d"], "em 0,5 L", 640, 1030, 52, "g", TINTA2)
        E.formula_em(c, t, C["s11.e"], "f{0,4}{0,5} =", 1180, 1000, 60, "g", TINTA2)
        bola_txt(c, t, C["s11.e"] + 1.4, "0,8 mol/L", xc + 200, 965, 105, 40)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("somar as concentrações", "i", 64), XE + 440, 190, passo=0.1)
    E.formula_em(c, t, C["s12.b"], "0,5 + 1 = 1,5 mol/L", XE, 420, 100, "g", ERRADO)
    if t >= C["s12.c"]:
        E.risco(c, XE - 10, 440, XE + 960, 330, t, C["s12.c"] + 1.6, largura=12)
    E.frase(c, t, C["s12.c"], ps("mais concentrada que as duas que você juntou?", "i", 58), XE, 600, passo=0.08)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: (E.selo(c, XE + 60, 750, 50, False, a), E.escreve(c, "impossível", XE + 140, 772, 76, "g", ERRADO, a)))
    E.frase(c, t, C["s12.e"], ps("some os", "i", 70) + [("mols,", "g", 66, COR), ("não", "i", 70), ("as", "i", 70), ("concentrações", "i", 70)], XE, 950, passo=0.12)
    copo(c, t, C["s12.a"], 1560, 820, 280, 380, 0.8, 40, rot="0,8 mol/L", semente=6)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("dois atalhos de prova", "i", 70, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s13.a"], [("1", "g", 60, CLARO), ("diluição:", "g", 60, BR)] + ps("o volume cresceu quantas vezes?", "i", 62, CLARO), XE, 300, passo=0.1)
            E.frase(c, t, C["s13.b"], ps("divida a concentração pelo mesmo número", "i", 62, CLARO), XE + 60, 400, passo=0.1)
            E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "100 mL → 500 mL: × 5", XE + 60, 560, 80, "g", BR, a))
            E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "0,5 ÷ 5 = 0,1 mol/L", XE + 60, 700, 80, "g", CLARO, a))
            E.frase(c, t, C["s13.d"] + 2.4, ps("o mesmo soluto num volume 5 vezes maior", "i", 54, CLARO), XE + 60, 820, passo=0.1)
            E.frase(c, t, C["s13.e"], [("não", "g", 54, ERRADO), ("compensa:", "i", 58, CLARO)] + ps("300 mL → 700 mL: use a fórmula", "b", 52, BR), XE + 60, 950, passo=0.1)
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], [("2", "g", 60, CLARO), ("mistura:", "g", 60, BR)] + ps("o resultado fica entre as duas", "i", 62, CLARO), XE, 250, passo=0.1)
    E.frase(c, t, C["s14.b"], ps("mais perto da que tem mais volume", "i", 62, CLARO), XE + 60, 350, passo=0.1)
    x0, x1, y = 360, 1560, 600
    if t >= C["s14.c"]:
        q = ep(t, C["s14.c"], 0.5)
        M.line(c, x0, y, x1, y, BR, q, 6)
        for v, s, cor in ((0.5, "0,5", BR), (1.0, "1", BR), (0.8, "0,8", E.CLARO)):
            x = lerp(x0, x1, (v - 0.5) / 0.5)
            c.drawCircle(x, y, 18 if v == 0.8 else 14, M.paint(cor, q))
            centro(c, s, x, y + 80, 60, "g", cor, q)
        centro(c, "200 mL", x0, y - 50, 40, "b", CLARO, q)
        centro(c, "300 mL", x1, y - 50, 40, "b", CLARO, q)
    E.frase(c, t, C["s14.d"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO)] + ps("quando os solutos reagem, como ácido e base", "i", 60, CLARO), XE, 860, passo=0.1)
    pilula_em(c, t, C["s14.d"] + 2.6, "assunto da próxima aula", 1400, 960, 44, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15.a"], [("250 mL", "g", 60, COR)] + ps("de sal com", "i", 64) + [("0,8 mol/L", "g", 60, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("diluídos até", "i", 64) + [("1 L", "g", 60, COR)], XE, 390, passo=0.1)
    E.frase(c, t, C["s15.c"], [("1", "g", 56, COR)] + ps("nova concentração?", "i", 62), XE, 500, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("depois: junta com", "i", 62) + [("3 L", "g", 60, COR)] + ps("de", "i", 62) + [("0,6 mol/L", "g", 60, COR)], XE, 660, passo=0.1)
    E.frase(c, t, C["s15.e"], [("2", "g", 56, COR)] + ps("concentração final?", "i", 62), XE, 770, passo=0.1)
    if t < C["s16"]:
        copo(c, t, C["s15.a"], 1500, 800, 300, 420, 0.3, 14, semente=8)
    else:
        E.relogio(c, t, C["s16.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], [("1", "g", 56, COR)] + ps("diluição", "i", 62, TINTA2), XE, 180, passo=0.1)
    E.formula_em(c, t, C["s17.a"], "250 mL → 1000 mL: × 4", XE, 300, 72, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "0,8 ÷ 4 =", XE, 460, 72, "g", TINTA2)
    bola_txt(c, t, C["s17.b"] + 1.2, "0,2 mol/L", XE + 560, 435, 100, 38, CERTO)
    E.frase(c, t, C["s18"], [("2", "g", 56, COR)] + ps("mistura: some os mols", "i", 62, TINTA2), XE, 600, passo=0.1)
    E.formula_em(c, t, C["s18.a"], "1 L × 0,2 = 0,2 mol", XE, 710, 62, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "3 L × 0,6 = 1,8 mol", XE, 800, 62, "g", TINTA)
    E.formula_em(c, t, C["s18.c"], "f{0,2 + 1,8}{1 + 3} = f{2}{4} =", XE, 960, 66, "g", TINTA2)
    bola_txt(c, t, C["s18.d"], "0,5 mol/L", 1200, 930, 110, 40, CERTO)
    rotulo(c, t, C["s18.e"], "entre 0,2 e 0,6, mais perto de 0,6", 1480, 760, 44, TINTA, "b")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.foco(c, t, C["s19.a"], 0.5, lambda a: (E.bola(c, 300, 374, 52, a=a), centro(c, "1", 300, 396, 60, "g", BR, a)))
        equacao(c, t, C["s19.a"] + 0.2, 820, 420, 110)
        rotulo(c, t, C["s19.a"] + 1.0, "diluição: o soluto não muda", 1500, 410, 46)
        E.foco(c, t, C["s19.b"], 0.5, lambda a: (E.bola(c, 300, 724, 52, a=a), centro(c, "2", 300, 746, 60, "g", BR, a)))
        E.foco(c, t, C["s19.b"] + 0.2, 0.5, lambda a: E.formula(c, "M = f{mols somados}{volume total}", 400, 770, 80, "g", TINTA, a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("titulação", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.b"], ps("a base conhecida descobre o ácido", "i", 62), XE, 520, passo=0.1)
    Q.erlenmeyer(c, t, C["s20.b"] + 0.4, 560, 960, 300, 320, 0.4, Q.muda_cor(t, C["s20.b"] + 1.4, Q.AGUA, "#F48FB1", 0.8))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, diluir=b_diluir, preparar=b_preparar, mistura=b_mistura, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
