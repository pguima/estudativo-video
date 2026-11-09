"""Visual — Estudativo · FIS-EGF-013: satélites e marés.

Segue a linguagem visual da Física (visual.py da FIS-CIN-001) e a da trilha Equilíbrio, Gravitação e Fluidos (cabeçalho do
visual.py da FIS-EGF-001): eixo e braço em cota, giro horário laranja e anti-horário azul, astros (Sol âmbar, Terra azul),
fluidos em azul translúcido, pressão em setinhas laranja, empuxo azul. O kit da trilha vem copiado logo abaixo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Equilíbrio, Gravitação e Fluidos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-EGF-013_satelites_e_mares.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("canhao", "orbita", "mares", "atalho", "questao", "fim"))

# todas as contas da aula
assert 8.8 < 10 * (6400 / 6800) ** 2 < 9.0  # g a 400 km de altura
assert math.isqrt(10 * 6_400_000) == 8000 and 80 < 2 * math.pi * 6.4e6 / 8000 / 60 < 90  # 8 km/s, volta em ~84 min
assert math.isqrt(4 * 4_000_000) == 4000 and (1 / 4) ** 0.5 == 0.5 and abs((1 / 9) ** 0.5 - 1 / 3) < 1e-12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha (o mesmo em todas as aulas FIS-EGF) ----------------
BR = "#FFFFFF"
MADEIRA, MADEIRA2 = "#B07A4A", "#7E5432"
AGUA, AGUA2, OLEO = "#5AB4E6", "#2C86C2", "#E9B44C"
SOL, TERRA, LUA = "#FFB020", "#2F6FB0", "#A9A9B4"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def linhas(c, t, itens, x, y0, dy, size=72, align="left", est="g"):
    """passo a passo: itens = [(instante, "fórmula", cor)], uma linha por etapa, de cima para baixo"""
    for i, it in enumerate(itens):
        t0, s, cor = it[0], it[1], (it[2] if len(it) > 2 else TINTA)
        E.formula_em(c, t, t0, s, x, y0 + i * dy, size, est, cor, align)


def cota(c, t, t0, A, B, rot, cor=TINTA2, size=46, lado=-1, d=0.5, cor_txt=None):
    """linha de medida de A até B, com tracinhos nas pontas e o rótulo no meio, do lado `lado` (−1 = acima/esquerda)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    ux, uy = E._uni(*A, *B)
    nx, ny = -uy, ux
    M.line(c, *A, lerp(A[0], B[0], q), lerp(A[1], B[1], q), cor, 1.0, 4)
    for P_ in (A, B):
        M.line(c, P_[0] - nx * 16, P_[1] - ny * 16, P_[0] + nx * 16, P_[1] + ny * 16, cor, q, 4)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    E.foco(c, t, t0 + d * 0.6, 0.4, lambda a: E._meio(c, rot, mx + nx * lado * (size * 0.8), my + ny * lado * (size * 0.8), size, "b", cor_txt or E.COR_TEXTO, a))


def seta_giro(c, cx, cy, r, ini, varre, cor, a=1.0, largura=9, p=1.0):
    """arco com ponta de seta: o sentido do giro. ini e varre em graus de tela (varre > 0 = horário)"""
    if a <= 0 or p <= 0:
        return
    v = varre * p
    E.arco(c, cx, cy, r, ini, v, cor, largura, a)
    g = math.radians(ini + v)
    x, y = cx + r * math.cos(g), cy + r * math.sin(g)
    s = 1 if v > 0 else -1
    ux, uy = -math.sin(g) * s, math.cos(g) * s
    F._cabeca(c, x + ux * largura * 1.6, y + uy * largura * 1.6, ux, uy, largura * 3.2, cor, a)


def apoio(c, x, y, s=70, a=1.0, escuro=False):
    """apoio triangular com o vértice (o eixo) em (x, y)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x - s * 0.7, y + s); p.lineTo(x + s * 0.7, y + s); p.close()
    c.drawPath(p, M.paint(BR if escuro else TINTA, a))
    c.drawCircle(x, y, s * 0.13, M.paint(E.COR, a))


def lembrete(c, t, C, cena, itens, numero, palavra="coisas"):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)], uma caixa por item"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de" if palavra == "coisas" else "você vai usar", "i", 80), XE, 410, passo=0.14)
    t1 = C.get(cena + ".a", C[cena] + 0.6) if hasattr(C, "get") else C[cena] + 0.6
    E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, str(numero), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, palavra, XE + 215, 700, 110 if palavra == "coisas" else 84, "i", TINTA, a))
    x, w = 820, 1000
    h = {2: 230, 3: 190, 4: 150}[n]
    gap = {2: 290, 3: 230, 4: 180}[n]
    y0 = {2: 230, 3: 150, 4: 140}[n]
    s1, s2 = {2: (58, 58), 3: (50, 52), 4: (44, 46)}[n]
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s2, COR)], x + 44, y + h * 0.4 + s2 * 1.3)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 50, COR) + ps("procure no canal", "i", 50), 820, 1010, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """até o fim da aula: itens = [(cue, texto)] numerados, com a órbita à direita"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.2 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, cena, itens):
    """itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 26, 52, a=a), centro(c, str(i + 1), 230, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.1)


def proxima(c, t, C, cena, l1, l2, desenho=None, k=("a", "c", "d")):
    """próxima aula + inscreva-se + bons estudos; desenho(a) ilustra a próxima aula na metade de baixo"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[f"{cena}.{k[0]}"], l1, XE, 400)
    if l2:
        E.frase(c, t, C[f"{cena}.{k[0]}"] + 0.5, l2, XE, 540)
    if desenho:
        desenho()
    E.foco(c, t, C[f"{cena}.{k[1]}"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[f"{cena}.{k[1]}"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[f"{cena}.{k[1]}"] + 0.2, 0.4))
    E.frase(c, t, C[f"{cena}.{k[2]}"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def hora_testar(c, t, C, cena):
    E.frase(c, t, C[cena], ps("hora de testar", "i", 72, COR), XE, 180)




def empurra(c, t, t0, P, ang, comp, rot=None, modulo=None, cor=None):
    """força que CHEGA ao ponto P vindo da direção oposta a ang (graus da Física): a ponta encosta no corpo"""
    dx, dy = F._dir(ang)
    F.vetor(c, t, t0, (P[0] - dx * comp, P[1] - dy * comp), P, rot, modulo, cor, 10, em=0.4)


# ---------------- peças desta aula ----------------
def estacao(c, x, y, s, a=1.0, giro=0.0):
    """estação espacial: módulo central e dois painéis solares"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(giro)
    for d in (-1, 1):
        M.rrect(c, d * s * 0.45 - (s * 0.9 if d < 0 else 0), -s * 0.3, s * 0.9, s * 0.6, 4, "#2F5DA8", a)
    M.line(c, -s * 0.5, 0, s * 0.5, 0, TINTA2, a, max(3, s * 0.08))
    M.rrect(c, -s * 0.22, -s * 0.18, s * 0.44, s * 0.36, 5, "#D9D9DE", a)
    c.restore()


def tracejado_circ(c, cx, cy, r, q, cor=TINTA, larg=4):
    pt = M.paint(cor, 0.7 * q, stroke=larg)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawCircle(cx, cy, r, pt)


def trajetoria(v0, r0=1.2, n=4000, dt=0.004):
    """bala lançada na horizontal do alto da montanha (GM = 1, raio da Terra = 1): pontos (x, y) até tocar o chão ou dar a volta"""
    x, y, vx, vy = 0.0, r0, v0, 0.0
    pts = [(x, y)]
    ang = 0.0
    for _ in range(n):
        r = math.hypot(x, y)
        ax, ay = -x / r ** 3, -y / r ** 3
        vx += ax * dt; vy += ay * dt
        x += vx * dt; y += vy * dt
        pts.append((x, y))
        ang = math.atan2(x, y)
        if math.hypot(x, y) < 1.0 or (ang < 0 and len(pts) > 50 and abs(ang) < 0.05):
            break
    return pts


TRAJ = [trajetoria(v) for v in (0.5, 0.74, math.sqrt(1 / 1.2))]


def canhao_cena(c, t, C, cx, cy, k):
    q = ep(t, C["s04.a"], 0.5)
    if q <= 0:
        return
    E.bola(c, cx, cy, k, TERRA, q)
    # montanha e canhão no topo
    p = skia.Path(); p.moveTo(cx - 120, cy - k + 30); p.lineTo(cx, cy - k * 1.2 - 4); p.lineTo(cx + 120, cy - k + 30); p.close()
    c.drawPath(p, M.paint("#6E6E78", q))
    M.rrect(c, cx - 10, cy - k * 1.2 - 22, 60, 18, 6, TINTA, q)
    for i, (kk, cor) in enumerate((("s04.b", TINTA2), ("s04.c", TINTA), ("s04.d", E.COR))):
        pp = ep(t, C[kk], 2.2 if i == 2 else 1.2)
        if pp > 0:
            pts = [(cx + x * k, cy - y * k) for x, y in TRAJ[i]]
            ponta = F.poli(c, pts, pp, cor, 1.0, 6, dash=E.TRACO if i < 2 else None)
            E.bola(c, *ponta, 12, cor, 1.0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            cx, cy, R = 1300, 1250, 700
            q = ep(t, C["s01.a"], 0.6)
            if q > 0:
                E.bola(c, cx, cy, R, TERRA, q)
                tracejado_circ(c, cx, cy, R + 170, q)
            g = math.radians(-112 + 4 * (t - C["s01.a"]))
            P = (cx + (R + 170) * math.cos(g), cy + (R + 170) * math.sin(g))
            E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: estacao(c, *P, 90, a, math.degrees(g) + 90))
            pass
            ux, uy = E._uni(*P, cx, cy)
            F.seta(c, P[0] + ux * 60, P[1] + uy * 60, P[0] + ux * 190, P[1] + uy * 190, E.COR, ep(t, C["s01.d"], 0.4), 10, p=ep(t, C["s01.d"], 0.5))
            E.frase(c, t, C["s01.a"], [("Estação Espacial:", "g", 62)] + ps("a 400 km de altura", "i", 62), XE, 180, passo=0.1)
            E.frase(c, t, C["s01.b"], [("g", "g", 64, COR), ("≈ 9 m/s²", "g", 64)] + ps("lá em cima", "i", 62), XE, 290, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("por que ela", "i", 76) + [("não cai?", "g", 76, COR)], XE, 470, passo=0.12)
            E.frase(c, t, C["s01.d"], [("ela cai.", "g", 76, ERRADO)] + ps("o tempo todo.", "i", 76), XE, 600, passo=0.15)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "a velocidade de um satélite"), ("s02.b", "as marés")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a gravitação:", "cai com a distância²"), ("s03.c", "a força centrípeta:", "a = v² / R, para o centro")), 2)


# ---------------- o canhão de Newton ----------------
def b_canhao(c, t, C, b):
    canhao_cena(c, t, C, 1420, 680, 280)
    E.frase(c, t, C["s04.a"], ps("o canhão", "i", 70) + [("de Newton", "g", 70, COR)], XE, 190, passo=0.12)
    E.frase(c, t, C["s04.b"], ps("lenta:", "i", 54) + [("cai perto", "g", 54, TINTA2)], XE, 340, passo=0.12)
    E.frase(c, t, C["s04.c"], ps("mais rápida:", "i", 54) + [("mais longe", "g", 54)], XE, 430, passo=0.12)
    E.frase(c, t, C["s04.d"], ps("rápida o bastante:", "i", 54) + [("o chão foge", "g", 54, COR)], XE, 520, passo=0.12)
    pilula_em(c, t, C["s04.e"], "nunca chega ao chão: órbita", 520, 820, 52, E.COR)


# ---------------- velocidade orbital ----------------
OX, OY, OR, ORB = 1350, 600, 220, 340


def satelite_orbita(c, t, t0, cx, cy, R, r, vel=0.5, setas=None, a=1.0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return None
    E.bola(c, cx, cy, R, TERRA, q)
    tracejado_circ(c, cx, cy, r, q)
    g = vel * t
    P = (cx + r * math.cos(g), cy - r * math.sin(g))
    F.bloco(c, *P, 44, 44, None, a=q)
    return P, g


def b_orbita(c, t, C, b):
    if t < C["s06"]:
        def s05():
            P, g = satelite_orbita(c, t, C["s05"], OX, OY, OR, ORB, 0.35) or ((0, 0), 0)
            if t >= C["s05.a"]:
                ux, uy = E._uni(*P, OX, OY)
                F.seta(c, P[0] + ux * 30, P[1] + uy * 30, P[0] + ux * 150, P[1] + uy * 150, E.COR, ep(t, C["s05.a"], 0.4), 10)
                tx, ty = -math.sin(g), -math.cos(g)
                F.seta(c, P[0] + tx * 30, P[1] + ty * 30, P[0] + tx * 170, P[1] + ty * 170, F.VEL, ep(t, C["s05.a"] + 0.4, 0.4), 10)
            E.frase(c, t, C["s05.a"], ps("só a gravidade puxa,", "i", 60) + [("para o centro", "g", 60, COR)], XE, 180, passo=0.1)
            E.frase(c, t, C["s05.b"], [("gravidade", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("força centrípeta", "i", 62), XE, 290, passo=0.12)
            E.formula_em(c, t, C["s05.d"], "f{v^2}{R} = g", XE, 560, 130, "g", TINTA)
            E.frase(c, t, C["s05.c"], ps("rente à Terra: a aceleração é", "i", 54, TINTA2) + [("g", "g", 54, COR)], XE, 400, passo=0.08)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            F.formula_legenda(c, t, C["s06.a"], "v = r{g · R}", [("g", "gravidade na altura da órbita", "m/s^2"), ("R", "raio da órbita, do centro", "m")],
                              XE, 330, 140, tl=[C["s06.b"], C["s06.c"]], size_l=48)
            pilula_em(c, t, C["s06.d"], "a massa do satélite não entra", XE + 480, 760, 46, E.COR)
            P = satelite_orbita(c, t, C["s06.c"], 1500, 620, 150, 300, 0.5)
            if P and t >= C["s06.c"]:
                M.line(c, 1500, 620, 1500 + 300, 620, TINTA, ep(t, C["s06.c"] + 0.2, 0.4), 4)
                cota(c, t, C["s06.c"] + 0.2, (1500, 620 + 190), (1500 + 300, 620 + 190), "R", lado=1, size=50)
            E.frase(c, t, C["s06.e"], ps("parafuso e estação:", "i", 58) + [("mesma velocidade", "g", 56, COR)], XE, 930, passo=0.1)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    if t < C["s08"]:
        def s07():
            linhas(c, t, [(C["s07.a"], "g = 10,   R = 6.400 km", TINTA), (C["s07.b"], "R = 6,4 × 10^6 m", TINTA2),
                          (C["s07.c"], "g · R = 64.000.000", TINTA), (C["s07.d"], "v = r{64.000.000} = 8.000 m/s", TINTA)], XE, 230, 165, 76)
            bola_txt(c, t, C["s07.e"], "8 km/s", 1520, 520, 160, 70)
            pilula_em(c, t, C["s07.e"] + 1.2, "1 volta: cerca de 1 h 30 min", 1520, 790, 44, TINTA)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], ps("mais longe:", "i", 66) + [("gravidade mais fraca", "g", 62)], XE, 190, passo=0.12)
            E.frase(c, t, C["s08.b"], [("velocidade menor", "g", 62, COR)], XE, 290)
            E.formula_em(c, t, C["s08.c"], "v^2 = f{G · M}{R}", XE, 520, 120, "g", TINTA)
            linhas(c, t, [(C["s08.d"], "R × 4  →  v^2 ÷ 4", TINTA), (C["s08.e"], "→  v ÷ 2", COR)], XE, 760, 140, 80)
            q = ep(t, C["s08.a"], 0.5)
            if q > 0:
                E.bola(c, 1450, 600, 70, TERRA, q)
                tracejado_circ(c, 1450, 600, 110, q)
                tracejado_circ(c, 1450, 600, 440, q)
                for r_, w, s in ((110, 1.6, 30), (440, 0.2, 30)):
                    P = (1450 + r_ * math.cos(w * t), 600 - r_ * math.sin(w * t))
                    F.bloco(c, *P, s, s, None, a=q)
            cota(c, t, C["s08.d"], (1450, 600 + 150), (1450 + 440, 600 + 150), "4R", lado=1, size=46)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.frase(c, t, C["s09.a"], [("geoestacionário", "g", 76, COR)], XE, 200)
    q = ep(t, C["s09.a"], 0.5)
    cx, cy = 1350, 640
    if q > 0:
        tracejado_circ(c, cx, cy, 380, q)
        rot = 0.6 * (t - C["s09.a"])
        E.bola(c, cx, cy, 150, TERRA, q)
        P0 = (cx + 150 * math.cos(rot), cy - 150 * math.sin(rot))
        c.drawCircle(*P0, 12, M.paint(BR, q))
        M.line(c, cx, cy, *P0, BR, q * 0.6, 3)
        P = (cx + 380 * math.cos(rot), cy - 380 * math.sin(rot))
        M.line(c, *P0, *P, E.COR, q * 0.5, 3, dash=E.TRACO)
        F.bloco(c, *P, 44, 44, None, a=q)
    E.frase(c, t, C["s09.b"], [("1 volta por dia,", "g", 58)] + ps("sobre o equador", "i", 60), XE, 330, passo=0.1)
    E.frase(c, t, C["s09.c"], ps("parece", "i", 60) + [("parado no céu", "g", 60, COR)], XE, 430, passo=0.1)
    E.frase(c, t, C["s09.d"], [("≈ 36 mil km", "g", 60)] + ps("de altura", "i", 60), XE, 560, passo=0.1)


# ---------------- marés ----------------
def b_mares(c, t, C, b):
    cx, cy, R = 760, 600, 220
    if t < C["s11"]:
        def s10():
            q = ep(t, C["s10.a"], 0.5)
            if q > 0:
                E.bola(c, cx, cy, R, TERRA, q)
                E.bola(c, 1650, cy, 70, LUA, q)
                centro(c, "Lua", 1650, cy + 130, 48, "i", TINTA2, q)
            for k_, x, comp in (("s10.c", cx + R, 230), ("s10.d", cx, 150), ("s10.e", cx - R, 90)):
                F.vetor(c, t, C[k_], (x, cy - 0 if x != cx else cy), (x + comp, cy), None, None, E.COR, 11)
            E.foco(c, t, C["s10.c"] + 0.3, 0.4, lambda a: E.escreve(c, "mais perto: mais força", cx + R + 20, cy + 80, 44, "b", COR, a))
            E.foco(c, t, C["s10.e"] + 0.3, 0.4, lambda a: E.escreve(c, "mais longe: menos", cx - R - 20 - E.larg("mais longe: menos", "b", 44), cy + 80, 44, "b", TINTA2, a))
            E.frase(c, t, C["s10.a"], ps("a Lua puxa a Terra inteira,", "i", 62), XE, 180, passo=0.1)
            E.frase(c, t, C["s10.b"], ps("mas", "i", 62) + [("não puxa tudo igual", "g", 62, COR)], XE, 270, passo=0.1)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    if t < C["s12"]:
        def s11():
            q = ep(t, C["s11.a"], 0.8)
            if q > 0:
                k = 1 + 0.32 * q
                c.drawOval(skia.Rect.MakeXYWH(cx - R * 1.12 * k, cy - R * 1.08, 2 * R * 1.12 * k, 2 * R * 1.08), M.paint(AGUA, 0.55))
            E.bola(c, cx, cy, R, TERRA, 1.0)
            E.bola(c, 1650, cy, 70, LUA, 1.0)
            pilula_em(c, t, C["s11.b"], "maré alta", cx + R + 150, cy - 110, 42, AGUA2)
            pilula_em(c, t, C["s11.c"], "maré alta", cx - R - 150, cy - 110, 42, AGUA2)
            if t >= C["s11.d"]:
                g = math.pi / 2 + 0.9 * (t - C["s11.d"])
                P = (cx + R * math.cos(g), cy - R * math.sin(g))
                E.bola(c, *P, 16, E.COR, 1.0)
                E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "a praia gira com a Terra", 1150, 900, 46, "i", TINTA2, a))
            E.frase(c, t, C["s11.a"], ps("o oceano se estica em", "i", 62) + [("dois montes", "g", 62, AGUA2)], XE, 180, passo=0.1)
            E.frase(c, t, C["s11.e"], [("2 altas e 2 baixas", "g", 58, COR)] + ps("por dia", "i", 60), XE, 1000, passo=0.1)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    E.frase(c, t, C["s12.a"], ps("o Sol também faz maré,", "i", 60) + [("mais fraca", "g", 60)], XE, 170, passo=0.1)
    for i, (k_, k2, tit, res, cor, ang) in enumerate((("s12.b", "s12.c", "lua cheia e nova", "maré maior", CERTO, 0),
                                                      ("s12.d", "s12.e", "crescente e minguante", "maré menor", ERRADO, 90))):
        x0 = 520 + i * 880
        q = ep(t, C[k_], 0.5)
        if q > 0:
            k = 1.35 if i == 0 else 1.12
            c.drawOval(skia.Rect.MakeXYWH(x0 - 110 * k, 600 - 110, 220 * k, 220), M.paint(AGUA, 0.55 * q))
            E.bola(c, x0, 600, 90, TERRA, q)
            E.bola(c, x0 + 230, 600, 32, LUA, q)
            sx, sy = (x0 - 330, 600) if i == 0 else (x0, 600 - 290)
            E.bola(c, sx, sy, 46, SOL, q)
            M.line(c, sx, sy, x0, 600, SOL, q * 0.6, 4, dash=E.TRACO)
            M.line(c, x0, 600, x0 + 230, 600, LUA, q * 0.9, 4, dash=E.TRACO)
        E.foco(c, t, C[k_] + 0.3, 0.4, lambda a, x0=x0, tit=tit: centro(c, tit, x0, 820, 46, "b", TINTA, a))
        E.foco(c, t, C[k2], 0.4, lambda a, x0=x0, res=res, cor=cor: E.pilula(c, res, x0, 920, 48, "g", fundo=cor, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("flutua porque não tem gravidade?", "i", 62), XE + 480, 190, passo=0.1)
    if t >= C["s13.b"] - 0.2:
        E.risco(c, XE + 470, 205, XE + 1440, 150, t, C["s13.b"] - 0.2, largura=10)
    E.frase(c, t, C["s13.b"], ps("a 400 km:", "i", 64) + [("g ≈ 9 m/s²", "g", 64, COR)], XE, 380, passo=0.12)
    nx, ny = 1450, 640
    q = ep(t, C["s13.c"], 0.5)
    if q > 0:
        M.rrect(c, nx - 260, ny - 180, 520, 360, 40, "#D9D9DE", q)
        M.rrect(c, nx - 260, ny - 180, 520, 360, 40, TINTA, q * 0.0)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(nx - 260, ny - 180, 520, 360), 40, 40), M.paint(TINTA, q, stroke=5))
        y_ast = ny + 12 * math.sin(t * 1.7)
        E.bola(c, nx - 20, y_ast - 40, 34, BR, q)
        M.rrect(c, nx - 55, y_ast - 10, 70, 90, 16, BR, q)
        c.drawCircle(nx - 20, y_ast - 40, 34, M.paint(TINTA, q, stroke=4))
    F.vetor(c, t, C["s13.c"] + 0.4, (nx + 330, ny - 120), (nx + 330, ny + 60), None, None, F.ACEL, 10)
    F.vetor(c, t, C["s13.c"] + 0.6, (nx + 30, ny - 40), (nx + 30, ny + 140), None, None, F.ACEL, 10)
    E.foco(c, t, C["s13.c"] + 0.8, 0.4, lambda a: centro(c, "mesma aceleração", nx, ny + 270, 48, "b", F.ACEL, a))
    E.frase(c, t, C["s13.c"], ps("ele", "i", 64) + [("cai junto", "g", 64, COR)] + ps("com a nave", "i", 64), XE, 520, passo=0.12)
    E.frase(c, t, C["s13.d"], ps("nada empurra:", "i", 60) + [("sem sensação de peso", "g", 56)], XE, 660, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.formula_em(c, t, C["s14.a"], "v^2 · R = constante", W / 2, 360, 110, "g", BR, "center")
            E.formula_em(c, t, C["s14.b"], "R × 9  →  v ÷ 3", W / 2, 560, 96, "g", CLARO, "center")
            E.formula_em(c, t, C["s14.c"], "R × 16  →  v ÷ 4", W / 2, 720, 96, "g", CLARO, "center")
            E.frase(c, t, C["s14.d"], ps("em volta do", "i", 64, CLARO) + [("mesmo planeta", "g", 64, BR)], W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("só cuidado com a", "i", 76, CLARO) + [("altura", "g", 76, BR)], W / 2, 250, "center", 0.12)
    E.formula_em(c, t, C["s15.b"], "R = raio do planeta + altura", W / 2, 520, 92, "g", BR, "center")
    cx, cy = W / 2, 900
    q = ep(t, C["s15.c"], 0.5)
    if q > 0:
        E.bola(c, cx - 300, cy, 110, TERRA, q)
        F.bloco(c, cx + 140, cy, 36, 36, None, a=q)
    cota(c, t, C["s15.c"], (cx - 300, cy - 150), (cx - 190, cy - 150), "raio", lado=-1, size=40, cor=CLARO, cor_txt=CLARO)
    cota(c, t, C["s15.c"] + 0.4, (cx - 190, cy - 150), (cx + 140, cy - 150), "altura", lado=-1, size=40, cor=CLARO, cor_txt=CLARO)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s16")
    E.frase(c, t, C["s16.a"], [("g =", "g", 66), ("4 m/s²", "g", 66, COR)] + ps("na superfície", "i", 66), XE, 330, passo=0.12)
    E.frase(c, t, C["s16.b"], [("raio =", "g", 66), ("4.000 km", "g", 66, COR)], XE, 440, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("v na órbita rente?", "i", 72), XE, 620, passo=0.12)
    E.frase(c, t, C["s16.d"], ps("e com o", "i", 72) + [("dobro da massa?", "g", 70, COR)], XE, 760, passo=0.12)
    if t < C["s17"]:
        q = ep(t, C["s16.a"], 0.5)
        if q > 0:
            E.bola(c, 1450, 600, 230, "#8E6FB8", q)
            tracejado_circ(c, 1450, 600, 262, q)
            g = 0.7 * t
            F.bloco(c, 1450 + 262 * math.cos(g), 600 - 262 * math.sin(g), 36, 36, None, a=q)
    else:
        E.relogio(c, t, C["s17.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        def s18():
            linhas(c, t, [(C["s18.a"], "R = 4 × 10^6 m", TINTA2), (C["s18.b"], "g · R = 4 · 4 × 10^6", TINTA),
                          (C["s18.c"], "= 16.000.000", TINTA), (C["s18.d"], "v = r{16.000.000}", TINTA)], XE, 240, 170, 84)
            bola_txt(c, t, C["s18.e"], "4.000 m/s", 1480, 560, 180, 62, CERTO)
            pilula_em(c, t, C["s18.e"] + 1.2, "4 km/s", 1480, 820, 50, TINTA)
        E.saida(c, t, C["s19"] - 0.1, s18)
        return
    E.frase(c, t, C["s19.a"], ps("massa", "i", 80) + [("× 2?", "g", 80, COR)], XE, 380, passo=0.12)
    E.frase(c, t, C["s19.b"], [("mesma velocidade", "g", 80, CERTO)], XE, 540)
    E.frase(c, t, C["s19.b"] + 0.8, ps("a massa do satélite não entra na conta", "i", 56, TINTA2), XE, 680, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s21"]:
        E.saida(c, t, C["s21"] - 0.1, lambda: resumo(c, t, C, "s20", (
            ("s20.a", [("gravidade", "g", 64, COR), ("=", "g", 64, TINTA2), ("força centrípeta", "i", 70)]),
            ("s20.b", [("rente:", "i", 70), ("v = √(g · R)", "g", 64, COR)]),
            ("s20.c", [("maré:", "g", 64), ("a Lua puxa", "i", 70), ("cada lado diferente", "g", 62, COR)]))))
        return

    def desenho():
        q = ep(t, C["s21.b"], 0.6)
        if q <= 0:
            return
        k = 0
        for i, x in enumerate((400, 800, 1200)):
            E.foco(c, t, C["s21.b"] + 0.3 * i, 0.4, lambda a, x=x, i=i: (
                apoio(c, x, 800, 60, a) if i == 0 else E.bola(c, x, 820, 60, SOL if i == 1 else TERRA, a)))
        E.foco(c, t, C["s21.b"], 0.4, lambda a: M.rrect(c, 250, 774, 300, 22, 8, MADEIRA, a))
    proxima(c, t, C, "s21", [("Praticando:", "g", 110, COR)], [("torque e gravitação", "i", 96)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, canhao=b_canhao, orbita=b_orbita, mares=b_mares, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
