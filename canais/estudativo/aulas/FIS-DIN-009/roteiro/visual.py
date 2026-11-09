"""Visual — Estudativo · FIS-DIN-009: blocos ligados e polias (o atalho do corpo só e a tração).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula: o "corpo só" é uma caixa
pontilhada em volta dos blocos; as trações internas aparecem e são riscadas quando a caixa fecha; a aceleração comum é uma
seta violeta ao longo do fio. Todo instante vem de C[...]."""
import math
import re

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Dinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
MARCA = ""
BACKGROUND = E.fundo
BR = "#FFFFFF"
ARQUIVO_FINAL = "estudativo_FIS-DIN-009_blocos_ligados_e_polias.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("junto", "polia", "atrito", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²)
assert 20 / (2 + 3) == 4 and 2 * 4 == 8 and (20 - 8) / 3 == 4
assert 4 * 10 / (6 + 4) == 4 and 6 * 4 == 24 and (40 - 24) / 4 == 4
assert 0.5 * 60 == 30 and (40 - 30) / 10 == 1 and 30 + 6 * 1 == 36 and (40 - 36) / 4 == 1
assert (30 - 20) / (3 + 2) == 2 and 20 + 2 * 2 == 24 and (30 - 24) / 3 == 2

def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha de Dinâmica (iguais em todas as aulas FIS-DIN; candidatas a fisica.py) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _partes_sub(s):
    return [(p, i % 2 == 1) for i, p in enumerate(re.split(r"_\{([^}]*)\}", s)) if p]


def sub(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """fórmula com subscrito: "F_{R} = m · a", "F_{at} = μ · N". Aceita a escrita de E.formula nos trechos. Devolve a largura"""
    partes = _partes_sub(s)
    ws = [E.formula(None, p, 0, 0, size * (0.6 if b else 1), E._est(p, est), a=0) + (size * 0.03 if b else 0) for p, b in partes]
    w = sum(ws)
    if c is not None and a > 0:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        for (p, b), wi in zip(partes, ws):
            E.formula(c, p, xi, y + (size * 0.2 if b else 0), size * (0.6 if b else 1), E._est(p, est), cor or TINTA, a)
            xi += wi
    return w


def sub_em(c, t, t0, s, x, y, size, est="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: sub(c, s, x, y, size, est, cor, a, align))


def contas(c, t, linhas, x, y0, size=80, dy=None, align="left", est="g"):
    """uma conta por linha, cada uma na sua fala: linhas = [(instante, texto[, cor])]"""
    dy = dy or size * 1.35
    for i, li in enumerate(linhas):
        sub_em(c, t, li[0], li[1], x, y0 + i * dy, size, est, li[2] if len(li) > 2 else TINTA, align)


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


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def rot_vetor(c, s, cx, yb, size, cor, a):
    """letra de força (com subscrito: "F_{R}") e a setinha de vetor sobre a letra principal; cx = centro, yb = linha de base"""
    w = sub(None, s, 0, 0, size)
    if c is None or a <= 0:
        return w
    x0 = cx - w / 2
    sub(c, s, x0, yb, size, "g", cor, a)
    wb = sub(None, s.split("_{")[0], 0, 0, size)
    ys, hw, mx = yb - size * 0.98, wb / 2 + size * 0.04, x0 + wb / 2
    M.line(c, mx - hw, ys, mx + hw - size * 0.05, ys, cor, a, max(3, size * 0.07))
    F._cabeca(c, mx + hw + size * 0.06, ys, 1, 0, size * 0.2, cor, a)
    return w


def seta_f(c, t, t0, P, ang, comp, rot=None, cor=None, modulo=None, lpos=None, size=56, larg=9, escuro=False, d=0.5):
    """força que sai de P no ângulo ang (graus, 90 = para cima) com comp px; rótulo (letra e/ou módulo) com centro em lpos
    (x, linha de base). Sem lpos, o rótulo fica depois da ponta. Devolve a ponta"""
    dx, dy = F._dir(ang)
    B = (P[0] + dx * comp, P[1] + dy * comp)
    if t < t0:
        return B
    cor = cor or E.COR
    F.seta(c, *P, *B, cor, 1.0, larg, p=ease_out(prog(t, t0, d)))
    if rot or modulo:
        if lpos is None:
            lpos = (B[0] + dx * size * 1.1, B[1] + dy * size * 0.9 + size * 0.36)
        cr = (E.CLARO if escuro else E.COR_TEXTO) if cor == E.COR else cor
        tinta = BR if escuro else TINTA

        def lab(a):
            v, _, u = (modulo or "").partition(" ")
            w1 = rot_vetor(None, rot, 0, 0, size, cr, 0) if rot else 0
            w2 = F.medida(None, v, u, 0, 0, size * 0.8) if modulo else 0
            gap = size * 0.4 if rot and modulo else 0
            x0 = lpos[0] - (w1 + gap + w2) / 2
            if rot:
                rot_vetor(c, rot, x0 + w1 / 2, lpos[1], size, cr, a)
            if modulo:
                F.medida(c, v, u, x0 + w1 + gap, lpos[1], size * 0.8, tinta, a, escuro=escuro)
        E.foco(c, t, t0 + d * 0.7, 0.4, lab)
    return B


def lembrete(c, t, C, cena, itens):
    """'você precisa de N coisas' à esquerda e uma caixa por item, cada uma no seu cue: itens = [(cue, linha fina, linha forte)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, y0 = (230, 290, 200) if n == 2 else (200, 240, 120)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + h * 0.42)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + h * 0.42 + 80)
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            x, y0 + (n - 1) * gap + h + 90, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """'até o fim da aula' + itens numerados (curtos) + a órbita da Física: itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    dy = 150 if len(itens) <= 3 else 128
    for i, (k, s, dt) in enumerate(itens):
        y = 430 + i * dy
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a),
                                                       centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 72, COR if i == 0 else TINTA)], XE + 110, y)


def pausa(c, t, C, cena_p, desenho, cx=1460, cy=440):
    """na cena da pausa, o desenho da questão dá lugar ao relógio"""
    if t < C[cena_p]:
        desenho()
    else:
        E.relogio(c, t, C[cena_p + ".a"], cx=cx, cy=cy, r=200)


def cabeca_q(c, t, C, cena, texto="hora de testar"):
    E.frase(c, t, C[cena], ps(texto, "i", 72, COR), XE, 190)


def resumo(c, t, C, cena, itens, t_fim):
    """'resumindo' + itens numerados: itens = [(cue, partes de E.frase)]; some em t_fim"""
    def fn():
        E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        dy = 170 if len(itens) <= 4 else 140
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * dy
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)
    E.saida(c, t, t_fim - 0.1, fn)


def proxima(c, t, C, cena, linhas, insc, bons, desenho=None):
    """ponte para a próxima aula: linhas = [(instante, partes)], desenho(a) embaixo à esquerda; pílula Inscreva-se e despedida"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    for i, (ti, partes) in enumerate(linhas):
        E.frase(c, t, ti, partes, XE, 400 + i * 140, passo=0.12)
    if desenho:
        desenho()
    E.foco(c, t, C[insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[insc] + 0.2, 0.4))
    E.frase(c, t, C[bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def formula_nova(c, t, t0, s, x, y, size, legendas, tl, size_l=54, dy=None):
    """fórmula nova: grande em tinta e, embaixo, cada letra em laranja + nome + (unidade do SI), cada linha em tl[i]"""
    sub_em(c, t, t0, s, x, y, size, "g", TINTA)
    dy = dy or size_l * 1.5
    for i, (letra, nome, unid) in enumerate(legendas):
        yy = y + size * 0.5 + size_l * 1.4 + i * dy

        def lin(a, letra=letra, nome=nome, unid=unid, yy=yy):
            wl = sub(c, letra, x, yy, size_l * 1.1, "g", COR, a)
            xx = x + max(wl, size_l * 0.9) + size_l * 0.5
            E.escreve(c, nome, xx, yy, size_l, "i", TINTA, a)
            if unid:
                E.formula(c, f"({unid})", xx + E.larg(nome, "i", size_l) + size_l * 0.4, yy, size_l * 0.9, "b", F.UNID, a)
        E.foco(c, t, tl[i], 0.5, lin)


def risca_em(c, t, t0, x0, y0, x1, y1, larg_=10):
    if t >= t0:
        E.risco(c, x0, y0, x1, y1, t, t0, largura=larg_)


# ---------------- desenhos de apoio ----------------
def pessoa(c, x, y, s, a=1.0, cor=None, inclina=0.0, braco=None, sentido=1):
    """pessoa de traço: pés em y, altura ~3,4·s. inclina = graus para a frente; braco = ângulo dos braços (graus, 0 = para a frente)"""
    if a <= 0:
        return
    cor = cor or TINTA2
    sg = 1 if sentido > 0 else -1
    g = math.radians(inclina) * sg
    quadril = (x, y - 1.5 * s)
    ombro = (quadril[0] + math.sin(g) * 1.3 * s, quadril[1] - math.cos(g) * 1.3 * s)
    cabeca = (ombro[0] + math.sin(g) * 0.55 * s, ombro[1] - math.cos(g) * 0.55 * s)
    lw = max(5, s * 0.2)
    for dx in (-0.35, 0.35):
        M.line(c, *quadril, x + dx * s + sg * s * 0.25 * (inclina / 30), y, cor, a, lw)
    M.line(c, *quadril, *ombro, cor, a, lw)
    br = math.radians(braco if braco is not None else -70)
    for k in (0, 0.18):
        M.line(c, *ombro, ombro[0] + sg * math.cos(br + k) * 1.2 * s, ombro[1] - math.sin(br + k) * 1.2 * s, cor, a, lw)
    c.drawCircle(*cabeca, 0.36 * s, M.paint(cor, a))


def polia(c, cx, cy, r, a=1.0, suporte=None):
    """roldana com eixo; suporte = (x, y) do ponto de fixação (desenha a haste até lá)"""
    if a <= 0:
        return
    if suporte:
        M.line(c, cx, cy, *suporte, TINTA2, a, 8)
    c.drawCircle(cx, cy, r, M.paint("#C9C9C4", a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=6))
    c.drawCircle(cx, cy, r * 0.62, M.paint(TINTA2, a * 0.5, stroke=3))
    c.drawCircle(cx, cy, r * 0.16, M.paint(TINTA, a))


def balanca_chao(c, cx, y, w, texto, a=1.0):
    """balança de banheiro com o visor; y = topo da balança (onde a pessoa pisa)"""
    if a <= 0:
        return
    h = w * 0.16
    M.rrect(c, cx - w / 2, y, w, h, h * 0.35, "#E4E4E0", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y, w, h), h * 0.35, h * 0.35), M.paint(TINTA2, a, stroke=4))
    vw, vh = w * 0.42, h * 0.62
    M.rrect(c, cx - vw / 2, y + (h - vh) / 2, vw, vh, 8, "#1B1B20", a)
    v, _, u = texto.partition(" ")
    F.medida(c, v, u, cx, y + h / 2 + vh * 0.3, vh * 0.72, "#7CFFB2", a, "center", cor_u="#7CFFB2")


def elevador(c, x, y, w, h, a=1.0):
    """cabine de elevador com o cabo; (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    M.line(c, x + w / 2, y - 260, x + w / 2, y, TINTA2, a, 6)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint("#FFFFFF", 0.55 * a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint(TINTA, a, stroke=6))


# ---------------- peças desta aula ----------------
MADEIRA = "#8B5E3C"


def mesa_polia(c, t, t0, x0, y, L, mA, mB, s=0.0, wA=200, hA=150, wB=150, hB=130, cor_b=None):
    """mesa (tampo em y, de x0 a x0+L), polia na borda direita, bloco A na mesa e B pendurado; s = quanto já andou (px).
    Devolve dict com centros de A e B, a ponta do fio em A, e a polia"""
    q = ep(t, t0, 0.5)
    pr = 34
    px, py = x0 + L + pr * 0.2, y - pr
    ax = x0 + L * 0.35 + s
    ay = y - hA / 2
    by = y + 140 + s
    if q > 0:
        M.rrect(c, x0, y, L, 26, 6, MADEIRA, q)
        M.rrect(c, x0 + 30, y + 22, 26, 260, 5, "#6E4A2F", q)
        M.line(c, ax + wA / 2, py - pr, px, py - pr, TINTA2, q, 5)
        M.line(c, px + pr, py, px + pr, by - hB / 2, TINTA2, q, 5)
        polia(c, px, py, pr, q, (x0 + L - 10, y + 8))
        F.bloco(c, ax, ay, wA, hA, mA, TINTA2, q, size=48)
        F.bloco(c, px + pr, by, wB, hB, mB, cor_b or E.COR, q, size=44)
    return dict(A=(ax, ay), B=(px + pr, by), fioA=(ax + wA / 2, py - pr), polia=(px, py), wA=wA, hA=hA, wB=wB, hB=hB, y=y)


def atwood(c, t, t0, cx, ytopo, mA, mB, s=0.0, w=125, h=115):
    """polia presa no teto com dois blocos pendurados; s = quanto o da esquerda já desceu (px)"""
    q = ep(t, t0, 0.5)
    pr = 95
    py = ytopo + 120
    yl, yr = py + 340 + s, py + 340 - s
    if q > 0:
        F.teto(c, cx - 150, cx + 150, ytopo, q)
        M.line(c, cx, ytopo, cx, py, TINTA2, q, 8)
        M.line(c, cx - pr, py, cx - pr, yl - h / 2, TINTA2, q, 5)
        M.line(c, cx + pr, py, cx + pr, yr - h / 2, TINTA2, q, 5)
        polia(c, cx, py, pr, q)
        F.bloco(c, cx - pr, yl, w, h, mA, E.COR, q, size=44)
        F.bloco(c, cx + pr, yr, w, h, mB, TINTA2, q, size=44)
    return (cx - pr, yl), (cx + pr, yr)


def par_horizontal(c, t, t0, x0, yb, s=0.0):
    """dois blocos ligados por fio no chão liso: 2 kg atrás, 3 kg na frente; devolve os centros"""
    q = ep(t, t0, 0.5)
    A = (x0 + 140 + s, yb - 75)
    B = (x0 + 560 + s, yb - 85)
    if q > 0:
        F.chao(c, x0 - 40, x0 + 1100, yb, q)
        M.line(c, A[0] + 90, A[1], B[0] - 110, A[1], TINTA2, q, 5)
        F.bloco(c, *A, 180, 150, "2 kg", TINTA2, q, size=44)
        F.bloco(c, *B, 220, 170, "3 kg", TINTA2, q, size=48)
    return A, B


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            s = 0 if t < C["s01.d"] else min(160, 0.5 * 90 * (t - C["s01.d"]) ** 2)
            q = ep(t, C["s01.a"], 0.5)
            if q > 0:
                M.rrect(c, 900, 560, 700, 26, 6, MADEIRA, q)
                M.rrect(c, 930, 582, 26, 260, 5, "#6E4A2F", q)
                F.bloco(c, 1145 + s, 485, 200, 150, None, TINTA2, q)
            qb = ep(t, C["s01.b"], 0.5)
            if qb > 0:
                M.line(c, 1245 + s, 492, 1607, 492, TINTA2, qb, 5)
                polia(c, 1607, 526, 34, qb, (1590, 568))
                M.line(c, 1641, 526, 1641, 640 + s, TINTA2, qb, 5)
            E.foco(c, t, C["s01.c"], 0.5, lambda a: F.bloco(c, 1641, 700 + s, 150, 130, None, E.COR, a))
            E.frase(c, t, C["s01.a"], ps("bloco na mesa,", "i", 66), XE, 250, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("fio, roldana", "i", 66), XE, 360, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("e bloco pendurado", "i", 66), XE, 470, passo=0.12)
            E.frase(c, t, C["s01.d"], ps("a aceleração", "i", 76) + ps("numa linha", "g", 76, COR), XE, 900, passo=0.12)
            F.vetor(c, t, C["s01.d"] + 0.4, (1120, 380), (1320, 380), "a", None, F.ACEL, 9, size=48)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "blocos ligados", 0), ("s02.c", "um corpo só", 0), ("s02.d", "a tração no fio", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "tração,", "a mesma no fio todo"), ("s03.c", "atrito cinético,", "μ · N"),
                              ("s03.d", "segunda lei,", "resultante = m × a")))


# ---------------- um corpo só ----------------
def b_junto(c, t, C, b):
    x0, yb = 700, 640
    A, B = par_horizontal(c, t, C["s04.a"], x0, yb)
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("mesa lisa, dois blocos e um fio", "i", 62), XE, 230, passo=0.1)
        seta_f(c, t, C["s04.d"], (B[0] + 110, B[1]), 0, 200, "F", modulo="20 N", lpos=(B[0] + 210, B[1] - 60), size=50)
        F.vetor(c, t, C["s04.e"], (A[0] - 60, yb + 110), (A[0] + 120, yb + 110), "a", None, F.ACEL, 8, size=46, lado=-1)
        F.vetor(c, t, C["s04.e"] + 0.3, (B[0] - 60, yb + 110), (B[0] + 120, yb + 110), "a", None, F.ACEL, 8, size=46, lado=-1)
        E.frase(c, t, C["s04.e"], ps("a mesma aceleração", "g", 60, F.ACEL), XE, 900, passo=0.1)
        return
    seta_f(c, t, C["s05"], (B[0] + 110, B[1]), 0, 200, "F", modulo="20 N", lpos=(B[0] + 210, B[1] - 60), size=50)
    if t < C["s06"]:
        p = ep(t, C["s05.a"], 0.5)
        E.caixa_pontilhada(c, A[0] - 130, A[1] - 150, B[0] - A[0] + 270, 280, p, prog_=p)
        E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: E.pilula(c, "um corpo só: 5 kg", (A[0] + B[0]) / 2, A[1] - 200, 48, "g", fundo=E.COR, a=a))
        seta_f(c, t, C["s05.b"], (A[0] + 90, A[1] - 20), 0, 80, "T", lpos=(A[0] + 150, A[1] - 60), size=44)
        seta_f(c, t, C["s05.b"] + 0.3, (B[0] - 110, A[1] - 20), 180, 80, "T", lpos=(B[0] - 170, A[1] - 60), size=44)
        risca_em(c, t, C["s05.c"], A[0] + 80, A[1] + 20, B[0] - 100, A[1] - 120, 8)
        E.frase(c, t, C["s05.c"], ps("as trações se cancelam dentro do conjunto", "i", 52, TINTA2), XE, 820, passo=0.08)
        E.foco(c, t, C["s05.d"], 0.5, lambda a: sub(c, "a = 20 ÷ 5", XE, 960, 84, "g", TINTA, a))
        bola_txt(c, t, C["s05.e"], "4 m/s^2", 1500, 940, 110, 50)
        return
    E.frase(c, t, C["s06.a"], ps("a tração: o bloco", "i", 62) + ps("de trás", "g", 60, COR), XE, 230, passo=0.1)
    p = ep(t, C["s06.a"], 0.5)
    E.caixa_pontilhada(c, A[0] - 120, A[1] - 120, 300, 230, p, prog_=p)
    seta_f(c, t, C["s06.a"] + 0.4, (A[0] + 90, A[1] - 20), 0, 110, "T", lpos=(A[0] + 170, A[1] - 70), size=46)
    contas(c, t, [(C["s06.b"], "T = 2 · 4"), (C["s06.d"], "frente: 20 − 8 = 12"), (C["s06.e"], "12 ÷ 3 = 4", CERTO)], XE, 820, 66, 100)
    bola_txt(c, t, C["s06.c"], "8 N", 1500, 900, 100, 56)


# ---------------- polia ----------------
def b_polia(c, t, C, b):
    x0, y, L = 760, 560, 760
    if t < C["s08"]:
        d = mesa_polia(c, t, C["s07.b"], x0, y, L, "6 kg", "4 kg")
        E.frase(c, t, C["s07.a"], ps("agora, com", "i", 76) + [("polia", "g", 76, COR)], XE, 230, passo=0.12)
        E.frase(c, t, C["s07.d"], ps("a polia só muda", "i", 58) + ps("a direção do fio", "g", 56), XE, 820, passo=0.1)
        if t >= C["s07.d"]:
            px, py = d["polia"]
            q = 0.5 + 0.5 * math.sin((t - C["s07.d"]) * 5)
            c.drawCircle(px, py, 70, M.paint(E.COR, q * ep(t, C["s07.d"], 0.3), stroke=6))
        F.vetor(c, t, C["s07.e"], (d["A"][0] - 80, y - 210), (d["A"][0] + 100, y - 210), "a", None, F.ACEL, 8, size=46)
        F.vetor(c, t, C["s07.e"] + 0.3, (d["B"][0] + 130, d["B"][1] - 90), (d["B"][0] + 130, d["B"][1] + 90), "a", None, F.ACEL, 8, size=46, lado=-1)
        E.frase(c, t, C["s07.e"], ps("a mesma aceleração", "g", 58, F.ACEL), XE, 920, passo=0.1)
        return
    d = mesa_polia(c, t, C["s08"], x0, y, L, "6 kg", "4 kg")
    Bx, By = d["B"]
    seta_f(c, t, C["s08.a"], (Bx, By + 65), -90, 160, "P", modulo="40 N", lpos=(Bx - 150, By + 200), size=46)
    Ax, Ay = d["A"]
    seta_f(c, t, C["s08.b"], (Ax - 40, Ay), -90, 150, "P", lpos=(Ax - 100, Ay + 170), size=44)
    seta_f(c, t, C["s08.b"] + 0.3, (Ax + 40, Ay - 75), 90, 150, "N", lpos=(Ax + 100, Ay - 180), size=44)
    E.foco(c, t, C["s08.b"] + 0.8, 0.4, lambda a: E.pilula(c, "se anulam", Ax, y + 330, 40, "b", fundo=TINTA2, a=a))
    E.frase(c, t, C["s08.a"], ps("quem puxa: o peso pendurado", "i", 56), XE, 220, passo=0.08)
    contas(c, t, [(C["s08.c"], "a = 40 ÷ 10"), (C["s08.e"], "T = 6 · 4")], XE, 380, 76, 120)
    bola_txt(c, t, C["s08.d"], "4 m/s^2", 330, 760, 100, 44)
    bola_txt(c, t, C["s08.f"], "24 N", 600, 760, 100, 50)


# ---------------- com atrito ----------------
def b_atrito(c, t, C, b):
    x0, y, L = 760, 560, 760
    d = mesa_polia(c, t, C["s09"], x0, y, L, "6 kg", "4 kg")
    Ax, Ay = d["A"]
    Bx, By = d["B"]
    E.frase(c, t, C["s09.a"], ps("mesa com atrito:", "i", 58) + [("μc = 0,5", "g", 56, COR)], XE, 220, passo=0.1)
    E.frase(c, t, C["s09.a"] + 1.6, ps("e o sistema já anda", "i", 50, TINTA2), XE, 300, passo=0.08)
    seta_f(c, t, C["s09.c"], (Ax - 100, y - 6), 180, 140, "F_{at}", modulo="30 N", lpos=(Ax - 110, y + 95), size=46)
    seta_f(c, t, C["s09.d"], (Bx, By + 65), -90, 160, "P", modulo="40 N", lpos=(Bx - 150, By + 200), size=46)
    if t < C["s10"]:
        contas(c, t, [(C["s09.b"], "N = 60 N"), (C["s09.c"], "F_{at} = 0,5 · 60 = 30 N"), (C["s09.e"], "a = (40 − 30) ÷ 10")], XE, 420, 64, 100)
        bola_txt(c, t, C["s09.f"], "1 m/s^2", 480, 800, 110, 48)
        return
    E.frase(c, t, C["s10.a"], ps("tração, pelo bloco da mesa", "i", 58), XE, 420, passo=0.1)
    seta_f(c, t, C["s10.a"] + 0.4, (Ax + 100, Ay - 20), 0, 160, "T", lpos=(Ax + 190, Ay - 80), size=46)
    contas(c, t, [(C["s10.b"], "T − 30 = 6 · 1")], XE, 560, 76)
    bola_txt(c, t, C["s10.c"], "36 N", 480, 800, 110, 56)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("tração = peso pendurado?", "i", 66), XE, 330, passo=0.12)
    d = mesa_polia(c, t, C["s11"], 900, 560, 640, "6 kg", "4 kg")
    Bx, By = d["B"]
    seta_f(c, t, C["s11.b"], (Bx, By + 65), -90, 160, "P", modulo="40 N", lpos=(Bx - 150, By + 200), size=46)
    seta_f(c, t, C["s11.c"], (Bx, By - 65), 90, 96, "T", modulo="24 N", lpos=(Bx + 170, By - 100), size=46)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: sub(c, "P = 40 N", XE, 480, 76, "g", TINTA, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: sub(c, "T = 24 N", XE + 400, 480, 76, "g", CERTO, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: sub(c, "T = 40 → F_{R} = 0", XE, 680, 76, "g", ERRADO, a))
    E.frase(c, t, C["s11.e"], ps("e ele não desceria acelerando", "i", 56, TINTA2), XE, 800, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("o atalho, numa linha", "i", 76, CLARO), W / 2, 180, "center")
        E.foco(c, t, C["s12.a"], 0.5, lambda a: sub(c, "a = f{a favor − contra}{soma das massas}", W / 2, 480, 110, "g", BR, a, "center"))
        E.frase(c, t, C["s12.c"], ps("depois, a tração:", "i", 62, CLARO) + ps("o bloco com menos forças", "g", 62, BR), W / 2, 800, "center", 0.1)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("as trações são internas:", "i", 62, CLARO) + ps("somem no conjunto", "g", 62, BR), W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s13.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("blocos que não andam juntos", "i", 64, CLARO), W / 2, 520, "center", 0.12)
    E.frase(c, t, C["s13.c"], ps("fio frouxo · polia que se move", "g", 60, BR), W / 2, 680, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], ps("polia presa no teto", "i", 64), XE, 330, passo=0.1)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "de um lado", XE, 450, 60, "i", TINTA, a), F.medida(c, 3, "kg", XE + 320, 450, 76, COR, a)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.escreve(c, "do outro", XE, 570, 60, "i", TINTA, a), F.medida(c, 2, "kg", XE + 320, 570, 76, COR, a)))
    E.frase(c, t, C["s14.d"], [("a", "g", 72, F.ACEL), ("=", "g", 72), ("?", "g", 72, COR)], XE, 760, passo=0.12)
    E.frase(c, t, C["s14.e"], [("T", "g", 72), ("=", "g", 72), ("?", "g", 72, COR)], XE + 300, 760, passo=0.12)

    def desenho():
        atwood(c, t, C["s14.a"], 1400, 180, "3 kg", "2 kg")
    pausa(c, t, C, "s15", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s = 0 if t < C["s16.a"] else min(80, 0.5 * 60 * (t - C["s16.a"]) ** 2)
    L, R = atwood(c, t, C["s16"], 1450, 140, "3 kg", "2 kg", s)
    if t < C["s17"]:
        seta_f(c, t, C["s16.b"], (L[0] - 70, L[1]), -90, 150, "P", modulo="30 N", lpos=(L[0] - 200, L[1] + 120), size=44)
        seta_f(c, t, C["s16.c"], (R[0] + 70, R[1]), -90, 100, "P", modulo="20 N", lpos=(R[0] + 200, R[1] + 70), size=44)
        E.frase(c, t, C["s16.a"], ps("o de 3 desce, o de 2 sobe", "i", 60), XE, 220, passo=0.1)
        contas(c, t, [(C["s16.b"], "a favor: 30 N"), (C["s16.c"], "contra: 20 N"), (C["s16.d"], "a = (30 − 20) ÷ 5")], XE, 380, 70, 115)
        bola_txt(c, t, C["s16.e"], "2 m/s^2", 560, 860, 120, 52)
        return
    seta_f(c, t, C["s17.a"], (R[0], R[1] - 60), 90, 140, "T", lpos=(R[0] + 90, R[1] - 160), size=46)
    E.frase(c, t, C["s17.a"], ps("tração, pelo de 2, que sobe", "i", 60), XE, 220, passo=0.1)
    contas(c, t, [(C["s17.b"], "T − 20 = 2 · 2"), (C["s17.d"], "3 kg: 30 − 24 = 6 → 6 ÷ 3 = 2", CERTO)], XE, 380, 66, 130)
    bola_txt(c, t, C["s17.c"], "24 N", 560, 800, 120, 56)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s18", (("s18.a", [("ligados:", "i", 64), ("a", "i", 64), ("mesma", "g", 60, COR), ("aceleração", "g", 60)]),
                            ("s18.b", [("um", "g", 60, COR), ("corpo", "g", 60, COR), ("só:", "g", 60, COR), ("a", "i", 64), ("tração", "i", 64), ("some", "i", 64)]),
                            ("s18.c", [("tração:", "i", 64), ("isole", "g", 60), ("o", "i", 64), ("bloco", "i", 64), ("mais", "i", 64), ("simples", "g", 60, COR)])), C["s19"])
    if t < C["s19"]:
        return

    def desenho():
        cx, cy, r = 600, 820, 170
        if t >= C["s19.a"]:
            pt = M.paint(TINTA2, ep(t, C["s19.a"], 0.5), stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
            c.drawCircle(cx, cy, r, pt)
            c.drawCircle(cx, cy, 9, M.paint(TINTA, ep(t, C["s19.a"], 0.5)))
        g = math.radians(30 + (t - C["s19.a"]) * 40) if t >= C["s19.a"] else 0
        P = (cx + r * math.cos(g), cy - r * math.sin(g))
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.bola(c, *P, 30, a=a))
        if t >= C["s19.b"]:
            ux, uy = (cx - P[0]) / r, (cy - P[1]) / r
            F.seta(c, P[0], P[1], P[0] + ux * 120, P[1] + uy * 120, E.COR, ep(t, C["s19.b"], 0.3), 9)
    proxima(c, t, C, "s19", ((C["s19.a"], [("Força", "g", 100), ("centrípeta", "g", 100, COR)]),), "s19.d", "s19.e", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, junto=b_junto, polia=b_polia, atrito=b_atrito, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
