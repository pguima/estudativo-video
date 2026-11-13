"""Visual — Estudativo · QUI-EQL-004: ácidos fracos, Ka e grau de ionização.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha Equilíbrio (QUI-EQL-001) e do módulo pH (QUI-EQL-003): H⁺ em bolinha
turquesa, A⁻ em bolinha cinza-escura, a molécula inteira HA em tinta; Ka em fração (kfrac). Nesta aula: o GRAU DE IONIZAÇÃO é
uma fileira de 100 moléculas (cem) em que só as ionizadas ganham cor; a lei de Ostwald fica numa caixa pontilhada.
Peça candidata ao kit: cem (fileira de 100 partículas com as k primeiras destacadas).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-004_acidos_fracos_ka_alfa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("grau", "ka", "ostwald", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL = Q.ELETRON

# as contas da aula
assert abs(0.1 * 0.01 - 0.001) < 1e-15 and -math.log10(0.001) == 3
assert abs(1e-5 / 1e-1 - 1e-4) < 1e-18 and abs(math.sqrt(1e-4) - 1e-2) < 1e-15 and abs(1e-1 * 1e-2 - 1e-3) < 1e-15
assert abs(math.sqrt(1e-5 * 1e-1) - 1e-3) < 1e-15
assert abs(1e-6 / 1e-2 - 1e-4) < 1e-18 and abs(math.sqrt(1e-6 * 1e-2) - 1e-4) < 1e-15


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


def cem(c, t, t0, x, y, w, k, tk=None, r=14):
    """100 moléculas em 5 fileiras; as k primeiras ionizadas (turquesa) a partir de tk"""
    for i in range(100):
        q = ep(t, t0 + i * 0.006, 0.3)
        if q <= 0:
            continue
        px, py = x + (i % 20) * w / 19, y + (i // 20) * (r * 3)
        ioniz = i < k and tk is not None and t >= tk
        c.drawCircle(px, py, r, M.paint(E.COR if ioniz else "#3A3B40", q))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("mesma concentração:", "i", 64), XE, 220, passo=0.1)
        E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: E.formula(c, "0,1 mol/L", XE + 620, 225, 70, "g", TINTA, a))
        for k, (tt, nome, f, ph, x) in enumerate(((C["s01.c"], "clorídrico", "HCl", "pH 1", 520), (C["s01.d"], "acético", "CH3COOH", "pH ≈ 3", 1360))):
            E.foco(c, t, C["s01.b"] + 0.3 * k, 0.4, lambda a, nome=nome, f=f, x=x: (centro(c, nome, x, 420, 60, "i", TINTA2, a), Q.formula(c, f, x, 540, 90, TINTA, a, "center")))
            bola_txt(c, t, tt, ph, x, 760, 120, 60, E.COR if k == 0 else E.mix(E.COR, "#FFFFFF", 0.35))
        E.frase(c, t, C["s01.d"] + 1.0, [("por quê?", "g", 70, COR)], W / 2, 1000, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("ácidos", "g", 110, COR), ("fracos", "g", 110)],
             [(C["s02.a"], [("o", "i", 74), ("Ka", "g", 70, COR)]), (C["s02.b"], [("o", "i", 74), ("grau", "g", 70), ("de", "i", 74), ("ionização", "g", 70)]),
              (C["s02.c"], [("o", "i", 74), ("pH", "g", 70), ("de", "i", 74), ("um", "i", 74), ("ácido", "g", 70), ("fraco", "g", 70, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "[H⁺] = 10^{−3}  →  pH 3", XE, 380, 86, "g", TINTA, a))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: E.escreve(c, "ácido fraco: ioniza pouco", XE, 540, 70, "g", COR, a))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "1% = 0,01", XE, 700, 86, "g", TINTA, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "r{10^{−4}} = 10^{−2}", XE + 700, 700, 86, "g", TINTA, a))


# ---------------- grau de ionização ----------------
def b_grau(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("forte:", "g", 66), ("ioniza tudo", "i", 70)], XE, 200, passo=0.1)
        E.frase(c, t, C["s04.b"], [("fraco:", "g", 66, COR), ("só uma parte", "i", 70)], XE + 760, 200, passo=0.1)
        cem(c, t, C["s04.b"], 320, 360, 1280, 1, tk=C["s04.e"])
        E.frase(c, t, C["s04.c"], [("grau de ionização", "g", 80, COR)], XE, 680)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.formula(c, "α = f{ionizadas}{dissolvidas}", XE, 860, 90, "g", TINTA, a))
        E.foco(c, t, C["s04.e"], 0.5, lambda a: E.formula(c, "1 de 100: α = 1%", 1150, 860, 80, "g", COR, a))
        return
    E.frase(c, t, C["s05.a"], ps("com o grau, sai o", "i", 70) + [("H⁺", "g", 66, COR)], XE, 200, passo=0.12)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "[H⁺] = M · α", XE, 380, 120, "g", TINTA, a))
    E.foco(c, t, C["s05.b"] + 0.6, 0.4, lambda a: E.escreve(c, "M = concentração do ácido", XE + 700, 370, 54, "b", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.escreve(c, "ácido acético 0,1 mol/L, α ≈ 1%", XE, 560, 64, "b", TINTA, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "0,1 · 0,01 = 0,001", XE, 720, 90, "g", TINTA2, a))
    E.foco(c, t, C["s05.f"], 0.5, lambda a: E.formula(c, "= 10^{−3}", XE + 900, 720, 90, "g", COR, a))
    bola_txt(c, t, C["s05.f"] + 0.4, "pH 3", 1600, 690, 100, 54)


# ---------------- Ka ----------------
def b_ka(c, t, C, b):
    E.frase(c, t, C["s06.a"], ps("é um equilíbrio: tem constante, o", "i", 64) + [("Ka", "g", 60, COR)], XE, 190, passo=0.1)
    Q.formula_em(c, t, C["s06.b"], "HA(aq) <=> H^+(aq) + A^-(aq)", W / 2, 340, 96, align="center")
    E.foco(c, t, C["s06.c"], 0.4, lambda a: (ion(c, 1200, 470, 44, "H^+", E.COR, a), ion(c, 1440, 470, 44, "A^-", "#3A3B40", a)))
    kfrac(c, t, C["s06.d"], "a", "[H^+] · [A^-]", "[HA]", XE, 640, 110)
    pilula_em(c, t, C["s06.e"], "na mesma concentração: Ka maior, ácido mais forte", W / 2, 860, 46, E.COR)
    if t >= C["s07"]:
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "A⁻ = a base conjugada", 1150, 640, 60, "g", TINTA, a))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.escreve(c, "o que sobra depois de soltar o H⁺", 1150, 720, 46, "b", TINTA2, a))


# ---------------- Ostwald ----------------
def b_ostwald(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("ligando Ka e o grau", "i", 66) + [("α", "g", 62, COR)], XE, 190, passo=0.1)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "ácido: M", XE, 340, 70, "g", TINTA, a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.formula(c, "[H⁺] = [A⁻] = M · α", XE, 470, 70, "g", TINTA, a))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.formula(c, "[HA] ≈ M  (α pequeno)", XE, 600, 70, "g", TINTA2, a))
        q = ep(t, C["s08.e"], 0.5)
        if q > 0:
            E.caixa_pontilhada(c, XE - 30, 690, 920, 200, q, E.COR, prog_=q)
        E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "Ka ≈ α^2 · M", XE + 40, 830, 120, "g", COR, a))
        E.foco(c, t, C["s08.e"] + 1.2, 0.4, lambda a: E.escreve(c, "lei de Ostwald", XE + 960, 820, 60, "i", TINTA2, a))
        return
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.formula(c, "Ka = 10^{−5},  M = 0,1 = 10^{−1}", XE, 220, 80, "g", TINTA, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "α^2 = f{Ka}{M}", XE, 400, 90, "g", TINTA, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "= f{10^{−5}}{10^{−1}} = 10^{−4}", XE + 420, 400, 90, "g", TINTA, a))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "α = r{10^{−4}} = 10^{−2} = 1%", XE, 590, 90, "g", COR, a))
    if t >= C["s10"]:
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "[H⁺] = M · α = 10^{−1} · 10^{−2}", XE, 780, 84, "g", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "= 10^{−3}", XE + 1150, 780, 84, "g", COR, a))
        bola_txt(c, t, C["s10.d"], "pH 3", 1000, 950, 90, 50)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("tratar o ácido fraco como", "i", 66) + [("forte", "g", 62, ERRADO)], XE, 320, passo=0.1)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "[H⁺] = 10^{−1}  →  pH 1", XE, 500, 96, "g", ERRADO, a))
    if t >= C["s11.c"]:
        E.risco(c, XE - 10, 520, XE + 1000, 420, t, C["s11.c"], largura=10)
    cem(c, t, C["s11.c"], 320, 620, 1280, 1, tk=C["s11.c"] + 0.5)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "só 1%: [H⁺] 100 vezes menor  →  pH 3", XE, 900, 76, "g", COR, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("o atalho", "i", 72, CLARO), W / 2, 160, "center", 0.12)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "[H⁺] = r{Ka · M}", W / 2, 340, 130, "g", BR, a, "center"))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "10^{−5} · 10^{−1} = 10^{−6}", W / 2, 540, 86, "g", BR, a, "center"))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "r{10^{−6}} = 10^{−3}", W / 2, 690, 86, "g", E.CLARO, a, "center"))
    pilula_em(c, t, C["s12.d"], "expoente par: divida por 2", W / 2, 810, 50, E.COR)
    if t >= C["s13"]:
        E.frase(c, t, C["s13.a"], ps("porque [H⁺] = α · M e α² = Ka / M", "b", 50, CLARO), W / 2, 920, "center", 0.08)
        pilula_em(c, t, C["s13.b"], "só para ácido fraco, α até uns 5%", W / 2, 1020, 44, TINTA2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "ácido fraco: M = 0,01 = 10^{−2} mol/L", XE, 360, 76, "g", TINTA, a))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "Ka = 10^{−6}", XE, 500, 90, "g", TINTA, a))
    E.frase(c, t, C["s14.c"], [("1", "g", 60, COR), ("grau de ionização?", "g", 62)], XE, 680, passo=0.1)
    E.frase(c, t, C["s14.d"], [("2", "g", 60, COR), ("pH?", "g", 62)], XE, 800, passo=0.1)
    relogio(c, t, C["s15.a"], 1450, 640, 130)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "α^2 = f{10^{−6}}{10^{−2}}", XE, 260, 90, "g", TINTA, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "= 10^{−4}", XE + 560, 260, 90, "g", TINTA, a))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.formula(c, "α = 10^{−2}", XE, 440, 90, "g", TINTA, a))
    bola_txt(c, t, C["s16.c"] + 0.4, "1%", 820, 410, 80, 56)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: E.formula(c, "[H⁺] = r{10^{−6} · 10^{−2}}", XE, 660, 90, "g", TINTA, a))
    E.foco(c, t, C["s16.e"], 0.5, lambda a: E.formula(c, "= r{10^{−8}}", XE + 820, 660, 90, "g", TINTA2, a))
    E.foco(c, t, C["s16.f"], 0.5, lambda a: E.formula(c, "= 10^{−4}", XE + 1250, 660, 90, "g", COR, a))
    bola_txt(c, t, C["s16.g"], "pH 4", 1000, 880, 110, 58)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s17.a"], ps("o ácido fraco se ioniza", "i", 74) + [("pouco", "g", 70, COR)], W / 2, 360, "center", 0.12)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "[H⁺] = M · α", W / 2, 560, 110, "g", TINTA, a, "center"))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "Ka ≈ α^2 · M", W / 2, 760, 110, "g", COR, a, "center"))
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    proxima(c, t, C, "s18", [("hidrólise", "g", 110, COR), ("salina", "g", 110)], (C["s18.b"], "a regra do forte vence"), "s18.c", "s18.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grau=b_grau, ka=b_ka, ostwald=b_ostwald, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
