"""Visual — Estudativo · QUI-EQL-005: hidrólise salina.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha Equilíbrio (QUI-EQL-001) e do módulo pH (QUI-EQL-003): escala de pH,
H⁺ turquesa, OH⁻ azul. Nesta aula: os PAIS DO SAL (pais) = o sal no meio, com a base à esquerda e o ácido à direita, cada um com a
pílula "forte" (tinta) ou "fraco/fraca" (cinza); o resultado sai na escala de pH e numa pílula (ácida turquesa, básica azul,
neutra cinza). Peça candidata ao kit: pais (árvore sal → base + ácido com a força de cada um).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-005_hidrolise_salina.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pais", "regra", "hidrolise", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL = Q.ELETRON
RES = {"ácida": E.COR, "básica": AZUL, "neutra": CINZA}

for eq in ("HCl + NaOH -> NaCl + H2O", "NH4^+ + H2O -> NH3 + H3O^+", "HCO3^- + H2O -> H2CO3 + OH^-"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


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


def pais(c, t, t0, sal, base, f_base, acido, f_acido, cx, y, size=80, tb=None, ta=None, res=None, tr=None, abre=460):
    """o sal no meio, a base à esquerda e o ácido à direita, com a força de cada um; res = 'ácida' | 'básica' | 'neutra'"""
    tb = tb if tb is not None else t0 + 0.5
    ta = ta if ta is not None else tb + 0.5
    E.foco(c, t, t0, 0.4, lambda a: Q.formula(c, sal, cx, y, size, TINTA, a, "center"))
    for k, (tt, s, forte, dx) in enumerate(((tb, base, f_base, -abre), (ta, acido, f_acido, abre))):
        if t < tt:
            continue
        p = ep(t, tt, 0.4)
        M.line(c, cx + dx * 0.25, y + 30, cx + dx * 0.75, y + 110, TINTA2, p, 4)
        E.foco(c, t, tt, 0.4, lambda a, s=s, dx=dx: Q.formula(c, s, cx + dx, y + 200, size * 0.8, TINTA, a, "center"))
        rot = ("forte" if forte else ("fraca" if k == 0 else "fraco"))
        E.foco(c, t, tt + 0.3, 0.4, lambda a, dx=dx, rot=rot, forte=forte: E.pilula(c, rot, cx + dx, y + 290, 44, "g", fundo=TINTA if forte else CINZA, a=a))
    if res and tr is not None:
        pilula_em(c, t, tr, res, cx, y + 290, 56, RES[res])


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (tt, nome, f, ph, x) in enumerate(((C["s01.a"], "sal de cozinha", "NaCl", 7, 360), (C["s01.b"], "bicarbonato", "NaHCO3", 8.3, 960),
                                                  (C["s01.c"], "cloreto de amônio", "NH4Cl", 5.1, 1560))):
            Q.bequer(c, t, tt, x, 620, 300, 300, 0.7, Q.cor_ph(ph), graduacao=False)
            E.foco(c, t, tt + 0.2, 0.4, lambda a, x=x, nome=nome, f=f: (centro(c, nome, x, 250, 50, "i", TINTA2, a), Q.formula(c, f, x, 740, 70, TINTA, a, "center")))
            E.foco(c, t, tt + 0.4, 0.4, lambda a, x=x, ph=ph: centro(c, "pH 7" if ph == 7 else ("pH > 7" if ph > 7 else "pH < 7"), x, 840, 60, "g", COR, a))
        E.frase(c, t, C["s01.d"], ps("três sais, três resultados. como prever?", "i", 64), W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("hidrólise", "g", 110, COR), ("salina", "g", 110)],
             [(C["s02.a"], [("neutra,", "g", 66), ("ácida", "g", 66, COR), ("ou", "i", 70), ("básica", "g", 66, AZUL)]),
              (C["s02.b"], [("a", "i", 74), ("regra", "i", 74), ("do", "i", 74), ("forte", "g", 70, COR), ("vence", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 190, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: Q.formula(c, "HCl + NaOH -> NaCl + H2O", XE, 340, 80, TINTA, a))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.escreve(c, "ácidos fortes:", XE, 500, 56, "b", TINTA2, a), Q.formula(c, "HCl, HNO3, H2SO4", XE + 420, 505, 66, TINTA, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: (E.escreve(c, "bases fortes:", XE, 640, 56, "b", TINTA2, a), Q.formula(c, "NaOH, KOH, Ca(OH)2", XE + 420, 645, 66, TINTA, a)))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.escreve(c, "Brønsted: ácido doa H⁺, base recebe", XE, 800, 62, "g", COR, a))


# ---------------- os pais do sal ----------------
def b_pais(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("descubra os", "i", 74) + [("pais do sal", "g", 70, COR)], XE, 200, passo=0.12)
        pais(c, t, C["s04.b"], "NaCl", "NaOH", True, "HCl", True, W / 2, 400, tb=C["s04.c"], ta=C["s04.d"])
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "metal (ou amônio) + OH", 220, 960, 50, "b", TINTA2, a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.escreve(c, "o resto + H", 1300, 960, 50, "b", TINTA2, a))
        return
    if t < C["s06"]:
        pais(c, t, C["s05.a"], "NaCl", "NaOH", True, "HCl", True, 520, 260, 64, tb=C["s05.b"], ta=C["s05.c"], abre=300)
        pais(c, t, C["s05.d"], "NH4Cl", "NH4OH", False, "HCl", True, 1400, 620, 64, tb=C["s05.e"], ta=C["s05.f"], abre=300)
        return
    pais(c, t, C["s06.a"], "NaHCO3", "NaOH", True, "H2CO3", False, W / 2, 400, tb=C["s06.b"], ta=C["s06.c"])


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("a regra do", "i", 80) + [("forte vence", "g", 76, COR)], XE, 220, passo=0.12)
        linhas = ((C["s07.b"], "ácido forte + base fraca", "ácida"), (C["s07.c"], "base forte + ácido fraco", "básica"), (C["s07.d"], "os dois fortes", "neutra"))
        for k, (tt, s, r) in enumerate(linhas):
            y = 430 + k * 180
            E.foco(c, t, tt, 0.4, lambda a, y=y, s=s: E.escreve(c, s, XE, y, 70, "g", TINTA, a))
            pilula_em(c, t, tt + 0.5, r, 1500, y - 24, 60, RES[r])
        return
    for k, (tt, f, r, ph) in enumerate(((C["s08.a"], "NaCl", "neutra", 7), (C["s08.b"], "NH4Cl", "ácida", 5), (C["s08.c"], "NaHCO3", "básica", 8.3))):
        y = 260 + k * 170
        E.foco(c, t, tt, 0.4, lambda a, y=y, f=f: Q.formula(c, f, XE, y, 80, TINTA, a))
        pilula_em(c, t, tt + 0.4, r, 900, y - 26, 56, RES[r])
    if t >= C["s08.d"]:
        Q.escala_ph(c, t, C["s08.d"], XE, 760, 1400, 60, marca=8.3, tm=C["s08.d"] + 0.2)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, "bicarbonato: alivia a azia", XE, 1040, 54, "b", AZUL, a))


# ---------------- por que funciona ----------------
def b_hidrolise(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("por que funciona?", "i", 70, TINTA2), XE, 170, passo=0.12)
    E.frase(c, t, C["s09.b"], ps("a parte do pai", "i", 64) + [("fraco", "g", 60, COR)] + ps("reage com a água:", "i", 64), XE, 270, passo=0.1)
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "hidrólise", 1350, 270, 64, "g", COR, a))
    Q.formula_em(c, t, C["s09.d"], "NH4^+ + H2O <=> NH3 + H3O^+", XE, 450, 84, cores={"H3O^+": E.COR})
    pilula_em(c, t, C["s09.e"], "H₃O⁺ = o H⁺ preso a uma água", 1500, 540, 40, TINTA2)
    pilula_em(c, t, C["s09.f"], "sobra H⁺: ácida", 560, 560, 50, E.COR)
    if t >= C["s10"]:
        Q.formula_em(c, t, C["s10.a"], "HCO3^- + H2O <=> H2CO3 + OH^-", XE, 740, 84, cores={"OH^-": AZUL})
        pilula_em(c, t, C["s10.c"], "sobra OH⁻: básica", 560, 850, 50, AZUL)
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "a parte do pai forte (Na⁺, Cl⁻) não reage", XE, 1000, 54, "b", TINTA2, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: Q.formula(c, "NaHCO3", XE, 380, 110, TINTA, a, cores={"H": ERRADO}))
    E.foco(c, t, C["s11.a"] + 0.6, 0.4, lambda a: E.escreve(c, "tem H, então é ácido?", XE + 560, 370, 66, "g", ERRADO, a))
    if t >= C["s11.b"]:
        E.risco(c, XE + 550, 390, XE + 1260, 320, t, C["s11.b"], largura=9)
    E.frase(c, t, C["s11.b"], ps("quem decide são os", "i", 66) + [("pais", "g", 62, COR)], XE, 540, passo=0.1)
    pais(c, t, C["s11.c"], "NaHCO3", "NaOH", True, "H2CO3", False, W / 2, 640, 64, tb=C["s11.c"], ta=C["s11.c"] + 0.3, res="básica", tr=C["s11.d"])


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho:", "i", 72, CLARO) + [("o lado forte dá o resultado", "g", 66, BR)], W / 2, 180, "center", 0.12)
    for k, (tt, s, r) in enumerate(((C["s12.b"], "ácido forte", "ácida"), (C["s12.c"], "base forte", "básica"), (C["s12.d"], "os dois fortes", "neutra"))):
        y = 380 + k * 160
        E.foco(c, t, tt, 0.4, lambda a, y=y, s=s: E.escreve(c, s, 480, y, 76, "g", BR, a))
        pilula_em(c, t, tt + 0.3, r, 1300, y - 26, 60, RES[r] if r != "neutra" else TINTA2)
    E.frase(c, t, C["s12.e"], ps("os dois fracos? compare a força de cada um", "i", 58, CLARO), W / 2, 900, "center", 0.1)
    pilula_em(c, t, C["s12.f"], "a questão precisa dar os valores", W / 2, 1010, 46, TINTA2)


# ---------------- questão ----------------
QS = (("KNO3", "nitrato de potássio"), ("Na2CO3", "carbonato de sódio"), ("NH4NO3", "nitrato de amônio"))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar: neutra, ácida ou básica?", "i", 66, COR), XE, 180, passo=0.1)
    for k, (tt, (f, nome)) in enumerate(zip((C["s13.a"], C["s13.b"], C["s13.c"]), QS)):
        y = 400 + k * 200
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(k + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.foco(c, t, tt + 0.1, 0.4, lambda a, y=y, f=f, nome=nome: (Q.formula(c, f, XE + 120, y, 86, TINTA, a), E.escreve(c, nome, XE + 600, y - 8, 56, "i", TINTA2, a)))
    relogio(c, t, C["s14.a"], 1600, 600, 110)


def b_resposta(c, t, C, b):
    dados = ((C["s15.a"], C["s15.b"], "KNO3", "KOH", True, "HNO3", True, "neutra"), (C["s15.c"], C["s15.d"], "Na2CO3", "NaOH", True, "H2CO3", False, "básica"),
             (C["s15.e"], C["s15.f"], "NH4NO3", "NH4OH", False, "HNO3", True, "ácida"))
    for k, (tt, tr, sal, bs, fb, ac, fa, r) in enumerate(dados):
        y = 260 + k * 270
        E.foco(c, t, tt, 0.4, lambda a, y=y, sal=sal: Q.formula(c, sal, XE, y, 76, TINTA, a))
        E.foco(c, t, tt + 0.3, 0.4, lambda a, y=y, bs=bs, fb=fb: (Q.formula(c, bs, 720, y, 62, TINTA, a), E.pilula(c, "forte" if fb else "fraca", 720 + 90, y + 60, 36, "g", fundo=TINTA if fb else CINZA, a=a)))
        E.foco(c, t, tt + 0.6, 0.4, lambda a, y=y, ac=ac, fa=fa: (Q.formula(c, ac, 1080, y, 62, TINTA, a), E.pilula(c, "forte" if fa else "fraco", 1080 + 90, y + 60, 36, "g", fundo=TINTA if fa else CINZA, a=a)))
        pilula_em(c, t, tr, r, 1620, y - 22, 58, RES[r])


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s16.a"], ps("ache os", "i", 74) + [("pais do sal", "g", 70, COR)], W / 2, 360, "center", 0.12)
        E.frase(c, t, C["s16.b"], ps("e deixe o", "i", 74) + [("forte vencer", "g", 70, COR)], W / 2, 500, "center", 0.12)
        for k, r in enumerate(("ácida", "básica", "neutra")):
            pilula_em(c, t, C["s16.c"] + 0.4 * k, r, 520 + k * 440, 720, 60, RES[r])
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    proxima(c, t, C, "s17", [("solução", "g", 110, COR), ("tampão", "g", 110)], (C["s17.b"], "a que segura o pH, como a do sangue"), "s17.c", "s17.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pais=b_pais, regra=b_regra, hidrolise=b_hidrolise, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
