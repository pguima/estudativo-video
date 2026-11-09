"""Visual — Estudativo · FIS-DIN-008: plano inclinado (decompor o peso; aceleração com e sem atrito).
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula: eixos girados tracejados (ao
longo da rampa e perpendicular); componentes do peso em laranja mais claro, com tracejado de projeção (como F.componentes);
P·sen θ sempre rampa abaixo, P·cos θ sempre contra a rampa. Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-008_plano_inclinado.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("decompor", "normal", "sematrito", "comatrito", "erro", "atalho", "questao", "fim"))

# todas as contas da aula (g = 10 m/s²; rampa "sen 0,6 / cos 0,8")
assert 10 * 0.5 == 5
assert 10 * 10 == 100 and 100 * 0.6 == 60 and 100 * 0.8 == 80 and 0.25 * 80 == 20 and 60 - 20 == 40 and 40 / 10 == 4
assert 0.25 * 100 == 25 and (60 - 25) / 10 == 3.5  # o erro: normal = peso
assert round(10 * (0.6 - 0.25 * 0.8), 9) == 4
assert round(0.5 * 0.8, 9) == 0.4 and round(0.6 - 0.4, 9) == 0.2 and round(10 * 0.2, 9) == 2
assert 2 * 10 * 0.8 == 16 and 2 * 10 * 0.6 == 12 and 0.5 * 16 == 8 and (12 - 8) / 2 == 2
TH = math.degrees(math.asin(0.6))  # rampa do exemplo, cerca de 37°

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
CLARA = E.mix(E.COR, "#FFFFFF", 0.35)


def rampa(c, t, t0, x, y, base, ang, u=0.55, w=170, h=120, rot=None, rotulo="θ", a_bloco=None):
    """rampa e bloco; devolve (R, centro do bloco)"""
    R = F.plano_inclinado(c, t, t0, x, y, base, ang, rotulo)
    a = ep(t, t0 + 0.4, 0.5) if a_bloco is None else a_bloco
    cxy = F.bloco_rampa(c, R, u, w, h, rot, a if t >= t0 + 0.4 else 0, TINTA2)
    return R, cxy


def eixos(c, t, t0, cxy, ang, L=330):
    """eixos girados tracejados: ao longo da rampa e perpendicular"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    for g in (ang, ang + 90):
        dx, dy = F._dir(g)
        M.line(c, cxy[0] - dx * L * q, cxy[1] - dy * L * q, cxy[0] + dx * L * q, cxy[1] + dy * L * q, TINTA2, 0.6, 4, dash=E.TRACO)


def componentes_peso(c, t, t1, t2, cxy, ang, L, rot1="P · sen θ", rot2="P · cos θ", lp1=None, lp2=None, size=46):
    """P·sen θ rampa abaixo (em t1) e P·cos θ contra a rampa (em t2), com projeções tracejadas"""
    s, co = math.sin(math.radians(ang)), math.cos(math.radians(ang))
    cx, cy = cxy
    B = (cx, cy + L)
    A1 = (cx - co * L * s, cy + s * L * s)       # componente ao longo, rampa abaixo
    A2 = (cx + s * L * co, cy + co * L * co)     # componente perpendicular, contra a rampa
    if t >= t1:
        M.line(c, *B, *A1, TINTA2, 0.5 * ep(t, t1, 0.4), 3, dash=E.TRACO)
        F.seta(c, cx, cy, *A1, CLARA, 1.0, 8, p=ease_out(prog(t, t1, 0.5)))
        E.foco(c, t, t1 + 0.3, 0.4, lambda a: sub(c, rot1, *(lp1 or (A1[0] - 30, A1[1] + 60)), size, "g", E.COR_TEXTO, a, "right"))
    if t >= t2:
        M.line(c, *B, *A2, TINTA2, 0.5 * ep(t, t2, 0.4), 3, dash=E.TRACO)
        F.seta(c, cx, cy, *A2, CLARA, 1.0, 8, p=ease_out(prog(t, t2, 0.5)))
        E.foco(c, t, t2 + 0.3, 0.4, lambda a: sub(c, rot2, *(lp2 or (A2[0] + 30, A2[1] + 50)), size, "g", E.COR_TEXTO, a))
    return A1, A2


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            u = 0.85 - 0.7 * min(1.0, 0.5 * 0.5 * max(0.0, t - C["s01.a"] - 0.6) ** 2 / 2.2)
            for i, (y, w, h, rot) in enumerate(((520, 170, 130, "pesada"), (960, 100, 75, "leve"))):
                R = F.plano_inclinado(c, t, C["s01.a"], 1050, y, 680, 30, None)
                if t >= C["s01.a"] + 0.4:
                    F.bloco_rampa(c, R, u, w, h, None, ep(t, C["s01.a"] + 0.4, 0.4), E.COR if i == 0 else CLARA)
                E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a, y=y, rot=rot: E.escreve(c, rot, 860, y - 20, 50, "i", TINTA2, a))
            E.frase(c, t, C["s01.a"], ps("rampa lisa, sem atrito", "i", 66), XE, 230, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("qual chega", "i", 76) + [("primeiro?", "g", 76, COR)], XE, 400, passo=0.12)
            E.frase(c, t, C["s01.c"], [("chegam", "g", 80, CERTO), ("juntas", "g", 80, CERTO)], XE, 600, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "dividir o peso", 0), ("s02.c", "a aceleração na rampa", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "decompor um vetor,", "com seno e cosseno"), ("s03.c", "atrito cinético,", "μ · N")))


# ---------------- decompor o peso ----------------
def b_decompor(c, t, C, b):
    ang = 30
    if t < C["s06"]:
        R, cxy = rampa(c, t, C["s04.a"], 760, 960, 1000, ang, 0.55, 190, 140)
        seta_f(c, t, C["s04.b"], cxy, -90, 280, "P", lpos=(cxy[0] - 60, cxy[1] + 270))
        E.frase(c, t, C["s04.a"], ps("rampa de ângulo", "i", 64) + [("θ", "g", 64, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("só anda ao longo da rampa", "i", 56, TINTA2), XE, 320, passo=0.1)
        eixos(c, t, C["s04.d"], cxy, ang)
        E.frase(c, t, C["s04.d"], [("gire", "g", 70, COR), ("os", "i", 70), ("eixos", "i", 70)], XE, 440, passo=0.12)
        componentes_peso(c, t, C["s05.b"], C["s05.c"], cxy, ang, 280, lp1=(cxy[0] - 250, cxy[1] + 220), lp2=(cxy[0] + 160, cxy[1] + 330))
        if t >= C["s05"]:
            E.frase(c, t, C["s05.a"], [("duas", "g", 66, COR), ("componentes", "i", 66)], XE, 560, passo=0.12)
            E.frase(c, t, C["s05.b"], [("rampa", "i", 54), ("abaixo:", "i", 54)], XE, 670, passo=0.1)
            sub_em(c, t, C["s05.b"] + 0.4, "P · sen θ", XE + 340, 670, 58, "g", COR)
            E.frase(c, t, C["s05.c"], [("aperta:", "i", 54)], XE, 760, passo=0.1)
            sub_em(c, t, C["s05.c"] + 0.4, "P · cos θ", XE + 340, 760, 58, "g", COR)
            if t >= C["s05.d"]:
                cx, cy = cxy
                s, co = math.sin(math.radians(ang)), math.cos(math.radians(ang))
                E.angulo(c, t, C["s05.d"], cxy, (cx, cy + 100), (cx + s * 100, cy + co * 100), "θ", r=110, size=50)
                E.frase(c, t, C["s05.d"] + 0.4, ps("entre P e a perpendicular:", "i", 48, TINTA2) + [("θ", "g", 48, COR)], XE, 880, passo=0.08)
        return
    # s06: rampa deitada
    E.frase(c, t, C["s06"], ps("um jeito de não trocar", "i", 70), XE, 220, passo=0.12)
    cx, yb = 1300, 700
    E.foco(c, t, C["s06.a"], 0.5, lambda a: F.bloco(c, cx, yb - 70, 200, 140, None, TINTA2, a))
    if t >= C["s06.a"]:
        F.chao(c, cx - 400, cx + 400, yb, ep(t, C["s06.a"], 0.4))
    E.frase(c, t, C["s06.a"], [("θ", "g", 72, COR), ("=", "g", 72), ("0:", "g", 72)] + ps("não desce", "i", 72), XE, 400, passo=0.12)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: sub(c, "sen 0° = 0", XE, 560, 90, "g", TINTA, a))
    E.frase(c, t, C["s06.c"], [("o", "i", 76), ("seno", "g", 76, COR), ("puxa", "i", 76), ("rampa", "i", 76), ("abaixo", "i", 76)], XE, 760, passo=0.12)


# ---------------- a normal ----------------
def b_normal(c, t, C, b):
    ang = 30
    R, cxy = rampa(c, t, C["s07"], 760, 960, 1000, ang, 0.55, 190, 140)
    seta_f(c, t, C["s07"] + 0.4, cxy, -90, 280, "P", lpos=(cxy[0] - 60, cxy[1] + 270))
    componentes_peso(c, t, 1e9, C["s07"] + 0.6, cxy, ang, 280, lp2=(cxy[0] + 160, cxy[1] + 330))
    nb = F.forca(c, t, C["s07.c"], cxy, R.normal, 280 * math.cos(math.radians(ang)), "N", None)
    E.frase(c, t, C["s07.a"], ps("na perpendicular,", "i", 62) + ps("não sai da rampa", "g", 58), XE, 220, passo=0.1)
    E.frase(c, t, C["s07.b"], ps("resultante zero nessa direção", "i", 56, TINTA2), XE, 320, passo=0.1)
    sub_em(c, t, C["s07.c"], "N = P · cos θ", XE, 470, 96, "g", COR)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: sub(c, "N < P", XE, 620, 96, "g", TINTA, a))
    E.frase(c, t, C["s07.d"] + 0.5, ps("na rampa", "i", 56, TINTA2), XE + 330, 610, passo=0.1)


# ---------------- sem atrito ----------------
def b_sematrito(c, t, C, b):
    ang = 30
    if t < C["s09"]:
        R, cxy = rampa(c, t, C["s08"], 980, 980, 860, ang, 0.55, 170, 120)
        componentes_peso(c, t, C["s08.a"], 1e9, cxy, ang, 250, lp1=(cxy[0] - 230, cxy[1] + 190))
        E.frase(c, t, C["s08.a"], ps("sem atrito: só", "i", 60) + [("P · sen θ", "g", 58, COR)] + ps("na rampa", "i", 60), XE, 210, passo=0.1)
        sub_em(c, t, C["s08.b"], "m · g · sen θ = m · a", XE, 380, 84, "g", TINTA)
        if t >= C["s08.c"]:
            w0 = sub(None, "m · g · sen θ = ", 0, 0, 84)
            wm = sub(None, "m", 0, 0, 84)
            risca_em(c, t, C["s08.c"], XE - 6, 395, XE + wm + 6, 330, 8)
            risca_em(c, t, C["s08.c"] + 0.2, XE + w0 - 6, 395, XE + w0 + wm + 6, 330, 8)
        sub_em(c, t, C["s08.d"], "a = g · sen θ", XE, 560, 130, "g", COR)
        return
    R, cxy = rampa(c, t, C["s09"], 980, 980, 860, ang, 0.55, 170, 120)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: sub(c, "θ = 30°: sen 30° = 0,5", XE, 230, 72, "g", TINTA, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: sub(c, "a = 10 · 0,5", XE, 370, 84, "g", TINTA, a))
    bola_txt(c, t, C["s09.b"] + 0.6, "5 m/s^2", 400, 600, 140, 60)
    E.frase(c, t, C["s09.c"], ps("pesada ou leve:", "i", 60) + ps("a mesma", "g", 60, CERTO), XE, 860, passo=0.1)


# ---------------- com atrito ----------------
def b_comatrito(c, t, C, b):
    R, cxy = rampa(c, t, C["s10"], 1080, 980, 760, TH, 0.55, 170, 120, "10 kg" if t < C["s11"] else None)
    base = F.bloco_rampa(c, R, 0.55, 170, 120, None, 0)
    nx, ny = F._dir(R.normal + 180)
    pc = (base[0] + nx * 60, base[1] + ny * 60)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("com atrito:", "i", 64) + ps("rampa acima", "g", 62, COR), XE, 220, passo=0.1)
        seta_f(c, t, C["s10.a"] + 0.5, pc, R.sobe, 170, "F_{at}", lpos=(pc[0] + 120, pc[1] - 170), size=48)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: F.medida(c, 10, "kg", XE, 380, 76, COR, a))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: sub(c, "sen θ = 0,6   cos θ = 0,8", XE, 500, 64, "g", TINTA, a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: sub(c, "μ_{c} = 0,25", XE, 620, 64, "g", TINTA, a))
        return
    contas(c, t, [(C["s11.a"], "P = 10 · 10 = 100 N"), (C["s11.b"], "P · sen θ = 100 · 0,6 = 60 N"), (C["s11.c"], "N = 100 · 0,8 = 80 N"),
                  (C["s11.d"], "F_{at} = 0,25 · 80 = 20 N"), (C["s11.e"], "F_{R} = 60 − 20 = 40 N"), (C["s11.f"], "a = 40 ÷ 10")], XE, 200, 60, 96)
    bola_txt(c, t, C["s11.f"] + 0.8, "4 m/s^2", 1500, 250, 120, 52)
    componentes_peso(c, t, C["s11.b"], 1e9, cxy, TH, 200, "60 N", lp1=(cxy[0] - 190, cxy[1] + 160))
    nb = F._dir(R.normal)
    seta_f(c, t, C["s11.c"], cxy, R.normal, 160, "N", modulo="80 N", lpos=(cxy[0] + nb[0] * 160 - 120, cxy[1] + nb[1] * 160 - 20), size=44)
    seta_f(c, t, C["s11.d"], pc, R.sobe, 60, None, modulo="20 N", lpos=(pc[0] + 110, pc[1] - 40), size=46)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("na rampa,", "i", 64) + [("N", "g", 64, ERRADO), ("=", "g", 64, ERRADO), ("P?", "g", 64, ERRADO)], XE, 330, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: sub(c, "F_{at} = 0,25 · 100 = 25 N", XE, 490, 70, "g", ERRADO, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: sub(c, "a = (60 − 25) ÷ 10 = 3,5", XE, 600, 70, "g", ERRADO, a))
    risca_em(c, t, C["s12.d"], XE - 10, 615, XE + 900, 450)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: sub(c, "N = P · cos θ = 80 N", XE, 800, 84, "g", CERTO, a))
    R, cxy = rampa(c, t, C["s12"], 1250, 980, 560, TH, 0.5, 140, 100)
    F.forca(c, t, C["s12.e"] + 0.3, cxy, R.normal, 150, "N", CERTO, size=46)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("sem atrito:", "i", 62, CLARO), 300, 360)
        sub_em(c, t, C["s13.a"] + 0.4, "a = g · sen θ", 760, 360, 100, "g", BR)
        E.frase(c, t, C["s13.b"], ps("com atrito, descendo:", "i", 62, CLARO), 300, 560)
        sub_em(c, t, C["s13.b"] + 0.6, "a = g · (sen θ − μ · cos θ)", W / 2, 700, 100, "g", BR, "center")
        sub_em(c, t, C["s13.c"], "10 · (0,6 − 0,2) = 4", W / 2, 880, 84, "g", CLARO, "center")
        E.frase(c, t, C["s13.c"] + 1.6, ps("sem calcular força nenhuma", "i", 54, CLARO), W / 2, 990, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("funciona porque", "i", 64, CLARO), W / 2, 250, "center", 0.1)
    E.frase(c, t, C["s14.a"] + 0.6, ps("toda força da rampa tem a massa:", "i", 62, CLARO) + ps("a massa corta", "g", 62, BR), W / 2, 380, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("alguém empurra ou puxa", "i", 64, CLARO), W / 2, 600, "center", 0.12)
    E.frase(c, t, C["s14.c"], ps("some as forças", "g", 70, BR), W / 2, 780, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s15")
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (E.escreve(c, "bloco de", XE, 330, 64, "i", TINTA, a), F.medida(c, 2, "kg", XE + 270, 330, 76, COR, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: sub(c, "sen θ = 0,6   cos θ = 0,8", XE, 460, 64, "g", TINTA, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: sub(c, "μ_{c} = 0,5", XE, 580, 64, "g", TINTA, a))
    E.frase(c, t, C["s15.d"], [("a", "g", 72, F.ACEL), ("=", "g", 72), ("?", "g", 72, COR)], XE, 760, passo=0.12)
    E.frase(c, t, C["s15.e"], [("N", "g", 72), ("=", "g", 72), ("?", "g", 72, COR)], XE + 300, 760, passo=0.12)

    def desenho():
        rampa(c, t, C["s15.a"], 1150, 900, 640, TH, 0.55, 140, 100, "2 kg")
    pausa(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s18"]:
        E.frase(c, t, C["s17"], ps("pelo atalho", "i", 70, COR), XE, 200)
        contas(c, t, [(C["s17.a"], "a = 10 · (0,6 − 0,5 · 0,8)"), (C["s17.b"], "0,5 · 0,8 = 0,4"), (C["s17.c"], "0,6 − 0,4 = 0,2")], XE, 360, 76, 130)
        bola_txt(c, t, C["s17.d"], "2 m/s^2", 1500, 520, 150, 64)
        return
    E.foco(c, t, C["s18.a"], 0.5, lambda a: sub(c, "N = P · cos θ = 20 · 0,8", XE, 250, 76, "g", TINTA, a))
    bola_txt(c, t, C["s18.c"], "16 N", 1500, 330, 120, 60)
    E.frase(c, t, C["s18.d"], ps("confira pelas forças:", "i", 60, TINTA2), XE, 470, passo=0.1)
    contas(c, t, [(C["s18.d"] + 0.6, "20 · 0,6 = 12 N  (rampa abaixo)"), (C["s18.d"] + 1.4, "0,5 · 16 = 8 N  (atrito)"),
                  (C["s18.e"], "F_{R} = 12 − 8 = 4 → a = 4 ÷ 2 = 2", CERTO)], XE, 600, 64, 110)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s19", (("s19.a", [("seno", "g", 62, COR), ("puxa,", "i", 66), ("cosseno", "g", 62, COR), ("aperta", "i", 66)]),
                            ("s19.b", [("N", "g", 62, COR), ("=", "g", 62), ("P · cos θ", "g", 62)]),
                            ("s19.c", [("sem", "i", 66), ("atrito:", "i", 66), ("a", "g", 62, COR), ("=", "g", 62), ("g · sen θ", "g", 62)])), C["s20"])
    if t < C["s20"]:
        return

    def desenho():
        E.foco(c, t, C["s20.a"], 0.5, lambda a: (M.rrect(c, 300, 780, 560, 26, 6, "#8B5E3C", a), F.bloco(c, 520, 720, 150, 110, None, TINTA2, a),
                                                 polia(c, 880, 790, 34, a, (860, 780)), M.line(c, 595, 720, 880, 756, TINTA2, a, 5),
                                                 M.line(c, 914, 790, 914, 900, TINTA2, a, 5), F.bloco(c, 914, 950, 110, 100, None, E.COR, a)))
    proxima(c, t, C, "s20", ((C["s20.a"], [("Blocos", "g", 100, COR), ("ligados", "g", 100)]), (C["s20.b"], [("e", "i", 80), ("polias", "g", 80, COR)])),
            "s20.d", "s20.e", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, decompor=b_decompor, normal=b_normal, sematrito=b_sematrito, comatrito=b_comatrito,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
