"""Visual — Estudativo · QUI-EQL-006: solução tampão.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha Equilíbrio (QUI-EQL-001) e do módulo pH (QUI-EQL-003): H⁺ turquesa,
OH⁻ azul, A⁻ cinza-escuro, HA em tinta; escala de pH. Nesta aula: as DUAS DEFESAS do tampão são dois "escudos" (escudo): o ácido HA
(contra base) e a base conjugada A⁻ (contra ácido); o íon que chega voa até o escudo e some. O pH na escala quase não se mexe.
Peça candidata ao kit: escudo (defesa do tampão que captura o íon que chega).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-006_solucao_tampao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("oque", "como", "sangue", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL = Q.ELETRON
ESCURO = "#3A3B40"

assert -math.log10(1e-5) == 5 and abs(-math.log10(2e-5) - 4.7) < 0.01 and abs(-math.log10(1.8e-5) - 4.74) < 0.01
assert -math.log10(1e-4) == 4


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


def ion(c, cx, cy, r, s, cor, a=1.0):
    if a <= 0:
        return
    E.bola(c, cx, cy, r, cor, a)
    Q.formula(c, s, cx, cy + r * 0.32, r * 0.8, BR, a, "center")


def escudo(c, t, t0, cx, cy, s, cor, rot, a=1.0):
    """uma defesa do tampão: bolinha grande com a fórmula e o rótulo embaixo"""
    E.foco(c, t, t0, 0.4, lambda q: (ion(c, cx, cy, 80, s, cor, q * a), centro(c, rot, cx, cy + 150, 48, "b", TINTA2, q * a)))


def chega(c, t, t0, x0, y0, x1, y1, s, cor, d=1.2):
    """o íon que chega voa até a defesa e some"""
    if t < t0:
        return
    u = prog(t, t0, d)
    if u >= 1:
        return
    k = ease_io(u)
    ion(c, lerp(x0, x1, k), lerp(y0, y1, k), 44, s, cor, 1 - ep(t, t0 + d * 0.8, d * 0.2))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.formula(c, "sangue: pH 7,35 a 7,45", XE, 300, 96, "g", TINTA, a))
        Q.escala_ph(c, t, C["s01.a"] + 0.3, XE, 400, 1500, 70, marca=7.4, tm=C["s01.a"] + 0.6)
        for k, s in enumerate(("limão", "refrigerante", "exercício")):
            pilula_em(c, t, C["s01.b"] + 0.4 * k, s, 420 + k * 420, 700, 54, TINTA, "b")
        E.frase(c, t, C["s01.c"], ps("e o pH quase não sai da faixa", "i", 66), XE, 860, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("quem segura?", "i", 70) + [("uma solução tampão", "g", 66, COR)], XE, 990, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("solução", "g", 110, COR), ("tampão", "g", 110)],
             [(C["s02.a"], [("como", "i", 74), ("segura", "i", 74), ("o", "i", 74), ("pH", "g", 70, COR)]),
              (C["s02.b"], [("pH", "g", 70), ("com", "i", 74), ("ácido", "i", 74), ("e", "i", 74), ("sal", "i", 74), ("iguais", "g", 70, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 200, passo=0.12)
    kfrac(c, t, C["s03.a"], "a", "[H^+] · [A^-]", "[HA]", XE, 400, 96)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.escreve(c, "A⁻: a base conjugada", XE + 1000, 410, 60, "g", TINTA, a))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.escreve(c, "Le Chatelier: o equilíbrio foge da perturbação", XE, 720, 62, "g", COR, a))


# ---------------- o que é ----------------
def b_oque(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("tampão", "g", 80, COR), ("=", "g", 80, TINTA2)] + ps("ácido fraco + sal dele", "i", 80), XE, 220, passo=0.12)
    E.foco(c, t, C["s04.b"], 0.5, lambda a: Q.formula(c, "CH3COOH + CH3COONa", XE, 380, 86, TINTA, a))
    E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.escreve(c, "ácido acético + acetato de sódio", XE, 460, 50, "b", TINTA2, a))
    E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "o sal entrega muito acetato, A⁻", XE, 580, 56, "b", TINTA, a))
    escudo(c, t, C["s04.e"], 560, 760, "HA", TINTA, "contra base")
    escudo(c, t, C["s04.f"], 1360, 760, "A^-", ESCURO, "contra ácido")
    pilula_em(c, t, C["s04.d"], "duas defesas", W / 2, 680, 50, E.COR)
    pilula_em(c, t, C["s04.g"], "também vale: base fraca + sal dela", W / 2, 1020, 42, TINTA2)


# ---------------- como segura ----------------
def b_como(c, t, C, b):
    if t < C["s07"]:
        escudo(c, t, C["s05"] - 0.6, 560, 520, "HA", TINTA, "ácido acético")
        escudo(c, t, C["s05"] - 0.6, 1360, 520, "A^-", ESCURO, "acetato")
        if t < C["s06"]:
            pilula_em(c, t, C["s05.a"], "pingou ácido forte", W / 2, 200, 54, E.COR)
            chega(c, t, C["s05.b"], W / 2, 300, 1360, 520, "H^+", E.COR, 1.4)
            E.foco(c, t, C["s05.c"], 0.4, lambda a: Q.formula(c, "H^+ + A^- -> HA", W / 2, 860, 90, TINTA, a, "center"))
            pilula_em(c, t, C["s05.d"], "o H⁺ some: o pH quase não muda", W / 2, 990, 48, TINTA)
        else:
            pilula_em(c, t, C["s06.a"], "pingou base forte", W / 2, 200, 54, AZUL)
            chega(c, t, C["s06.b"], W / 2, 300, 560, 520, "OH^-", AZUL, 1.4)
            E.foco(c, t, C["s06.c"], 0.4, lambda a: Q.formula(c, "HA + OH^- -> A^- + H2O", W / 2, 860, 90, TINTA, a, "center"))
            pilula_em(c, t, C["s06.d"], "o OH⁻ some: o pH quase não muda", W / 2, 990, 48, TINTA)
        return
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("pelo Le Chatelier, é a mesma história", "i", 66), XE, 220, passo=0.1)
        Q.formula_em(c, t, C["s07.b"], "HA <=> H^+ + A^-", W / 2, 420, 120, align="center")
        if t >= C["s07.c"]:
            pilula_em(c, t, C["s07.c"], "chegou H⁺", 500, 600, 50, E.COR)
            F.seta(c, 1100, 680, 800, 680, CINZA, ep(t, C["s07.c"] + 0.3, 0.4), 16, 40)
            E.foco(c, t, C["s07.c"] + 0.5, 0.4, lambda a: E.escreve(c, "vai para a esquerda e consome", 1150, 700, 50, "b", TINTA2, a))
        if t >= C["s07.d"]:
            pilula_em(c, t, C["s07.d"], "a base levou H⁺", 500, 840, 50, AZUL)
            F.seta(c, 800, 920, 1100, 920, E.COR, ep(t, C["s07.d"] + 0.3, 0.4), 16, 40)
            E.foco(c, t, C["s07.d"] + 0.5, 0.4, lambda a: E.escreve(c, "vai para a direita e repõe", 1150, 940, 50, "b", COR, a))
        return
    E.frase(c, t, C["s08.a"], ps("mas o tampão tem", "i", 80) + [("limite", "g", 76, ERRADO)], XE, 330, passo=0.12)
    E.frase(c, t, C["s08.b"], ps("ácido ou base demais esgota as defesas", "i", 66, TINTA2), XE, 500, passo=0.1)
    Q.escala_ph(c, t, C["s08.c"], XE, 700, 1500, 70, marca=4.7 - 3.0 * ep(t, C["s08.c"] + 0.4, 1.0), tm=C["s08.c"] + 0.2)


# ---------------- o sangue ----------------
def b_sangue(c, t, C, b):
    E.frase(c, t, C["s09"], ps("no sangue", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: (Q.formula(c, "H2CO3", XE, 380, 110, TINTA, a), E.escreve(c, "ácido carbônico", XE, 460, 50, "b", TINTA2, a)))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (Q.formula(c, "HCO3^-", XE + 700, 380, 110, TINTA, a), E.escreve(c, "bicarbonato", XE + 700, 460, 50, "b", TINTA2, a)))
    Q.escala_ph(c, t, C["s09.c"], XE, 620, 1500, 70, marca=7.4, tm=C["s09.c"] + 0.2)
    pilula_em(c, t, C["s09.c"] + 0.6, "abaixo de 7,35: acidose", 560, 880, 46, E.COR)
    pilula_em(c, t, C["s09.c"] + 1.6, "acima de 7,45: alcalose", 1360, 880, 46, AZUL)
    pilula_em(c, t, C["s09.d"], "ambas perigosas", W / 2, 1010, 46, ERRADO)


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("agora, a conta", "i", 72, TINTA2), XE, 180, passo=0.12)
        kfrac(c, t, C["s10.b"], "a", "[H^+] · [A^-]", "[HA]", XE, 400, 110)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "A⁻: quase todo do sal", 1150, 340, 52, "b", TINTA2, a))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "HA: quase não se ioniza", 1150, 470, 52, "b", TINTA2, a))
        pilula_em(c, t, C["s10.e"], "concentrações iguais: [A⁻] = [HA]", W / 2, 680, 52, E.COR)
        if t >= C["s10.f"]:
            E.risco(c, 700, 410, 860, 330, t, C["s10.f"], cor=CINZA, largura=8)
            E.risco(c, 600, 540, 760, 460, t, C["s10.f"] + 0.2, cor=CINZA, largura=8)
        E.foco(c, t, C["s10.g"], 0.5, lambda a: Q.formula(c, "Ka = [H^+]", W / 2, 900, 130, COR, a, "center"))
        return
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.formula(c, "pH = pKa = −log Ka", W / 2, 260, 110, "g", TINTA, a, "center"))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "Ka = 10^{−5}", XE, 470, 90, "g", TINTA, a))
    bola_txt(c, t, C["s11.c"], "pH 5", 900, 440, 90, 54)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "ácido acético: Ka ≈ 2 · 10^{−5}", XE, 680, 80, "g", TINTA, a))
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.formula(c, "5 − 0,3 =", XE, 860, 90, "g", TINTA2, a))
    bola_txt(c, t, C["s11.f"], "4,7", 760, 830, 90, 64)
    E.foco(c, t, C["s11.f"] + 0.3, 0.4, lambda a: E.escreve(c, "log 2 ≈ 0,3", 940, 860, 56, "b", TINTA2, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.escreve(c, "“todo tampão tem pH 7”", XE, 330, 70, "g", ERRADO, a))
    if t >= C["s12.b"]:
        E.risco(c, XE - 10, 345, XE + 860, 280, t, C["s12.b"], largura=9)
    E.frase(c, t, C["s12.b"], ps("tampão não quer dizer neutro:", "i", 64) + [("quer dizer estável", "g", 60, COR)], XE, 470, passo=0.1)
    Q.escala_ph(c, t, C["s12.c"], XE, 600, 1500, 70, marca=4.7, tm=C["s12.c"] + 0.2)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "acetato: perto de 4,7", XE, 860, 56, "b", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "sangue: perto de 7,4 (mais bicarbonato que ácido)", XE, 960, 52, "b", TINTA, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho", "i", 72, CLARO), W / 2, 160, "center", 0.12)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "ácido = sal  →  pH = pKa", W / 2, 330, 100, "g", BR, a, "center"))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "Ka = 10^{−n}  →  pH = n", W / 2, 500, 90, "g", E.CLARO, a, "center"))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "tampão: ácido fraco + sal do mesmo ácido", 380, 680, 60, "b", BR, a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (Q.formula(c, "HCl + NaCl", 600, 860, 90, BR, a, escuro=True), E.escreve(c, "não é tampão", 1100, 860, 70, "g", ERRADO, a)))
    pilula_em(c, t, C["s13.e"], "o Cl⁻ não segura H⁺", W / 2, 990, 46, TINTA2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "ácido fraco: Ka = 10^{−4}", XE, 360, 86, "g", TINTA, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "ácido e sal: 0,1 mol/L cada", XE, 500, 76, "g", TINTA, a))
    E.frase(c, t, C["s14.c"], [("1", "g", 60, COR), ("pH?", "g", 62)], XE, 680, passo=0.1)
    E.frase(c, t, C["s14.d"], [("2", "g", 60, COR)] + ps("pingou HCl: quem consome o H⁺?", "b", 56), XE, 800, passo=0.1)
    relogio(c, t, C["s15.a"], 1500, 620, 120)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "ácido = sal  →  pH = pKa", XE, 260, 86, "g", TINTA, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "Ka = 10^{−4}", XE, 420, 86, "g", TINTA, a))
    bola_txt(c, t, C["s16.b"] + 0.4, "pH 4", 860, 390, 90, 54)
    escudo(c, t, C["s16.c"], 1400, 520, "A^-", ESCURO, "a base conjugada, do sal")
    chega(c, t, C["s16.c"] + 0.3, 1000, 300, 1400, 520, "H^+", E.COR, 1.4)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: Q.formula(c, "H^+ + A^- -> HA", XE, 800, 90, TINTA, a))
    pilula_em(c, t, C["s16.e"], "o pH fica perto de 4", W / 2, 980, 52, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s17.a"], [("tampão", "g", 70, COR)] + ps("= ácido fraco + o seu sal", "i", 74), W / 2, 360, "center", 0.12)
        E.frase(c, t, C["s17.b"], ps("a base conjugada consome ácido; o ácido consome base", "i", 60, TINTA2), W / 2, 520, "center", 0.08)
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "iguais: pH = pKa", W / 2, 720, 110, "g", COR, a, "center"))
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    proxima(c, t, C, "s18", [("produto", "g", 100, COR), ("de", "i", 100), ("solubilidade", "g", 100, COR)],
            (C["s18.b"], "o Kps e o precipitado"), "s18.c", "s18.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oque=b_oque, como=b_como, sangue=b_sangue, conta=b_conta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
