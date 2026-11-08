"""Visual — Estudativo · MAT-RAZ-001: o que é razão.
Peças locais: fita() é a fita de medida em escala (50 cm contra 2 m = 200 cm, na mesma escala de px por cm); pessoa()/turma()
são os bonecos da turma (meninos na cor da matéria, meninas em preto); fr2() é a fração com o de cima e o de baixo em cores
próprias (o primeiro da frase na cor da matéria); zeros() risca os zeros do final, um por um; degraus() é a escada do metro
encurtada (m, dm, cm) da trilha de Medidas; partes() é a barra cortada em pedaços iguais (mesma peça de MAT-RAZ-013).
Instantes: cues C[...] e, dentro da frase, a palavra falada (PW, lida de audio/tempos.json)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-001_o_que_e_razao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("razao", "unidade", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 9 / 15 == 3 / 5 and 9 // 3 == 3 and 15 // 3 == 5 and 3 + 5 == 8
assert 2 * 100 == 200 and 50 / 200 == 1 / 4 and 200 // 50 == 4 and 4 * 50 == 200 and 50 / 2 == 25
assert 50 // 10 == 5 and 200 // 10 == 20 and 5 / 20 == 1 / 4
assert round(1.2 * 100) == 120 and 80 / 120 == 2 / 3 and 8 / 12 == 2 / 3 and 8 // 4 == 2 and 12 // 4 == 3

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima `palavra` da cena sid"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            k = 0
            for tk in s["tokens"]:
                if _n(tk["disp"]) == _n(palavra):
                    k += 1
                    if k == n:
                        return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, n))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fr2(c, n, d, cx, cy, size, cn=None, cd=None, a=1.0):
    """fração empilhada (mesma geometria de E.fracao) com cor própria em cima e embaixo"""
    if a <= 0:
        return
    n, d = str(n), str(d)
    lw = max(E.larg(n, "g", size), E.larg(d, "g", size)) + size * 0.2
    E.escreve(c, n, cx - E.larg(n, "g", size) / 2, cy - size * 0.2, size, "g", cn or TINTA, a)
    E.escreve(c, d, cx - E.larg(d, "g", size) / 2, cy + size * 0.9, size, "g", cd or TINTA, a)
    b = size * 0.085
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(TINTA if (cn or cd) else TINTA, a))


def fr2_em(c, t, t0, n, d, cx, cy, size, cn=None, cd=None):
    E.foco(c, t, t0, 0.5, lambda a: fr2(c, n, d, cx, cy, size, cn, cd, a))


def _xchar(s, i, cx, size):
    """centro x do caractere i de s, escrito centrado em cx (com o aperto de E.escreve)"""
    x0 = cx - E.larg(s, "g", size) / 2
    pre = E.larg(s[:i], "g", size) + E.APERTO["g"] * size if i > 0 else 0
    return x0 + pre + E.larg(s[i], "g", size) / 2


def zeros(c, t, n, d, cx, cy, size, k, tn, td, cor=ERRADO):
    """risca os k últimos algarismos de cima (em tn) e de baixo (em td) de uma fração E.fracao em (cx, cy)"""
    n, d = str(n), str(d)
    for s, yc, t0 in ((n, cy - size * 0.2 - size * 0.36, tn), (d, cy + size * 0.9 - size * 0.36, td)):
        for j in range(k):
            i = len(s) - k + j
            xc = _xchar(s, i, cx, size)
            E.risco(c, xc - size * 0.3, yc + size * 0.42, xc + size * 0.3, yc - size * 0.42, t, t0 + j * 0.15, cor, max(6, size * 0.07))


def fita(c, x, y, w, h, cor, a=1.0, p=1.0):
    """fita de medida que se desenrola da esquerda (p = 0..1), com tracinhos de régua"""
    if a <= 0 or p <= 0:
        return
    ww = w * ease_io(min(1.0, p))
    M.rrect(c, x, y, ww, h, h * 0.22, cor, a)
    k = 0
    passo = 35  # um tracinho a cada 5 cm na escala de 7 px por cm
    while k * passo < ww - 6:
        if k:
            alto = h * (0.38 if k % 2 == 0 else 0.22)
            M.line(c, x + k * passo, y, x + k * passo, y + alto, BR, a * 0.7, 3)
        k += 1


PX_CM = 7.0  # escala das fitas e tábuas: 200 cm = 1400 px


def pessoa(c, cx, base, h, cor=None, a=1.0, menina=False):
    """bonequinho: cabeça e corpo arredondado; a menina tem o corpo em saia (mais largo embaixo)"""
    if a <= 0:
        return
    cor = cor or E.COR
    r = h * 0.18
    c.drawCircle(cx, base - h + r, r, M.paint(cor, a))
    w = h * 0.56
    if not menina:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - h * 0.58, w, h * 0.58), w * 0.42, w * 0.42), M.paint(cor, a))
    else:
        p = skia.Path()
        top, wt, wb = base - h * 0.58, w * 0.5, w * 1.05
        p.moveTo(cx - wt / 2, top + w * 0.12)
        p.quadTo(cx, top - w * 0.12, cx + wt / 2, top + w * 0.12)
        p.lineTo(cx + wb / 2, base - h * 0.04)
        p.quadTo(cx, base + h * 0.03, cx - wb / 2, base - h * 0.04)
        p.close()
        c.drawPath(p, M.paint(cor, a))


def turma(c, t, t0, n, x, base, h=90, gap=22, cor=None, menina=False, passo=0.08):
    """n bonecos lado a lado, a partir de x; entram um por um. Devolve a largura."""
    for i in range(n):
        E.foco(c, t, t0 + i * passo, 0.4, lambda a, i=i: pessoa(c, x + i * (h * 0.56 + gap) + h * 0.28, base, h, cor, a, menina))
    return n * (h * 0.56 + gap) - gap


def larg_turma(n, h, gap=22):
    return n * (h * 0.56 + gap) - gap


def grupo(c, t, t0, x, base, h, gap=22, meio=34, passo=0.06):
    """3 meninos e 5 meninas; devolve a largura"""
    w1 = turma(c, t, t0, 3, x, base, h, gap, E.COR, passo=passo)
    w2 = turma(c, t, t0 + 3 * passo, 5, x + w1 + meio, base, h, gap, TINTA, True, passo)
    return w1 + meio + w2


def partes(c, x, y, w, h, n, cor, a=1.0, cortes=1.0, rotulos=(), size=50):
    """barra cortada em n pedaços iguais, toda pintada; rotulos = [(i, texto, a)] no meio do pedaço i"""
    if a <= 0:
        return
    rr = E._casco(c, x, y, w, h, 14, a)
    c.save(); c.clipRRect(rr, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(cor, a))
    for i in range(1, n):
        lx = x + w * i / n
        M.line(c, lx, y, lx, y + h * M.clamp(cortes), BR, a, 5)
    c.restore()
    for i, s, q in rotulos:
        if q > 0:
            centro(c, s, x + w / n * (i + 0.5), y + h / 2 + size * 0.36, size, "g", BR, a * q)


# --- escada do metro, encurtada: m, dm, cm ---
def degraus(c, t, t0, x, y, sw, sh, base, hops, a=1.0):
    """3 degraus descendo (m, dm, cm); hops = instantes dos dois pulos (× 10 cada)"""
    un, nomes = ("m", "dm", "cm"), ("metro", "decímetro", "centímetro")
    for i in range(3):
        ti = t0 + 0.12 * i
        q = ep(t, ti, 0.45)
        if q <= 0:
            continue
        top, x0 = y + i * sh, x + i * sw
        hh = (base - top) * ease_io(prog(t, ti, 0.45))
        meio = i == 0
        fundo, borda, tinta = (E.COR, E.COR, E.SOBRE) if meio else ("#FFFFFF", TINTA2, TINTA)
        M.rrect(c, x0 + 4, base - hh, sw - 8, hh, 12, fundo, q * a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, base - hh, sw - 8, hh), 12, 12), M.paint(borda, q * a, stroke=3))
        E.foco(c, t, ti + 0.2, 0.45, lambda b, i=i, top=top, x0=x0, tinta=tinta: (
            centro(c, un[i], x0 + sw / 2, top + 70, 60, "g", tinta, b * a),
            centro(c, nomes[i], x0 + sw / 2, top + 116, 34, "i", E.SOBRE if i == 0 else TINTA2, b * a)))
    for k, th in enumerate(hops):  # arco do pulo com "× 10"
        p = ep(t, th, 0.6)
        if p <= 0:
            continue
        xa, ya = x + (k + 0.5) * sw, y + k * sh - 20
        xb, yb = x + (k + 1.5) * sw, y + (k + 1) * sh - 20
        mx, my = (xa + xb) / 2, min(ya, yb) - 70
        pts = [(lerp(lerp(xa, mx, u), lerp(mx, xb, u), u), lerp(lerp(ya, my, u), lerp(my, yb, u), u)) for u in [p * j / 24 for j in range(25)]]
        path = skia.Path(); path.moveTo(*pts[0])
        for px, py in pts[1:]:
            path.lineTo(px, py)
        c.drawPath(path, M.paint(E.COR, 0.8 * a, stroke=6, cap_round=True))
        E.foco(c, t, th + 0.2, 0.4, lambda b, mx=mx, my=my: E.pilula(c, "× 10", mx, my - 30, 40, "g", a=b * a))


# ---------------- gancho ----------------
X0 = 260  # início das fitas


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    t25 = PW("s01", "Vinte", 2)

    def cena():
        y1, y2 = 300, 500
        fita(c, X0, y1, 50 * PX_CM, 90, E.COR, 1.0, prog(t, a1, 0.7))
        E.foco(c, t, a1 + 0.4, 0.5, lambda a: E.escreve(c, "50 cm", X0, y1 - 30, 64, "g", COR, a))
        fita(c, X0, y2, 200 * PX_CM, 90, TINTA, 1.0, prog(t, b1, 1.0))
        E.foco(c, t, b1 + 0.5, 0.5, lambda a: E.escreve(c, "2 m", X0, y2 - 30, 64, "g", TINTA, a))
        E.foco(c, t, c1 - 0.6, 0.5, lambda a: E.formula(c, "50 ÷ 2 =", 900, 800, 110, "g", TINTA, a, "right"))
        E.foco(c, t, c1, 0.5, lambda a: E.formula(c, "25", 940, 800, 130, "g", ERRADO, a))
        E.frase(c, t, t25, ps("25 vezes o quê?", "i", 76, ERRADO), 1180, 790, passo=0.12)
        if t >= d1:
            E.foco(c, t, d1 + 0.5, 0.5, lambda a: E.pilula(c, "a menor!", X0 + 50 * PX_CM + 190, y1 + 45, 60, "g", a=a))
            E.frase(c, t, d1 + 0.2, ps("a fita de 50", "i", 76) + [("é a menor", "g", 76, COR)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "compara"), [("comparar", "g", 110, COR)], XE, 490)
        E.frase(c, t, PW("s02", "duas"), ps("duas quantidades", "i", 84), XE, 620, passo=0.12)
        E.frase(c, t, PW("s02", "jeito"), ps("do jeito", "i", 84) + [("certo", "g", 84, COR)], XE, 740, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "simplificar fração", "÷ em cima e embaixo"), ("s03.c", "converter comprimento", "a escada do metro"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "faltar"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- o que é razão ----------------
def b_razao(c, t, C, b):
    # s04: a turma
    def turma1():
        a4, b4 = C["s04.a"], C["s04.b"]
        E.frase(c, t, C["s04"] + 0.3, ps("numa turma", "i", 84), W / 2, 190, "center", 0.14)
        h = 170
        w = larg_turma(3, h) + 120 + larg_turma(5, h)
        x = (W - w) / 2
        turma(c, t, a4, 3, x, 560, h, cor=E.COR)
        turma(c, t, PW("s04", "cinco"), 5, x + larg_turma(3, h) + 120, 560, h, cor=TINTA, menina=True)
        E.linha(c, t, [("3 meninos", "g", 76, COR, a4), ("para cada", "i", 76, TINTA, PW("s04", "para")),
                       ("5 meninas", "g", 76, TINTA, PW("s04", "cinco"))], W / 2, 720, "center")
        E.frase(c, t, PW("s04", "compara"), ps("compara duas quantidades", "i", 64, TINTA2), W / 2, 830, "center", 0.12)
        E.foco(c, t, b4, 0.5, lambda a: E.pilula(c, "razão", W / 2, 960, 90, "g", a=a))
    E.saida(c, t, C["s05"] - 0.1, turma1)

    # s05: definição, fração, leitura, dois-pontos
    def defin():
        a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
        E.frase(c, t, a5, [("razão", "g", 90, COR)] + ps("= comparar dois números", "i", 80), W / 2, 200, "center", 0.12)
        E.frase(c, t, PW("s05", "divisao"), ps("pela", "i", 80) + [("divisão", "g", 84, COR)], W / 2, 310, "center", 0.12)
        fr2_em(c, t, b5, 3, 5, 640, 560, 200, COR, TINTA)
        E.foco(c, t, b5 + 0.3, 0.5, lambda a: (E.escreve(c, "meninos", 760, 470, 48, "i", COR, a), E.escreve(c, "meninas", 760, 700, 48, "i", TINTA, a)))
        E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "lê-se: 3 para 5", 640, 900, 60, "i", a=a))
        E.foco(c, t, d5 - 0.4, 0.5, lambda a: centro(c, "ou", 1180, 610, 70, "i", TINTA2, a))
        E.foco(c, t, d5, 0.5, lambda a: (centro(c, "3 : 5", 1520, 640, 200, "g", TINTA, a)))
        E.foco(c, t, d5 + 0.4, 0.5, lambda a: centro(c, "dois-pontos", 1520, 760, 52, "i", TINTA2, a))
        E.foco(c, t, PW("s05", "Le-se"), 0.5, lambda a: E.pilula(c, "lê-se: 3 para 5", 1520, 900, 60, "i", fundo=TINTA, a=a))
    if t >= C["s05"]:
        E.saida(c, t, C["s06"] - 0.1, defin)

    # s06: 9 meninos e 15 meninas = 3/5
    if t >= C["s06"]:
        a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
        h, meio, gap_g = 74, 30, 70
        wg = larg_turma(3, h) + meio + larg_turma(5, h)
        x0 = (W - (3 * wg + 2 * gap_g)) / 2
        E.frase(c, t, a6, ps("a cada", "i", 76) + [("3 meninos,", "g", 76, COR), ("5 meninas", "g", 76, TINTA)], W / 2, 170, "center", 0.12)
        for g in range(3):
            tg = a6 if g == 0 else b6 + 0.1 + 0.35 * (g - 1)
            xg = x0 + g * (wg + gap_g)
            grupo(c, t, tg, xg, 400, h)
            E.foco(c, t, tg + 0.3, 0.5, lambda a, xg=xg: E.caixa_pontilhada(c, xg - 22, 280, wg + 44, 150, a, E.COR))
        E.linha(c, t, [("9 meninos", "g", 64, COR, b6), ("e", "i", 64, TINTA, PW("s06", "quinze") - 0.2),
                       ("15 meninas", "g", 64, TINTA, PW("s06", "quinze"))], W / 2, 530, "center")
        cy = 720
        fr2_em(c, t, c6, 9, 15, 760, cy, 120, COR, TINTA)
        E.pontes(c, t, 870, 1060, cy, 120, "÷ 3", PW("s06", "Divida"), PW("s06", "Divida") + 0.4, size=44)
        fr2_em(c, t, d6, 3, 5, 1170, cy, 120, COR, TINTA)
        E.foco(c, t, PW("s06", "simplifica"), 0.5, lambda a: E.pilula(c, "simplifica igual à fração", 1580, cy + 10, 44, "i", fundo=TINTA, a=a))
        E.linha(c, t, [("não diz quantos alunos há:", "i", 60, TINTA, e6), ("diz como se repartem", "g", 60, COR, PW("s06", "Diz", 2))],
                W / 2, 990, "center")


# ---------------- a ordem ----------------
def b_ordem(c, t, C, b):
    def ordem():
        a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        E.frase(c, t, a7, ps("a", "i", 96) + [("ordem", "g", 96, COR)] + ps("importa", "i", 96), W / 2, 200, "center", 0.12)
        E.frase(c, t, PW("s07", "Meninos"), [("meninos", "g", 56, COR)] + ps("para meninas", "i", 56), 560, 380, "center", 0.1)
        fr2_em(c, t, b7, 3, 5, 560, 570, 160, COR, TINTA)
        E.frase(c, t, PW("s07", "Meninas"), [("meninas", "g", 56, TINTA)] + ps("para meninos", "i", 56), 1360, 380, "center", 0.1)
        fr2_em(c, t, c7, 5, 3, 1360, 570, 160, TINTA, COR)
        E.foco(c, t, PW("s07", "maior"), 0.5, lambda a: E.pilula(c, "maior que 1", 1360, 820, 52, "g", fundo=TINTA, a=a))
        E.foco(c, t, c7 + 0.3, 0.5, lambda a: centro(c, "≠", W / 2, 640, 120, "g", TINTA2, a))
        E.frase(c, t, d7, ps("o 1º da frase vai", "i", 72) + [("em cima", "g", 72, COR)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s08"] - 0.1, ordem)

    if t >= C["s08"]:
        a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, C["s08"] + 0.6, ps("a parte e o", "i", 80) + [("todo", "g", 80, COR)], W / 2, 170, "center", 0.12)
        h = 120
        w = larg_turma(3, h) + 40 + larg_turma(5, h)
        x = (W - w) / 2
        grupo(c, t, PW("s08", "cada"), x, 410, h, meio=40)
        E.chave(c, x - 6, x + w + 6, 440, TINTA2, ep(t, a8, 0.5), 24)
        E.foco(c, t, a8 + 0.2, 0.5, lambda a: centro(c, "8 alunos", W / 2, 540, 64, "g", TINTA, a))
        cy = 790
        E.foco(c, t, b8 - 1.6, 0.5, lambda a: E.escreve(c, "meninos para o total", 1280 - E.larg("meninos para o total", "i", 46) / 2, 640, 46, "i", TINTA2, a))
        fr2_em(c, t, b8, 3, 8, 1280, cy, 120, COR, TINTA)
        E.foco(c, t, c8, 0.5, lambda a: E.escreve(c, "meninos para meninas", 640 - E.larg("meninos para meninas", "i", 46) / 2, 640, 46, "i", TINTA2, a))
        fr2_em(c, t, c8, 3, 5, 640, cy, 120, COR, TINTA)
        E.foco(c, t, c8 + 0.2, 0.5, lambda a: centro(c, "≠", 960, cy + 50, 110, "g", ERRADO, a))
        E.foco(c, t, PW("s08", "Leia"), 0.5, lambda a: E.pilula(c, "leia o que o problema compara", W / 2, 1000, 50, "i", fundo=TINTA, a=a))


# ---------------- mesma unidade ----------------
def b_unidade(c, t, C, b):
    def fitas():
        a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, a9, ps("antes de dividir:", "i", 76) + [("mesma unidade", "g", 76, COR)], W / 2, 150, "center", 0.12)
        y1, y2 = 270, 420
        t0 = C["s09"] + 0.3
        fita(c, X0, y1, 50 * PX_CM, 80, E.COR, 1.0, prog(t, t0, 0.6))
        E.foco(c, t, t0 + 0.3, 0.5, lambda a: E.escreve(c, "50 cm", X0 + 50 * PX_CM + 30, y1 + 62, 60, "g", COR, a))
        fita(c, X0, y2, 200 * PX_CM, 80, TINTA, 1.0, prog(t, t0 + 0.3, 0.8))
        if t < c9:
            E.foco(c, t, t0 + 0.7, 0.5, lambda a: E.pilula(c, "2 m", X0 + 1400 - 120, y2 - 50, 50, "g", fundo=TINTA, a=a))
        else:
            E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "200 cm", X0 + 1400 - 160, y2 - 50, 50, "g", a=a))
        degraus(c, t, b9 - 0.9, 300, 690, 220, 70, 1000, (b9, b9 + 0.7))
        E.foco(c, t, PW("s09", "vezes"), 0.5, lambda a: E.pilula(c, "× 100", 1080, 760, 64, "g", a=a))
        fcen(c, t, c9, "2 m = 200 cm", 1480, 900, 90, TINTA)
    E.saida(c, t, C["s10"] - 0.1, fitas)

    def simplifica():
        a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
        E.frase(c, t, C["s10"] + 0.2, ps("a razão", "i", 80), W / 2, 170, "center")
        cy = 440
        E.foco(c, t, a10, 0.5, lambda a: fr2(c, 50, 200, 560, cy, 150, COR, TINTA, a))
        E.foco(c, t, PW("s10", "MDC"), 0.5, lambda a: E.pilula(c, "MDC(50, 200) = 50", 960, 260, 46, "g", fundo=TINTA, a=a))
        E.pontes(c, t, 730, 1130, cy, 150, "÷ 50", b10, c10, size=46)
        E.frac_q(c, t, a10 + 0.5, 1, 4, b10 + 0.4, c10 + 0.4, 1300, cy, 150)
        E.foco(c, t, d10, 0.5, lambda a: E.caixa_pontilhada(c, 1210, cy - 200, 180, 400, a, E.COR))
        E.saida(c, t, e10 - 0.1, lambda: E.frase(c, t, PW("s10", "fita"), ps("a menor é a", "i", 70) + [("quarta parte", "g", 70, COR)] + ps("da maior", "i", 70),
                                                W / 2, 800, "center", 0.12))
        # 4 fitas de 50 cm, uma atrás da outra, embaixo da fita de 200 cm
        if t >= e10:
            fita(c, X0, 720, 200 * PX_CM, 70, TINTA, 1.0, prog(t, e10, 0.6))
            for i in range(4):
                ti = e10 + 0.6 + i * 0.4
                E.foco(c, t, ti, 0.4, lambda a, i=i: (fita(c, X0 + i * 50 * PX_CM + 4, 820, 50 * PX_CM - 8, 70, E.COR, a),
                                                      centro(c, "50", X0 + (i + 0.5) * 50 * PX_CM, 875, 44, "g", BR, a)))
            E.foco(c, t, e10 + 0.3, 0.5, lambda a: E.escreve(c, "200 cm", X0, 700, 50, "g", TINTA, a))
            fcen(c, t, PW("s10", "exatamente"), "4 · 50 = 200 cm = 2 m", W / 2, 1010, 70, TINTA)
    if t >= C["s10"]:
        E.saida(c, t, C["s11"] - 0.1, simplifica)

    if t >= C["s11"]:
        a11, b11 = C["s11.a"], C["s11.b"]
        cx, cy, s = 620, 470, 120
        E.foco(c, t, C["s11"] + 0.3, 0.5, lambda a: fr2(c, "50 cm", "200 cm", cx, cy, s, TINTA, TINTA, a))
        tc = PW("s11", "Centimetro")
        for txt, base in (("50 cm", cy - s * 0.2), ("200 cm", cy + s * 0.9)):
            x0 = cx - E.larg(txt, "g", s) / 2 + E.larg(txt[:-2], "g", s)
            E.risco(c, x0, base + 6, x0 + E.larg("cm", "g", s) + 6, base - s * 0.62, t, tc, ERRADO, 10)
        E.foco(c, t, PW("s11", "some"), 0.5, lambda a: E.formula(c, "= f{1}{4}", 950, cy + 45, 130, "g", TINTA, a))
        E.foco(c, t, a11, 0.5, lambda a: E.pilula(c, "sem unidade", 1500, cy, 64, "g", a=a))
        E.frase(c, t, b11, [("1/4", "g", 80, COR)] + ps("em qualquer unidade:", "i", 76), W / 2, 860, "center", 0.12)
        E.frase(c, t, PW("s11", "so"), ps("é só uma", "i", 76) + [("comparação", "g", 76, COR)], W / 2, 970, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    E.frase(c, t, C["s12"] + 0.4, ps("o erro", "i", 96) + [("mais comum", "g", 96, ERRADO)], W / 2, 190, "center", 0.12)
    E.frase(c, t, a12, ps("dividir em", "i", 72) + [("unidades diferentes", "g", 72, ERRADO)], W / 2, 320, "center", 0.12)
    y = 560
    E.linha(c, t, [("50", "g", 130, TINTA, b12), ("cm", "i", 100, ERRADO, b12 + 0.1), ("÷ 2", "g", 130, TINTA, PW("s12", "dois")),
                   ("m", "i", 100, ERRADO, PW("s12", "dois") + 0.1), ("= 25", "g", 130, ERRADO, PW("s12", "vinte"))], W / 2, y, "center")
    if t >= PW("s12", "misturou"):
        E.risco(c, 560, y + 30, 1360, y - 110, t, PW("s12", "misturou"), ERRADO, 14)
    E.frase(c, t, PW("s12", "misturou"), ps("misturou", "i", 60, TINTA2) + [("cm", "g", 60, ERRADO)] + ps("com", "i", 60, TINTA2) + [("m", "g", 60, ERRADO)],
            W / 2, 690, "center", 0.1)
    p = ep(t, c12, 0.5)
    E.caixa_pontilhada(c, 430, 790, 1060, 170, p, E.COR, prog_=p)
    E.foco(c, t, PW("s12", "teste"), 0.5, lambda a: E.pilula(c, "teste rápido", 430 + 150, 790, 40, "g", a=a))
    fcen(c, t, c12, "menor ÷ maior  <  1", W / 2, 905, 84, COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def corta():
        a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 80, CLARO), W / 2, 180, "center", 0.12)
        E.frase(c, t, a13, ps("corte os", "i", 84, CLARO) + ps("zeros do final", "g", 84, BR), W / 2, 310, "center", 0.12)
        E.frase(c, t, PW("s13", "cima"), ps("em cima e embaixo,", "i", 64, CLARO) + ps("na mesma quantidade", "g", 64, BR), W / 2, 420, "center", 0.1)
        cy, s = 660, 150
        E.foco(c, t, b13, 0.5, lambda a: E.fracao(c, 50, 200, 520, cy, s, BR, a))
        zeros(c, t, 50, 200, 520, cy, s, 1, PW("s13", "vira") - 0.3, PW("s13", "vira"), CLARO)
        tv = PW("s13", "cinco")
        if t >= tv:
            p = ep(t, tv - 0.2, 0.5)
            M.arrow(c, 720, cy + 10, 860, cy + 10, CLARO, p, 5, 18, p)
        E.foco(c, t, tv, 0.5, lambda a: E.fracao(c, 5, 20, 1010, cy, s, BR, a))
        E.ponte(c, t, PW("s13", "dividindo"), 1150, 1360, cy + 10, "÷ 5", CLARO, 44)
        E.foco(c, t, c13, 0.5, lambda a: (E.bola(c, 1530, cy, 130, a=a), E.fracao(c, 1, 4, 1530, cy, 100, BR, a)))
    E.saida(c, t, C["s14"] - 0.1, corta)

    def porque():
        a14, b14 = C["s14.a"], C["s14.b"]
        E.frase(c, t, a14, ps("cortar um zero =", "i", 84, CLARO) + [("÷ 10", "g", 90, BR)], W / 2, 260, "center", 0.12)
        cy, s = 560, 130
        E.foco(c, t, a14 + 0.8, 0.5, lambda a: E.fracao(c, 50, 200, 720, cy, s, BR, a))
        E.pontes(c, t, 860, 1060, cy, s, "÷ 10", b14, PW("s14", "embaixo"), CLARO, 42)
        E.foco(c, t, b14 + 0.3, 0.5, lambda a: E.fracao(c, 5, 20, 1200, cy, s, BR, a))
    if t >= C["s14"]:
        E.saida(c, t, C["s14.c"] - 0.1, porque)

    if t >= C["s14.c"]:
        c14, d14 = C["s14.c"], C["s14.d"]
        E.frase(c, t, c14, ps("só vale se", "i", 80, CLARO) + ps("os dois terminam em 0", "g", 80, BR), W / 2, 260, "center", 0.12)
        cy, s = 540, 170
        E.foco(c, t, d14, 0.5, lambda a: E.fracao(c, 45, 100, W / 2, cy, s, BR, a))
        xc = _xchar("45", 1, W / 2, s)
        E.foco(c, t, PW("s14", "termina"), 0.5, lambda a: (c.drawCircle(xc, cy - s * 0.56, s * 0.48, M.paint(ERRADO, a, stroke=7)),
                                                           E.escreve(c, "não termina em 0", xc + s * 0.6, cy - s * 0.4, 48, "i", CLARO, a)))
        E.foco(c, t, PW("s14", "nao"), 0.5, lambda a: E.pilula(c, "não corte nada", W / 2, 900, 72, "g", fundo=ERRADO, cor=BR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 200)
    k = 7.0
    fita(c, XE, 340, 120 * k, 90, E.COR, 1.0, prog(t, a15, 0.7))
    E.foco(c, t, a15 + 0.4, 0.5, lambda a: E.escreve(c, "1,2 m", XE, 315, 64, "g", COR, a))
    fita(c, XE, 560, 80 * k, 90, TINTA, 1.0, prog(t, b15, 0.7))
    E.foco(c, t, b15 + 0.4, 0.5, lambda a: E.escreve(c, "80 cm", XE, 535, 64, "g", TINTA, a))
    E.frase(c, t, c15, ps("razão entre a", "i", 76) + [("menor", "g", 76, COR)], XE, 820, passo=0.12)
    E.frase(c, t, c15 + 0.8, ps("e a", "i", 76) + [("maior?", "g", 76, COR)], XE, 930, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1500, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]

    def contas():
        E.frase(c, t, C["s17"] + 1.2, ps("mesma unidade", "i", 70, COR), W / 2, 160, "center")
        fcen(c, t, a17, "1,2 m · 100 = 120 cm", W / 2, 290, 90, TINTA)
        cy, s = 540, 130
        E.foco(c, t, PW("s17", "menor"), 0.5, lambda a: (E.escreve(c, "menor", 200, cy - 40, 44, "i", COR, a),
                                                         E.escreve(c, "maior", 200, cy + 100, 44, "i", TINTA2, a)))
        E.foco(c, t, b17, 0.5, lambda a: fr2(c, 80, 120, 450, cy, s, COR, TINTA, a))
        zeros(c, t, 80, 120, 450, cy, s, 1, c17, c17 + 0.3, ERRADO)
        E.ponte(c, t, c17 + 0.5, 590, 760, cy + 10, "corta 0", None, 36)
        E.foco(c, t, PW("s17", "oito"), 0.5, lambda a: fr2(c, 8, 12, 870, cy, s, COR, TINTA, a))
        E.ponte(c, t, d17, 980, 1180, cy + 10, "÷ 4", None, 44)
        E.foco(c, t, PW("s17", "dois", 2), 0.5, lambda a: (E.bola(c, 1350, cy, 130, a=a), E.fracao(c, 2, 3, 1350, cy, 100, E.SOBRE, a)))
        E.frase(c, t, a18, ps("razão de", "i", 76) + [("2 para 3", "g", 80, COR)], W / 2, 830, "center", 0.12)
        E.frase(c, t, b18, [("menor que 1,", "g", 64, CERTO)] + ps("como devia", "i", 64), W / 2, 950, "center", 0.12)
        E.foco(c, t, b18 + 0.8, 0.5, lambda a: E.selo(c, 1440, 930, 44, True, a))
    E.saida(c, t, c18 - 0.1, contas)

    if t >= c18:
        pw = 240  # pedaço de mesmo tamanho nas duas tábuas
        x = 520
        E.frase(c, t, c18, ps("a cada", "i", 76) + [("2 pedaços", "g", 76, COR)] + ps("na menor,", "i", 76), W / 2, 230, "center", 0.12)
        E.foco(c, t, c18 + 0.3, 0.5, lambda a: E.escreve(c, "menor", 230, 435, 56, "i", COR, a))
        partes(c, x, 360, 2 * pw, 120, 2, E.COR, ep(t, c18 + 0.3, 0.5), ep(t, c18 + 0.8, 0.5), [(i, str(i + 1), ep(t, c18 + 0.9 + 0.3 * i, 0.4)) for i in range(2)], 60)
        tm = PW("s18", "maior")
        E.foco(c, t, tm, 0.5, lambda a: E.escreve(c, "maior", 230, 635, 56, "i", TINTA, a))
        partes(c, x, 560, 3 * pw, 120, 3, TINTA, ep(t, tm, 0.5), ep(t, tm + 0.3, 0.5), [(i, str(i + 1), ep(t, tm + 0.4 + 0.25 * i, 0.4)) for i in range(3)], 60)
        E.frase(c, t, tm, ps("a maior tem", "i", 76) + [("3", "g", 80, TINTA)], W / 2, 860, "center", 0.12)
        E.foco(c, t, tm + 0.8, 0.5, lambda a: fr2(c, 2, 3, 1500, 470, 120, COR, TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "razão = divisão em fração"), ("s19.b", "na ordem da frase"), ("s19.c", "na mesma unidade"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20, e20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 260)
    E.frase(c, t, a20, ps("duas razões", "i", 76) + [("iguais", "g", 76, COR)], XE, 390, passo=0.12)
    fcen(c, t, b20, "f{2}{3} = f{6}{9}", XE + 230, 585, 140, TINTA)
    E.frase(c, t, c20, [("proporção", "g", 150, COR)], XE, 820)
    E.foco(c, t, d20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, d20 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, d20 + 0.2, 0.4))
    E.frase(c, t, e20, [("bons", "i", 110), ("estudos!", "i", 110, COR)], 1430, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, razao=b_razao, ordem=b_ordem, unidade=b_unidade, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
