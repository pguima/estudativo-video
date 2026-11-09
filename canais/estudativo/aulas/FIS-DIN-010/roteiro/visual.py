"""Visual — Estudativo · FIS-DIN-010: força centrípeta (aceleração v²/R e quem faz o papel de centrípeta).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula a curva é vista DE CIMA: trajetória
circular tracejada, centro marcado, velocidade petróleo sempre tangente, aceleração centrípeta violeta e força laranja
sempre para o centro. Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-010_forca_centripeta.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("curva", "formula", "papel", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
assert 0.5 ** 2 * 4 == 1
assert 20 ** 2 / 50 == 8 and 1000 * 8 == 8000
assert 4 ** 2 == 16 and 16 / 2 == 8 and 0.5 * 8 == 4
assert 8 ** 2 == 64 and 64 / 2 == 32 and 0.5 * 32 == 16 and 16 / 4 == 4

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
def trilha(c, t, t0, cx, cy, r, a_max=1.0):
    """trajetória circular tracejada e o centro"""
    q = ep(t, t0, 0.6) * a_max
    if q <= 0:
        return
    pt = M.paint(TINTA2, q * 0.7, stroke=4)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, 360 * ease_io(prog(t, t0, 0.9)), False, pt)
    c.drawCircle(cx, cy, 10, M.paint(TINTA, q))
    E.escreve(c, "centro", cx - 60, cy + 54, 38, "i", TINTA2, q)


def no_circulo(cx, cy, r, g):
    """ponto e vetores unitários (tangente no sentido anti-horário, e para o centro) no ângulo g (graus)"""
    a = math.radians(g)
    P = (cx + r * math.cos(a), cy - r * math.sin(a))
    tg = (-math.sin(a), -math.cos(a))
    dentro = (-math.cos(a), math.sin(a))
    return P, tg, dentro


def carro_cima(c, x, y, ang, s, a=1.0, cor=None):
    """carro visto de cima, apontando no ângulo ang (graus, tela)"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(ang)
    M.rrect(c, -s, -s * 0.5, 2 * s, s, s * 0.25, cor or E.COR, a)
    M.rrect(c, -s * 0.15, -s * 0.38, s * 0.7, s * 0.76, s * 0.12, E.mix(cor or E.COR, "#FFFFFF", 0.7), a)
    for dx in (-0.6, 0.6):
        for dy in (-0.55, 0.55):
            M.rrect(c, dx * s - s * 0.18, dy * s - s * 0.08, s * 0.36, s * 0.16, 3, "#1B1B20", a)
    c.restore()


def movel_circ(c, t, t0, cx, cy, r, w, g0=90, desenho="bola", vel=True, acel=False, forca=False, tv=None, ta=None, tf=None,
               rot_f=None, s=34, comp=150):
    """objeto girando (w em graus/s, anti-horário) com v tangente, a e F para o centro, cada um no seu instante"""
    g = g0 + w * max(0.0, t - t0)
    P, tg, dentro = no_circulo(cx, cy, r, g)
    q = ep(t, t0, 0.4)
    if desenho == "carro":
        carro_cima(c, *P, math.degrees(math.atan2(tg[1], tg[0])), s, q)
    else:
        E.bola(c, *P, s, a=q)
    if vel and t >= (tv or t0):
        F.seta(c, *P, P[0] + tg[0] * comp, P[1] + tg[1] * comp, F.VEL, ep(t, tv or t0, 0.3), 8)
    if acel and t >= ta:
        F.seta(c, *P, P[0] + dentro[0] * comp * 0.8, P[1] + dentro[1] * comp * 0.8, F.ACEL, ep(t, ta, 0.3), 8)
    if forca and t >= tf:
        F.seta(c, *P, P[0] + dentro[0] * comp, P[1] + dentro[1] * comp, E.COR, ep(t, tf, 0.3), 10)
        if rot_f:
            E.foco(c, t, tf + 0.2, 0.3, lambda a: rot_vetor(c, rot_f, P[0] + dentro[0] * comp * 0.5 - tg[0] * 50, P[1] + dentro[1] * comp * 0.5 - tg[1] * 50 + 18, 46, E.COR_TEXTO, a))
    return P


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            cx, cy, r = 1350, 560, 300
            trilha(c, t, C["s01.a"], cx, cy, r)
            P = movel_circ(c, t, C["s01.a"], cx, cy, r, 30, 200, "carro", vel=True, forca=True, tf=C["s01.c"], rot_f="F_{cp}", s=46)
            if C["s01.b"] <= t < C["s01.c"] + 0.4:
                g = 200 + 30 * (t - C["s01.a"])
                _, tg, dentro = no_circulo(cx, cy, r, g)
                F.seta(c, *P, P[0] - dentro[0] * 150, P[1] - dentro[1] * 150, ERRADO, ep(t, C["s01.b"], 0.3) * (1 - ep(t, C["s01.c"], 0.3)), 9)
            E.frase(c, t, C["s01.a"], ps("na curva, você sente", "i", 66), XE, 240, passo=0.12)
            E.frase(c, t, C["s01.a"] + 1.0, ps("ser jogado para fora", "g", 64), XE, 340, passo=0.12)
            E.frase(c, t, C["s01.b"], [("nenhuma", "g", 70, ERRADO)] + ps("força para fora", "i", 70), XE, 560, passo=0.12)
            E.frase(c, t, C["s01.c"], [("uma", "i", 76), ("para", "g", 76, COR), ("dentro", "g", 76, COR)], XE, 760, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "aceleração centrípeta", 0), ("s02.c", "quem faz o papel", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "segunda lei,", "resultante = m × a"), ("s03.c", "no círculo,", "v = ω · R")))


# ---------------- a curva ----------------
def b_curva(c, t, C, b):
    cx, cy, r = 1350, 580, 300
    trilha(c, t, C["s04.a"], cx, cy, r)
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("curva a", "i", 66), XE, 230, passo=0.12)
        E.foco(c, t, C["s04.a"] + 0.5, 0.5, lambda a: F.medida(c, 60, "km/h", XE + 230, 230, 76, COR, a))
        E.frase(c, t, C["s04.b"], ps("o velocímetro não muda", "i", 58, TINTA2), XE, 340, passo=0.1)
        # três posições fantasma com a velocidade tangente: a direção muda
        for i, g in enumerate((200, 270, 340)):
            ti = C["s04.c"] + 0.4 * i
            P, tg, _ = no_circulo(cx, cy, r, g)
            E.foco(c, t, ti, 0.4, lambda a, P=P: E.bola(c, *P, 26, a=a))
            if t >= ti:
                F.seta(c, *P, P[0] + tg[0] * 170, P[1] + tg[1] * 170, F.VEL, ep(t, ti, 0.3), 8)
        E.frase(c, t, C["s04.c"], ps("mas a", "i", 62) + [("direção", "g", 62, F.VEL)] + ps("muda", "i", 62), XE, 500, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("mudou a velocidade:", "i", 60) + [("aceleração", "g", 60, F.ACEL)], XE, 660, passo=0.1)
        return
    movel_circ(c, t, C["s05"], cx, cy, r, 28, 200, "bola", acel=True, ta=C["s05.a"])
    E.frase(c, t, C["s05.a"], ps("aponta para o", "i", 66) + [("centro", "g", 66, F.ACEL)], XE, 230, passo=0.12)
    E.frase(c, t, C["s05.b"], [("centrípeta", "g", 96, F.ACEL)], XE, 400)
    E.frase(c, t, C["s05.c"], ps("= que busca o centro", "i", 60, TINTA2), XE, 500, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("não muda o valor:", "i", 58) + ps("só vira a direção", "g", 56), XE, 680, passo=0.1)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    if t < C["s07"]:
        formula_nova(c, t, C["s06.a"], "a_{cp} = f{v^2}{R}", XE, 330, 150, (("v", "velocidade", "m/s"), ("R", "raio da curva", "m")),
                     (C["s06.b"], C["s06.c"]), dy=86)
        E.foco(c, t, C["s06.d"], 0.5, lambda a: sub(c, "f{(m/s)^2}{m} = f{m^2/s^2}{m}", 1050, 430, 84, "b", F.UNID, a))
        E.foco(c, t, C["s06.e"], 0.5, lambda a: sub(c, "= m/s^2", 1050, 640, 96, "g", CERTO, a))
        E.foco(c, t, C["s06.e"] + 0.6, 0.4, lambda a: E.pilula(c, "é uma aceleração", 1400, 780, 48, "g", fundo=CERTO, a=a))
        return
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("se der", "i", 66) + [("ω", "g", 70, COR)] + ps("(velocidade angular)", "i", 56, TINTA2), XE, 220, passo=0.12)
        E.foco(c, t, C["s07.a"] + 1.0, 0.5, lambda a: sub(c, "v = ω · R", XE, 360, 80, "g", TINTA2, a))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: sub(c, "a_{cp} = ω^2 · R", XE, 520, 110, "g", TINTA, a))
        E.foco(c, t, C["s07.c"], 0.5, lambda a: sub(c, "ω = 0,5 rad/s   R = 4 m", XE, 700, 64, "g", TINTA, a))
        E.foco(c, t, C["s07.d"], 0.5, lambda a: sub(c, "0,25 · 4", XE, 830, 76, "g", TINTA2, a))
        bola_txt(c, t, C["s07.d"] + 0.8, "1 m/s^2", 1450, 600, 150, 64)
        return
    E.frase(c, t, C["s08"], ps("e a força?", "i", 72), XE, 210)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: sub(c, "F_{cp} = m · f{v^2}{R}", XE, 380, 110, "g", TINTA, a))
    contas(c, t, [(C["s08.b"], "m = 1.000 kg   v = 20 m/s"), (C["s08.c"], "R = 50 m"), (C["s08.d"], "a_{cp} = 400 ÷ 50 = 8 m/s^2")], XE, 580, 62, 100)
    bola_txt(c, t, C["s08.e"], "8.000 N", 1500, 560, 170, 62)


# ---------------- quem faz o papel ----------------
def b_papel(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("centrípeta", "g", 90, COR) + ps("não é força nova", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("é um", "i", 70) + [("papel:", "g", 70)] + ps("a resultante para o centro", "i", 70), XE, 440, passo=0.1)
        E.frase(c, t, C["s09.c"], ps("alguma força de verdade faz esse papel", "g", 58, TINTA2), XE, 620, passo=0.08)
        return
    if t < C["s11"]:
        for i, (k, kq, tit, quem, desenho) in enumerate((("s10.a", "s10.b", "pedra no fio", "o fio", "bola"), ("s10.c", "s10.d", "carro na curva", "o atrito do chão", "carro"),
                                                         ("s10.e", "s10.f", "a Lua", "a atração da Terra", "lua"))):
            x = 170 + i * 540
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, 220, 500, 720, p, prog_=p)
            E.frase(c, t, C[k] + 0.1, [(tit, "g", 50)], x + 30, 300)
            cx, cy, r = x + 250, 560, 150
            trilha(c, t, C[k] + 0.2, cx, cy, r)
            if desenho == "lua":
                E.foco(c, t, C[k] + 0.2, 0.4, lambda a, cx=cx, cy=cy: E.bola(c, cx, cy, 50, "#2F7FD8", a))
            Pp = movel_circ(c, t, C[k] + 0.3, cx, cy, r, 40, 150, "carro" if desenho == "carro" else "bola", vel=False, forca=True, tf=C[kq], s=28 if desenho != "carro" else 30, comp=110)
            if desenho == "bola" and t >= C[k] + 0.3:
                M.line(c, cx, cy, *Pp, TINTA2, ep(t, C[k] + 0.3, 0.4), 4)
            if desenho == "lua":
                E.foco(c, t, C[k] + 0.3, 0.4, lambda a, Pp=Pp: E.bola(c, *Pp, 28, "#C9C9C4", a))
            E.foco(c, t, C[kq], 0.4, lambda a, x=x, quem=quem: E.pilula(c, quem, x + 250, 820, 40, "b", fundo=E.COR, a=a))
        E.foco(c, t, C["s10.d"] + 1.4, 0.4, lambda a: E.escreve(c, "atrito: outra aula", 750, 900, 36, "i", TINTA2, a))
        E.foco(c, t, C["s10.f"] + 1.0, 0.4, lambda a: E.escreve(c, "gravitação: outra aula", 1270, 900, 36, "i", TINTA2, a))
        return
    E.frase(c, t, C["s11.a"], ps("e se o fio", "i", 72) + [("arrebenta?", "g", 72, COR)], XE, 220, passo=0.12)
    cx, cy, r = 1250, 600, 260
    trilha(c, t, C["s11"], cx, cy, r)
    tq = C["s11.b"]
    g0 = 200
    if t < tq:
        g = g0 + 40 * max(0.0, t - C["s11"])
        P, tg, _ = no_circulo(cx, cy, r, g)
        M.line(c, cx, cy, *P, TINTA2, ep(t, C["s11"], 0.4), 4)
        E.bola(c, *P, 30, a=ep(t, C["s11"], 0.4))
    else:
        gq = g0 + 40 * (tq - C["s11"])
        P0, tg, _ = no_circulo(cx, cy, r, gq)
        k = min(1.0, (t - tq) / 1.6)
        P = (P0[0] + tg[0] * 520 * k, P0[1] + tg[1] * 520 * k)
        M.line(c, *P0, P0[0] + tg[0] * 560, P0[1] + tg[1] * 560, F.VEL, 0.7 * ep(t, tq, 0.4), 5, dash=E.TRACO)
        E.bola(c, *P, 30)
        _, _, dentro = no_circulo(cx, cy, r, gq)
        if t >= C["s11.c"]:
            F.seta(c, *P0, P0[0] - dentro[0] * 260, P0[1] - dentro[1] * 260, ERRADO, ep(t, C["s11.c"], 0.3), 8)
            risca_em(c, t, C["s11.c"] + 0.5, P0[0] - dentro[0] * 60 - 50, P0[1] - dentro[1] * 160 + 50, P0[0] - dentro[0] * 200 + 50, P0[1] - dentro[1] * 160 - 50, 8)
    E.frase(c, t, C["s11.b"], ps("segue reto, pela", "i", 60) + [("tangente", "g", 60, F.VEL)], XE, 820, passo=0.1)
    E.frase(c, t, C["s11.c"], [("não", "g", 60, ERRADO)] + ps("para fora", "i", 60), XE, 930, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("força para fora:", "i", 64) + [("centrífuga", "g", 62, ERRADO)], XE, 330, passo=0.12)
    risca_em(c, t, C["s12.a"] + 1.4, XE + 470, 340, XE + 830, 290)
    cx, cy, r = 1350, 640, 300
    trilha(c, t, C["s12"], cx, cy, r)
    g = 300 + min(50, 12 * max(0.0, t - C["s12.b"]))
    P, tg, dentro = no_circulo(cx, cy, r, g)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: carro_cima(c, *P, math.degrees(math.atan2(tg[1], tg[0])), 46, a))
    if t >= C["s12.b"]:
        P0, tg0, _ = no_circulo(cx, cy, r, 300)
        M.line(c, *P0, P0[0] + tg0[0] * 300, P0[1] + tg0[1] * 300, F.VEL, 0.6 * ep(t, C["s12.b"], 0.4), 5, dash=E.TRACO)
        E.foco(c, t, C["s12.b"] + 0.4, 0.4, lambda a: E.escreve(c, "você tenta seguir reto", P0[0] - 60, P0[1] + 110, 40, "i", F.VEL, a))
    E.frase(c, t, C["s12.b"], ps("seu corpo segue reto:", "i", 58) + [("inércia", "g", 58, F.VEL)], XE, 480, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("o carro vira para dentro", "i", 58), XE, 590, passo=0.1)
    if t >= C["s12.d"]:
        F.seta(c, *P, P[0] + dentro[0] * 160, P[1] + dentro[1] * 160, E.COR, ep(t, C["s12.d"], 0.3), 10)
    E.frase(c, t, C["s12.d"], ps("a porta vem até você", "g", 58), XE, 750, passo=0.1)
    E.frase(c, t, C["s12.e"], ps("e empurra para o", "i", 62) + [("centro", "g", 62, COR)], XE, 860, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.foco(c, t, C["s13.a"], 0.5, lambda a: sub(c, "F_{cp} = m · f{v^2}{R}", W / 2, 360, 110, "g", BR, a, "center"))
        for i, (k, l, r_) in enumerate((("s13.b", "v × 2", "F × 4"), ("s13.c", "v × 3", "F × 9"), ("s13.d", "R × 2", "F ÷ 2"))):
            y = 580 + i * 140
            E.foco(c, t, C[k], 0.5, lambda a, l=l, r_=r_, y=y: (sub(c, l, 860, y, 90, "g", BR, a, "right"), E.escreve(c, "→", 910, y, 90, "g", CLARO, a),
                                                              sub(c, r_, 1040, y, 90, "g", CLARO, a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("proporcional ao", "i", 62, CLARO) + ps("quadrado de v", "g", 62, BR), W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s14.a"] + 1.6, ps("e inversamente ao raio", "i", 62, CLARO), W / 2, 380, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("tudo muda junto", "i", 64, CLARO), W / 2, 600, "center", 0.12)
    E.frase(c, t, C["s14.c"], ps("faça a conta inteira", "g", 66, BR), W / 2, 760, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s15")
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "pedra de", XE, 330, 62, "i", TINTA, a), F.medida(c, "0,5", "kg", XE + 270, 330, 76, COR, a)))
    E.foco(c, t, C["s15.a"] + 1.4, 0.5, lambda a: (E.escreve(c, "fio de", XE, 450, 62, "i", TINTA, a), F.medida(c, 2, "m", XE + 210, 450, 76, COR, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "a", XE, 570, 62, "i", TINTA, a), F.medida(c, 4, "m/s", XE + 70, 570, 76, COR, a)))
    E.frase(c, t, C["s15.c"], ps("força do fio = ?", "g", 70), XE, 740, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("e com", "i", 62) + [("v × 2?", "g", 64, COR)], XE, 860, passo=0.12)

    def desenho():
        cx, cy, r = 1450, 560, 260
        trilha(c, t, C["s15.a"], cx, cy, r)
        P = movel_circ(c, t, C["s15.a"], cx, cy, r, 35, 120, "bola", vel=True, tv=C["s15.b"], s=30, comp=170)
        if t >= C["s15.a"]:
            M.line(c, cx, cy, *P, TINTA2, ep(t, C["s15.a"], 0.4), 4)
    pausa(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cx, cy, r = 1500, 560, 220
    trilha(c, t, C["s17"], cx, cy, r)
    P = movel_circ(c, t, C["s17"], cx, cy, r, 35, 120, "bola", vel=False, forca=True, tf=C["s17.a"], rot_f="F", s=28, comp=140)
    if t >= C["s17"]:
        M.line(c, cx, cy, *P, TINTA2, ep(t, C["s17"], 0.4), 4)
    if t < C["s18"]:
        E.frase(c, t, C["s17.a"], ps("quem faz a centrípeta:", "i", 60) + [("o", "g", 60), ("fio", "g", 60, COR)], XE, 220, passo=0.1)
        contas(c, t, [(C["s17.b"], "v^2 = 16"), (C["s17.c"], "a_{cp} = 16 ÷ 2 = 8 m/s^2"), (C["s17.d"], "F = 0,5 · 8")], XE, 400, 76, 130)
        bola_txt(c, t, C["s17.d"] + 0.6, "4 N", 560, 860, 110, 60)
        return
    E.frase(c, t, C["s18"], ps("velocidade dobrada:", "i", 62), XE, 220, passo=0.1)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: sub(c, "F × 4", XE, 380, 110, "g", COR, a))
    bola_txt(c, t, C["s18.b"], "16 N", 760, 350, 100, 56)
    contas(c, t, [(C["s18.c"], "8^2 = 64 → 64 ÷ 2 = 32 → 0,5 · 32 = 16", CERTO)], XE, 640, 58)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s19", (("s19.a", [("curva:", "i", 64), ("aceleração", "g", 60, F.ACEL), ("v²/R", "g", 60), ("para", "i", 64), ("o", "i", 64), ("centro", "i", 64)]),
                            ("s19.b", [("centrípeta", "g", 60, COR), ("=", "g", 60), ("resultante", "i", 64), ("para", "i", 64), ("o", "i", 64), ("centro", "i", 64)]),
                            ("s19.c", [("uma", "i", 64), ("força", "g", 60), ("de", "i", 64), ("verdade", "g", 60, COR), ("faz", "i", 64), ("o", "i", 64), ("papel", "i", 64)])), C["s20"])
    if t < C["s20"]:
        return

    def desenho():
        cx, cy, r = 620, 860, 150
        if t >= C["s20.a"]:
            pt = M.paint(TINTA2, ep(t, C["s20.a"], 0.5), stroke=40)
            c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, 180, False, pt)
        g = 180 - min(180, 60 * max(0.0, t - C["s20.a"]))
        P, tg, _ = no_circulo(cx, cy, r, g)
        E.foco(c, t, C["s20.a"], 0.4, lambda a: carro_cima(c, *P, math.degrees(math.atan2(-tg[1], -tg[0])), 30, a))
    proxima(c, t, C, "s20", ((C["s20.a"], [("Carro", "g", 110, COR), ("na", "i", 110), ("curva", "g", 110)]),
                             (C["s20.b"], [("seco,", "i", 72), ("molhado", "i", 72), ("e", "i", 72), ("inclinado", "g", 68, COR)])), "s20.d", "s20.e", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, curva=b_curva, formula=b_formula, papel=b_papel, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
