"""Visual — Estudativo · FIS-OND-002: ondas, tipos e a equação v = λ·f.
Linguagem visual da trilha Ondas e Som: docstring do visual.py da FIS-OND-001 (onda laranja sobre eixo tracejado,
crista/vale em itálico cinza, A = seta do eixo à crista, λ = cota de crista a crista com a letra na grotesca pesada,
onda longitudinal = faixas que se apertam, conta em pilha com o resultado na esfera)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-002_ondas_tipos_e_equacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("onda", "tipos", "desenho", "equacao", "sismo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 0.5 * 4 == 2                      # corda: λ = 0,5 m, f = 4 Hz → 2 m/s
assert 4000 / 2 == 2000                  # onda S: 4.000 m/s, 2 Hz → λ = 2.000 m = 2 km
assert 10 / 2 == 5                       # crista a vale = 2A → A = 5 cm
assert 60 / 2 == 30                      # 1ª à 3ª crista = 2λ → λ = 30 cm = 0,3 m
assert abs(0.3 * 5 - 1.5) < 1e-12        # v = 0,3 · 5 = 1,5 m/s


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
    """resposta na esfera: "2 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    """conta em pilha: linhas = [(instante, fórmula[, cor])]; a linha da vez fica laranja até a próxima chegar"""
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) desenha à direita da caixa"""
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


def senoide(c, x0, x1, y, A, lam, fase=0.0, cor=None, a=1.0, largura=7, eixo=True):
    """senoide parada (a onda num instante): crista em x0 + lam/4 + fase"""
    if a <= 0:
        return
    if eixo:
        M.line(c, x0 - 20, y, x1 + 20, y, TINTA, 0.35 * a, 3, dash=E.TRACO)
    n = max(2, int((x1 - x0) / 4))
    pts = [(x0 + (x1 - x0) * i / n, y - A * math.sin(2 * math.pi * ((x1 - x0) * i / n - fase) / lam)) for i in range(n + 1)]
    F.poli(c, pts, 1.0, cor or E.COR, a, largura)


def longitudinal(c, t, t0, x0, x1, y, h, lam, amp, vel, n=34, a=1.0, cor=None):
    """onda longitudinal: faixas verticais que se apertam (compressão) e se afastam, andando para a direita"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.5) * a
    desl = vel * max(0.0, t - t0)
    for i in range(n):
        xe = x0 + (x1 - x0) * i / (n - 1)
        x = xe - amp * math.sin(2 * math.pi * (xe - x0 - desl) / lam)
        M.line(c, x, y - h / 2, x, y + h / 2, cor or E.COR, q, 6)


def pessoa(c, x, y, s, sobe, a=1.0, cor=None):
    """torcedor: cabeça e corpo; sobe de 0 a 1 levanta o corpo e os braços"""
    if a <= 0:
        return
    cor = cor or TINTA
    yy = y - s * 0.9 * sobe
    M.rrect(c, x - s * 0.32, yy - s * 1.0, s * 0.64, s * 1.0 + s * 0.9 * sobe, s * 0.25, cor, a)
    c.drawCircle(x, yy - s * 1.3, s * 0.3, M.paint(cor, a))
    if sobe > 0.3:
        for d in (-1, 1):
            M.line(c, x + d * s * 0.28, yy - s * 0.85, x + d * s * 0.5, yy - s * 1.75 * sobe, cor, a, s * 0.16)


def barco(c, x, y, s, ang=0.0, a=1.0):
    """barquinho laranja com a quilha em y"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(ang)
    p = skia.Path()
    p.moveTo(-s, -s * 0.35); p.lineTo(s, -s * 0.35); p.lineTo(s * 0.65, s * 0.12); p.lineTo(-s * 0.65, s * 0.12); p.close()
    c.drawPath(p, M.paint(E.COR, a))
    M.line(c, 0, -s * 0.35, 0, -s * 1.3, TINTA, a, 5)
    v = skia.Path()
    v.moveTo(4, -s * 1.25); v.lineTo(s * 0.7, -s * 0.45); v.lineTo(4, -s * 0.45); v.close()
    c.drawPath(v, M.paint(TINTA2, a))
    c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("no estádio, a", "i", 84) + [("ola", "g", 90, COR)], XE, 260, passo=0.12)
        # arquibancada: 16 torcedores; o pulso anda da esquerda para a direita a partir de s01.b
        n, x0, x1, y = 16, 280, 1640, 760
        q = ep(t, C["s01.a"] + 0.4, 0.6)
        if t >= C["s01.a"] + 0.4:
            M.line(c, x0 - 80, y + 10, x1 + 80, y + 10, TINTA, q, 6)
        pos = lerp(x0 - 300, x1 + 300, ((t - C["s01.b"]) / 3.2) % 1.0) if t >= C["s01.b"] else -9999
        for i in range(n):
            x = lerp(x0, x1, i / (n - 1))
            sobe = math.exp(-((x - pos) / 150) ** 2)
            destaque = i == 7 and t >= C["s01.c"]
            pessoa(c, x, y, 52, sobe, q, E.COR if destaque else TINTA)
        if t >= C["s01.b"]:
            F.seta(c, x0, 420, lerp(x0, x1, ep(t, C["s01.b"], 0.8)), 420, COR, 1.0, 8)
            E.foco(c, t, C["s01.b"] + 0.4, 0.4, lambda a: E.escreve(c, "a onda anda", x0, 390, 54, "i", COR, a))
        xi = lerp(x0, x1, 7 / 15)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "não sai do lugar", xi, 900, 46, "b", fundo=E.COR, a=a))
        E.frase(c, t, C["s01.d"], ps("cada pessoa só", "i", 64) + [("levanta e senta", "g", 64)], W / 2, 1010, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.a", "classificar", 1.2), ("s02.b", "ler A e λ", 0), ("s02.c", "v = λ · f", 0))
    for i, (k, s, dt) in enumerate(itens):
        y = 460 + i * 170
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.foco(c, t, C[k] + dt + 0.1, 0.5, lambda a, s=s, i=i, y=y: E.formula(c, s, XE + 110, y, 84, "g", COR if i == 2 else TINTA, a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def osc(a, x, y):
        F.pendulo(c, 99, 0, x + 40, y - 105, 120, 18 * math.sin(t * 2.6), r=20)

    def seno(a, x, y):
        senoide(c, x - 120, x + 110, y, 40, 115, 0, a=a, largura=6)
    lembrete2(c, t, C, "s03", (("s03.b", "a oscilação:", "A, T e f"), ("s03.c", "o gráfico do seno,", "sobe e desce")), (osc, seno))


# ---------------- o que é onda ----------------
def b_onda(c, t, C, b):
    E.frase(c, t, C["s04"], [("onda", "g", 110, COR)], XE, 230)
    E.frase(c, t, C["s04.a"], ps("uma sacudida que", "i", 70) + [("viaja", "g", 70)], XE + 340, 230, passo=0.12)
    if t < C["s04.d"]:
        def mar():
            y, A, lam = 640, 55, 520
            vel = 160
            F.onda(c, t, C["s04.a"], 120, 1800, y, A, lam, d=1.0, velocidade=vel)
            if t >= C["s04.b"]:  # barco preso no x = 1100: só sobe e desce
                xb = 1100
                desl = vel * (t - C["s04.a"])
                yy = y - A * math.sin(2 * math.pi * (xb - 120 - desl) / lam)
                incl = -math.degrees(math.atan(A * 2 * math.pi / lam * math.cos(2 * math.pi * (xb - 120 - desl) / lam))) * 0.5
                E.foco(c, t, C["s04.b"], 0.5, lambda a: barco(c, xb, yy, 70, incl, a))
                E.frase(c, t, C["s04.b"], ps("leva", "i", 66) + [("energia", "g", 66, COR)], XE, 380, passo=0.12)
            if t >= C["s04.c"]:
                M.line(c, 1100, 520, 1100, 760, TINTA2, 0.6 * ep(t, C["s04.c"], 0.4), 4, dash=E.TRACO)
                E.frase(c, t, C["s04.c"], ps("não leva a", "i", 66) + [("matéria", "g", 66, ERRADO)], XE, 900, passo=0.12)
                E.foco(c, t, C["s04.c"] + 1.0, 0.4, lambda a: E.pilula(c, "o barco fica no lugar", 1100, 860, 44, "b", fundo=TINTA, a=a))
        E.saida(c, t, C["s04.d"] - 0.1, mar)
        return
    # a corda: um ponto marcado só sobe e desce, a forma anda
    y, A, lam, vel = 620, 90, 460, 150
    F.onda(c, t, C["s04.d"], 160, 1760, y, A, lam, d=0.6, velocidade=vel)
    xp = 900
    desl = vel * (t - C["s04.d"])
    yp = y - A * math.sin(2 * math.pi * (xp - 160 - desl) / lam)
    M.line(c, xp, y - A - 40, xp, y + A + 40, TINTA2, 0.5, 3, dash=E.TRACO)
    E.bola(c, xp, yp, 26, TINTA, ep(t, C["s04.d"], 0.4))
    E.frase(c, t, C["s04.d"], ps("cada ponto só", "i", 66) + [("sobe e desce", "g", 66)], XE, 380, passo=0.12)
    if t >= C["s04.e"]:
        F.seta(c, 700, 900, lerp(700, 1300, ep(t, C["s04.e"], 0.6)), 900, COR, 1.0, 9)
        E.frase(c, t, C["s04.e"], ps("o", "i", 66) + [("formato", "g", 66, COR)] + ps("é que anda", "i", 66), XE, 1000, passo=0.12)


# ---------------- tipos ----------------
def b_tipos(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("1.", "g", 84, COR), ("a", "i", 88), ("natureza", "g", 84)], XE, 220, passo=0.12)
        x1, x2, w, y, h = 170, 1000, 750, 320, 640
        for x, k in ((x1, "s05.b"), (x2, "s05.d")):
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C["s05.b"], [("mecânica", "g", 70, COR)], x1 + 50, y + 100)
        E.frase(c, t, C["s05.b"] + 0.5, ps("precisa de um meio", "i", 54), x1 + 50, y + 180, passo=0.1)
        for i, s in enumerate(("corda", "água", "ar")):
            E.foco(c, t, C["s05.b"] + 1.4 + 0.3 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, x1 + 120 + i * 200, y + 280, 44, "b", fundo=TINTA, a=a))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: (E.escreve(c, "vácuo:", x1 + 50, y + 450, 58, "i", TINTA, a), E.escreve(c, "sem som", x1 + 260, y + 450, 58, "g", ERRADO, a)))
        F.onda(c, t, C["s05.b"] + 0.3, x1 + 60, x1 + w - 60, y + 560, 30, 170, d=0.8, velocidade=80)
        E.frase(c, t, C["s05.d"], [("eletromagnética", "g", 62, COR)], x2 + 50, y + 100)
        E.frase(c, t, C["s05.d"] + 0.6, ps("anda até no vácuo", "i", 54), x2 + 50, y + 180, passo=0.1)
        for i, s in enumerate(("luz do Sol", "rádio")):
            E.foco(c, t, C["s05.d"] + 1.6 + 0.4 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, x2 + 170 + i * 300, y + 280, 44, "b", fundo=E.COR, a=a))
        E.foco(c, t, C["s05.d"] + 2.6, 0.5, lambda a: E.escreve(c, "do que é feita: outra aula", x2 + 50, y + 450, 46, "i", TINTA2, a))
        F.onda(c, t, C["s05.d"] + 0.3, x2 + 60, x2 + w - 60, y + 560, 30, 120, d=0.8, velocidade=80)
        return
    E.frase(c, t, C["s06.a"], [("2.", "g", 84, COR), ("a", "i", 88), ("direção", "g", 84), ("da", "i", 88), ("vibração", "g", 84)], XE, 200, passo=0.12)
    # transversal: corda + seta da vibração vertical e da propagação horizontal
    y1 = 420
    E.frase(c, t, C["s06.b"], [("transversal", "g", 66, COR)], XE, y1 - 90)
    E.foco(c, t, C["s06.b"] + 0.5, 0.4, lambda a: E.escreve(c, "vibra em ângulo reto", XE, y1 - 30, 46, "i", TINTA2, a))
    F.onda(c, t, C["s06.b"], 820, 1750, y1, 70, 310, d=0.8, velocidade=140)
    if t >= C["s06.b"] + 1.0:
        q = ep(t, C["s06.b"] + 1.0, 0.4)
        F.seta(c, 760, y1 + 60, 760, y1 - 80, TINTA, q, 7)
        F.seta(c, 760, y1 - 60, 760, y1 + 80, TINTA, q, 7)
        F.seta(c, 1450, y1 + 130, 1700, y1 + 130, COR, q, 7)
    # longitudinal: faixas que se apertam
    y2 = 800
    E.frase(c, t, C["s06.c"], [("longitudinal", "g", 66, COR)], XE, y2 - 90)
    E.foco(c, t, C["s06.c"] + 0.6, 0.4, lambda a: E.escreve(c, "vibra na direção do caminho", XE, y2 - 30, 46, "i", TINTA2, a))
    longitudinal(c, t, C["s06.c"], 820, 1750, y2, 170, 310, 22, 140)
    if t >= C["s06.c"] + 1.0:
        q = ep(t, C["s06.c"] + 1.0, 0.4)
        F.seta(c, 720, y2 + 120, 800, y2 + 120, TINTA, q, 7)
        F.seta(c, 800, y2 + 150, 720, y2 + 150, TINTA, q, 7)
        F.seta(c, 1450, y2 + 130, 1700, y2 + 130, COR, q, 7)
    pilula(c, t, C["s06.d"], "mola que aperta e estica", 1290, y2 - 140, 40, TINTA, "b")
    pilula(c, t, C["s06.e"], "som: o ar vai e volta", XE + 240, y2 + 60, 44, E.COR)


# ---------------- desenho ----------------
def b_desenho(c, t, C, b):
    x0, x1, y, A, lam = 170, 1750, 560, 150, 560
    if t < C["s08"]:
        E.frase(c, t, C["s07"], ps("o desenho da onda", "i", 76), XE, 170, passo=0.12)
        cr = F.onda(c, t, C["s07"] + 0.2, x0, x1, y, A, lam, d=1.0, tl=C["s07.d"], ta=C["s07.c"], size=80)
        if cr:
            E.foco(c, t, C["s07.a"], 0.4, lambda a: E.centro(c, "crista", cr[-1], y - A - 34, 50, "i", TINTA2, a))
            E.foco(c, t, C["s07.b"], 0.4, lambda a: E.centro(c, "vale", cr[0] + lam / 2, y + A + 70, 50, "i", TINTA2, a))
            for k, xc in enumerate(cr):
                E.foco(c, t, C["s07.a"] + 0.1 * k, 0.3, lambda a, xc=xc: c.drawCircle(xc, y - A, 14, M.paint(E.COR, a)))
                E.foco(c, t, C["s07.b"] + 0.1 * k, 0.3, lambda a, xc=xc: c.drawCircle(xc + lam / 2, y + A, 14, M.paint(TINTA, a)) if xc + lam / 2 < x1 else None)
        E.frase(c, t, C["s07.c"] + 0.4, [("amplitude", "i", 60), ("A:", "g", 60, COR)] + ps("do meio à crista", "i", 60), XE, 900, passo=0.1)
        E.frase(c, t, C["s07.e"], [("comprimento de onda", "i", 60), ("λ:", "g", 60, COR)] + ps("de crista a crista", "i", 60), XE, 990, passo=0.1)
        return
    # s08: frequência e período: a mão balança a ponta da corda
    E.frase(c, t, C["s08.a"], [("frequência", "i", 76), ("f:", "g", 76, COR)] + ps("oscilações por segundo", "i", 60), XE, 220, passo=0.12)
    E.foco(c, t, C["s08.a"] + 1.4, 0.4, lambda a: E.pilula(c, "hertz (Hz)", XE + 240, 320, 46, "b", fundo=TINTA, a=a))
    yy, lam2, A2, vel = 640, 360, 90, 220
    F.onda(c, t, C["s08.a"], 380, 1750, yy, A2, lam2, d=0.6, velocidade=vel)
    if t >= C["s08.b"]:
        desl = vel * (t - C["s08.a"])
        ym = yy - A2 * math.sin(2 * math.pi * (0 - desl) / lam2)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: (M.rrect(c, 330, ym - 50, 70, 100, 20, E.COR, a), E.escreve(c, "a fonte", 260, ym - 80, 50, "i", COR, a)))
    E.frase(c, t, C["s08.c"], [("período", "i", 70), ("T:", "g", 70, COR)] + ps("o tempo de uma oscilação", "i", 60), XE, 920, passo=0.12)
    E.foco(c, t, C["s08.c"] + 0.4, 0.5, lambda a: F.cronometro(c, 1640, 900, 70, 15, a, ""))


# ---------------- equação ----------------
def b_equacao(c, t, C, b):
    if t < C["s10"]:
        def s09():
            # a onda anda um λ enquanto o ponto faz uma oscilação
            x0, y, A, lam = 200, 400, 90, 500
            T = 2.4
            if t >= C["s09"]:
                fr = min(1.0, max(0.0, (t - C["s09.a"]) / T)) if t >= C["s09.a"] else 0.0
                senoide(c, x0, 1700, y, A, lam, fase=lam * fr, a=ep(t, C["s09"], 0.5))
                xc0 = x0 + lam / 4
                c.drawCircle(xc0 + lam * fr, y - A, 16, M.paint(E.COR, ep(t, C["s09"], 0.5)))
                if t >= C["s09.a"]:
                    q = ep(t, C["s09.a"], 0.4)
                    M.line(c, xc0, y - A - 20, xc0, y - A - 120, TINTA2, 0.6 * q, 3, dash=E.TRACO)
                    F.seta(c, xc0, y - A - 90, xc0 + lam * fr, y - A - 90, TINTA, q, 6, 22)
                    E.foco(c, t, C["s09.a"] + T, 0.4, lambda a: E._meio(c, "λ", xc0 + lam / 2, y - A - 150, 70, "g", COR, a))
                    E.foco(c, t, C["s09.a"] + 0.2, 0.4, lambda a: (F.cronometro(c, 1600, y + 220, 60, min(60, 60 * fr), a, ""), E.escreve(c, "T", 1690, y + 245, 80, "g", COR, a)))
            E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "v = f{λ}{T}", XE, 820, 120, "g", TINTA, a))
            E.foco(c, t, C["s09.b"] + 0.8, 0.4, lambda a: E.escreve(c, "distância ÷ tempo", XE, 950, 46, "i", TINTA2, a))
            E.foco(c, t, C["s09.c"] - 1.6, 0.5, lambda a: E.formula(c, "f{1}{T} = f", 760, 820, 90, "g", TINTA2, a))
            E.formula_em(c, t, C["s09.c"], "v = λ · f", 1150, 820, 130, "g", COR)
            E.frase(c, t, C["s09.d"], [("λ", "g", 50, COR), ("(m)", "b", 46, F.UNID), ("f", "g", 50, COR), ("(Hz)", "b", 46, F.UNID), ("v", "g", 50, COR), ("(m/s)", "b", 46, F.UNID)],
                    1150, 950, "left", 0.12)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    E.formula_em(c, t, C["s10"], "v = λ · f", XE, 220, 90, "g", TINTA2)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: (E.escreve(c, "λ =", 1150, 200, 72, "g", TINTA, a), F.medida(c, "0,5", "m", 1290, 200, 72, COR, a)))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: (E.escreve(c, "f =", 1150, 300, 72, "g", TINTA, a), F.medida(c, "4", "Hz", 1290, 300, 72, COR, a)))
    F.onda(c, t, C["s10.a"], 200, 1000, 420, 50, 200, d=0.8, velocidade=200 * 1.0)
    conta(c, t, [(C["s10.c"], "v = 0,5 · 4")], XE, 680, 160, 110)
    bola_txt(c, t, C["s10.d"], "2 m/s", 1450, 700, 160, 84)


# ---------------- sísmicas ----------------
def b_sismo(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("nos", "i", 84) + [("terremotos", "g", 84, COR)], XE, 220, passo=0.12)
        x1, x2, w, y, h = 170, 1000, 750, 330, 640
        for x, k in ((x1, "s11.b"), (x2, "s11.c")):
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C["s11.b"], [("onda", "i", 70), ("P", "g", 80, COR)], x1 + 50, y + 100)
        E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: E.escreve(c, "primária", x1 + 330, y + 100, 52, "i", TINTA2, a))
        longitudinal(c, t, C["s11.b"] + 0.3, x1 + 70, x1 + w - 70, y + 260, 130, 160, 14, 160, n=26)
        for i, s in enumerate(("longitudinal", "mais rápida")):
            E.foco(c, t, C["s11.b"] + 1.4 + 0.6 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, x1 + w / 2, y + 430 + i * 100, 44, "b", fundo=E.COR if i else TINTA, a=a))
        E.frase(c, t, C["s11.c"], [("onda", "i", 70), ("S", "g", 80, COR)], x2 + 50, y + 100)
        E.foco(c, t, C["s11.c"] + 0.4, 0.4, lambda a: E.escreve(c, "secundária", x2 + 330, y + 100, 52, "i", TINTA2, a))
        F.onda(c, t, C["s11.c"] + 0.3, x2 + 70, x2 + w - 70, y + 260, 55, 160, d=0.8, velocidade=90)
        for i, s in enumerate(("transversal", "mais lenta", "não passa em líquido")):
            E.foco(c, t, C["s11.c"] + 1.2 + 0.6 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, x2 + w / 2, y + 430 + i * 85, 40, "b", fundo=ERRADO if i == 2 else TINTA, a=a))
        return
    E.formula_em(c, t, C["s12"], "λ = f{v}{f}", XE, 240, 110, "g", TINTA2)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: (E.escreve(c, "v =", 1100, 200, 72, "g", TINTA, a), F.medida(c, "4.000", "m/s", 1240, 200, 72, COR, a)))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "f =", 1100, 300, 72, "g", TINTA, a), F.medida(c, "2", "Hz", 1240, 300, 72, COR, a)))
    conta(c, t, [(C["s12.c"], "λ = 4.000 ÷ 2")], XE, 560, 160, 110)
    bola_txt(c, t, C["s12.d"], "2.000 m", 1450, 640, 175, 74)
    E.foco(c, t, C["s12.d"] + 1.2, 0.4, lambda a: E.pilula(c, "2 km de crista a crista", XE + 470, 800, 56, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    x0, x1, y, A, lam = 200, 1700, 600, 170, 640
    senoide(c, x0, x1, y, A, lam, a=ep(t, C["s13"], 0.5))
    xc = x0 + lam / 4
    xv = xc + lam / 2
    if t >= C["s13.a"]:  # crista a vale na vertical: errado = 2A
        q = ep(t, C["s13.a"], 0.5)
        M.line(c, xc - 80, y - A, xv + 80, y - A, TINTA2, 0.5 * q, 3, dash=E.TRACO)
        M.line(c, xc - 80, y + A, xv + 80, y + A, TINTA2, 0.5 * q, 3, dash=E.TRACO)
        F.seta(c, xv + 70, y, xv + 70, y - A, ERRADO, q, 6, 22)
        F.seta(c, xv + 70, y, xv + 70, y + A, ERRADO, q, 6, 22)
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.pilula(c, "= 2A", xv + 200, y, 64, "g", fundo=ERRADO, a=a))
    if t >= C["s13.c"]:  # crista ao vale na horizontal: λ/2
        q = ep(t, C["s13.c"], 0.5)
        F.seta(c, xc, y + A + 70, xv, y + A + 70, ERRADO, q, 6, 22)
        E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: E._meio(c, "f{λ}{2}", (xc + xv) / 2, y + A + 150, 70, "g", ERRADO, a))
    if t >= C["s13.d"]:
        q = ep(t, C["s13.d"], 0.5)
        F.seta(c, xc, y - A - 70, xc + lam, y - A - 70, CERTO, q, 7, 24)
        F.seta(c, xc + lam, y - A - 70, xc, y - A - 70, CERTO, q, 7, 24)
        E.foco(c, t, C["s13.d"] + 0.3, 0.4, lambda a: E._meio(c, "λ", xc + lam / 2, y - A - 130, 80, "g", CERTO, a))
        E.frase(c, t, C["s13.d"] + 0.8, ps("crista a crista", "i", 60, CERTO), 1400, 980, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
    E.frase(c, t, C["s14.a"], [("f", "g", 84, BR), ("é", "i", 84, CLARO), ("da", "i", 84, CLARO), ("fonte", "g", 84, BR)], W / 2 - 420, 320, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("v", "g", 84, BR), ("é", "i", 84, CLARO), ("do", "i", 84, CLARO), ("meio", "g", 84, BR)], W / 2 + 420, 320, "center", 0.12)
    if t >= C["s14.c"]:
        q = ep(t, C["s14.c"], 0.5)
        F.onda(c, t, C["s14.c"], 260, 1660, 520, 55, 400, d=0.6, escuro=True, cor=CLARO)
        F.onda(c, t, C["s14.c"] + 0.8, 260, 1660, 720, 55, 200, d=0.6, escuro=True)
        E.foco(c, t, C["s14.c"] + 0.3, 0.4, lambda a: E.pilula(c, "f", 160, 520, 56, "g", fundo="#3A3A48", a=a, cor=BR))
        E.foco(c, t, C["s14.c"] + 1.1, 0.4, lambda a: E.pilula(c, "2f", 160, 720, 56, "g", fundo=E.COR, a=a, cor=BR))
        E.foco(c, t, C["s14.c"] + 1.6, 0.4, lambda a: E.formula(c, "λ ÷ 2", 1770, 745, 64, "g", BR, a, "center"))
    E.frase(c, t, C["s14.d"], ps("mão mais rápida:", "i", 60, CLARO) + [("ondas", "g", 60, BR), ("mais", "g", 60, BR), ("curtas", "g", 60, CLARO)], W / 2, 880, "center", 0.1)
    E.frase(c, t, C["s14.e"], [("trocou de meio?", "g", 54, ERRADO)] + ps("aí v muda: próxima aula", "i", 56, CLARO), W / 2, 990, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("1ª à 3ª crista:", "i", 64), XE, 340, passo=0.1)
    E.foco(c, t, C["s15.a"] + 0.8, 0.5, lambda a: F.medida(c, 60, "cm", XE + 470, 340, 84, COR, a))
    E.frase(c, t, C["s15.b"], ps("crista ao vale, na vertical:", "i", 64), XE, 470, passo=0.1)
    E.foco(c, t, C["s15.b"] + 1.2, 0.5, lambda a: F.medida(c, 10, "cm", XE + 760, 470, 84, COR, a))
    E.frase(c, t, C["s15.c"], ps("a fonte:", "i", 64), XE, 600, passo=0.1)
    E.foco(c, t, C["s15.c"] + 0.6, 0.5, lambda a: F.medida(c, 5, "Hz", XE + 260, 600, 84, COR, a))
    E.frase(c, t, C["s15.d"], [("A?", "g", 90, COR), ("λ?", "g", 90, COR), ("v?", "g", 90, COR)], XE, 790, passo=0.3)
    if t < C["s16"]:
        if t >= C["s15.a"]:
            cr = F.onda(c, t, C["s15.a"], 1080, 1800, 640, 60, 300, d=0.8)
            for i, xc in enumerate(cr[:3]):
                E.foco(c, t, C["s15.a"] + 0.6, 0.3, lambda a, i=i, xc=xc: E.centro(c, str(i + 1), xc, 560, 44, "g", COR, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        x0, y, A, lam = 900, 330, 80, 380
        senoide(c, x0, 1800, y, A, lam, a=ep(t, C["s17"], 0.4))
        xc = x0 + lam / 4
        if t >= C["s17.a"]:
            q = ep(t, C["s17.a"], 0.4)
            F.seta(c, xc + lam / 2 + 60, y + A, xc + lam / 2 + 60, y - A, TINTA, q, 6, 20)
            E.foco(c, t, C["s17.a"] + 0.3, 0.4, lambda a: E.pilula(c, "10 cm = 2A", xc + lam / 2 + 230, y, 40, "b", fundo=TINTA, a=a))
        if t >= C["s17.c"]:
            q = ep(t, C["s17.c"], 0.5)
            F.seta(c, xc, y - A - 50, xc + 2 * lam, y - A - 50, TINTA, q, 6, 20)
            F.seta(c, xc + 2 * lam, y - A - 50, xc, y - A - 50, TINTA, q, 6, 20)
            E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: E._meio(c, "60 cm = 2λ", xc + lam, y - A - 100, 48, "b", TINTA2, a))
        conta(c, t, [(C["s17.a"], "A = 10 ÷ 2"), (C["s17.c"], "λ = 60 ÷ 2")], XE, 580, 260, 100)
        bola_txt(c, t, C["s17.b"], "5 cm", 1250, 560, 110, 64)
        bola_txt(c, t, C["s17.d"], "30 cm", 1250, 820, 110, 60)
        E.foco(c, t, C["s17.d"] + 1.2, 0.4, lambda a: E.escreve(c, "= 0,3 m", 1400, 840, 64, "g", TINTA, a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.formula_em(c, t, C["s18"], "v = λ · f", XE, 260, 90, "g", TINTA2)
    conta(c, t, [(C["s18.a"], "v = 0,3 · 5")], XE, 520, 160, 120)
    bola_txt(c, t, C["s18.b"], "1,5 m/s", 1400, 560, 190, 84)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("energia", "g", 66), ("sem", "i", 66), ("matéria", "g", 66)]),
                 ("s19.b", [("mecânica:", "g", 66), ("meio;", "i", 66), ("eletromagnética:", "g", 66), ("vácuo", "i", 66)]),
                 ("s19.c", [("λ:", "g", 66, COR), ("crista", "i", 66), ("a", "i", 66), ("crista", "i", 66)]),
                 ("s19.d", [("v = λ · f", "g", 72, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("a onda encontra", "i", 90), XE, 390, passo=0.12)
    E.frase(c, t, C["s20.a"] + 0.6, [("obstáculos", "g", 110, COR)], XE, 520)
    for i, (k, s) in enumerate((("s20.b", "bate e volta"), ("s20.c", "muda de meio"), ("s20.d", "contorna"))):
        E.foco(c, t, C[k], 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 200 + i * 400, 680, 54, "g", fundo=E.COR if i == 1 else TINTA, a=a))
    F.onda(c, t, C["s20.a"], XE, 1250, 860, 50, 220, d=1.2, velocidade=120)
    E.foco(c, t, C["s20.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.e"] + 0.2, 0.4))
    E.frase(c, t, C["s20.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, onda=b_onda, tipos=b_tipos, desenho=b_desenho, equacao=b_equacao,
              sismo=b_sismo, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
