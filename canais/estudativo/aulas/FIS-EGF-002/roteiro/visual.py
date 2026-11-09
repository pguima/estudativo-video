"""Visual — Estudativo · FIS-EGF-002: leis de Kepler.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-002_leis_de_kepler.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("elipse", "areas", "terceira", "atalho", "questao", "fim"))

# todas as contas da aula
assert 4 ** 3 == 64 and math.isqrt(64) == 8 and 4 * math.isqrt(4) == 8 and 9 * math.isqrt(9) == 27
assert 16 * math.isqrt(16) == 64 and 64 ** 2 == 4096 == 16 ** 3 and 8 == 4 * 2
assert 152 - 147 == 5  # a distância Terra-Sol muda pouco (milhões de km)


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
def kepler(a, b, Mang):
    """posição (dx, dy) em relação ao centro da elipse para a anomalia média Mang (rad); periélio à direita, giro anti-horário"""
    e = math.sqrt(max(0.0, 1 - (b / a) ** 2))
    Ee = Mang
    for _ in range(12):
        Ee -= (Ee - e * math.sin(Ee) - Mang) / (1 - e * math.cos(Ee))
    return a * math.cos(Ee), -b * math.sin(Ee)


def foco(a, b):
    return math.sqrt(max(0.0, a * a - b * b))


def elipse(c, cx, cy, a, b, q=1.0, cor=TINTA, largura=4):
    """órbita tracejada"""
    if q <= 0:
        return
    pt = M.paint(cor, 0.8 * q, stroke=largura)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawOval(skia.Rect.MakeXYWH(cx - a, cy - b, 2 * a, 2 * b), pt)


def setor(c, cx, cy, a, b, M0, M1, cor=None, alfa=0.35, p=1.0):
    """área varrida pela linha Sol-planeta entre as anomalias médias M0 e M1 (p = quanto já varreu)"""
    if p <= 0:
        return
    fx = cx + foco(a, b)
    path = skia.Path(); path.moveTo(fx, cy)
    n = 40
    for k in range(n + 1):
        dx, dy = kepler(a, b, M0 + (M1 - M0) * p * k / n)
        path.lineTo(cx + dx, cy + dy)
    path.close()
    c.drawPath(path, M.paint(cor or E.COR, alfa))
    c.drawPath(path, M.paint(cor or E.COR, 0.9, stroke=3))


def arco_orb(c, cx, cy, a, b, M0, M1, cor, largura=10, p=1.0):
    pts = [(cx + kepler(a, b, M0 + (M1 - M0) * k / 30)[0], cy + kepler(a, b, M0 + (M1 - M0) * k / 30)[1]) for k in range(31)]
    F.poli(c, pts, p, cor, 1.0, largura)


def sistema(c, t, t0, cx, cy, a, b, giro=0.0, r_sol=60, r_pl=26, linha=False, cor_pl=None):
    """órbita + Sol no foco da direita + planeta na anomalia média `giro`; devolve a posição do planeta"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return None
    elipse(c, cx, cy, a, b, q)
    fx = cx + foco(a, b)
    dx, dy = kepler(a, b, giro)
    P = (cx + dx, cy + dy)
    if linha:
        M.line(c, fx, cy, *P, TINTA2, q, 4)
    E.bola(c, fx, cy, r_sol * ease_back(prog(t, t0, 0.6)), SOL, q)
    E.bola(c, *P, r_pl * q, cor_pl or TERRA, q)
    return P


def circulo_orb(c, cx, cy, r, q, cor=TINTA):
    pt = M.paint(cor, 0.7 * q, stroke=4)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawCircle(cx, cy, r, pt)


# ---------------- gancho ----------------
OX, OY, OA, OB = 1150, 620, 520, 333


def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            g = 0.55 * (t - C["s01.a"])
            sistema(c, t, C["s01.a"], OX, OY, OA, OB, giro=g)
            fx = OX + foco(OA, OB)
            E.frase(c, t, C["s01.a"], ps("não é um", "i", 70) + [("círculo perfeito", "g", 70, COR)], XE, 190, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("nem sempre a", "i", 70) + [("mesma velocidade", "g", 70, COR)], XE, 290, passo=0.12)
            E.foco(c, t, C["s01.c"], 0.4, lambda a: (E.pilula(c, "janeiro: mais rápido", fx + 30, OY - 120, 42, "g", fundo=E.COR, a=a)))
            E.foco(c, t, C["s01.d"], 0.4, lambda a: (E.pilula(c, "julho: mais devagar", OX - OA + 170, OY - 100, 42, "g", fundo=TINTA, a=a)))
            E.frase(c, t, C["s01.e"], [("Johannes", "i", 76), ("Kepler", "g", 76, COR)], XE, 1010, passo=0.15)
            E.frase(c, t, C["s01.e"] + 0.8, ps("há mais de 400 anos", "i", 52, TINTA2), XE + 610, 1010, passo=0.1)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "a órbita"), ("s02.b", "onde é mais rápido"), ("s02.c", "o ano de dois planetas")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o período T:", "o tempo de uma volta"), ("s03.c", "para a conta:", "potência e raiz")), 2)


# ---------------- primeira lei ----------------
def b_elipse(c, t, C, b):
    cx, cy, a = 1180, 620, 560
    if t < C["s05"]:
        def s04():
            bq = lerp(a, 360, ease_io(prog(t, C["s04.c"], 1.0)))
            q = ep(t, C["s04.a"], 0.6)
            if q > 0:
                elipse(c, cx, cy, a, bq, q) if t >= C["s04.c"] else circulo_orb(c, cx, cy, a * 0.999, q)
            fx = cx + foco(a, bq) * ease_io(prog(t, C["s04.d"], 1.0))
            E.foco(c, t, C["s04.a"], 0.5, lambda al: E.bola(c, fx, cy, 60, SOL, al))
            g = 0.5 * (t - C["s04.a"])
            if t >= C["s04.a"]:
                E.bola(c, cx + a * math.cos(g), cy - bq * math.sin(g), 26, TERRA, q)
            E.frase(c, t, C["s04.a"], [("órbita", "g", 76, COR), ("=", "g", 70, TINTA2)] + ps("o caminho do planeta", "i", 70), XE, 180, passo=0.12)
            E.frase(c, t, C["s04.b"], [("1ª lei:", "g", 70), ("elipse", "g", 70, COR)], XE, 330, passo=0.15)
            E.frase(c, t, C["s04.c"], ps("um círculo achatado", "i", 62, TINTA2), XE, 420, passo=0.1)
            E.frase(c, t, C["s04.d"], ps("o Sol", "i", 62) + [("não fica no centro", "g", 58, ERRADO)], XE, 1000, passo=0.12)
            if t >= C["s04.d"]:
                E.foco(c, t, C["s04.d"], 0.4, lambda al: (M.line(c, cx - 14, cy, cx + 14, cy, TINTA2, al, 4), M.line(c, cx, cy - 14, cx, cy + 14, TINTA2, al, 4),
                                                          centro(c, "centro", cx, cy + 60, 40, "i", TINTA2, al)))
            pilula_em(c, t, C["s04.e"], "foco", cx + foco(a, 360), cy - 110, 50, E.COR)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    # s05: periélio e afélio
    b_ = 360
    fx = cx + foco(a, b_)

    def s05():
        q = ep(t, C["s05"], 0.5)
        elipse(c, cx, cy, a, b_, q)
        E.bola(c, fx, cy, 60, SOL, q)
        E.foco(c, t, C["s05.a"], 0.5, lambda al: E.bola(c, cx + a, cy, 26, TERRA, al))
        cota(c, t, C["s05.a"] + 0.3, (fx, cy + 120), (cx + a, cy + 120), "perto", lado=1, size=42)
        pilula_em(c, t, C["s05.a"] + 0.2, "periélio", cx + a - 40, cy - 90, 46, E.COR)
        E.foco(c, t, C["s05.b"], 0.5, lambda al: E.bola(c, cx - a, cy, 26, TERRA, al))
        cota(c, t, C["s05.b"] + 0.3, (cx - a, cy + 120), (fx, cy + 120), "longe", lado=1, size=42)
        pilula_em(c, t, C["s05.b"] + 0.2, "afélio", cx - a + 40, cy - 90, 46, TINTA)
        E.frase(c, t, C["s05"], ps("a distância ao Sol", "i", 70) + [("muda", "g", 70, COR)], XE, 190, passo=0.12)
    E.saida(c, t, C["s05.c"] - 0.1, s05)
    if t < C["s05.c"]:
        return
    pilula_em(c, t, C["s05.c"], "no desenho: achatada de propósito", W / 2, 200, 50, ERRADO)
    E.frase(c, t, C["s05.d"], ps("a órbita da Terra:", "i", 70) + [("quase um círculo", "g", 70, COR)], W / 2, 360, "center", 0.12)
    q = ep(t, C["s05.d"] + 0.5, 0.6)
    if q > 0:
        elipse(c, W / 2, 680, 260, 259.6, q)
        E.bola(c, W / 2 + 5, 680, 50, SOL, q)
        E.bola(c, W / 2 + 260 * math.cos(t * 0.6), 680 - 259.6 * math.sin(t * 0.6), 22, TERRA, q)
    E.frase(c, t, C["s05.d"] + 2.4, [("147", "g", 64), ("a", "i", 66), ("152", "g", 64), ("milhões de km", "i", 62, TINTA2)], W / 2, 1020, "center", 0.12)


# ---------------- segunda lei ----------------
AX, AY, AA, AB = 1000, 640, 500, 320
M_PERI = (-0.35, 0.35)   # trechos de mesmo tempo: perto e longe do Sol
M_AFE = (math.pi - 0.35, math.pi + 0.35)


def b_areas(c, t, C, b):
    fx = AX + foco(AA, AB)
    if t < C["s07"]:
        def s06():
            g = 0.45 * (t - C["s06"])
            P = sistema(c, t, C["s06"], AX, AY, AA, AB, giro=g, linha=t >= C["s06.b"])
            E.frase(c, t, C["s06.a"], [("2ª lei:", "g", 70), ("a velocidade", "i", 74)], XE, 170, passo=0.15)
            if t >= C["s06.c"]:
                setor(c, AX, AY, AA, AB, g - 0.9 * ease_io(prog(t, C["s06.c"], 1.0)), g, alfa=0.25)
            E.frase(c, t, C["s06.d"], ps("tempos iguais", "i", 66) + [("→", "g", 64, TINTA2), ("áreas iguais", "g", 66, COR)], XE, 1010, passo=0.12)
        E.saida(c, t, C["s06.d"] - 0.1, s06)
        if t >= C["s06.d"]:
            sistema(c, t, C["s06.d"], AX, AY, AA, AB, giro=0.0)
            setor(c, AX, AY, AA, AB, *M_PERI, p=ep(t, C["s06.d"] + 0.3, 0.9))
            setor(c, AX, AY, AA, AB, *M_AFE, p=ep(t, C["s06.d"] + 1.0, 0.9))
            E.frase(c, t, C["s06.d"], ps("tempos iguais", "i", 66) + [("→", "g", 64, TINTA2), ("áreas iguais", "g", 66, COR)], XE, 1010, passo=0.12)
        return
    sistema(c, t, C["s07"] - 0.3, AX, AY, AA, AB, giro=0.0)
    setor(c, AX, AY, AA, AB, *M_PERI)
    setor(c, AX, AY, AA, AB, *M_AFE)
    if t >= C["s07.a"]:
        M.line(c, fx, AY, AX + AA, AY, TINTA, ep(t, C["s07.a"], 0.4), 6)
    E.frase(c, t, C["s07.a"], ps("perto:", "i", 52) + [("linha curta", "g", 52)], 1440, 290, passo=0.1)
    arco_orb(c, AX, AY, AA, AB, *M_PERI, E.COR, 12, ep(t, C["s07.b"], 0.8))
    E.frase(c, t, C["s07.b"], ps("arco maior:", "i", 56), 1440, 380, passo=0.1)
    E.frase(c, t, C["s07.c"], [("mais rápido", "g", 60, COR)], 1440, 465)
    if t >= C["s07.d"]:
        M.line(c, fx, AY, AX - AA, AY, TINTA, ep(t, C["s07.d"], 0.5), 6)
    arco_orb(c, AX, AY, AA, AB, *M_AFE, F.NEG, 12, ep(t, C["s07.e"], 0.8))
    E.frase(c, t, C["s07.d"], ps("longe:", "i", 60) + [("linha comprida", "g", 60)], XE, 210, passo=0.1)
    E.frase(c, t, C["s07.e"], ps("arco curto:", "i", 60) + [("devagar", "g", 64, F.NEG)], XE, 300, passo=0.1)
    E.frase(c, t, C["s07.f"], [("periélio", "g", 62, COR), ("rápido", "i", 66), ("·", "g", 62, TINTA2), ("afélio", "g", 62, F.NEG), ("devagar", "i", 66)], W / 2, 1010, "center", 0.12)


# ---------------- terceira lei ----------------
def b_terceira(c, t, C, b):
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], [("3ª lei:", "g", 70)] + ps("o período e o tamanho da órbita", "i", 66), XE, 180, passo=0.1)
            F.formula_legenda(c, t, C["s08.c"], "f{T^2}{R^3} = constante", [("T", "período", "s"), ("R", "raio médio da órbita", "m")],
                              XE, 470, 110, tl=[C["s08.c"] + 0.4, C["s08.b"]], size_l=50)
            pilula_em(c, t, C["s08.d"], "o mesmo para todos os planetas do Sol", XE + 520, 800, 44, E.COR)
            sx, sy = 1480, 560
            q = ep(t, C["s08.b"] - 0.4, 0.5)
            if q > 0:
                circulo_orb(c, sx, sy, 300, q)
                E.bola(c, sx, sy, 50, SOL, q)
                g = 0.5 * t
                E.bola(c, sx + 300 * math.cos(g), sy - 300 * math.sin(g), 24, TERRA, q)
            cota(c, t, C["s08.b"], (sx, sy), (sx + 300, sy), "R", lado=-1, size=56)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            E.formula_em(c, t, C["s09.a"], "T^2 = T · T", XE, 300, 110, "g", TINTA)
            E.formula_em(c, t, C["s09.b"], "R^3 = R · R · R", XE, 470, 110, "g", TINTA)
            E.frase(c, t, C["s09.c"], ps("mais longe do Sol", "i", 66) + [("→", "g", 64, TINTA2), ("ano maior", "g", 66, COR)], XE, 700, passo=0.12)
            E.frase(c, t, C["s09.d"], ps("e o ano cresce", "i", 66) + [("mais depressa", "g", 66, COR)] + ps("que a distância", "i", 66), XE, 830, passo=0.1)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    if t < C["s11"]:
        def s10():
            sx, sy, r1 = 1460, 600, 100
            q = ep(t, C["s10.a"], 0.5)
            if q > 0:
                E.bola(c, sx, sy, 40, SOL, q)
                circulo_orb(c, sx, sy, r1, q)
                circulo_orb(c, sx, sy, 4 * r1, q)
                E.bola(c, sx + r1 * math.cos(t), sy - r1 * math.sin(t), 16, TERRA, q)
                E.bola(c, sx + 4 * r1 * math.cos(t / 8), sy - 4 * r1 * math.sin(t / 8), 26, LUA, q)
            cota(c, t, C["s10.c"], (sx, sy - 160), (sx + r1, sy - 160), "1", lado=-1, size=44)
            cota(c, t, C["s10.c"] + 0.4, (sx - 4 * r1, sy + 160), (sx, sy + 160), "4", lado=1, size=50)
            E.frase(c, t, C["s10.a"], ps("4 vezes mais longe", "i", 66), XE, 180, passo=0.12)
            E.frase(c, t, C["s10.b"], [("ano", "i", 66), ("?", "g", 70, COR)], XE, 280, passo=0.12)
            E.frase(c, t, C["s10.c"], [("distância:", "i", 52, TINTA2), ("Terra-Sol = 1", "g", 52)], XE, 420, passo=0.1)
            E.frase(c, t, C["s10.d"], [("tempo:", "i", 52, TINTA2), ("1 ano", "g", 52)], XE, 500, passo=0.1)
            E.formula_em(c, t, C["s10.e"], "Terra: f{1^2}{1^3} = 1", XE, 680, 80, "g", TINTA)
            E.formula_em(c, t, C["s10.f"], "T^2 = R^3", XE, 900, 120, "g", COR)
            E.frase(c, t, C["s10.f"] + 0.6, ps("nessas unidades", "i", 48, TINTA2), XE + 520, 900, passo=0.1)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    if t < C["s12"]:
        def s11():
            linhas(c, t, [(C["s11.a"], "R = 4  →  R^3 = 4^3 = 64", TINTA), (C["s11.b"], "T^2 = 64", TINTA), (C["s11.c"], "T = r{64}", TINTA)], XE, 260, 170, 92)
            bola_txt(c, t, C["s11.d"], "8 anos", 1450, 520, 170, 80)
            E.frase(c, t, C["s11.e"], [("4 ×", "g", 72, TINTA), ("mais longe", "i", 72), ("→", "g", 70, TINTA2), ("8 ×", "g", 72, COR), ("mais tempo", "i", 72)], W / 2, 930, "center", 0.12)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    E.frase(c, t, C["s12"], ps("cuidado:", "i", 70) + [("mesmo astro no centro", "g", 70, COR)], W / 2, 200, "center", 0.12)
    for i, (k_, cx, cor, nome, raz) in enumerate((("s12.a", 560, SOL, "planetas do Sol", "uma razão"), ("s12.b", 1360, "#C99A6B", "luas de Júpiter", "outra razão"))):
        q = ep(t, C[k_], 0.5)
        if q > 0:
            E.bola(c, cx, 580, 60, cor, q)
            for r_, v in ((150, 0.9), (240, 0.5)):
                circulo_orb(c, cx, 580, r_, q)
                E.bola(c, cx + r_ * math.cos(t * v), 580 - r_ * math.sin(t * v), 18, TERRA if i == 0 else LUA, q)
        E.foco(c, t, C[k_] + 0.3, 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx, 900, 52, "g", TINTA, a))
        E.foco(c, t, C["s12.c"] + 0.3 * i, 0.4, lambda a, cx=cx, raz=raz, i=i: E.pilula(c, raz, cx, 990, 44, "g", fundo=E.COR if i == 0 else F.NEG, a=a))
    E.foco(c, t, C["s12.c"] + 0.6, 0.4, lambda a: centro(c, "≠", W / 2, 1010, 90, "g", ERRADO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("verão = mais perto do Sol?", "i", 66), XE + 480, 190, passo=0.1)
    if C["s13.a"] + 1.5 <= t:
        E.risco(c, XE + 470, 205, XE + 1240, 150, t, C["s13.b"] - 0.3, largura=10)
    sx, sy = 640, 600
    q = ep(t, C["s13.b"], 0.5)
    if q > 0:
        elipse(c, 960, sy, 560, 300, q)
        E.bola(c, 960 + foco(560, 300) - 60, sy, 55, SOL, q)
        E.bola(c, 960 + 560, sy, 34, TERRA, q)
    pilula_em(c, t, C["s13.b"] + 0.4, "janeiro: o ponto mais perto", 1500, sy - 130, 42, TINTA)
    pilula_em(c, t, C["s13.c"], "Brasil: verão", 640, 520, 52, E.COR)
    pilula_em(c, t, C["s13.c"] + 0.7, "Europa: inverno", 640, 660, 52, F.NEG)
    E.frase(c, t, C["s13.d"], ps("a distância muda pouco:", "i", 60) + [("não explica as estações", "g", 58, ERRADO)], W / 2, 960, "center", 0.1)
    E.frase(c, t, C["s13.e"], ps("é a inclinação do eixo (outra aula)", "i", 52, TINTA2), W / 2, 1040, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s14.a"], [("raio", "i", 76, CLARO), ("× k", "g", 80, BR)], W / 2 - 330, 340, "center", 0.12)
            E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.formula(c, "→", W / 2 - 120, 340, 80, "g", CLARO, a),
                                                      E.escreve(c, "período", W / 2 - 10, 340, 76, "i", CLARO, a),
                                                      E.formula(c, "× k · r{k}", W / 2 + 270, 340, 80, "g", BR, a)))
            E.formula_em(c, t, C["s14.c"], "4  →  4 · r{4} = 4 · 2 =", W / 2 - 110, 580, 96, "g", BR, "center")
            bola_txt(c, t, C["s14.d"], "8 ×", W / 2 + 470, 550, 85, 60)
            E.formula_em(c, t, C["s14.e"], "9  →  9 · r{9} = 9 · 3 =", W / 2 - 110, 820, 96, "g", BR, "center")
            bola_txt(c, t, C["s14.f"], "27 ×", W / 2 + 470, 790, 85, 56)
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], [("T²", "g", 76, BR)] + ps("acompanha", "i", 76, CLARO) + [("R³", "g", 76, BR)], W / 2, 200, "center", 0.12)
    E.formula_em(c, t, C["s15.b"], "4^3 = 64,   r{64} = 8 = 4 · 2", W / 2, 420, 96, "g", CLARO, "center")
    E.frase(c, t, C["s15.c"], ps("compensa com raiz exata:", "i", 66, CLARO) + [("4, 9, 16", "g", 66, BR)], W / 2, 680, "center", 0.12)
    E.frase(c, t, C["s15.d"], ps("senão,", "i", 66, CLARO) + [("faça a conta inteira", "g", 64, BR)], W / 2, 840, "center", 0.12)


# ---------------- questão ----------------
def dois_planetas(c, t, t0, cx, cy, r1, r2, a=1.0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    E.bola(c, cx, cy, 46, SOL, q)
    circulo_orb(c, cx, cy, r1, q)
    circulo_orb(c, cx, cy, r2, q)
    E.bola(c, cx + r1 * math.cos(t * 1.2), cy - r1 * math.sin(t * 1.2), 16, TERRA, q)
    E.bola(c, cx + r2 * math.cos(t * 0.15 + 2), cy - r2 * math.sin(t * 0.15 + 2), 26, LUA, q)


def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s16")
    E.frase(c, t, C["s16.a"], ps("2 planetas, a mesma estrela", "i", 64), XE, 310, passo=0.1)
    E.frase(c, t, C["s16.b"], [("raio", "i", 66), ("16 vezes", "g", 66, COR), ("maior", "i", 66)], XE, 430, passo=0.12)
    E.frase(c, t, C["s16.c"], ps("o ano: quantas vezes maior?", "i", 66), XE, 600, passo=0.1)
    E.frase(c, t, C["s16.d"], ps("onde ele é", "i", 66) + [("mais rápido?", "g", 66, COR)], XE, 720, passo=0.1)
    if t < C["s17"]:
        dois_planetas(c, t, C["s16.a"], 1450, 560, 90, 380)
        cota(c, t, C["s16.b"], (1450, 560 + 130), (1450 + 380, 560 + 130), "16 R", lado=1, size=50)
        cota(c, t, C["s16.b"], (1450, 560 - 30), (1450 + 90, 560 - 30), "R", lado=-1, size=44)
        pilula_em(c, t, C["s16.b"] + 0.6, "fora de escala", 1450, 1000, 40, TINTA2)
    else:
        E.relogio(c, t, C["s17.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        def s18():
            E.frase(c, t, C["s18.a"], ps("mesma estrela:", "i", 64) + [("mesma razão", "g", 64, COR)], XE, 220, passo=0.12)
            E.formula_em(c, t, C["s18.b"], "raio × 16  →  período × 16 · r{16}", XE, 400, 84, "g", TINTA)
            E.formula_em(c, t, C["s18.c"], "= 16 · 4", XE, 560, 96, "g", TINTA)
            bola_txt(c, t, C["s18.d"], "64 vezes", 1500, 600, 150, 64, CERTO)
            E.formula_em(c, t, C["s18.e"], "64^2 = 4.096", XE, 830, 90, "g", TINTA2)
            E.formula_em(c, t, C["s18.f"], "16^3 = 4.096", XE + 720, 830, 90, "g", TINTA2)
        E.saida(c, t, C["s19"] - 0.1, s18)
        return
    g = 0.5 * (t - C["s19"])
    sistema(c, t, C["s19"], 1100, 620, 520, 333, giro=g)
    setor(c, 1100, 620, 520, 333, -0.4, 0.4, p=ep(t, C["s19.b"], 0.9))
    E.frase(c, t, C["s19.a"], [("mais rápido", "g", 70, CERTO)] + ps("perto da estrela", "i", 70), XE, 190, passo=0.12)
    E.frase(c, t, C["s19.b"], ps("arco maior para a mesma área", "i", 60, TINTA2), XE, 1000, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s21"]:
        E.saida(c, t, C["s21"] - 0.1, lambda: resumo(c, t, C, "s20", (
            ("s20.a", [("elipse", "g", 66, COR), ("com o Sol", "i", 70), ("num foco", "g", 66)]),
            ("s20.b", [("áreas iguais,", "g", 66), ("tempos iguais", "i", 70)]),
            ("s20.c", [("T² / R³", "g", 66, COR), ("igual", "i", 70), ("em volta do mesmo astro", "i", 70)]))))
        return

    def desenho():
        q = ep(t, C["s21.b"], 0.6)
        if q <= 0:
            return
        E.bola(c, 600, 820, 110 * q, TERRA, q)
        E.bola(c, 1080, 820, 40 * q, LUA, q)
        F.seta(c, 700, 820, 860, 820, E.COR, q, 10)
        F.seta(c, 1040, 820, 920, 820, E.COR, q, 10)
    proxima(c, t, C, "s21", [("Gravitação", "g", 120, COR)], [("universal", "i", 110)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, elipse=b_elipse, areas=b_areas, terceira=b_terceira, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
