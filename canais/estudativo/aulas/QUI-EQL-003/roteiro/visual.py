"""Visual — Estudativo · QUI-EQL-003: produto iônico da água, pH e pOH. Primeira aula do módulo pH, hidrólise, tampão e Kps.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha Equilíbrio Químico (QUI-EQL-001).
LINGUAGEM VISUAL DO MÓDULO pH (QUI-EQL-003 a 008 copiam daqui):
- ÍONS: H⁺ numa bolinha turquesa (íon_h) e OH⁻ numa bolinha azul Q.ELETRON (íon_oh), com a fórmula dentro; a proporção entre
  elas mostra se a solução é ácida (mais turquesa), neutra (iguais) ou básica (mais azul).
- ESCALA DE pH: Q.escala_ph (cores do indicador universal) com a seta na marca; ácido à esquerda, básico à direita, 7 no meio.
- POTÊNCIA DE 10 com E.formula ("10^{−3}"); o expoente que vira pH fica na cor da matéria. log com E.formula ("log 2 ≈ 0,3").
- pH na esfera turquesa; pOH na esfera azul.
Peças candidatas ao kit: ion (bolinha de íon com a fórmula), pot10 (potência de 10 com o expoente destacado).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-003_produto_ionico_ph_poh.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("agua", "ph", "exemplo", "erro", "log", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL = Q.ELETRON

# as contas da aula
assert -math.log10(1e-3) == 3 and 14 - 2 == 12 and 10 ** (7 - 2) == 100000
assert abs(-math.log10(2e-3) - 2.7) < 0.01 and abs(-math.log10(2e-4) - 3.7) < 0.01 and abs(14 - 3.7 - 10.3) < 1e-9
assert abs(55.5 / 1e-7 - 5.55e8) < 1e6     # ~ 1 em 550 milhões


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


def ion(c, cx, cy, r, s, cor, a=1.0, escuro=False):
    """íon numa bolinha com a fórmula dentro"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, cor, a)
    Q.formula(c, s, cx, cy + r * 0.32, r * 0.85, BR, a, "center")


def ions_campo(c, t, t0, x, y, w, h, nh, noh, a=1.0, semente=1):
    """vários íons H⁺ e OH⁻ espalhados, mexendo"""
    import random
    rnd = random.Random(semente)
    q = ep(t, t0, 0.5) * a
    for k in range(nh + noh):
        px, py = x + rnd.uniform(40, w - 40), y + rnd.uniform(40, h - 40)
        px += 10 * math.sin(t * 1.3 + k)
        py += 10 * math.cos(t * 1.1 + k * 0.7)
        ion(c, px, py, 30, "H^+" if k < nh else "OH^-", E.COR if k < nh else AZUL, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.escala_ph(c, t, C["s01.a"], 260, 430, 1400, 80, marca=2 if t < C["s01.b"] else 7, tm=C["s01.a"] + 0.4)
        E.foco(c, t, C["s01.a"], 0.4, lambda a: E.escreve(c, "suco de limão: pH ≈ 2", XE, 300, 70, "g", TINTA, a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.escreve(c, "água pura: pH 7", XE + 1000, 300, 70, "g", TINTA, a))
        E.frase(c, t, C["s01.c"], ps("parece pouca diferença,", "i", 64, TINTA2), XE, 740, passo=0.1)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.formula(c, "10^5 = 100 000 vezes mais H⁺", XE, 900, 90, "g", COR, a))
        E.frase(c, t, C["s01.e"], ps("de onde sai esse número?", "i", 60), 1300, 1020, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("pH", "g", 120, COR), ("e", "i", 120), ("pOH", "g", 120, COR)],
             [(C["s02.a"], [("o", "i", 74), ("pH", "g", 70), ("de", "i", 74), ("um", "i", 74), ("ácido", "g", 70)]),
              (C["s02.b"], [("pH + pOH = 14", "g", 70, COR)]), (C["s02.c"], [("pH", "g", 70), ("com", "i", 74), ("log 2", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 200, passo=0.12)
    Q.escala_ph(c, t, C["s03.a"], XE, 290, 1300, 60, marca=7, tm=C["s03.a"] + 0.4)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (Q.formula(c, "HCl -> H^+ + Cl^-", XE, 560, 76, TINTA, a), E.escreve(c, "ácido forte: ioniza tudo", XE + 760, 555, 54, "b", TINTA2, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "log 10^{−3} = −3", XE, 740, 86, "g", TINTA, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "log 2 ≈ 0,3", XE + 900, 740, 86, "g", COR, a))


# ---------------- a água se ioniza ----------------
def b_agua(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("até a água pura se ioniza, só um pouquinho", "i", 64), XE, 200, passo=0.1)
        Q.formula_em(c, t, C["s04.b"], "H2O(l) <=> H^+(aq) + OH^-(aq)", W / 2, 360, 96, align="center")
        Q.molecula(c, t, C["s04.b"], "H2O", 400, 640, 120)
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: (ion(c, 1260, 600, 54, "H^+", E.COR, a), ion(c, 1460, 680, 54, "OH^-", AZUL, a)))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.formula(c, "[H⁺] = [OH⁻] = 10^{−7} mol/L", W / 2, 880, 80, "g", TINTA, a, "center"))
        pilula_em(c, t, C["s04.d"], "cerca de 1 em 550 milhões de moléculas", W / 2, 1000, 46, TINTA2)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("é um equilíbrio: tem constante", "i", 66), XE, 200, passo=0.1)
        Q.formula(c, "H2O(l) <=> H^+(aq) + OH^-(aq)", W / 2, 340, 84, align="center")
        if t >= C["s05.b"]:
            sp = Q.centros("H2O(l) <=> H^+(aq) + OH^-(aq)", W / 2, 340, 84, "center")
            wk = Q.formula(None, "H2O(l)", 0, 0, 84)
            E.risco(c, sp[0] - wk / 2, 360, sp[0] + wk / 2, 270, t, C["s05.b"], cor=CINZA, largura=8)
        E.frase(c, t, C["s05.c"], [("produto iônico da água", "g", 70, COR)], XE, 520)
        kfrac(c, t, C["s05.d"], "w", "[H^+] · [OH^-]", None, XE, 680, 110)
        E.foco(c, t, C["s05.e"], 0.5, lambda a: E.formula(c, "= 10^{−14}  (25 °C)", 1100, 720, 90, "g", COR, a))
        return
    E.frase(c, t, C["s06.a"], ps("a 25 °C, vale para qualquer solução em água", "i", 62), XE, 200, passo=0.1)
    k = ep(t, C["s06.b"], 1.5)
    nh, noh = int(round(4 + 6 * k)), int(round(4 - 3 * k))
    ions_campo(c, t, C["s06"], 260, 280, 1400, 480, nh, noh, semente=3)
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "H⁺ sobe, OH⁻ desce", XE, 860, 64, "g", TINTA, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "[H⁺] · [OH⁻] = 10^{−14}", 1000, 860, 76, "g", COR, a))


# ---------------- pH e pOH ----------------
def b_ph(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("para não escrever potências, o", "i", 66) + [("pH", "g", 62, COR)], XE, 200, passo=0.1)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: Q.formula(c, "pH = −log [H^+]", W / 2, 420, 140, TINTA, a, "center"))
        E.foco(c, t, C["s07.d"], 0.5, lambda a: E.formula(c, "[H⁺] = 10^{−3}  →  pH = 3", W / 2, 700, 100, "g", COR, a, "center"))
        pilula_em(c, t, C["s07.e"], "o menos do log cancela o menos do expoente", W / 2, 880, 50, TINTA)
        return
    E.foco(c, t, C["s08.a"], 0.5, lambda a: Q.formula(c, "pOH = −log [OH^-]", W / 2, 260, 110, TINTA, a, "center"))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "10^{−a} · 10^{−b} = 10^{−14}", W / 2, 480, 96, "g", TINTA, a, "center"))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "a + b = 14", W / 2, 640, 96, "g", TINTA2, a, "center"))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.formula(c, "pH + pOH = 14", W / 2, 860, 150, "g", COR, a, "center"))


# ---------------- exemplos ----------------
def b_exemplo(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("ácido clorídrico", "i", 66, TINTA2), XE, 200, passo=0.1)
        E.foco(c, t, C["s09"] + 0.6, 0.5, lambda a: Q.formula(c, "HCl: 0,001 mol/L", XE, 340, 90, TINTA, a))
        E.foco(c, t, C["s09.a"], 0.4, lambda a: Q.formula(c, "HCl -> H^+ + Cl^-", XE, 500, 80, TINTA2, a))
        pilula_em(c, t, C["s09.a"] + 0.5, "ácido forte: ioniza tudo", 1350, 475, 46, TINTA)
        E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "[H⁺] = 0,001", XE, 680, 90, "g", TINTA, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "= 10^{−3}", XE + 600, 680, 90, "g", COR, a))
        bola_txt(c, t, C["s09.e"], "pH 3", 1500, 820, 110, 60)
        return
    E.frase(c, t, C["s10.a"], ps("hidróxido de sódio, uma base forte", "i", 66, TINTA2), XE, 200, passo=0.1)
    E.foco(c, t, C["s10.a"] + 1.0, 0.5, lambda a: Q.formula(c, "NaOH: 0,01 mol/L", XE, 340, 90, TINTA, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "[OH⁻] = 10^{−2}", XE, 520, 90, "g", TINTA, a))
    bola_txt(c, t, C["s10.c"], "pOH 2", 1100, 490, 100, 54, AZUL)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "pH = 14 − 2 =", XE, 760, 90, "g", TINTA2, a))
    bola_txt(c, t, C["s10.e"], "12", 820, 730, 90, 70)
    Q.escala_ph(c, t, C["s10.e"] + 0.3, XE, 900, 1400, 60, marca=12, tm=C["s10.e"] + 0.5)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.b"], ps("fez a conta com o", "i", 64) + [("OH⁻", "g", 60, AZUL)] + ps("e chamou de pH", "i", 64), XE, 320, passo=0.1)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "NaOH: pH = 2", XE, 500, 100, "g", ERRADO, a))
    if t >= C["s11.d"]:
        E.risco(c, XE - 10, 520, XE + 700, 430, t, C["s11.d"], largura=10)
        Q.escala_ph(c, t, C["s11.d"], XE, 640, 1400, 60, marca=2, tm=C["s11.d"] + 0.2)
        E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: E.escreve(c, "seria bem ácida!", XE + 900, 500, 60, "g", ERRADO, a))
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.formula(c, "base: pOH primeiro, depois pH = 14 − pOH", XE, 900, 76, "g", COR, a))


# ---------------- com log 2 ----------------
def b_log(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("e quando não é uma potência de dez exata?", "i", 64), XE, 190, passo=0.1)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "[H⁺] = 2 · 10^{−3}", XE, 360, 100, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "log (2 · 10^{−3}) = log 2 + log 10^{−3}", XE, 540, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.formula(c, "0,3", XE + 560, 660, 76, "g", COR, a))
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.formula(c, "−3", XE + 1060, 660, 76, "g", COR, a))
    E.foco(c, t, C["s12.f"], 0.5, lambda a: E.formula(c, "= −2,7", XE, 820, 90, "g", TINTA2, a))
    bola_txt(c, t, C["s12.g"], "pH 2,7", 1200, 790, 120, 56)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho", "i", 72, CLARO), W / 2, 160, "center", 0.12)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "1 · 10^{−n}  →  pH = n", W / 2, 320, 100, "g", BR, a, "center"))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.escreve(c, "na forma decimal, conte as casas até o 1", 340, 480, 58, "b", CLARO, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "0,001: 3 casas  →  pH 3", W / 2, 620, 90, "g", E.CLARO, a, "center"))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "2 na frente: tire 0,3", W / 2, 780, 80, "g", BR, a, "center"))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "2 · 10^{−3}  →  3 − 0,3 = 2,7", W / 2, 920, 80, "g", E.CLARO, a, "center"))
    if t >= C["s14"]:
        if t < C["s14.b"]:
            pilula_em(c, t, C["s14.a"], "o pH conta as potências de dez", W / 2, 1020, 44, E.COR)
        else:
            pilula_em(c, t, C["s14.b"], "outro número na frente? use o log dado", W / 2, 1020, 44, TINTA2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "[H⁺] = 2 · 10^{−4} mol/L", XE, 380, 96, "g", TINTA, a))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.formula(c, "log 2 = 0,3", XE, 540, 76, "g", TINTA2, a))
    E.frase(c, t, C["s15.c"], [("1", "g", 60, COR), ("pH?", "g", 66)], XE, 720, passo=0.1)
    E.frase(c, t, C["s15.d"], [("2", "g", 60, COR), ("pOH?", "g", 66)], XE, 840, passo=0.1)
    relogio(c, t, C["s16.a"], 1450, 640, 130)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s17"], 0.4, lambda a: E.formula(c, "[H⁺] = 2 · 10^{−4}", XE, 200, 80, "g", TINTA2, a))
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "sem o 2: pH 4", XE, 380, 84, "g", TINTA, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "com o 2: 4 − 0,3 =", XE, 540, 84, "g", TINTA, a))
    bola_txt(c, t, C["s17.c"], "pH 3,7", 1080, 510, 110, 54)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.formula(c, "pOH = 14 − 3,7 =", XE, 760, 84, "g", TINTA, a))
    bola_txt(c, t, C["s17.e"], "10,3", 1000, 730, 100, 60, AZUL)
    if t >= C["s17.f"]:
        Q.escala_ph(c, t, C["s17.f"], XE, 900, 1400, 60, marca=3.7, tm=C["s17.f"] + 0.2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "[H⁺] · [OH⁻] = 10^{−14}", W / 2, 380, 100, "g", TINTA, a, "center"))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "pH = −log [H⁺]", W / 2, 580, 100, "g", TINTA, a, "center"))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "pH + pOH = 14", W / 2, 780, 110, "g", COR, a, "center"))
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    proxima(c, t, C, "s19", [("ácidos", "g", 110, COR), ("fracos", "g", 110)], (C["s19.b"], "o Ka e o grau de ionização"), "s19.c", "s19.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, agua=b_agua, ph=b_ph, exemplo=b_exemplo, erro=b_erro, log=b_log, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
