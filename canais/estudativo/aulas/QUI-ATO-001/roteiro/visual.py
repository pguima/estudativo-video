"""Visual — Estudativo · QUI-ATO-001: modelos de Dalton e Thomson. Primeira aula da trilha Átomo e Tabela Periódica.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho de QUI-MIS-001/roteiro/visual.py. Acréscimos desta trilha (as aulas
QUI-ATO-002 a 007 copiam daqui):
- CARGA ELÉTRICA: positivo = esfera turquesa com "+" (F.carga, a cor da matéria, como o núcleo); negativo = esfera azul
  Q.ELETRON com "−". O elétron solto é sempre a bolinha azul pequena (r ≈ 12 a 20), em qualquer modelo.
- CADA MODELO TEM UM DESENHO FIXO, que volta igual nas aulas seguintes e na linha do tempo:
  Dalton = esfera cinza maciça (bola de bilhar, dalton()); Thomson = esfera turquesa clara com "+" espalhados e elétrons
  azuis (pudim()); Rutherford = núcleo turquesa pequeno com elétrons em órbitas finas; Bohr = Q.bohr (camadas K, L, M...).
  O nome do modelo vai numa pílula escura embaixo do desenho; o ano, em cinza, em cima.
- TROCA DE MODELO = seta turquesa do modelo velho para o novo, com o FATO NOVO numa pílula sobre a seta. O modelo
  derrubado fica cinza (dessatura) e leva E.risco só quando a fala diz que ele "caiu".
- EXPERIMENTO: aparelho em traço de vidro (Q.VIDRO) e metal cinza; o que se mede (feixe, partícula, luz) na cor da matéria
  ou no azul do elétron. Placa positiva com "+" turquesa, negativa com "−" azul.
- DISTRIBUIÇÃO ELETRÔNICA (005 a 007): E.formula("1s^2 2s^2 ...", "g") em tinta; o subnível da vez na cor da matéria;
  diagrama com Q.pauling; soma de conferência em cinza-tinta e o total na esfera.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-001_modelos_dalton_thomson.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("modelo", "dalton", "eletrico", "thomson", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA_D = "#7A7D86"          # a bola de bilhar de Dalton
PUDIM = E.mix(E.COR, "#FFFFFF", 0.55)


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


def lista(c, t, itens, x, y0, dy, size=70):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def eletron(c, x, y, r=16, a=1.0, sinal=True):
    E.bola(c, x, y, r, Q.ELETRON, a)
    if sinal and r >= 12:
        M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(3, r * 0.16))


def mais(c, x, y, s, cor, a=1.0, w=None):
    w = w or max(3, s * 0.22)
    M.line(c, x - s / 2, y, x + s / 2, y, cor, a, w)
    M.line(c, x, y - s / 2, x, y + s / 2, cor, a, w)


def dalton(c, cx, cy, r, a=1.0, cinza=0.0):
    """a esfera maciça: bola de bilhar cinza com reflexo"""
    if a <= 0 or r <= 0:
        return
    E.bola(c, cx, cy, r, M.mix(CINZA_D, "#B9BCC2", cinza), a)


# posições fixas dos elétrons e dos "+" no pudim (unidades do raio)
_PE = ((-0.45, -0.35), (0.38, -0.5), (0.05, 0.05), (-0.5, 0.35), (0.48, 0.3), (0.0, 0.62), (-0.1, -0.72))
_PM = ((0.0, -0.4), (-0.6, -0.05), (0.62, -0.1), (-0.28, 0.6), (0.3, 0.68), (0.2, -0.15), (-0.25, 0.1))


def pudim(c, t, t0, cx, cy, r, te=None, a=1.0, cinza=0.0):
    """modelo de Thomson: esfera positiva clara com "+" espalhados e elétrons azuis que entram em te"""
    k = ease_back(prog(t, t0, 0.6)) if t0 is not None else 1.0
    if k <= 0 or a <= 0:
        return
    E.bola(c, cx, cy, r * k, M.mix(PUDIM, "#C9CCD2", cinza), a)
    for (ux, uy) in _PM:
        mais(c, cx + ux * r * k, cy + uy * r * k, r * 0.13 * k, M.mix(E.COR, "#8A8D96", cinza), a * 0.9)
    for i, (ux, uy) in enumerate(_PE):
        q = ease_back(prog(t, (te if te is not None else t0) + 0.12 * i, 0.35)) if (te is not None or t0 is not None) else 1.0
        if q > 0:
            eletron(c, cx + ux * r * k, cy + uy * r * k, r * 0.12 * q, a)


def pente(c, x, y, w, h, a=1.0, cor="#2A2B31"):
    """pente de plástico: costas em cima e dentes para baixo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h * 0.32, 10, cor, a)
    n = int(w / 22)
    for k in range(n):
        xx = x + 8 + k * (w - 16) / (n - 1)
        M.line(c, xx, y + h * 0.3, xx, y + h, cor, a, 8)


def papeis(c, t, t0, x0, y_chao, y_pente, n=9, a=1.0, cor=None):
    """papel picado: pedacinhos que pulam do chão e grudam embaixo do pente a partir de t0"""
    cor = cor or "#F3C845"
    for k in range(n):
        px = x0 + k * 46 + (k % 3) * 9
        q = ease_out(prog(t, t0 + 0.08 * k, 0.6)) if t0 is not None else 0
        y = lerp(y_chao, y_pente + 18 + (k % 2) * 10, q)
        ang = (k * 37 % 50 - 25) * (1 - q) + (k % 2 * 2 - 1) * 8 * q
        c.save(); c.translate(px, y); c.rotate(ang)
        M.rrect(c, -13, -9, 26, 18, 3, cor, a, shadow=True)
        c.restore()


def tubo(c, t, t0, x, y, w, h, tb, tc, a=1.0):
    """tubo de raios catódicos: vidro, cátodo à esquerda, placas + (em cima) e − (embaixo); o feixe nasce em tb e curva em tc"""
    if a <= 0 or t < t0:
        return
    q = ep(t, t0, 0.5) * a
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), h / 2, h / 2)
    c.drawRRect(r, M.paint("#FFFFFF", 0.55 * q))
    c.drawRRect(r, M.paint(Q.VIDRO, q, stroke=5))
    # cátodo: placa de metal à esquerda, ligada ao polo negativo
    M.rrect(c, x + 40, y + h / 2 - 70, 20, 140, 5, "#8A8D96", q)
    E.escreve(c, "cátodo", x + 6, y + h + 56, 40, "i", TINTA2, q)
    # placas do meio
    px0, px1 = x + w * 0.42, x + w * 0.72
    M.rrect(c, px0, y + 26, px1 - px0, 18, 5, E.COR, q)
    M.rrect(c, px0, y + h - 44, px1 - px0, 18, 5, Q.ELETRON, q)
    mais(c, (px0 + px1) / 2, y - 26, 34, E.COR, q, 7)
    M.line(c, (px0 + px1) / 2 - 17, y + h + 30, (px0 + px1) / 2 + 17, y + h + 30, Q.ELETRON, q, 7)
    # o feixe
    p = ease_io(prog(t, tb, 0.8))
    if p <= 0:
        return
    curva = ease_io(prog(t, tc, 0.8)) if tc is not None else 0
    x0, y0 = x + 62, y + h / 2
    x1 = x + w - 40
    yf = y0 - curva * (h * 0.34)
    pth = skia.Path(); pth.moveTo(x0, y0); pth.lineTo(px0, y0); pth.quadTo(px1, y0, x1, yf)
    meas = skia.PathMeasure(pth, False)
    L = meas.getLength()
    seg = skia.Path(); meas.getSegment(0, L * p, seg, True)
    glow = M.paint(E.COR, 0.25 * q, stroke=22, cap_round=True)
    c.drawPath(seg, glow)
    c.drawPath(seg, M.paint(E.COR, q, stroke=7, cap_round=True))
    # elétrons andando no feixe
    for k in range(6):
        u = ((t - tb) * 0.45 + k / 6) % 1.0
        if u > p:
            continue
        pos, _ = meas.getPosTan(L * u)
        eletron(c, pos.x(), pos.y(), 11, q, sinal=False)


def seta_troca(c, t, t0, x0, x1, y, rotulo, size=44):
    E.ponte(c, t, t0, x0, x1, y, rotulo, E.COR, size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("pente no cabelo seco", "i", 80), XE, 230, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("perto de", "i", 80) + [("papel picado", "g", 76, COR)], XE, 340, passo=0.12)
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: pente(c, 1150, 400, 520, 120, a))
        papeis(c, t, C["s01.c"], 1180, 900, 400 + 120)
        if t < C["s01.c"]:
            papeis(c, t, None, 1180, 900, 520)
        E.frase(c, t, C["s01.c"] + 0.2, [("o papel", "i", 76), ("pula!", "g", 76, COR)], XE, 520, passo=0.15)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: dalton(c, XE + 120, 820, 100, a))
        E.frase(c, t, C["s01.d"] + 0.3, ps("o primeiro modelo", "i", 64), XE + 270, 790, passo=0.1)
        E.frase(c, t, C["s01.d"] + 1.0, [("não", "g", 62, ERRADO)] + ps("explicava isso", "i", 64), XE + 270, 880, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("o átomo de", "i", 74), ("Dalton", "g", 70)]),
                 (C["s02.b"], [("o átomo de", "i", 74), ("Thomson", "g", 70)]),
                 (C["s02.c"], [("o", "i", 74), ("fato", "g", 70, COR), ("que trocou um pelo outro", "i", 64)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula de átomos", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("tudo é feito de", "i", 80) + [("átomos", "g", 76, COR)], XE, 340, passo=0.12)
    for k, el in enumerate(("H", "O", "C", "N")):
        Q.atomo_em(c, t, C["s03.a"] + 0.6 + 0.15 * k, 1300 + 130 * k, 320, 50, el)
    E.frase(c, t, C["s03.b"], ps("cada tipo de átomo:", "i", 80) + [("elemento", "g", 76, COR)], XE, 480, passo=0.12)
    E.frase(c, t, C["s03.c"] - 1.8, ps("ninguém enxerga um átomo", "i", 70, TINTA2), XE, 640, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("a ciência cria", "i", 90), XE, 820, passo=0.12)
    E.frase(c, t, C["s03.c"] + 0.2, [("modelos", "g", 150, COR)], XE + 640, 830)


# ---------------- modelo ----------------
def mapa(c, x, y, w, h, a=1.0):
    """um mapa simples: papel, quadras, uma avenida e o alfinete"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    for k in range(1, 4):
        M.line(c, x + k * w / 4, y + 20, x + k * w / 4, y + h - 20, "#D9DCE1", a, 10)
        M.line(c, x + 20, y + k * h / 4, x + w - 20, y + k * h / 4, "#D9DCE1", a, 10)
    M.line(c, x + 30, y + h - 40, x + w - 30, y + 40, E.mix(E.COR, "#FFFFFF", 0.4), a, 16)
    px, py = x + w * 0.62, y + h * 0.42
    E.bola(c, px, py - 30, 26, ERRADO, a)
    M.line(c, px, py - 6, px, py + 24, ERRADO, a, 6)


def b_modelo(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("modelo", "g", 110, COR)], XE, 260)
        E.frase(c, t, C["s04.a"] + 0.7, ps("imagem simplificada que", "i", 68), XE, 380, passo=0.1)
        E.frase(c, t, C["s04.a"] + 1.4, ps("explica o que se observa", "i", 68), XE, 470, passo=0.1)
        E.foco(c, t, C["s04.b"], 0.6, lambda a: mapa(c, 1180, 200, 560, 400, a))
        E.frase(c, t, C["s04.b"] + 0.6, ps("não é a cidade, mas ajuda", "i", 50, TINTA2), 1460, 670, "center", 0.08)
    if t < C["s04.c"]:
        E.saida(c, t, C["s04.c"] - 0.1, s04)
        return
    # o ciclo: modelo velho → fato novo → modelo melhor
    E.frase(c, t, C["s04.c"], ps("apareceu um fato que ele", "i", 70) + [("não explica?", "g", 66, ERRADO)], W / 2, 260, "center", 0.1)
    E.foco(c, t, C["s04.c"] + 0.5, 0.5, lambda a: (M.rrect(c, 330, 420, 420, 300, 30, "#FFFFFF", a, shadow=True),
                                                   centro(c, "modelo velho", 540, 590, 56, "i", TINTA2, a)))
    if t >= C["s04.d"]:
        E.risco(c, 380, 680, 700, 470, t, C["s04.d"] + 0.9, largura=10)
    seta_troca(c, t, C["s04.d"], 790, 1130, 570, "fato novo")
    E.foco(c, t, C["s04.d"] + 0.6, 0.5, lambda a: (M.rrect(c, 1170, 420, 420, 300, 30, E.COR, a, shadow=True),
                                                   centro(c, "modelo melhor", 1380, 590, 56, "g", E.SOBRE, a)))
    E.frase(c, t, C["s04.d"] + 1.2, ps("é trocado por um melhor", "i", 70), W / 2, 900, "center", 0.1)


# ---------------- Dalton ----------------
def b_dalton(c, t, C, b):
    if t < C["s06"]:
        def s05():
            E.foco(c, t, C["s05"] + 0.2, 0.4, lambda a: E.escreve(c, "por volta de 1800", XE, 190, 54, "i", TINTA2, a))
            E.frase(c, t, C["s05.a"], [("John", "g", 96), ("Dalton", "g", 96, COR)], XE, 320, passo=0.15)
            E.frase(c, t, C["s05.b"], ps("uma esfera", "i", 80) + [("maciça", "g", 76, COR)], XE, 470, passo=0.12)
            E.frase(c, t, C["s05.c"], ps("como uma", "i", 70) + [("bola de bilhar", "g", 66)], XE, 580, passo=0.12)
            r = 230 * ease_back(prog(t, C["s05.b"] + 0.3, 0.7))
            dalton(c, 1440, 520, r)
            for k, (ck, s, dy) in enumerate((("s05.d", "inteira por dentro", 760), ("s05.e", "impossível de dividir", 860))):
                pilula_em(c, t, C[ck], s, XE + (E.larg(s, "g", 52) + 60) / 2, dy, 52, TINTA)
            # a tentativa de dividir: uma linha de corte que não entra
            if t >= C["s05.e"]:
                p = ep(t, C["s05.e"] + 0.3, 0.5)
                M.line(c, 1440, 230, 1440, lerp(230, 290, p), ERRADO, p, 8, dash=[16, 12])
                E.foco(c, t, C["s05.e"] + 0.8, 0.4, lambda a: E.selo(c, 1440, 200, 40, False, a))
            E.foco(c, t, C["s05.b"] + 0.9, 0.4, lambda a: E.pilula(c, "Dalton", 1440, 820, 46, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    # s06: átomos iguais, átomos diferentes; transformação = troca de lugar
    def iguais():
        E.frase(c, t, C["s06.a"], ps("mesmo elemento:", "i", 64) + [("iguais", "g", 62, COR)], XE, 220, passo=0.12)
        for k in range(3):
            Q.atomo_em(c, t, C["s06.a"] + 0.6 + 0.15 * k, XE + 820 + 130 * k, 200, 50, "O")
        E.frase(c, t, C["s06.b"], ps("elementos diferentes:", "i", 64) + [("diferentes", "g", 62, COR)], XE, 340, passo=0.12)
        for k, el in enumerate(("O", "H", "C")):
            Q.atomo_em(c, t, C["s06.b"] + 0.8 + 0.15 * k, XE + 1080 + 130 * k, 320, 50 if el != "H" else 36, el)
    E.saida(c, t, C["s06.c"] - 0.1, iguais)
    if t < C["s06.c"]:
        return
    E.frase(c, t, C["s06.c"], ps("os átomos só", "i", 76) + [("trocam de lugar", "g", 72, COR)], W / 2, 220, "center", 0.12)
    # antes: H₂ + H₂ + O₂ ; depois: H₂O + H₂O — os mesmos 6 átomos
    sep = ease_io(prog(t, C["s06.c"] + 1.0, 1.4))
    antes = [("H", -150, -60), ("H", -70, -60), ("H", -150, 80), ("H", -70, 80), ("O", 80, -10), ("O", 190, -10)]
    depois = [("H", 230, -70), ("H", 230, 80), ("H", 470, -70), ("H", 470, 80), ("O", 300, 5), ("O", 540, 5)]
    for k, ((el, x0, y0), (_, x1, y1)) in enumerate(zip(antes, depois)):
        cx = 620 + lerp(x0, x1 + 260, sep)
        cy = 560 + lerp(y0, y1, sep)
        Q.atomo_em(c, t, C["s06.c"] + 0.1 * k, cx, cy, 46 if el == "H" else 62, el)
    if t < C["s06.c"] + 1.0:
        E.frase(c, t, C["s06.c"] + 0.4, ps("antes", "i", 54, TINTA2), 560, 740, "center")
    E.frase(c, t, C["s06.c"] + 2.4, ps("depois: as mesmas bolinhas", "i", 54, TINTA2), 1240, 740, "center", 0.08)
    E.frase(c, t, C["s06.d"], [("nenhum", "g", 62), ("some,", "i", 66), ("nenhum", "g", 62), ("aparece", "i", 66)], W / 2, 880, "center", 0.12)
    pilula_em(c, t, C["s06.e"], "transformações: outra aula", W / 2, 990, 44, TINTA2, "b")


# ---------------- a eletricidade ----------------
def b_eletrico(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07"] + 0.3, ps("algo que a bola de bilhar não explicava:", "i", 60, TINTA2), XE, 200, passo=0.08)
        E.frase(c, t, C["s07.a"], [("eletricidade", "g", 110, COR)], XE, 340)
        F.carga(c, t, C["s07.b"], XE + 90, 520, 62, "+")
        E.frase(c, t, C["s07.b"] + 0.2, ps("positiva", "i", 70), XE + 190, 545)
        F.carga(c, t, C["s07.c"], XE + 590, 520, 62, "−")
        E.frase(c, t, C["s07.c"] + 0.2, ps("negativa", "i", 70), XE + 690, 545)
        # opostas se atraem; iguais se empurram
        for k, (ck, s1, s2, txt, perto) in enumerate((("s07.d", "+", "−", "opostas se atraem", True), ("s07.e", "−", "−", "iguais se repelem", False))):
            y = 740 + k * 190
            if t < C[ck]:
                continue
            u = ease_io(prog(t, C[ck] + 0.4, 0.8))
            d = lerp(260, 150, u) if perto else lerp(170, 300, u)
            cx = 1420
            F.carga(c, t, C[ck], cx - d / 2, y, 52, s1)
            F.carga(c, t, C[ck], cx + d / 2, y, 52, s2)
            for sgn in (-1, 1):
                x0 = cx + sgn * (d / 2 - 70) if perto else cx + sgn * (d / 2 + 70)
                x1 = x0 - sgn * 40 if perto else x0 + sgn * 50
                p = ep(t, C[ck] + 0.4, 0.4)
                if p > 0:
                    M.arrow(c, x0, y, x1, y, TINTA2, p, 5, 16)
            E.frase(c, t, C[ck], ps(txt, "i", 64), XE, y + 22, passo=0.1)
        return
    # s08: o pente pega carga; a bola de Dalton não tem o que passar
    E.foco(c, t, C["s08"], 0.5, lambda a: pente(c, XE + 40, 260, 460, 100, a))
    for k in range(6):
        q = ep(t, C["s08.a"] + 0.15 * k, 0.4)
        if q > 0:
            eletron(c, XE + 80 + 70 * k, 250 + 190 * (1 - ease_io(prog(t, C["s08.a"] + 0.15 * k, 0.6))), 16, q)
    E.frase(c, t, C["s08.a"] + 0.2, ps("o atrito faz", "i", 64) + [("carga passar", "g", 60, COR)], XE, 520, passo=0.1)
    E.foco(c, t, C["s08.b"], 0.5, lambda a: dalton(c, 1420, 430, 180, a))
    E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: centro(c, "?", 1420, 470, 140, "g", BR, a))
    E.frase(c, t, C["s08.b"] + 0.4, ps("maciça e sem partes:", "i", 60), 1420, 700, "center", 0.1)
    E.frase(c, t, C["s08.b"] + 1.4, [("nada", "g", 60, ERRADO)] + ps("para passar", "i", 62), 1420, 790, "center", 0.1)
    E.frase(c, t, C["s08.c"], ps("a resposta veio com uma descoberta:", "i", 62), XE, 960, passo=0.08)
    E.foco(c, t, C["s08.c"] + 1.8, 0.4, lambda a: (eletron(c, 1340, 940, 26, a), E.escreve(c, "o elétron", 1390, 960, 64, "g", COR, a)))


# ---------------- Thomson ----------------
TX, TY, TW, TH = 520, 470, 1100, 230


def b_thomson(c, t, C, b):
    if t < C["s11"]:
        E.foco(c, t, C["s09"] + 0.2, 0.4, lambda a: E.escreve(c, "1897", XE, 170, 54, "i", TINTA2, a))
        E.frase(c, t, C["s09.a"], [("J. J.", "g", 80), ("Thomson", "g", 80, COR)], XE + 170, 170, passo=0.15)
        E.frase(c, t, C["s09.b"], ps("um tubo de vidro quase sem ar", "i", 62, TINTA2), XE, 280, passo=0.1)
        tubo(c, t, C["s09.b"] + 0.3, TX, TY, TW, TH, C["s09.c"], C["s10.b"] if C["s10.b"] <= t else None)
        if C["s09.c"] <= t < C["s10"]:
            E.frase(c, t, C["s09.c"] + 0.4, [("raio", "g", 64, COR), ("catódico:", "g", 64, COR)] + ps("sai do cátodo, o polo negativo", "i", 56), XE, 900, passo=0.1)
        if t >= C["s10"]:
            E.frase(c, t, C["s10.a"], ps("placa", "i", 56) + [("+", "g", 56, COR)] + ps("em cima,", "i", 56) + [("−", "g", 56, Q.ELETRON)] + ps("embaixo", "i", 56), TX + TW - 10, 390, "right", 0.08)
            E.frase(c, t, C["s10.b"] + 0.4, ps("o feixe se curva para o", "i", 62) + [("+", "g", 62, COR)], XE, 880, passo=0.1)
            E.frase(c, t, C["s10.c"], [("→", "g", 60, TINTA2)] + ps("feito de partículas", "i", 62) + [("negativas", "g", 58, Q.ELETRON)], XE, 970, passo=0.1)
            if t >= C["s10.d"]:
                def metais():
                    for k, s in enumerate(("ferro", "cobre", "alumínio")):
                        E.foco(c, t, C["s10.d"] + 0.3 * k, 0.4, lambda a, k=k, s=s: E.pilula(c, s, 1380 + 170 * k, 900, 40, "b", fundo=TINTA, a=a))
                    E.foco(c, t, C["s10.d"] + 1.0, 0.4, lambda a: centro(c, "em todos os átomos", 1550, 990, 46, "i", TINTA2, a))
                E.saida(c, t, C["s10.e"] - 0.1, metais)
            E.foco(c, t, C["s10.e"], 0.5, lambda a: (E.bola(c, 1480, 930, 100, Q.ELETRON, a), centro(c, "elétron", 1480, 948, 50, "g", BR, a)))
        return
    # s11: o átomo pode ser dividido
    E.frase(c, t, C["s11.a"], ps("o elétron é um", "i", 76) + [("pedaço", "g", 72, COR)] + ps("do átomo", "i", 76), W / 2, 230, "center", 0.12)
    sai = ease_io(prog(t, C["s11.a"] + 0.8, 1.0))
    dalton(c, 600, 600, 180, ep(t, C["s11"], 0.4), cinza=ep(t, C["s11.c"], 0.5))
    eletron(c, 600 + 120 + 260 * sai, 600 - 60 - 120 * sai, 30, ep(t, C["s11.a"] + 0.6, 0.3))
    E.frase(c, t, C["s11.b"], ps("o átomo pode ser", "i", 72) + [("dividido", "g", 70, COR)], 1050, 600, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("Dalton:", "i", 62, TINTA2) + [("indivisível", "g", 58, TINTA2)], 1050, 760, passo=0.12)
    if t >= C["s11.c"] + 0.8:
        E.risco(c, 1280, 785, 1640, 725, t, C["s11.c"] + 0.8, largura=10)


# ---------------- o pudim ----------------
def b_pudim(c, t, C, b):
    if t < C["s13"]:
        E.frase(c, t, C["s12"], ps("o modelo de", "i", 76) + [("Thomson", "g", 72, COR)], XE, 200, passo=0.12)
        pudim(c, t, C["s12.a"], 1400, 560, 270, te=C["s12.b"])
        E.frase(c, t, C["s12.a"] + 0.3, ps("esfera de carga", "i", 66) + [("positiva", "g", 62, COR)], XE, 360, passo=0.1)
        E.frase(c, t, C["s12.b"] + 0.3, ps("com", "i", 66) + [("elétrons", "g", 62, Q.ELETRON)] + ps("espalhados", "i", 66), XE, 470, passo=0.1)
        pilula_em(c, t, C["s12.c"], "pudim de passas", XE + 250, 590, 56, TINTA)
        E.frase(c, t, C["s12.d"], [("+", "g", 70, COR), ("e", "i", 70), ("−", "g", 70, Q.ELETRON)] + ps("se equilibram", "i", 70), XE, 760, passo=0.12)
        E.frase(c, t, C["s12.e"], ps("átomo", "i", 70) + [("neutro,", "g", 70, COR)] + ps("sem carga", "i", 70), XE, 870, passo=0.12)
        E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: E.pilula(c, "Thomson", 1400, 900, 46, "g", fundo=TINTA, a=a))
        return
    # s13: e o pente? elétrons passam no atrito
    E.frase(c, t, C["s13"], ps("e o pente?", "i", 84), XE, 200)
    E.foco(c, t, C["s13"] + 0.4, 0.5, lambda a: pente(c, 1080, 280, 600, 120, a))
    for k in range(5):
        q = ease_io(prog(t, C["s13.a"] + 0.2 * k, 0.7))
        if q > 0:
            eletron(c, 1120 + 120 * k, lerp(700, 300, q), 20)
    E.frase(c, t, C["s13.a"], ps("no atrito,", "i", 64) + [("elétrons", "g", 60, Q.ELETRON)] + ps("passam", "i", 64), XE, 340, passo=0.1)
    E.frase(c, t, C["s13.b"], ps("ganhou elétrons:", "i", 64), XE, 480, passo=0.1)
    F.carga(c, t, C["s13.b"] + 0.5, XE + 560, 460, 40, "−")
    E.frase(c, t, C["s13.b"] + 0.6, [("negativo", "g", 58, Q.ELETRON)], XE + 620, 480)
    E.frase(c, t, C["s13.c"], ps("perdeu elétrons:", "i", 64), XE, 600, passo=0.1)
    F.carga(c, t, C["s13.c"] + 0.5, XE + 560, 580, 40, "+")
    E.frase(c, t, C["s13.c"] + 0.6, [("positivo", "g", 58, COR)], XE + 620, 600)
    papeis(c, t, C["s13.d"], 1110, 920, 400)
    if t < C["s13.d"]:
        papeis(c, t, None, 1110, 920, 400)
    E.frase(c, t, C["s13.d"] + 0.4, ps("o pente carregado", "i", 64) + [("atrai", "g", 60, COR)] + ps("o papel", "i", 64), XE, 820, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("Thomson descobriu o", "i", 70) + [("núcleo?", "g", 66, ERRADO)], XE, 320, passo=0.12)
    if t >= C["s14.a"] + 1.6:
        E.risco(c, XE, 340, XE + 880, 270, t, C["s14.a"] + 1.6, largura=12)
    pudim(c, t, C["s14.b"], 1420, 560, 230, te=C["s14.b"])
    E.frase(c, t, C["s14.b"] + 0.3, ps("no pudim", "i", 66) + [("não há núcleo", "g", 62)], XE, 480, passo=0.1)
    E.frase(c, t, C["s14.c"], ps("o", "i", 66) + [("+", "g", 66, COR)] + ps("está espalhado pela esfera toda", "i", 62), XE, 590, passo=0.1)
    if t >= C["s14.c"]:
        q = ep(t, C["s14.c"], 0.5)
        c.drawCircle(1420, 560, 252 + 6 * math.sin(t * 4), M.paint(E.COR, q, stroke=6))
    E.frase(c, t, C["s14.d"], ps("Thomson descobriu o", "i", 70) + [("elétron", "g", 66, Q.ELETRON)], XE, 760, passo=0.12)
    E.foco(c, t, C["s14.d"] + 1.2, 0.4, lambda a: E.selo(c, XE + 1000, 735, 40, True, a))
    pilula_em(c, t, C["s14.e"], "o núcleo: próxima aula", XE + 260, 900, 50, E.COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o atalho de prova:", "i", 72, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, C["s15.a"], [("palavra-chave", "g", 80, BR)] + ps("do enunciado", "i", 76, CLARO), W / 2, 270, "center", 0.12)
        cols = ((C["s15.b"], C["s15.c"], 520, "Dalton", ("indivisível", "sem partes", "bola de bilhar"), "d"),
                (C["s15.d"], C["s15.e"], 1400, "Thomson", ("elétrons", "esfera positiva", "pudim de passas"), "t"))
        for tk, tn, cx, nome, palavras, tipo in cols:
            for k, s in enumerate(palavras):
                E.foco(c, t, tk + 0.35 * k, 0.4, lambda a, s=s, k=k, cx=cx: E.pilula(c, s, cx, 420 + 95 * k, 46, "b", fundo="#22232B", a=a, cor=BR))
            E.foco(c, t, tn, 0.5, lambda a, cx=cx, tipo=tipo: (dalton(c, cx, 800, 110, a) if tipo == "d" else pudim(c, t, None, cx, 800, 110, None, a)))
            E.foco(c, t, tn + 0.2, 0.4, lambda a, cx=cx, nome=nome: E.pilula(c, nome, cx, 980, 56, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s16.a"], ps("cada modelo nasceu de uma", "i", 70, CLARO) + [("ideia central", "g", 66, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s16.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 68, CLARO)] + ps("pediu o motivo da troca?", "i", 68, CLARO), W / 2, 420, "center", 0.12)
    E.frase(c, t, C["s16.c"], ps("lembre do", "i", 70, CLARO) + [("fato", "g", 66, BR)], W / 2, 540, "center", 0.12)
    tf = C["s16.c"] + 0.8
    E.foco(c, t, tf, 0.5, lambda a: dalton(c, 560, 780, 100, a))
    E.ponte(c, t, tf + 0.5, 700, 1220, 780, "o elétron", E.COR, 44)
    E.foco(c, t, tf + 1.0, 0.5, lambda a: pudim(c, t, None, 1360, 780, 100, None, a))
    E.frase(c, t, tf + 1.4, ps("o átomo se divide", "i", 60, CLARO), W / 2, 980, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s17"] + 1.0, ps("um texto descreve o átomo:", "i", 62, TINTA2), XE, 290, passo=0.1)
    def citacao(a):
        M.rrect(c, XE, 340, 1000, 230, 24, "#FFFFFF", a, shadow=True)
        M.rrect(c, XE, 340, 14, 230, 6, E.COR, a)
        E.escreve(c, "“uma esfera de carga positiva,", XE + 50, 430, 54, "i", TINTA, a)
        E.escreve(c, "com partículas negativas presas nela”", XE + 50, 510, 54, "i", TINTA, a)
    E.foco(c, t, C["s17.a"], 0.6, citacao)
    E.frase(c, t, C["s17.b"], [("1", "g", 56, COR)] + ps("que modelo é esse?", "i", 62), XE, 720, passo=0.1)
    E.frase(c, t, C["s17.c"], [("2", "g", 56, COR)] + ps("que descoberta derrubou", "i", 62), XE, 830, passo=0.1)
    E.frase(c, t, C["s17.c"] + 1.4, ps("o modelo anterior?", "i", 62), XE + 60, 920, passo=0.1)
    if t < C["s18"]:
        E.foco(c, t, C["s17.a"] + 0.6, 0.6, lambda a: E.simbolo(c, 1560, 460, 170 * a, giro=6 * math.sin(t * 0.5)), blur=0)
    else:
        E.relogio(c, t, C["s18.a"], cx=1530, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s19.a"], ps("esfera positiva + partículas negativas", "i", 60, TINTA2), XE, 190, passo=0.08)
    pudim(c, t, C["s19.a"] + 0.4, 560, 500, 200, te=C["s19.a"] + 0.8)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "Thomson", 560, 770, 60, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s19.b"] + 0.4, 0.4, lambda a: centro(c, "pudim de passas", 560, 860, 48, "i", TINTA2, a))
    E.frase(c, t, C["s19.c"], ps("o anterior:", "i", 60, TINTA2), 1060, 320, passo=0.1)
    E.foco(c, t, C["s19.c"] + 0.3, 0.5, lambda a: dalton(c, 1500, 460, 130, a, cinza=ep(t, C["s19.d"] + 0.6, 0.5)))
    E.foco(c, t, C["s19.c"] + 0.6, 0.4, lambda a: E.pilula(c, "Dalton", 1500, 650, 46, "g", fundo=TINTA, a=a))
    if t >= C["s19.d"] + 0.8:
        E.risco(c, 1370, 600, 1630, 330, t, C["s19.d"] + 0.8, largura=10)
    E.frase(c, t, C["s19.d"], ps("caiu com a descoberta do", "i", 60) + [("elétron", "g", 58, Q.ELETRON)], 1060, 800, passo=0.1)
    E.frase(c, t, C["s19.e"], ps("o átomo tem partes:", "i", 58, TINTA2) + [("divisível", "g", 56, COR)], 1060, 900, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        dalton(c, 500, 480, 150 * ease_back(prog(t, C["s20.a"], 0.6)))
        E.frase(c, t, C["s20.a"] + 0.3, [("Dalton", "g", 64)], 500, 720, "center")
        E.frase(c, t, C["s20.a"] + 0.6, ps("maciça e indivisível", "i", 52, TINTA2), 500, 800, "center", 0.08)
        E.ponte(c, t, C["s20.c"], 700, 1200, 480, "o elétron", E.COR, 44)
        pudim(c, t, C["s20.b"], 1400, 480, 150, te=C["s20.b"] + 0.3)
        E.frase(c, t, C["s20.b"] + 0.3, [("Thomson", "g", 64, COR)], 1400, 720, "center")
        E.frase(c, t, C["s20.b"] + 0.6, ps("esfera positiva com elétrons", "i", 52, TINTA2), 1400, 800, "center", 0.08)
        E.frase(c, t, C["s20.c"] + 0.6, ps("o átomo se divide", "i", 60), W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], ps("uma folha de", "i", 80) + [("ouro", "g", 100, COR)], XE, 400)
    E.foco(c, t, C["s21.a"] + 0.4, 0.5, lambda a: M.rrect(c, XE + 40, 470, 18, 300, 4, "#D8B24A", a))
    for k in range(5):
        q = ep(t, C["s21.b"] + 0.15 * k, 0.4)
        if q > 0:
            x = lerp(XE + 520, XE - 30, ease_io(prog(t, C["s21.b"] + 0.15 * k, 1.2)))
            E.bola(c, x, 520 + 55 * k, 12, E.COR, q)
    E.frase(c, t, C["s21.b"], ps("derruba o pudim", "i", 64), XE + 140, 560, passo=0.1)
    E.frase(c, t, C["s21.c"], ps("e revela o", "i", 64) + [("núcleo", "g", 62, COR)], XE + 140, 680, passo=0.1)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, modelo=b_modelo, dalton=b_dalton, eletrico=b_eletrico, thomson=b_thomson,
              pudim=b_pudim, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
