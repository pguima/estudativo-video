"""Visual — Estudativo · QUI-EQL-009: calcular Kc pelo quadro início, reage, equilíbrio.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha Equilíbrio Químico (cabeçalho da QUI-EQL-001): seta dupla,
constante em fração (kfrac). Nesta aula entra o QUADRO início/reage/equilíbrio (quadro): espécies no cabeçalho, linha do reage
com "−" em vermelho para o que se gasta e "+" em turquesa para o que se forma; a linha do equilíbrio em turquesa escuro é a única
que vai para o Kc (uma seta leva os números dela para a fração). Grau de equilíbrio (α) em pílula com a porcentagem.
Peça candidata ao kit: quadro (tabela início, reage, equilíbrio).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-009_calcular_kc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("direto", "quadro", "grau", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula
assert abs(0.8 ** 2 / (0.1 * 0.1) - 64) < 1e-9
assert abs(1.6 / 2 - 0.8) < 1e-12 and abs(1 - 0.8 - 0.2) < 1e-12 and abs(1.6 ** 2 / (0.2 * 0.2) - 64) < 1e-9
assert abs(0.8 / 1 - 0.80) < 1e-12 and abs(1.6 ** 2 / (1 * 1) - 2.56) < 1e-9
assert abs(2 / 2 - 1) < 1e-12 and abs(0.8 / 2 - 0.4) < 1e-12 and abs(0.4 / 2 - 0.2) < 1e-12
assert abs(0.4 ** 2 / 0.8 - 0.2) < 1e-12 and abs(0.2 / 1 - 0.20) < 1e-12
assert Q.lados("H2 + I2 -> 2 HI")[0] == Q.lados("H2 + I2 -> 2 HI")[1]

EQ = "H2(g) + I2(g) <=> 2 HI(g)"
EQN = "N2O4(g) <=> 2 NO2(g)"


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("hidrogênio e iodo num frasco", "i", 66), XE, 230, passo=0.1)
        Q.formula_em(c, t, C["s01.a"] + 1.0, EQ, W / 2, 400, 96, align="center")
        E.frase(c, t, C["s01.b"], ps("você mede uma coisa só:", "i", 64), XE, 580, passo=0.1)
        E.foco(c, t, C["s01.b"] + 1.2, 0.5, lambda a: Q.formula(c, "[HI]", XE + 760, 590, 90, COR, a))
        E.frase(c, t, C["s01.c"], ps("e descobre o resto e o", "i", 64) + [("Kc", "g", 60, COR)], XE, 740, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("o truque: um", "i", 66) + [("quadro de três linhas", "g", 62, COR)], XE, 900, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("calcular", "g", 100, COR), ("o", "i", 100), ("Kc", "g", 100)],
             [(C["s02.a"], [("o", "i", 74), ("Kc", "g", 70)]), (C["s02.b"], [("o", "i", 74), ("grau", "g", 70), ("de", "i", 74), ("equilíbrio", "g", 70)]),
              (C["s02.c"], [("início,", "g", 66), ("reage,", "g", 66), ("equilíbrio", "g", 66, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 80, TINTA2), XE, 200, passo=0.12)
    kfrac(c, t, C["s03.a"], "c", "produtos", "reagentes", XE, 420, 100)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.formula(c, "f{0,64}{0,01} = f{64}{1} = 64", XE, 760, 86, "g", TINTA, a))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "0,8 = 80%", XE + 1000, 760, 86, "g", TINTA, a))


# ---------------- cálculo direto ----------------
def b_direto(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("a questão já dá o", "i", 66) + [("equilíbrio", "g", 62, COR)], XE, 170, passo=0.1)
    Q.formula_em(c, t, C["s04.b"], EQ, W / 2, 320, 90, align="center")
    sp = Q.centros(EQ, W / 2, 320, 90, "center")
    for k, (tt, v) in enumerate(((C["s04.c"], "0,1"), (C["s04.d"], "0,1"), (C["s04.e"], "0,8"))):
        E.foco(c, t, tt, 0.4, lambda a, k=k, v=v: E.pilula(c, v, sp[k], 430, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "mol/L", sp[2] + 160, 445, 42, "i", TINTA2, a))
    kfrac(c, t, C["s05.a"], "c", "[HI]^{2}", "[H2] · [I2]", XE, 640, 96)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "0,8^2 = 0,64", 1150, 600, 64, "g", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.formula(c, "0,1 × 0,1 = 0,01", 1150, 720, 64, "g", TINTA2, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.formula(c, "f{0,64}{0,01} =", 1150, 900, 76, "g", TINTA, a))
    bola_txt(c, t, C["s05.e"], "64", 1580, 875, 80, 66)


# ---------------- o quadro ----------------
QX, QY = 170, 380
ESP = ("H2", "I2", "HI")


def b_quadro(c, t, C, b):
    Q.formula_em(c, t, C["s06"], EQ, W / 2, 200, 84, align="center", cores={"coef": E.COR} if t >= C["s08.a"] else None)
    L = [["1", "1", "0"], [None, None, None], [None, None, None]]
    tl = [[C["s07.a"]] * 3, [C["s08.d"], C["s08.d"] + 0.3, C["s07.d"]], [C["s09.a"], C["s09.b"], C["s09.c"]]]
    if t >= C["s07.d"]:
        L[1][2] = "+1,6"
    if t >= C["s08.d"]:
        L[1][0] = L[1][1] = "−0,8"
    if t >= C["s09.a"]:
        L[2] = ["0,2", "0,2", "1,6"]
    dest = 0 if C["s06.b"] <= t < C["s06.c"] else 1 if C["s06.c"] <= t < C["s06.d"] else 2 if C["s06.d"] <= t < C["s07"] else None
    xs, ys = quadro(c, t, C["s06.a"], ESP, L, QX, QY, 260, 130, 64, tl=tl, destaque=dest)
    if not ys:
        return
    if C["s06.e"] <= t < C["s07"]:
        pilula_em(c, t, C["s06.e"], "equilíbrio = início + reage", 1500, 900, 46, E.COR)
    if C["s07.b"] <= t < C["s08"]:
        E.foco(c, t, C["s07.b"], 0.4, lambda a: (E.formula(c, "1,6", xs[2], ys[2], 64, "g", COR, a, "center")))
        E.caixa_pontilhada(c, xs[2] - 90, ys[2] - 70, 180, 90, ep(t, C["s07.b"], 0.4), E.COR)
    if C["s08.b"] <= t < C["s09"]:
        pilula_em(c, t, C["s08.b"], "2 HI gastam 1 H₂ e 1 I₂", 1520, 620, 44, TINTA)
        pilula_em(c, t, C["s08.d"] + 0.4, "1,6 ÷ 2 = 0,8".replace("÷", "/"), 1520, 720, 44, E.COR)
    if C["s08.e"] <= t < C["s09"]:
        pilula_em(c, t, C["s08.e"], "reagente: −   produto: +", 1520, 820, 44, TINTA2)
    if t >= C["s10"]:
        kfrac(c, t, C["s10.a"], "c", "1,6^{2}", "0,2 · 0,2", 1270, 470, 80)
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.formula(c, "= f{2,56}{0,04} =", 1290, 760, 70, "g", TINTA2, a))
        bola_txt(c, t, C["s10.c"], "64", 1760, 738, 76, 62)
        pilula_em(c, t, C["s10.d"], "mesma reação e temperatura: mesmo Kc", 960, 1030, 44, TINTA)


# ---------------- grau de equilíbrio ----------------
def b_grau(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("grau de equilíbrio", "g", 90, COR)], XE, 230)
    E.frase(c, t, C["s11.a"] + 1.2, ps("quanto do reagente reagiu, em porcentagem", "i", 60, TINTA2), XE, 330, passo=0.1)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "α = f{reagiu}{início}", XE, 540, 110, "g", TINTA, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "α = f{0,8}{1} = 0,8", XE, 800, 110, "g", TINTA, a))
    bola_txt(c, t, C["s11.e"], "80%", 1300, 765, 110, 70)
    E.foco(c, t, C["s11.e"] + 0.4, 0.4, lambda a: E.escreve(c, "do H₂ reagiu", 1440, 790, 60, "b", TINTA, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("pôr os reagentes do", "i", 64) + [("início", "g", 60, ERRADO)] + ps("no Kc", "i", 64), XE, 320, passo=0.1)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "f{1,6^2}{1 · 1} = 2,56", XE, 520, 96, "g", ERRADO, a))
    if t >= C["s12.c"] + 0.4:
        E.risco(c, XE - 10, 560, XE + 820, 420, t, C["s12.c"] + 0.4, largura=10)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.escreve(c, "não é 64", XE + 900, 510, 60, "g", ERRADO, a))
    pilula_em(c, t, C["s12.d"], "o Kc só aceita a linha do equilíbrio", W / 2, 800, 60, E.COR)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho", "i", 72, CLARO), W / 2, 170, "center", 0.12)
    E.frase(c, t, C["s13.a"], ps("achou um número do", "i", 66, CLARO) + [("reage,", "g", 62, BR)] + ps("achou todos", "i", 66, CLARO), W / 2, 320, "center", 0.1)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "HI formado: 1,6   →   H₂ e I₂ gastos: 1,6 / 2 = 0,8", W / 2, 500, 64, "g", E.CLARO, a, "center"))
    E.frase(c, t, C["s13.c"], ps("deu mols e o volume?", "i", 66, CLARO), W / 2, 700, "center", 0.1)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "divida pelo volume antes: mol/L", W / 2, 860, 76, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "frasco de 2 L, início: 2 mol de N₂O₄", XE, 330, 66, "g", TINTA, a))
    Q.formula_em(c, t, C["s14.b"], EQN, XE, 480, 90, cores={"coef": E.COR})
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "no equilíbrio: 0,8 mol de NO₂", XE, 630, 66, "g", TINTA, a))
    E.frase(c, t, C["s14.d"], ps("calcule o", "i", 66) + [("Kc", "g", 62, COR), ("e", "i", 66), ("o grau de equilíbrio", "g", 62, COR)], XE, 800, passo=0.1)
    relogio(c, t, C["s15.a"], 1560, 560, 120)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.escreve(c, "divida pelo volume", XE, 150, 56, "b", COR, a))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.formula(c, "N₂O₄: 2 mol / 2 L = 1", XE, 240, 54, "g", TINTA, a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.formula(c, "NO₂: 0,8 mol / 2 L = 0,4", XE + 760, 240, 54, "g", TINTA, a))
    L = [["1", "0"], [None, None], [None, None]]
    if t >= C["s17.a"]:
        L[1][1] = "+0,4"
    if t >= C["s17.b"]:
        L[1][0] = "−0,2"
    if t >= C["s17.c"]:
        L[2] = ["0,8", "0,4"]
    xs, ys = quadro(c, t, C["s16.b"], ("N2O4", "NO2"), L, XE, 400, 260, 120, 60, tl=[[C["s16.b"], C["s16.c"]], [C["s17.b"], C["s17.a"]], [C["s17.c"]] * 2])
    kfrac(c, t, C["s18.a"], "c", "0,4^{2}", "0,8", 1180, 480, 80)
    E.foco(c, t, C["s18.a"] + 0.4, 0.4, lambda a: E.formula(c, "= f{0,16}{0,8} =", 1180, 720, 66, "g", TINTA2, a))
    bola_txt(c, t, C["s18.c"], "0,2", 1640, 695, 70, 56)
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.formula(c, "α = f{0,2}{1} = 0,2 =", 1000, 960, 66, "g", TINTA, a, "right"))
    bola_txt(c, t, C["s18.e"], "20%", 1110, 935, 76, 54)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for k, (tt, s) in enumerate(((C["s19.a"], "monte início, reage e equilíbrio"), (C["s19.b"], "o reage segue os coeficientes"),
                                     (C["s19.c"], "no Kc, só a linha do equilíbrio"))):
            y = 380 + k * 180
            E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 80, y - 26, 44, a=a), centro(c, str(k + 1), XE + 80, y - 4, 54, "g", E.SOBRE, a)))
            E.foco(c, t, tt + 0.1, 0.5, lambda a, y=y, s=s, k=k: E.escreve(c, s, XE + 160, y, 72, "g", COR if k == 2 else TINTA, a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20", [("princípio", "g", 100, COR), ("de", "i", 100), ("Le Chatelier", "g", 100, COR)],
            (C["s20.b"], "concentração, pressão e temperatura"), "s20.d", "s20.e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, direto=b_direto, quadro=b_quadro, grau=b_grau, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
