"""Visual — Estudativo · QUI-AMB-006: química verde e economia atômica.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(cabeçalho de QUI-AMB-001/roteiro/visual.py). Nesta aula:
- BARRA DE MASSA (barra_massa): a massa dos reagentes é uma barra; a parte que vira o produto desejado enche na cor da
  matéria e a que sai como subproduto fica em cinza riscado. A porcentagem da economia atômica vai na esfera.
- Equação com as massas embaixo de cada espécie (Q.equacao + Q.sob_termos); o produto desejado na cor da matéria.
- PRINCÍPIOS = cartões numerados com um ícone simples cada.
Peças candidatas ao kit: barra_massa (economia atômica), cartao_principio.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Química e Ambiente")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-AMB-006_quimica_verde_economia_atomica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("verde", "conta", "compara", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MASSA = {"H": 1, "C": 12, "N": 14, "O": 16, "Ca": 40, "Fe": 56}


def mm(f):
    return sum(MASSA[k] * n for k, n in Q.contar(f).items())


AMONIA, CAL, FERRO = "N2 + 3 H2 -> 2 NH3", "CaCO3 -> CaO + CO2", "Fe2O3 + 3 CO -> 2 Fe + 3 CO2"
for e in (AMONIA, CAL, FERRO):
    r, p = Q.lados(e)
    assert r == p, e
assert mm("N2") + 3 * mm("H2") == 34 == 2 * mm("NH3")
assert mm("CaCO3") == 100 and mm("CaO") == 56 and mm("CO2") == 44
assert mm("Fe2O3") == 160 and mm("CO") == 28 and 160 + 3 * 28 == 244 and 2 * mm("Fe") == 112
assert round(112 / 244 * 100) == 46 and 244 / 2 == 122 and round(112 / 188 * 100) == 60  # o erro: esquecer o 3


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, r=44):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, r, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def riscado(c, t, t0, s, x, y, size=56, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, est, ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, est, size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def barra_massa(c, t, t0, x, y, w, h, total, produto, t1, rot_p="produto", rot_s="subproduto"):
    """barra da massa dos reagentes; a partir de t1 a parte do produto enche na cor da matéria e o resto fica cinza"""
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    M.rrect(c, x, y, w, h, h / 2, "#E3E5E8", q)
    E.escreve(c, f"reagentes: {E._num(total)} g", x, y - 24, 44, "b", TINTA2, q)
    if t >= t1:
        p = ease_io(prog(t, t1, 1.0))
        wp = w * produto / total
        M.rrect(c, x, y, max(h, wp * p), h, h / 2, E.COR, 1)
        if produto < total:
            E.foco(c, t, t1 + 1.0, 0.4, lambda a: (c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + wp + 6, y, w - wp - 6, h), h / 2, h / 2), M.paint(CINZA, a, stroke=4)),
                                                  E.escreve(c, rot_s, x + wp + 24, y + h + 50, 42, "b", CINZA, a)))
        E.foco(c, t, t1 + 0.6, 0.4, lambda a: E.escreve(c, rot_p, x, y + h + 50, 42, "b", COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("rendimento", "g", 90), ("100%", "g", 90, CERTO)], XE, 280, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("e quase metade da massa vai para o lixo", "i", 64), XE, 420, passo=0.1)
        barra_massa(c, t, C["s01.b"], XE, 560, 1500, 90, 100, 56, C["s01.b"] + 0.6, "o que você queria", "jogado fora")
        E.frase(c, t, C["s01.c"], ps("a química verde criou outra conta:", "i", 60, TINTA2), XE, 860, passo=0.08)
        E.frase(c, t, C["s01.d"], [("economia", "g", 90, COR), ("atômica", "g", 90, COR)], XE, 990, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("os", "i", 66), ("princípios", "g", 62, COR), ("da", "i", 66), ("química", "i", 66), ("verde", "g", 62, COR)]),
                 (C["s02.c"], [("calcular", "i", 66), ("a", "i", 66), ("economia", "g", 62), ("atômica", "g", 62)]),
                 (C["s02.d"], [("qual", "i", 66), ("caminho", "g", 62, COR), ("desperdiça", "i", 66), ("menos", "i", 66)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("massa", "g", 66, COR), ("molar:", "g", 66, COR)] + ps("soma das massas dos átomos", "i", 64), XE, 380, passo=0.1)
    Q.formula_em(c, t, C["s03.a"] + 1.4, "NH3", XE + 80, 470, 60, TINTA2)
    E.formula_em(c, t, C["s03.a"] + 1.4, ": 14 + 3 · 1 = 17 g/mol", XE + 220, 470, 60, "g", TINTA2)
    E.frase(c, t, C["s03.b"], [("conservação:", "g", 66, COR)] + ps("reagentes e produtos somam a mesma massa", "i", 60), XE, 620, passo=0.08)
    E.frase(c, t, C["s03.c"], [("porcentagem", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("parte dividida pelo total, vezes cem", "i", 60), XE, 800, passo=0.08)


# ---------------- química verde ----------------
def icone(c, k, cx, cy, a):
    if k == 0:  # prevenir: lixeira riscada
        M.rrect(c, cx - 30, cy - 30, 60, 70, 8, "#9AA0A8", a); M.line(c, cx - 50, cy + 50, cx + 50, cy - 50, ERRADO, a, 8)
    elif k == 1:  # menos tóxico: caveira simplificada → bola
        E.bola(c, cx, cy, 34, "#9AA0A8", a); M.line(c, cx - 50, cy + 50, cx + 50, cy - 50, ERRADO, a, 8)
    elif k == 2:  # água como solvente
        p = skia.Path(); p.moveTo(cx, cy - 40); p.cubicTo(cx + 34, cy, cx + 30, cy + 34, cx, cy + 34); p.cubicTo(cx - 30, cy + 34, cx - 34, cy, cx, cy - 40)
        c.drawPath(p, M.paint(Q.AGUA, a)); c.drawPath(p, M.paint("#5FA8C4", a, stroke=4))
    elif k == 3:  # pouca energia: termômetro baixo
        M.rrect(c, cx - 12, cy - 44, 24, 80, 12, BR, a, stroke=3, stroke_color=Q.VIDRO); E.bola(c, cx, cy + 40, 20, "#6FA8FF", a)
    elif k == 4:  # renovável: folha
        p = skia.Path(); p.moveTo(cx - 34, cy + 30); p.cubicTo(cx - 30, cy - 30, cx + 20, cy - 40, cx + 36, cy - 36); p.cubicTo(cx + 30, cy + 10, cx, cy + 36, cx - 34, cy + 30)
        c.drawPath(p, M.paint(E.COR, a))
    else:  # catalisador: engrenagem → anel
        c.drawCircle(cx, cy, 30, M.paint(TINTA2, a, stroke=12)); E.bola(c, cx, cy, 10, TINTA2, a)


def b_verde(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("química", "g", 100, COR), ("verde", "g", 100, COR)], XE, 300, passo=0.14)
        E.frase(c, t, C["s04.a"] + 0.8, ps("planejar a reação para não sujar desde o começo", "i", 58), XE, 420, passo=0.08)
        E.frase(c, t, C["s04.b"], ps("a ideia principal:", "i", 60, TINTA2), XE, 620, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("melhor não gerar o resíduo do que tratá-lo depois", "i", 64), XE, 740, passo=0.08)
        return
    E.frase(c, t, C["s05"], [("12", "g", 70, COR)] + ps("princípios; a prova cobra estes:", "i", 60, TINTA2), XE, 170, passo=0.1)
    itens = (("s05.a", "prevenir o resíduo"), ("s05.b", "menos tóxicas"), ("s05.c", "água como solvente"),
             ("s05.d", "menos energia"), ("s05.e", "matéria-prima renovável"), ("s05.f", "catalisadores"))
    for k, (key, s) in enumerate(itens):
        x, y = 160 + 560 * (k % 3), 260 + 300 * (k // 3)
        E.foco(c, t, C[key], 0.4, lambda a, x=x, y=y, k=k, s=s: (M.rrect(c, x, y, 500, 250, 26, BR, a, stroke=3, stroke_color=FIO),
                                                                icone(c, k, x + 90, y + 125, a), E.bola(c, x + 20, y + 20, 26, a=a),
                                                                centro(c, str(k + 1), x + 20, y + 33, 34, "g", BR, a),
                                                                E.escreve(c, s.split(" ", 1)[0], x + 170, y + 110, 44, "g", TINTA, a),
                                                                E.escreve(c, s.split(" ", 1)[1] if " " in s else "", x + 170, y + 170, 40, "b", TINTA2, a)))
    if t >= C["s06"]:
        E.foco(c, t, C["s06.a"], 0.4, lambda a: M.rrect(c, 160, 880, 1600, 150, 30, E.COR, 0.15 * a))
        E.frase(c, t, C["s06.a"], ps("um princípio dá para medir:", "i", 54, TINTA2), 200, 940, passo=0.08)
        E.frase(c, t, C["s06.b"], [("os", "i", 54), ("átomos", "g", 54, COR), ("dos", "i", 54), ("reagentes", "i", 54), ("no", "i", 54), ("produto", "g", 54, COR)], 200, 1005, passo=0.08)


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07"], [("economia", "g", 90, COR), ("atômica", "g", 90, COR)], W / 2, 220, "center", 0.14)
        E.formula_em(c, t, C["s07.a"], "f{massa do produto desejado}{soma das massas dos reagentes} × 100", W / 2, 520, 70, "g", TINTA, "center")
        pilula_em(c, t, C["s07.d"], "use a equação balanceada, com os coeficientes", W / 2, 800, 46, TINTA, "b")
        return
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("amônia", "g", 80, COR)], XE, 200)
        Q.equacao(c, t, C["s08.b"], AMONIA, W / 2, 400, 110, tl=[C["s08.b"] + 0.3 * k for k in range(4)], cores={"NH3": E.COR})
        Q.sob_termos(c, t, AMONIA, W / 2, 400, 110, [["28 g", "6 g", "34 g"]], tl=[C["s08.c"]])
        barra_massa(c, t, C["s08.c"], 260, 640, 1400, 90, 34, 34, C["s08.d"], "tudo vira amônia")
        E.formula_em(c, t, C["s08.e"], "34 ÷ 34 × 100 =", 1100, 930, 80, "g", TINTA, "right")
        bola_txt(c, t, C["s08.f"], "100%", 1260, 900, 90, 60, CERTO)
        return
    E.frase(c, t, C["s09.a"], [("cal", "g", 80, COR), ("virgem", "g", 80, COR)], XE, 200, passo=0.12)
    Q.equacao(c, t, C["s09.b"], CAL, W / 2, 400, 110, tl=[C["s09.b"], C["s09.b"] + 0.4, C["s09.b"] + 0.7, C["s09.b"] + 1.0], cores={"CaO": E.COR})
    Q.sob_termos(c, t, CAL, W / 2, 400, 110, [["100 g", "56 g", "44 g"]], tl=[C["s09.c"]])
    barra_massa(c, t, C["s09.c"], 260, 640, 1400, 90, 100, 56, C["s09.d"], "cal: 56 g", "CO₂: 44 g")
    E.formula_em(c, t, C["s09.e"], "56 ÷ 100 × 100 =", 1100, 930, 80, "g", TINTA, "right")
    bola_txt(c, t, C["s09.e"] + 0.8, "56%", 1260, 900, 90, 64)
    if t >= C["s10"]:
        pilula_em(c, t, C["s10.a"], "44% vira CO₂, que você não queria", 520, 1030, 40, CINZA, "b")
        pilula_em(c, t, C["s10.b"], "mesmo com rendimento de 100%", 1520, 1030, 40, TINTA, "b")


# ---------------- rendimento × economia ----------------
def b_compara(c, t, C, b):
    E.frase(c, t, C["s11"], ps("qual é a diferença?", "i", 64, TINTA2), XE, 180, passo=0.1)
    for k, (key, titulo, linha, cor) in enumerate((("s11.a", "rendimento", "obtido ÷ o que a equação promete", TINTA),
                                                   ("s11.b", "economia atômica", "quanto da massa pode virar o produto", COR))):
        x = 160 + 820 * k
        E.foco(c, t, C[key], 0.4, lambda a, x=x, titulo=titulo, linha=linha, cor=cor: (M.rrect(c, x, 280, 760, 520, 30, BR, a, stroke=3, stroke_color=FIO),
                                                                                      E.escreve(c, titulo, x + 40, 380, 64, "g", cor, a),
                                                                                      E.escreve(c, linha, x + 40, 470, 40, "b", TINTA2, a)))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "olha a própria equação", 1020, 560, 46, "i", TINTA, a))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "a reação foi bem feita?", 200, 700, 54, "g", TINTA, a))
    E.foco(c, t, C["s11.e"], 0.4, lambda a: E.escreve(c, "o caminho é bom?", 1020, 700, 54, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s12.a"], "rendimento de 100% = processo verde", XE, 340, 64, "b")
    E.frase(c, t, C["s12.b"], ps("a cal acabou de mostrar que não:", "i", 60), XE, 500, passo=0.1)
    barra_massa(c, t, C["s12.c"], 260, 640, 1400, 90, 100, 56, C["s12.c"] + 0.3, "cal: 56%", "CO₂: 44%")
    E.foco(c, t, C["s12.c"] + 1.4, 0.4, lambda a: E.escreve(c, "rendimento 100%, economia atômica 56%", XE, 920, 54, "g", TINTA, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho:", "i", 66, CLARO), XE, 180, passo=0.12)
        E.frase(c, t, C["s13.a"], [("um", "i", 70, CLARO), ("produto", "g", 70, BR), ("só", "i", 70, CLARO), ("=", "g", 70, CLARO), ("100%", "g", 76, E.CLARO)], XE, 330, passo=0.12)
        E.frase(c, t, C["s13.a"] + 1.4, ps("sem conta", "i", 60, CLARO), XE, 420, passo=0.1)
        Q.formula_em(c, t, C["s13.b"], "N2 + 3 H2 -> 2 NH3", W / 2, 620, 110, align="center", escuro=True, cores={"NH3": E.CLARO})
        E.frase(c, t, C["s13.b"] + 0.8, ps("todos os átomos vão para ele", "i", 60, BR), W / 2, 780, "center", 0.1)
        return
    E.frase(c, t, C["s14.a"], [("com", "i", 66, CLARO), ("subproduto,", "g", 66, BR)] + ps("faça a conta", "i", 66, CLARO), W / 2, 320, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("economia", "i", 66, CLARO), ("alta", "g", 66, BR), ("não", "g", 66, ERRADO), ("basta", "i", 66, CLARO)], W / 2, 500, "center", 0.12)
    E.frase(c, t, C["s14.c"], ps("reagente tóxico ou muita energia ferem outros princípios", "i", 54, BR), W / 2, 680, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], ps("na siderurgia, o ferro sai do minério:", "i", 58, TINTA2), XE, 300, passo=0.08)
    Q.equacao(c, t, C["s15.b"], FERRO, 760, 480, 90, tl=[C["s15.b"] + 0.25 * k for k in range(6)], cores={"Fe": E.COR})
    E.frase(c, t, C["s15.c"], [("massas", "i", 56), ("molares:", "i", 56)], XE, 640, passo=0.1)
    for k, (f, v) in enumerate((("Fe2O3", "= 160"), ("CO", "= 28"), ("Fe", "= 56"))):
        x = XE + 470 * k
        Q.formula_em(c, t, C["s15.c"] + 0.6 + 0.2 * k, f, x, 730, 66)
        E.formula_em(c, t, C["s15.c"] + 0.6 + 0.2 * k, v, x + Q.grupos(f, 0, 0, 66)[-1]["x1"] + 20, 730, 66, "g", TINTA)
    E.frase(c, t, C["s15.d"], ps("economia atômica, se o produto desejado é o ferro?", "i", 56), XE, 880, passo=0.08)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1620, cy=740, r=150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "reagentes: 160 + 3 × 28", XE, 260, 76, "g", TINTA)
    E.formula_em(c, t, C["s17.b"], "3 × 28 = 84", XE + 140, 360, 64, "g", TINTA2)
    E.formula_em(c, t, C["s17.c"], "160 + 84 = 244", XE + 140, 450, 64, "g", TINTA)
    E.formula_em(c, t, C["s17.d"], "produto: 2 × 56 = 112", XE, 570, 76, "g", COR)
    barra_massa(c, t, C["s18"], 1100, 330, 700, 80, 244, 112, C["s18"] + 0.2, "ferro: 112 g", "CO₂")
    E.foco(c, t, C["s18.b"], 0.4, lambda a: (E.escreve(c, "metade de 244 é 122;", 1100, 580, 44, "b", TINTA2, a), E.escreve(c, "112 é um pouco menos", 1100, 640, 44, "b", TINTA2, a)))
    E.formula_em(c, t, C["s18.a"], "112 ÷ 244 × 100 ≈", 1480, 760, 70, "g", TINTA, "right")
    bola_txt(c, t, C["s18.c"], "46%", 1640, 735, 90, 60, CERTO)
    riscado(c, t, C["s18.d"], "esqueceu o 3: 112 de 188", XE, 760, 54, "b")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("química", "g", 62), ("verde:", "g", 62, COR), ("não", "i", 66), ("gerar", "i", 66), ("o", "i", 66), ("resíduo", "i", 66)]),
                 ("s19.b", [("economia", "g", 62), ("atômica:", "g", 62, COR), ("produto", "i", 66), ("÷", "g", 62, TINTA2), ("reagentes", "i", 66), ("×", "g", 62, TINTA2), ("100", "g", 62)]),
                 ("s19.c", [("um", "i", 66), ("produto", "g", 62), ("só", "i", 66), ("=", "g", 62, TINTA2), ("100%", "g", 62, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Praticando:", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.6, ps("energia, poluição e água", "i", 80), XE, 520, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, verde=b_verde, conta=b_conta, compara=b_compara, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
