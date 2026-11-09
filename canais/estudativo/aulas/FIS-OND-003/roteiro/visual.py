"""Visual — Estudativo · FIS-OND-003: reflexão, refração e difração de ondas.
Linguagem visual da trilha Ondas e Som: docstring do visual.py da FIS-OND-001. Nesta aula, a onda vista de cima é feita de
frentes (linhas laranja, uma por crista) que andam; tanque fundo = azul mais escuro, raso = mais claro; raio de onda e
normal como na Óptica (F.raio, F.normal); a frequência fixa aparece como pílula "f igual" em todos os fenômenos."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-003_reflexao_refracao_difracao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reflexao", "refracao", "difracao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FUNDO_AGUA, RASO_AGUA = "#9CCFE6", "#D3ECF6"

# todas as contas da aula
assert 170 * 2 == 340 and 340 / 340 == 1          # eco: 170 m ida e volta = 340 m, a 340 m/s → 1 s
assert abs(0.4 / 2 - 0.2) < 1e-12                 # tanque fundo: λ = 0,4 ÷ 2 = 0,2 m
assert abs(0.2 / 2 - 0.1) < 1e-12                 # tanque raso: λ = 0,2 ÷ 2 = 0,1 m (metade da velocidade, metade do λ)
assert 1500 / 500 == 3                            # na água: λ = 1.500 ÷ 500 = 3 m
assert abs(340 / 500 - 0.68) < 1e-12              # no ar: λ = 0,68 m


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def frentes_tanque(c, t, t0, x0, xb, x1, y0, y1, v1, v2, f, a=1.0, cor=None):
    """vista de cima: frentes retas que nascem em x0, andam a v1 (px/s) até a fronteira xb e a v2 depois.
    A frequência f é a mesma dos dois lados: cada frente cruza a fronteira, nenhuma some"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    dt = t - t0
    T = 1.0 / f
    k = 0
    while True:
        nasc = k * T  # instante em que a frente k nasce em x0
        if nasc > dt:
            break
        s = (dt - nasc) * v1
        x = x0 + s
        if x > xb:
            x = xb + (x - xb) / v1 * v2
        if x <= x1:
            M.line(c, x, y0 + 10, x, y1 - 10, cor, a * min(1.0, (dt - nasc) * 3), 7)
        k += 1


def arcos(c, t, t0, cx, cy, lam, vel, rmax, a1, a2, a=1.0, cor=None, largura=6):
    """frentes circulares (arcos de a1 a a2 graus, sentido da tela) saindo de (cx, cy) e crescendo com vel px/s"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    desl = (vel * (t - t0)) % lam
    r = desl
    while r < rmax:
        if r > 8:
            al = a * min(1.0, (rmax - r) / (0.35 * rmax)) * min(1.0, r / 40)
            c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), a1, a2 - a1, False, M.paint(cor, al, stroke=largura))
        r += lam


def boneco(c, x, y, s, a=1.0, cor=None):
    """pessoa de pé com os pés em y"""
    if a <= 0:
        return
    cor = cor or TINTA
    M.rrect(c, x - s * 0.3, y - s * 1.55, s * 0.6, s * 1.0, s * 0.25, cor, a)
    M.line(c, x - s * 0.15, y - s * 0.6, x - s * 0.18, y, cor, a, s * 0.2)
    M.line(c, x + s * 0.15, y - s * 0.6, x + s * 0.18, y, cor, a, s * 0.2)
    c.drawCircle(x, y - s * 1.85, s * 0.3, M.paint(cor, a))


def muro(c, x, y_chao, h, w=60, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - w / 2, y_chao - h, w, h, 6, TINTA2, a)
    for yy in range(int(y_chao - h + 30), int(y_chao), 40):
        M.line(c, x - w / 2, yy, x + w / 2, yy, "#FFFFFF", 0.35 * a, 3)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        yc = 820
        q = ep(t, C["s01.a"], 0.5)
        if t >= C["s01.a"]:
            F.chao(c, 760, 1820, yc, q)
        # som: arcos saindo da pessoa da direita, contornando o muro (desenhados antes, o muro fica por cima)
        arcos(c, t, C["s01.a"] + 0.6, 1560, yc - 200, 70, 90, 620, 120, 300, ep(t, C["s01.a"] + 0.6, 0.5), largura=5)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: (muro(c, 1300, yc, 420, 70, a), boneco(c, 1560, yc, 110, a, E.COR), boneco(c, 1000, yc, 110, a)))
        E.frase(c, t, C["s01.a"], ps("você", "i", 76) + [("ouve", "g", 76, CERTO)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("mas não", "i", 76) + [("vê", "g", 76, ERRADO)], XE, 420, passo=0.12)
        E.frase(c, t, C["s01.c"], [("som:", "g", 66), ("contorna", "g", 66, COR)], XE, 600, passo=0.12)
        E.frase(c, t, C["s01.d"], [("luz:", "g", 66), ("quase", "i", 70), ("nada", "g", 66, ERRADO)], XE, 710, passo=0.12)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "não vê", 1000, 900, 46, "b", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.d"] + 1.2, [("por", "i", 90), ("quê?", "g", 90, COR)], XE, 900, passo=0.15)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, nome) in enumerate((("s02.b", "bate e volta", "reflexão"), ("s02.c", "troca de meio", "refração"), ("s02.d", "passa por uma fresta", "difração"))):
        y = 460 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "i", 66)], XE + 110, y)
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, XE + 110, y + 70, 54, "g", COR, a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def eq(a, x, y):
        n = 60
        F.poli(c, [(x - 130 + 250 * i / n, y - 40 * math.sin(2 * math.pi * 250 * i / n / 110)) for i in range(n + 1)], 1.0, E.COR, a, 6)

    def snell(a, x, y):
        M.line(c, x - 140, y, x + 120, y, TINTA, a, 4)
        M.line(c, x, y - 90, x, y + 90, TINTA2, 0.6 * a, 3, dash=E.TRACO)
        F.poli(c, [(x - 90, y - 90), (x, y), (x + 40, y + 90)], 1.0, E.COR, a, 5)
    lembrete2(c, t, C, "s03", (("s03.b", "a equação da onda,", "v = λ · f"), ("s03.c", "a lei de Snell e a", "normal, a 90° da fronteira")), (eq, snell))


# ---------------- reflexão ----------------
def b_reflexao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("reflexão:", "g", 84, COR)] + ps("bate e volta", "i", 84), XE, 230, passo=0.12)
        # parede vertical à direita; raio chega inclinado e volta com o mesmo ângulo
        Px, Py = 1500, 560
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: F.parede(c, Px, 300, 820, 1, a))
        F.normal(c, t, C["s04.a"] + 0.6, (Px, Py), 0, 380)
        F.raio(c, t, C["s04.a"] + 0.9, [(Px - 380, Py - 230), (Px, Py), (Px - 380, Py + 230)], d=1.4)
        pilula(c, t, C["s04.b"], "eco = som refletido", XE + 300, 380, 50, TINTA)
        E.frase(c, t, C["s04.c"], [("mesmo", "i", 70), ("meio:", "g", 70)], XE, 540, passo=0.12)
        for i, s in enumerate(("v igual", "f igual", "λ igual")):
            E.foco(c, t, C["s04.c"] + 0.6 + 0.4 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 120 + i * 250, 640, 50, "g", fundo=E.COR if s.startswith("f") else TINTA, a=a))
        if t >= C["s04.d"]:
            E.angulo(c, t, C["s04.d"], (Px, Py), (Px - 300, Py), (Px - 380, Py - 230), "i", r=110, size=50)
            E.angulo(c, t, C["s04.d"] + 0.3, (Px, Py), (Px - 300, Py), (Px - 380, Py + 230), "r", r=110, size=50)
            E.frase(c, t, C["s04.d"] + 0.5, [("chegada", "i", 70), ("=", "g", 70, COR), ("saída", "i", 70)], XE, 820, passo=0.15)
        return
    E.frase(c, t, C["s05"], ps("o eco", "i", 84), XE, 220)
    yc = 760
    E.foco(c, t, C["s05"] + 0.3, 0.4, lambda a: (boneco(c, 380, yc, 110, a, E.COR), F.chao(c, 250, 1700, yc, a), muro(c, 1640, yc, 480, 90, a)))
    E.foco(c, t, C["s05.a"], 0.5, lambda a: F.medida(c, 340, "m/s", XE + 330, 220, 84, COR, a))
    if t >= C["s05.b"]:
        q = ep(t, C["s05.b"], 0.6)
        M.line(c, 380, yc + 60, lerp(380, 1595, q), yc + 60, TINTA2, 1.0, 4)
        E.foco(c, t, C["s05.b"] + 0.4, 0.4, lambda a: F.medida(c, 170, "m", 990, yc + 130, 70, TINTA, a, "center"))
    if t >= C["s05.c"]:
        F.seta(c, 480, 420, lerp(480, 1580, ep(t, C["s05.c"], 0.8)), 420, COR, 1.0, 9)
        if t >= C["s05.c"] + 0.8:
            F.seta(c, 1580, 520, lerp(1580, 480, ep(t, C["s05.c"] + 0.8, 0.8)), 520, COR, 1.0, 9)
        E.foco(c, t, C["s05.c"] + 1.0, 0.4, lambda a: E.pilula(c, "vai e volta: 340 m", 1030, 610, 50, "g", fundo=TINTA, a=a))
    bola_txt(c, t, C["s05.d"], "1 s", 1030, 320, 90, 70)


# ---------------- refração ----------------
def tanque(c, x0, xb, x1, y0, y1, a=1.0):
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, xb, y1), M.paint(FUNDO_AGUA, a))
    c.drawRect(skia.Rect.MakeLTRB(xb, y0, x1, y1), M.paint(RASO_AGUA, a))
    M.line(c, xb, y0, xb, y1, TINTA2, 0.6 * a, 3, dash=E.TRACO)


def b_refracao(c, t, C, b):
    x0, xb, x1, y0, y1 = 170, 960, 1750, 560, 900
    if t < C["s08"]:
        E.frase(c, t, C["s06.a"], [("refração:", "g", 84, COR)] + ps("troca de meio", "i", 84), XE, 220, passo=0.12)
        E.frase(c, t, C["s06.b"], [("a", "i", 70), ("velocidade", "g", 70), ("muda", "g", 70, COR)], XE, 340, passo=0.12)
        if t >= C["s06.c"]:
            q = ep(t, C["s06.c"], 0.5)
            tanque(c, x0, xb, x1, y0, y1, q)
            E.foco(c, t, C["s06.c"] + 0.3, 0.4, lambda a: (E.escreve(c, "fundo: mais rápida", x0 + 20, y0 - 25, 46, "b", TINTA, a),
                                                         E.escreve(c, "raso: mais lenta", xb + 20, y0 - 25, 46, "b", TINTA, a)))
            frentes_tanque(c, t, C["s06.c"] + 0.3, x0, xb, x1, y0, y1, 200, 100, 1.0, q)
        if t >= C["s07"]:
            E.frase(c, t, C["s07.a"], [("f", "g", 80, COR), ("não muda", "g", 80, CERTO)], 1100, 340, passo=0.12)
            pilula(c, t, C["s07.b"], "quem decide é a fonte", 1340, 430, 42, TINTA, "b")
            E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "toda crista passa", xb + 20, y1 + 70, 50, "i", TINTA2, a))
            E.frase(c, t, C["s07.d"], [("muda", "i", 70), ("o", "i", 70), ("λ", "g", 76, COR)], XE, 1010, passo=0.12)
        return
    if t < C["s09"]:
        tanque(c, x0, xb, x1, y0, y1, 1.0)
        frentes_tanque(c, t, C["s08"], x0, xb, x1, y0, y1, 200, 100, 1.0, ep(t, C["s08"], 0.5))
        col = ((x0 + 40, "s08.a", "s08.b", "s08.c", "fundo", "0,4", "0,2"), (xb + 40, "s08.a", "s08.d", "s08.e", "raso", "0,2", "0,1"))
        for x, kf, kv, kl, nome, v, lam in col:
            E.foco(c, t, C[kv], 0.4, lambda a, x=x, nome=nome: E.escreve(c, nome, x, 200, 60, "g", TINTA, a))
            E.foco(c, t, C[kf], 0.4, lambda a, x=x: (E.escreve(c, "f =", x, 290, 60, "g", TINTA, a), F.medida(c, 2, "Hz", x + 120, 290, 60, COR, a)))
            E.foco(c, t, C[kv], 0.4, lambda a, x=x, v=v: (E.escreve(c, "v =", x, 380, 60, "g", TINTA, a), F.medida(c, v, "m/s", x + 120, 380, 60, TINTA, a)))
            E.foco(c, t, C[kl], 0.4, lambda a, x=x, lam=lam: (E.escreve(c, "λ =", x, 470, 60, "g", TINTA, a), F.medida(c, lam, "m", x + 120, 470, 60, COR, a)))
        pilula(c, t, C["s08.f"], "metade de v, metade de λ", W / 2, 990, 54, E.COR)
        return
    # s09: chegando inclinada
    E.frase(c, t, C["s09.a"], ps("chegando", "i", 76) + [("inclinada", "g", 76)], XE, 220, passo=0.12)
    Px, Py = 1330, 560
    E.foco(c, t, C["s09.a"], 0.4, lambda a: (c.drawRect(skia.Rect.MakeLTRB(960, 300, 1780, Py), M.paint(FUNDO_AGUA, 0.6 * a)),
                                             c.drawRect(skia.Rect.MakeLTRB(960, Py, 1780, 860), M.paint(RASO_AGUA, a)),
                                             M.line(c, 960, Py, 1780, Py, TINTA, a, 4),
                                             E.escreve(c, "rápido", 980, 350, 46, "b", TINTA2, a), E.escreve(c, "lento", 980, 840, 46, "b", TINTA2, a)))
    F.normal(c, t, C["s09.a"] + 0.3, (Px, Py), 90, 260)
    F.raio(c, t, C["s09.b"], [(Px - 240, Py - 240), (Px, Py), (Px + 100, Py + 240)], d=1.2)
    E.frase(c, t, C["s09.b"], [("lento:", "g", 60), ("aproxima", "g", 60, COR)] + ps("da normal", "i", 60), XE, 420, passo=0.1)
    E.frase(c, t, C["s09.c"], [("rápido:", "g", 60), ("afasta", "g", 60, COR)] + ps("da normal", "i", 60), XE, 530, passo=0.1)
    if t >= C["s09.d"]:
        F.raio(c, t, C["s09.d"], [(Px + 300, 300), (Px + 300, 860)], d=0.8, cor=TINTA)
        E.frase(c, t, C["s09.d"], [("na", "i", 60), ("normal:", "g", 60), ("segue", "i", 60), ("reto", "g", 60, COR)], XE, 700, passo=0.1)


# ---------------- difração ----------------
def b_difracao(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("difração:", "g", 84, COR)] + ps("contorna e se espalha", "i", 76), XE, 220, passo=0.12)
        xf, yc, hf = 1000, 640, 90
        q = ep(t, C["s10.a"], 0.5)
        if t >= C["s10.a"]:
            M.rrect(c, xf - 18, 330, 36, yc - hf / 2 - 330, 6, TINTA, q)
            M.rrect(c, xf - 18, yc + hf / 2, 36, 950 - yc - hf / 2, 6, TINTA, q)
            lam, vel = 70, 80
            desl = (vel * (t - C["s10.a"])) % lam
            x = xf - desl
            while x > 250:
                M.line(c, x, 360, x, 920, E.COR, q, 6)
                x -= lam
            arcos(c, t, C["s10.a"], xf, yc, lam, vel, 560, -80, 80, q)
        E.frase(c, t, C["s10.b"], ps("forte com fresta", "i", 56), XE, 1020, passo=0.1)
        E.foco(c, t, C["s10.b"] + 1.4, 0.4, lambda a: E.formula(c, "≈ λ ou menor", XE + 420, 1020, 60, "g", COR, a))
        return
    E.frase(c, t, C["s11"], [("som", "g", 80, COR)] + ps("x", "i", 70, TINTA2) + [("luz", "g", 80)], XE, 210, passo=0.15)
    yc = 760
    # lado do som (esquerda): muro e arcos que passam por cima
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (F.chao(c, 160, 900, yc, a), muro(c, 520, yc, 300, 50, a), boneco(c, 300, yc, 90, a, E.COR), boneco(c, 760, yc, 90, a)))
    arcos(c, t, C["s11.a"] + 0.3, 300, yc - 170, 90, 110, 330, 200, 360, ep(t, C["s11.a"], 0.5), largura=5)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.formula(c, "λ do som: dezenas de cm a metros", XE, 900, 46, "b", TINTA, a))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "contorna", 520, 1000, 50, "g", fundo=CERTO, a=a))
    # lado da luz (direita): raios retos e sombra atrás do muro
    if t >= C["s11.c"]:
        q = ep(t, C["s11.c"], 0.5)
        F.chao(c, 1020, 1800, yc, q)
        lx, ly = 1070, 400
        c.drawCircle(lx, ly, 40, M.paint("#FFC400", q))
        mx, mt = 1400, yc - 300
        p = skia.Path(); p.moveTo(mx + 25, mt); p.lineTo(1800, mt + (1800 - mx) * (mt - ly) / (mx - lx)); p.lineTo(1800, yc); p.lineTo(mx + 25, yc); p.close()
        c.drawPath(p, M.paint(TINTA, 0.18 * ep(t, C["s11.d"], 0.6)))
        muro(c, mx, yc, 300, 50, q)
        for k in range(5):
            yy = lerp(ly + 60, yc, k / 4)
            F.raio(c, t, C["s11.c"] + 0.1 * k, [(lx + 40, ly + 10), (lx + 40 + (mx - 25 - lx - 40), yy)], d=0.6, setas=False, largura=4)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.formula(c, "λ da luz: menos de 0,001 mm", 1030, 900, 46, "b", TINTA, a))
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "sombra", 1640, 1000, 50, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("na refração, a frequência muda?", "i", 64), XE, 320, passo=0.1)
    # dois meios: lento à esquerda, rápido à direita, mesma frequência
    xb = 960
    E.foco(c, t, C["s12.a"] + 0.5, 0.4, lambda a: (c.drawRect(skia.Rect.MakeLTRB(170, 440, xb, 760), M.paint(RASO_AGUA, a)),
                                                  c.drawRect(skia.Rect.MakeLTRB(xb, 440, 1750, 760), M.paint(FUNDO_AGUA, a)),
                                                  E.escreve(c, "mais lento", 190, 490, 44, "b", TINTA2, a), E.escreve(c, "mais rápido", xb + 20, 490, 44, "b", TINTA2, a)))
    if t >= C["s12.a"] + 0.5:
        n = 600
        pts = []
        for i in range(n + 1):
            x = lerp(170, 1750, i / n)
            ph = (x - 170) / 130 if x < xb else (xb - 170) / 130 + (x - xb) / 260
            pts.append((x, 620 - 70 * math.sin(2 * math.pi * ph)))
        F.poli(c, pts, ep(t, C["s12.a"] + 0.7, 1.0), E.COR, 1.0, 7)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "f aumentou?", xb + 60, 860, 70, "g", ERRADO, a)))
    if t >= C["s12.b"] + 0.8:
        E.risco(c, xb + 50, 870, xb + 480, 800, t, C["s12.b"] + 0.8, largura=10)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "λ aumentou", 300, 860, 70, "g", CERTO, a))
    E.frase(c, t, C["s12.d"], [("f", "g", 64, COR), ("é", "i", 66), ("da", "i", 66), ("fonte", "g", 64)] + ps("e a fonte não mudou", "i", 66), W / 2, 1000, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
    for i, s in enumerate(("reflexão", "refração", "difração")):
        E.foco(c, t, C["s13.a"] + 0.4 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, 520 + i * 440, 330, 58, "g", fundo="#3A3A48", a=a, cor=BR))
    E.frase(c, t, C["s13.a"] + 1.4, [("f", "g", 96, CLARO), ("não muda", "g", 90, BR), ("nos três", "i", 90, CLARO)], W / 2, 500, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("v", "g", 90, BR), ("e", "i", 90, CLARO), ("λ", "g", 90, BR)] + ps("andam juntos", "i", 80, CLARO), W / 2, 680, "center", 0.12)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.pilula(c, "v ×3", W / 2 - 200, 810, 64, "g", fundo=E.COR, a=a, cor=BR),
                                             F.seta(c, W / 2 - 90, 810, W / 2 + 90, 810, CLARO, a, 7),
                                             E.pilula(c, "λ ×3", W / 2 + 200, 810, 64, "g", fundo=CERTO, a=a, cor=BR)))
    E.frase(c, t, C["s13.d"], ps("já tem f e o novo v?", "i", 56, CLARO) + [("v = λ · f", "g", 56, BR)] + ps("direto", "i", 56, CLARO), W / 2, 980, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("som", "i", 76)], XE, 350)
    E.foco(c, t, C["s14.a"] + 0.3, 0.5, lambda a: F.medida(c, 500, "Hz", XE + 200, 350, 90, COR, a))
    E.frase(c, t, C["s14.a"] + 1.2, [("ar:", "g", 70)], XE, 480)
    E.foco(c, t, C["s14.a"] + 1.6, 0.5, lambda a: F.medida(c, 340, "m/s", XE + 160, 480, 80, TINTA, a))
    E.frase(c, t, C["s14.b"], [("água:", "g", 70)], XE, 600)
    E.foco(c, t, C["s14.b"] + 0.6, 0.5, lambda a: F.medida(c, "1.500", "m/s", XE + 220, 600, 80, TINTA, a))
    E.frase(c, t, C["s14.c"], ps("na água:", "i", 70) + [("f?", "g", 80, COR), ("λ?", "g", 80, COR)], XE, 780, passo=0.15)
    if t < C["s15"]:
        if t >= C["s14.a"]:
            q = ep(t, C["s14.a"], 0.5)
            c.drawRect(skia.Rect.MakeLTRB(1100, 600, 1800, 900), M.paint(FUNDO_AGUA, q))
            M.line(c, 1100, 600, 1800, 600, TINTA, q, 4)
            arcos(c, t, C["s14.a"], 1450, 380, 60, 90, 500, 0, 180, q)
            E.foco(c, t, C["s14.a"], 0.4, lambda a: E.bola(c, 1450, 380, 30, a=a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16.a"], [("f", "g", 90, COR), ("não muda:", "g", 76)], XE, 240, passo=0.12)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: F.medida(c, 500, "Hz", XE + 560, 240, 100, CERTO, a))
    E.formula_em(c, t, C["s16.c"], "λ = f{v}{f}", XE, 460, 100, "g", TINTA2)
    conta(c, t, [(C["s16.d"], "λ = 1.500 ÷ 500")], XE, 650, 160, 100)
    bola_txt(c, t, C["s16.e"], "3 m", 1400, 520, 150, 90)
    E.foco(c, t, C["s16.f"], 0.5, lambda a: (E.escreve(c, "no ar:", XE, 880, 64, "i", TINTA2, a),
                                             E.formula(c, "λ = 340 ÷ 500 = 0,68 m", XE + 200, 880, 64, "g", TINTA2, a)))
    E.frase(c, t, C["s16.f"] + 1.4, [("v", "g", 60, COR), ("maior,", "i", 64), ("λ", "g", 60, COR), ("maior", "i", 64)], XE, 990, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s17.a", [("reflexão:", "g", 70), ("volta", "i", 70)]),
                 ("s17.b", [("refração:", "g", 70), ("mudam", "i", 70), ("v", "g", 70, COR), ("e", "i", 70), ("λ", "g", 70, COR)]),
                 ("s17.c", [("difração:", "g", 70), ("contorna", "i", 70)]),
                 ("s17.d", [("f", "g", 70, COR), ("não muda", "g", 70, CERTO)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], ps("duas ondas se", "i", 90) + [("encontram", "g", 96, COR)], XE, 400, passo=0.12)
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "reforço", XE + 150, 560, 56, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.pilula(c, "cancelamento", XE + 560, 560, 56, "g", fundo=ERRADO, a=a))
    F.onda(c, t, C["s18.b"], XE, 1250, 760, 60, 260, d=1.0)
    F.onda(c, t, C["s18.c"], XE, 1250, 760, -60, 260, d=1.0, cor=F.NEG, eixo=False)
    E.foco(c, t, C["s18.c"] + 0.8, 0.5, lambda a: (M.line(c, XE, 920, 1250, 920, TINTA, a, 7), E.escreve(c, "a soma: zero", XE, 1000, 50, "b", TINTA, a)))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.d"] + 0.2, 0.4))
    E.frase(c, t, C["s18.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reflexao=b_reflexao, refracao=b_refracao, difracao=b_difracao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
