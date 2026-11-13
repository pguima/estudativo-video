"""Visual — Estudativo · QUI-EQL-008: praticando equilíbrio, pH e Kps (prática, 5 questões).

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha Equilíbrio (QUI-EQL-001) e do módulo pH (QUI-EQL-003). Cada questão
tem o cabeçalho "questão n de 5"; enunciado no alto, resolução embaixo, resultado na esfera (turquesa; pOH em azul). Peças das
aulas anteriores copiadas aqui: kfrac e quadro (EQL-009), desloca (EQL-002), escala de pH (EQL-003).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Equilíbrio Químico")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-EQL-008_praticando_equilibrio_ph_kps.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR = Q.ELETRON, "#E8A317"

assert Q.lados("CO + 2 H2 -> CH3OH")[0] == Q.lados("CO + 2 H2 -> CH3OH")[1] and 1 + 2 == 3
assert abs(0.5 * 0.5 / 0.5 - 0.5) < 1e-12
assert abs(-math.log10(2e-3) - 2.7) < 0.01 and abs(14 - 2.7 - 11.3) < 1e-9
assert abs(-math.log10(2e-5) - 4.7) < 0.01
assert abs(math.sqrt(1e-10) - 1e-5) < 1e-18 and 1e-4 * 1e-4 > 1e-10


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da QUI-EQL-001 e da QUI-TER-004) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def _fq(c, s, x, y, size, cor, a=1.0, align="left", cores=None, escuro=False):
    """palavra comum sai em E.formula; espécie química, em Q.formula"""
    if not any(ch.isupper() for ch in s):   # palavra ou número: E.formula (aceita ^ e fração)
        return E.formula(c, s, x, y, size, "g", cor, a, align)
    return Q.formula(c, s, x, y, size, cor, a, align, cores=cores, escuro=escuro)


def kfrac(c, t, t0, sub, num, den, x, y, size, tn=None, td=None, escuro=False, cor_exp=None):
    """K_sub = num / den (den=None: sem fração). x = borda esquerda, y = linha da barra"""
    tinta = BR if escuro else TINTA
    ce = cor_exp or (E.CLARO if escuro else E.COR)
    E.foco(c, t, t0, 0.4, lambda a: (E.escreve(c, "K", x, y + size * 0.36, size, "g", tinta, a),
                                     E.escreve(c, sub, x + E.larg("K", "g", size) + 4, y + size * 0.56, size * 0.55, "g", tinta, a),
                                     E.escreve(c, "=", x + E.larg("K", "g", size) + E.larg(sub, "g", size * 0.55) + size * 0.3, y + size * 0.36, size, "g", tinta, a)))
    x0 = x + E.larg("K", "g", size) + E.larg(sub, "g", size * 0.55) + size * 0.3 + E.larg("=", "g", size) + size * 0.35
    s_ = size * 0.85
    wn = _fq(None, num, 0, 0, s_, None, 0)
    if den is None:
        E.foco(c, t, tn if tn is not None else t0 + 0.3, 0.4, lambda a: _fq(c, num, x0, y + s_ * 0.36, s_, tinta, a, cores={"carga": ce}, escuro=escuro))
        return x0 + wn
    wd = _fq(None, den, 0, 0, s_, None, 0)
    w = max(wn, wd) + size * 0.3
    q = ep(t, tn if tn is not None else t0 + 0.3, 0.4)
    if q > 0:
        M.line(c, x0, y, x0 + w * ease_out(q), y, tinta, q, max(5, size * 0.07))
    E.foco(c, t, tn if tn is not None else t0 + 0.3, 0.4, lambda a: _fq(c, num, x0 + w / 2, y - size * 0.28, s_, tinta, a, "center", cores={"carga": ce}, escuro=escuro))
    E.foco(c, t, td if td is not None else t0 + 0.6, 0.4, lambda a: _fq(c, den, x0 + w / 2, y + size * 0.95, s_, tinta, a, "center", cores={"carga": ce}, escuro=escuro))
    return x0 + w


def proxima(c, t, C, s, partes, sub, k_ins, k_bons, extra=None):
    """tela da próxima aula: partes = título (E.frase), sub = frase cinza; k_ins/k_bons = cues do inscreva-se e do bons estudos"""
    E.frase(c, t, C[s], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[s + ".a"], partes, XE, 420)
    if sub:
        E.frase(c, t, sub[0], ps(sub[1], "i", 62, TINTA2), XE, 560, passo=0.1)
    if extra:
        extra()
    E.foco(c, t, C[k_ins], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_ins] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1020, 845, p), ep(t, C[k_ins] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 920)


def abertura(c, t, C, titulo, itens, t_tit=None):
    """a promessa da aula com o hexágono"""
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1640, 640, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, t_tit if t_tit is not None else C["s02"], titulo, XE, 300, passo=0.14)
    lista(c, t, itens, XE, 500, 170)


def relogio(c, t, t0, cx, cy, r):
    E.relogio(c, t, t0, cx=cx, cy=cy, r=r)


def quadro(c, t, t0, especies, linhas, x, y, wcol=300, dy=120, size=60, tl=None, destaque=None, wrot=260):
    """quadro início / reage / equilíbrio: especies = fórmulas (cabeçalho); linhas = 3 listas de textos; tl = instante de cada célula
    (lista de listas) ou de cada linha. Devolve (xs das colunas, ys das linhas)"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return [], []
    xs = [x + wrot + wcol * k + wcol / 2 for k in range(len(especies))]
    for k, s in enumerate(especies):
        Q.formula(c, s, xs[k], y, size * 0.9, TINTA, q, "center")
    M.line(c, x, y + size * 0.45, x + wrot + wcol * len(especies), y + size * 0.45, TINTA2, 0.6 * q, 3)
    ys = []
    for i, rot in enumerate(("início", "reage", "equilíbrio")):
        yy = y + size * 0.45 + (i + 1) * dy - dy * 0.3
        ys.append(yy)
        if destaque == i:
            M.rrect(c, x - 10, yy - size * 0.95, wrot + wcol * len(especies) + 20, size * 1.3, 14, E.mix(E.COR, "#FFFFFF", 0.78), q)
        E.foco(c, t, t0 + 0.1 * i, 0.4, lambda a, rot=rot, yy=yy, i=i: E.escreve(c, rot, x, yy, size * 0.8, "b" if i < 2 else "g", TINTA2 if i < 2 else COR, a))
        for k, s in enumerate(linhas[i]):
            if s is None:
                continue
            ti = (tl[i][k] if isinstance(tl[i], (list, tuple)) else tl[i]) if tl else t0 + 0.3 + 0.2 * i
            cor = (ERRADO if s.startswith("−") else E.COR_TEXTO) if i == 1 else (COR if i == 2 else TINTA)
            E.foco(c, t, ti, 0.4, lambda a, s=s, k=k, yy=yy, cor=cor: E.formula(c, s, xs[k], yy, size, "g", cor, a, "center"))
    return xs, ys


def cab_q(c, t, t0, n):
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, XE + 40, 130, 44, a=a), centro(c, str(n), XE + 40, 152, 54, "g", E.SOBRE, a),
                                     E.escreve(c, f"questão {n} de 5", XE + 110, 152, 52, "b", TINTA2, a)))


def desloca(c, t, t0, cx, y, sentido, rot=None, w=420):
    if t < t0:
        return
    if sentido == 0:
        E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "não desloca", cx, y, 50, "g", fundo=TINTA2, a=a))
        return
    p = ease_out(prog(t, t0, 0.6))
    cor = E.COR if sentido > 0 else CINZA
    x0, x1 = cx - sentido * w / 2, cx + sentido * w / 2
    F.seta(c, x0, y, lerp(x0, x1, p), y, cor, 1, 20, 46)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot, cx, y + 80, 46, "g", COR if sentido > 0 else TINTA2, a))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("cinco", "g", 130, COR), ("questões", "g", 130)], XE, 330, passo=0.14)
    for k, s in enumerate(("deslocamento", "Kc", "pH", "tampão", "Kps")):
        E.foco(c, t, C["s01.b"] + 0.3 * k, 0.4, lambda a, k=k, s=s: (E.bola(c, 260 + k * 340, 600, 60, a=a),
                                                                       centro(c, str(k + 1), 260 + k * 340, 626, 72, "g", E.SOBRE, a),
                                                                       centro(c, s, 260 + k * 340, 740, 50, "b", TINTA, a)))
    E.frase(c, t, C["s01.c"], ps("pause, tente, e só depois veja a resolução", "i", 60), W / 2, 960, "center", 0.1)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02.a"], ps("a caixa de ferramentas", "i", 76, TINTA2), XE, 170, passo=0.12)
    linhas = ((C["s02.b"], "o equilíbrio foge da perturbação"), (C["s02.c"], "no Kc, só a linha do equilíbrio"), (C["s02.d"], "pH + pOH = 14"),
              (C["s02.e"], "o forte vence;  tampão: pH = pKa"), (C["s02.f"], "Kps = produto dos íons"))
    for k, (tt, s) in enumerate(linhas):
        y = 320 + k * 145
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 40, y - 22, 40, a=a), centro(c, str(k + 1), XE + 40, y - 2, 48, "g", E.SOBRE, a)))
        E.foco(c, t, tt + 0.1, 0.5, lambda a, y=y, s=s: E.formula(c, s, XE + 100, y, 60, "g", TINTA, a))


# ---------------- questão 1: deslocamento ----------------
EQ1 = "CO(g) + 2 H2(g) <=> CH3OH(g)"


def b_q1(c, t, C, b):
    cab_q(c, t, C["s03.a"], 1)
    Q.formula_em(c, t, C["s03.b"], EQ1, XE, 330, 90)
    E.foco(c, t, C["s03.b"] + 0.8, 0.4, lambda a: (E.formula(c, "ΔH < 0", XE + 1250, 330, 70, "g", AZUL, a), E.escreve(c, "o metanol", XE, 420, 50, "i", TINTA2, a)))
    for k, (tt, s) in enumerate(((C["s03.c"], "pressão ↑"), (C["s03.d"], "esquentar"), (C["s03.e"], "catalisador"))):
        pilula_em(c, t, tt, s, 420 + k * 480, 600, 60, AMBAR if k < 2 else TINTA)
    relogio(c, t, C["s04.a"], W / 2, 860, 90)


def b_r1(c, t, C, b):
    cab_q(c, t, C["s05"] - 0.6, 1)
    Q.formula(c, EQ1, XE, 330, 90, cores={"coef": E.COR} if t < C["s05.c"] else None)
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.formula(c, "pressão ↑: 3 gases → 1", XE, 520, 64, "g", TINTA, a))
    desloca(c, t, C["s05.b"], 1420, 500, +1, "mais metanol")
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.formula(c, "esquentar: favorece a volta (absorve calor)", XE, 720, 60, "g", TINTA, a))
    desloca(c, t, C["s05.d"], 1500, 800, -1, None, 300)
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.formula(c, "catalisador: não desloca, só chega antes", XE, 950, 60, "g", TINTA2, a))


# ---------------- questão 2: Kc pelo quadro ----------------
EQ2 = "PCl5(g) <=> PCl3(g) + Cl2(g)"


def b_q2(c, t, C, b):
    cab_q(c, t, C["s06.a"], 2)
    Q.formula_em(c, t, C["s06.b"], EQ2, XE, 330, 90)
    E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: E.formula(c, "1 L, início: 1 mol de PCl₅", XE, 470, 66, "g", TINTA, a))
    E.foco(c, t, C["s06.c"], 0.4, lambda a: E.formula(c, "no equilíbrio: 0,5 mol de Cl₂", XE, 590, 66, "g", TINTA, a))
    E.frase(c, t, C["s06.d"], ps("calcule o", "i", 66) + [("Kc", "g", 62, COR), ("e", "i", 66), ("o grau", "g", 62, COR)], XE, 760, passo=0.1)
    relogio(c, t, C["s07.a"], 1500, 700, 110)


def b_r2(c, t, C, b):
    cab_q(c, t, C["s08"] - 0.6, 2)
    E.foco(c, t, C["s08.a"], 0.4, lambda a: E.escreve(c, "1 L: mol = mol/L", XE + 800, 152, 52, "b", COR, a))
    L = [["1", "0", "0"], [None, None, None], [None, None, None]]
    if t >= C["s08.b"]:
        L[1][2] = "+0,5"
    if t >= C["s08.c"]:
        L[1][1] = "+0,5"
    if t >= C["s08.d"]:
        L[1][0] = "−0,5"
    if t >= C["s08.e"]:
        L[2] = ["0,5", "0,5", "0,5"]
    quadro(c, t, C["s08"] - 0.6, ("PCl5", "PCl3", "Cl2"), L, XE, 300, 250, 120, 60,
           tl=[[C["s08"] - 0.6] * 3, [C["s08.d"], C["s08.c"], C["s08.b"]], [C["s08.e"]] * 3])
    if t >= C["s09"]:
        kfrac(c, t, C["s09.a"], "c", "0,5 · 0,5", "0,5", 1200, 420, 80)
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.formula(c, "=", 1710, 448, 80, "g", TINTA, a))
        bola_txt(c, t, C["s09.c"], "0,5", 1830, 420, 66, 54)
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.formula(c, "α = f{0,5}{1} =", XE, 860, 80, "g", TINTA, a))
        bola_txt(c, t, C["s09.e"], "50%", 720, 835, 80, 54)


# ---------------- questão 3: pH de base ----------------
def b_q3(c, t, C, b):
    cab_q(c, t, C["s10.a"], 3)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (Q.formula(c, "KOH", XE, 360, 100, TINTA, a), E.formula(c, "2 · 10^{−3} mol/L", XE + 330, 360, 90, "g", TINTA, a)))
    E.foco(c, t, C["s10.b"] + 0.6, 0.4, lambda a: E.escreve(c, "base forte", XE, 450, 50, "b", TINTA2, a))
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.formula(c, "log 2 = 0,3", XE, 580, 76, "g", TINTA2, a))
    E.frase(c, t, C["s10.d"], ps("qual é o", "i", 70) + [("pH?", "g", 66, COR)], XE, 760, passo=0.1)
    relogio(c, t, C["s11.a"], 1500, 640, 120)


def b_r3(c, t, C, b):
    cab_q(c, t, C["s12"] - 0.6, 3)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "[OH⁻] = 2 · 10^{−3}", XE, 320, 86, "g", TINTA, a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "dá o pOH, não o pH", XE + 900, 315, 56, "g", AZUL, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "pOH = 3 − 0,3 =", XE, 500, 86, "g", TINTA, a))
    bola_txt(c, t, C["s12.c"] + 0.5, "2,7", 900, 470, 80, 60, AZUL)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "pH = 14 − 2,7 =", XE, 700, 86, "g", TINTA, a))
    bola_txt(c, t, C["s12.e"], "11,3", 900, 670, 90, 56)
    if t >= C["s12.f"]:
        Q.escala_ph(c, t, C["s12.f"], XE, 860, 1500, 60, marca=11.3, tm=C["s12.f"] + 0.2)


# ---------------- questão 4: hidrólise e tampão ----------------
def b_q4(c, t, C, b):
    cab_q(c, t, C["s13.a"], 4)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (Q.formula(c, "CH3COONa", XE, 340, 90, TINTA, a), E.escreve(c, "ácida, neutra ou básica?", XE + 620, 330, 56, "b", TINTA2, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: Q.formula(c, "CH3COOH + CH3COONa", XE, 540, 86, TINTA, a))
    E.foco(c, t, C["s13.c"] + 0.8, 0.4, lambda a: E.escreve(c, "mesma concentração", XE, 620, 50, "b", TINTA2, a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "Ka = 2 · 10^{−5}:  pH?   (log 2 = 0,3)", XE, 760, 76, "g", TINTA, a))
    relogio(c, t, C["s14.a"], 1600, 600, 100)


def b_r4(c, t, C, b):
    cab_q(c, t, C["s15"] - 0.6, 4)
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (E.formula(c, "NaOH forte  +  CH₃COOH fraco", XE, 320, 70, "g", TINTA, a)))
    pilula_em(c, t, C["s15.b"], "o forte vence: básica", 1500, 300, 50, AZUL)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: E.escreve(c, "ácido fraco + o seu sal, iguais: tampão", XE, 520, 62, "g", TINTA, a))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "pH = pKa", XE, 700, 96, "g", TINTA, a))
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.formula(c, "= 5 − 0,3 =", XE + 500, 700, 96, "g", TINTA2, a))
    bola_txt(c, t, C["s15.f"], "4,7", 1250, 670, 90, 66)


# ---------------- questão 5: Kps ----------------
def b_q5(c, t, C, b):
    cab_q(c, t, C["s16.a"], 5)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (Q.formula(c, "AgCl", XE, 340, 100, TINTA, a), E.formula(c, "Kps = 1 · 10^{−10}", XE + 360, 340, 86, "g", TINTA, a)))
    E.foco(c, t, C["s16.b"] + 0.6, 0.4, lambda a: E.escreve(c, "cloreto de prata", XE, 430, 50, "b", TINTA2, a))
    E.frase(c, t, C["s16.c"], [("1", "g", 60, COR), ("solubilidade?", "g", 62)], XE, 600, passo=0.1)
    E.frase(c, t, C["s16.d"], [("2", "g", 60, COR)] + ps("mistura: Ag⁺ e Cl⁻ a 10⁻⁴. precipita?", "b", 54), XE, 720, passo=0.08)
    relogio(c, t, C["s17.a"], 1550, 620, 110)


def b_r5(c, t, C, b):
    cab_q(c, t, C["s18"] - 0.6, 5)
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.formula(c, "um íon de cada: Kps = s^2", XE, 320, 76, "g", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "s = r{10^{−10}} =", XE, 500, 86, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "10^{−5} mol/L", XE + 640, 500, 86, "g", COR, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "produto = 10^{−4} · 10^{−4} = 10^{−8}", XE, 700, 80, "g", TINTA, a))
    E.foco(c, t, C["s18.e"], 0.5, lambda a: E.formula(c, "10^{−8}  >  10^{−10}", XE, 880, 90, "g", COR, a))
    pilula_em(c, t, C["s18.f"], "forma precipitado", 1400, 855, 56, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s20"]:
        E.frase(c, t, C["s19.a"], ps("acertou três das cinco?", "i", 80), W / 2, 400, "center", 0.12)
        E.frase(c, t, C["s19.a"] + 1.4, [("o equilíbrio está no lugar", "g", 80, COR)], W / 2, 540, "center")
        E.frase(c, t, C["s19.b"], ps("errou alguma? volte na aula daquela ferramenta", "i", 60, TINTA2), W / 2, 740, "center", 0.1)
        return
    E.frase(c, t, C["s20.a"], [("fim", "g", 120, COR), ("da", "i", 120), ("trilha", "g", 120)], XE, 380)
    E.frase(c, t, C["s20.a"] + 0.8, ps("equilíbrio químico e pH", "i", 70, TINTA2), XE, 500, passo=0.1)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1020, 845, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 920)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
