"""Visual — Estudativo · FIS-DIN-001: força resultante e primeira lei (inércia). Primeira aula da trilha de Dinâmica.

LINGUAGEM VISUAL DA DINÂMICA (as aulas FIS-DIN-* copiam daqui; a base da Física está no visual.py da FIS-CIN-001):
- FORÇA = seta laranja (COR) que SAI do ponto onde a força age, com a letra-vetor (setinha em cima) e o módulo com unidade
  ao lado ("F  200 N"). Letras fixas: P peso, N normal, T tração, F_{at} atrito, F_{el} força elástica, F força aplicada,
  F_{cp} centrípeta. Subscrito sempre com sub()/rot_vetor() (peças da trilha, abaixo).
- RESULTANTE F_{R} = seta em TINTA, mais grossa, desenhada fora do corpo (embaixo ou ao lado), nunca misturada às forças.
  Resultante zero = pílula "F_R = 0" e as setas iguais lado a lado.
- ACELERAÇÃO = seta violeta (F.ACEL) fina, fora do corpo; VELOCIDADE = seta petróleo (F.VEL), como na Cinemática.
- CORPO no diagrama de forças = bloco cinza (F.corpo_livre / F.bloco com TINTA2), para as forças laranja aparecerem;
  objeto do dia a dia (carro, ônibus, caixa da história) em laranja ou nas cores dele. Chão, fio, polia e suporte em tinta.
- CONTA: uma linha por fala (contas()), resultado final na esfera laranja (bola_txt) com a unidade menor. O que sai da conta
  (força que corta, ação e reação em corpos diferentes) é mostrado pela posição, não por cor nova.
- FÓRMULA NOVA: formula_nova() — fórmula grande em tinta e, embaixo, letra laranja + nome + (unidade do SI).
- Certo = verde com selo; errado = vermelho com risco. Atalho no palco escuro (E.palco) com CLARO e branco. Questão com o
  relógio (pausa()). Texto à esquerda (XE), desenho à direita; texto de apoio com 44 px ou mais.
- Peças da trilha (copiadas em cada aula, entre as marcas "peças da trilha"): sub, sub_em, contas, bola_txt, troca, pilula_em,
  rot_vetor, seta_f, lembrete, promessa, pausa, cabeca_q, resumo, proxima, formula_nova, pessoa, polia, balanca_chao, elevador.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
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
ARQUIVO_FINAL = "estudativo_FIS-DIN-001_forca_resultante_primeira_lei_inercia.mp4"
CORTINAS = E.carregar_cortinas(__file__, ("forca", "resultante", "inercia", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
assert 200 + 150 == 350 and 300 - 200 == 100 and 300 - 300 == 0
assert 250 + 200 == 450 and 450 - 300 == 150
assert 1 * 10 == 10  # saco de 1 kg: uns 10 N (P = m·g fica para FIS-DIN-004)

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
def onibus(c, x, y, w, a=1.0, dentro=None):
    """ônibus de lado, rodas em y, centro em x; dentro(piso) desenha o passageiro antes da lataria de baixo"""
    if a <= 0:
        return
    r = w * 0.07
    base = y - r * 1.2
    h = w * 0.36
    topo = base - h
    M.rrect(c, x - w / 2, topo, w, h, w * 0.05, mix_(E.COR, BR, 0.82), a)
    piso = base - h * 0.08
    if dentro:
        dentro(piso)
    M.rrect(c, x - w / 2, base - h * 0.42, w, h * 0.42, w * 0.03, E.COR, a)
    M.rrect(c, x - w / 2, topo, w, h * 0.14, w * 0.04, E.COR, a)
    for k in range(5):
        M.line(c, x - w / 2 + w * (0.08 + 0.2 * k), topo + h * 0.14, x - w / 2 + w * (0.08 + 0.2 * k), base - h * 0.42, E.COR, a, 6)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, topo, w, h), w * 0.05, w * 0.05), M.paint(TINTA, a, stroke=4))
    for wx in (x - w * 0.32, x + w * 0.32):
        c.drawCircle(wx, y - r, r, M.paint("#1B1B20", a))
        c.drawCircle(wx, y - r, r * 0.45, M.paint("#9A9AA2", a))


def mix_(a, b, k):
    return E.mix(a, b, k)


def passageiro(c, x, y, s, a=1.0, inclina=0.0, cinto=0.0):
    """passageiro sentado de lado (olhando para a direita): quadril em (x, y); cinto = 0..1 desenha a faixa"""
    if a <= 0:
        return
    M.rrect(c, x - s * 0.9, y - s * 2.6, s * 0.45, s * 2.7, 12, "#55555C", a)       # encosto
    M.rrect(c, x - s * 0.9, y - s * 0.1, s * 1.9, s * 0.45, 12, "#55555C", a)       # assento
    g = math.radians(inclina)
    ombro = (x + math.sin(g) * 1.5 * s, y - math.cos(g) * 1.5 * s)
    lw = max(6, s * 0.24)
    M.line(c, x, y, *ombro, TINTA2, a, lw)
    M.line(c, x, y, x + s * 1.2, y, TINTA2, a, lw)
    M.line(c, x + s * 1.2, y, x + s * 1.3, y + s * 1.1, TINTA2, a, lw)
    M.line(c, *ombro, ombro[0] + s * 0.9, ombro[1] + s * 0.5, TINTA2, a, lw)
    c.drawCircle(ombro[0] + math.sin(g) * 0.6 * s, ombro[1] - math.cos(g) * 0.6 * s, s * 0.42, M.paint(TINTA2, a))
    if cinto > 0:
        M.line(c, ombro[0] - s * 0.1, ombro[1], lerp(ombro[0] - s * 0.1, x + s * 0.5, cinto), lerp(ombro[1], y + s * 0.15, cinto), E.COR, a, lw * 0.7)


def cabo(c, t, t0, x0, x1, y, esq, dir_, d=0.5):
    """cabo de guerra: corda e uma pessoa por força em cada ponta; esq/dir_ = número de pessoas"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    M.line(c, x0, y, x1, y, "#9C7A4B", q, 9)
    for i in range(esq):
        pessoa(c, x0 + 40 + i * 90, y + 170, 52, q, inclina=-20, braco=-10, sentido=1)
    for i in range(dir_):
        pessoa(c, x1 - 40 - i * 90, y + 170, 52, q, inclina=-20, braco=-10, sentido=-1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            # o ônibus chega da esquerda e freia em s01.a; o passageiro segue para a frente em s01.b
            t0, tf = C["s01"], C["s01.a"] + 0.9
            if t < C["s01.a"]:
                x = lerp(700, 1300, prog(t, t0, C["s01.a"] - t0))
            else:
                q = prog(t, C["s01.a"], 0.9)
                x = 1300 + 120 * (1 - (1 - q) ** 2)
            inc = 32 * ease_out(prog(t, C["s01.b"] - 0.2, 0.6))
            dx = 70 * ease_out(prog(t, C["s01.b"] - 0.2, 0.6))
            E.foco(c, t, t0, 0.5, lambda a: onibus(c, x, 760, 760, a, lambda piso: pessoa(c, x + dx - 60, piso, 66, a, inclina=inc, braco=-60)))
            F.chao(c, 820, 1840, 760, ep(t, t0, 0.5))
            if t < C["s01.a"] + 0.3:
                F.vetor(c, t, t0 + 0.3, (x - 120, 300), (x + 160, 300), "v", None, F.VEL, 10, size=54)
            F.vetor(c, t, C["s01.b"], (x + 60, 300), (x + 320, 300), "v", None, F.VEL, 10, size=54)
            E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.escreve(c, "você segue", x + 340, 318, 44, "i", F.VEL, a))
            E.frase(c, t, C["s01.a"], [("o", "i", 84), ("ônibus", "i", 84), ("freia", "g", 84, COR)], XE, 300)
            E.frase(c, t, C["s01.b"], [("você", "i", 84), ("vai", "i", 84), ("para", "i", 84), ("a", "i", 84), ("frente", "g", 84)], XE, 430)
            E.frase(c, t, C["s01.c"], [("ninguém", "g", 76, ERRADO), ("empurrou", "i", 80)], XE, 900)
            E.frase(c, t, C["s01.c"] + 1.6, [("o", "i", 70), ("que", "i", 70), ("aconteceu?", "g", 70, COR)], XE, 1010)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.b", "somar as forças", 0), ("s02.c", "parado ou reto", 0), ("s02.d", "o cinto", 0)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "somar vetores,", "o barco no rio"), ("s03.c", "movimento uniforme,", "reta e mesma velocidade")))


# ---------------- força ----------------
def b_forca(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("força", "g", 110, COR)], XE, 260)
        E.frase(c, t, C["s04.a"] + 0.5, ps("empurrão ou puxão", "i", 80), XE, 380, passo=0.14)
        E.foco(c, t, C["s04.a"] + 0.3, 0.5, lambda a: (pessoa(c, 1150, 620, 70, a, inclina=25, braco=5),
                                                       F.bloco(c, 1440, 520, 240, 200, None, E.COR, a)))
        F.chao(c, 1000, 1700, 620, ep(t, C["s04.a"] + 0.3, 0.4)) if t >= C["s04.a"] + 0.3 else None
        seta_f(c, t, C["s04.a"] + 0.9, (1560, 520), 0, 200, "F", lpos=(1660, 470))
        pilula_em(c, t, C["s04.b"], "VETORIAL", XE + 230, 540, 64, E.COR)
        E.frase(c, t, C["s04.b"] + 0.5, ps("módulo · direção · sentido", "i", 56, TINTA2), XE, 660, passo=0.12)
        # a porta, vista de cima: empurrar para dentro e puxar para fora
        E.foco(c, t, C["s04.c"] - 0.4, 0.4, lambda a: (M.rrect(c, 900, 860, 300, 26, 8, "#8B5E3C", a), centro(c, "porta", 1050, 950, 44, "i", TINTA2, a)))
        F.vetor(c, t, C["s04.c"], (1050, 700), (1050, 850), None, None, E.COR, 10)
        E.foco(c, t, C["s04.c"] + 0.2, 0.4, lambda a: E.escreve(c, "para dentro", 1090, 780, 46, "i", TINTA, a))
        F.vetor(c, t, C["s04.d"], (1550, 850), (1550, 700), None, None, E.COR, 10)
        E.foco(c, t, C["s04.d"] - 0.4, 0.4, lambda a: M.rrect(c, 1400, 860, 300, 26, 8, "#8B5E3C", a))
        E.foco(c, t, C["s04.d"] + 0.2, 0.4, lambda a: E.escreve(c, "para fora", 1590, 780, 46, "i", TINTA, a))
        E.foco(c, t, C["s04.d"] + 0.8, 0.4, lambda a: E.pilula(c, "efeitos opostos", 1300, 1010, 44, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], ps("unidade de força:", "i", 76), XE, 280, passo=0.12)
    E.frase(c, t, C["s05.a"] + 0.6, [("newton", "g", 130, COR)], XE, 450)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.bola(c, XE + 700, 405, 90, a=a), centro(c, "N", XE + 700, 440, 100, "g", BR, a)))
    # o saco de arroz de 1 kg segurado pela mão: uns 10 N para cima
    def saco(a):
        F.bloco(c, 1400, 760, 230, 270, "1 kg", "#EDE3C8", a, size=64)
        E.escreve(c, "arroz", 1345, 690, 40, "i", TINTA2, a)
    E.foco(c, t, C["s05.c"], 0.5, saco)
    seta_f(c, t, C["s05.c"] + 0.5, (1400, 620), 90, 220, "F", modulo="10 N", lpos=(1600, 500))
    E.frase(c, t, C["s05.c"], ps("segurar 1 kg:", "i", 66), XE, 680, passo=0.12)
    E.foco(c, t, C["s05.c"] + 0.6, 0.5, lambda a: (E.escreve(c, "≈", XE, 820, 100, "g", TINTA2, a), F.medida(c, 10, "N", XE + 90, 820, 110, COR, a)))
    pilula_em(c, t, C["s05.end"] - 2.6, "por quê: aula de peso", XE + 280, 960, 44, TINTA2, "b")


# ---------------- resultante ----------------
def b_resultante(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("várias forças,", "i", 80) + [("um", "g", 76), ("corpo", "g", 76)], XE, 250, passo=0.12)
        cx, cy = 1250, 560
        E.foco(c, t, C["s06.a"] + 0.4, 0.5, lambda a: F.bloco(c, cx, cy, 220, 170, None, TINTA2, a))
        seta_f(c, t, C["s06.a"] + 0.8, (cx + 110, cy - 30), 0, 220, "F_{1}", lpos=(cx + 260, cy - 70))
        seta_f(c, t, C["s06.a"] + 1.1, (cx + 110, cy + 40), 0, 130, "F_{2}", lpos=(cx + 210, cy + 120))
        seta_f(c, t, C["s06.a"] + 1.4, (cx - 110, cy), 180, 160, "F_{3}", lpos=(cx - 220, cy - 50))
        # soma: 2 + 1,3 − 1,6 = 1,9 de 100 px
        if t >= C["s06.b"]:
            F.seta(c, cx - 95, cy + 210, cx - 95 + 190, cy + 210, TINTA, 1.0, 14, p=ease_out(prog(t, C["s06.b"] + 0.4, 0.6)))
            E.foco(c, t, C["s06.b"] + 0.8, 0.4, lambda a: rot_vetor(c, "F_{R}", cx + 190, cy + 230, 60, TINTA, a))
        E.frase(c, t, C["s06.b"], [("força", "i", 80), ("resultante", "g", 80, COR)], XE, 400)
        E.frase(c, t, C["s06.b"] + 0.6, ps("a soma de todas", "i", 60, TINTA2), XE, 500, passo=0.12)
        E.frase(c, t, lerp(C["s06.b"], C["s06.end"], 0.55), ps("é ela que", "i", 66) + [("decide", "g", 66, COR)], XE, 860, passo=0.12)
        return

    def cena(k, titulo, setas, conta, res, cor_res=TINTA, pessoas=None, carro=False):
        y = 470
        E.frase(c, t, C[k], titulo, XE, 190, passo=0.12)
        if carro:
            E.foco(c, t, C[k + ".a"], 0.5, lambda a: (F.carrinho(c, 1200, 620, 360, a=a), pessoa(c, 880, 620, 60, a, inclina=25, braco=0),
                                                       pessoa(c, 790, 620, 60, a * 0.8, inclina=25, braco=0)))
            F.chao(c, 600, 1500, 620, ep(t, C[k + ".a"], 0.4)) if t >= C[k + ".a"] else None
        if pessoas:
            cabo(c, t, C[k + ".a"], 520, 1400, 520, *pessoas)
            if t >= C[k + ".a"]:
                M.line(c, 960, 470, 960, 570, ERRADO, ep(t, C[k + ".a"], 0.4) * 0.8, 5, dash=E.TRACO)
        for ti, P, ang, comp, rot, mod, lp in setas:
            seta_f(c, t, ti, P, ang, comp, rot, modulo=mod, lpos=lp, size=50)
        for ti, s in conta:
            sub_em(c, t, ti, s, W / 2, 900, 96, "g", TINTA, "center")
        if res:
            ti, P, comp, mod = res
            if t >= ti:
                F.seta(c, *P, P[0] + comp, P[1], cor_res, 1.0, 14, p=ease_out(prog(t, ti, 0.6)))
                E.foco(c, t, ti + 0.4, 0.4, lambda a: (rot_vetor(c, "F_{R}", P[0] + comp + 90, P[1] + 22, 58, cor_res, a),
                                                       F.medida(c, *mod.split(" "), P[0] + comp + 150, P[1] + 22, 58, cor_res, a)))

    if t < C["s08"]:
        E.saida(c, t, C["s08"] - 0.1, lambda: cena(
            "s07", ps("mesmo sentido:", "i", 76) + [("soma", "g", 76, COR)],
            [(C["s07.b"], (1400, 470), 0, 200, "F_{1}", "200 N", (1740, 488)), (C["s07.c"], (1400, 560), 0, 150, "F_{2}", "150 N", (1700, 578))],
            [], (C["s07.d"], (700, 760), 350, "350 N"), carro=True))
        if t >= C["s07.d"]:
            E.foco(c, t, C["s07.d"], 0.5, lambda a: sub(c, "200 + 150 = 350", W / 2, 960, 84, "g", TINTA, a, "center"))
        return
    if t < C["s09"]:
        def s08():
            cena("s08", ps("sentidos opostos:", "i", 76) + [("subtrai", "g", 76, COR)],
                 [(C["s08.b"], (1400, 520), 0, 300, "F_{1}", "300 N", (1560, 470)), (C["s08.c"], (520, 520), 180, 200, "F_{2}", "200 N", (400, 470))],
                 [], (C["s08.e"], (900, 800), 100, "100 N"), pessoas=(2, 3))
            E.foco(c, t, C["s08.d"], 0.5, lambda a: sub(c, "300 − 200 = 100", W / 2, 960, 84, "g", TINTA, a, "center"))
            E.foco(c, t, C["s08.e"] + 0.8, 0.4, lambda a: E.pilula(c, "para a direita", 1500, 790, 44, "b", fundo=TINTA, a=a))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    cena("s09", ps("e se", "i", 76) + [("empatam?", "g", 76, COR)],
         [(C["s09.a"], (1400, 520), 0, 300, "F_{1}", "300 N", (1560, 470)), (C["s09.a"] + 0.4, (520, 520), 180, 300, "F_{2}", "300 N", (360, 470))],
         [], None, pessoas=(3, 3))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: sub(c, "300 − 300 = 0", W / 2, 860, 84, "g", TINTA, a, "center"))
    pilula_em(c, t, C["s09.b"] + 0.5, "resultante zero", W / 2, 980, 56, E.COR)
    E.frase(c, t, C["s09.c"], ps("uma cancela a outra", "i", 56, TINTA2), 1500, 860, "center", 0.1)


# ---------------- primeira lei ----------------
def b_inercia(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("1ª", "g", 96, COR), ("lei", "i", 100), ("de", "i", 100), ("Newton", "g", 96)], XE, 220, passo=0.12)
        E.foco(c, t, C["s10.b"] - 1.4, 0.5, lambda a: sub(c, "F_{R} = 0", XE, 360, 84, "g", TINTA, a))
        E.frase(c, t, C["s10.b"], ps("o corpo", "i", 70) + [("mantém", "g", 70, COR)] + ps("o que fazia", "i", 70), XE + 430, 360, passo=0.12)
        for i, (k, l1, l2) in enumerate((("s10.c", "parado", "continua parado"), ("s10.d", "em movimento", "reto, mesma velocidade"))):
            x = 170 + i * 820
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, 450, 760, 520, p, prog_=p)
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 60, TINTA2)], x + 40, 530)
            E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 40, 620)
            if t >= C[k]:
                F.chao(c, x + 40, x + 720, 880, p)
        E.foco(c, t, C["s10.c"] + 0.5, 0.5, lambda a: F.bloco(c, 550, 800, 200, 160, "v = 0", TINTA2, a, size=46))
        if t >= C["s10.d"] + 0.4:
            q = ((t - C["s10.d"] - 0.4) * 160) % 900
            xx = 1050 + q
            c.save(); c.clipRect(skia.Rect.MakeXYWH(990, 450, 760, 520))
            F.carrinho(c, xx, 880, 220, a=ep(t, C["s10.d"] + 0.4, 0.4), giro=q * 2)
            F.seta(c, xx + 120, 690, xx + 300, 690, F.VEL, 1.0, 9)
            c.restore()
            E.foco(c, t, C["s10.d"] + 1.6, 0.4, lambda a: E.pilula(c, "movimento uniforme", 1370, 940, 40, "b", fundo=F.VEL, a=a))
        return
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], [("inércia", "g", 140, COR)], XE, 320)
            E.frase(c, t, C["s11.a"] + 0.6, ps("tendência de manter o movimento", "i", 56, TINTA2), XE, 420, passo=0.1)
            E.frase(c, t, C["s11.b"], ps("mudar a velocidade", "i", 70) + [("→", "g", 70, TINTA2)], XE, 580, passo=0.12)
            E.foco(c, t, C["s11.c"], 0.5, lambda a: sub(c, "F_{R} ≠ 0", XE + 780, 580, 84, "g", COR, a))
            E.frase(c, t, C["s11.d"], ps("mais massa,", "i", 64) + [("mais", "g", 64, COR), ("inércia", "g", 64, COR)], XE, 760, passo=0.12)
            E.foco(c, t, C["s11.d"] + 0.6, 0.5, lambda a: (F.bloco(c, 1250, 900, 150, 120, "vazio", TINTA2, a, size=36),
                                                           F.bloco(c, 1600, 870, 300, 180, "cheio", E.COR, a, size=50)))
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    if t < C["s13"]:
        def s12():
            t0 = C["s12"]
            q = ease_out(prog(t, C["s12.a"], 1.2))
            x = 1180 + 160 * q
            dx = 110 * ease_out(prog(t, C["s12.c"], 0.9))
            E.foco(c, t, t0, 0.5, lambda a: onibus(c, x, 760, 760, a, lambda piso: pessoa(c, x - 80 + dx, piso, 66, a, inclina=30 * dx / 110, braco=-60)))
            F.chao(c, 760, 1840, 760, ep(t, t0, 0.5))
            seta_f(c, t, C["s12.a"], (x - 380, 520), 180, 170, "F", lpos=(x - 600, 500))
            E.foco(c, t, C["s12.a"] + 0.5, 0.4, lambda a: E.escreve(c, "freio", x - 630, 600, 44, "i", TINTA2, a))
            E.frase(c, t, C["s12.a"], ps("freio:", "i", 66) + [("força", "g", 66, COR), ("no", "i", 66), ("ônibus", "i", 66)], XE, 230, passo=0.12)
            E.frase(c, t, C["s12.b"], ps("em você:", "i", 66) + [("nenhuma", "g", 66, ERRADO)] + ps("na horizontal", "i", 66), XE, 340, passo=0.12)
            F.vetor(c, t, C["s12.c"], (x - 40 + dx, 300), (x + 220 + dx, 300), "v", None, F.VEL, 10, size=50)
            E.frase(c, t, C["s12.d"], ps("o ônibus", "i", 66) + [("parou", "g", 66, COR)] + ps("embaixo de você", "i", 66), XE, 960, passo=0.12)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    # s13: o cinto
    E.frase(c, t, C["s13.a"], [("cinto", "i", 100), ("de", "i", 100), ("segurança", "g", 100, COR)], XE, 240, passo=0.12)
    E.foco(c, t, C["s13"] + 0.2, 0.5, lambda a: passageiro(c, 1180, 760, 90, a, 0, ep(t, C["s13.a"], 0.6)))
    seta_f(c, t, C["s13.b"], (1200, 600), 180, 220, "F", lpos=(1000, 560))
    E.frase(c, t, C["s13.b"], ps("força", "i", 70) + [("para", "g", 66), ("trás", "g", 66, COR)], XE, 470, passo=0.12)
    E.frase(c, t, C["s13.b"] + 1.0, ps("você para junto com o carro", "i", 56, TINTA2), XE, 570, passo=0.1)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (M.rrect(c, 1560, 500, 70, 360, 16, "#55555C", a), centro(c, "painel", 1595, 920, 44, "i", TINTA2, a)))
    E.foco(c, t, C["s13.c"] + 0.4, 0.5, lambda a: E.selo(c, 1700, 450, 54, False, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], ps("em movimento", "i", 72) + [("→", "g", 72, TINTA2)] + ps("força para a frente?", "i", 72), XE, 340, passo=0.12)
        E.foco(c, t, C["s14.a"] + 1.4, 0.4, lambda a: E.selo(c, 1720, 320, 50, False, a))
        E.foco(c, t, C["s14.b"], 0.5, lambda a: F.medida(c, 80, "km/h", XE, 560, 110, COR, a))
        if t >= C["s14.b"]:
            q = ((t - C["s14.b"]) * 220) % 1500
            c.save(); c.clipRect(skia.Rect.MakeXYWH(150, 600, 1620, 400))
            F.carrinho(c, 300 + q, 900, 300, a=ep(t, C["s14.b"], 0.4), giro=q * 1.5)
            F.seta(c, 300 + q + 170, 680, 300 + q + 400, 680, F.VEL, 1.0, 9)
            c.restore()
            F.chao(c, 160, 1760, 900, ep(t, C["s14.b"], 0.4))
            E.foco(c, t, C["s14.b"] + 1.2, 0.4, lambda a: E.pilula(c, "velocidade constante, em linha reta", 1250, 560, 44, "b", fundo=F.VEL, a=a))
        E.frase(c, t, C["s14.end"] - 1.4, [("F", "g", 70), ("=", "g", 70), ("?", "g", 70, COR)], 1700, 1010, "center")
        return
    cx, cy = 960, 640
    E.foco(c, t, C["s15"], 0.5, lambda a: F.carrinho(c, cx, cy + 90, 420, a=a))
    F.chao(c, 500, 1420, cy + 90, ep(t, C["s15"], 0.4))
    seta_f(c, t, C["s15"] + 0.4, (cx + 220, cy - 10), 0, 260, "F", lpos=(cx + 360, cy - 50))
    seta_f(c, t, C["s15.a"], (cx - 220, cy - 10), 180, 260, None)
    E.foco(c, t, C["s15.a"] + 0.3, 0.4, lambda a: E.escreve(c, "ar + atrito", cx - 640, cy - 50, 50, "i", TINTA, a))
    E.foco(c, t, C["s15.a"] + 1.0, 0.4, lambda a: E.pilula(c, "atrito: outra aula", cx - 470, cy + 40, 36, "b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: sub(c, "F_{R} = 0", W / 2, 360, 110, "g", CERTO, a, "center"))
    E.frase(c, t, C["s15.c"], ps("frente", "g", 70) + [("=", "g", 70, COR)] + ps("trás", "g", 70), W / 2, 900, "center", 0.12)
    E.foco(c, t, C["s15.c"] + 0.8, 0.4, lambda a: E.selo(c, W / 2 + 330, 880, 46, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s16.a"] - 0.5, ps("leu", "i", 64, CLARO), XE, 330)
        for i, (k, s) in enumerate((("s16.a", "parado"), ("s16.b", "em equilíbrio"), ("s16.c", "velocidade constante"))):
            E.foco(c, t, C[k], 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 30 + E.larg(s, "g", 50) / 2 + 30 + i * 0, 430 + i * 110, 50, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s16.d"] - 0.3, 0.4, lambda a: E.escreve(c, "→", 1000, 560, 110, "g", CLARO, a))
        E.foco(c, t, C["s16.d"], 0.5, lambda a: sub(c, "F_{R} = 0", 1160, 560, 130, "g", BR, a))
        E.frase(c, t, C["s16.e"], ps("forças numa linha:", "i", 60, CLARO), W / 2, 830, "center", 0.1)
        E.frase(c, t, C["s16.e"] + 0.8, [("um", "g", 76, BR), ("lado", "g", 76, BR), ("=", "g", 76, CLARO), ("outro", "g", 76, BR), ("lado", "g", 76, BR)],
                W / 2, 950, "center", 0.12)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17.a"], ps("funciona porque", "i", 66, CLARO), W / 2, 230, "center", 0.1)
    E.foco(c, t, C["s17.a"] + 0.6, 0.5, lambda a: sub(c, "F_{R} = 0  →  parado ou MU", W / 2, 370, 84, "g", BR, a, "center"))
    E.frase(c, t, C["s17.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("forças inclinadas", "i", 66, CLARO), W / 2, 580, "center", 0.12)
    if t >= C["s17.b"] + 0.6:
        F.seta(c, 820, 900, 1080, 700, CLARO, 1.0, 10, p=ease_out(prog(t, C["s17.b"] + 0.6, 0.6)))
        q = ep(t, C["s17.b"] + 1.2, 0.5)
        M.line(c, 820, 900, 1080, 900, BR, 0.5 * q, 4, dash=E.TRACO)
        M.line(c, 1080, 900, 1080, 700, BR, 0.5 * q, 4, dash=E.TRACO)
    pilula_em(c, t, C["s17.b"] + 1.6, "decompor: outra aula", 1400, 820, 46, E.COR, "b")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    cabeca_q(c, t, C, "s18")
    E.frase(c, t, C["s18.a"], ps("esquerda:", "i", 64), XE, 340)
    E.foco(c, t, C["s18.a"] + 0.6, 0.5, lambda a: (F.medida(c, 250, "N", XE + 300, 340, 72, COR, a), E.escreve(c, "e", XE + 560, 340, 64, "i", TINTA, a),
                                                   F.medida(c, 200, "N", XE + 630, 340, 72, COR, a)))
    E.frase(c, t, C["s18.b"], ps("direita:", "i", 64), XE, 470)
    E.foco(c, t, C["s18.b"] + 0.3, 0.5, lambda a: F.medida(c, 300, "N", XE + 300, 470, 72, COR, a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: (E.escreve(c, "e", XE + 560, 470, 64, "i", TINTA, a), E.escreve(c, "F = ?", XE + 630, 470, 72, "g", COR, a)))
    E.frase(c, t, C["s18.d"], ps("a corda", "i", 64) + [("parada", "g", 64)], XE, 620, passo=0.1)
    E.frase(c, t, C["s18.e"], ps("quanto vale", "i", 76) + [("F?", "g", 76, COR)], XE, 790, passo=0.12)

    def desenho():
        y = 700
        cabo(c, t, C["s18.a"], 1150, 1650, y, 2, 2)
        seta_f(c, t, C["s18.a"] + 0.4, (1150, y - 60), 180, 112, None, modulo="250 N", lpos=(965, y - 45))
        seta_f(c, t, C["s18.a"] + 0.8, (1150, y), 180, 90, None, modulo="200 N", lpos=(985, y + 15))
        seta_f(c, t, C["s18.b"], (1650, y - 60), 0, 135, None, modulo="300 N", lpos=(1720, y - 95))
        seta_f(c, t, C["s18.c"], (1650, y), 0, 68, "F", lpos=(1765, y + 18))
        pilula_em(c, t, C["s18.d"], "parada", 1400, y - 150, 46, TINTA)
    pausa(c, t, C, "s19", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s20():
        E.frase(c, t, C["s20.a"], ps("parada:", "i", 72), XE, 220)
        E.foco(c, t, C["s20.a"] + 0.2, 0.5, lambda a: sub(c, "F_{R} = 0", XE + 300, 220, 84, "g", COR, a))
        E.frase(c, t, C["s20.b"], [("esquerda", "g", 72), ("=", "g", 72, COR), ("direita", "g", 72)], XE, 360, passo=0.12)
        contas(c, t, [(C["s20.c"], "250 + 200 = 450"), (C["s20.d"], "300 + F = 450"), (C["s20.e"] - 0.6, "F = 450 − 300", TINTA2)], XE, 540, 84)
        bola_txt(c, t, C["s20.e"], "150 N", 1460, 640, 170, 90)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], ps("e se andasse", "i", 72) + [("com", "g", 66), ("velocidade", "g", 66), ("constante?", "g", 66, F.VEL)], XE, 260, passo=0.12)
    y = 560
    q = (t - C["s21.a"]) * 70
    if t >= C["s21.a"]:
        c.save(); c.translate(-min(q, 200), 0)
        cabo(c, t, C["s21.a"], 760, 1560, y, 2, 2)
        c.restore()
        F.vetor(c, t, C["s21.a"] + 0.4, (1000, y - 180), (760, y - 180), "v", None, F.VEL, 10, size=50)
    E.frase(c, t, C["s21.b"], [("mesma", "g", 76, CERTO), ("resposta:", "i", 80)], XE, 900, passo=0.12)
    E.foco(c, t, C["s21.b"] + 0.6, 0.5, lambda a: F.medida(c, 150, "N", XE + 700, 900, 96, CERTO, a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: sub(c, "F_{R} = 0", 1500, 900, 96, "g", CERTO, a, "center"))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    resumo(c, t, C, "s22", (("s22.a", [("some", "g", 66), ("as", "i", 70), ("forças:", "i", 70), ("resultante", "g", 66, COR)]),
                            ("s22.b", [("resultante", "g", 66), ("zero:", "g", 66, COR), ("parado", "i", 70), ("ou", "i", 70), ("reto", "i", 70)]),
                            ("s22.c", [("isso", "i", 70), ("é", "i", 70), ("inércia", "g", 66, COR)])), C["s23"])
    if t < C["s23"]:
        return

    def desenho():
        E.foco(c, t, C["s23.a"], 0.5, lambda a: F.bloco(c, 600, 780, 220, 170, "m", TINTA2, a, size=70))
        seta_f(c, t, C["s23.a"] + 0.4, (710, 780), 0, 230, "F", lpos=(1000, 760))
        F.vetor(c, t, C["s23.a"] + 0.8, (520, 920), (760, 920), "a", None, F.ACEL, 8, size=50, lado=-1)
    proxima(c, t, C, "s23", ((C["s23.a"], [("Segunda", "g", 110, COR), ("lei", "i", 110)]),
                             (C["s23.b"], [("F", "g", 96), ("=", "g", 96, TINTA2), ("m · a", "g", 96, COR)])), "s23.c", "s23.d", desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, forca=b_forca, resultante=b_resultante, inercia=b_inercia, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
