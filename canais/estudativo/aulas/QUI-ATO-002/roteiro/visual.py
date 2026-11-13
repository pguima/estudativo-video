"""Visual — Estudativo · QUI-ATO-002: modelo de Rutherford, o experimento da folha de ouro.
Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-ATO-001): carga + turquesa e − azul,
um desenho fixo por modelo (pudim de Thomson, núcleo + órbitas de Rutherford), experimento em traço de vidro e metal cinza.
Partícula alfa = bolinha turquesa pequena com "+"; o ponto onde ela bate na tela acende em turquesa claro.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-002_rutherford_folha_de_ouro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("alfa", "resultado", "nuclear", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OURO = "#D8B24A"
PUDIM = E.mix(E.COR, "#FFFFFF", 0.55)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def eletron(c, x, y, r=16, a=1.0):
    E.bola(c, x, y, r, Q.ELETRON, a)
    if r >= 12:
        M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(3, r * 0.16))


def mais(c, x, y, s, cor, a=1.0, w=None):
    w = w or max(3, s * 0.22)
    M.line(c, x - s / 2, y, x + s / 2, y, cor, a, w)
    M.line(c, x, y - s / 2, x, y + s / 2, cor, a, w)


def alfa(c, x, y, r=14, a=1.0):
    """partícula alfa: bolinha turquesa com +"""
    E.bola(c, x, y, r, E.COR, a)
    mais(c, x, y, r * 0.9, BR, a, max(2.5, r * 0.2))


_PE = ((-0.45, -0.35), (0.38, -0.5), (0.05, 0.05), (-0.5, 0.35), (0.48, 0.3), (0.0, 0.62), (-0.1, -0.72))
_PM = ((0.0, -0.4), (-0.6, -0.05), (0.62, -0.1), (-0.28, 0.6), (0.3, 0.68), (0.2, -0.15), (-0.25, 0.1))


def pudim(c, cx, cy, r, a=1.0, cinza=0.0):
    if a <= 0 or r <= 0:
        return
    E.bola(c, cx, cy, r, M.mix(PUDIM, "#C9CCD2", cinza), a)
    for ux, uy in _PM:
        mais(c, cx + ux * r, cy + uy * r, r * 0.13, M.mix(E.COR, "#8A8D96", cinza), a * 0.9)
    for ux, uy in _PE:
        eletron(c, cx + ux * r, cy + uy * r, r * 0.12, a)


def rutherford(c, t, cx, cy, R, a=1.0, rn=None, n=4, gira=0.6):
    """modelo nuclear: núcleo turquesa minúsculo e elétrons em órbitas finas (elipses inclinadas)"""
    if a <= 0:
        return
    rn = rn or R * 0.08
    for k in range(3):
        c.save(); c.translate(cx, cy); c.rotate(k * 60)
        c.drawOval(skia.Rect.MakeXYWH(-R, -R * 0.38, 2 * R, R * 0.76), M.paint(TINTA2, 0.55 * a, stroke=3))
        ang = t * gira * (1 + 0.3 * k) + k * 2
        eletron(c, R * math.cos(ang), R * 0.38 * math.sin(ang), max(9, R * 0.06), a)
        c.restore()
    E.bola(c, cx, cy, rn, E.COR, a)
    if rn >= 14:
        mais(c, cx, cy, rn * 0.9, BR, a)


# trajetórias do experimento: (ângulo final em graus, tipo)
_TRAJ = [(0, "r"), (2, "r"), (-2, "r"), (1, "r"), (0, "r"), (34, "d"), (-1, "r"), (3, "r"), (-28, "d"), (0, "r"), (172, "v"), (-2, "r"), (1, "r"), (0, "r")]


def experimento(c, t, t0, cx, cy, R, ativo, tipos="rdv", a=1.0, previsao=False):
    """fonte à esquerda, folha de ouro no centro (cx, cy), tela circular de raio R; alfas saem em fila a partir de ativo"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    # tela que brilha
    c.drawCircle(cx, cy, R, M.paint(TINTA2, 0.35 * q, stroke=10))
    E.escreve(c, "tela", cx + R * 0.72, cy - R * 0.76, 42, "i", TINTA2, q)
    # fonte radioativa: caixa de chumbo com furo
    fx = cx - R * 0.78
    M.rrect(c, fx - 70, cy - 60, 110, 120, 14, "#3A3B42", q)
    M.rrect(c, fx + 10, cy - 10, 30, 20, 4, E.COR, q)
    centro(c, "fonte", fx - 15, cy + 110, 40, "i", TINTA2, q)
    # folha de ouro
    M.rrect(c, cx - 6, cy - R * 0.42, 12, R * 0.84, 3, OURO, q)
    centro(c, "folha de ouro", cx, cy + R * 0.42 + 54, 42, "i", TINTA2, q)
    if ativo is None or t < ativo:
        return
    x0 = fx + 40
    T = 1.4                       # duração de uma viagem
    for i, (ang, tp) in enumerate(_TRAJ):
        if tp not in tipos:
            continue
        if previsao:
            ang = (i % 5 - 2) * 1.5
        ti = ativo + i * 0.22
        u = (t - ti) / T
        if u < 0:
            continue
        ciclo = int(u)
        u -= ciclo
        if ciclo > 6:
            continue
        dy = ((i * 7) % 9 - 4) * 3
        if u < 0.45:
            px, py = lerp(x0, cx, u / 0.45), cy + dy
        else:
            v = (u - 0.45) / 0.55
            r = R - 10
            g = math.radians(ang)
            px, py = cx + r * v * math.cos(g), cy + dy - r * v * math.sin(g)
            if v > 0.97:
                c.drawCircle(cx + r * math.cos(g), cy + dy - r * math.sin(g), 22, M.paint(E.CLARO, 0.8 * q))
        alfa(c, px, py, 11, q)


def estadio(c, cx, cy, w, h, a=1.0):
    """estádio visto de cima: arquibancada cinza, campo verde e a bolinha de gude no meio"""
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint("#B9BCC2", a))
    c.drawOval(skia.Rect.MakeXYWH(cx - w * 0.4, cy - h * 0.36, w * 0.8, h * 0.72), M.paint("#6DBB6A", a))
    M.line(c, cx, cy - h * 0.36, cx, cy + h * 0.36, BR, a * 0.8, 4)
    c.drawCircle(cx, cy, h * 0.12, M.paint(BR, a * 0.8, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("bolinhas contra", "i", 80) + [("uma folha", "g", 76)], XE, 250, passo=0.12)
        # bolinhas indo contra a folha; algumas voltam
        fx, fy = 1350, 500
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: (M.rrect(c, fx, fy - 220, 22, 440, 4, "#FFFFFF", a, shadow=True), c.drawRect(skia.Rect.MakeXYWH(fx, fy - 220, 22, 440), M.paint(TINTA2, a, stroke=3))))
        for k in range(7):
            ti = C["s01.a"] + 0.6 + k * 0.35
            u = clamp01((t - ti) / 1.0)
            if t < ti:
                continue
            volta = k in (2, 5) and t >= C["s01.b"]
            yy = fy - 180 + k * 60
            if volta:
                v = clamp01((t - max(ti, C["s01.b"])) / 1.0)
                px = lerp(fx - 10, 1040, ease_out(v))
            else:
                px = lerp(1040, fx + 420, u) if k not in (2, 5) else lerp(1040, fx - 10, min(1, u * 1.4))
            alfa(c, px, yy, 16)
        E.frase(c, t, C["s01.b"], ps("e algumas", "i", 80) + [("voltam", "g", 76, COR)], XE, 380, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("no laboratório de", "i", 64, TINTA2), XE, 560, passo=0.1)
        E.frase(c, t, C["s01.c"] + 0.8, [("Ernest", "g", 76), ("Rutherford", "g", 76, COR)], XE, 660, passo=0.15)
        E.frase(c, t, C["s01.d"], ps("isso mudou a imagem do átomo", "i", 64), XE, 860, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("por que a maioria", "i", 70), ("atravessou", "g", 66)]),
                 (C["s02.b"], [("por que algumas", "i", 70), ("voltaram", "g", 66)]),
                 (C["s02.c"], [("o", "i", 70), ("núcleo", "g", 70, COR)])], XE, 460, 170)


def clamp01(v):
    return max(0.0, min(1.0, v))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("Thomson: esfera", "i", 72) + [("positiva", "g", 68, COR)], XE, 340, passo=0.12)
    E.frase(c, t, C["s03.a"] + 1.4, ps("com", "i", 72) + [("elétrons", "g", 68, Q.ELETRON)] + ps("espalhados", "i", 72), XE, 440, passo=0.12)
    E.foco(c, t, C["s03.a"] + 0.4, 0.6, lambda a: pudim(c, 1480, 400, 200 * ease_back(prog(t, C["s03.a"] + 0.4, 0.6)), a))
    for k, (ck, s1, s2, txt) in enumerate((("s03.b", "+", "+", "iguais se repelem"), ("s03.c", "+", "−", "opostas se atraem"))):
        y = 700 + k * 170
        F.carga(c, t, C[ck], XE + 60, y, 46, s1)
        F.carga(c, t, C[ck] + 0.1, XE + 180, y, 46, s2)
        E.frase(c, t, C[ck] + 0.2, ps(txt, "i", 66), XE + 270, y + 22, passo=0.1)


# ---------------- a alfa e a montagem ----------------
EX, EY, ER = 1300, 560, 380


def b_alfa(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("o projétil:", "i", 72, TINTA2), XE, 220, passo=0.12)
        E.frase(c, t, C["s04.a"] + 0.6, [("partícula", "g", 100, COR), ("alfa", "g", 100, COR)], XE, 360, passo=0.15)
        for k, s in enumerate(("minúscula", "positiva", "muito rápida")):
            pilula_em(c, t, C["s04.b"] + 0.4 * k, s, XE + 150 + k * 330, 480, 52, TINTA)
        E.frase(c, t, C["s04.c"], ps("sai de um material radioativo", "i", 62), XE, 640, passo=0.1)
        pilula_em(c, t, C["s04.d"], "radioatividade: outra aula", XE + 330, 760, 46, TINTA2, "b")
        E.frase(c, t, C["s04.e"], ps("aqui: um", "i", 72) + [("projétil positivo", "g", 68, COR)], XE, 920, passo=0.12)
        q = ease_back(prog(t, C["s04.a"] + 0.3, 0.6))
        if q > 0:
            alfa(c, 1500 + 30 * math.sin(t * 2), 300, 90 * q)
            for k in range(4):
                M.line(c, 1380 - k * 40, 270 + k * 20, 1300 - k * 60, 270 + k * 20, E.COR, 0.4 * q, 6)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("uma", "i", 66) + [("folha de ouro", "g", 62, COR)] + ps("finíssima", "i", 66), XE, 180, passo=0.12)
        E.frase(c, t, C["s05.b"], ps("em volta, uma", "i", 60, TINTA2) + [("tela que brilha", "g", 56)], XE, 270, passo=0.1)
        experimento(c, t, C["s05"] + 0.2, EX, EY + 40, ER, C["s05.c"], "r")
        E.frase(c, t, C["s05.c"] + 0.3, ps("dá para ver o caminho de cada uma", "i", 54, TINTA2), XE, 1010, passo=0.08)
        return
    # s06: a previsão de Thomson
    E.frase(c, t, C["s06"], ps("o que se esperava?", "i", 76), XE, 200, passo=0.12)
    pudim(c, 420, 520, 150 * ease_back(prog(t, C["s06.a"], 0.6)), ep(t, C["s06.a"], 0.4))
    E.frase(c, t, C["s06.a"] + 0.3, ps("positivo espalhado,", "i", 56), 420, 760, "center", 0.1)
    E.frase(c, t, C["s06.a"] + 1.0, ps("fraco em cada ponto", "i", 56), 420, 830, "center", 0.1)
    experimento(c, t, C["s06"] + 0.2, EX + 60, EY + 20, ER - 40, C["s06.b"], "rdv", previsao=True)
    E.frase(c, t, C["s06.b"] + 0.3, [("todas", "g", 60, COR)] + ps("deviam atravessar", "i", 62), XE, 970, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("quase em linha reta", "i", 56, TINTA2), XE + 780, 970, passo=0.1)
    E.foco(c, t, C["s06"] + 0.4, 0.4, lambda a: E.pilula(c, "previsão de Thomson", EX + 60, 150, 44, "b", fundo=TINTA, a=a))


# ---------------- as três observações ----------------
def zoom(c, t, t0, cx, cy, tipo, a=1.0):
    """por dentro da folha: átomos de ouro (núcleo + eletrosfera) e a alfa da vez"""
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a
    for i in range(3):
        y = cy - 230 + i * 230
        c.drawCircle(cx, y, 105, M.paint(E.COR, 0.07 * q))
        c.drawCircle(cx, y, 105, M.paint(TINTA2, 0.35 * q, stroke=2))
        E.bola(c, cx, y, 9, E.COR, q)
    def pos(u):
        if tipo == "r":
            return lerp(cx - 420, cx + 420, u), cy - 115
        if tipo == "d":
            if u < 0.5:
                return lerp(cx - 420, cx - 20, u / 0.5), cy - 30
            v = (u - 0.5) / 0.5
            return cx - 20 + 400 * v, cy - 30 - 260 * v * v
        if u < 0.5:
            return lerp(cx - 420, cx - 40, ease_out(u / 0.5)), cy
        return lerp(cx - 40, cx - 420, (u - 0.5) / 0.5), cy + 40 * (u - 0.5)
    pts = [pos(k / 40) for k in range(41)]
    for A_, B_ in zip(pts, pts[1:]):
        M.line(c, A_[0], A_[1], B_[0], B_[1], E.COR, 0.45 * q, 4)
    u = ((t - t0 - 0.4) % 2.4) / 2.0
    if u > 1:
        return
    if tipo == "r":
        px, py = lerp(cx - 420, cx + 420, u), cy - 115
    elif tipo == "d":
        if u < 0.5:
            px, py = lerp(cx - 420, cx - 20, u / 0.5), cy - 30
        else:
            v = (u - 0.5) / 0.5
            px, py = cx - 20 + 400 * v, cy - 30 - 260 * v * v
    else:
        if u < 0.5:
            px, py = lerp(cx - 420, cx - 40, ease_out(u / 0.5)), cy
        else:
            px, py = lerp(cx - 40, cx - 420, (u - 0.5) / 0.5), cy + 40 * (u - 0.5)
    alfa(c, px, py, 14, q)


def b_resultado(c, t, C, b):
    itens = (("s07", "atravessou reto", "átomo quase vazio", "r", "a grande maioria"),
             ("s08", "desviou", "existe região positiva", "d", "algumas"),
             ("s09", "voltou", "pequena e com quase toda a massa", "v", "pouquíssimas"))
    atual = 0 if t < C["s08"] else 1 if t < C["s09"] else 2
    E.frase(c, t, C["s07"], ps("três observações", "i", 64, TINTA2), XE, 160, passo=0.12)
    for i, (k, obs, conc, tp, quantas) in enumerate(itens):
        if t < C[k]:
            continue
        y = 300 + i * 230
        ativo = i == atual
        cor_t = TINTA if ativo else TINTA2
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, C[k + ".b"], [(quantas, "i", 58, cor_t), (obs, "g", 58, cor_t)], XE + 110, y, passo=0.12)
        kc = k + (".c" if k != "s09" else ".c")
        E.frase(c, t, C[kc], [("→", "g", 54, COR), (conc, "i", 52, COR if ativo else TINTA2)], XE + 110, y + 80, passo=0.1)
    tp = itens[atual][3]
    zoom(c, t, C[itens[atual][0] + ".b"], 1500, 560, tp)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: centro(c, "por dentro da folha", 1500, 1000, 42, "i", TINTA2, a))
    if t >= C["s09.e"]:
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.pilula(c, "o núcleo", 1500, 150, 60, "g", fundo=E.COR, a=a))


# ---------------- o modelo nuclear ----------------
def b_nuclear(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("o modelo de", "i", 76) + [("Rutherford", "g", 72, COR)], XE, 200, passo=0.12)
        rq = ease_back(prog(t, C["s10.a"], 0.6))
        if t >= C["s10.b"]:
            rutherford(c, t, 1420, 580, 320, ep(t, C["s10.b"], 0.6), rn=22)
        if rq > 0:
            E.bola(c, 1420, 580, 22 * rq, E.COR)
        E.frase(c, t, C["s10.a"] + 0.2, [("núcleo:", "g", 60, COR)] + ps("pequeno, positivo,", "i", 60), XE, 360, passo=0.1)
        E.frase(c, t, C["s10.a"] + 1.4, ps("quase toda a massa", "i", 60), XE + 230, 440, passo=0.1)
        E.frase(c, t, C["s10.b"], [("eletrosfera:", "g", 60, Q.ELETRON)] + ps("onde os elétrons giram", "i", 60), XE, 600, passo=0.1)
        E.frase(c, t, C["s10.c"], ps("ocupa quase todo o", "i", 60) + [("tamanho", "g", 58)], XE, 760, passo=0.1)
        if t >= C["s10.c"]:
            q = ep(t, C["s10.c"], 0.6)
            c.drawCircle(1420, 580, 340, M.paint(Q.ELETRON, 0.08 * q))
            c.drawCircle(1420, 580, 340, M.paint(Q.ELETRON, 0.6 * q, stroke=4))
        return
    E.frase(c, t, C["s11.a"], ps("o núcleo é de", "i", 66) + [("10 mil a 100 mil", "g", 62, COR)], XE, 210, passo=0.12)
    E.frase(c, t, C["s11.a"] + 1.4, ps("vezes menor que o átomo", "i", 66), XE, 300, passo=0.1)
    E.foco(c, t, C["s11.b"], 0.6, lambda a: estadio(c, W / 2, 680, 1100, 520, a))
    E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: E.pilula(c, "o átomo: um estádio", 600, 430, 46, "b", fundo=TINTA, a=a))
    if t >= C["s11.c"]:
        q = ease_back(prog(t, C["s11.c"], 0.5))
        E.bola(c, W / 2, 680, 9 * q, E.COR)
        p = ep(t, C["s11.c"] + 0.3, 0.4)
        M.arrow(c, W / 2 + 260, 520, W / 2 + 20, 668, E.COR, p, 5, 18, ease_io(prog(t, C["s11.c"] + 0.3, 0.5)))
        E.foco(c, t, C["s11.c"] + 0.5, 0.4, lambda a: E.pilula(c, "o núcleo: uma bolinha de gude", W / 2 + 470, 500, 46, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("muita massa", "i", 66) + [("=", "g", 62, ERRADO)] + ps("núcleo grande?", "i", 66, ERRADO), XE, 320, passo=0.12)
    if t >= C["s12.b"]:
        E.risco(c, XE, 340, XE + 780, 270, t, C["s12.b"], largura=12)
    E.frase(c, t, C["s12.c"], [("núcleo:", "g", 60, COR)] + ps("pesado e", "i", 62) + [("minúsculo", "g", 60)], XE, 480, passo=0.12)
    E.frase(c, t, C["s12.d"], [("eletrosfera:", "g", 60, Q.ELETRON)] + ps("enorme, quase vazia,", "i", 62), XE, 600, passo=0.1)
    E.frase(c, t, C["s12.d"] + 1.6, ps("quase sem massa", "i", 62), XE + 380, 690, passo=0.1)
    E.foco(c, t, C["s12.a"] + 0.4, 0.5, lambda a: rutherford(c, t, 1480, 560, 260, a, rn=16))
    if t >= C["s12.e"]:
        for k in range(4):
            u = ((t - C["s12.e"] - 0.3 * k) % 1.8) / 1.8
            if t - C["s12.e"] - 0.3 * k < 0:
                continue
            alfa(c, lerp(1100, 1860, u), 380 + k * 110 if k != 2 else 690, 13)
        E.frase(c, t, C["s12.e"] + 0.3, ps("a alfa passa longe do núcleo", "i", 58, TINTA2), XE, 880, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("o atalho:", "i", 72, CLARO) + [("três linhas", "g", 70, BR)], W / 2, 170, "center", 0.12)
        linhas = (("s13.b", "atravessou", "átomo vazio"), ("s13.c", "desviou", "região positiva"), ("s13.d", "voltou", "núcleo pequeno e denso"))
        for i, (k, o, cc) in enumerate(linhas):
            y = 360 + i * 200
            E.foco(c, t, C[k], 0.4, lambda a, y=y, o=o: E.pilula(c, o, 560, y - 22, 60, "g", fundo="#22232B", a=a, cor=BR))
            p = ep(t, C[k] + 0.4, 0.4)
            if p > 0:
                M.arrow(c, 820, y - 22, lerp(820, 1060, ease_io(prog(t, C[k] + 0.4, 0.4))), y - 22, E.CLARO, p, 6, 22)
            E.frase(c, t, C[k] + 0.6, [(cc, "g", 60, E.CLARO)], 1110, y, passo=0.1)
        E.frase(c, t, C["s13.d"] + 1.6, ps("denso: muita massa num espaço minúsculo", "i", 52, CLARO), W / 2, 1000, "center", 0.08)
        return
    E.frase(c, t, C["s14.a"], ps("cada observação,", "i", 70, CLARO) + [("uma conclusão", "g", 66, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s14.a"] + 1.6, ps("a prova troca uma pela outra", "i", 62, CLARO), W / 2, 360, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 64, ERRADO), ("basta:", "i", 68, CLARO)] + ps("pediu o porquê do desvio?", "i", 68, CLARO), W / 2, 520, "center", 0.12)
    tc = C["s14.c"]
    F.carga(c, t, tc, 820, 760, 70, "+")
    E.foco(c, t, tc + 0.2, 0.4, lambda a: centro(c, "núcleo", 820, 880, 46, "i", CLARO, a))
    u = ease_out(prog(t, tc + 0.4, 1.2))
    if t >= tc + 0.3:
        alfa(c, lerp(1350, 940, u * 2) if u < 0.5 else lerp(940, 1300, (u - 0.5) * 2), 760 if u < 0.5 else lerp(760, 650, (u - 0.5) * 2), 30)
    E.frase(c, t, tc + 0.4, ps("positivo empurra positivo", "i", 60, CLARO), 1350, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], [("1", "g", 56, COR)] + ps("qual mostrou que o átomo", "i", 60), XE, 300, passo=0.08)
    E.frase(c, t, C["s15.a"] + 1.6, ps("é quase todo vazio?", "i", 60), XE + 50, 380, passo=0.08)
    E.frase(c, t, C["s15.b"], [("2", "g", 56, COR)] + ps("qual mostrou uma região muito pequena,", "i", 60), XE, 500, passo=0.08)
    E.frase(c, t, C["s15.b"] + 2.2, ps("com quase toda a massa?", "i", 60), XE + 50, 580, passo=0.08)
    for k, (ck, letra, s) in enumerate((("s15.c", "A", "a maioria atravessou"), ("s15.d", "B", "algumas desviaram"), ("s15.e", "C", "pouquíssimas voltaram"))):
        y = 720 + k * 110
        E.foco(c, t, C[ck], 0.4, lambda a, y=y, letra=letra: E.pilula(c, letra, XE + 40, y - 20, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C[ck] + 0.1, ps(s, "i", 60), XE + 110, y, passo=0.08)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1540, cy=480, r=190)
    else:
        E.foco(c, t, C["s15"] + 0.5, 0.5, lambda a: experimento(c, t, -1, 1640, 560, 210, None, a=a))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("vamos lá", "i", 70, TINTA2), XE, 190)
    E.frase(c, t, C["s17.a"], ps("vazio = caminho livre", "i", 64), XE, 320, passo=0.1)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: (E.pilula(c, "A", XE + 40, 410, 54, "g", fundo=CERTO, a=a),
                                            E.escreve(c, "a maioria atravessou", XE + 110, 430, 60, "g", TINTA, a)))
    E.frase(c, t, C["s17.c"], ps("pequena e pesada: joga a alfa de volta", "i", 60), XE, 580, passo=0.08)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: (E.pilula(c, "C", XE + 40, 670, 54, "g", fundo=CERTO, a=a),
                                            E.escreve(c, "pouquíssimas voltaram", XE + 110, 690, 60, "g", TINTA, a)))
    E.foco(c, t, C["s17.e"] - 1.2, 0.5, lambda a: (E.pilula(c, "B", XE + 40, 840, 54, "g", fundo=TINTA2, a=a),
                                                  E.escreve(c, "algumas desviaram", XE + 110, 860, 56, "i", TINTA2, a)))
    E.frase(c, t, C["s17.e"], [("→", "g", 54, COR), ("região positiva", "g", 54, COR)], XE + 640, 860, passo=0.1)
    E.foco(c, t, C["s17"] + 0.3, 0.5, lambda a: rutherford(c, t, 1560, 520, 230, a, rn=14))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s18.a"], ps("a maioria atravessa:", "i", 66) + [("átomo quase vazio", "g", 62)], XE, 360, passo=0.1)
        E.frase(c, t, C["s18.b"], ps("as que voltam revelam o", "i", 66) + [("núcleo", "g", 62, COR)], XE, 500, passo=0.1)
        for k, s in enumerate(("pequeno", "positivo", "quase toda a massa")):
            pilula_em(c, t, C["s18.b"] + 1.2 + 0.3 * k, s, XE + 150 + [0, 280, 640][k], 620, 48, E.COR)
        E.foco(c, t, C["s18.a"] + 0.4, 0.5, lambda a: rutherford(c, t, 1560, 800, 170, a, rn=12))
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("Bohr:", "g", 100, COR)] + ps("camadas", "i", 100), XE, 400)
    Q.bohr(c, t, C["s19.a"] + 0.4, 700, 720, (2, 8, 1), r0=70, dr=48)
    E.frase(c, t, C["s19.b"], ps("e as cores dos", "i", 60) + [("fogos", "g", 58, COR)], 960, 740, passo=0.1)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, alfa=b_alfa, resultado=b_resultado, nuclear=b_nuclear, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
