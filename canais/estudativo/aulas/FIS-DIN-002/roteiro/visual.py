"""Visual — Estudativo · FIS-DIN-002: segunda lei de Newton, F = m·a.
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001 (força laranja, resultante em tinta grossa,
aceleração violeta, velocidade petróleo, corpo cinza no diagrama). Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-002_segunda_lei_de_newton.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("lei", "exemplo", "proporcao", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
assert 3000 / 1000 == 3 and 30 - 10 == 20 and 20 / 5 == 4 and 30 / 5 == 6
assert 60 / 20 == 3 and 60 / 60 == 1
assert 100 - 40 == 60 and 60 / 20 == 3 and 0 + 3 * 4 == 12 and 60 / 40 == 1.5
assert 60 - 10 == 50 and 50 != 2 * 20  # dobrar uma só força (30 → 60) não dobra a resultante

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
def carrinho_mercado(c, x, y, w, a=1.0, cheio=False):
    """carrinho de supermercado de lado, rodas em y, centro em x"""
    if a <= 0:
        return
    h = w * 0.62
    top, bot = y - w * 0.18 - h, y - w * 0.18
    p = skia.Path()
    p.moveTo(x - w / 2, top); p.lineTo(x + w / 2, top); p.lineTo(x + w * 0.36, bot); p.lineTo(x - w * 0.42, bot); p.close()
    if cheio:
        for i, (dx, cor, k) in enumerate(((-0.34, "#2F7FD8", 0.42), (-0.06, "#16A36A", 0.5), (0.2, "#E5484D", 0.38), (-0.2, "#FFC400", 0.3))):
            hh = h * k
            M.rrect(c, x + dx * w, bot - hh - (h * 0.42 if i == 3 else 0), w * 0.24, hh, 6, cor, a)
    c.drawPath(p, M.paint(mix_(TINTA2, BR, 0.85), 0.35 * a))
    pt = M.paint(TINTA2, a, stroke=6)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    for k in range(1, 5):
        M.line(c, x - w / 2 + w * k / 5, top, x - w * 0.42 + w * 0.78 * k / 5, bot, TINTA2, a * 0.5, 3)
    M.line(c, x - w / 2, top, x - w / 2 - w * 0.12, top - w * 0.14, TINTA2, a, 7)
    M.line(c, x - w * 0.42, bot, x - w * 0.36, y - w * 0.07, TINTA2, a, 6)
    M.line(c, x + w * 0.36, bot, x + w * 0.3, y - w * 0.07, TINTA2, a, 6)
    for wx in (x - w * 0.36, x + w * 0.3):
        c.drawCircle(wx, y - w * 0.06, w * 0.06, M.paint("#1B1B20", a))


def mix_(a, b, k):
    return E.mix(a, b, k)


def caixa_forcas(c, t, t0, cx, cy, w, h, rot, forcas, cor=None):
    """bloco no chão com forças horizontais: forcas = [(instante, sentido ±1, comp, rótulo, módulo)]"""
    E.foco(c, t, t0, 0.5, lambda a: F.bloco(c, cx, cy, w, h, rot, cor or TINTA2, a, size=min(64, h * 0.4)))
    if t >= t0:
        F.chao(c, cx - w * 1.6, cx + w * 1.6, cy + h / 2, ep(t, t0, 0.4))
    for ti, sg, comp, r, mod in forcas:
        P = (cx + sg * w / 2, cy)
        seta_f(c, t, ti, P, 0 if sg > 0 else 180, comp, r, modulo=mod, lpos=(cx + sg * (w / 2 + max(comp / 2, 110)), cy - 50), size=52)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            # os dois carrinhos recebem a mesma força; em s01.c o vazio dispara e o cheio mal anda
            s = max(0.0, t - C["s01.c"])
            xv = 760 + min(900, 0.5 * 260 * s * s)
            xc = 760 + min(900, 0.5 * 40 * s * s)
            for k, (yy, x, cheio, rot) in enumerate(((520, xv, False, "vazio"), (920, xc, True, "cheio"))):
                tk = C["s01.a"] if k == 0 else C["s01.b"]
                E.foco(c, t, tk, 0.5, lambda a, x=x, yy=yy, cheio=cheio: carrinho_mercado(c, x, yy, 280, a, cheio))
                if t >= tk:
                    F.chao(c, 560, 1840, yy, ep(t, tk, 0.4))
                    E.foco(c, t, tk + 0.3, 0.4, lambda a, yy=yy, rot=rot: E.escreve(c, rot, XE, yy - 30, 54, "i", TINTA2, a))
                if t < C["s01.c"]:
                    seta_f(c, t, tk + 0.4, (x - 220, yy - 140), 0, 120, "F", lpos=(x - 160, yy - 200), size=50)
            E.frase(c, t, C["s01"], ps("a mesma força", "i", 80), XE, 230, passo=0.12)
            E.frase(c, t, C["s01.c"], [("o", "i", 70), ("vazio", "g", 70, COR), ("dispara", "i", 70)], XE, 1010, passo=0.12)
            E.foco(c, t, C["s01.d"], 0.5, lambda a: sub(c, "a = ?", 1500, 230, 96, "g", F.ACEL, a, "center"))
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "força, massa, aceleração", 0), ("s02.c", "ler como proporção", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "força resultante,", "a soma das forças"), ("s03.c", "aceleração,", "quanto v muda por segundo")))


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("resultante zero:", "i", 64, TINTA2) + ps("mantém", "g", 60, TINTA2), XE, 220, passo=0.1)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: sub(c, "F_{R} ≠ 0", XE, 380, 96, "g", COR, a))
        E.frase(c, t, C["s04.a"] + 0.6, [("→", "g", 80, TINTA2), ("muda", "i", 84), ("a", "i", 84), ("velocidade", "i", 84)], XE + 380, 380, passo=0.12)
        E.frase(c, t, C["s04.b"], [("acelera", "g", 96, F.ACEL)], XE, 520)
        cx, cy = 1480, 560
        E.foco(c, t, C["s04.a"], 0.5, lambda a: F.bloco(c, cx, cy, 220, 170, None, TINTA2, a))
        if t >= C["s04.a"]:
            F.chao(c, cx - 300, cx + 300, cy + 85, ep(t, C["s04.a"], 0.4))
        seta_f(c, t, C["s04.a"] + 0.3, (cx + 110, cy), 0, 200, "F_{R}", cor=TINTA, lpos=(cx + 200, cy - 50), larg=13)
        F.vetor(c, t, C["s04.b"], (cx - 110, cy - 150), (cx + 110, cy - 150), "a", None, F.ACEL, 8, size=50)
        sub_em(c, t, C["s04.c"], "F_{R} = m · a", W / 2, 860, 170, "g", TINTA, "center")
        return
    if t < C["s06"]:
        formula_nova(c, t, C["s05"] - 0.2, "F_{R} = m · a", XE, 290, 150,
                     (("F_{R}", "força resultante", "N"), ("m", "massa", "kg"), ("a", "aceleração", "m/s^2")), (C["s05.a"], C["s05.b"], C["s05.c"]))
        cx, cy = 1500, 560
        E.foco(c, t, C["s05.d"], 0.5, lambda a: F.bloco(c, cx, cy, 200, 160, "m", TINTA2, a, size=60))
        seta_f(c, t, C["s05.d"] + 0.3, (cx + 100, cy), 0, 190, "F_{R}", cor=TINTA, lpos=(cx + 190, cy - 50), larg=13)
        F.vetor(c, t, C["s05.d"] + 0.8, (cx - 100, cy + 150), (cx + 120, cy + 150), "a", None, F.ACEL, 8, size=50, lado=-1)
        E.foco(c, t, C["s05.d"] + 1.2, 0.4, lambda a: E.pilula(c, "mesmo sentido", cx, cy - 190, 44, "b", fundo=F.ACEL, a=a))
        return
    E.frase(c, t, C["s06.a"], ps("o que é", "i", 80) + [("1", "g", 80, COR), ("newton", "g", 80, COR)], XE, 230, passo=0.12)
    cx, cy = 960, 560
    E.foco(c, t, C["s06.b"], 0.5, lambda a: F.bloco(c, cx, cy, 220, 170, "1 kg", TINTA2, a, size=56))
    if t >= C["s06.b"]:
        F.chao(c, cx - 400, cx + 400, cy + 85, ep(t, C["s06.b"], 0.4))
    seta_f(c, t, C["s06.b"] + 0.4, (cx + 110, cy), 0, 200, "F_{R}", cor=TINTA, modulo="1 N", lpos=(cx + 230, cy - 60), larg=13)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (F.seta(c, cx - 110, cy + 160, cx + 110, cy + 160, F.ACEL, a, 8),
                                             F.medida(c, 1, "m/s^2", cx + 150, cy + 178, 56, F.ACEL, a)))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: sub(c, "N = kg · m/s^2", W / 2, 940, 110, "g", COR, a, "center"))


# ---------------- exemplos ----------------
def b_exemplo(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07"], ps("vamos usar", "i", 72, COR), XE, 200)
        E.foco(c, t, C["s07.a"], 0.5, lambda a: (F.carrinho(c, 1350, 520, 420, a=a), F.medida(c, "1.000", "kg", 1350, 250, 64, TINTA, a, "center")))
        if t >= C["s07.a"]:
            F.chao(c, 1000, 1750, 520, ep(t, C["s07.a"], 0.4))
        seta_f(c, t, C["s07.b"], (1580, 420), 0, 180, "F_{R}", cor=TINTA, modulo="3.000 N", lpos=(1640, 360), larg=13, size=52)
        contas(c, t, [(C["s07.c"], "a = F_{R} ÷ m"), (C["s07.d"], "a = 3.000 ÷ 1.000")], XE, 400, 84, 140)
        bola_txt(c, t, C["s07.e"], "3 m/s^2", 520, 820, 150, 70)
        E.frase(c, t, C["s07.e"] + 1.2, ps("a cada segundo,", "i", 52) + [("+3 m/s", "g", 52, F.VEL)], 1300, 830, "center", 0.1)
        return
    E.frase(c, t, C["s08.a"], [("caixa", "i", 76)], XE, 200)
    E.foco(c, t, C["s08.a"] + 0.3, 0.5, lambda a: F.medida(c, 5, "kg", XE + 240, 200, 76, TINTA, a))
    caixa_forcas(c, t, C["s08.a"], 1350, 430, 220, 170, "5 kg", ((C["s08.b"], 1, 240, "F_{1}", "30 N"), (C["s08.c"], -1, 80, "F_{2}", "10 N")))
    contas(c, t, [(C["s08.d"], "F_{R} = 30 − 10 = 20 N"), (C["s08.e"], "a = 20 ÷ 5")], XE, 680, 84, 140)
    bola_txt(c, t, C["s08.f"], "4 m/s^2", 1450, 780, 150, 70)
    E.foco(c, t, C["s08.f"] + 1.0, 0.4, lambda a: E.pilula(c, "para a direita", 1450, 980, 44, "b", fundo=TINTA, a=a))


# ---------------- proporção ----------------
def linha_prop(c, t, t0, t1, y, w0, w1, f0, f1, a0, a1, rot0, rot1, rf0, rf1, ra0, ra1):
    """antes → depois: bloco, força e aceleração; t1 = instante do depois"""
    for k, (tk, x, ww, fl, al, rb, rf, ra) in enumerate(((t0, 520, w0, f0, a0, rot0, rf0, ra0), (t1, 1300, w1, f1, a1, rot1, rf1, ra1))):
        E.foco(c, t, tk, 0.5, lambda a, x=x, ww=ww, rb=rb: F.bloco(c, x, y, ww, 150, rb, TINTA2, a, size=48))
        seta_f(c, t, tk + 0.3, (x + ww / 2, y), 0, fl, None, cor=E.COR, modulo=rf, lpos=(x + ww / 2 + fl / 2, y - 40), size=52)
        if t >= tk + 0.6:
            F.seta(c, x - ww / 2, y + 130, x - ww / 2 + al, y + 130, F.ACEL, 1.0, 8, p=ease_out(prog(t, tk + 0.6, 0.5)))
            E.foco(c, t, tk + 0.9, 0.4, lambda a, x=x, ww=ww, al=al, ra=ra: sub(c, ra, x - ww / 2 + al + 20, y + 150, 50, "g", F.ACEL, a))
    E.foco(c, t, t1 - 0.3, 0.4, lambda a: E.escreve(c, "→", 870, y + 20, 90, "g", TINTA2, a))


def b_proporcao(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("leitura como", "i", 76) + [("proporção", "g", 76, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s09.a"], ps("mesma massa,", "i", 60, TINTA2) + [("força", "g", 60), ("dobrada", "g", 60, COR)], XE, 330, passo=0.1)
        linha_prop(c, t, C["s09.a"], C["s09.a"] + 1.2, 560, 200, 200, 140, 280, 140, 280, "m", "m", "F", "2F", "a", "2a")
        E.frase(c, t, C["s09.b"], ps("a aceleração", "i", 60) + [("dobra", "g", 60, F.ACEL)], XE, 860, passo=0.1)
        pilula_em(c, t, C["s09.c"], "diretamente proporcionais", 1300, 990, 50, E.COR)
        return
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("mesma força,", "i", 60, TINTA2) + [("massa", "g", 60), ("dobrada", "g", 60, COR)], XE, 220, passo=0.1)
        linha_prop(c, t, C["s10.a"], C["s10.a"] + 1.2, 470, 200, 400, 200, 200, 240, 120, "m", "2m", "F", "F", "a", "a/2")
        E.frase(c, t, C["s10.b"], ps("a aceleração cai", "i", 60) + [("pela", "g", 60, F.ACEL), ("metade", "g", 60, F.ACEL)], XE, 760, passo=0.1)
        pilula_em(c, t, C["s10.c"], "inversamente proporcionais", 1300, 880, 50, E.COR)
        E.frase(c, t, C["s10.d"], ps("mais massa,", "i", 54, TINTA2) + ps("menos aceleração", "g", 54), XE, 1000, passo=0.1)
        return
    E.frase(c, t, C["s11.a"], ps("com números:", "i", 70), XE, 200)
    E.foco(c, t, C["s11.a"] + 0.5, 0.5, lambda a: sub(c, "F_{R} = 60 N", XE + 470, 200, 80, "g", COR, a))
    for k, (tk, x, cheio, m, ac) in enumerate(((C["s11.b"], 560, False, "20 kg", "3 m/s^2"), (C["s11.c"], 1360, True, "60 kg", "1 m/s^2"))):
        E.foco(c, t, tk, 0.5, lambda a, x=x, cheio=cheio: carrinho_mercado(c, x, 640, 320, a, cheio))
        E.foco(c, t, tk + 0.3, 0.4, lambda a, x=x, m=m: F.medida(c, *m.split(), x, 350, 64, TINTA, a, "center"))
        E.foco(c, t, tk + 0.8, 0.4, lambda a, x=x, m=m, ac=ac: sub(c, "a = 60 ÷ " + m.split()[0] + " = " + ac, x, 790, 64, "g", F.ACEL, a, "center"))
    E.frase(c, t, C["s11.d"], [("3×", "g", 70, COR), ("a", "i", 76), ("massa,", "i", 76), ("1/3", "g", 70, F.ACEL), ("da", "i", 76), ("aceleração", "i", 76)],
            W / 2, 960, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("uma força só, em vez da resultante", "i", 64), XE + 470, 200, passo=0.1)
    caixa_forcas(c, t, C["s12.a"], 1350, 440, 220, 170, "5 kg", ((C["s12.a"] + 0.3, 1, 240, "F_{1}", "30 N"), (C["s12.a"] + 0.6, -1, 80, "F_{2}", "10 N")))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: sub(c, "a = 30 ÷ 5 = 6", XE, 720, 96, "g", ERRADO, a))
    risca_em(c, t, C["s12.c"], XE - 10, 740, XE + 690, 640)
    if t >= C["s12.c"]:
        q = 0.5 + 0.5 * math.sin((t - C["s12.c"]) * 6)
        c.drawCircle(1350 - 110 - 40, 440, 90, M.paint(ERRADO, 0.6 * q * ep(t, C["s12.c"], 0.3), stroke=6))
    E.frase(c, t, C["s12.c"] + 0.8, ps("os 10 N também agem", "i", 56, TINTA2), XE, 840, passo=0.1)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: sub(c, "a = 20 ÷ 5 = 4", 1300, 960, 96, "g", CERTO, a, "center"))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("mudou", "i", 70, CLARO) + [("só", "g", 70, BR), ("uma", "g", 70, BR), ("coisa?", "g", 70, BR)], W / 2, 300, "center", 0.12)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: sub(c, "F × 3,  m igual", 860, 520, 84, "g", BR, a, "right"))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: sub(c, "→  a × 3", 920, 520, 84, "g", CLARO, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: sub(c, "m × 4,  F igual", 860, 720, 84, "g", BR, a, "right"))
        E.foco(c, t, C["s13.e"], 0.5, lambda a: sub(c, "→  a ÷ 4", 920, 720, 84, "g", CLARO, a))
        E.frase(c, t, C["s13.e"] + 1.0, ps("sem refazer a conta", "i", 60, CLARO), W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("funciona porque", "i", 64, CLARO), W / 2, 200, "center", 0.1)
    E.foco(c, t, C["s14.a"] + 0.5, 0.5, lambda a: sub(c, "F_{R} = m · a  é uma multiplicação", W / 2, 330, 72, "g", BR, a, "center"))
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("mudou uma entre várias forças", "i", 64, CLARO),
            W / 2, 520, "center", 0.1)
    E.foco(c, t, C["s14.b"] + 1.6, 0.5, lambda a: sub(c, "30 − 10 = 20", 860, 700, 80, "g", BR, a, "right"))
    E.foco(c, t, C["s14.b"] + 2.4, 0.5, lambda a: sub(c, "60 − 10 = 50", 1060, 700, 80, "g", CLARO, a))
    E.foco(c, t, C["s14.b"] + 2.8, 0.4, lambda a: E.pilula(c, "uma força dobrou, a resultante não", W / 2, 820, 44, "b", fundo=E.COR, a=a))
    E.frase(c, t, C["s14.c"], ps("calcule a nova resultante", "g", 60, BR), W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s15")
    E.frase(c, t, C["s15.a"], [("caixa", "i", 70)], XE, 330)
    E.foco(c, t, C["s15.a"] + 0.3, 0.5, lambda a: (F.medida(c, 20, "kg", XE + 210, 330, 76, COR, a), E.escreve(c, "parada", XE + 460, 330, 60, "i", TINTA2, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (F.medida(c, 100, "N", XE, 460, 76, COR, a), E.escreve(c, "→", XE + 240, 460, 70, "g", TINTA2, a)))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (F.medida(c, 40, "N", XE + 360, 460, 76, COR, a), E.escreve(c, "←", XE + 540, 460, 70, "g", TINTA2, a)))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: sub(c, "a = ?", XE, 640, 90, "g", F.ACEL, a))
    E.foco(c, t, C["s15.e"], 0.5, lambda a: sub(c, "v depois de 4 s = ?", XE, 800, 80, "g", F.VEL, a))

    def desenho():
        caixa_forcas(c, t, C["s15.a"], 1450, 560, 220, 170, "20 kg", ((C["s15.b"], 1, 200, None, "100 N"), (C["s15.c"], -1, 80, None, "40 N")))
    pausa(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.frase(c, t, C["s17"], ps("resultante primeiro", "i", 72, COR), XE, 200)
        contas(c, t, [(C["s17.a"], "F_{R} = 100 − 40 = 60 N"), (C["s17.b"], "a = 60 ÷ 20")], XE, 400, 90, 160)
        bola_txt(c, t, C["s17.c"], "3 m/s^2", 1450, 600, 170, 76)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], ps("partiu do repouso", "i", 66, TINTA2), XE, 200)
    contas(c, t, [(C["s18.a"], "v_{0} = 0"), (C["s18.b"], "v = v_{0} + a · t = 0 + 3 · 4")], XE, 360, 84, 140)
    bola_txt(c, t, C["s18.c"], "12 m/s", 1540, 560, 150, 70, F.VEL)
    E.frase(c, t, C["s18.c"] + 1.0, [("e", "i", 60), ("com", "i", 60)], XE, 760, passo=0.1)
    E.foco(c, t, C["s18.c"] + 1.4, 0.4, lambda a: F.medida(c, 40, "kg?", XE + 200, 760, 72, COR, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: sub(c, "massa × 2  →  a ÷ 2 = 1,5 m/s^2", XE, 910, 76, "g", F.ACEL, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s19", (("s19.a", [("resultante", "g", 62), ("=", "g", 62, COR), ("massa", "i", 66), ("×", "g", 62, COR), ("aceleração", "i", 66)]),
                            ("s19.b", [("sempre", "i", 66), ("com", "i", 66), ("a", "i", 66), ("resultante", "g", 62, COR)]),
                            ("s19.c", [("é", "i", 66), ("uma", "i", 66), ("proporção", "g", 62, COR)])), C["s20"])
    if t < C["s20"]:
        return

    def desenho():
        E.foco(c, t, C["s20.b"], 0.5, lambda a: (F.parede(c, 1000, 640, 960, -1, a), pessoa(c, 760, 960, 70, a, inclina=20, braco=5)))
        F.vetor(c, t, C["s20.b"] + 0.4, (900, 700), (1000, 700), None, None, E.COR, 9)
        F.vetor(c, t, C["s20.b"] + 0.9, (1000, 800), (900, 800), None, None, E.COR, 9)
        E.foco(c, t, C["s20.b"] + 0.5, 0.4, lambda a: E.escreve(c, "você empurra", 1030, 715, 40, "i", TINTA, a))
        E.foco(c, t, C["s20.b"] + 1.0, 0.4, lambda a: E.escreve(c, "a parede empurra", 1030, 815, 40, "i", TINTA, a))
    proxima(c, t, C, "s20", ((C["s20.a"], [("Terceira", "g", 110, COR), ("lei", "i", 110)]),
                             (C["s20.c"], [("ação", "g", 90), ("e", "i", 90), ("reação", "g", 90, COR)])), "s20.d", "s20.e", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, exemplo=b_exemplo, proporcao=b_proporcao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
