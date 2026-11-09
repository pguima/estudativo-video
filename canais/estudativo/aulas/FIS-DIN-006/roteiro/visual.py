"""Visual — Estudativo · FIS-DIN-006: praticando as leis de Newton (cinco situações).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Prática: cada situação tem a tela da
questão (texto à esquerda, desenho à direita, relógio na pausa) e a tela da resposta (contas uma por fala, resultado na esfera).
Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-006_praticando_leis_de_newton.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "atalho", "questao5", "fim"))

# todas as contas da aula (g = 10 m/s²)
assert 0 == 20 ** 2 + 2 * (-5) * 40 and 1000 * 5 == 5000
assert 0 == 20 + 80 * (-0.25) and 1000 * 0.25 == 250  # o erro de não elevar ao quadrado
assert 70 * 10 == 700 and 70 * (10 + 1) == 770 and 770 / 10 == 77
assert 800 * 0.05 == 40 and 40 / 10 == 4 and 800 * 5 == 4000 and 4000 / 10 == 400

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
def garrafa(c, x, yb, s, a=1.0, giro=0.0):
    """garrafa deitada ou em pé; base em yb"""
    if a <= 0:
        return
    c.save(); c.translate(x, yb); c.rotate(giro)
    M.rrect(c, -s * 0.3, -s * 1.3, s * 0.6, s * 1.3, s * 0.15, "#3FA9D9", a)
    M.rrect(c, -s * 0.12, -s * 1.7, s * 0.24, s * 0.45, s * 0.06, "#3FA9D9", a)
    M.rrect(c, -s * 0.14, -s * 1.8, s * 0.28, s * 0.14, 3, E.COR, a)
    c.restore()


def barco(c, x, y, w, a=1.0, remo=0.0):
    """barco de lado na água (linha da água em y); remo = ângulo (graus) do remo"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x - w, y, 2 * w, 160), M.paint("#7FC8E8", 0.35 * a))
    M.line(c, x - w, y, x + w, y, "#3B8DB5", a, 5)
    p = skia.Path(); p.moveTo(x - w * 0.5, y - 50); p.lineTo(x + w * 0.55, y - 50); p.lineTo(x + w * 0.4, y + 30); p.lineTo(x - w * 0.42, y + 30); p.close()
    c.drawPath(p, M.paint("#8B5E3C", a))
    pessoa(c, x - 20, y - 50, 48, a, inclina=-10, braco=-30)
    g = math.radians(remo)
    M.line(c, x - 60, y - 120, x - 60 - math.sin(g) * 260, y - 120 + math.cos(g) * 260, "#6E4A2F", a, 9)


def elevador_q(c, t, t0, x, y, kg, w=380, h=520, s=72):
    """cabine com balança, pessoa e visor grande; devolve (pé, centro do corpo)"""
    piso = y + h - 30
    bw = 200

    def fn(a):
        elevador(c, x, y, w, h, a)
        balanca_chao(c, x + w / 2, piso - bw * 0.16, bw, kg, a)
        pessoa(c, x + w / 2, piso - bw * 0.16, s, a, braco=-80)
        M.rrect(c, x - 250, y + 60, 210, 100, 18, "#1B1B20", a)
        v, _, u = kg.partition(" ")
        F.medida(c, v, u, x - 145, y + 134, 60, "#7CFFB2", a, "center", cor_u="#7CFFB2")
    E.foco(c, t, t0, 0.5, fn)
    pe = (x + w / 2, piso - bw * 0.16)
    return pe, (x + w / 2, pe[1] - s * 2)


def dinamometro(c, x, ytop, L, a=1.0):
    """balança de gancho: argola em ytop, tubo com a mola (comprimento L) e gancho. Devolve o y do gancho"""
    if a <= 0:
        return ytop + 540
    c.drawCircle(x, ytop, 16, M.paint(TINTA2, a, stroke=6))
    tw, th = 90, 420
    M.rrect(c, x - tw / 2, ytop + 16, tw, th, 18, "#FFFFFF", 0.55 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - tw / 2, ytop + 16, tw, th), 18, 18), M.paint(TINTA, a, stroke=4))
    F.mola(c, x, ytop + 30, x, ytop + 60 + L, 8, 40, TINTA2, a, 4, 14)
    M.line(c, x - 30, ytop + 60 + L, x + 30, ytop + 60 + L, E.COR, a, 7)
    M.line(c, x, ytop + 60 + L, x, ytop + th + 60, TINTA2, a, 6)
    gy = ytop + th + 60
    c.drawArc(skia.Rect.MakeXYWH(x - 22, gy - 4, 44, 44), 180, -250, False, M.paint(TINTA2, a, stroke=6))
    return gy + 30


def mala(c, cx, ytop, w, h, a=1.0):
    if a <= 0:
        return
    M.line(c, cx - 30, ytop, cx - 30, ytop + 30, TINTA2, a, 6)
    M.line(c, cx + 30, ytop, cx + 30, ytop + 30, TINTA2, a, 6)
    M.line(c, cx - 30, ytop, cx + 30, ytop, TINTA2, a, 6)
    M.rrect(c, cx - w / 2, ytop + 30, w, h, 16, "#2F5DA8", a)
    M.line(c, cx - w / 2 + 20, ytop + 30 + h * 0.5, cx + w / 2 - 20, ytop + 30 + h * 0.5, "#1F4280", a, 5)


def situacao(c, t, C, cena, n):
    E.frase(c, t, C[cena + ".a"], [("situação", "i", 72, TINTA2), (str(n), "g", 80, COR)], XE, 200, passo=0.12)


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 220, COR), ("situações", "i", 110)], XE, 400, passo=0.14)
    E.frase(c, t, C["s01.a"] + 1.2, ps("do trânsito e do dia a dia", "i", 64, TINTA2), XE, 520, passo=0.1)
    for i, s in enumerate(("1ª lei", "2ª lei", "3ª lei")):
        E.foco(c, t, C["s01.b"] + 0.3 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 120 + i * 260, 680, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s01.c"], 0.6, lambda a: E.relogio(c, t, C["s01.c"], cx=1500, cy=480, r=170), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("antes de qualquer conta", "i", 72), XE, 200, passo=0.12)
    cx, cy = 1450, 560
    E.foco(c, t, C["s02.a"], 0.5, lambda a: F.bloco(c, cx, cy, 200, 160, None, TINTA2, a))
    seta_f(c, t, C["s02.b"], (cx, cy), -90, 210, "P", lpos=(cx + 60, cy + 250))
    seta_f(c, t, C["s02.b"] + 0.8, (cx + 100, cy), 0, 160, None)
    seta_f(c, t, C["s02.b"] + 1.1, (cx, cy - 80), 90, 150, None)
    E.frase(c, t, C["s02.a"], [("1.", "g", 64, COR)] + ps("desenhe as forças", "g", 64), XE, 360, passo=0.1)
    for i, (k, l1, l2) in enumerate((("s02.c", "resultante zero", "1ª lei"), ("s02.d", "resultante e aceleração", "2ª lei"), ("s02.e", "força entre dois corpos", "3ª lei"))):
        y = 540 + i * 140
        E.frase(c, t, C[k], [(l1, "i", 58), ("→", "g", 58, TINTA2), (l2, "g", 58, COR)], XE, y, passo=0.12)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C, "s03", 1)
    E.frase(c, t, C["s03.b"], ps("o carro freia de repente", "i", 66), XE, 360, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("a garrafa rola para a frente", "i", 66), XE, 480, passo=0.1)
    E.frase(c, t, C["s03.d"], ps("que força", "i", 76) + [("empurrou?", "g", 76, COR)], XE, 680, passo=0.12)

    def desenho():
        E.foco(c, t, C["s03.b"], 0.5, lambda a: F.carrinho(c, 1450, 760, 520, a=a))
        if t >= C["s03.b"]:
            F.chao(c, 1100, 1800, 760, ep(t, C["s03.b"], 0.4))
        dx = 80 * ease_out(prog(t, C["s03.c"], 0.8))
        E.foco(c, t, C["s03.c"], 0.4, lambda a: garrafa(c, 1380 + dx, 580, 50, a, 90))
    pausa(c, t, C, "s04", desenho)


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("nenhuma", "g", 110, ERRADO)], XE, 280)
    E.frase(c, t, C["s05.b"], ps("o freio age no carro, não na garrafa", "i", 56), XE, 420, passo=0.08)
    E.frase(c, t, C["s05.c"], [("inércia:", "g", 64, COR)] + ps("a garrafa mantém a velocidade", "i", 60), XE, 560, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("o carro para embaixo dela", "i", 60, TINTA2), XE, 680, passo=0.1)
    pilula_em(c, t, C["s05.d"] + 1.6, "1ª lei de Newton", XE + 250, 800, 52, E.COR)
    E.foco(c, t, C["s05"], 0.5, lambda a: F.carrinho(c, 1500, 760, 420, a=a))
    F.vetor(c, t, C["s05.c"], (1420, 420), (1620, 420), "v", None, F.VEL, 9, size=48)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: garrafa(c, 1470, 600, 44, a, 90))
    E.frase(c, t, C["s05.e"], [("cinto:", "g", 56, COR)] + ps("faz em você a força para trás", "i", 54), XE, 950, passo=0.1)


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C, "s06", 2)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (F.medida(c, "1.000", "kg", XE, 360, 76, COR, a), E.escreve(c, "a", XE + 330, 360, 64, "i", TINTA, a),
                                             F.medida(c, 20, "m/s", XE + 400, 360, 76, COR, a)))
    E.frase(c, t, C["s06.c"], ps("freia até parar em", "i", 64), XE, 490, passo=0.1)
    E.foco(c, t, C["s06.c"] + 1.0, 0.5, lambda a: F.medida(c, 40, "m", XE + 560, 490, 76, COR, a))
    E.frase(c, t, C["s06.d"], [("resultante", "g", 72), ("=", "g", 72, TINTA2), ("?", "g", 72, COR)], XE, 680, passo=0.12)

    def desenho():
        E.foco(c, t, C["s06.b"], 0.5, lambda a: F.carrinho(c, 1250, 900, 300, a=a))
        if t >= C["s06.b"]:
            F.chao(c, 1050, 1850, 900, ep(t, C["s06.b"], 0.4))
        if t >= C["s06.c"]:
            q = ep(t, C["s06.c"], 0.5)
            M.line(c, 1250, 960, 1750, 960, TINTA2, q, 4)
            E.foco(c, t, C["s06.c"] + 0.3, 0.4, lambda a: F.medida(c, 40, "m", 1500, 1020, 50, TINTA, a, "center"))
    pausa(c, t, C, "s07", desenho)


def b_resposta2(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("sem", "i", 66), ("o", "i", 66), ("tempo:", "i", 66), ("Torricelli", "g", 66, COR)], XE, 220, passo=0.12)
        contas(c, t, [(C["s08.b"], "v^2 = v_{0}^2 + 2 · a · Δs"), (C["s08.c"], "0 = 400 + 80 · a"), (C["s08.d"], "a = −5 m/s^2", F.ACEL)], XE, 400, 84, 150)
        E.frase(c, t, C["s08.d"] + 1.6, ps("o menos: está freando", "i", 54, TINTA2), XE, 860, passo=0.1)
        return
    E.frase(c, t, C["s09"], ps("segunda lei, com o módulo", "i", 66), XE, 220, passo=0.1)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: sub(c, "F_{R} = 1.000 · 5", XE, 400, 90, "g", TINTA, a))
    bola_txt(c, t, C["s09.b"], "5.000 N", 1480, 420, 160, 62)
    pilula_em(c, t, C["s09.c"], "para trás", 1480, 640, 50, TINTA)
    E.foco(c, t, C["s09.d"], 0.5, lambda a: sub(c, "0 = 20 + 80 · a", XE, 760, 76, "g", ERRADO, a))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: sub(c, "→ 250 N", XE + 620, 760, 76, "g", ERRADO, a))
    risca_em(c, t, C["s09.e"] + 0.8, XE - 10, 780, XE + 960, 700)
    E.frase(c, t, C["s09.e"] + 1.4, ps("pequena demais para parar um carro", "i", 54, TINTA2), XE, 900, passo=0.08)


# ---------------- situação 3 ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C, "s10", 3)
    E.frase(c, t, C["s10.b"], ps("uma pessoa rema um barco", "i", 66), XE, 360, passo=0.1)
    E.frase(c, t, C["s10.b"] + 1.2, [("para", "g", 62), ("a", "g", 62), ("frente", "g", 62)], XE, 460, passo=0.1)
    E.frase(c, t, C["s10.c"], [("quem", "g", 76, COR)] + ps("empurra o barco?", "i", 76), XE, 640, passo=0.12)

    def desenho():
        E.foco(c, t, C["s10.b"], 0.5, lambda a: barco(c, 1400, 820, 360, a, 30 + 10 * math.sin(t * 2)))
    pausa(c, t, C, "s11", desenho)


def b_resposta3(c, t, C, b):
    E.foco(c, t, C["s12"], 0.5, lambda a: barco(c, 1300, 700, 420, a, 35))
    pa = (1300 - 60 - math.sin(math.radians(35)) * 230, 700 - 120 + math.cos(math.radians(35)) * 230)
    seta_f(c, t, C["s12.a"], (pa[0] + 20, pa[1] + 30), 180, 180, None)
    E.foco(c, t, C["s12.a"] + 0.3, 0.4, lambda a: E.pilula(c, "na água", pa[0] - 100, pa[1] + 110, 40, "b", fundo=E.COR, a=a))
    seta_f(c, t, C["s12.b"], (pa[0] + 20, pa[1] - 40), 0, 180, None)
    E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.pilula(c, "no remo", pa[0] + 120, pa[1] - 100, 40, "b", fundo=E.COR, a=a))
    E.frase(c, t, C["s12.a"], ps("remo empurra água", "b", 58), XE, 240, passo=0.1)
    E.frase(c, t, C["s12.b"], ps("água empurra remo", "b", 58, COR), XE, 340, passo=0.1)
    E.frase(c, t, C["s12.c"], [("é", "i", 66), ("a", "i", 66), ("água", "g", 66, COR)] + ps("que empurra", "i", 66), XE, 900, passo=0.12)
    pilula_em(c, t, C["s12.c"] + 2.0, "3ª lei", XE + 120, 480, 52, E.COR)
    E.frase(c, t, C["s12.d"], ps("não se anulam: corpos diferentes", "i", 52, TINTA2), XE, 1010, passo=0.08)


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C, "s13", 4)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (E.escreve(c, "pessoa de", XE, 360, 62, "i", TINTA, a), F.medida(c, 70, "kg", XE + 310, 360, 76, COR, a)))
    E.frase(c, t, C["s13.c"], ps("elevador", "i", 62) + [("sobe", "g", 62), ("acelerando", "g", 62, COR)], XE, 490, passo=0.1)
    E.foco(c, t, C["s13.c"] + 1.2, 0.5, lambda a: F.medida(c, 1, "m/s^2", XE, 600, 76, F.ACEL, a))
    E.frase(c, t, C["s13.d"], [("normal", "g", 72), ("=", "g", 72, TINTA2), ("?", "g", 72, COR)], XE, 790, passo=0.12)

    def desenho():
        elevador_q(c, t, C["s13.b"], 1350, 300, "? kg")
        F.vetor(c, t, C["s13.c"], (1810, 700), (1810, 520), "a", None, F.ACEL, 9, size=48)
    pausa(c, t, C, "s14", desenho)


def b_resposta4(c, t, C, b):
    kg = "77 kg" if t >= C["s15.e"] else "70 kg"
    pe, cm = elevador_q(c, t, C["s15"], 1350, 300, kg)
    seta_f(c, t, C["s15.a"], (pe[0] - 50, cm[1]), -90, 160, "P", modulo="700 N", lpos=(1240, 720), size=46)
    seta_f(c, t, C["s15.a"] + 0.6, (pe[0] + 50, pe[1]), 90, 200, "N", lpos=(pe[0] + 130, pe[1] - 180), size=48)
    F.vetor(c, t, C["s15"], (1810, 700), (1810, 520), "a", None, F.ACEL, 9, size=48)
    E.frase(c, t, C["s15.a"] + 1.8, ps("aceleração para cima:", "i", 58) + ps("N vence P", "g", 58, COR), XE, 230, passo=0.1)
    contas(c, t, [(C["s15.b"], "N = m · (g + a)"), (C["s15.c"], "N = 70 · 11")], XE, 400, 84, 150)
    bola_txt(c, t, C["s15.d"], "770 N", 520, 800, 130, 60)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "mostra 77 kg", 1000, 960, 46, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16"], ps("o atalho que mais salva tempo", "i", 72, CLARO), W / 2, 180, "center", 0.1)
    E.frase(c, t, C["s16.a"], ps("antes da conta:", "i", 64, CLARO) + ps("para onde aponta a?", "g", 64, BR), W / 2, 330, "center", 0.1)
    y1, y2 = 560, 760
    E.frase(c, t, C["s16.b"], ps("velocidade aumentando:", "i", 58, CLARO), 300, y1, "left", 0.1)
    F.seta(c, 1100, y1 - 20, 1300, y1 - 20, F.VEL, ep(t, C["s16.b"] + 0.5, 0.3), 9) if t >= C["s16.b"] + 0.5 else None
    F.seta(c, 1400, y1 - 20, 1600, y1 - 20, "#B48CFF", ep(t, C["s16.b"] + 0.9, 0.3), 9) if t >= C["s16.b"] + 0.9 else None
    E.frase(c, t, C["s16.c"], ps("freando:", "i", 58, CLARO), 300, y2, "left", 0.1)
    F.seta(c, 1100, y2 - 20, 1300, y2 - 20, F.VEL, ep(t, C["s16.c"] + 0.4, 0.3), 9) if t >= C["s16.c"] + 0.4 else None
    F.seta(c, 1600, y2 - 20, 1400, y2 - 20, "#B48CFF", ep(t, C["s16.c"] + 0.8, 0.3), 9) if t >= C["s16.c"] + 0.8 else None
    for x, s, cor in ((1200, "v", F.VEL), (1500, "a", "#B48CFF")):
        E.foco(c, t, C["s16.b"] + 0.5, 0.4, lambda a, x=x, s=s, cor=cor: centro(c, s, x, 470, 56, "g", cor, a))
    E.frase(c, t, C["s16.d"], ps("a resultante aponta", "i", 62, CLARO) + ps("para o mesmo lado", "g", 62, BR), W / 2, 950, "center", 0.1)


# ---------------- situação 5 ----------------
def b_questao5(c, t, C, b):
    situacao(c, t, C, "s17", 5)
    E.frase(c, t, C["s17.b"], ps("mala no dinamômetro, parada", "i", 62), XE, 360, passo=0.1)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: (E.escreve(c, "estica", XE, 490, 62, "i", TINTA, a), F.medida(c, 5, "cm", XE + 210, 490, 76, COR, a)))
    E.foco(c, t, C["s17.d"], 0.5, lambda a: (E.escreve(c, "k =", XE, 620, 66, "g", TINTA, a), F.medida(c, 800, "N/m", XE + 130, 620, 76, COR, a)))
    E.frase(c, t, C["s17.e"], [("massa", "g", 72), ("=", "g", 72, TINTA2), ("?", "g", 72, COR)], XE, 800, passo=0.12)

    def desenho():
        E.foco(c, t, C["s17.b"], 0.5, lambda a: (F.teto(c, 1300, 1600, 160, a), dinamometro(c, 1450, 180, 220, a), mala(c, 1450, 720, 260, 200, a)))
    pausa(c, t, C, "s18", desenho)


def b_resposta5(c, t, C, b):
    contas(c, t, [(C["s19.a"], "5 cm = 0,05 m"), (C["s19.b"], "F = 800 · 0,05 = 40 N"), (C["s19.d"], "F = P"), (C["s19.e"], "40 = m · 10")],
           XE, 230, 80, 130)
    bola_txt(c, t, C["s19.f"], "4 kg", 1500, 420, 150, 70)
    E.foco(c, t, C["s19.f"] + 1.6, 0.5, lambda a: sub(c, "800 · 5 = 4.000 N → 400 kg", XE, 900, 66, "g", ERRADO, a))
    risca_em(c, t, C["s19.f"] + 3.6, XE - 10, 915, XE + 900, 850)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s20", (("s20.a", [("desenhe", "g", 66), ("as", "i", 70), ("forças", "i", 70)]),
                            ("s20.b", [("para", "i", 70), ("onde", "i", 70), ("aponta", "i", 70), ("a", "g", 66, F.ACEL), ("aceleração", "g", 66, F.ACEL)]),
                            ("s20.c", [("escolha", "i", 70), ("a", "i", 70), ("lei", "g", 66, COR), ("e", "i", 70), ("faça", "i", 70), ("a", "i", 70), ("conta", "g", 66)])), C["s21"])
    if t < C["s21"]:
        return

    def desenho():
        cx, cy = 640, 860
        E.foco(c, t, C["s21.a"], 0.5, lambda a: F.bloco(c, cx, cy, 220, 150, None, TINTA2, a))
        if t >= C["s21.a"]:
            F.chao(c, cx - 330, cx + 330, cy + 75, ep(t, C["s21.a"], 0.4))
        seta_f(c, t, C["s21.a"] + 0.4, (cx + 110, cy), 0, 170, "F", lpos=(cx + 220, cy - 40), size=48)
        seta_f(c, t, C["s21.a"] + 0.8, (cx - 60, cy + 75), 180, 170, "F_{at}", lpos=(cx - 260, cy + 50), size=48)
    proxima(c, t, C, "s21", ((C["s21.a"], [("Força", "g", 100), ("de", "i", 100), ("atrito", "g", 100, COR)]),
                             (C["s21.b"], [("e", "i", 70), ("o", "i", 70), ("freio", "g", 66), ("ABS", "g", 66, COR)])), "s21.c", "s21.d", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, atalho=b_atalho,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
