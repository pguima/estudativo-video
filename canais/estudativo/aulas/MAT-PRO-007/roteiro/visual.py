"""Visual — Estudativo · MAT-PRO-007: praticando sequências e PA (quatro situações).

Linguagem visual da trilha Progressões (MAT-PRO-001, 002 e 004): fila de caixas de borda índigo com o termo dentro (preto) e a posição
embaixo (índigo); a razão é o arco verde por cima; índice como índice (aₙ, letra preta e índice índigo) com fx(); palitos grossos de
pontas redondas com os palitos NOVOS de cada figura na cor da matéria (palito() da MAT-PRO-002); atalho no palco escuro.
Nesta aula: triângulos de palitos (triangulos()); a semana como fila de sete caixas com a casa do bloco embaixo e o resto andando;
as 12 parcelas em colunas (E.colunas) com a linha da média 210 no atalho; a estrada com os postos de água sobre E.reta (poste()).
Cada situação: pergunta, relógio de pausa (E.relogio) e resposta.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da MAT-PRO-004), palito(), triangulos(), poste()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-007_praticando_sequencias_e_pa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"

PARC = [100 + 20 * i for i in range(12)]
POSTOS = list(range(3, 40, 4))
assert [2 * n + 1 for n in (1, 2, 3)] == [3, 5, 7] and 2 * 30 + 1 == 61 and 2 * 10 + 1 == 21 and sum(2 * n + 1 for n in range(1, 11)) == 120
assert divmod(200, 7) == (28, 4) and PARC[-1] == 320 == 100 + 11 * 20 and sum(PARC) == 2520 == 420 * 6 == 210 * 12
assert len(POSTOS) == 10 == (39 - 3) // 4 + 1 and POSTOS[5] == 23 == 3 + 5 * 4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _pedacos(s):
    """separa "a_{20} = 5" em [(0, "a"), (1, "20"), (0, " = 5")]: 1 = índice"""
    out, buf, i = [], "", 0
    while i < len(s):
        if s[i] == "_":
            if buf:
                out.append((0, buf))
                buf = ""
            if s[i + 1] == "{":
                j = s.index("}", i)
                out.append((1, s[i + 2:j]))
                i = j + 1
            else:
                out.append((1, s[i + 1]))
                i += 2
        else:
            buf += s[i]
            i += 1
    if buf:
        out.append((0, buf))
    return out


def _w(s, size, est):
    return sum(E.formula(None, p, 0, 0, size * (0.6 if k else 1), est, a=0) + (size * 0.03 if k else 0) for k, p in _pedacos(s))


def fx(c, partes, x, y, size, a=1.0, align="left", est="g", cor=None):
    """fórmula com índice de verdade (a_n, a_1, a_{20}); partes = texto ou [(texto, cor)]. Devolve [(x0, largura)] de cada parte.
    Como na MAT-PRO-001: em pedaço preto (SAI), a letra fica preta e o índice (a posição) sai em índigo"""
    if isinstance(partes, str):
        partes = [(partes, cor or TINTA)]
    ws = [_w(s, size, est) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    out = []
    for (s, cr), w in zip(partes, ws):
        out.append((xx, w))
        if a > 0:
            px = xx
            for k, p in _pedacos(s):
                sz = size * (0.6 if k else 1)
                E.formula(c, p, px + (size * 0.01 if k else 0), y + (size * 0.2 if k else 0), sz, est, ENT if (k and cr == SAI) else cr, a)
                px += E.formula(None, p, 0, 0, sz, est, a=0) + (size * 0.03 if k else 0)
        xx += w
    return out


def fx_em(c, t, t0, partes, x, y, size, align="left", est="g", cor=None):
    E.foco(c, t, t0, 0.5, lambda a: fx(c, partes, x, y, size, a, align, est, cor))
    return fx(c, partes, x, y, size, 0, align, est, cor)


def caixa(c, cx, cy, w, h, val, a=1.0, pos=None, size=80, cor=None, borda=None, escuro=False, pos_size=44):
    """um termo: caixa de borda índigo com o valor dentro (preto) e a posição embaixo (índigo), como casa() da MAT-PRO-001"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 20, 20)
    c.drawRRect(rr, M.paint("#1A1830" if escuro else "#FFFFFF", a))
    c.drawRRect(rr, M.paint(borda or (CLARO if escuro else COR), a, stroke=5))
    if val is not None and val != "":
        fx(c, [(str(val), cor or (BR if escuro else SAI))], cx, cy + size * 0.36, size, a, "center")
    if pos:
        centro(c, pos, cx, cy + h / 2 + pos_size + 14, pos_size, "b", CLARO if escuro else ENT, a)


def fila(c, t, itens, cy, w=190, h=150, size=80, escuro=False, pos_size=44):
    """itens = [(cx, valor, posição, t0[, cor[, borda]])]; valor "…" = reticências sem caixa"""
    for it in itens:
        cx, val, pos, t0 = it[:4]
        cor = it[4] if len(it) > 4 else None
        borda = it[5] if len(it) > 5 else None
        if val == "…":
            E.foco(c, t, t0, 0.5, lambda a, cx=cx: centro(c, "…", cx, cy + 20, 90, "g", BR if escuro else TINTA2, a))
        else:
            E.foco(c, t, t0, 0.5, lambda a, cx=cx, val=val, pos=pos, cor=cor, borda=borda: caixa(
                c, cx, cy, w, h, val, a, pos, size, cor, borda, escuro, pos_size))


def pula(c, t, t0, x0, x1, ytopo, rot, cor=RAZ, alto=80, size=52):
    """a razão: arco por cima das caixas, de um termo para o seguinte"""
    E.salto(c, t, t0, x0, x1, ytopo - 8, alto, cor, rot, size=size)


def resultado(c, t, t0, s, cx, cy, r=110, cor=None):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k, cor)
        size = r * (0.62 if len(s) <= 3 else 0.5 if len(s) <= 5 else 0.4)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g"):
    """par (posição, termo): posição em índigo, termo em preto"""
    partes = (("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def caixa_em(c, t, t0, x0, w, y, size, cor=None, d=0.5):
    """caixa pontilhada em volta de um trecho já escrito (x0 = início, y = linha de base)"""
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, x0 - 16, y - size * 0.9, w + 32, size * 1.25, p, cor, p)


def eixos_pa(c, t, t0, P, nome_y="a_n"):
    """depois de E.plano: o eixo das posições em índigo e os nomes n (índigo) e aₙ (preto)"""
    x, y, w, h = P.caixa
    if t >= t0:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 22, ep(t, t0, 0.6))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (fx(c, [("n", ENT)], x + w + 30, P.oy + 70, 56, a),
                                          fx(c, [(nome_y, SAI)], P.ox + 24, y - 20, 56, a)))


def palito(c, x0, y0, x1, y1, cor=None, a=1.0, w=10, gap=9):
    """um palito (MAT-PRO-002): segmento grosso de pontas redondas, um pouco mais curto que o lado"""
    if a <= 0 or cor is None:
        return
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1.0
    ux, uy = dx / n, dy / n
    M.line(c, x0 + ux * gap, y0 + uy * gap, x1 - ux * gap, y1 - uy * gap, cor, a, w)


def triangulos(c, x, y, n, L, a=1.0, cor=None, w=10):
    """n triângulos de palitos alternados (ponta para cima, para baixo), encaixados; (x, y) = canto de baixo à esquerda.
    cor(id) → cor; ids: ("d", j) = j-ésima diagonal (n + 1 delas), ("h", k) = palito deitado do triângulo k"""
    cor = cor or (lambda k: TINTA)
    h = L * math.sqrt(3) / 2
    B = lambda i: (x + i * L, y)
    T = lambda i: (x + L / 2 + i * L, y - h)
    for j in range(n + 1):
        p0, p1 = (B(j // 2), T(j // 2)) if j % 2 == 0 else (T((j - 1) // 2), B((j + 1) // 2))
        palito(c, *p0, *p1, cor(("d", j)), a, w)
    for k in range(n):
        p0, p1 = (B(k // 2), B(k // 2 + 1)) if k % 2 == 0 else (T((k - 1) // 2), T((k + 1) // 2))
        palito(c, *p0, *p1, cor(("h", k)), a, w)
    return L * (n + 1) / 2


def larg_tri(n, L):
    return L * (n + 1) / 2


def poste(c, X, y, a=1.0, cor=None, num=None, r=24):
    """posto de água na estrada: haste e gota (esfera) com o número do posto (a posição)"""
    if a <= 0:
        return
    M.line(c, X, y, X, y - 80, TINTA2, a, 6)
    E.bola(c, X, y - 80 - r, r, cor or COR, a)
    if num is not None:
        centro(c, str(num), X, y - 80 - r + 10, 28, "g", BR, a)


def pergunta(c, t, t0, i, partes, y, size=70, x=XE):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i), x + 40, y - 4, 52, "g", BR, a)))
    fx_em(c, t, t0 + 0.1, partes, x + 120, y, size)


def situacao(c, t, t0, n):
    E.frase(c, t, t0, [("situação", "i", 72, COR), (str(n), "g", 72, COR)], XE, 150)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 130, COR), ("situações", "i", 120)], XE, 330)
    E.frase(c, t, C["s01.a"] + 0.8, ps("do dia a dia", "i", 100), XE, 460)
    itens = ("figuras", "calendário", "parcelas", "postos de água")
    for i, s in enumerate(itens):
        E.foco(c, t, C["s01.a"] + 1.4 + 0.25 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 160 + i * 0 + (i % 2) * 380, 610 + (i // 2) * 110, 46, "g",
                                                                                     fundo=COR if i % 2 == 0 else TINTA, a=a))
    E.relogio(c, t, C["s01.b"], 1460, 450, 170)
    E.frase(c, t, C["s01.b"] + 3.4, [("errar", "i", 70), ("aqui", "i", 70), ("ensina", "g", 66, COR)], 1460, 900, "center")


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], [("4", "g", 90, COR), ("ferramentas", "i", 90)], XE, 180)
    itens = (("s02.a", "lei das figuras", [("o aumento vira o nº do ", TINTA), ("n", ENT)]),
             ("s02.b", "padrões que se repetem", [("o resto manda", COR)]),
             ("s02.c", "termo geral da PA", [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" + (", TINTA), ("n", ENT), (" − 1) · ", TINTA), ("r", RAZ)]),
             ("s02.d", "soma da PA", [("(1º + último) · n ÷ 2", TINTA)]))
    for i, (k, l1, l2) in enumerate(itens):
        x, y = 170 + (i % 2) * 820, 280 + (i // 2) * 330
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, 760, 260, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 40, y + 90)
        fx_em(c, t, C[k] + 0.3, l2, x + 40, y + 200, 60)


# ---------------- situação 1: triângulos ----------------
def figuras(c, t, t0, L, y, xs, novos=None, tdiv=None, size=54):
    for n, x in zip((1, 2, 3), xs):
        def cor(k, n=n):
            if novos is not None and t >= novos and n > 1 and k in (("d", n), ("h", n - 1)):
                return COR
            if tdiv is not None and k[0] == "d" and 0 < k[1] < n:
                return mix_(TINTA, COR, E.ep(t, tdiv, 0.4) * (1 - E.ep(t, tdiv + 2.4, 0.4)))
            return TINTA
        E.foco(c, t, t0 + 0.4 * (n - 1), 0.5, lambda a, n=n, x=x, cor=cor: triangulos(c, x - larg_tri(n, L) / 2, y, n, L, a, cor))
        E.foco(c, t, t0 + 0.4 * (n - 1), 0.5, lambda a, n=n, x=x: centro(c, f"figura {n}", x, y + 64, size * 0.8, "b", ENT, a))


def mix_(c1, c2, k):
    return E.mix(c1, c2, max(0.0, min(1.0, k)))


QX1 = (380, 760, 1200)


def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1)
    y = 470
    figuras(c, t, C["s03.a"] + 1.0, 140, y, QX1, tdiv=C["s03.b"])
    for i, (x, v) in enumerate(zip(QX1, (3, 5, 7))):
        E.foco(c, t, C["s03.c"] + 0.46 * i, 0.4, lambda a, x=x, v=v: centro(c, f"{v} palitos", x, y + 150, 60, "g", SAI, a))
    pergunta(c, t, C["s03.d"], 1, [("figura ", TINTA), ("30", ENT), (": quantos palitos?", TINTA)], 800)
    pergunta(c, t, C["s03.e"], 2, [("as ", TINTA), ("10", ENT), (" primeiras, juntas?", TINTA)], 920)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], 1600, 740, 120)


def b_resposta1(c, t, C, b):
    y = 250
    figuras(c, t, C["s05"] - 0.6, 110, y, QX1, novos=C["s05.a"])
    for i, (x, v) in enumerate(zip(QX1, (3, 5, 7))):
        E.foco(c, t, C["s05"] - 0.6, 0.4, lambda a, x=x, v=v: centro(c, str(v), x, 450, 76, "g", SAI, a))
    for i in range(2):
        pula(c, t, C["s05.a"] + 0.3 * i, QX1[i] + 50, QX1[i + 1] - 50, 400, "+2", alto=40, size=46)

    def s05():
        fx_em(c, t, C["s05.b"], [("aumento 2  →  ", TINTA2), ("2", RAZ), ("n", ENT)], XE, 580, 80)
        fx_em(c, t, C["s05.c"], [("P = ", SAI), ("2", RAZ), ("n", ENT), (" + 1", TINTA)], XE, 720, 100)
        E.foco(c, t, C["s05.c"] - 1.6, 0.4, lambda a: E.escreve(c, "figura 1: 2 · 1 = 2, faltou 1", 900, 580, 48, "i", TINTA2, a))
        fx_em(c, t, C["s05.d"], [("2 · ", TINTA), ("30", ENT), (" + 1 = ", TINTA)], XE, 880, 96)
        resultado(c, t, C["s05.d"] + 1.6, "61", XE + E.formula(None, "2 · 30 + 1 = ", 0, 0, 96, "g", a=0) + 100, 845, 90)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"], [("10", "g", 74, ENT), ("primeiras:", "i", 78), ("uma", "i", 78), ("soma", "g", 74, COR)], XE, 580)
    fx_em(c, t, C["s06.b"], [("a_{10}", SAI), (" = 2 · ", TINTA), ("10", ENT), (" + 1 = 21", TINTA)], XE, 720, 84)
    fx_em(c, t, C["s06.c"], "3 + 21 = 24", 1050, 720, 84)
    fx_em(c, t, C["s06.d"], "f{24 · 10}{2} = f{240}{2} = ", XE, 900, 96)
    resultado(c, t, C["s06.d"] + 2.4, "120", XE + E.formula(None, "f{24 · 10}{2} = f{240}{2} = ", 0, 0, 96, "g", a=0) + 110, 865, 95)


# ---------------- situação 2: calendário ----------------
DIAS = ("seg", "ter", "qua", "qui", "sex", "sáb", "dom")
DX = [330 + 210 * i for i in range(7)]


def semana(c, t, t0, cy, pos_t=None, luz=None, w=180, h=120):
    for i, (x, d) in enumerate(zip(DX, DIAS)):
        E.foco(c, t, t0 + 0.06 * i, 0.4, lambda a, x=x, d=d: caixa(c, x, cy, w, h, d, a, None, 60))
        if luz:
            q = luz(i)
            if q > 0:
                M.rrect(c, x - w / 2, cy - h / 2, w, h, 20, COR, 0.2 * q)
        if pos_t is not None:
            E.foco(c, t, pos_t + 0.12 * i, 0.4, lambda a, x=x, i=i: centro(c, str(i + 1), x, cy + h / 2 + 62, 52, "b", ENT, a))


def b_questao2(c, t, C, b):
    situacao(c, t, C["s07.a"], 2)
    cy = 400
    semana(c, t, C["s07.a"] + 0.6, cy)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.pilula(c, "dia 1", DX[0], cy + 120, 46, "g", a=a),))
    pergunta(c, t, C["s07.c"], 1, [("o ", TINTA), ("dia 200", ENT), (" cai em que dia?", TINTA)], 760, 70)
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], 1600, 740, 120)


def b_resposta2(c, t, C, b):
    cy = 300
    luz = lambda i: ep(t, C["s09.d"] + 0.5 * i, 0.3) if i < 4 else 0
    semana(c, t, C["s09"] - 0.4, cy, C["s09.a"], luz)
    if t >= C["s10.c"]:
        p = ep(t, C["s10.c"], 0.4)
        E.caixa_pontilhada(c, DX[6] - 110, cy - 80, 220, 160, p, ERRADO, p)

    def s09():
        E.frase(c, t, C["s09.a"], [("bloco:", "i", 66), ("7", "g", 64, COR), ("dias", "i", 66)], XE, 520)
        E.frase(c, t, C["s09.b"], [("o", "i", 66), ("número", "i", 66), ("é", "i", 66), ("a", "i", 66), ("posição", "g", 62, ENT), ("no", "i", 66), ("curso", "i", 66)], 700, 520)
        fx_em(c, t, C["s09.c"], [("200", ENT), (" ÷ 7 = 28, resto ", TINTA), ("4", COR)], XE, 680, 86)
        E.foco(c, t, C["s09.c"] + 1.0, 0.4, lambda a: E.escreve(c, "28 voltas completas", XE + 20, 760, 48, "i", TINTA2, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.escreve(c, "4ª casa do bloco", XE, 880, 62, "g", COR, a))
        resultado(c, t, C["s09.e"], "quinta", 1450, 780, 150)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("“daqui", "i", 70, ERRADO), ("a", "i", 70, ERRADO), ("200", "g", 66, ERRADO), ("dias”", "i", 70, ERRADO), ("→", "g", 66, TINTA2),
                               ("sexta", "g", 66, ERRADO)], XE, 560)
    E.frase(c, t, C["s10.b"], [("aqui,", "i", 70), ("o", "i", 70), ("dia", "i", 70), ("1", "g", 66, ENT), ("já", "i", 70), ("é", "i", 70), ("a", "i", 70),
                               ("segunda", "g", 66, CERTO)], XE, 700)
    E.frase(c, t, C["s10.c"], [("resto", "i", 70), ("0", "g", 66, COR), ("→", "g", 66, TINTA2), ("fim", "i", 70), ("da", "i", 70), ("volta:", "i", 70),
                               ("domingo", "g", 66)], XE, 840)


# ---------------- situação 3: parcelas ----------------
PX3 = (330, 600, 870)
CX, CY, CWD, CHT, CMAX = 900, 230, 900, 560, 360


def b_questao3(c, t, C, b):
    situacao(c, t, C["s11.a"], 3)
    cy = 360
    E.frase(c, t, C["s11.b"], [("12", "g", 70, ENT), ("parcelas", "i", 74), ("mensais", "i", 74)], 1130, 150)
    fila(c, t, [(PX3[0], "R$ 100", "1ª", C["s11.c"])], cy, 230, 130, 60, pos_size=44)
    fila(c, t, [(x, f"R$ {v}", f"{i + 2}ª", C["s11.d"] + 0.6 + 0.3 * i) for i, (x, v) in enumerate(zip(PX3[1:], (120, 140)))], cy, 230, 130, 60, pos_size=44)
    for i in range(2):
        pula(c, t, C["s11.d"] + 0.3 * i, PX3[i], PX3[i + 1], cy - 65, "+20", alto=60, size=46)
    fila(c, t, [(1110, "…", None, C["s11.e"] - 0.3)], cy)
    E.foco(c, t, C["s11.e"] - 0.2, 0.5, lambda a: caixa(c, 1360, cy, 230, 130, "?", a, "12ª", 60, CINZA, pos_size=44))
    pergunta(c, t, C["s11.e"], 1, [("a ", TINTA), ("última", COR), (" parcela?", TINTA)], 680)
    pergunta(c, t, C["s11.f"], 2, [("o ", TINTA), ("total", COR), (" pago?", TINTA)], 800)
    if t >= C["s12"]:
        E.relogio(c, t, C["s12.a"], 1600, 740, 120)


def parcelas(c, t, t0, escuro=False, cor=None, ultima=None, rotulos=True):
    centros = E.colunas(c, t, t0, [(str(i + 1), v) for i, v in enumerate(PARC)], CX, CY, CWD, CHT, vmax=CMAX, cor=cor or (CLARO if escuro else COR),
                        valores=False, escuro=escuro, passo=0.06, size=34, d=0.5)
    tinta = BR if escuro else TINTA
    if rotulos:
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: centro(c, "100", centros[0][0], centros[0][1] - 18, 44, "g", tinta, a))
    if ultima is not None and rotulos:
        E.foco(c, t, ultima, 0.4, lambda a: centro(c, "320", centros[-1][0], centros[-1][1] - 18, 44, "g", tinta, a))
    return centros


def b_resposta3(c, t, C, b):
    parcelas(c, t, C["s13"] - 0.4, ultima=C["s13.c"])

    def s13():
        E.frase(c, t, C["s13.a"], [("1ª", "g", 66, ENT), ("→", "g", 66, TINTA2), ("12ª:", "g", 66, ENT)], XE, 330)
        E.frase(c, t, C["s13.a"] + 0.6, [("11", "g", 66, COR), ("saltos", "i", 70), ("de", "i", 70), ("20", "g", 66, RAZ)], XE, 430)
        fx_em(c, t, C["s13.b"], "11 · 20 = 220", XE, 590, 80)
        fx_em(c, t, C["s13.c"], [("a_{12}", SAI), (" = 100 + 220", TINTA)], XE, 750, 80)
        fx_em(c, t, C["s13.c"] + 0.6, [("= R$ 320", COR)], XE + 60, 870, 80)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], [("total", "g", 70, COR)], XE, 330)
    fx_em(c, t, C["s14.a"], "100 + 320 = 420", XE, 470, 80)
    fx_em(c, t, C["s14.b"], [("12", ENT), (" ÷ 2 = 6", TINTA)], XE, 610, 80)
    fx_em(c, t, C["s14.c"], "420 · 6 =", XE, 760, 80)
    resultado(c, t, C["s14.c"] + 0.5, "R$ 2.520", XE + E.formula(None, "420 · 6 =", 0, 0, 80, "g", a=0) + 140, 730, 115)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], [("o", "i", 70, CLARO), ("atalho", "g", 70, BR), ("da", "i", 70, CLARO), ("média", "g", 70, BR)], XE, 150)
    centros = parcelas(c, t, C["s15"] - 0.4, escuro=True, rotulos=False)
    vy = lambda v: CY + CHT - v / CMAX * CHT
    falta = ep(t, C["s15.d"], 0.6)
    if falta > 0:
        bw = CWD / 12 * 0.62
        for (cx, _), v in zip(centros, PARC):
            y0, y1 = sorted((vy(v), vy(210)))
            c.drawRect(skia.Rect.MakeLTRB(cx - bw / 2, y0, cx + bw / 2, y1), M.paint(ERRADO if v < 210 else CERTO, 0.75 * falta))
    p = ep(t, C["s15.a"] + 0.4, 0.6)
    if p > 0:
        M.line(c, CX - 10, vy(210), CX - 10 + (CWD + 20) * p, vy(210), BR, 1.0, 5, dash=[18, 12])
    E.foco(c, t, C["s15.a"] + 0.8, 0.4, lambda a: E.escreve(c, "210", CX + CWD + 20, vy(210) + 20, 54, "g", BR, a))
    fx_em(c, t, C["s15.a"], [("f{420}{2} = 210", BR)], XE, 360, 84)
    E.frase(c, t, C["s15.b"], [("12", "g", 64, BR), ("parcelas", "i", 66, CLARO), ("de", "i", 66, CLARO), ("210", "g", 64, BR)], XE, 520)
    fx_em(c, t, C["s15.c"], [("210 · 12 = ", BR), ("2.520", CLARO)], XE, 650, 80)
    E.foco(c, t, C["s15.d"] + 0.4, 0.4, lambda a: (E.escreve(c, "a menos", CX + 10, CY + CHT + 120, 50, "g", ERRADO, a),
                                                   E.escreve(c, "a mais", CX + CWD - 170, CY - 20, 50, "g", CERTO, a)))
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "só se sobe sempre o mesmo tanto", 520, 960, 44, "g", fundo=CERTO, a=a))


# ---------------- situação 4: postos de água ----------------
RX0, RX1, RY = 260, 1660, 560


def estrada(c, t, t0, marcas, tm=None):
    return E.reta(c, t, t0, RX0, RX1, RY, 0, 40, marcas, fmt=lambda v: str(v), size=42, tm=tm)


def b_questao4(c, t, C, b):
    E.frase(c, t, C["s16.a"], [("última", "i", 72, COR), ("situação", "i", 72, COR)], XE, 150)
    vx = estrada(c, t, C["s16.a"] + 0.4, [0, 3, 39], tm=[C["s16.a"] + 0.6, C["s16.c"], C["s16.d"]])
    E.foco(c, t, C["s16.a"] + 0.6, 0.4, lambda a: E.escreve(c, "km", RX1 + 80, RY + 80, 42, "i", TINTA2, a))
    E.frase(c, t, C["s16.b"], [("um", "i", 70), ("posto", "i", 70), ("a", "i", 70), ("cada", "i", 70), ("4", "g", 66, RAZ), ("km", "i", 70)], XE, 300)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: poste(c, vx(3), RY, a, num=1))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: poste(c, vx(39), RY, a, num="?"))
    E.foco(c, t, C["s16.d"] + 0.4, 0.4, lambda a: centro(c, "…", (vx(3) + vx(39)) / 2, RY - 60, 80, "g", TINTA2, a))
    pergunta(c, t, C["s16.e"], 1, [("quantos", COR), (" postos?", TINTA)], 800)
    pergunta(c, t, C["s16.f"], 2, [("o ", TINTA), ("6º", ENT), (" posto: em que km?", TINTA)], 920)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], 1620, 800, 90)


def b_resposta4(c, t, C, b):
    t0 = C["s18"] - 0.4
    vx = estrada(c, t, t0, [0] + POSTOS, tm=[t0] + [t0 + 0.1 * i for i in range(10)])
    seis = t >= C["s19.c"]
    for i, km in enumerate(POSTOS):
        cor = CERTO if (seis and i == 5) else COR
        E.foco(c, t, t0 + 0.1 * i, 0.4, lambda a, km=km, i=i, cor=cor: poste(c, vx(km), RY, a, cor, i + 1 if t >= C["s18.c"] else None))
    for i in range(9):
        q = 1 - ep(t, C["s19"] - 0.2, 0.3) if i >= 5 else 1
        if q > 0:
            E.salto(c, t, C["s18.b"] + 0.12 * i, vx(POSTOS[i]) + 8, vx(POSTOS[i + 1]) - 8, RY - 140, 40, RAZ, None, d=0.4, largura=5)
    if C["s18.d"] <= t < C["s19"]:
        p = prog(t, C["s18.d"], 1.2)
        if p < 1:
            c.drawCircle(vx(3), RY - 104, 30 + 50 * ease_out(p), M.paint(COR, 1 - p, stroke=6))

    def s18():
        fx_em(c, t, C["s18.a"], "39 − 3 = 36", XE, 780, 80)
        fx_em(c, t, C["s18.b"], [("36 ÷ 4 = ", TINTA), ("9 saltos", RAZ)], 760, 780, 80)
        fx_em(c, t, C["s18.c"], [("9 + 1 = ", TINTA), ("10 postos", COR)], XE, 920, 80)
        E.foco(c, t, C["s18.d"], 0.4, lambda a: E.escreve(c, "o posto do km 3 não precisou de salto", XE, 1010, 48, "i", TINTA2, a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19.a"], [("6º", "g", 66, ENT), ("posto:", "i", 70), ("5", "g", 66, RAZ), ("saltos", "i", 70)], XE, 780)
    fx_em(c, t, C["s19.b"], "5 · 4 = 20", XE, 920, 80)
    fx_em(c, t, C["s19.c"], "3 + 20 = 23", 700, 920, 80)
    resultado(c, t, C["s19.c"] + 0.5, "km 23", 1450, 860, 110, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("o que se ", TINTA), ("repete", COR), (", o que se ", TINTA), ("soma", COR)]),
                 ("s20.b", [("posição", ENT), (" ≠ ", TINTA), ("valor", SAI)]),
                 ("s20.c", [("termos = saltos + 1", TINTA)]))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 430, y, 80)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s21.b"], [("Progressão", "g", 130, COR)], XE, 420)
    E.frase(c, t, C["s21.b"] + 0.3, [("geométrica", "g", 130, COR)], XE, 560)
    XS = (1270, 1470, 1670)
    fila(c, t, [(x, v, None, C["s21.a"] + 0.4 * i) for i, (x, v) in enumerate(zip(XS, (3, 6, 12)))], 280, 150, 110, 66)
    for i in range(2):
        pula(c, t, C["s21.a"] + 0.4 + 0.3 * i, XS[i], XS[i + 1], 280 - 55, "×2", alto=50, size=44)
    fx_em(c, t, C["s21.c"], [("a_8", SAI), (" = ?", TINTA)], 1200, 500, 80)
    E.frase(c, t, C["s21.d"], [("juros", "g", 62, COR), ("compostos", "g", 62, COR)], 1200, 620)
    E.foco(c, t, C["s21.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.e"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s21.e"] + 0.2, 0.4))
    E.frase(c, t, C["s21.f"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
