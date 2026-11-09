"""Visual — Estudativo · FIS-DIN-012: lombada, baixada, globo da morte e pêndulo (normal e tração nos pontos extremos).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula: a curva é vista DE LADO; o centro
da curva é um ponto com a pílula "centro" e um tracejado até o corpo; força para o centro entra com "+" (pílula verde),
para fora com "−" (pílula vermelha). Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-012_lombada_globo_da_morte_e_pendulo.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "lombada", "looping", "pendulo", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²)
assert 10 ** 2 / 20 == 5 and 10000 - 1000 * 5 == 5000 and 10000 + 1000 * 5 == 15000
assert round((10 * 3.6) ** 0.5, 9) == 6
assert 20 + 2 * 3 ** 2 / 1 == 38
assert (10 * 10) ** 0.5 == 10 and round(10 * 3.6) == 36
assert 20 ** 2 / 10 == 40 and 60 * 40 == 2400 and 2400 - 600 == 1800

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
def centro_pt(c, t, t0, P, Q=None, rot="centro"):
    """centro da curva em P (ponto e pílula) e, se Q, o tracejado até o corpo"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    if Q:
        M.line(c, *P, *Q, TINTA2, 0.6 * q, 4, dash=E.TRACO)
    c.drawCircle(*P, 11, M.paint(TINTA, q))
    E.pilula(c, rot, P[0] + 90, P[1] + 4, 34, "b", fundo=TINTA2, a=q)


def sinal(c, t, t0, s, x, y, ok=True):
    E.foco(c, t, t0, 0.3, lambda a: E.pilula(c, s, x, y, 40, "g", fundo=CERTO if ok else ERRADO, a=a))


def lombada(c, t, t0, cx, yb, R, meia, baixada=False):
    """perfil de lombada (arco para cima) ou baixada (arco para baixo) com raio R px; devolve o ponto mais alto/baixo e o centro"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return (cx, yb), (cx, yb)
    ang = math.degrees(math.asin(meia / R))
    if not baixada:
        C0 = (cx, yb + R)
        ret = skia.Rect.MakeXYWH(C0[0] - R, C0[1] - R, 2 * R, 2 * R)
        c.drawArc(ret, -90 - ang, 2 * ang, False, M.paint(TINTA, q, stroke=8))
        topo = (cx, yb)
    else:
        C0 = (cx, yb - R)
        ret = skia.Rect.MakeXYWH(C0[0] - R, C0[1] - R, 2 * R, 2 * R)
        c.drawArc(ret, 90 - ang, 2 * ang, False, M.paint(TINTA, q, stroke=8))
        topo = (cx, yb)
    yl = C0[1] + (-1 if not baixada else 1) * R * math.cos(math.radians(ang))
    M.line(c, cx - meia - 200, yl, cx - meia, yl, TINTA, q, 8)
    M.line(c, cx + meia, yl, cx + meia + 200, yl, TINTA, q, 8)
    return topo, C0


def globo(c, t, t0, cx, cy, R, ang_moto=90):
    """globo da morte: círculo e a moto (bolinha laranja) por dentro no ângulo ang_moto (90 = topo)"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return (cx, cy - R)
    for k in range(7):
        pt = M.paint(TINTA2, 0.18 * q, stroke=3)
        c.drawOval(skia.Rect.MakeXYWH(cx - R * abs(math.cos(k * math.pi / 7)), cy - R, 2 * R * abs(math.cos(k * math.pi / 7)), 2 * R), pt)
    c.drawCircle(cx, cy, R, M.paint(TINTA, q, stroke=8))
    a = math.radians(ang_moto)
    P = (cx + (R - 34) * math.cos(a), cy - (R - 34) * math.sin(a))
    E.bola(c, *P, 30, a=q)
    return P


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            topo, C0 = lombada(c, t, C["s01.a"], 700, 620, 420, 260)
            k = min(1.0, max(0.0, (t - C["s01.a"]) / 3.0))
            x = lerp(500, 900, k)
            yy = 620 + 420 - math.sqrt(max(0, 420 ** 2 - (x - 700) ** 2)) if abs(x - 700) < 260 else 620 + 420 - 420 * math.cos(math.asin(260 / 420))
            E.foco(c, t, C["s01.a"], 0.4, lambda a: F.carrinho(c, x, yy, 200, a=a))
            E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "mais leve?", 700, 450, 44, "g", fundo=E.COR, a=a))
            P = globo(c, t, C["s01.c"], 1450, 560, 300, 90 + 80 * math.sin(max(0.0, t - C["s01.c"]) * 1.2) if t < C["s01.c"] + 2 else 90)
            E.foco(c, t, C["s01.c"] + 0.6, 0.4, lambda a: E.pilula(c, "não cai?", 1450, 960, 44, "g", fundo=E.COR, a=a))
            E.frase(c, t, C["s01.d"], ps("a mesma física", "g", 70, COR), XE, 230, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "lombada e baixada", 0), ("s02.c", "o topo do globo", 0), ("s02.d", "o fio do pêndulo", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "centrípeta,", "a resultante para o centro"), ("s03.c", "peso e normal,", "P = m · g")))


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s04"], ps("o método é um só", "i", 76), XE, 210, passo=0.12)
    for i, (k, s) in enumerate((("s04.a", "marque o centro"), ("s04.b", "para o centro: +"), ("s04.c", "para fora: −"))):
        y = 400 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 40, a=a), centro(c, str(i + 1), XE + 40, y - 4, 50, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 66, (TINTA, CERTO, ERRADO)[i])], XE + 110, y)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: sub(c, "soma = m · f{v^2}{R}", XE, 900, 110, "g", COR, a))
    cx, cy, R = 1450, 560, 230
    if t >= C["s04.a"]:
        pt = M.paint(TINTA2, ep(t, C["s04.a"], 0.5), stroke=5)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawCircle(cx, cy, R, pt)
    centro_pt(c, t, C["s04.a"], (cx, cy), (cx, cy - R))
    E.foco(c, t, C["s04.a"], 0.4, lambda a: E.bola(c, cx, cy - R, 32, a=a))
    seta_f(c, t, C["s04.b"], (cx - 20, cy - R + 30), -90, 140, None)
    sinal(c, t, C["s04.b"] + 0.3, "+", cx - 90, cy - R + 110)
    seta_f(c, t, C["s04.c"], (cx + 20, cy - R - 30), 90, 140, None)
    sinal(c, t, C["s04.c"] + 0.3, "−", cx + 90, cy - R - 110, False)


# ---------------- lombada e baixada ----------------
def b_lombada(c, t, C, b):
    if t < C["s07"]:
        topo, C0 = lombada(c, t, C["s05"], 1350, 520, 360, 280)
        E.foco(c, t, C["s05"], 0.4, lambda a: F.carrinho(c, topo[0], topo[1], 220, a=a))
        centro_pt(c, t, C["s05.a"], (C0[0], 940), (topo[0], topo[1] + 10), "centro (embaixo)")
        seta_f(c, t, C["s05.b"], (topo[0] - 40, topo[1] - 60), -90, 170, "P", lpos=(topo[0] - 110, topo[1] + 120), size=48)
        sinal(c, t, C["s05.b"] + 0.3, "+", topo[0] - 190, topo[1] + 40)
        seta_f(c, t, C["s05.c"], (topo[0] + 50, topo[1] - 10), 90, 170, "N", lpos=(topo[0] + 120, topo[1] - 170), size=48)
        sinal(c, t, C["s05.c"] + 0.3, "−", topo[0] + 190, topo[1] - 100, False)
        if t < C["s06"]:
            E.frase(c, t, C["s05.a"], ps("no topo, o centro fica", "i", 60) + [("embaixo", "g", 60, COR)], XE, 230, passo=0.1)
            E.foco(c, t, C["s05.d"], 0.5, lambda a: sub(c, "P − N = m · f{v^2}{R}", XE, 900, 100, "g", COR, a))
            return
        E.foco(c, t, C["s06.a"], 0.5, lambda a: sub(c, "m = 1.000 kg   v = 10 m/s   R = 20 m", XE, 230, 56, "g", TINTA, a))
        contas(c, t, [(C["s06.b"], "f{v^2}{R} = 100 ÷ 20 = 5"), (C["s06.c"], "10.000 − N = 1.000 · 5")], XE, 820, 70, 120)
        bola_txt(c, t, C["s06.d"], "5.000 N", 1720, 640, 115, 42)
        E.foco(c, t, C["s06.d"] + 0.8, 0.4, lambda a: E.pilula(c, "metade do peso", 1720, 800, 40, "b", fundo=TINTA, a=a))
        return
    topo, C0 = lombada(c, t, C["s07"], 1350, 760, 360, 280, baixada=True)
    E.foco(c, t, C["s07"], 0.4, lambda a: F.carrinho(c, topo[0], topo[1], 220, a=a))
    centro_pt(c, t, C["s07.a"], (C0[0], 320), (topo[0], topo[1] - 140), "centro (em cima)")
    seta_f(c, t, C["s07.b"], (topo[0] + 50, topo[1] - 10), 90, 230, "N", lpos=(topo[0] + 120, topo[1] - 230), size=48)
    sinal(c, t, C["s07.b"] + 0.3, "+", topo[0] + 200, topo[1] - 130)
    seta_f(c, t, C["s07.b"] + 0.4, (topo[0] - 40, topo[1] - 60), -90, 150, "P", lpos=(topo[0] - 110, topo[1] + 110), size=48)
    sinal(c, t, C["s07.b"] + 0.7, "−", topo[0] - 190, topo[1] + 40, False)
    E.frase(c, t, C["s07.a"], ps("na baixada, o centro fica", "i", 58) + [("em", "g", 58, COR), ("cima", "g", 58, COR)], XE, 230, passo=0.1)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: sub(c, "N − P = m · f{v^2}{R}", XE, 400, 84, "g", COR, a))
    bola_txt(c, t, C["s07.d"], "15.000 N", 420, 700, 130, 44)
    E.frase(c, t, C["s07.e"], ps("normal maior que o peso", "g", 54), XE, 960, passo=0.1)


# ---------------- globo da morte ----------------
def b_looping(c, t, C, b):
    cx, cy, R = 1450, 560, 330
    P = globo(c, t, C["s08"], cx, cy, R, 90)
    centro_pt(c, t, C["s08.a"], (cx, cy), P)
    seta_f(c, t, C["s08.b"], (P[0] - 30, P[1] + 20), -90, 150, "P", lpos=(P[0] - 110, P[1] + 140), size=46)
    seta_f(c, t, C["s08.c"], (P[0] + 30, P[1] - 30), -90, 150 if t < C["s09.a"] else 150 * (1 - ep(t, C["s09.b"], 1.0)) + 1, "N", lpos=(P[0] + 100, P[1] + 140), size=46)
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("no topo, de cabeça para baixo:", "i", 54) + ps("centro embaixo", "g", 54, COR), XE, 230, passo=0.08)
        E.frase(c, t, C["s08.b"], ps("peso: para o centro", "i", 58), XE, 380, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("normal: também", "i", 58), XE, 480, passo=0.1)
        E.foco(c, t, C["s08.d"], 0.5, lambda a: sub(c, "N + P = m · f{v^2}{R}", XE, 680, 90, "g", COR, a))
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("mais devagar,", "i", 60) + ps("menos normal", "g", 58), XE, 230, passo=0.1)
        E.foco(c, t, C["s09.b"], 0.5, lambda a: sub(c, "mínimo: N = 0", XE, 380, 80, "g", TINTA, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: sub(c, "m · g = m · f{v^2}{R}", XE, 560, 80, "g", TINTA, a))
        if t >= C["s09.d"] + 0.8:
            wm = sub(None, "m", 0, 0, 80)
            w1 = sub(None, "m · g = ", 0, 0, 80)
            risca_em(c, t, C["s09.d"] + 0.8, XE - 6, 575, XE + wm + 6, 515, 8)
            risca_em(c, t, C["s09.d"] + 1.0, XE + w1 - 6, 575, XE + w1 + wm + 6, 515, 8)
        E.foco(c, t, C["s09.e"], 0.5, lambda a: sub(c, "v_{mín} = r{g · R}", XE, 790, 120, "g", COR, a))
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: sub(c, "R = 3,6 m", XE, 230, 80, "g", TINTA, a))
    contas(c, t, [(C["s10.b"], "g · R = 10 · 3,6 = 36"), (C["s10.c"], "v_{mín} = r{36}")], XE, 400, 76, 140)
    bola_txt(c, t, C["s10.c"] + 0.6, "6 m/s", 480, 760, 120, 60)
    E.frase(c, t, C["s10.d"], ps("mais devagar: descola no topo", "i", 54, ERRADO), XE, 960, passo=0.08)


# ---------------- pêndulo ----------------
def b_pendulo(c, t, C, b):
    px, py, L = 1400, 200, 500
    ang = 0 if t >= C["s11.c"] else 35 * math.cos(max(0.0, t - C["s11"]) * 2.2)
    F.pendulo(c, t, C["s11"], px, py, L, ang, 44)
    B = (px, py + L)
    if t >= C["s11.c"]:
        centro_pt(c, t, C["s11.c"], (px, py + 20))
    seta_f(c, t, C["s11.d"], (B[0] + 20, B[1] - 50), 90, 200, "T", lpos=(B[0] + 90, B[1] - 200), size=50)
    sinal(c, t, C["s11.d"] + 0.3, "+", B[0] + 170, B[1] - 120)
    seta_f(c, t, C["s11.d"] + 0.5, (B[0] - 20, B[1] + 40), -90, 120, "P", lpos=(B[0] - 90, B[1] + 140), size=50)
    sinal(c, t, C["s11.d"] + 0.8, "−", B[0] - 170, B[1] + 70, False)
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("agora, o", "i", 70) + [("pêndulo", "g", 70, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s11.b"], [("tração", "g", 64, COR), ("(T):", "g", 64)] + ps("a força do fio, só puxa", "i", 60), XE, 360, passo=0.1)
        E.frase(c, t, C["s11.c"], ps("embaixo, o centro fica em cima", "i", 58), XE, 500, passo=0.1)
        E.foco(c, t, C["s11.e"], 0.5, lambda a: sub(c, "T − P = m · f{v^2}{R}", XE, 720, 90, "g", COR, a))
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: sub(c, "m = 2 kg   L = 1 m   v = 3 m/s", XE, 230, 56, "g", TINTA, a))
    contas(c, t, [(C["s12.b"], "T − 20 = 2 · 9 ÷ 1")], XE, 420, 80)
    bola_txt(c, t, C["s12.c"], "38 N", 460, 700, 120, 60)
    E.frase(c, t, C["s12.d"], ps("quase o dobro do peso", "g", 56) + ps("(20 N)", "i", 56, TINTA2), XE, 920, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("numa curva,", "i", 64) + [("N", "g", 64, ERRADO), ("=", "g", 64, ERRADO), ("P?", "g", 64, ERRADO)], XE, 340, passo=0.12)
    E.frase(c, t, C["s13.b"], ps("só no chão plano, parado ou com v constante", "i", 50, TINTA2), XE, 450, passo=0.06)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: sub(c, "lombada: N = 10.000 N", XE, 640, 80, "g", ERRADO, a))
    risca_em(c, t, C["s13.c"] + 1.4, XE - 10, 660, XE + 820, 580)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: sub(c, "N = 5.000 N", XE, 820, 96, "g", CERTO, a))
    topo, C0 = lombada(c, t, C["s13"], 1550, 640, 300, 220)
    E.foco(c, t, C["s13"], 0.4, lambda a: F.carrinho(c, topo[0], topo[1], 180, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], ps("por cima, no topo (lombada):", "i", 58, CLARO) + ps("normal menor", "g", 58, BR), W / 2, 320, "center", 0.1)
        sub_em(c, t, C["s14.b"], "N = m · (g − f{v^2}{R})", W / 2, 470, 96, "g", BR, "center")
        E.frase(c, t, C["s14.c"], ps("embaixo (baixada, pêndulo):", "i", 58, CLARO) + ps("força maior", "g", 58, BR), W / 2, 680, "center", 0.1)
        sub_em(c, t, C["s14.d"], "m · (g + f{v^2}{R})", W / 2, 830, 96, "g", BR, "center")
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], ps("topo do looping, por dentro:", "i", 62, CLARO), W / 2, 240, "center", 0.1)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: sub(c, "v_{mín} = r{g · R}", W / 2, 440, 130, "g", BR, a, "center"))
    E.frase(c, t, C["s15.b"], ps("funciona porque as forças estão na vertical", "i", 56, CLARO), W / 2, 660, "center", 0.08)
    E.frase(c, t, C["s15.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("no meio da curva", "i", 62, CLARO), W / 2, 820, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s16")
    E.frase(c, t, C["s16.a"], ps("looping de", "i", 64), XE, 330, passo=0.1)
    E.foco(c, t, C["s16.a"] + 0.6, 0.5, lambda a: F.medida(c, 10, "m", XE + 330, 330, 76, COR, a))
    E.frase(c, t, C["s16.b"], ps("v mínima no topo?", "g", 66), XE, 470, passo=0.1)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (E.escreve(c, "a", XE, 610, 62, "i", TINTA, a), F.medida(c, 20, "m/s", XE + 70, 610, 76, COR, a)))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: (E.escreve(c, "pessoa de", XE, 740, 62, "i", TINTA, a), F.medida(c, 60, "kg", XE + 300, 740, 76, COR, a)))
    E.frase(c, t, C["s16.d"] + 1.2, [("N", "g", 72), ("=", "g", 72), ("?", "g", 72, COR)], XE, 880, passo=0.12)

    def desenho():
        globo(c, t, C["s16.a"], 1450, 560, 300, 90)
    pausa(c, t, C, "s17", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    contas(c, t, [(C["s18.a"], "v_{mín} = r{10 · 10}"), (C["s18.c"], "f{v^2}{R} = 400 ÷ 10 = 40"), (C["s18.d"], "N + 600 = 60 · 40 = 2.400")], XE, 240, 70, 150)
    bola_txt(c, t, C["s18.b"], "10 m/s", 1500, 300, 110, 50)
    E.foco(c, t, C["s18.b"] + 0.6, 0.4, lambda a: E.pilula(c, "36 km/h", 1500, 460, 44, "b", fundo=TINTA, a=a))
    bola_txt(c, t, C["s18.e"], "1.800 N", 1450, 780, 150, 54)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s19", (("s19.a", [("marque", "i", 66), ("o", "i", 66), ("centro", "g", 62, COR)]),
                            ("s19.b", [("para", "i", 66), ("o", "i", 66), ("centro:", "i", 66), ("+", "g", 62, CERTO), ("para", "i", 66), ("fora:", "i", 66), ("−", "g", 62, ERRADO)]),
                            ("s19.c", [("topo", "i", 66), ("do", "i", 66), ("looping:", "i", 66), ("v", "g", 62), ("=", "g", 62), ("√(g·R)", "g", 62, COR)])), C["s20"])
    if t < C["s20"]:
        return

    def desenho():
        R = F.plano_inclinado(c, t, C["s20.b"], 360, 980, 420, 30, None)
        if t >= C["s20.b"] + 0.4:
            F.bloco_rampa(c, R, 0.5, 110, 80, None, ep(t, C["s20.b"] + 0.4, 0.4))
        E.foco(c, t, C["s20.b"] + 0.6, 0.4, lambda a: (polia(c, 1000, 800, 30, a), M.line(c, 970, 800, 970, 900, TINTA2, a, 5), F.bloco(c, 970, 940, 90, 80, None, E.COR, a)))
    proxima(c, t, C, "s20", ((C["s20.a"], [("Praticando", "g", 100, COR)]), (C["s20.b"], [("atrito,", "i", 66), ("rampas", "i", 66), ("e", "i", 66), ("curvas", "g", 62)])),
            "s20.c", "s20.d", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, lombada=b_lombada, looping=b_looping, pendulo=b_pendulo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
