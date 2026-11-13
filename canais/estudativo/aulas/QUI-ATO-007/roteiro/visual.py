"""Visual — Estudativo · QUI-ATO-007: praticando átomos e distribuição eletrônica.
Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-ATO-001): cada questão abre com o número
numa pílula escura, o enunciado à esquerda e o desenho do assunto à direita (modelo, chama, núcleo, distribuição);
a pausa é E.relogio no lugar do desenho. Resposta com o raciocínio em passos e o resultado na esfera.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-007_praticando_atomos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"
NEUTRON = "#8A8D96"
LUZ_CU = "#1FB5A5"

K19 = Q.distribuicao(19)
assert K19 == [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 1)] and 19 - 1 == 18
assert 16 + 16 == 32 and 16 - 18 == -2 and 34 - 16 == 18


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def particula(c, x, y, r, tipo, a=1.0):
    if a <= 0 or r <= 0:
        return
    E.bola(c, x, y, r, {"p": E.COR, "n": NEUTRON, "e": Q.ELETRON}[tipo], a)
    w = max(3, r * 0.17)
    if tipo in "pe" and r >= 10:
        M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, w)
        if tipo == "p":
            M.line(c, x, y - r * 0.45, x, y + r * 0.45, BR, a, w)


def nucleo(c, t, t0, cx, cy, p, n, r=22):
    tipos = []
    for k in range(p + n):
        tipos.append("p" if (k % 2 == 0 and tipos.count("p") < p) or tipos.count("n") >= n else "n")
    for k, tp in enumerate(tipos):
        g, d = k * 2.4, r * 0.95 * math.sqrt(k)
        particula(c, cx + d * math.cos(g), cy + d * math.sin(g), r * ease_back(prog(t, t0 + 0.03 * k, 0.35)), tp)


def rutherford(c, t, cx, cy, R, a=1.0):
    if a <= 0:
        return
    for k in range(3):
        c.save(); c.translate(cx, cy); c.rotate(k * 60)
        c.drawOval(skia.Rect.MakeXYWH(-R, -R * 0.38, 2 * R, R * 0.76), M.paint(TINTA2, 0.55 * a, stroke=3))
        g = t * 0.6 * (1 + 0.3 * k) + k * 2
        particula(c, R * math.cos(g), R * 0.38 * math.sin(g), max(9, R * 0.06), "e", a)
        c.restore()
    E.bola(c, cx, cy, R * 0.08, E.COR, a)


def chama(c, cx, yb, w, h, cor, a=1.0, t=0.0):
    if a <= 0:
        return
    k = 1 + 0.04 * math.sin(t * 9)
    pth = skia.Path()
    pth.moveTo(cx - w / 2, yb)
    pth.cubicTo(cx - w * 0.7, yb - h * 0.5 * k, cx - w * 0.1, yb - h * 0.7 * k, cx, yb - h * k)
    pth.cubicTo(cx + w * 0.1, yb - h * 0.7 * k, cx + w * 0.7, yb - h * 0.5 * k, cx + w / 2, yb)
    pth.close()
    pnt = skia.Paint(AntiAlias=True)
    pnt.setShader(skia.GradientShader.MakeLinear([skia.Point(0, yb), skia.Point(0, yb - h)], [M.hexc("#5B8DEF", a), M.hexc(cor, a), M.hexc(cor, 0.0)], [0, 0.35, 1]))
    c.drawPath(pth, pnt)
    M.rrect(c, cx - w * 0.22, yb, w * 0.44, 120, 8, "#8A8D96", a)


def termo(sub, n):
    return f"{sub}^{{{n}}}"


def dist(c, t, itens, tl, x, y, size, cores=None):
    xx = x
    for k, ((s, n), ti) in enumerate(zip(itens, tl)):
        txt = termo(s, n)
        w = E.formula(None, txt, 0, 0, size, "g", a=0)
        cor = (cores or {}).get(k, TINTA)
        E.foco(c, t, ti, 0.4, lambda a, txt=txt, xx=xx, cor=cor: E.formula(c, txt, xx, y, size, "g", cor, a))
        xx += w + size * 0.32


def cabeca(c, t, t0, n, txt=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 140, 160, 50, "g", fundo=TINTA, a=a))
    if txt:
        E.frase(c, t, t0 + 0.4, ps(txt, "i", 54, TINTA2), XE + 320, 178, passo=0.08)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 200, COR)] + ps("questões", "i", 120), XE, 380, passo=0.2)
    E.frase(c, t, C["s01.a"] + 0.8, ps("sobre o átomo, criadas para esta aula", "i", 60, TINTA2), XE, 490, passo=0.1)
    E.frase(c, t, C["s01.b"], [("pause", "g", 70, COR)] + ps("e resolva antes da resposta", "i", 70), XE, 680, passo=0.12)
    E.foco(c, t, C["s01.b"] + 0.4, 0.6, lambda a: E.relogio(c, t, C["s01.b"] + 0.4, cx=1560, cy=440, r=150))


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("quatro ferramentas", "i", 70, TINTA2), XE, 190, passo=0.12)
    itens = (("s02.a", "modelos atômicos"), ("s02.b", "o salto do elétron"), ("s02.c", "prótons, nêutrons e elétrons"), ("s02.d", "diagrama de Pauling"))
    for i, (k, s) in enumerate(itens):
        y = 340 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62)], XE + 110, y)
    E.frase(c, t, C["s02.d"] + 1.4, ps("travou? procure a aula no canal", "i", 54, TINTA2), XE, 960, passo=0.08)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    cabeca(c, t, C["s03.a"], 1)
    def citacao(a):
        M.rrect(c, XE, 260, 1060, 230, 24, "#FFFFFF", a, shadow=True)
        M.rrect(c, XE, 260, 14, 230, 6, E.COR, a)
        E.escreve(c, "“bombardeou uma folha de ouro e concluiu", XE + 50, 350, 50, "i", TINTA, a)
        E.escreve(c, "que o átomo tem um núcleo pequeno e positivo”", XE + 50, 430, 50, "i", TINTA, a)
    E.foco(c, t, C["s03.b"], 0.6, citacao)
    E.frase(c, t, C["s03.c"], [("1", "g", 56, COR)] + ps("de quem é esse modelo?", "i", 60), XE, 640, passo=0.08)
    E.frase(c, t, C["s03.d"], [("2", "g", 56, COR)] + ps("que observação mostrou o átomo quase vazio?", "i", 60), XE, 760, passo=0.08)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1560, cy=600, r=180)


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05"] + 0.3, [("folha de ouro", "g", 60), ("+", "g", 60, TINTA2), ("núcleo", "g", 60)], XE, 200, passo=0.15)
    E.foco(c, t, C["s05.a"], 0.5, lambda a: E.pilula(c, "Rutherford", XE + 230, 330, 72, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s05.a"] + 0.3, 0.5, lambda a: rutherford(c, t, 1500, 420, 230, a))
    E.frase(c, t, C["s05.b"], ps("vazio:", "i", 62) + [("a grande maioria atravessou", "g", 58)], XE, 520, passo=0.1)
    E.frase(c, t, C["s05.c"], [("não", "g", 58, ERRADO)] + ps("troque com Thomson:", "i", 62), XE, 720, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("no pudim de passas", "i", 62) + [("não há núcleo", "g", 58)], XE, 820, passo=0.1)


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    cabeca(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.a"] + 0.6, ps("um fio de cobre vai à chama", "i", 64), XE, 320, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("e a chama fica", "i", 64) + [("verde-azulada", "g", 60, LUZ_CU)], XE, 430, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("a luz sai quando o elétron", "i", 62), XE, 620, passo=0.1)
    E.frase(c, t, C["s06.c"] + 1.6, [("sobe", "g", 64), ("ou", "i", 66), ("volta?", "g", 64, COR)], XE, 720, passo=0.15)
    if t < C["s07"]:
        cor = Q.muda_cor(t, C["s06.b"], "#F29A3A", LUZ_CU, 0.6)
        E.foco(c, t, C["s06.a"] + 0.4, 0.5, lambda a: chama(c, 1500, 820, 220, 440, cor, a, t))
    else:
        E.relogio(c, t, C["s07.a"], cx=1560, cy=520, r=180)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08.a"], ps("o calor dá energia:", "i", 64) + [("sobe", "g", 60, "#F2A33A")], XE, 240, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("na subida,", "i", 62) + [("recebe", "g", 60)] + ps("energia", "i", 62), XE, 350, passo=0.1)
    E.frase(c, t, C["s08.c"], ps("a luz sai na", "i", 70) + [("volta", "g", 70, COR)], XE, 530, passo=0.12)
    E.foco(c, t, C["s08.c"] + 0.6, 0.4, lambda a: E.selo(c, XE + 620, 505, 40, True, a))
    E.frase(c, t, C["s08.d"], ps("cor do cobre: degraus próprios", "i", 58, TINTA2), XE, 700, passo=0.1)
    # átomo com o salto
    cx, cy = 1450, 520
    for r in (90, 160, 230):
        c.drawCircle(cx, cy, r, M.paint(TINTA2, 0.6, stroke=3))
    E.bola(c, cx, cy, 40, E.COR)
    sobe = ease_io(prog(t, C["s08.a"] + 0.3, 0.6)) * (1 - ease_io(prog(t, C["s08.c"], 0.6)))
    r = lerp(90, 230, sobe)
    particula(c, cx + r * math.cos(1.1), cy + r * math.sin(1.1), 18, "e")
    if t >= C["s08.c"]:
        p = ease_out(prog(t, C["s08.c"] + 0.2, 1.0))
        g = math.radians(-30)
        pth = skia.Path()
        x0, y0 = cx + 120, cy + 60
        for k in range(int(420 * p / 4) + 1):
            s = k * 4
            w = 16 * math.sin(s / 46 * math.tau)
            x, y = x0 + math.cos(g) * s - math.sin(g) * w, y0 + math.sin(g) * s + math.cos(g) * w
            pth.moveTo(x, y) if k == 0 else pth.lineTo(x, y)
        c.drawPath(pth, M.paint(LUZ_CU, 1, stroke=6, cap_round=True))


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    cabeca(c, t, C["s09.a"], 3, "das partículas para os números")
    for k, (ck, tp, nome, n) in enumerate((("s09.b", "p", "prótons", 16), ("s09.c", "n", "nêutrons", 16), ("s09.d", "e", "elétrons", 18))):
        y = 320 + k * 110
        E.foco(c, t, C[ck], 0.4, lambda a, y=y, tp=tp, nome=nome, n=n: (particula(c, XE + 30, y - 22, 28, tp, a), E.escreve(c, f"{n} {nome}", XE + 80, y, 62, "g", TINTA, a)))
    E.frase(c, t, C["s09.e"], [("1", "g", 56, COR)] + ps("Z, número de massa e carga?", "i", 60), XE, 720, passo=0.08)
    E.frase(c, t, C["s09.f"], [("2", "g", 56, COR)] + ps("Z 16 e massa 34: é isótopo?", "i", 60), XE, 840, passo=0.08)
    if t < C["s10"]:
        nucleo(c, t, C["s09.b"], 1500, 480, 16, 16, 22)
    else:
        E.relogio(c, t, C["s10.a"], cx=1560, cy=520, r=180)


def b_resposta3(c, t, C, b):
    linhas = (("s11.a", "Z = prótons = 16", "enxofre"), ("s11.b", "A = 16 + 16 = 32", ""), ("s11.d", "carga: ganhou 2 → 2−", ""))
    for i, (k, s, extra) in enumerate(linhas):
        y = (230, 360, 600)[i]
        E.foco(c, t, C[k], 0.4, lambda a, y=y, s=s: E.formula(c, s, XE, y, 70, "g", TINTA, a))
        if extra:
            E.foco(c, t, C[k] + 0.8, 0.4, lambda a, y=y, extra=extra: E.pilula(c, extra, XE + 820, y - 22, 50, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s11.c"], ps("2 elétrons a mais que prótons", "i", 58, TINTA2), XE, 480, passo=0.08)
    E.foco(c, t, C["s11.d"] + 0.6, 0.5, lambda a: Q.formula(c, "^{32}_{16}S^{2-}", 1380, 420, 180, a=a))
    E.frase(c, t, C["s11.e"], ps("massa 34, mesmo Z:", "i", 62), XE, 780, passo=0.1)
    E.foco(c, t, C["s11.f"], 0.5, lambda a: E.pilula(c, "é isótopo", XE + 660, 760, 60, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s11.f"] + 0.6, ps("com 2 nêutrons a mais", "i", 56, TINTA2), XE, 900, passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12"], ps("um atalho", "i", 72, CLARO), W / 2, 200, "center", 0.12)
        E.foco(c, t, C["s12.a"], 0.5, lambda a: E.pilula(c, "carga = prótons − elétrons", W / 2, 380, 84, "g", fundo=E.COR, a=a))
        E.formula_em(c, t, C["s12.b"], "16 − 18 = −2", W / 2, 640, 140, "g", BR, "center")
        E.frase(c, t, C["s12.c"], ps("o sinal já sai certo", "i", 66, CLARO), W / 2, 860, "center", 0.1)
        return
    E.frase(c, t, C["s13.a"], ps("cada próton vale", "i", 64, CLARO) + [("+1", "g", 62, E.CLARO)] + ps("e cada elétron", "i", 64, CLARO) + [("−1", "g", 62, "#8FB8FF")], W / 2, 330, "center", 0.1)
    E.frase(c, t, C["s13.b"], ps("os nêutrons não entram:", "i", 64, CLARO) + [("sem carga", "g", 60, BR)], W / 2, 500, "center", 0.1)
    E.frase(c, t, C["s13.c"], ps("só não esqueça a ordem:", "i", 64, CLARO) + [("prótons primeiro", "g", 60, BR)], W / 2, 680, "center", 0.1)
    for k, tp in enumerate("pne"):
        E.foco(c, t, C["s13.a"] + 0.3 * k, 0.4, lambda a, k=k, tp=tp: particula(c, W / 2 - 160 + 160 * k, 880, 40, tp, a))


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    cabeca(c, t, C["s14.a"], 4, "junta tudo")
    E.frase(c, t, C["s14.b"], [("potássio:", "g", 70), ("Z 19", "g", 70, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s14.c"], [("1", "g", 56, COR)] + ps("faça a distribuição", "i", 60), XE, 500, passo=0.08)
    E.frase(c, t, C["s14.d"], [("2", "g", 56, COR)] + ps("quantos elétrons na valência?", "i", 60), XE, 620, passo=0.08)
    E.frase(c, t, C["s14.e"], [("3", "g", 56, COR)] + ps("distribua o íon", "i", 60), XE, 740, passo=0.08)
    Q.formula_em(c, t, C["s14.e"] + 0.8, "K^+", XE + 560, 750, 90)
    if t < C["s15"]:
        Q.pauling(c, t, C["s14.c"], 1300, 260, 48, setas=False)
    else:
        E.relogio(c, t, C["s15.a"], cx=1560, cy=520, r=180)


def b_resposta4(c, t, C, b):
    if t < C["s17"]:
        dist(c, t, K19, [C["s16.a"]] * 5 + [C["s16.b"]], XE, 320, 92, cores={5: COR})
        E.foco(c, t, C["s16.a"] + 1.2, 0.4, lambda a: E.escreve(c, "já são 18", XE, 430, 54, "i", TINTA2, a))
        E.foco(c, t, C["s16.b"] + 1.0, 0.4, lambda a: (E.formula(c, "3d^1", XE + 400, 560, 80, "g", ERRADO, a), E.escreve(c, "não: o 4s vem antes", XE + 600, 555, 54, "i", ERRADO, a)))
        if t >= C["s16.b"] + 1.4:
            E.risco(c, XE + 390, 575, XE + 540, 495, t, C["s16.b"] + 1.4, largura=8)
        E.frase(c, t, C["s16.c"], ps("camada mais externa: a 4, com", "i", 60) + [("1", "g", 58, COR)] + ps("elétron", "i", 60), XE, 720, passo=0.1)
        bola_txt(c, t, C["s16.d"], "1", XE + 64, 860, 56, 64)
        E.foco(c, t, C["s16.d"] + 0.2, 0.4, lambda a: E.escreve(c, "elétron na valência", XE + 150, 882, 56, "i", TINTA, a))
        Q.pauling(c, t, C["s16"], 1380, 470, 40, Z=19, passo=0.25)
        return
    Q.formula_em(c, t, C["s17.a"], "K^+", XE, 280, 140, cores={"carga": E.COR})
    E.frase(c, t, C["s17.a"] + 0.4, ps("sai 1 elétron da camada de fora:", "i", 58), XE + 260, 250, passo=0.08)
    E.formula_em(c, t, C["s17.b"], "4s^1", XE + 1180, 260, 80, "g", ERRADO)
    if t >= C["s17.b"] + 0.5:
        E.risco(c, XE + 1170, 280, XE + 1340, 200, t, C["s17.b"] + 0.5, largura=8)
    dist(c, t, K19[:5], [C["s17.c"]] * 5, XE, 520, 92, cores={4: COR})
    E.foco(c, t, C["s17.c"] + 0.6, 0.4, lambda a: E.escreve(c, "18 elétrons", XE, 640, 60, "g", TINTA, a))
    E.formula_em(c, t, C["s17.d"], "19 − 1 = 18", XE, 820, 84, "g", TINTA2)
    E.foco(c, t, C["s17.d"] + 0.8, 0.4, lambda a: E.selo(c, XE + 560, 790, 40, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("palavra-chave", "g", 64, COR), ("do modelo", "i", 68)]),
                 ("s18.b", [("partículas pelo", "i", 68), ("Z", "g", 64, COR), ("e pelo", "i", 68), ("A", "g", 64)]),
                 ("s18.c", [("diagonais;", "g", 64), ("tire da", "i", 68), ("camada de fora", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("tabela periódica", "g", 90, COR)], XE, 400)
    E.frase(c, t, C["s19.b"], [("período", "g", 66), ("e", "i", 70), ("família", "g", 66)] + ps("pela distribuição", "i", 70), XE, 520, passo=0.12)
    Q.tabela(c, t, C["s19.a"] + 0.3, XE + 20, 620, 44, numeros=False, d=1.0)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
