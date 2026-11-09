"""Visual — Estudativo · FIS-DIN-003: terceira lei de Newton, ação e reação.
Linguagem visual da trilha de Dinâmica: cabeçalho do visual.py da FIS-DIN-001. Nesta aula, o par de ação e reação são duas
setas laranja de mesmo tamanho, cada uma saindo do corpo onde age e com uma pílula dizendo "em <corpo>". Todo instante vem de C[...]."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-003_terceira_lei_acao_e_reacao.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("lei", "par", "anula", "erro", "atalho", "questao", "fim"))
# aula conceitual: nenhuma conta

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
MARROM = "#8B5E3C"


def cavalo(c, x, y, s, a=1.0):
    """cavalo de lado, olhando para a direita; cascos em y, x = meio do corpo"""
    if a <= 0:
        return
    cor = "#7A4A2A"
    corpo = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s * 1.1, y - s * 1.75, s * 2.2, s * 0.85), s * 0.4, s * 0.4)
    c.drawRRect(corpo, M.paint(cor, a))
    pesc = skia.Path()
    pesc.moveTo(x + s * 0.7, y - s * 1.65); pesc.lineTo(x + s * 1.25, y - s * 2.6); pesc.lineTo(x + s * 1.6, y - s * 2.45); pesc.lineTo(x + s * 1.1, y - s * 1.3); pesc.close()
    c.drawPath(pesc, M.paint(cor, a))
    cab = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + s * 1.2, y - s * 2.75, s * 0.95, s * 0.42), s * 0.2, s * 0.2)
    c.save(); c.rotate(18, x + s * 1.2, y - s * 2.55); c.drawRRect(cab, M.paint(cor, a)); c.restore()
    for dx in (-0.85, -0.55, 0.55, 0.85):
        M.line(c, x + dx * s, y - s * 1.0, x + dx * s, y - s * 0.05, cor, a, s * 0.2)
        M.rrect(c, x + dx * s - s * 0.13, y - s * 0.12, s * 0.26, s * 0.12, 3, "#2A1A10", a)
    M.line(c, x - s * 1.05, y - s * 1.6, x - s * 1.45, y - s * 0.9, "#3A2414", a, s * 0.16)


def carroca(c, x, y, s, a=1.0):
    """carroça de lado: caixa e uma roda; rodas em y, x = meio"""
    if a <= 0:
        return
    M.rrect(c, x - s * 1.2, y - s * 1.75, s * 2.4, s * 0.85, 8, MARROM, a)
    for k in range(1, 4):
        M.line(c, x - s * 1.2 + s * 0.6 * k, y - s * 1.75, x - s * 1.2 + s * 0.6 * k, y - s * 0.9, "#6E4A2F", a, 4)
    c.drawCircle(x, y - s * 0.55, s * 0.55, M.paint(TINTA2, a, stroke=s * 0.1))
    c.drawCircle(x, y - s * 0.55, s * 0.1, M.paint(TINTA2, a))
    M.line(c, x + s * 1.2, y - s * 1.2, x + s * 1.9, y - s * 1.3, TINTA2, a, 6)


def foguete(c, x, y, s, a=1.0, gases=True):
    """foguete de pé; base em y"""
    if a <= 0:
        return
    M.rrect(c, x - s * 0.35, y - s * 2.2, s * 0.7, s * 1.9, s * 0.2, "#E9E9E4", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s * 0.35, y - s * 2.2, s * 0.7, s * 1.9), s * 0.2, s * 0.2), M.paint(TINTA2, a, stroke=4))
    p = skia.Path(); p.moveTo(x - s * 0.35, y - s * 2.15); p.lineTo(x, y - s * 2.9); p.lineTo(x + s * 0.35, y - s * 2.15); p.close()
    c.drawPath(p, M.paint(E.COR, a))
    for d in (-1, 1):
        f = skia.Path(); f.moveTo(x + d * s * 0.35, y - s * 0.9); f.lineTo(x + d * s * 0.75, y - s * 0.2); f.lineTo(x + d * s * 0.35, y - s * 0.35); f.close()
        c.drawPath(f, M.paint(E.COR, a))
    c.drawCircle(x, y - s * 1.55, s * 0.17, M.paint("#7FC8E8", a))
    if gases:
        for i, (dx, dy, r) in enumerate(((0, 0.2, 0.3), (-0.25, 0.5, 0.24), (0.25, 0.5, 0.24), (0, 0.75, 0.22))):
            c.drawCircle(x + dx * s, y + dy * s, r * s, M.paint("#FFC400" if i == 0 else "#C9C9C4", 0.85 * a))


def prego(c, x, y, s, a=1.0):
    if a <= 0:
        return
    M.line(c, x - s, y, x + s * 0.8, y, "#8A8A90", a, s * 0.14)
    M.line(c, x - s, y - s * 0.3, x - s, y + s * 0.3, "#6A6A70", a, s * 0.14)
    p = skia.Path(); p.moveTo(x + s * 0.8, y - s * 0.07); p.lineTo(x + s * 1.05, y); p.lineTo(x + s * 0.8, y + s * 0.07); p.close()
    c.drawPath(p, M.paint("#8A8A90", a))


def mesa(c, x, y, w, a=1.0):
    """mesa de lado: tampo em y"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, 30, 8, MARROM, a)
    for lx in (x + 30, x + w - 60):
        M.rrect(c, lx, y + 26, 30, 200, 6, "#6E4A2F", a)


def livro(c, cx, yb, w, h, a=1.0):
    """livro deitado com a base em yb"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, yb - h, w, h, 6, "#2F5DA8", a)
    M.rrect(c, cx - w / 2 + 8, yb - h + 8, w - 16, h * 0.22, 3, "#F3F3F0", a)


def caminhao(c, x, y, w, a=1.0, sentido=1):
    """caminhão de lado: rodas em y, frente para o lado de sentido"""
    if a <= 0:
        return
    sg = 1 if sentido > 0 else -1
    r = w * 0.08
    base = y - r * 1.2
    bx = x - sg * w * 0.12
    M.rrect(c, bx - w * 0.36, base - w * 0.42, w * 0.72, w * 0.42, 8, "#2F5DA8", a)
    cx_ = x + sg * w * 0.36
    M.rrect(c, cx_ - w * 0.14, base - w * 0.3, w * 0.28, w * 0.3, 10, "#1F4280", a)
    M.rrect(c, cx_ - w * 0.08 + sg * w * 0.02, base - w * 0.26, w * 0.12, w * 0.1, 4, "#BFE3F2", a)
    for wx in (x - sg * w * 0.34, x - sg * w * 0.05, x + sg * w * 0.36):
        c.drawCircle(wx, y - r, r, M.paint("#1B1B20", a))
        c.drawCircle(wx, y - r, r * 0.45, M.paint("#9A9AA2", a))


def em(c, t, t0, s, cx, cy, cor=None):
    """pílula 'em <corpo>' que diz onde a força age"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, 38, "b", fundo=cor or TINTA, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            y = 760
            E.foco(c, t, C["s01.a"], 0.5, lambda a: (carroca(c, 760, y, 130, a), cavalo(c, 1300, y, 150, a)))
            if t >= C["s01.a"]:
                F.chao(c, 500, 1700, y, ep(t, C["s01.a"], 0.4))
            seta_f(c, t, C["s01.a"] + 0.6, (920, 480), 0, 200, None)
            em(c, t, C["s01.a"] + 0.9, "cavalo puxa carroça", 900, 400, E.COR)
            seta_f(c, t, C["s01.b"] + 0.3, (1140, 560), 180, 200, None)
            em(c, t, C["s01.b"] + 0.6, "carroça puxa cavalo", 1260, 640, E.COR)
            E.frase(c, t, C["s01.b"] + 1.4, ps("mesma força", "g", 56, TINTA2), 1640, 300, "center", 0.1)
            E.frase(c, t, C["s01.a"], ps("terceira lei", "i", 80), XE, 230, passo=0.12)
            E.frase(c, t, C["s01.c"], [("como", "i", 84), ("saem", "g", 84, COR), ("do", "i", 84), ("lugar?", "i", 84)], XE, 980, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "achar o par", 0), ("s02.c", "por que não se anulam", 0)))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "força é vetor,", "módulo, direção, sentido"), ("s03.c", "o que decide o movimento,", "a resultante no corpo")))


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("força", "g", 80, COR), ("=", "g", 80, TINTA2)] + ps("troca entre dois corpos", "i", 80), XE, 210, passo=0.12)
        y = 640
        E.foco(c, t, C["s04.b"] - 0.3, 0.5, lambda a: (pessoa(c, 800, y + 220, 75, a, inclina=15, braco=0), mesa(c, 1050, y - 20, 520, a)))
        seta_f(c, t, C["s04.b"], (1050, y - 90), 0, 200, None)
        em(c, t, C["s04.b"] + 0.3, "na mesa", 1160, y - 170, E.COR)
        seta_f(c, t, C["s04.c"], (1000, y + 40), 180, 200, None)
        em(c, t, C["s04.c"] + 0.3, "na mão", 880, y + 120, E.COR)
        for i, (k, s) in enumerate((("s04.d", "mesmo módulo"), ("s04.e", "mesma direção"), ("s04.f", "sentidos opostos"))):
            E.foco(c, t, C[k], 0.4, lambda a, i=i, s=s: (E.bola(c, XE + 24, 360 + i * 100 - 18, 24, a=a), E.escreve(c, s, XE + 70, 360 + i * 100, 54, "g", TINTA, a)))
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("de patins,", "i", 76) + ps("empurre a parede", "g", 72), XE, 220, passo=0.12)
        dx = -260 * ease_out(prog(t, C["s05.c"], 1.2))
        E.foco(c, t, C["s05.a"], 0.5, lambda a: (F.parede(c, 1500, 380, 900, 1, a), pessoa(c, 1330 + dx, 860, 80, a, inclina=10 * (1 + dx / 260), braco=0)))
        if t >= C["s05.a"]:
            F.chao(c, 600, 1500, 900, ep(t, C["s05.a"], 0.4))
            for wx in (-30, 30):
                c.drawCircle(1330 + dx + wx, 885, 14, M.paint(TINTA2, ep(t, C["s05.a"], 0.4)))
        if t < C["s05.c"] + 0.2:
            seta_f(c, t, C["s05.a"] + 0.8, (1300, 560), 0, 190, None)
            em(c, t, C["s05.a"] + 1.0, "na parede", 1330, 480, E.COR)
        seta_f(c, t, C["s05.b"], (1300 + dx, 640), 180, 190, None)
        em(c, t, C["s05.b"] + 0.3, "em você", 1160 + dx, 720, E.COR)
        E.frase(c, t, C["s05.c"], ps("a parede", "i", 70) + [("joga", "g", 70, COR), ("você", "i", 70)], XE, 360, passo=0.12)
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("quem empurra quem?", "i", 72), XE, 200, passo=0.12)
        # andar
        y = 820
        E.foco(c, t, C["s06.a"], 0.5, lambda a: pessoa(c, 560, y, 85, a, inclina=8, braco=-80))
        if t >= C["s06.a"]:
            F.chao(c, 230, 900, y, ep(t, C["s06.a"], 0.4))
        seta_f(c, t, C["s06.a"] + 0.4, (560, y + 25), 180, 200, None)
        em(c, t, C["s06.a"] + 0.6, "no chão", 380, y + 110, E.COR)
        seta_f(c, t, C["s06.b"], (620, 600), 0, 200, None)
        em(c, t, C["s06.b"] + 0.3, "em você", 760, 520, E.COR)
        # foguete
        E.foco(c, t, C["s06.c"], 0.5, lambda a: foguete(c, 1450, 780, 110, a))
        seta_f(c, t, C["s06.c"] + 0.4, (1600, 820), -90, 150, None)
        em(c, t, C["s06.c"] + 0.6, "nos gases", 1720, 900, E.COR)
        seta_f(c, t, C["s06.d"], (1600, 560), 90, 150, None)
        em(c, t, C["s06.d"] + 0.3, "no foguete", 1720, 390, E.COR)
        return
    E.frase(c, t, C["s07"], ps("e não precisa", "i", 76) + [("encostar", "g", 76, COR)], XE, 220, passo=0.12)
    dx = 330 * ease_io(prog(t, C["s07.d"], 1.0))
    E.foco(c, t, C["s07.a"], 0.5, lambda a: prego(c, 1300, 600, 110, a))
    F.ima(c, t, C["s07.a"], 700 + dx, 600, 300, 100)
    if t < C["s07.d"]:
        seta_f(c, t, C["s07.a"] + 0.6, (1180, 680), 180, 170, None)
        em(c, t, C["s07.a"] + 0.8, "no prego", 1240, 770, E.COR)
        seta_f(c, t, C["s07.b"], (860, 520), 0, 170, None)
        em(c, t, C["s07.b"] + 0.3, "no ímã", 900, 430, E.COR)
    E.frase(c, t, C["s07.c"], ps("segure o prego, solte o ímã", "i", 60, TINTA2), XE, 900, passo=0.1)
    E.frase(c, t, C["s07.d"], [("o", "i", 66), ("ímã", "g", 66, COR), ("anda", "i", 66)], XE, 1000, passo=0.12)


# ---------------- achar o par ----------------
def b_par(c, t, C, b):
    E.frase(c, t, C["s08"], ps("como achar o par?", "i", 76), XE, 200, passo=0.12)
    E.frase(c, t, C["s08.a"], [("troque", "g", 96, COR), ("os", "i", 100), ("nomes", "i", 100)], XE, 340, passo=0.12)
    y1, y2 = 530, 690
    E.frase(c, t, C["s08.b"], [("pé", "g", 90, F.VEL), ("empurra", "i", 90), ("chão", "g", 90, E.COR)], XE, y1, passo=0.12)
    if t >= C["s08.c"]:
        q = ease_io(prog(t, C["s08.c"], 0.9))
        wp, we, wc = E.larg("pé", "g", 90), E.larg("empurra", "i", 90), E.larg("chão", "g", 90)
        gap = 24
        xa, xb = XE, XE + wp + gap + we + gap   # posições de "pé" e "chão" na primeira frase
        xc2 = XE + wc + gap + we + gap           # onde "pé" termina na segunda frase
        a = ep(t, C["s08.c"], 0.3)
        E.escreve(c, "chão", lerp(xb, XE, q), lerp(y1, y2, q) - 60 * math.sin(q * math.pi), 90, "g", E.COR, a)
        E.escreve(c, "empurra", lerp(XE + wp + gap, XE + wc + gap, q), lerp(y1, y2, q), 90, "i", TINTA, a)
        E.escreve(c, "pé", lerp(xa, xc2, q), lerp(y1, y2, q) + 60 * math.sin(q * math.pi), 90, "g", F.VEL, a)
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "nascem e somem juntas", 1420, 560, 46, "b", fundo=TINTA, a=a))
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.pilula(c, "cada uma num corpo diferente", 1240, 880, 54, "g", fundo=E.COR, a=a))


# ---------------- não se anulam ----------------
def b_anula(c, t, C, b):
    y = 860
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("nunca", "g", 84, ERRADO), ("se", "i", 88), ("anulam", "i", 88)], XE, 210, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("só se somam forças", "i", 64) + [("no", "g", 62), ("mesmo", "g", 62, COR), ("corpo", "g", 62)], XE, 330, passo=0.1)
        E.foco(c, t, C["s09"], 0.5, lambda a: (carroca(c, 640, y, 120, a), cavalo(c, 1300, y, 140, a)))
        if t >= C["s09"]:
            F.chao(c, 300, 1750, y, ep(t, C["s09"], 0.4))
        for k, (x0, w, nome) in enumerate(((420, 470, "carroça"), (1050, 560, "cavalo"))):
            ti = C["s09.c"] if k == 0 else C["s09.d"]
            p = ep(t, ti, 0.5)
            E.caixa_pontilhada(c, x0, 440, w, 460, p, prog_=p)
        seta_f(c, t, C["s09.c"] + 0.3, (800, 610), 0, 180, None)
        em(c, t, C["s09.c"] + 0.5, "na carroça", 655, 490, E.COR)
        seta_f(c, t, C["s09.d"] + 0.3, (1160, 690), 180, 180, None)
        em(c, t, C["s09.d"] + 0.5, "no cavalo", 1330, 490, E.COR)
        return
    E.frase(c, t, C["s10.a"], ps("olhe só as forças", "i", 72) + [("no", "g", 70), ("cavalo", "g", 70, COR)], XE, 210, passo=0.12)
    E.foco(c, t, C["s10"], 0.5, lambda a: cavalo(c, 1100, y, 150, a))
    if t >= C["s10"]:
        F.chao(c, 600, 1650, y, ep(t, C["s10"], 0.4))
    seta_f(c, t, C["s10.b"], (900, 620), 180, 200, None, modulo=None)
    em(c, t, C["s10.b"] + 0.3, "carroça puxa", 760, 540, E.COR)
    seta_f(c, t, C["s10.c"], (1000, y - 20), 0, 300, None)
    em(c, t, C["s10.c"] + 0.3, "chão empurra", 1200, y + 70, E.COR)
    E.frase(c, t, C["s10.d"], [("chão", "g", 64), (">", "g", 64, COR), ("carroça", "g", 64)] + [("→", "g", 66, TINTA2), ("anda", "i", 66)], XE, 360, passo=0.12)
    if t >= C["s10.d"] + 0.6:
        F.seta(c, 950, 1000, 1050, 1000, TINTA, 1.0, 13, p=ease_out(prog(t, C["s10.d"] + 0.6, 0.5)))
        E.foco(c, t, C["s10.d"] + 0.9, 0.4, lambda a: rot_vetor(c, "F_{R}", 1120, 1022, 56, TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    cx, yb = 1500, 640
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (mesa(c, cx - 300, yb, 600, a), livro(c, cx, yb, 260, 70, a)))
    seta_f(c, t, C["s11.b"], (cx - 60, yb - 35), -90, 190, None)
    em(c, t, C["s11.b"] + 0.3, "Terra puxa livro", cx + 150, yb + 300, E.COR)
    seta_f(c, t, C["s11.c"], (cx + 60, yb - 70), 90, 190, None)
    em(c, t, C["s11.c"] + 0.3, "mesa empurra livro", cx + 120, yb - 300, E.COR)
    if t < C["s12"]:
        E.frase(c, t, C["s11.d"], ps("é um par de", "i", 72) + [("ação", "g", 70), ("e", "i", 72), ("reação?", "g", 70, COR)], XE, 380, passo=0.12)
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.selo(c, XE + 60, 360, 60, False, a))
    E.frase(c, t, C["s12.a"], [("não", "g", 90, ERRADO)], XE + 150, 390)
    E.frase(c, t, C["s12.b"], ps("as duas estão", "i", 60) + ps("no livro", "g", 58, COR), XE, 500, passo=0.1)
    pares = (("s12.c", "Terra puxa livro", "s12.d", "livro puxa Terra"), ("s12.e", "mesa empurra livro", "s12.f", "livro empurra mesa"))
    for i, (k1, s1, k2, s2) in enumerate(pares):
        y = 640 + i * 110
        E.frase(c, t, C[k1], [(s1, "b", 50)], XE, y)
        E.foco(c, t, C[k2] - 0.2, 0.4, lambda a, y=y: E.escreve(c, "↔", XE + 470, y, 54, "g", TINTA2, a))
        E.frase(c, t, C[k2], [(s2, "b", 50, COR)], XE + 540, y)
    E.foco(c, t, C["s12.g"], 0.5, lambda a: E.pilula(c, "iguais porque o livro está parado: resultante zero", 760, 990, 46, "b", fundo=CERTO, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("escreva:", "i", 66, CLARO) + [("quem", "g", 66, BR), ("faz", "g", 66, BR), ("em", "g", 66, BR), ("quem", "g", 66, BR)], W / 2, 310, "center", 0.12)
        E.frase(c, t, C["s13.a"] + 1.4, [("A", "g", 110, CLARO), ("empurra", "i", 110, BR), ("B", "g", 110, BR)], W / 2, 500, "center", 0.12)
        E.frase(c, t, C["s13.b"], [("B", "g", 110, BR), ("empurra", "i", 110, BR), ("A", "g", 110, CLARO)], W / 2, 680, "center", 0.12)
        E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: E.pilula(c, "o par", 1500, 640, 46, "b", fundo=E.COR, a=a))
        E.frase(c, t, C["s13.c"], [("mesmo", "g", 62, ERRADO), ("corpo?", "g", 62, ERRADO)] + ps("não é par", "i", 66, CLARO), W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("a terceira lei: dois corpos trocando força", "i", 62, CLARO), W / 2, 280, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO)] + ps("diz se alguém se move", "i", 66, CLARO), W / 2, 480, "center", 0.12)
    E.frase(c, t, C["s14.c"], ps("some só as forças", "g", 72, BR) + ps("no corpo que interessa", "i", 72, CLARO), W / 2, 720, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s15")
    E.frase(c, t, C["s15.a"], ps("caminhão e carro", "i", 72) + [("batem", "g", 70, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s15.b"], ps("força do caminhão no carro", "i", 60), XE, 490, passo=0.1)
    E.frase(c, t, C["s15.b"] + 1.4, [("maior,", "g", 64), ("menor", "g", 64), ("ou", "i", 66), ("igual", "g", 64, COR)], XE, 590, passo=0.12)
    E.frase(c, t, C["s15.b"] + 2.4, ps("à do carro no caminhão?", "i", 60), XE, 690, passo=0.1)

    def desenho():
        E.foco(c, t, C["s15.a"], 0.5, lambda a: (caminhao(c, 1260, 900, 420, a), F.carrinho(c, 1690, 900, 250, a=a, sentido=-1)))
        if t >= C["s15.a"]:
            F.chao(c, 1000, 1850, 900, ep(t, C["s15.a"], 0.4))
        E.foco(c, t, C["s15.b"] + 0.8, 0.4, lambda a: centro(c, "?", 1530, 720, 120, "g", COR, a))
    pausa(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("troque os nomes", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], ps("caminhão empurra carro", "b", 56), XE, 320, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("carro empurra caminhão", "b", 56, COR), XE, 410, passo=0.1)
    y = 760
    E.foco(c, t, C["s17"], 0.5, lambda a: (caminhao(c, 1100, y, 420, a), F.carrinho(c, 1480, y, 250, a=a, sentido=-1)))
    F.chao(c, 820, 1700, y, ep(t, C["s17"], 0.4)) if t >= C["s17"] else None
    seta_f(c, t, C["s17.a"] + 0.3, (1360, 560), 0, 200, None)
    em(c, t, C["s17.a"] + 0.5, "no carro", 1460, 480, E.COR)
    seta_f(c, t, C["s17.b"] + 0.3, (1340, 640), 180, 200, None)
    em(c, t, C["s17.b"] + 0.5, "no caminhão", 1150, 830, E.COR)
    E.frase(c, t, C["s17.c"], [("iguais", "g", 100, CERTO)], XE, 600)
    E.foco(c, t, C["s17.c"] + 0.4, 0.4, lambda a: E.selo(c, XE + 470, 570, 50, True, a))
    E.frase(c, t, C["s17.d"], ps("estrago maior no carro:", "i", 56), XE, 900, passo=0.1)
    E.foco(c, t, C["s17.e"], 0.5, lambda a: E.pilula(c, "a massa, assunto da segunda lei", 640, 990, 44, "b", fundo=TINTA2, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s18", (("s18.a", [("toda", "i", 66), ("força", "i", 66), ("tem", "i", 66), ("um", "i", 66), ("par", "g", 62, COR)]),
                            ("s18.b", [("mesmo", "g", 62), ("módulo", "i", 66), ("e", "i", 66), ("direção;", "i", 66), ("sentido", "g", 62), ("oposto", "g", 62, COR)]),
                            ("s18.c", [("em", "i", 66), ("outro", "g", 62, COR), ("corpo", "g", 62)]),
                            ("s18.d", [("nunca", "g", 62, ERRADO), ("se", "i", 66), ("anulam", "i", 66)])), C["s19"])
    if t < C["s19"]:
        return

    def desenho():
        cx, yb = 650, 860
        E.foco(c, t, C["s19.a"], 0.5, lambda a: (mesa(c, cx - 250, yb, 500, a), livro(c, cx, yb, 220, 60, a)))
        seta_f(c, t, C["s19.a"] + 0.4, (cx - 50, yb - 30), -90, 150, "P", lpos=(cx - 110, yb + 150))
        seta_f(c, t, C["s19.a"] + 0.8, (cx + 50, yb - 60), 90, 150, "N", lpos=(cx + 110, yb - 160))
    proxima(c, t, C, "s19", ((C["s19"] + 0.8, [("Peso", "g", 110, COR), ("e", "i", 110), ("normal", "g", 110, COR)]),
                             (C["s19.b"], [("a", "i", 70), ("balança", "g", 66), ("no", "i", 70), ("elevador", "g", 66)])), "s19.c", "s19.d", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, par=b_par, anula=b_anula, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
