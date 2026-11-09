"""Visual — Estudativo · FIS-EGF-014: praticando: torque e gravitação.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-014_praticando_torque_e_gravitacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))

# todas as contas da aula
assert abs(800 * 0.4 - 320) < 1e-9 and abs(320 / 1.6 - 200) < 1e-9 and abs(1.6 / 0.4 - 4) < 1e-9
assert abs(80 * 1.5 - 120) < 1e-9 and 30 * 2 == 60 and (120 - 60) / 20 == 3 and 800 + 300 + 200 == 1300
assert 2 * 4 * math.isqrt(4) == 16 and 800 / 2 ** 2 == 200 and 6 ** 2 * 1 == 36 and 36 / 9 == 4 and math.isqrt(4) == 2


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


# ---------------- peças desta aula (gangorra copiada da FIS-EGF-001) ----------------
def tabua(c, cx, cy, L, ang=0.0, a=1.0, esp=26):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    M.rrect(c, -L / 2, -esp / 2, L, esp, 8, MADEIRA, a)
    M.line(c, -L / 2 + 10, -esp / 2 + 6, L / 2 - 10, -esp / 2 + 6, "#D19A66", a * 0.7, 3)
    c.restore()


def sobre(cx, cy, u, h):
    """centro de um bloco de altura h sentado na tábua (horizontal) a u pixels do eixo"""
    return cx + u, cy - 13 - h / 2


def tracejado_circ(c, cx, cy, r, q, cor=TINTA, larg=4):
    pt = M.paint(cor, 0.7 * q, stroke=larg)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawCircle(cx, cy, r, pt)


def situacao(c, t, t0, n, titulo):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, 160, 44, a=a), centro(c, str(n), XE + 40, 180, 54, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("situação", "i", 66), (titulo, "g", 62, COR)], XE + 110, 180, passo=0.12)


def enunciado(c, t, C, cena, n, titulo, linhas, desenho):
    """tela da questão: título, linhas [(instante, partes, y)] e o desenho à direita; na cena da pausa, o relógio"""
    situacao(c, t, C[cena], n, titulo)
    for t0, partes, y in linhas:
        E.frase(c, t, t0, partes, XE, y, passo=0.1)
    pausa = f"s{int(cena[1:]) + 1:02d}"
    if t < C[pausa]:
        desenho()
    else:
        E.relogio(c, t, C[pausa + ".a"], cx=1480, cy=480, r=200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 110)], XE, 380, passo=0.2)
    E.frase(c, t, C["s01.a"] + 1.0, ps("criadas para esta aula", "i", 60, TINTA2), XE, 480, passo=0.1)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: (apoio(c, 1150, 413, 60, a), M.rrect(c, 1000, 387, 300, 26, 8, MADEIRA, a),
                                              centro(c, "alavanca", 1150, 530, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s01.c"], 0.5, lambda a: (E.bola(c, 1550, 400, 60, TERRA, a), F.bloco(c, 1650, 300, 34, 34, None, a=a),
                                              centro(c, "satélite", 1600, 530, 46, "i", TINTA2, a)))
    E.frase(c, t, C["s01.d"], ps("pause o vídeo e", "i", 70) + [("resolva antes", "g", 70, COR)], XE, 760, passo=0.12)


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s02", (("s02.a", "torque:", "força × braço, do eixo"), ("s02.b", "Kepler:", "T² / R³ constante"),
                              ("s02.c", "gravitação:", "cai com a distância²"), ("s02.d", "satélites:", "v² · R constante")), 4, "ferramentas")


# ---------------- situação 1: carrinho de mão ----------------
CX, CY, CK = 1150, 700, 400  # eixo (roda), altura da tábua, pixels por metro


def carrinho_mao(c, t, t0, ta, tb):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    E.bola(c, CX, CY + 60, 60, TINTA2, q)
    c.drawCircle(CX, CY + 60, 12, M.paint(E.COR, q))
    tabua(c, CX + 0.8 * CK, CY, 1.6 * CK + 60, 0, q)
    F.chao(c, CX - 140, CX + 140, CY + 122, q * 0.8)
    cx, cy = sobre(CX, CY, 0.4 * CK, 130)
    E.foco(c, t, ta, 0.5, lambda a: F.bloco(c, cx, cy, 160, 130, "800 N", a=a, size=38))
    cota(c, t, ta + 0.3, (CX, CY - 200), (CX + 0.4 * CK, CY - 200), "0,4 m", lado=-1, size=40)
    empurra(c, t, tb, (CX + 1.6 * CK, CY + 13), 90, 170, None, None)
    E.foco(c, t, tb + 0.3, 0.4, lambda a: E.escreve(c, "F?", CX + 1.6 * CK - 110, CY + 150, 60, "g", COR, a))
    cota(c, t, tb + 0.3, (CX, CY + 220), (CX + 1.6 * CK, CY + 220), "1,6 m", lado=1, size=44)


def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03", 1, "carrinho de mão", [
        (C["s03.b"], ps("a roda é o", "i", 60) + [("eixo", "g", 60, COR)], 330),
        (C["s03.c"], [("carga", "i", 60), ("800 N", "g", 60), ("a", "i", 60), ("0,4 m", "g", 60)], 450),
        (C["s03.d"], [("mãos a", "i", 60), ("1,6 m", "g", 60)], 570),
        (C["s03.e"], ps("que força", "i", 70) + [("F?", "g", 70, COR)], 720)],
        lambda: carrinho_mao(c, t, C["s03.b"], C["s03.c"], C["s03.d"]))


def b_resposta1(c, t, C, b):
    linhas(c, t, [(C["s05.a"], "M = 800 · 0,4", TINTA), (C["s05.c"], "F · 1,6 = 320", TINTA)], XE, 260, 170, 84)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.formula(c, "= 320 N·m", XE + E.formula(None, "M = 800 · 0,4 ", 0, 0, 84, a=0), 260, 84, "g", COR, a))
    bola_txt(c, t, C["s05.d"], "F = 200 N", 1450, 380, 160, 58, CERTO)
    E.frase(c, t, C["s05.e"], [("braço", "i", 66), ("× 4", "g", 66, COR), ("→", "g", 62, TINTA2), ("força", "i", 66), ("÷ 4", "g", 66, COR)], XE, 700, passo=0.12)
    E.formula_em(c, t, C["s05.e"] + 1.6, "800 ÷ 4 = 200", XE, 860, 84, "g", TINTA2)


# ---------------- situação 2: gangorra de três ----------------
GX, GY, GK = 1270, 880, 180


def gangorra3(c, t, t0, tp, tf, tm, d_filha=None):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    p = skia.Path(); p.moveTo(GX, GY + 13); p.lineTo(GX - 56, GY + 93); p.lineTo(GX + 56, GY + 93); p.close()
    c.drawPath(p, M.paint(TINTA, q))
    tabua(c, GX, GY, 6 * GK, 0, q)
    F.chao(c, GX - 3 * GK - 40, GX + 3 * GK + 40, GY + 93, q * 0.8)
    for ti, u, w, h, rot in ((tp, -1.5, 130, 130, "80 kg"), (tf, 2, 100, 100, "30 kg")):
        cx, cy = sobre(GX, GY, u * GK, h)
        E.foco(c, t, ti, 0.5, lambda a, cx=cx, cy=cy, w=w, h=h, rot=rot: F.bloco(c, cx, cy, w, h, rot, a=a, size=34))
    cota(c, t, tp + 0.3, (GX - 1.5 * GK, GY + 130), (GX, GY + 130), "1,5 m", lado=1, size=38)
    cota(c, t, tf + 0.3, (GX, GY + 130), (GX + 2 * GK, GY + 130), "2 m", lado=1, size=38)
    u = d_filha if d_filha is not None else 2.6
    cx, cy = sobre(GX, GY, u * GK, 80)
    E.foco(c, t, tm, 0.5, lambda a: F.bloco(c, cx, cy, 80, 80, "20", a=a, size=30, cor=E.COR if d_filha else E.mix(E.COR, BR, 0.4)))
    if d_filha is None:
        E.foco(c, t, tm + 0.3, 0.4, lambda a: centro(c, "?", cx, cy - 70, 60, "g", COR, a))


def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s06", 2, "a gangorra de três", [
        (C["s06.a"], [("6 m,", "g", 56), ("apoio no meio", "i", 58)], 320),
        (C["s06.b"], [("pai", "i", 58), ("80 kg", "g", 58), ("a", "i", 58), ("1,5 m", "g", 58)], 430),
        (C["s06.c"], [("filho", "i", 58), ("30 kg", "g", 58), ("a", "i", 58), ("2 m", "g", 58)], 540),
        (C["s06.d"], [("filha", "i", 64), ("20 kg:", "g", 64), ("a que distância?", "i", 64, COR)], 690)],
        lambda: gangorra3(c, t, C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]))


def b_resposta2(c, t, C, b):
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], ps("só pesos:", "i", 60) + [("o 10 corta", "g", 60, COR)], XE, 200, passo=0.12)
            linhas(c, t, [(C["s08.b"], "pai: 80 · 1,5 = 120", F.NEG), (C["s08.c"], "filhos: 30 · 2 + 20 · d", COR),
                          (C["s08.d"], "60 + 20 d = 120", TINTA), (C["s08.e"], "20 d = 60", TINTA)], XE, 350, 140, 72)
            bola_txt(c, t, C["s08.f"], "d = 3 m", 1500, 420, 150, 60, CERTO)
            pilula_em(c, t, C["s08.g"], "na ponta da gangorra", 1500, 650, 46, TINTA)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    gangorra3(c, t, C["s09"], C["s09"], C["s09"], C["s09"], d_filha=3)
    F.forca(c, t, C["s09.b"], (GX, GY - 13), 90, 280, "N", lado=-1)
    E.frase(c, t, C["s09.a"], ps("e o apoio?", "i", 70), XE, 220, passo=0.12)
    E.formula_em(c, t, C["s09.c"], "N = 800 + 300 + 200", XE, 400, 76, "g", TINTA)
    bola_txt(c, t, C["s09.d"], "1.300 N", 500, 590, 120, 52, CERTO)


# ---------------- situação 3: duas luas ----------------
def duas_luas(c, t, t0, tb, ta_):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cx, cy = 1450, 560
    E.bola(c, cx, cy, 60, "#C99A6B", q)
    tracejado_circ(c, cx, cy, 95, q)
    tracejado_circ(c, cx, cy, 380, ep(t, tb, 0.5))
    E.bola(c, cx + 95 * math.cos(1.4 * t), cy - 95 * math.sin(1.4 * t), 16, LUA, q)
    E.foco(c, t, tb, 0.5, lambda a: E.bola(c, cx + 380 * math.cos(0.18 * t + 2), cy - 380 * math.sin(0.18 * t + 2), 24, LUA, a))
    E.foco(c, t, ta_, 0.4, lambda a: E.escreve(c, "A: 2 dias", cx + 120, cy + 20, 40, "b", TINTA, a))
    cota(c, t, tb + 0.3, (cx, cy + 420), (cx + 380, cy + 420), "4 R", lado=1, size=44)


def b_questao3(c, t, C, b):
    enunciado(c, t, C, "s10", 3, "duas luas", [
        (C["s10.b"], ps("mesmo planeta", "i", 60), 320),
        (C["s10.c"], [("lua A:", "i", 60), ("2 dias", "g", 60)], 430),
        (C["s10.d"], [("lua B:", "i", 60), ("raio × 4", "g", 60)], 540),
        (C["s10.e"], [("período de B?", "g", 66, COR)], 690)],
        lambda: duas_luas(c, t, C["s10.b"], C["s10.d"], C["s10.c"]))


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("mesmo planeta:", "i", 60) + [("T² / R³ igual", "g", 60, COR)], XE, 220, passo=0.12)
    linhas(c, t, [(C["s12.b"], "raio × 4", TINTA), (C["s12.c"], "período × 4 · r{4} = 4 · 2 = 8", TINTA), (C["s12.e"], "2 dias × 8", TINTA)], XE, 400, 170, 80)
    bola_txt(c, t, C["s12.f"], "16 dias", 1500, 560, 150, 60, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho que serviu duas vezes", "i", 70, CLARO), W / 2, 170, "center", 0.1)
    E.frase(c, t, C["s13.a"], ps("antes da conta,", "i", 76, CLARO) + [("procure o fator", "g", 76, BR)], W / 2, 330, "center", 0.12)
    E.formula_em(c, t, C["s13.b"], "braço × 4  →  força ÷ 4", W / 2, 500, 84, "g", CLARO, "center")
    E.formula_em(c, t, C["s13.c"], "raio × 4  →  período × 8", W / 2, 640, 84, "g", CLARO, "center")
    E.frase(c, t, C["s13.d"], ps("uma multiplicação só", "i", 64, CLARO), W / 2, 780, "center", 0.1)
    E.frase(c, t, C["s13.e"], [("mais de duas forças:", "g", 56, BR)] + ps("some os torques", "i", 60, CLARO), W / 2, 920, "center", 0.1)


# ---------------- situação 4: peso em órbita ----------------
def astronauta(c, t, t0, tc):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cx, cy, R = 1300, 600, 180
    E.bola(c, cx, cy, R, TERRA, q)
    c.drawCircle(cx, cy, 8, M.paint(BR, q))
    F.bloco(c, cx, cy - R - 30, 40, 60, None, a=q)
    E.foco(c, t, tc, 0.5, lambda a: F.bloco(c, cx + 2 * R, cy, 40, 60, None, a=a))
    cota(c, t, tc + 0.3, (cx + R, cy - 120), (cx + 2 * R, cy - 120), "altura = R", lado=-1, size=40)
    cota(c, t, tc + 0.6, (cx, cy + 260), (cx + 2 * R, cy + 260), "2R do centro", lado=1, size=44)


def b_questao4(c, t, C, b):
    enunciado(c, t, C, "s14", 4, "o astronauta", [
        (C["s14.b"], [("800 N", "g", 60), ("na superfície", "i", 60)], 330),
        (C["s14.c"], [("a uma altura", "i", 60), ("= R", "g", 60), ("?", "g", 60, COR)], 450),
        (C["s14.d"], ps("por que ele", "i", 64) + [("flutua?", "g", 64, COR)], 620)],
        lambda: astronauta(c, t, C["s14.b"], C["s14.c"]))


def b_resposta4(c, t, C, b):
    if t < C["s17"]:
        def s16():
            astronauta(c, t, C["s16"] - 0.2, C["s16"] - 0.2)
            E.frase(c, t, C["s16.a"], ps("do", "i", 64) + [("centro da Terra", "g", 64, COR)], XE, 220, passo=0.12)
            E.formula_em(c, t, C["s16.b"], "R + R = 2R", XE, 400, 84, "g", TINTA)
            E.formula_em(c, t, C["s16.d"], "d × 2  →  F ÷ 4", XE, 560, 84, "g", TINTA)
            bola_txt(c, t, C["s16.e"], "200 N", 470, 770, 130, 60, CERTO)
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    E.frase(c, t, C["s17.a"], ps("flutua porque", "i", 70) + [("cai junto com a nave", "g", 66, COR)], XE, 300, passo=0.12)
    E.frase(c, t, C["s17.b"], ps("a gravidade", "i", 70) + [("está lá:", "g", 70)], XE, 480, passo=0.12)
    E.frase(c, t, C["s17.c"], ps("ela segura a nave", "i", 70) + [("na órbita", "g", 70, COR)], XE, 620, passo=0.12)


# ---------------- situação 5: dois satélites ----------------
def dois_sat(c, t, t0, tc):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    cx, cy = 1450, 560
    E.bola(c, cx, cy, 70, TERRA, q)
    tracejado_circ(c, cx, cy, 120, q)
    F.bloco(c, cx + 120 * math.cos(1.2 * t), cy - 120 * math.sin(1.2 * t), 28, 28, None, a=q)
    if t >= tc:
        tracejado_circ(c, cx, cy, 400, ep(t, tc, 0.5))
        F.bloco(c, cx + 400 * math.cos(0.15 * t + 1), cy - 400 * math.sin(0.15 * t + 1), 34, 34, None, a=ep(t, tc, 0.5))
        cota(c, t, tc + 0.3, (cx, cy + 440), (cx + 400, cy + 440), "9 R", lado=1, size=44)


def b_questao5(c, t, C, b):
    enunciado(c, t, C, "s18", 5, "dois satélites", [
        (C["s18.b"], [("satélite 1:", "i", 60), ("6 km/s", "g", 60)], 330),
        (C["s18.c"], [("satélite 2:", "i", 60), ("raio × 9", "g", 60)], 450),
        (C["s18.d"], [("velocidade do 2?", "g", 66, COR)], 620)],
        lambda: dois_sat(c, t, C["s18.b"], C["s18.c"]))


def b_resposta5(c, t, C, b):
    E.formula_em(c, t, C["s20.a"], "v^2 · R = constante", XE, 230, 84, "g", COR)
    linhas(c, t, [(C["s20.b"], "6^2 · 1 = 36", TINTA), (C["s20.c"], "v^2 · 9 = 36", TINTA), (C["s20.d"], "v^2 = 4", TINTA)], XE, 400, 150, 80)
    bola_txt(c, t, C["s20.e"], "2 km/s", 1450, 520, 150, 60, CERTO)
    E.frase(c, t, C["s20.f"], [("raio × 9", "g", 64), ("→", "g", 60, TINTA2), ("velocidade ÷ 3", "g", 64, COR)], XE, 900, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s22"]:
        E.saida(c, t, C["s22"] - 0.1, lambda: resumo(c, t, C, "s21", (
            ("s21.a", [("torque:", "g", 66), ("sempre a partir do", "i", 70), ("eixo", "g", 66, COR)]),
            ("s21.b", [("órbita maior:", "g", 64), ("período maior,", "i", 68), ("velocidade menor", "g", 64, COR)]),
            ("s21.c", [("gravitação:", "g", 64), ("distância do", "i", 68), ("centro", "g", 64, COR)]))))
        return

    def desenho():
        q = ep(t, C["s22.b"], 0.6)
        if q <= 0:
            return
        p = skia.Path(); p.moveTo(380, 760); p.lineTo(900, 790); p.lineTo(380, 820); p.close()
        c.drawPath(p, M.paint("#B9BCC4", q))
        M.rrect(c, 180, 765, 210, 52, 14, TINTA, q)
        E.bola(c, 1080, 820, 90, "#D8342C", q)
    proxima(c, t, C, "s22", [("Pressão:", "g", 120, COR)], [("força por área", "i", 100)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
