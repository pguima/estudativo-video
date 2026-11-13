"""Visual — Estudativo · QUI-INO-009: síntese, análise e combustão.
Linguagem visual: a da Química (QUI-MIS-001), a da trilha (QUI-INO-007) e a do módulo (QUI-INO-008). Tipo de reação = blocos
coloridos (pecas): síntese junta, análise separa. Combustão = chama azul (completa) ou amarela com fuligem (incompleta)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-009_sintese_analise_combustao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('sintese', 'analise', 'combustao', 'atalho', 'questao', 'fim'))
BR = "#FFFFFF"
ACIDO, BASE, NEUTRO = "#E8602C", "#4B3FB5", TINTA2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns da trilha (as mesmas da QUI-INO-007; candidatas ao kit) ----------------
def clampf(v):
    return max(0.0, min(1.0, v))


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else BR, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, y=y, i=i: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def promessa(c, t, t0, itens, x=XE, y0=460, dy=170):
    """a promessa do gancho: 'até o fim da aula' + lista + hexágono da Química"""
    tb = t0 + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 540, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, t0, ps("até o fim da aula", "i", 88), x, 280, passo=0.14)
    lista(c, t, itens, x, y0, dy)


def lado(c, t, t0, x0, x1, y, rot, cor, sub=None, size=54):
    """chave embaixo de um trecho da equação, com o nome"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.chave(c, x0, x1, y, cor, p, 26)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, (x0 + x1) / 2, y + 90, size, "g", cor, a))
    if sub:
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: centro(c, sub, (x0 + x1) / 2, y + 150, 44, "i", TINTA2, a))


def selo_carga(c, cx, cy, r, carga, a=1.0):
    pos = "+" in carga
    E.bola(c, cx, cy, r, "#F2A516" if pos else Q.ELETRON, a)
    centro(c, carga.replace("-", "−"), cx, cy + r * 0.42, r * 1.15, "g", BR, a)


def ion(c, cx, cy, r, s, carga, a=1.0, escuro=False, cor=None):
    """íon: bolinha do elemento (ou esfera de grupo com a fórmula dentro) e a carga num selo no alto à direita"""
    if a <= 0 or r <= 0:
        return
    if s in Q.NOMES and cor is None:
        Q.atomo(c, cx, cy, r, s, a, escuro=escuro)
    else:
        E.bola(c, cx, cy, r, cor or "#6E6E76", a)
        sz = r * (0.95 if len(s) <= 2 else 0.75 if len(s) <= 3 else 0.6)
        Q.formula(c, s, cx, cy + sz * 0.36, sz, BR, a, "center")
    selo_carga(c, cx + r * 0.8, cy - r * 0.8, max(18, r * 0.38), carga, a)


def ion_em(c, t, t0, cx, cy, r, s, carga, cor=None, escuro=False):
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        ion(c, cx, cy, r * k, s, carga, min(1.0, prog(t, t0, 0.25)), escuro, cor)


def frasco_fechado(c, t, t0, cx, yb, w=220, h=260, particulas=None, cor=None):
    """erlenmeyer com rolha: o sistema fechado"""
    Q.erlenmeyer(c, t, t0, cx, yb, w, h, 0.0 if not cor else 0.3, cor or Q.AGUA, particulas=particulas)
    q = ep(t, t0 + 0.2, 0.4)
    if q > 0:
        M.rrect(c, cx - w * 0.16, yb - h - 34, w * 0.32, 52, 10, "#8B5E3C", q)


def caixa(c, t, t0, x, y, w, h, cor=None, t1=None):
    """caixa pontilhada que se desenha em volta de um trecho"""
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)


def questao(c, t, C, sq, linhas, sp, desenho=None, titulo="hora de testar"):
    """tela da questão: texto à esquerda (linhas = [(instante, partes, y)]), desenho à direita até a pausa, e o relógio"""
    E.frase(c, t, C[sq], ps(titulo, "i", 72, COR), XE, 180)
    for ti, partes, y in linhas:
        E.frase(c, t, ti, partes, XE, y, passo=0.08)
    if t < C[sp]:
        if desenho:
            desenho()
    else:
        E.relogio(c, t, C[sp + ".a"], cx=1500, cy=470, r=200)


def fim(c, t, C, sr, itens, sp, l1, l2, k_insc, k_bons, desenho=None, dy=180):
    """fechamento: resumo numerado, depois a próxima aula, inscreva-se e bons estudos"""
    def resumo():
        E.frase(c, t, C[sr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * dy
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[sp] - 0.1, resumo)
    if t < C[sp]:
        return
    E.frase(c, t, C[sp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[sp] + 0.6, [(l1, "g", 110, COR)], XE, 400)
    if l2:
        E.frase(c, t, C[sp] + 1.0, [(l2, "g", 110, COR)], XE, 530)
    if desenho:
        desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


def palco_titulo(c, t, t0, txt):
    E.frase(c, t, t0, ps(txt, "i", 72, CLARO), W / 2, 150, "center", 0.12)


# ======================== desta aula ========================
for eq in ("2 H2 + O2 -> 2 H2O", "N2 + 3 H2 -> 2 NH3", "2 H2O2 -> 2 H2O + O2", "CaCO3 -> CaO + CO2", "CH4 + 2 O2 -> CO2 + 2 H2O",
           "2 CH4 + 3 O2 -> 2 CO + 4 H2O", "CH4 + O2 -> C + 2 H2O", "C + O2 -> CO2", "2 HgO -> 2 Hg + O2", "CaO + CO2 -> CaCO3",
           "2 C4H10 + 13 O2 -> 8 CO2 + 10 H2O", "2 C4H10 + 9 O2 -> 8 CO + 10 H2O"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
SIN, ANA, COMB = "#2B8FD6", "#8E5BD0", "#E8602C"


def pecas(c, t, t0, cx, cy, p, junta=True, s=90):
    """dois blocos que se encaixam (síntese, p 0→1) ou se separam (análise)"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    e = ease_io(p if junta else 1 - p)
    gap = lerp(140, 0, e)
    M.rrect(c, cx - s - gap / 2, cy - s / 2, s, s, 16, "#2B8FD6", q, shadow=True)
    M.rrect(c, cx + gap / 2, cy - s / 2, s, s, 16, "#F2A516", q, shadow=True)


def chama2(c, cx, cy, s, t, cor="azul", a=1.0):
    if a <= 0:
        return
    tr = 1 + 0.06 * math.sin(t * 17) + 0.04 * math.sin(t * 29)
    cores = (("#2B6FD6", "#7FB2FF", "#E6F0FF") if cor == "azul" else ("#FF8A1F", "#FFD34D", "#FFF7D6"))
    for k, cc in zip((1.0, 0.62, 0.3), cores):
        hh, ww = s * 2.2 * k * tr, s * 0.62 * k
        pth = skia.Path()
        pth.moveTo(cx, cy - hh)
        pth.cubicTo(cx + ww * 1.2, cy - hh * 0.45, cx + ww, cy + s * 0.1 * k, cx, cy + s * 0.12 * k)
        pth.cubicTo(cx - ww, cy + s * 0.1 * k, cx - ww * 1.2, cy - hh * 0.45, cx, cy - hh)
        c.drawPath(pth, M.paint(cc, a * 0.92))
    if cor != "azul":
        for k in range(5):
            f = (t * 0.4 + k / 5) % 1
            c.drawCircle(cx - 20 + 10 * k, cy - s * 2.4 - f * 200, 10 + 6 * f, M.paint("#2A2B31", a * 0.6 * (1 - f)))


def fogao(c, cx, cy, cor, t, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 160, cy, 320, 40, 10, "#5B6470", a)
    for dx in (-60, 0, 60):
        chama2(c, cx + dx, cy - 4, 34, t + dx, cor, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a chama do fogão deve ser", "i", 76) + [("azul", "g", 72, "#2B6FD6")], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.b"], [("amarela", "g", 72, "#E09A10")] + ps("e com fuligem?", "i", 76), XE, 420, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("outra reação", "i", 76, TINTA2), XE, 560, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("pode soltar um gás que mata,", "i", 66) + [("sem cheiro", "g", 62, ERRADO)], XE, 760, passo=0.1)
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: fogao(c, 1500, 560, "azul" if t < C["s01.b"] else "amarela", t, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("síntese", "g", 70, SIN), ("ou", "i", 74), ("análise", "g", 70, ANA)]),
                              (C["s02.b"], [("o", "i", 74), ("que", "i", 74), ("sai", "i", 74), ("da", "i", 74), ("queima", "g", 70, COMB)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 80, TINTA2), XE, 200)
    cs = Q.equacao(c, t, C["s03.a"], "2 H2 + O2 -> 2 H2O", W / 2, 450, 130, passo=0.25, cores={"coef": E.COR})
    lado(c, t, C["s03.a"] + 0.6, cs[0] - 130, cs[1] + 90, 520, "reagentes", TINTA2)
    lado(c, t, C["s03.a"] + 1.0, cs[2] - 140, cs[2] + 140, 520, "produtos", COR)
    E.frase(c, t, C["s03.b"], ps("balancear: coeficientes na ordem", "i", 64) + [("MACHO", "g", 62, COR)], W / 2, 860, "center", 0.12)


# ---------------- síntese ----------------
def b_sintese(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("síntese:", "g", 90, SIN)] + ps("várias formam uma só", "i", 80), XE, 230, passo=0.14)
    pecas(c, t, C["s04.b"], 1640, 200, prog(t, C["s04.b"], 1.0), True)
    if t < C["s05"]:
        Q.equacao(c, t, C["s04.c"], "2 H2 + O2 -> 2 H2O", W / 2, 640, 140, passo=0.3)
        E.frase(c, t, C["s04.d"], ps("hidrogênio e oxigênio viram", "i", 66) + [("água", "g", 62, COR)], W / 2, 830, "center", 0.12)
        return
    cs = Q.equacao(c, t, C["s05.a"], "N2 + 3 H2 -> 2 NH3", W / 2, 640, 140, passo=0.3)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: centro(c, "amônia: matéria-prima dos adubos", cs[2], 760, 46, "i", TINTA2, a))
    E.frase(c, t, C["s05.c"], [("2", "g", 66, SIN)] + ps("entram,", "i", 70) + [("1", "g", 66, SIN)] + ps("sai", "i", 70), W / 2, 900, "center", 0.12)
    pilula_em(c, t, C["s05.d"], "síntese ou adição", W / 2, 1000, 46, SIN)


# ---------------- análise ----------------
def b_analise(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("análise:", "g", 90, ANA)] + ps("uma se quebra em várias", "i", 80), XE, 230, passo=0.14)
    pecas(c, t, C["s06.b"], 1640, 200, prog(t, C["s06.b"], 1.0), False)
    if t < C["s07"]:
        E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: E.escreve(c, "ou decomposição", XE, 330, 54, "i", TINTA2, a))
        Q.equacao(c, t, C["s06.c"], "2 H2O2 -> 2 H2O + O2", W / 2, 640, 140, passo=0.3)
        E.frase(c, t, C["s06.d"], ps("as bolhas no machucado são", "i", 64) + [("oxigênio", "g", 60, COR)], W / 2, 840, "center", 0.12)
        return
    E.frase(c, t, C["s07.a"], ps("muitas precisam de energia", "i", 64, TINTA2), XE, 340, passo=0.1)
    cs = Q.equacao(c, t, C["s07.b"], "CaCO3 ->{Δ} CaO + CO2", W / 2, 560, 130, tl=[C["s07.b"], C["s07.b"] + 0.6, C["s07.c"], C["s07.c"] + 0.3, C["s07.c"] + 0.6])
    E.foco(c, t, C["s07.b"] + 0.4, 0.4, lambda a: centro(c, "calcário", cs[0], 680, 46, "i", TINTA2, a))
    E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: centro(c, "cal", cs[1], 680, 46, "i", TINTA2, a))
    for i, (k, nome, fonte) in enumerate((("s07.d", "pirólise", "calor"), ("s07.e", "fotólise", "luz"), ("s07.f", "eletrólise", "corrente elétrica"))):
        x = 420 + i * 540
        pilula_em(c, t, C[k], nome, x, 840, 54, ANA)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, fonte=fonte: centro(c, fonte, x, 940, 50, "i", TINTA, a))


# ---------------- combustão ----------------
def b_combustao(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("combustão", "g", 110, COMB)] + ps("= a queima", "i", 90) if False else [("combustão:", "g", 110, COMB)] + ps("a queima", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, C["s08.b"], [("combustível", "g", 70), ("+", "g", 70, TINTA2), ("O₂", "g", 70, COR)], XE, 480, passo=0.14)
        E.foco(c, t, C["s08.b"] + 1.0, 0.4, lambda a: E.escreve(c, "o comburente", XE + 560, 540, 54, "i", TINTA2, a))
        E.frase(c, t, C["s08.c"], ps("libera", "i", 70) + [("calor", "g", 66, COMB), ("e", "i", 70), ("luz", "g", 66, COMB)], XE, 700, passo=0.12)
        E.foco(c, t, C["s08.a"] + 0.4, 0.5, lambda a: chama2(c, 1550, 720, 110, t, "azul", a))
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("oxigênio de sobra:", "i", 70) + [("completa", "g", 66, "#2B6FD6")], XE, 220, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("combustível de C e H dá", "i", 62, TINTA2), XE, 340, passo=0.1)
        E.frase(c, t, C["s09.c"], [("CO₂", "g", 66, COR), ("+", "g", 66, TINTA2), ("H₂O", "g", 66, COR)], XE + 680, 340, passo=0.14)
        Q.equacao(c, t, C["s09.d"], "CH4 + 2 O2 -> CO2 + 2 H2O", W / 2, 600, 120, tl=[C["s09.d"], C["s09.d"] + 0.4, C["s09.d"] + 0.8, C["s09.e"] - 0.2, C["s09.e"], C["s09.e"] + 0.3, C["s09.e"] + 0.5])
        E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.escreve(c, "metano, do gás natural", XE, 720, 50, "i", TINTA2, a))
        E.foco(c, t, C["s09.a"] + 0.3, 0.5, lambda a: fogao(c, 1500, 940, "azul", t, a))
        return
    E.frase(c, t, C["s10.a"], ps("pouco oxigênio:", "i", 70) + [("incompleta", "g", 66, "#E09A10")], XE, 220, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("o carbono não chega a", "i", 62, TINTA2) + [("CO₂", "g", 58)], XE, 330, passo=0.1)
    if t < C["s11"]:
        pilula_em(c, t, C["s10.c"], "CO: monóxido de carbono", 560, 520, 54, ERRADO)
        pilula_em(c, t, C["s10.d"], "C: fuligem", 560, 660, 54, "#2A2B31")
        E.frase(c, t, C["s10.e"], ps("e a água continua saindo", "i", 62), XE, 820, passo=0.1)
    else:
        Q.equacao(c, t, C["s11.a"], "2 CH4 + 3 O2 -> 2 CO + 4 H2O", W / 2, 560, 110, passo=0.3)
        E.frase(c, t, C["s11.b"], ps("menos oxigênio entra", "i", 60), XE, 720, passo=0.1)
        E.frase(c, t, C["s11.c"], ps("cada carbono sai com", "i", 60) + [("um O só", "g", 56, ERRADO)], XE, 820, passo=0.1)
        pilula_em(c, t, C["s11.d"], "CO: sem cheiro, toma o lugar do O₂ no sangue", W / 2, 960, 44, ERRADO)
    E.foco(c, t, C["s10.a"] + 0.3, 0.5, lambda a: fogao(c, 1500, 900 if t < C["s11"] else 420, "amarela", t, a * (1 if t < C["s11"] else 0.0)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("toda queima solta CO₂?", "i", 74) if False else ps("toda queima solta", "i", 74) + [("CO₂?", "g", 70)], XE + 450, 190, passo=0.12)
    for i, (nome, prod, cor) in enumerate((("completa", "CO2 + H2O", "azul"), ("incompleta", "CO ou C + H2O", "amarela"))):
        x = 560 + i * 800
        E.foco(c, t, C["s12.b"] - 0.6 + 1.0 * i, 0.5, lambda a, x=x, cor=cor: fogao(c, x, 600, cor, t, a))
        E.foco(c, t, C["s12.b"] - 0.4 + 1.0 * i, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 720, 60, "g", TINTA, a))
        Q.formula_em(c, t, C["s12.b"] + 1.0 * i - 0.2, prod, x, 830, 76, align="center", cor=ERRADO if i else None)
    E.frase(c, t, C["s12.c"], ps("o", "i", 66) + [("monóxido", "g", 62, ERRADO)] + ps("envenena em lugar fechado", "i", 66), W / 2, 990, "center", 0.12)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        palco_titulo(c, t, C["s13"], "o atalho de prova")
        E.frase(c, t, C["s13.a"], ps("conte as substâncias", "i", 66, CLARO) + [("diferentes", "g", 62, BR)] + ps("(sem olhar coeficientes)", "i", 56, CLARO), W / 2, 270, "center", 0.1)
        for i, (k, a_, b_, rot, cor) in enumerate((("s13.b", "várias", "1", "síntese", SIN), ("s13.c", "1", "várias", "análise", ANA), ("s13.d", "combustível + O₂", "calor", "combustão", COMB))):
            y = 430 + i * 130
            E.foco(c, t, C[k], 0.4, lambda a, a_=a_, b_=b_, y=y: (E.escreve(c, a_, 300, y, 62, "g", BR, a), E.escreve(c, "→ " + b_, 920, y, 62, "g", CLARO, a)))
            pilula_em(c, t, C[k] + 0.3, rot, 1520, y - 22, 52, cor)
        E.frase(c, t, C["s13.e"], ps("completa:", "i", 62, CLARO) + [("C → CO₂", "g", 60, BR), ("H → H₂O", "g", 60, BR)], W / 2, 900, "center", 0.12)
        return
    palco_titulo(c, t, C["s14"], "funciona porque")
    E.frase(c, t, C["s14.a"], ps("o tipo depende de", "i", 66, CLARO) + [("quantas entram e quantas saem", "g", 60, BR)], W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("cuidado:", "g", 62, ERRADO)] + ps("uma queima pode ser síntese também", "i", 64, CLARO), W / 2, 460, "center", 0.1)
    Q.formula_em(c, t, C["s14.c"], "C + O2 -> CO2", W / 2, 650, 130, align="center", escuro=True)
    E.frase(c, t, C["s14.d"], ps("o enunciado fala em queima?", "i", 64, CLARO), W / 2, 860, "center", 0.12)
    pilula_em(c, t, C["s14.d"] + 1.0, "combustão", W / 2, 960, 56, COMB)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        pass
    E.frase(c, t, C["s15"], ps("hora de testar: classifique", "i", 72, COR), XE, 180, passo=0.12)
    Q.formula_em(c, t, C["s15.a"], "2 HgO ->{Δ} 2 Hg + O2", XE + 100, 360, 96)
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (E.bola(c, XE + 30, 330, 34, a=a), centro(c, "1", XE + 30, 346, 44, "g", BR, a)))
    Q.formula_em(c, t, C["s15.b"], "CaO + CO2 -> CaCO3", XE + 100, 520, 96)
    E.foco(c, t, C["s15.b"], 0.4, lambda a: (E.bola(c, XE + 30, 490, 34, a=a), centro(c, "2", XE + 30, 506, 44, "g", BR, a)))
    E.foco(c, t, C["s15.c"], 0.4, lambda a: (E.bola(c, XE + 30, 650, 34, a=a), centro(c, "3", XE + 30, 666, 44, "g", BR, a)))
    E.frase(c, t, C["s15.c"], ps("queima completa e incompleta do butano", "i", 58), XE + 100, 680, passo=0.08)
    Q.formula_em(c, t, C["s15.c"] + 1.2, "C4H10", XE + 100, 800, 96)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1560, cy=640, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.formula_em(c, t, C["s17"], "2 HgO ->{Δ} 2 Hg + O2", XE, 260, 90)
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "uma vira duas", XE + 1000, 250, 54, "i", TINTA2, a))
    pilula_em(c, t, C["s17.b"], "análise (pirólise)", 1550, 340, 46, ANA)
    Q.formula_em(c, t, C["s17"] + 0.3, "CaO + CO2 -> CaCO3", XE, 460, 90)
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.escreve(c, "duas viram uma", XE + 1000, 450, 54, "i", TINTA2, a))
    pilula_em(c, t, C["s17.d"], "síntese", 1550, 540, 46, SIN)
    if t >= C["s18"]:
        Q.formula_em(c, t, C["s18.a"], "C4H10", XE, 700, 90)
        E.frase(c, t, C["s18.b"], ps("completa:", "i", 60, "#2B6FD6") + [("CO₂ + H₂O", "g", 58)], XE + 360, 695, passo=0.1)
        E.frase(c, t, C["s18.c"], ps("incompleta:", "i", 60, "#E09A10") + [("CO", "g", 58, ERRADO)] + ps("ou", "i", 60) + [("C", "g", 58)] + [("+ H₂O", "g", 58)], XE + 360, 820, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        Q.equacao(c, t, C["s20.b"], "Zn + 2 HCl -> ZnCl2 + H2", 800, 820, 90, passo=0.3)
    fim(c, t, C, "s19", [("s19.a", [("síntese:", "g", 66, SIN), ("várias", "i", 72), ("→", "g", 66, TINTA2), ("uma", "i", 72)]),
                         ("s19.b", [("análise:", "g", 66, ANA), ("uma", "i", 72), ("→", "g", 66, TINTA2), ("várias", "i", 72)]),
                         ("s19.c", [("completa:", "g", 66, COMB), ("CO₂ + H₂O;", "g", 66), ("incompleta:", "g", 66, COMB), ("CO", "g", 66)])],
        "s20", "Simples troca", None, "s20.c", "s20.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sintese=b_sintese, analise=b_analise, combustao=b_combustao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
