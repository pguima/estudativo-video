"""Visual — Estudativo · QUI-EQL-007: produto de solubilidade, Kps.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha Equilíbrio (QUI-EQL-001) e do módulo pH (QUI-EQL-003). Nesta aula:
SOLUÇÃO SATURADA = béquer com o sólido no fundo (Q.bequer) e íons dissolvidos em bolinhas (cátion turquesa, ânion cinza-escuro) que
saem do sólido e voltam; o Kps em fração sem denominador (kfrac); a solubilidade "s" na cor da matéria. PRECIPITADO = sólido que
aparece caindo no fundo do béquer. Comparação Q × Kps numa balança de texto: ">" forma precipitado (pílula tinta), "<" não forma.
Peça candidata ao kit: saturada (béquer com sólido no fundo e íons indo e voltando), precipita (sólido se formando).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-007_produto_solubilidade_kps.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("kps", "solub", "precip", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ESCURO = "#3A3B40"

assert abs(math.sqrt(1e-10) - 1e-5) < 1e-18
assert abs(3.2e-11 / 4 - 8e-12) < 1e-24 and abs((8e-12) ** (1 / 3) - 2e-4) < 1e-12 and abs(4 * (2e-4) ** 3 - 3.2e-11) < 1e-22
assert 1e-3 * 1e-3 > 1e-10
assert abs((4e-9 / 4) ** (1 / 3) - 1e-3) < 1e-12 and abs(1e-2 * (1e-4) ** 2 - 1e-10) < 1e-22 and 1e-10 < 4e-9
assert abs((3.2e-11) ** (1 / 3) - 3.17e-4) < 1e-6     # o erro (s³ sem o 4) dá ~3 × 10⁻⁴


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


def saturada(c, t, t0, cx, yb, w=380, h=420, cat="Ba^{2+}", an="SO4^{2-}", fundo="#FFFFFF", precip=0.0):
    """béquer com sólido no fundo e íons que saem dele e voltam"""
    Q.bequer(c, t, t0, cx, yb, w, h, 0.72, Q.AGUA, graduacao=False)
    q = ep(t, t0 + 0.4, 0.5)
    if q <= 0:
        return
    c.drawOval(skia.Rect.MakeLTRB(cx - w * 0.38, yb - 48, cx + w * 0.38, yb - 6), M.paint(fundo, q))
    c.drawOval(skia.Rect.MakeLTRB(cx - w * 0.38, yb - 48, cx + w * 0.38, yb - 6), M.paint(TINTA2, q, stroke=3))
    for k in range(6):
        ph = (t * 0.25 + k / 6) % 1.0
        sobe = math.sin(ph * math.pi)
        px = cx - w * 0.3 + (k * 53 % int(w * 0.6))
        py = yb - 50 - sobe * h * 0.45
        cor = E.COR if k % 2 == 0 else ESCURO
        c.drawCircle(px, py, 16, M.paint(cor, q))
    if precip > 0:
        for k in range(18):
            px = cx - w * 0.35 + (k * 37 % int(w * 0.7))
            py = lerp(yb - h * 0.6, yb - 40 - (k % 3) * 12, ease_out(min(1.0, precip * 1.5 - k * 0.02)))
            c.drawRect(skia.Rect.MakeXYWH(px, py, 14, 14), M.paint("#F2C94C" if fundo != "#FFFFFF" else "#FFFFFF", q))
            c.drawRect(skia.Rect.MakeXYWH(px, py, 14, 14), M.paint(TINTA2, q, stroke=2))


def compara(c, t, t0, esq, sinal, dir_, x, y, size=80):
    """Q > Kps / Q < Kps, com a decisão embaixo"""
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, f"{esq}  {sinal}  {dir_}", x, y, size, "g", TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        saturada(c, t, C["s01.a"], 1450, 900)
        E.frase(c, t, C["s01.a"], ps("raio X do estômago:", "i", 64), XE, 240, passo=0.1)
        E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: (Q.formula(c, "BaSO4", XE, 370, 100, TINTA, a), E.escreve(c, "sulfato de bário", XE + 380, 360, 54, "b", TINTA2, a)))
        E.frase(c, t, C["s01.b"], [("Ba²⁺", "g", 60, ERRADO)] + ps("solto no sangue: venenoso", "i", 60), XE, 520, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("mesmo assim, o exame é", "i", 62) + [("seguro", "g", 58, COR)], XE, 660, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("quase nada se dissolve", "i", 62), XE, 800, passo=0.1)
        E.frase(c, t, C["s01.e"], ps("quanto é esse", "i", 66) + [("quase nada?", "g", 62, COR)], XE, 960, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("Kps", "g", 120, COR)],
             [(C["s02.a"], [("o", "i", 74), ("Kps", "g", 70), ("de", "i", 74), ("BaSO₄", "g", 70), ("e", "i", 74), ("CaF₂", "g", 70)]),
              (C["s02.b"], [("calcular", "i", 74), ("a", "i", 74), ("solubilidade", "g", 70, COR)]),
              (C["s02.c"], [("vai", "i", 74), ("formar", "i", 74), ("precipitado?", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "saturada: não dissolve mais, sobra sólido no fundo", XE, 380, 60, "g", TINTA, a))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.escreve(c, "na constante, o sólido fica de fora", XE, 540, 60, "g", COR, a))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: (E.formula(c, "r{10^{−10}} = 10^{−5}", XE, 740, 86, "g", TINTA, a), E.formula(c, "r3{8} = 2", XE + 820, 740, 86, "g", TINTA, a)))
    saturada(c, t, C["s03.a"] + 0.4, 1650, 1000, 260, 280)


# ---------------- o Kps ----------------
def b_kps(c, t, C, b):
    E.saida(c, t, C["s05.e"] - 0.1, lambda: saturada(c, t, C["s04"], 1550, 900, 380, 420))
    E.frase(c, t, C["s04.a"], ps("o sólido do fundo se dissolve", "i", 60), XE, 220, passo=0.1)
    E.frase(c, t, C["s04.b"], ps("e os íons voltam,", "i", 60) + [("na mesma velocidade", "g", 56, COR)], XE, 310, passo=0.1)
    E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "é um equilíbrio", XE, 400, 56, "g", TINTA, a))
    Q.formula_em(c, t, C["s04.d"], "BaSO4(s) <=> Ba^{2+}(aq) + SO4^{2-}(aq)", XE, 540, 70)
    if t >= C["s05"]:
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.escreve(c, "produto de solubilidade, Kps", XE, 660, 60, "g", COR, a))
        if t >= C["s05.b"]:
            wk = Q.formula(None, "BaSO4(s)", 0, 0, 70)
            E.risco(c, XE, 555, XE + wk, 480, t, C["s05.b"], cor=CINZA, largura=7)
        kfrac(c, t, C["s05.c"], "ps", "[Ba^{2+}] · [SO4^{2-}]", None, XE, 780, 86)
        Q.formula_em(c, t, C["s05.e"], "CaF2(s) <=> Ca^{2+} + 2 F^-", 1080, 660, 66, cores={"coef": E.COR})
        kfrac(c, t, C["s05.f"], "ps", "[Ca^{2+}] · [F^-]^{2}", None, 1080, 780, 74)


# ---------------- solubilidade ----------------
def b_solub(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s06.a"], [("solubilidade", "g", 80, COR)] + ps("quanto se dissolve até saturar", "i", 64), XE, 200, passo=0.1)
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.formula(c, "= s (mol/L)", XE + 1200, 205, 66, "g", TINTA, a))
        Q.formula_em(c, t, C["s06.c"], "BaSO4 <=> Ba^{2+} + SO4^{2-}", XE, 360, 80)
        sp = Q.centros("BaSO4 <=> Ba^{2+} + SO4^{2-}", XE, 360, 80, "left")
        E.foco(c, t, C["s06.d"], 0.4, lambda a: (centro(c, "s", sp[1], 450, 70, "g", COR, a), centro(c, "s", sp[2], 450, 70, "g", COR, a)))
        if t >= C["s07"]:
            E.foco(c, t, C["s07.a"], 0.5, lambda a: E.formula(c, "Kps = s · s = s^2", XE, 600, 90, "g", TINTA, a))
            E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "s^2 = 10^{−10}", XE, 760, 90, "g", TINTA, a))
            E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "s = 10^{−5} mol/L", XE + 700, 760, 90, "g", COR, a))
            pilula_em(c, t, C["s07.d"], "100 000 vezes menos que 1 mol por litro", W / 2, 920, 50, TINTA)
        return
    if t < C["s09"]:
        Q.formula_em(c, t, C["s08.a"], "CaF2 <=> Ca^{2+} + 2 F^-", XE, 260, 90, cores={"coef": E.COR})
        sp = Q.centros("CaF2 <=> Ca^{2+} + 2 F^-", XE, 260, 90, "left")
        E.foco(c, t, C["s08.b"], 0.4, lambda a: centro(c, "s", sp[1], 360, 70, "g", COR, a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "2s", sp[2], 360, 70, "g", COR, a))
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.formula(c, "Kps = s · (2s)^2", XE, 560, 96, "g", TINTA, a))
        E.foco(c, t, C["s08.d"] + 1.2, 0.5, lambda a: E.formula(c, "= s · 4s^2", XE + 820, 560, 96, "g", TINTA2, a))
        E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "Kps = 4s^3", XE, 760, 130, "g", COR, a))
        return
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.formula(c, "4s^3 = 3,2 · 10^{−11}", XE, 240, 86, "g", TINTA, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "s^3 = f{3,2 · 10^{−11}}{4} = 0,8 · 10^{−11} = 8 · 10^{−12}", XE, 430, 76, "g", TINTA, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "r3{8} = 2", XE, 640, 86, "g", TINTA, a))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "r3{10^{−12}} = 10^{−4}", XE + 600, 640, 86, "g", TINTA, a))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "s = 2 · 10^{−4} mol/L", XE, 860, 110, "g", COR, a))


# ---------------- precipitado ----------------
def b_precip(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s10.a"], [("precipitado", "g", 80, COR)] + ps("= o sólido que se forma", "i", 66), XE, 200, passo=0.1)
        E.frase(c, t, C["s10.b"], ps("calcule o produto dos íons como o Kps,", "i", 60), XE, 320, passo=0.1)
        E.frase(c, t, C["s10.c"], ps("com as concentrações da mistura", "i", 60), XE, 400, passo=0.1)
        if t >= C["s11"]:
            for k, (tt, s, r) in enumerate(((C["s11.a"], "produto > Kps", "forma precipitado"), (C["s11.c"], "produto < Kps", "tudo dissolvido"), (C["s11.d"], "produto = Kps", "no limite: saturada"))):
                y = 580 + k * 150
                E.foco(c, t, tt, 0.4, lambda a, y=y, s=s: E.formula(c, s, XE, y, 76, "g", TINTA, a))
                pilula_em(c, t, tt + 0.4, r, 1300, y - 26, 54, (TINTA, E.COR, CINZA)[k])
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "[Ba²⁺] = 10^{−3},  [SO₄²⁻] = 10^{−3}", XE, 260, 76, "g", TINTA, a))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "produto = 10^{−3} · 10^{−3} = 10^{−6}", XE, 440, 80, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "10^{−6}  >  10^{−10}", XE, 620, 96, "g", COR, a))
    saturada(c, t, C["s12.c"], 1500, 960, 340, 360, precip=ep(t, C["s12.d"], 2.0))
    pilula_em(c, t, C["s12.d"], "forma precipitado", 700, 820, 60, TINTA)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("o fluoreto conta", "i", 66) + [("em dobro", "g", 62, COR)], XE, 320, passo=0.1)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "Kps = s · s^2 = s^3", XE, 500, 96, "g", ERRADO, a))
    if t >= C["s13.c"]:
        E.risco(c, XE - 10, 520, XE + 880, 420, t, C["s13.c"] - 0.3, largura=10)
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "s ≈ 3 · 10^{−4}: errado", XE + 980, 500, 66, "g", ERRADO, a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: Q.formula(c, "CaF2 -> Ca^{2+} + 2 F^-", XE, 700, 86, TINTA, a, cores={"coef": E.COR}))
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "[F⁻] = 2s  →  Kps = 4s^3", XE, 880, 96, "g", COR, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14.a"], ps("o atalho: decore dois formatos", "i", 72, CLARO), W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: (E.escreve(c, "um íon de cada", 300, 380, 66, "g", BR, a), Q.formula(c, "BaSO4", 300, 480, 76, CLARO, a, escuro=True)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "Kps = s^2", 1300, 430, 110, "g", E.CLARO, a))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: (E.escreve(c, "um de um tipo, dois do outro", 300, 660, 66, "g", BR, a), Q.formula(c, "CaF2", 300, 760, 76, CLARO, a, escuro=True)))
    E.foco(c, t, C["s14.e"], 0.5, lambda a: E.formula(c, "Kps = 4s^3", 1300, 710, 110, "g", E.CLARO, a))
    if t >= C["s15"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: E.formula(c, "(2s)^2 = 4s^2", W / 2, 950, 76, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: (Q.formula(c, "PbI2", XE, 340, 110, TINTA, a), E.escreve(c, "iodeto de chumbo: 1 chumbo e 2 iodetos", XE + 380, 330, 52, "b", TINTA2, a)))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "Kps = 4 · 10^{−9}", XE, 500, 86, "g", TINTA, a))
    E.frase(c, t, C["s16.c"], [("1", "g", 60, COR), ("solubilidade?", "g", 62)], XE, 670, passo=0.1)
    E.frase(c, t, C["s16.d"], [("2", "g", 60, COR)] + ps("mistura: [Pb²⁺] = 10⁻², [I⁻] = 10⁻⁴. precipita?", "b", 52), XE, 790, passo=0.08)
    relogio(c, t, C["s17.a"], 1550, 560, 110)
    E.foco(c, t, C["s16.a"] + 0.4, 0.4, lambda a: None)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.escreve(c, "1 chumbo e 2 iodetos: formato 4s³", XE, 220, 62, "g", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "4s^3 = 4 · 10^{−9}", XE, 380, 86, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "s^3 = 10^{−9}", XE + 800, 380, 86, "g", TINTA2, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.formula(c, "s = 10^{−3} mol/L", XE, 540, 96, "g", COR, a))
    if t >= C["s19"]:
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "produto = 10^{−2} · (10^{−4})^2", XE, 720, 80, "g", TINTA, a))
        E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "= 10^{−10}", XE + 1060, 720, 80, "g", TINTA, a))
        E.foco(c, t, C["s19.d"], 0.5, lambda a: E.formula(c, "10^{−10}  <  4 · 10^{−9}", XE, 880, 90, "g", COR, a))
        pilula_em(c, t, C["s19.e"], "não forma precipitado", 1400, 855, 54, E.COR)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s20.a"], [("Kps", "g", 70, COR)] + ps("= produto dos íons, coeficientes no expoente", "i", 64), W / 2, 360, "center", 0.1)
        E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "s^2  ou  4s^3", W / 2, 560, 110, "g", TINTA, a, "center"))
        E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "produto > Kps: precipita", W / 2, 760, 96, "g", COR, a, "center"))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    proxima(c, t, C, "s21", [("praticando", "g", 110, COR)], (C["s21.b"], "deslocamento, pH e solubilidade"), "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, kps=b_kps, solub=b_solub, precip=b_precip, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
