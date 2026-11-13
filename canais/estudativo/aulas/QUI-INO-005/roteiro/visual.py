"""Visual — Estudativo · QUI-INO-005: escala de pH e indicadores.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). Escala de pH = Q.escala_ph, com o
marcador na fala; o indicador aparece como o líquido do béquer mudando de cor (Q.muda_cor). Peça nova: cor_repolho(ph),
as cores do extrato de repolho roxo (candidata ao kit, ao lado de Q.cor_indicador)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-005_escala_ph_indicadores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('escala', 'fenol', 'repolho', 'atalho', 'questao', 'fim'))
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
FENOL_ROSA = "#E85AA8"


def cor_repolho(ph):
    """cor do extrato de repolho roxo: vermelho/rosa no ácido, roxo no neutro, azul/verde no básico, amarelo no muito básico"""
    pts = [(1, "#D7263D"), (3, "#E0457B"), (5, "#B04A9E"), (7, "#7A3FA0"), (8.5, "#3E5FBF"), (10, "#2FA084"), (12, "#8DBF3A"), (14, "#E6C229")]
    for (a, ca), (b_, cb) in zip(pts, pts[1:]):
        if ph <= b_:
            return E.mix(ca, cb, max(0.0, min(1.0, (ph - a) / (b_ - a))))
    return pts[-1][1]


def cor_fenol(ph):
    return Q.AGUA if ph < 8.2 else FENOL_ROSA


ESX, ESY, ESW = 260, 520, 1400


def ph_x(ph):
    return ESX + ESW * ph / 14


def marca(c, t, t0, ph, rot, cor=TINTA, dy=0):
    """seta sobre a escala com o rótulo"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    x = ph_x(ph)
    M.arrow(c, x, ESY - 150 - dy, x, ESY - 50, cor, q, 5, 18)
    E.foco(c, t, t0, 0.4, lambda a: centro(c, rot, x, ESY - 170 - dy, 46, "b", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("suco de", "i", 80) + [("repolho roxo", "g", 76, "#7A3FA0")], XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("no vinagre:", "i", 70) + [("vermelho", "g", 66, cor_repolho(2.5))], XE, 420, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("no sabão em pó:", "i", 70) + [("verde", "g", 66, cor_repolho(10.5))], XE, 540, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("conta se é", "i", 64) + [("ácida", "g", 60, ACIDO)] + ps("ou", "i", 64) + [("básica", "g", 60, BASE)], XE, 760, passo=0.12)
        Q.bequer(c, t, C["s01.a"], 1340, 900, 280, 360, 0.7, lambda tt: Q.muda_cor(tt, C["s01.b"], cor_repolho(7), cor_repolho(2.5), 1.0))
        Q.bequer(c, t, C["s01.a"] + 0.2, 1680, 900, 280, 360, 0.7, lambda tt: Q.muda_cor(tt, C["s01.c"], cor_repolho(7), cor_repolho(10.5), 1.0))
        E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: centro(c, "vinagre", 1340, 980, 48, "i", TINTA2, a))
        E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: centro(c, "sabão em pó", 1680, 980, 48, "i", TINTA2, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("ler", "i", 74), ("a", "i", 74), ("escala", "g", 70, COR), ("de", "i", 74), ("pH", "g", 70, COR)]),
                              (C["s02.b"], [("prever", "i", 74), ("a", "i", 74), ("cor", "g", 70), ("do", "i", 74), ("indicador", "g", 70, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 80, TINTA2), XE, 200)
    E.frase(c, t, C["s03.a"], [("ácido", "g", 80, ACIDO)] + ps("solta", "i", 80), XE, 400, passo=0.14)
    ion_em(c, t, C["s03.a"] + 0.6, XE + 560, 375, 50, "H", "+")
    E.frase(c, t, C["s03.b"], [("base", "g", 80, BASE)] + ps("solta", "i", 80), XE, 560, passo=0.14)
    ion_em(c, t, C["s03.b"] + 0.6, XE + 560, 535, 56, "OH", "-", cor="#B3343A")
    E.frase(c, t, C["s03.c"], ps("água pura:", "i", 66, TINTA2) + [("os dois íons", "g", 62)] + ps("na mesma quantidade, bem pouco", "i", 66, TINTA2), XE, 800, passo=0.1)
    ion_em(c, t, C["s03.c"] + 1.0, 1450, 520, 40, "H", "+")
    ion_em(c, t, C["s03.c"] + 1.2, 1600, 520, 46, "OH", "-", cor="#B3343A")


# ---------------- escala ----------------
def b_escala(c, t, C, b):
    E.frase(c, t, C["s04"], ps("quão ácida ou básica?", "i", 70, TINTA2), XE, 170, passo=0.12)
    Q.escala_ph(c, t, C["s04.a"], ESX, ESY, ESW, 70, size=40, rotulos=False)
    E.foco(c, t, C["s04.a"] + 0.2, 0.4, lambda a: E.escreve(c, "pH", ESX - 140, ESY + 50, 70, "g", COR, a))
    if t < C["s06"]:
        E.frase(c, t, C["s04.b"], ps("de", "i", 66) + [("0", "g", 62, COR)] + ps("a", "i", 66) + [("14", "g", 62, COR)], XE, 300, passo=0.12)
        marca(c, t, C["s05.a"], 7, "7: neutro (água pura)", NEUTRO)
        lado(c, t, C["s05.b"], ESX, ph_x(6.9), ESY + 110, "ácido", ACIDO)
        lado(c, t, C["s05.c"], ph_x(7.1), ESX + ESW, ESY + 110, "básico", BASE)
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("mais", "i", 66) + [("H⁺", "g", 62, ACIDO)] + ps(": menor o pH", "i", 66), XE, 760, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("mais", "i", 66) + [("OH⁻", "g", 62, BASE)] + ps(": maior o pH", "i", 66), 1000, 760, passo=0.12)
        E.frase(c, t, C["s06.c"], ps("cada número a menos:", "i", 62, TINTA2) + [("10 vezes", "g", 58, COR)] + ps("mais ácida", "i", 62, TINTA2), XE, 900, passo=0.1)
        p = ease_io(prog(t, C["s06.a"], 1.2)) - ease_io(prog(t, C["s06.b"], 1.6)) * 0
        if t >= C["s06.a"]:
            x0 = ph_x(7)
            x1 = lerp(x0, ph_x(1), ease_io(prog(t, C["s06.a"], 1.0))) if t < C["s06.b"] else lerp(ph_x(1), ph_x(13), ease_io(prog(t, C["s06.b"], 1.4)))
            M.arrow(c, x1, ESY - 180, x1, ESY - 50, TINTA, 1, 5, 18)
        return
    if t < C["s08"]:
        for k, ph, rot, cor in (("s07.a", 2, "limão ≈ 2", ACIDO), ("s07.b", 7, "água pura 7", NEUTRO), ("s07.c", 13.6, "soda ≈ 14", BASE)):
            marca(c, t, C[k], ph, rot, cor)
        for k, ph, nome in (("s07.a", 2, "ácido"), ("s07.b", 7, "neutra"), ("s07.c", 13.6, "muito básica")):
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, ph=ph, nome=nome: centro(c, nome, ph_x(ph), ESY + 180, 52, "i", TINTA, a))
        return
    for i, (k, ph, rot) in enumerate((("s08.a", 3, "refrigerante ≈ 3"), ("s08.b", 5, "café ≈ 5"), ("s08.c", 7.4, "sangue ≈ 7,4"), ("s08.d", 12, "água sanitária ≈ 12"))):
        marca(c, t, C[k], ph, rot, TINTA, dy=90 * (i % 2))
    E.frase(c, t, C["s08.e"], ps("quase tudo o que você bebe é um pouco", "i", 64) + [("ácido", "g", 60, ACIDO)], W / 2, 860, "center", 0.1)


# ---------------- fenolftaleína ----------------
def b_fenol(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("ninguém vê o pH a olho nu", "i", 76, TINTA2), XE, 220, passo=0.12)
        E.frase(c, t, C["s09.a"], [("indicador", "g", 110, COR)], XE, 400)
        E.frase(c, t, C["s09.b"], ps("muda de cor conforme o pH", "i", 70), XE, 520, passo=0.12)
        Q.bequer(c, t, C["s09.a"], 1450, 900, 320, 360, 0.7, lambda tt: Q.muda_cor(tt, C["s09.c"] + 0.8, Q.AGUA, FENOL_ROSA, 1.2))
        Q.conta_gotas(c, 1450, 520, ep(t, C["s09.c"], 0.4), FENOL_ROSA)
        Q.gotas(c, t, C["s09.c"] + 0.2, 1450, 530, 700, 3, "#F3D3E6")
        return
    E.frase(c, t, C["s10.a"], [("fenolftaleína", "g", 90, COR)], XE, 210)
    xs = (420, 960, 1500)
    for i, (k, ph, rot, cor, nome) in enumerate((("s10.b", 2, "ácido", ACIDO, "incolor"), ("s10.c", 7, "neutro", NEUTRO, "incolor"), ("s10.d", 11, "básico", BASE, "rosa"))):
        Q.bequer(c, t, C[k], xs[i], 760, 280, 320, 0.7, lambda tt, ph=ph, k=k: Q.muda_cor(tt, C[k] + 0.5, Q.AGUA, cor_fenol(ph), 0.8))
        pilula_em(c, t, C[k] + 0.2, rot, xs[i], 360, 50, cor)
        E.foco(c, t, C[k] + 0.8, 0.4, lambda a, i=i, nome=nome: centro(c, nome, xs[i], 860, 60, "g", FENOL_ROSA if nome == "rosa" else TINTA2, a))
    E.foco(c, t, C["s10.d"] + 1.4, 0.4, lambda a: centro(c, "rosa só com pH acima de 8, mais ou menos", W / 2, 990, 52, "i", TINTA2, a))


# ---------------- repolho ----------------
def b_repolho(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("repolho roxo", "g", 90, "#7A3FA0")] + ps("indicador caseiro", "i", 76, TINTA2), XE, 210, passo=0.14)
        xs = (330, 750, 1170, 1590)
        for i, (k, ph, nome) in enumerate((("s11.b", 2.5, "ácido: vermelho"), ("s11.c", 7, "neutro: roxo"), ("s11.d", 10, "básico: verde"), ("s11.e", 13.5, "muito básico: amarelo"))):
            Q.bequer(c, t, C[k], xs[i], 760, 260, 320, 0.7, lambda tt, ph=ph, k=k: Q.muda_cor(tt, C[k] + 0.4, cor_repolho(7), cor_repolho(ph), 0.8))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, i=i, nome=nome, ph=ph: centro(c, nome, xs[i], 860, 46, "b", cor_repolho(ph) if ph != 13.5 else "#9A7B0A", a))
        Q.escala_ph(c, t, C["s11.e"] + 0.8, 360, 950, 1200, 40, rotulos=False)
        return
    E.frase(c, t, C["s12.a"], ps("um pigmento que", "i", 70) + [("muda de forma", "g", 66, COR)] + ps("com o pH", "i", 70), XE, 260, passo=0.12)
    def faixa(a, f, y, rot):
        for k in range(29):
            ph = k / 2
            M.rrect(c, 260 + k * 48, y, 46, 80, 8, f(ph), a)
        E.escreve(c, rot, 260, y - 24, 52, "g", TINTA, a)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: faixa(a, cor_repolho, 470, "repolho: várias cores"))
    E.foco(c, t, C["s12.b"] + 0.6, 0.5, lambda a: faixa(a, cor_fenol, 720, "fenolftaleína: só duas"))
    Q.escala_ph(c, t, C["s12.b"], 260, 880, 1392, 40, rotulos=True, size=34)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("fenolftaleína", "i", 74) + [("vermelha", "g", 70, ERRADO)] + ps("no ácido?", "i", 74), XE + 450, 190, passo=0.12)
    Q.bequer(c, t, C["s13.b"], 520, 760, 300, 340, 0.7, Q.AGUA)
    E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: centro(c, "incolor", 520, 860, 64, "g", TINTA, a))
    E.frase(c, t, C["s13.c"], [("incolor", "g", 66)] + ps("não quer dizer ácido:", "i", 70), 1000, 420, passo=0.12)
    for i, (rot, cor) in enumerate((("ácido", ACIDO), ("neutro", NEUTRO), ("um pouco básico (sangue)", BASE))):
        pilula_em(c, t, C["s13.d"] + 0.4 * i, rot, 1000 + E.larg(rot, "g", 48) / 2 + 30, 560 + i * 110, 48, cor)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        palco_titulo(c, t, C["s14"], "o atalho de prova")
        E.foco(c, t, C["s14.a"], 0.4, lambda a: E.pilula(c, "rosa", 520, 360, 70, "g", fundo=FENOL_ROSA, a=a))
        E.frase(c, t, C["s14.a"] + 0.3, [("=", "g", 70, CLARO), ("base,", "g", 70, BR)] + ps("sempre", "i", 74, CLARO), 720, 385, passo=0.12)
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.pilula(c, "incolor", 520, 560, 70, "g", fundo="#3A3B42", a=a))
        E.frase(c, t, C["s14.b"] + 0.3, [("=", "g", 70, CLARO), ("pH abaixo de 8", "g", 70, BR)], 760, 585, passo=0.12)
        E.frase(c, t, C["s14.c"], ps("ácido ou neutro? use", "i", 66, CLARO) + [("outro indicador", "g", 62, BR)], W / 2, 800, "center", 0.12)
        return
    palco_titulo(c, t, C["s15"], "cuidado com a escala")
    Q.escala_ph(c, t, C["s15"] + 0.3, 260, 500, 1400, 70, escuro=True, size=40)
    E.frase(c, t, C["s15.a"], ps("o número", "i", 70, CLARO) + [("menor", "g", 66, BR)] + ps("é o mais ácido", "i", 70, CLARO), W / 2, 760, "center", 0.12)
    E.frase(c, t, C["s15.b"], [("pH 2", "g", 70, BR), (">", "g", 70, CLARO), ("pH 5", "g", 70, BR)] + ps("em acidez", "i", 70, CLARO), W / 2, 900, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        for i, (k, ph, nome) in enumerate((("s16.a", 3, "vinagre"), ("s16.b", 7, "água + açúcar"), ("s16.c", 10, "leite de magnésia"))):
            Q.bequer(c, t, C[k], 1170 + i * 260, 760, 200, 260, 0.7, Q.AGUA if i < 2 else "#F4F4F2")
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, i=i, nome=nome, ph=ph: (centro(c, f"pH {ph}", 1170 + i * 260, 830, 50, "g", TINTA, a),
                                                                           centro(c, nome, 1170 + i * 260, 890, 38, "i", TINTA2, a)))
    questao(c, t, C, "s16", [(C["s16.a"], ps("três copos", "i", 64, TINTA2), 300),
                             (C["s16.d"], [("1", "g", 56, COR)] + ps("ácido, neutro ou básico?", "i", 60), 480),
                             (C["s16.e"], [("2", "g", 56, COR)] + ps("cor da fenolftaleína", "i", 60), 600),
                             (C["s16.e"] + 0.8, [("3", "g", 56, COR)] + ps("cor do repolho roxo", "i", 60), 720)], "s17", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs = (420, 960, 1500)
    for i, (k, kk, ph, nome, rot, cor) in enumerate((("s18.a", "s18.b", 3, "vinagre", "ácido", ACIDO), ("s18.c", "s18.d", 7, "água + açúcar", "neutro", NEUTRO),
                                                    ("s19.a", "s19.b", 10, "leite de magnésia", "básico", BASE))):
        E.foco(c, t, C[k], 0.4, lambda a, i=i, nome=nome, ph=ph: (centro(c, nome, xs[i], 220, 56, "g", TINTA, a), centro(c, f"pH {ph}", xs[i], 290, 50, "b", TINTA2, a)))
        pilula_em(c, t, C[k] + 0.4, rot, xs[i], 370, 50, cor)
        Q.bequer(c, t, C[kk], xs[i] - 120, 720, 180, 230, 0.7, lambda tt, ph=ph, kk=kk: Q.muda_cor(tt, C[kk] + 0.3, Q.AGUA, cor_fenol(ph), 0.6))
        Q.bequer(c, t, C[kk] + 0.3, xs[i] + 120, 720, 180, 230, 0.7, lambda tt, ph=ph, kk=kk: Q.muda_cor(tt, C[kk] + 0.8, cor_repolho(7), cor_repolho(ph), 0.6))
        E.foco(c, t, C[kk] + 0.4, 0.4, lambda a, i=i: (centro(c, "fenolft.", xs[i] - 120, 790, 36, "i", TINTA2, a), centro(c, "repolho", xs[i] + 120, 790, 36, "i", TINTA2, a)))
    E.frase(c, t, C["s19.c"], ps("a fenolftaleína deixou", "i", 60) + [("dois copos iguais", "g", 56)], W / 2, 920, "center", 0.1)
    E.frase(c, t, C["s19.d"], ps("o repolho", "i", 60) + [("separou os três", "g", 56, COR)], W / 2, 1010, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        Q.equacao(c, t, C["s21.b"], "HCl + H2O -> H3O^+ + Cl^-", 760, 800, 96, passo=0.3)
        E.frase(c, t, C["s21.c"], ps("e pares de elétrons", "i", 64, TINTA2), XE, 940, passo=0.1)
    fim(c, t, C, "s20", [("s20.a", [("<", "g", 66, ACIDO), ("7", "g", 66), ("ácido,", "i", 72), ("7", "g", 66), ("neutro,", "i", 72), (">", "g", 66, BASE), ("7", "g", 66), ("básico", "i", 72)]),
                         ("s20.b", [("fenolftaleína", "g", 66), ("rosa", "g", 66, FENOL_ROSA), ("só", "i", 72), ("na", "i", 72), ("base", "g", 66, BASE)]),
                         ("s20.c", [("repolho:", "g", 66), ("do", "i", 72), ("vermelho", "g", 66, cor_repolho(2)), ("ao", "i", 72), ("verde", "g", 66, cor_repolho(10.5))])],
        "s21", "Brønsted-Lowry", "e Lewis", "s21.d", "s21.e", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, escala=b_escala, fenol=b_fenol, repolho=b_repolho, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
