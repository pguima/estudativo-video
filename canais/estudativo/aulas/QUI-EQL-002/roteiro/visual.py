"""Visual — Estudativo · QUI-EQL-002: princípio de Le Chatelier.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha Equilíbrio Químico (QUI-EQL-001). Nesta aula: a equação fica no
alto e o DESLOCAMENTO é uma seta larga embaixo dela (desloca), turquesa para a direita (mais produto) e cinza para a esquerda (mais
reagente), com a pílula do que aumenta. A PERTURBAÇÃO entra como pílula âmbar ("+ N₂", "pressão ↑", "esquentou").
Calor como substância = a palavra "calor" na equação, do lado indicado pelo sinal do ΔH (azul < 0, âmbar > 0, como na TER-001).
Peça candidata ao kit: desloca (seta de deslocamento do equilíbrio).
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
ARQUIVO_FINAL = "estudativo_QUI-EQL-002_principio_le_chatelier.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("principio", "concentracao", "pressao", "temperatura", "catalisador", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR = Q.ELETRON, "#E8A317"

EQ = "N2(g) + 3 H2(g) <=> 2 NH3(g)"
EQS = "2 SO2(g) + O2(g) <=> 2 SO3(g)"
assert Q.lados("N2 + 3 H2 -> 2 NH3")[0] == Q.lados("N2 + 3 H2 -> 2 NH3")[1] and 1 + 3 == 4
assert Q.lados("2 SO2 + O2 -> 2 SO3")[0] == Q.lados("2 SO2 + O2 -> 2 SO3")[1] and 2 + 1 == 3


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


def desloca(c, t, t0, cx, y, sentido, rot=None, w=520, escuro=False):
    """seta larga de deslocamento: sentido +1 direita (turquesa), −1 esquerda (cinza), 0 = não desloca (×)"""
    if t < t0:
        return
    p = ease_out(prog(t, t0, 0.6))
    if sentido == 0:
        E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, "não desloca", cx, y, 52, "g", fundo=TINTA2, a=a))
        return
    cor = E.COR if sentido > 0 else CINZA
    x0, x1 = cx - sentido * w / 2, cx + sentido * w / 2
    F.seta(c, x0, y, lerp(x0, x1, p), y, cor, 1, 22, 50)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot, cx, y + 90, 50, "g", COR if sentido > 0 else TINTA2, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a amônia dos fertilizantes vem de um equilíbrio", "i", 60), XE, 220, passo=0.08)
        Q.formula_em(c, t, C["s01.a"] + 1.2, EQ, W / 2, 400, 96, align="center")
        Q.molecula(c, t, C["s01.a"] + 1.6, "NH3", 1600, 620, 110)
        E.frase(c, t, C["s01.b"], ps("nas condições erradas,", "i", 64) + [("quase nada", "g", 60, ERRADO)], XE, 600, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("a fábrica mexe em", "i", 64) + [("pressão", "g", 60, AMBAR), ("e", "i", 64), ("temperatura", "g", 60, AMBAR)], XE, 760, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("como saber o", "i", 70) + [("lado?", "g", 66, COR)], XE, 920, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    abertura(c, t, C, [("Le", "g", 100, COR), ("Chatelier", "g", 100, COR)],
             [(C["s02.a"], [("prever", "i", 74), ("o", "i", 74), ("lado", "g", 70)]),
              (C["s02.b"], [("concentração,", "g", 62), ("pressão,", "g", 62), ("temperatura", "g", 62)]),
              (C["s02.c"], [("o", "i", 74), ("catalisador", "g", 70), ("não", "i", 74), ("desloca", "g", 70, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você já sabe", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "equilíbrio: v ida = v volta", XE, 400, 90, "g", TINTA, a))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.formula(c, "ΔH < 0", XE, 600, 90, "g", AZUL, a), E.escreve(c, "libera calor", XE + 380, 595, 64, "i", TINTA2, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.escreve(c, "catalisador: abaixa a energia de ativação", XE, 800, 66, "g", COR, a))


# ---------------- o princípio ----------------
def b_principio(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("princípio de Le Chatelier", "g", 84, COR)], XE, 210)
    E.frase(c, t, C["s04.b"], ps("perturbou o equilíbrio? ele se desloca", "i", 64), XE, 340, passo=0.1)
    E.frase(c, t, C["s04.b"] + 2.0, ps("para", "i", 64) + [("diminuir a perturbação", "g", 60)], XE, 430, passo=0.1)
    pilula_em(c, t, C["s04.c"], "o equilíbrio foge da mudança", W / 2, 560, 60, E.COR)
    Q.formula_em(c, t, C["s04.d"] - 0.4, "reagentes <=> produtos", W / 2, 760, 84, align="center")
    desloca(c, t, C["s04.d"], 1280, 880, +1, "mais produto", 360)
    desloca(c, t, C["s04.e"], 640, 880, -1, "mais reagente", 360)


# ---------------- concentração ----------------
def b_concentracao(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("1", "g", 70, COR), ("concentração", "g", 76)], XE, 160, passo=0.12)
    Q.formula_em(c, t, C["s05"], EQ, W / 2, 330, 96, align="center")
    if C["s05.b"] <= t < C["s05.e"]:
        pilula_em(c, t, C["s05.b"], "+ N₂", 520, 200, 56, AMBAR)
        desloca(c, t, C["s05.c"], W / 2, 500, +1, "consome o N₂ e forma mais NH₃")
    if C["s05.e"] <= t < C["s06"]:
        pilula_em(c, t, C["s05.e"], "− NH₃", 1500, 200, 56, AMBAR)
        desloca(c, t, C["s05.f"], W / 2, 500, +1, "repõe a NH₃: também para a direita")
    if t >= C["s06"]:
        E.frase(c, t, C["s06.a"], [("adicionou:", "g", 66), ("vai para o", "i", 70), ("lado oposto", "g", 66, COR)], XE, 680, passo=0.12)
        E.frase(c, t, C["s06.b"], [("retirou:", "g", 66), ("vai para o", "i", 70), ("lado dela", "g", 66, COR)], XE, 800, passo=0.12)
        pilula_em(c, t, C["s06.b"] + 1.5, "sólido e líquido puro não contam: estão fora do Kc", W / 2, 960, 44, TINTA2)


# ---------------- pressão ----------------
def b_pressao(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("2", "g", 70, COR), ("pressão", "g", 76)] + ps("(só gases)", "i", 66, TINTA2), XE, 160, passo=0.12)
    Q.formula_em(c, t, C["s07"], EQ, W / 2, 330, 96, align="center", cores={"coef": E.COR} if t >= C["s07.b"] else None)
    sp = Q.centros(EQ, W / 2, 330, 96, "center")
    E.foco(c, t, C["s07.c"], 0.4, lambda a: (E.chave(c, sp[0] - 120, sp[1] + 140, 380, TINTA2, a, 24), centro(c, "1 + 3 = 4", (sp[0] + sp[1]) / 2, 460, 54, "g", TINTA, a)))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: (E.chave(c, sp[2] - 150, sp[2] + 150, 380, TINTA2, a, 24), centro(c, "2", sp[2], 460, 54, "g", COR, a)))
    if t >= C["s08"]:
        k = 1 - 0.4 * ep(t, C["s08.a"], 1.0)
        x0 = 220
        M.rrect(c, x0, 560, 480 * k, 380, 20, "#FFFFFF", 1, shadow=True)
        Q.particulas(c, t, x0 + 12, 572, 480 * k - 24, 356, 22, "gas", tipos=[("N", 0.25), ("H", 0.75)], r=12, semente=4)
        if t >= C["s08.a"]:
            F.seta(c, x0 + 640, 750, x0 + 480 * k + 30, 750, AMBAR, ep(t, C["s08.a"], 0.4), 12, 32)
            pilula_em(c, t, C["s08.a"], "pressão ↑", x0 + 640, 660, 46, AMBAR)
        desloca(c, t, C["s08.b"], 1450, 620, +1, "menos gás: mais NH₃", 420)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, "pressão ↓: o contrário", 1100, 860, 50, "b", TINTA2, a))
        E.foco(c, t, C["s08.e"], 0.4, lambda a: E.escreve(c, "mesmo número de gás: não desloca", 1100, 960, 46, "b", TINTA, a))


# ---------------- temperatura ----------------
def b_temperatura(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("3", "g", 70, COR), ("temperatura", "g", 76)], XE, 160, passo=0.12)
    Q.formula_em(c, t, C["s09"], EQ, W / 2, 330, 96, align="center")
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.formula(c, "ΔH = −92 kJ", W / 2, 450, 64, "g", AZUL, a, "center"))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "ida: libera calor", 380, 580, 54, "b", AZUL, a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "volta: absorve calor", 1180, 580, 54, "b", AMBAR, a))
    if C["s09.e"] <= t < C["s09.g"]:
        pilula_em(c, t, C["s09.e"], "esquentou", 300, 720, 50, AMBAR)
        desloca(c, t, C["s09.e"] + 0.6, W / 2, 740, -1, "favorece a volta: menos NH₃")
    if C["s09.g"] <= t < C["s10"]:
        pilula_em(c, t, C["s09.g"], "esfriou", 300, 720, 50, AZUL)
        desloca(c, t, C["s09.g"] + 0.3, W / 2, 740, +1, "favorece a ida: mais NH₃")
    if t >= C["s10"]:
        pilula_em(c, t, C["s10.a"], "só a temperatura muda o valor do Kc", W / 2, 760, 56, E.COR)
        E.frase(c, t, C["s10.b"], ps("as outras perturbações: o equilíbrio anda e volta ao mesmo Kc", "i", 54, TINTA2), W / 2, 900, "center", 0.08)


# ---------------- catalisador ----------------
def b_catalisador(c, t, C, b):
    E.frase(c, t, C["s11.a"], ps("e o", "i", 80) + [("catalisador?", "g", 76, COR)], XE, 200, passo=0.12)
    Y = Q.energia(c, t, C["s11.b"] - 0.4, 260, 300, 820, 480, er=60, ep_=30, pico=110, cat=80 if t >= C["s11.b"] else None, sinal=False)
    E.frase(c, t, C["s11.b"] + 0.5, ps("baixa a", "i", 60) + [("ida e a volta", "g", 56, COR)], 1220, 420, passo=0.1)
    E.frase(c, t, C["s11.c"], ps("as duas aceleram juntas", "i", 60), 1220, 520, passo=0.1)
    E.frase(c, t, C["s11.d"], ps("chega", "i", 60) + [("mais cedo", "g", 56, COR)], 1220, 620, passo=0.1)
    E.frase(c, t, C["s11.e"], ps("ao", "i", 60) + [("mesmo lugar", "g", 56)], 1220, 720, passo=0.1)
    desloca(c, t, C["s11.e"] + 0.8, W / 2, 940, 0)


# ---------------- a fábrica ----------------
def b_haber(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("na fábrica", "i", 80, TINTA2), XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s12.a"], EQ, W / 2, 340, 90, align="center")
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "pressão alta", XE, 520, 70, "g", TINTA, a), E.formula(c, "≈ 200 atm", XE + 600, 520, 70, "g", COR, a)))
    E.foco(c, t, C["s12.b"] + 0.5, 0.4, lambda a: E.escreve(c, "empurra para a amônia", XE + 1000, 515, 50, "i", TINTA2, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.escreve(c, "temperatura baixa: empurraria, mas fica lenta demais", XE, 660, 54, "b", TINTA2, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: (E.escreve(c, "meio-termo", XE, 820, 70, "g", TINTA, a), E.formula(c, "≈ 450 °C", XE + 600, 820, 70, "g", AMBAR, a)))
    pilula_em(c, t, C["s12.e"], "catalisador de ferro para compensar a lentidão", W / 2, 970, 48, E.COR)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s13.a"], ps("“o catalisador aumenta a quantidade de produto”", "i", 60, ERRADO), XE, 360, passo=0.08)
    if t >= C["s13.b"]:
        E.risco(c, XE - 10, 375, XE + 1250, 315, t, C["s13.b"], largura=9)
    E.frase(c, t, C["s13.b"], ps("só faz o equilíbrio", "i", 66) + [("chegar mais rápido", "g", 62, COR)], XE, 520, passo=0.1)
    for k, (cor, tt) in enumerate(((TINTA2, 3.0), (E.COR, 1.2))):
        y = 700 + k * 150
        p = ease_out(prog(t, C["s13.b"] + 0.5, tt))
        M.rrect(c, 520, y - 50, 900 * p, 70, 14, cor, 1)
        E.foco(c, t, C["s13.b"] + 0.5, 0.4, lambda a, k=k, y=y: E.escreve(c, ("sem", "com")[k], XE, y, 54, "g", TINTA, a))
    E.frase(c, t, C["s13.c"], ps("o equilíbrio não fica com mais amônia", "i", 58, TINTA2), XE, 1000, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14.a"], ps("o atalho:", "i", 72, CLARO) + [("calor é uma substância", "g", 66, BR)], W / 2, 180, "center", 0.12)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: Q.formula(c, "N2 + 3 H2 <=> 2 NH3 + calor", W / 2, 400, 96, BR, a, "center", escuro=True))
    if t >= C["s14.c"]:
        pilula_em(c, t, C["s14.c"], "esquentar = adicionar calor", W / 2, 540, 54, AMBAR)
        desloca(c, t, C["s14.d"], W / 2, 680, -1, None)
        E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: centro(c, "foge do calor: esquerda", W / 2, 780, 56, "g", CLARO, a))
    E.frase(c, t, C["s14.e"], ps("temperatura vira a regra da concentração", "i", 60, CLARO), W / 2, 900, "center", 0.1)
    pilula_em(c, t, C["s14.f"], "precisa do sinal do ΔH", W / 2, 1010, 46, TINTA2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 160)
    Q.formula_em(c, t, C["s15.a"], EQS, XE, 330, 86)
    E.foco(c, t, C["s15.a"] + 0.6, 0.4, lambda a: E.formula(c, "ΔH < 0", XE + 1150, 330, 70, "g", AZUL, a))
    for k, (tt, s) in enumerate(((C["s15.b"], "adicionar O₂"), (C["s15.c"], "aumentar a pressão"), (C["s15.d"], "esquentar"), (C["s15.e"], "pôr catalisador"))):
        y = 500 + k * 120
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k, s=s: (E.bola(c, XE + 36, y - 22, 36, a=a), centro(c, "abcd"[k], XE + 36, y - 6, 44, "g", E.SOBRE, a),
                                                        E.escreve(c, s, XE + 100, y, 60, "b", TINTA, a)))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.escreve(c, "o que acontece com o SO₃?", XE + 760, 470, 48, "b", TINTA2, a))
    relogio(c, t, C["s16.a"], 1500, 760, 110)


def b_resposta(c, t, C, b):
    Q.formula(c, EQS, W / 2, 200, 86, align="center", cores={"coef": E.COR} if C["s17.b"] <= t < C["s18"] else None)
    linhas = ((C["s17.a"], "a  adicionar O₂", +1, "consome o O₂: mais SO₃"), (C["s17.b"], "b  pressão ↑", +1, "3 gases → 2: mais SO₃"),
              (C["s18.a"], "c  esquentar", -1, "favorece a volta: menos SO₃"), (C["s18.c"], "d  catalisador", 0, "fica igual, só chega antes"))
    for k, (tt, s, sn, rot) in enumerate(linhas):
        y = 360 + k * 175
        E.foco(c, t, tt, 0.4, lambda a, y=y, s=s: E.escreve(c, s, XE, y, 62, "g", TINTA, a))
        if t >= tt + 0.3:
            if sn:
                F.seta(c, 820 - sn * 110, y - 22, 820 - sn * 110 + sn * 220 * ease_out(prog(t, tt + 0.3, 0.5)), y - 22, E.COR if sn > 0 else CINZA, 1, 14, 36)
            else:
                E.foco(c, t, tt + 0.3, 0.4, lambda a, y=y: E.formula(c, "=", 820, y, 70, "g", TINTA2, a, "center"))
        E.foco(c, t, tt + 0.5, 0.4, lambda a, y=y, rot=rot, sn=sn: E.escreve(c, rot, 1000, y, 50, "b", COR if sn > 0 else TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        pilula_em(c, t, C["s19.a"], "o equilíbrio foge da perturbação", W / 2, 330, 60, E.COR)
        for k, (tt, s) in enumerate(((C["s19.b"], "concentração e pressão: deslocam"), (C["s19.c"], "temperatura: desloca e muda o Kc"),
                                     (C["s19.d"], "catalisador: não desloca"))):
            E.foco(c, t, tt, 0.5, lambda a, k=k, s=s: centro(c, s, W / 2, 520 + k * 150, 70, "g", TINTA if k < 2 else TINTA2, a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20", [("pH", "g", 120, COR), ("e", "i", 120), ("pOH", "g", 120, COR)], (C["s20.b"], "o equilíbrio da própria água"), "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, principio=b_principio, concentracao=b_concentracao, pressao=b_pressao,
              temperatura=b_temperatura, catalisador=b_catalisador, haber=b_haber, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
