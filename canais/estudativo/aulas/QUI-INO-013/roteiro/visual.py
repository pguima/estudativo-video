"""Visual — Estudativo · QUI-INO-013: Brønsted-Lowry e Lewis.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). O H⁺ que passa de uma espécie para a
outra é uma bolinha H com selo + que salta num arco (salta_h). Pares conjugados = chave colorida ligando as duas fórmulas: par 1
em ACIDO, par 2 em BASE (par_conj). Lewis = Q.lewis com pares em azul; o par doado anda até o receptor."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-013_bronsted_lowry_lewis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('bronsted', 'pares', 'lewis', 'atalho', 'questao', 'fim'))
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
for eq in ("NH3 + H2O -> NH4^+ + OH^-", "HCl + H2O -> H3O^+ + Cl^-", "HNO3 + H2O -> H3O^+ + NO3^-", "NH3 + BF3 -> NH3BF3"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


def salta_h(c, t, t0, x0, x1, y, alto=160, d=1.0):
    """o H⁺ salta de x0 para x1 num arco"""
    p = prog(t, t0, d)
    if p <= 0 or p >= 1:
        return
    e = ease_io(p)
    x = lerp(x0, x1, e)
    yy = y - alto * math.sin(math.pi * e)
    ion(c, x, yy, 30, "H", "+", min(1, p * 4, (1 - p) * 4))


def par_conj(c, t, t0, xa, xb, y, cor, rot, baixo=True):
    """ligação de um par conjugado: colchete sob duas espécies"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    h = 60 if baixo else -60
    pth = skia.Path()
    pth.moveTo(xa, y); pth.lineTo(xa, y + h); pth.lineTo(xb, y + h); pth.lineTo(xb, y)
    m = skia.PathMeasure(pth, False)
    seg = skia.Path()
    m.getSegment(0, m.getLength() * ease_out(p), seg, True)
    c.drawPath(seg, M.paint(cor, 1, stroke=6))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot, (xa + xb) / 2, y + h + (60 if baixo else -24), 46, "b", cor, a))


EQ_NH3 = "NH3 + H2O -> NH4^+ + OH^-"
EQ_HCL = "HCl + H2O -> H3O^+ + Cl^-"
AMONIA = [("N", 0, 0, [90]), ("H", -1.05, 0.35, []), ("H", 1.05, 0.35, []), ("H", 0, 1.1, [])]
LIG_AM = [(0, 1, 1), (0, 2, 1), (0, 3, 1)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a amônia deixa a água", "i", 80) + [("básica", "g", 76, BASE)], XE, 260, passo=0.14)
        Q.formula_em(c, t, C["s01.a"] + 0.4, "NH3", XE, 470, 170)
        E.frase(c, t, C["s01.b"], ps("mas não tem", "i", 70) + [("OH", "g", 66, ERRADO)] + ps("na fórmula", "i", 70), XE, 640, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("pela regra de Arrhenius, nem seria base", "i", 62, TINTA2), XE, 760, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("a regra precisa", "i", 74) + [("crescer", "g", 70, COR)], XE, 920, passo=0.12)
        Q.molecula(c, t, C["s01.a"] + 0.3, "NH3", 1450, 500, 170, passo=0.15)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("Brønsted", "g", 70, COR), ("e", "i", 74), ("Lowry", "g", 70, COR)]),
                              (C["s02.b"], [("pares", "g", 70), ("conjugados", "g", 70)]),
                              (C["s02.c"], [("ácido", "g", 70, ACIDO), ("de", "i", 74), ("Lewis", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 80, TINTA2), XE, 200)
    ion_em(c, t, C["s03.a"], XE + 60, 340, 46, "H", "+")
    E.frase(c, t, C["s03.a"] + 0.3, [("H⁺", "g", 70, COR)] + [("=", "g", 62, TINTA2)] + ps("hidrogênio sem elétron:", "i", 66) + [("um próton", "g", 62)], XE + 140, 360, passo=0.1)
    E.frase(c, t, C["s03.b"], ps("Lewis: elétrons", "i", 66) + [("aos pares", "g", 62, Q.ELETRON)], XE, 540, passo=0.12)
    Q.lewis(c, t, C["s03.b"] + 0.4, AMONIA, LIG_AM, 1300, 650, escala=150, size=96, tp=C["s03.c"])
    E.frase(c, t, C["s03.c"], ps("o", "i", 66) + [("par livre", "g", 62, Q.ELETRON)] + ps("do nitrogênio", "i", 66), XE, 720, passo=0.12)
    if t >= C["s03.c"]:
        q = ep(t, C["s03.c"] + 0.3, 0.4)
        c.drawCircle(1300, 650 - 95, 46 + 3 * math.sin(t * 5), M.paint(Q.ELETRON, q, stroke=5))


# ---------------- Brønsted-Lowry ----------------
def b_bronsted(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("1923:", "i", 66, TINTA2) + [("Brønsted", "g", 66), ("e", "i", 70), ("Lowry", "g", 66)], XE, 220, passo=0.12)
        E.frase(c, t, C["s04.a"], [("ácido", "g", 110, ACIDO)] + ps("doa", "i", 100) + [("H⁺", "g", 110)], XE, 470, passo=0.16)
        E.frase(c, t, C["s04.b"], [("base", "g", 110, BASE)] + ps("recebe", "i", 100) + [("H⁺", "g", 110)], XE, 680, passo=0.16)
        salta_h(c, t, C["s04.b"] + 0.4, 1300, 1650, 600, 200, 1.4)
        return
    y = 330
    if t < C["s06"]:
        cs = Q.equacao(c, t, C["s05.a"], EQ_NH3, W / 2, y, 120, tl=[C["s05.a"], C["s05.a"] + 0.3, C["s05.a"] + 0.6, C["s05.b"] - 0.2, C["s05.b"], C["s05.c"] - 0.1, C["s05.c"]])
        salta_h(c, t, C["s05.d"], cs[1], cs[0], y - 140, 120, 1.0)
        pilula_em(c, t, C["s05.d"] + 0.4, "ácido: doou", cs[1], 520, 46, ACIDO)
        pilula_em(c, t, C["s05.e"], "base: recebeu", cs[0], 520, 46, BASE)
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: centro(c, "amônio", cs[2], 450, 46, "i", TINTA2, a))
        E.frase(c, t, C["s05.f"], ps("o", "i", 66) + [("OH⁻", "g", 62, BASE)] + ps("que sobrou deixa a água básica", "i", 66), W / 2, 760, "center", 0.12)
        ion_em(c, t, C["s05.f"] + 0.5, W / 2, 900, 56, "OH", "-", cor="#B3343A")
        return
    cs = Q.equacao(c, t, C["s06.a"], EQ_HCL, W / 2, y, 120, tl=[C["s06.a"], C["s06.a"] + 0.3, C["s06.a"] + 0.6, C["s06.b"] - 0.2, C["s06.b"], C["s06.b"] + 0.3, C["s06.b"] + 0.5])
    salta_h(c, t, C["s06.c"] - 0.6, cs[0], cs[1], y - 140, 120, 1.0)
    pilula_em(c, t, C["s06.c"], "ácido: doou", cs[0], 520, 46, ACIDO)
    pilula_em(c, t, C["s06.d"], "base: recebeu", cs[1], 520, 46, BASE)
    E.frase(c, t, C["s06.e"], ps("a água muda de papel:", "i", 66), W / 2, 760, "center", 0.12)
    pilula_em(c, t, C["s06.e"] + 1.6, "anfótera: ácido ou base", W / 2, 880, 56, E.COR)


# ---------------- pares ----------------
def b_pares(c, t, C, b):
    y = 360
    cs = Q.equacao(c, t, C["s07"], EQ_HCL, W / 2, y, 130, tl=[C["s07"]] * 7)
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("o HCl doa o", "i", 60, TINTA2) + [("H⁺", "g", 56)] + ps("e sobra o", "i", 60, TINTA2) + [("Cl⁻", "g", 56)], W / 2, 170, "center", 0.1)
    par_conj(c, t, C["s07.b"], cs[0], cs[3], y + 60, ACIDO, "ácido e base conjugada")
    E.frase(c, t, C["s07.c"], ps("diferem por um", "i", 62) + [("H⁺", "g", 58, COR)] + ps(", e só", "i", 62), W / 2, 640, "center", 0.12)
    if t >= C["s08"]:
        E.foco(c, t, C["s08.a"], 0.4, lambda a: centro(c, "Cl⁻: base conjugada do HCl", W / 2, 760, 52, "g", ACIDO, a))
        par_conj(c, t, C["s08.b"], cs[1], cs[2], y - 120, BASE, "base e ácido conjugado", baixo=False)
        E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "H₃O⁺: ácido conjugado da água", W / 2, 860, 52, "g", BASE, a))
    if t >= C["s09"]:
        E.frase(c, t, C["s09.a"], ps("sempre", "i", 64) + [("dois pares", "g", 60, COR)], W / 2, 970, "center", 0.12)


# ---------------- Lewis ----------------
def b_lewis(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("o americano", "i", 66, TINTA2) + [("Lewis", "g", 66)] + ps("olhou os elétrons", "i", 66, TINTA2), XE, 220, passo=0.12)
        E.frase(c, t, C["s10.a"], [("base", "g", 100, BASE)] + ps("doa um", "i", 90) + [("par", "g", 100, Q.ELETRON)], XE, 470, passo=0.16)
        E.frase(c, t, C["s10.b"], [("ácido", "g", 100, ACIDO)] + ps("recebe o", "i", 90) + [("par", "g", 100, Q.ELETRON)], XE, 680, passo=0.16)
        return
    if t < C["s12"]:
        Q.lewis(c, t, C["s11"], AMONIA, LIG_AM, 700, 600, escala=150, size=96, tp=C["s11"])
        p = ease_io(prog(t, C["s11.b"], 1.2))
        hx = lerp(1300, 700, p)
        if p < 1:
            ion(c, hx + 90, 440, 40, "H", "+")
        else:
            M.line(c, 700, 520, 700, 420, TINTA, 1, 8)
            Q.formula(c, "H", 700, 400, 96, TINTA, 1, "center")
        E.frase(c, t, C["s11.a"], ps("a amônia recebe um", "i", 64) + [("H⁺", "g", 60)], XE, 200, passo=0.12)
        E.frase(c, t, C["s11.c"], ps("doou o par:", "i", 62) + [("base de Lewis", "g", 60, BASE)], 1050, 640, passo=0.1)
        E.frase(c, t, C["s11.d"], ps("recebeu o par:", "i", 62) + [("ácido de Lewis", "g", 60, ACIDO)], 1050, 760, passo=0.1)
        Q.formula_em(c, t, C["s11.d"] + 1.2, "NH4^+", 1050, 940, 110)
        return
    E.frase(c, t, C["s12.a"], ps("ácido de Lewis", "i", 66) + [("sem H", "g", 62, ACIDO)], XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s12.b"], "BF3", XE, 380, 130)
    BF3 = [("B", 0, 0, []), ("F", 0, -1.1, [90, 0, 180]), ("F", -1.0, 0.6, [180, 240, 300]), ("F", 1.0, 0.6, [0, 300, 240])]
    Q.lewis(c, t, C["s12.b"] + 0.3, BF3, [(0, 1, 1), (0, 2, 1), (0, 3, 1)], 1400, 520, escala=140, size=80, tp=C["s12.b"] + 0.3)
    E.frase(c, t, C["s12.b"] + 0.6, ps("o boro tem só", "i", 62) + [("6 elétrons", "g", 58, Q.ELETRON)], XE, 520, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("falta", "i", 62) + [("um par", "g", 58)] + ps("para o octeto", "i", 62), XE, 630, passo=0.1)
    caixa(c, t, C["s12.c"] + 0.4, 1350, 610, 100, 70, E.COR)
    Q.formula_em(c, t, C["s12.d"], "NH3 + BF3 -> H3N–BF3", W / 2, 900, 90, align="center")
    pilula_em(c, t, C["s12.d"] + 0.8, "BF₃: ácido de Lewis", W / 2, 1010, 46, ACIDO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("cruzar os pares", "i", 74), XE + 450, 190, passo=0.12)
    y = 470
    cs = Q.equacao(c, t, C["s13"], EQ_HCL, W / 2, y, 130, tl=[C["s13"]] * 7)
    def errado():
        par_conj(c, t, C["s13.b"], cs[0], cs[2], y + 60, ERRADO, "ácido com ácido?")
        if t >= C["s13.c"]:
            E.risco(c, cs[0], y + 200, cs[2], y + 80, t, C["s13.c"], largura=9)
    E.saida(c, t, C["s13.d"], errado)
    par_conj(c, t, C["s13.d"], cs[0], cs[3], y + 60, ACIDO, "o ácido e a base que sobra dele")
    E.foco(c, t, C["s13.d"] + 0.8, 0.5, lambda a: E.selo(c, 1700, 850, 44, True, a))


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    palco_titulo(c, t, C["s14"], "o atalho de prova")
    E.frase(c, t, C["s14.a"], [("− H", "g", 66, BR)] + ps("e carga", "i", 64, CLARO) + [("−1:", "g", 62, CLARO)] + [("base conjugada", "g", 62, BR)], W / 2, 290, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("+ H", "g", 66, BR)] + ps("e carga", "i", 64, CLARO) + [("+1:", "g", 62, CLARO)] + [("ácido conjugado", "g", 62, BR)], W / 2, 400, "center", 0.12)
    Q.formula_em(c, t, C["s15.a"], "H2O", W / 2, 640, 140, align="center", escuro=True)
    E.foco(c, t, C["s15.a"] + 0.3, 0.4, lambda a: M.arrow(c, W / 2 - 160, 600, W / 2 - 400, 600, E.CLARO, a, 6, 22))
    Q.formula_em(c, t, C["s15.b"], "OH^-", W / 2 - 600, 640, 120, align="center", escuro=True)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: M.arrow(c, W / 2 + 160, 600, W / 2 + 400, 600, E.CLARO, a, 6, 22))
    Q.formula_em(c, t, C["s15.d"], "H3O^+", W / 2 + 600, 640, 120, align="center", escuro=True)
    E.frase(c, t, C["s15.e"], ps("o", "i", 62, CLARO) + [("H⁺", "g", 58, BR)] + ps("leva uma carga positiva", "i", 62, CLARO), W / 2, 820, "center", 0.12)
    E.frase(c, t, C["s15.f"], [("Lewis:", "g", 58, ERRADO)] + ps("sem H para contar; procure quem", "i", 60, CLARO) + [("recebe o par", "g", 56, BR)], W / 2, 950, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        Q.formula_em(c, t, C["s16.a"], "HNO3 + H2O", 1480, 400, 80, align="center")
        Q.formula_em(c, t, C["s16.b"], "-> H3O^+ + NO3^-", 1480, 540, 80, align="center")
        Q.formula_em(c, t, C["s16.e"], "Cl^- + AlCl3", 1480, 800, 80, align="center")
    questao(c, t, C, "s16", [(C["s16.c"], [("1", "g", 56, COR)] + ps("ácido e base de Brønsted?", "i", 60), 330),
                             (C["s16.d"], [("2", "g", 56, COR)] + ps("os dois pares conjugados?", "i", 60), 450),
                             (C["s16.e"], [("3", "g", 56, COR), ("Cl⁻", "g", 56), ("+", "g", 56, TINTA2), ("AlCl₃", "g", 56)], 640),
                             (C["s16.e"] + 0.8, ps("Al com só 6 elétrons: quem é o ácido de Lewis?", "i", 54, TINTA2), 740)], "s17", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y = 300
    eq = "HNO3 + H2O -> H3O^+ + NO3^-"
    cs = Q.equacao(c, t, C["s18"], eq, W / 2, y, 120, tl=[C["s18"]] * 7)
    pilula_em(c, t, C["s18.a"], "ácido", cs[0], 160, 44, ACIDO)
    pilula_em(c, t, C["s18.b"], "base", cs[1], 160, 44, BASE)
    par_conj(c, t, C["s18.c"], cs[0], cs[3], y + 50, ACIDO, "par 1")
    par_conj(c, t, C["s18.d"], cs[1], cs[2], y + 50 + 0, BASE, "par 2") if False else par_conj(c, t, C["s18.d"], cs[1], cs[2], y + 170, BASE, "par 2")
    if t >= C["s19"]:
        Q.formula_em(c, t, C["s19.a"], "Cl^- + AlCl3 -> AlCl4^-", W / 2, 760, 100, align="center")
        pilula_em(c, t, C["s19.b"], "Cl⁻: doa o par = base de Lewis", 620, 900, 44, BASE)
        pilula_em(c, t, C["s19.d"], "AlCl₃: recebe = ácido de Lewis", 1320, 1000, 44, ACIDO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        for i, f in enumerate(("HCl", "NaOH", "NaCl", "CaO")):
            Q.formula_em(c, t, C["s21.b"] + 0.3 * i, f, XE + i * 380, 820, 90)
    fim(c, t, C, "s20", [("s20.a", [("ácido", "g", 66, ACIDO), ("doa", "i", 72), ("H⁺,", "g", 66), ("base", "g", 66, BASE), ("recebe", "i", 72)]),
                         ("s20.b", [("par", "g", 66), ("conjugado:", "g", 66), ("um", "i", 72), ("H⁺", "g", 66, COR), ("de", "i", 72), ("diferença", "i", 72)]),
                         ("s20.c", [("ácido", "g", 66, ACIDO), ("de", "i", 72), ("Lewis:", "g", 66), ("recebe", "i", 72), ("o", "i", 72), ("par", "g", 66, Q.ELETRON)])],
        "s21", "Praticando", "o módulo", "s21.c", "s21.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, bronsted=b_bronsted, pares=b_pares, lewis=b_lewis, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
