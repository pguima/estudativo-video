"""Visual — Estudativo · FIS-CAL-017: geladeira e entropia (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001), a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001) e as peças da termodinâmica do cabeçalho do visual.py da FIS-CAL-011. Nesta aula:
- GELADEIRA = `maquina(..., inv=True)`: as setas de calor SOBEM (da fonte fria para a quente) e o trabalho ENTRA.
- O CICLO DO GÁS dentro da geladeira (`circuito_gel`): um laço de canos; no congelador o cano é azul (o gás frio tira calor),
  na grade de trás é laranja (o gás quente entrega calor); uma bolinha percorre o laço.
- ENTROPIA = espalhamento: a gota de tinta (`gota`) que se espalha; seta para cima = entropia aumenta, para baixo = diminui.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import re

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Calor e Termodinâmica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CAL-017_geladeira_entropia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("invertida", "ciclo", "porta", "entropia", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"
TINTA_GOTA = "#7A3FD0"

# todas as contas da aula (Qq = Qf + τ)
assert 300 + 100 == 400 and 400 - 300 == 100     # porta aberta: a cozinha ganha 100 J por volta
assert 600 + 200 == 800                         # questão
def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-CAL-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "300 J" com a unidade menor"""
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


def formula_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor, align)


def passos(c, t, linhas, x, y0, dy=125, size=80, align="left"):
    """contas empilhadas: linhas = [(t0, fórmula, cor)]"""
    for i, (ti, s, cor) in enumerate(linhas):
        formula_em(c, t, ti, s, x, y0 + i * dy, size, cor=cor, align=align)


def tracejado(c, t, t0, x0, x1, y, cor=TINTA2, d=0.6, largura=4):
    if t >= t0:
        M.line(c, x0, y, x1, y, cor, 0.8, largura, dash=E.TRACO, progress=ease_io(prog(t, t0, d)))


def particulas(c, t, x, y, w, h, agit, cor, a=1.0, n=(6, 4), r=17, borda=True):
    """caixa com partículas que tremem; agit = 0 (quase paradas) a 1 (muito agitadas)"""
    if a <= 0:
        return
    if borda:
        M.rrect(c, x, y, w, h, 26, E.mix(cor, "#FFFFFF", 0.86), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26), M.paint(cor, a, stroke=4))
    nc, nl = n
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x + 4, y + 4, w - 8, h - 8), True)
    amp = 3 + 26 * agit
    vel = 4 + 18 * agit
    for i in range(nc):
        for j in range(nl):
            k = i * 7 + j * 13
            px = x + w * (i + 0.5 + 0.25 * math.sin(k)) / nc + amp * math.sin(t * vel + k * 1.7)
            py = y + h * (j + 0.5 + 0.2 * math.cos(k * 1.3)) / nl + amp * math.cos(t * vel * 1.13 + k * 2.3)
            E.bola(c, px, py, r, cor, a)
    c.restore()


def seta_calor(c, t, t0, A, B, rotulo="calor", cor=None, d=0.7, size=50, a=1.0, ondas=3.0, amp=16, lado=-1, escuro=False):
    """seta ondulada de A até B (o calor passando); rótulo acima (lado=-1) ou abaixo (lado=1)"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    p = ease_io(prog(t, t0, d))
    L = math.dist(A, B)
    ux, uy = (B[0] - A[0]) / L, (B[1] - A[1]) / L
    nx, ny = -uy, ux
    corpo = L - 34
    pts = []
    for i in range(61):
        s = corpo * p * i / 60
        o = amp * math.sin(2 * math.pi * ondas * s / corpo - t * 6)
        pts.append((A[0] + ux * s + nx * o, A[1] + uy * s + ny * o))
    F.poli(c, pts, 1.0, cor, a, 8)
    if p > 0.05:
        tip = (A[0] + ux * (corpo * p + 34), A[1] + uy * (corpo * p + 34))
        F._cabeca(c, tip[0], tip[1], ux, uy, 40, cor, a)
    if rotulo:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        yl = my - amp - 30 if lado < 0 else my + amp + 30 + size * 0.7
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda q: E.formula(c, rotulo, mx, yl, size, "g", cor if not escuro else BR, q * a, "center"))


def seta_reta(c, t, t0, A, B, rotulo=None, cor=TINTA, d=0.5, largura=12, size=56, lado=-1, escuro=False, cab=None):
    """seta grossa e reta (o TRABALHO, o vento, a luz), crescendo de A a B; rótulo no meio (acima com lado=-1)"""
    if t < t0:
        return
    F.seta(c, *A, *B, cor, 1.0, largura, cab, ease_io(prog(t, t0, d)))
    if rotulo:
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        if abs(B[0] - A[0]) < abs(B[1] - A[1]):
            xl, yl, al = mx + lado * 34, my + size * 0.36, "right" if lado < 0 else "left"
        else:
            xl, yl, al = mx, (my - 34 if lado < 0 else my + 34 + size * 0.75), "center"
        E.foco(c, t, t0 + d * 0.6, 0.4, lambda q: E.formula(c, rotulo, xl, yl, size, "g", BR if escuro else cor, q, al))


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) desenha à direita da caixa"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def promessa(c, t, C, cena, itens, y0=450, dy=150, size=78):
    """'até o fim da aula' + itens numerados; itens = [(cue, texto)]. A órbita da Física gira à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", size, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, itens, y0=350, dy=170, size=66):
    """resumindo: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[itens[0][0].split(".")[0]], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.1)


def inscreva(c, t, ti, tb):
    """fim: pílula de inscrição com o cursor (ti) e 'bons estudos' (tb)"""
    E.foco(c, t, ti, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, ti + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, ti + 0.2, 0.4))
    E.frase(c, t, tb, [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")

# ---------------- peças da termodinâmica (FIS-CAL-011 a 017; candidatas ao fisica.py) ----------------
GAS = "#FFE3D3"   # fundo do gás no cilindro


def cilindro(c, t, x, y, w, h, frac, a=1.0, agit=0.4, cor=None, haste=True):
    """cilindro em pé com gás embaixo e êmbolo por cima. (x, y) = canto de cima à esquerda; frac = parte ocupada pelo gás
    (0 a 1, de baixo para cima). Devolve o y da face de baixo do êmbolo"""
    if a <= 0:
        return y + h * (1 - frac)
    cor = cor or E.COR
    ye = y + h * (1 - frac)
    eh = 46
    M.rrect(c, x + 8, ye, w - 16, y + h - ye - 8, 6, GAS, a)
    particulas(c, t, x + 8, ye + 4, w - 16, y + h - ye - 12, agit, cor, a, n=(5, max(1, round(4 * frac + 0.4))), r=13, borda=False)
    M.rrect(c, x + 8, ye - eh, w - 16, eh, 8, TINTA2, a)
    if haste:
        M.rrect(c, x + w / 2 - 12, ye - eh - 150, 24, 150, 6, TINTA2, a)
    p = skia.Path()
    p.moveTo(x, y - 30); p.lineTo(x, y + h); p.lineTo(x + w, y + h); p.lineTo(x + w, y - 30)
    pt = M.paint(TINTA, a, stroke=8)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    return ye


def caixa_gas(c, x, y, w, h, a=1.0, t=0.0, agit=0.4, rotulo="gás", cor=None):
    """o gás como uma caixa (atalho do balanço): borda grossa, partículas e o nome"""
    if a <= 0:
        return
    cor = cor or E.COR
    particulas(c, t, x, y, w, h, agit, cor, a, n=(5, 3), r=14)
    E.pilula(c, rotulo, x + w / 2, y + h + 60, 46, "g", fundo=TINTA, a=a)


def fonte(c, cx, cy, w, h, nome, cor, a=1.0, temp=None, size=50):
    """fonte quente ou fria: faixa arredondada na cor (laranja = quente, azul = frio) com o nome e a temperatura"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 30, cor, a)
    if temp:
        centro(c, nome, cx, cy - 6, size, "g", BR, a)
        E.formula(c, temp, cx, cy + size * 1.0, size * 0.8, "b", BR, a, "center")
    else:
        centro(c, nome, cx, cy + size * 0.36, size, "g", BR, a)


def maquina(c, t, T, cx=1380, y0=150, y1=920, w=560, inv=False, rot=None, temps=(None, None), nome=None, escuro=False, k=1.0):
    """máquina térmica (inv=False) ou geladeira (inv=True) entre a fonte quente (em cima) e a fria (embaixo).
    T = instantes: dict(q=fonte quente, f=fonte fria, m=máquina, Qq=, tau=, Qf=). rot = rótulos das setas
    (padrão "Qq", "τ", "Qf"). Calor = seta ondulada laranja; trabalho = seta reta em tinta (entra na geladeira, sai do motor)"""
    rot = dict(dict(Qq="Q_q", tau="τ", Qf="Q_f"), **(rot or {}))
    hf = 150 * k
    yq, yf = y0 + hf / 2, y1 - hf / 2
    ym = (y0 + y1) / 2
    r = 105 * k
    tinta = BR if escuro else TINTA
    E.foco(c, t, T.get("q", 1e9), 0.5, lambda a: fonte(c, cx, yq, w, hf, "fonte quente", E.COR, a, temps[0]))
    E.foco(c, t, T.get("f", 1e9), 0.5, lambda a: fonte(c, cx, yf, w, hf, "fonte fria", FRIO, a, temps[1]))

    def corpo(a):
        E.bola(c, cx, ym, r, "#3A3A46" if not escuro else "#E8E8EE", a)
        centro(c, nome or ("geladeira" if inv else "máquina"), cx, ym + 16, 40 * k, "g", BR if not escuro else TINTA, a)
    E.foco(c, t, T.get("m", 1e9), 0.5, corpo)
    A1, B1 = (cx, y0 + hf + 12), (cx, ym - r - 12)
    A2, B2 = (cx, ym + r + 12), (cx, y1 - hf - 12)
    if inv:
        A1, B1, A2, B2 = B1, A1, B2, A2
    seta_calor(c, t, T.get("Qq", 1e9), A1, B1, None, d=0.6, amp=12, ondas=2)
    seta_calor(c, t, T.get("Qf", 1e9), A2, B2, None, d=0.6, amp=12, ondas=2)
    for key, (A, B) in (("Qq", (A1, B1)), ("Qf", (A2, B2))):
        if key in T:
            E.foco(c, t, T[key] + 0.4, 0.4, lambda a, key=key, A=A, B=B: fs(c, rot[key], cx - 60, (A[1] + B[1]) / 2 + 22, 56 * k, "g", E.COR if not escuro else E.CLARO, a, "right"))
    if "tau" in T:
        if inv:
            seta_reta(c, t, T["tau"], (cx + r + 260 * k, ym), (cx + r + 14, ym), rot["tau"], tinta, size=56 * k)
        else:
            seta_reta(c, t, T["tau"], (cx + r + 14, ym), (cx + r + 260 * k, ym), rot["tau"], tinta, size=56 * k)
    return dict(ym=ym, r=r, yq=yq, yf=yf)


def ciclo(c, t, t0, P, pts, d=1.6, cor=None, setas=True, largura=7):
    """caminho fechado no gráfico (valores, não pixels), desenhado no sentido dos pontos, com setas no meio de cada lado"""
    cor = cor or TINTA
    px = [P(*v) for v in pts] + [P(*pts[0])]
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    F.poli(c, px, q, cor, 1.0, largura)
    if setas:
        n = len(px) - 1
        for i in range(n):
            if q >= (i + 0.55) / n:
                (x0, y0), (x1, y1) = px[i], px[i + 1]
                L = math.dist((x0, y0), (x1, y1))
                F._cabeca(c, (x0 + x1) / 2 + (x1 - x0) / L * 16, (y0 + y1) / 2 + (y1 - y0) / L * 16, (x1 - x0) / L, (y1 - y0) / L, 34, cor, 1.0)
    for v in px[:-1]:
        c.drawCircle(*v, 11 * min(1, q * 3), M.paint(cor))


def retangulo_area(c, t, t0, P, x0, x1, y0, y1, cor=None, alfa=0.26, d=0.8):
    """pinta o retângulo de valores [x0, x1] × [y0, y1] da esquerda para a direita"""
    if t < t0:
        return
    cor = cor or E.COR
    p = ease_io(prog(t, t0, d))
    L, R = P.x(x0), P.x(x1)
    c.drawRect(skia.Rect.MakeLTRB(L, P.y(y1), lerp(L, R, p), P.y(y0)), M.paint(cor, alfa))


# ---- fórmula com índice embaixo (Q_q, T_f): E.formula ainda não tem índice; esta cópia de _medir/_desenhar acrescenta "_x" ----
def _sub_nos(nos):
    out = []
    for n in nos:
        if n[0] == "t":
            for i, pp in enumerate(re.split(r"_(\w)", n[1])):
                if i % 2 == 0:
                    if pp:
                        out.append(("t", pp))
                else:
                    out.append(("s", [("t", pp)]))
        elif n[0] == "e":
            out.append(("e", _sub_nos(n[1])))
        elif n[0] == "r":
            out.append(("r", _sub_nos(n[1]), n[2]))
        else:
            out.append((n[0], _sub_nos(n[1]), _sub_nos(n[2])))
    return out


def _med(nos, size, est):
    w = 0.0
    for n in nos:
        if n[0] == "t":
            w += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] in "es":
            w += _med(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "r":
            w += _med(n[1], size, est) + size * 0.62
        else:
            w += max(_med(n[1], size * 0.78, est), _med(n[2], size * 0.78, est)) + size * 0.22
    return w


def _des(c, nos, x, y, size, est, cor, a):
    for n in nos:
        if n[0] == "t":
            E.escreve(c, n[1], x, y, size, est, cor, a)
            x += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] in "es":
            _des(c, n[1], x + size * 0.02, y + (size * 0.13 if n[0] == "s" else -size * 0.42), size * 0.58, est, cor, a)
            x += _med(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "r":
            E.formula(c, "r{x}", x, y, size, est, cor, 0)
            x += _med(n[1], size, est) + size * 0.62
        else:
            s_ = size * 0.78
            wc, wb = _med(n[1], s_, est), _med(n[2], s_, est)
            w = max(wc, wb) + size * 0.12
            _des(c, n[1], x + (w - wc) / 2, y - size * 0.46, s_, est, cor, a)
            _des(c, n[2], x + (w - wb) / 2, y + size * 0.46, s_, est, cor, a)
            b = max(4, size * 0.07)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
            x += w + size * 0.1
    return x


def fs(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.formula, com índice: "η = 1 − f{T_f}{T_q}". Devolve a largura"""
    nos = _sub_nos(E._ler(s)[0])
    w = _med(nos, size, est)
    if a > 0 and c is not None:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        _des(c, nos, xi, y, size, est, cor or TINTA, a)
    return w


def fs_em(c, t, t0, s, x, y, size, est="g", cor=TINTA, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fs(c, s, x, y, size, est, cor, a, align))



# ---------------- peças desta aula ----------------
def geladeira(c, x, y, w, h, a=1.0, aberta=0.0):
    """geladeira de frente: congelador em cima; aberta (0 a 1) mostra o interior azul-claro"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 24, "#F4F4F6", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), M.paint(TINTA, a, stroke=6))
    if aberta > 0:
        M.rrect(c, x + 20, y + 20, w - 40, h - 40, 14, GELO, a * aberta)
        for k in range(3):
            M.line(c, x + 30, y + h * (0.35 + 0.2 * k), x + w - 30, y + h * (0.35 + 0.2 * k), TINTA2, a * aberta, 4)
        p = skia.Path()
        p.moveTo(x + w, y + 10); p.lineTo(x + w + w * 0.55 * aberta, y + 40); p.lineTo(x + w + w * 0.55 * aberta, y + h - 40); p.lineTo(x + w, y + h - 10); p.close()
        c.drawPath(p, M.paint("#E2E4EA", a))
        c.drawPath(p, M.paint(TINTA, a, stroke=5))
    else:
        M.line(c, x + 10, y + h * 0.28, x + w - 10, y + h * 0.28, TINTA, a, 5)
        M.rrect(c, x + w - 50, y + h * 0.36, 16, 120, 8, TINTA2, a)


def circuito_gel(c, t, t0, x, y, w, h, ts=None):
    """o laço de canos da geladeira vista de lado: congelador (azul, à esquerda), grade de trás (laranja, à direita),
    compressor embaixo à direita, cano fino em cima. ts = instantes de cada parte: dict(comp, grade, fino, cong)"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    ts = ts or {}
    pts = [(x, y + h), (x + w, y + h), (x + w, y), (x, y)]
    cores = (TINTA2, E.COR, TINTA2, FRIO)
    for i in range(4):
        A, B = pts[i], pts[(i + 1) % 4]
        M.line(c, *A, *B, cores[i], q, 14 if i != 2 else 6, cap_round=True)
    for k in range(6):  # serpentina da grade
        yy = y + h * (k + 0.5) / 6
        M.line(c, x + w - 40, yy, x + w + 40, yy, E.COR, q * ep(t, ts.get("grade", t0), 0.5), 8, cap_round=True)
    for k in range(4):  # serpentina do congelador
        yy = y + h * (k + 0.5) / 4
        M.line(c, x - 40, yy, x + 40, yy, FRIO, q * ep(t, ts.get("cong", t0), 0.5), 8, cap_round=True)
    E.foco(c, t, ts.get("comp", t0), 0.4, lambda a: (M.rrect(c, x + w - 120, y + h - 70, 140, 110, 18, "#3A3A46", a),
                                                    centro(c, "compressor", x + w - 50, y + h + 100, 40, "b", TINTA, a)))
    # a bolinha do gás percorre o laço no sentido: compressor → grade (sobe) → cano fino (esquerda) → congelador (desce)
    L = 2 * (w + h)
    s = ((t - t0) * 260) % L
    seq = [(x + w, y + h, x + w, y), (x + w, y, x, y), (x, y, x, y + h), (x, y + h, x + w, y + h)]
    for (x0, y0, x1, y1) in seq:
        d = math.dist((x0, y0), (x1, y1))
        if s <= d:
            px, py = lerp(x0, x1, s / d), lerp(y0, y1, s / d)
            cor = E.COR if x0 == x + w and y1 == y else (FRIO if x0 == x else TINTA2)
            E.bola(c, px, py, 20, cor, q)
            break
        s -= d


def gota(c, t, t0, cx, cy, r, a=1.0):
    """copo de água com uma gota de tinta que se espalha a partir de t0"""
    if a <= 0:
        return
    M.rrect(c, cx - r, cy - r * 1.2, 2 * r, r * 2.4, 16, AGUA, a * 0.35)
    p = skia.Path()
    p.moveTo(cx - r, cy - r * 1.3); p.lineTo(cx - r * 0.92, cy + r * 1.2); p.lineTo(cx + r * 0.92, cy + r * 1.2); p.lineTo(cx + r, cy - r * 1.3)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    k = ease_io(prog(t, t0, 4.0))
    for i in range(40):
        g = i * 2.399
        rr = (math.sqrt(i / 40)) * r * 0.85 * k + 6 * (1 - k)
        px = cx + math.cos(g) * rr
        py = lerp(cy - r * 0.9, cy, k) + math.sin(g) * rr * 1.2
        c.drawCircle(px, py, 8, M.paint(TINTA_GOTA, a * (0.9 - 0.4 * k)))


def seta_s(c, t, t0, x, y, sobe, rot, size=56, grande=False):
    """entropia: seta grossa para cima (aumenta) ou para baixo (diminui) com o rótulo"""
    L = 200 if grande else 120
    cor = E.COR if sobe else FRIO
    A, B = ((x, y + L / 2), (x, y - L / 2)) if sobe else ((x, y - L / 2), (x, y + L / 2))
    seta_reta(c, t, t0, A, B, None, cor, largura=16 if grande else 12)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot, x, y + L / 2 + 70, size, "g", cor, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        E.foco(c, t, C["s01.a"], 0.6, lambda a: geladeira(c, 1150, 300, 360, 640, a, ep(t, C["s01.a"] + 0.8, 0.8)))
        if t >= C["s01.a"] + 0.6:
            F.termometro(c, t, C["s01.a"] + 0.6, 1780, 900, 420, lerp(55, 80, ease_io(prog(t, C["s01.d"], 1.2))), 0, 100, (), d=0.01)
            E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: centro(c, "cozinha", 1780, 1010, 44, "b", TINTA2, a))
        E.frase(c, t, C["s01.a"], ps("porta da geladeira", "i", 76) + [("aberta", "g", 76, COR)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.6, ps("para refrescar a cozinha", "i", 64, TINTA2), XE, 400, passo=0.1)
        E.frase(c, t, C["s01.b"], [("funciona?", "g", 90)], XE, 580)
        E.frase(c, t, C["s01.c"], [("não:", "g", 90, ERRADO)], XE, 720)
        E.frase(c, t, C["s01.d"], ps("a cozinha", "i", 80) + [("esquenta", "g", 80, COR)], XE, 860, passo=0.12)
        return
    promessa(c, t, C, "s02", (("s02.b", "máquina ao contrário"), ("s02.c", "o que a entropia mede")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def maq(a, x, y):
        fs(c, "Q_q = τ + Q_f", x - 60, y + 20, 52, "g", TINTA, a, "center")

    def desce(a, x, y):
        E.bola(c, x - 130, y, 30, E.COR, a)
        E.bola(c, x + 90, y, 30, FRIO, a)
        F.seta(c, x - 90, y, x + 50, y, E.COR, a, 6)
    lembrete2(c, t, C, "s03", (("s03.b", "a máquina térmica:", "calor em trabalho"), ("s03.c", "o calor sozinho:", "do quente para o frio")), (maq, desce))


# ---------------- a máquina ao contrário ----------------
def b_invertida(c, t, C, b):
    if t < C["s05"]:
        # dentro frio, cozinha quente
        E.foco(c, t, C["s04.a"], 0.5, lambda a: (M.rrect(c, 260, 420, 520, 360, 30, FRIO, a), centro(c, "dentro: frio", 520, 620, 60, "g", BR, a)))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: (M.rrect(c, 1140, 420, 520, 360, 30, E.COR, a), centro(c, "cozinha: quente", 1400, 620, 60, "g", BR, a)))
        E.saida(c, t, C["s04.d"] - 0.1, lambda: seta_calor(c, t, C["s04.c"], (1120, 560), (800, 560), "sozinho", d=0.7, amp=10, ondas=2))
        seta_calor(c, t, C["s04.d"], (800, 640), (1120, 640), None, FRIO, d=0.7, amp=10, ondas=2)
        E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: centro(c, "a geladeira", 960, 740, 46, "g", FRIO, a))
        E.frase(c, t, C["s04.d"], ps("a geladeira faz o", "i", 70) + [("contrário", "g", 70, COR)], W / 2, 240, "center", 0.1)
        E.foco(c, t, C["s04.e"], 0.4, lambda a: E.pilula(c, "do frio para o quente: não vai sozinho", W / 2, 900, 52, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s04.f"], 0.4, lambda a: E.pilula(c, "precisa de trabalho", W / 2, 1000, 56, "g", fundo=E.COR, a=a))
        return
    T = dict(q=C["s05.a"], m=C["s05.a"], f=C["s05.a"], tau=C["s05.b"], Qf=C["s05.c"], Qq=C["s05.d"])
    maquina(c, t, T, cx=1380, y0=150, y1=930, w=540, inv=True, rot=dict(Qq="Q_q", Qf="Q_f"))
    E.foco(c, t, C["s05.a"], 0.4, lambda a: (E.escreve(c, "cozinha", 1700, 330, 44, "i", COR, a), E.escreve(c, "interior", 1700, 900, 44, "i", FRIO, a)))
    E.frase(c, t, C["s05.a"], ps("as setas se", "i", 76) + [("invertem", "g", 76, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s05.b"], ps("o compressor dá", "i", 64) + [("τ", "g", 64, COR)], XE, 400, passo=0.1)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: fs(c, "retira Q_f de dentro", XE, 510, 60, "g", FRIO, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: fs(c, "joga Q_q na cozinha", XE, 610, 60, "g", COR, a))
    E.frase(c, t, C["s05.e"], ps("tudo o que entra,", "i", 64) + [("sai", "g", 64, COR)], XE, 760, passo=0.1)
    fs_em(c, t, C["s05.f"], "Q_q = Q_f + τ", XE, 900, 110)


# ---------------- o ciclo do gás ----------------
def b_ciclo(c, t, C, b):
    x, y, w, h = 1080, 260, 440, 600
    circuito_gel(c, t, C["s06.a"], x, y, w, h, dict(comp=C["s06.b"], grade=C["s06.d"], cong=C["s07.c"]))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "grade de trás", x + w + 60, y + h / 2, 44, "g", COR, a))
    E.foco(c, t, C["s07.a"], 0.4, lambda a: centro(c, "cano fino", x + w / 2, y - 30, 44, "g", TINTA2, a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: centro(c, "congelador", x, y + h + 100, 44, "g", FRIO, a))
    seta_calor(c, t, C["s06.d"] + 0.6, (x + w + 60, y + h / 2 + 60), (x + w + 260, y + h / 2 + 60), None, d=0.5, amp=8, ondas=2)
    seta_calor(c, t, C["s07.c"] + 0.6, (x + 260, y + h / 2 + 60), (x + 60, y + h / 2 + 60), None, d=0.5, amp=8, ondas=2)
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("nos canos,", "i", 70) + [("um", "g", 70), ("gás", "g", 70, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("o compressor aperta:", "i", 60), XE, 420, passo=0.08)
        E.frase(c, t, C["s06.c"], [("esquenta", "g", 64, COR)] + ps("(adiabática)", "i", 56, TINTA2), XE, 510, passo=0.1)
        E.frase(c, t, C["s06.d"], ps("a grade entrega calor", "i", 60), XE, 650, passo=0.08)
        E.frase(c, t, C["s06.d"] + 1.4, ps("para a cozinha", "i", 60), XE, 730, passo=0.08)
        E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "por isso a grade fica morna", XE + 320, 880, 48, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s07.a"], ps("no cano fino,", "i", 66) + [("expande", "g", 64)], XE, 300, passo=0.1)
    E.frase(c, t, C["s07.b"], [("esfria", "g", 76, FRIO), ("muito", "i", 76)], XE, 440, passo=0.12)
    E.frase(c, t, C["s07.c"], ps("no congelador, tira", "i", 60) + [("calor", "g", 60, COR)], XE, 580, passo=0.08)
    E.frase(c, t, C["s07.c"] + 1.4, ps("dos alimentos", "i", 60), XE, 660, passo=0.08)
    E.frase(c, t, C["s07.d"], ps("e o ciclo", "i", 66) + [("recomeça", "g", 64, COR)], XE, 820, passo=0.1)


# ---------------- a porta aberta ----------------
def b_porta(c, t, C, b):
    gx, gy, gw, gh = 760, 330, 320, 560
    E.foco(c, t, C["s08"], 0.5, lambda a: geladeira(c, gx, gy, gw, gh, a, 1.0))
    seta_calor(c, t, C["s08.a"], (gx + gw + 400, gy + 260), (gx + gw + 200, gy + 260), None, d=0.6, amp=10, ondas=2)
    seta_calor(c, t, C["s08.b"], (gx - 20, gy + 260), (gx - 300, gy + 260), None, d=0.6, amp=14, ondas=2)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: (M.rrect(c, gx + gw / 2 - 40, gy + gh + 60, 80, 50, 10, "#3A3A46", a)))
    seta_reta(c, t, C["s08.c"], (gx + gw / 2, gy + gh + 60), (gx + gw / 2, gy + gh + 4), None, TINTA, largura=10)
    if t < C["s09"]:
        E.frase(c, t, C["s08"] + 0.3, ps("a porta aberta", "i", 76), XE, 200, passo=0.12)
        E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: E.escreve(c, "entra pela porta", gx + gw + 200, gy + 200, 52, "i", TINTA, a))
        E.foco(c, t, C["s08.b"] + 0.4, 0.4, lambda a: E.escreve(c, "sai pela grade", 130, gy + 200, 52, "i", TINTA, a))
        E.foco(c, t, C["s08.c"] + 0.4, 0.4, lambda a: E.escreve(c, "+ o trabalho do motor", gx + gw / 2 + 80, gy + gh + 100, 52, "i", TINTA, a))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "sai mais calor do que entra", 1480, 760, 50, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s08.e"], ps("a cozinha", "i", 70) + [("esquenta", "g", 70, COR)], 1480, 900, "center", 0.1)
        return
    E.frase(c, t, C["s09"] + 0.3, ps("com números", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s09.a"], 0.4, lambda a: F.medida(c, 300, "J", gx + gw + 300, gy + 200, 64, COR, a, "center"))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: F.medida(c, 100, "J", gx + gw / 2 + 200, gy + gh + 110, 56, TINTA, a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: F.medida(c, 400, "J", gx - 160, gy + 200, 64, COR, a, "center"))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "a cozinha ganha 100 J por volta", 1480, 760, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "ar-condicionado: o lado quente fica fora de casa", 1260, 200, 44, "g", fundo=TINTA, a=a))


# ---------------- entropia ----------------
def b_entropia(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], [("entropia", "g", 90, COR)], XE, 220)
        E.foco(c, t, C["s10.a"], 0.5, lambda a: gota(c, t, C["s10.b"], 560, 600, 200, a))
        E.frase(c, t, C["s10.b"], ps("se espalha sozinha", "i", 56), 560, 940, "center", 0.08)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "nunca volta a ser gota", 560, 1020, 44, "g", fundo=TINTA, a=a))
        if t >= C["s10.d"]:
            F.termometro(c, t, C["s10.d"], 1500, 820, 400, lerp(85, 30, ease_io(prog(t, C["s10.d"] + 0.4, 2.0))), 0, 100, (), d=0.01)
        E.frase(c, t, C["s10.d"], ps("café quente", "i", 60) + [("esfria", "g", 60, FRIO)], 1500, 940, "center", 0.08)
        E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "nunca esquenta sozinho", 1500, 1020, 44, "g", fundo=TINTA, a=a))
        return
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("entropia", "g", 84, COR)] + ps("mede o", "i", 84) + [("espalhamento", "g", 84)], XE, 300, passo=0.12)
        E.frase(c, t, C["s11.a"] + 2.0, ps("da energia e da matéria: a desorganização", "i", 58, TINTA2), XE, 400, passo=0.06)
        E.frase(c, t, C["s11.b"], ps("nos processos que acontecem sozinhos,", "i", 60), XE, 580, passo=0.06)
        E.frase(c, t, C["s11.b"] + 1.6, ps("a entropia total", "i", 70) + [("sempre", "g", 70, COR), ("aumenta", "g", 70, COR)], XE, 690, passo=0.1)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "outro jeito de dizer a segunda lei", XE + 450, 880, 54, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s11.a"], 0.5, lambda a: gota(c, t, C["s11"] - 10, 1600, 640, 150, a))
        return
    E.frase(c, t, C["s12"], ps("e a geladeira?", "i", 76), W / 2, 200, "center", 0.12)
    seta_s(c, t, C["s12.a"], 340, 500, False, "dentro: diminui", size=50)
    seta_s(c, t, C["s12.c"], 960, 500, True, "cozinha: aumenta mais", size=50, grande=True)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "solta calor + trabalho na cozinha", 660, 300, 46, "i", TINTA2, a))
    seta_s(c, t, C["s12.d"], 1590, 500, True, "universo: cresce", size=50)
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.pilula(c, "energia espalhada é mais difícil de aproveitar", W / 2, 940, 50, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], [("“geladeira", "i", 76), ("produz", "i", 76), ("frio”", "i", 76)], XE + 480, 200, passo=0.12)
    if t >= C["s13.b"]:
        E.risco(c, XE + 470, 220, XE + 1180, 150, t, C["s13.b"], largura=12)
    E.frase(c, t, C["s13.b"], ps("frio não se", "i", 70) + [("fabrica", "g", 70)], XE, 380, passo=0.1)
    E.foco(c, t, C["s13.c"], 0.6, lambda a: geladeira(c, 1150, 330, 300, 520, a))
    seta_calor(c, t, C["s13.c"] + 0.4, (1300, 560), (1700, 560), "calor", d=0.7, amp=12, ondas=2)
    E.frase(c, t, C["s13.c"], ps("ela", "i", 70) + [("tira", "g", 70, COR), ("calor", "g", 70, COR)] + ps("de dentro", "i", 70), XE, 540, passo=0.1)
    E.frase(c, t, C["s13.d"], ps("frio é só o lugar com", "i", 64) + [("menos", "g", 62, FRIO), ("calor", "g", 62, FRIO)], XE, 720, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14.a"], ps("o atalho:", "i", 70, CLARO) + [("três", "g", 70, BR), ("setas", "g", 70, BR)], W / 2, 140, "center", 0.12)
    T1 = dict(q=C["s14.b"], m=C["s14.b"], f=C["s14.b"], Qq=C["s14.b"] + 0.3, tau=C["s14.b"] + 0.6, Qf=C["s14.b"] + 0.9)
    T2 = dict(q=C["s14.c"], m=C["s14.c"], f=C["s14.c"], Qf=C["s14.c"] + 0.3, tau=C["s14.c"] + 0.6, Qq=C["s14.c"] + 0.9)
    maquina(c, t, T1, cx=560, y0=220, y1=780, w=420, k=0.75, escuro=True)
    maquina(c, t, T2, cx=1360, y0=220, y1=780, w=420, k=0.75, inv=True, escuro=True)
    E.foco(c, t, C["s14.b"], 0.4, lambda a: centro(c, "máquina: o calor desce", 560, 860, 46, "g", E.CLARO, a))
    E.foco(c, t, C["s14.c"], 0.4, lambda a: centro(c, "geladeira: o calor sobe", 1360, 860, 46, "g", E.CLARO, a))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: fs(c, "nas duas: Q_q = τ + Q_f", W / 2, 960, 76, "g", BR, a, "center"))
    if t >= C["s15"]:
        E.foco(c, t, C["s15.b"], 0.4, lambda a: E.pilula(c, "sem números? lembre só o sentido das setas", W / 2, 1045, 40, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], ps("retira", "i", 74) + [("600 J", "g", 72, FRIO)] + ps("do interior", "i", 74), XE, 360, passo=0.1)
    E.frase(c, t, C["s16.b"], ps("o compressor gasta", "i", 74) + [("200 J", "g", 72)], XE, 480, passo=0.1)
    E.frase(c, t, C["s16.c"], ps("calor para a cozinha", "i", 70) + [("=", "g", 70), ("?", "g", 76, COR)], XE, 650, passo=0.1)
    E.frase(c, t, C["s16.d"], [("entropia", "g", 66), ("do", "i", 70), ("universo?", "g", 66, COR)], XE, 790, passo=0.12)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)
    else:
        maquina(c, t, dict(q=C["s16.a"], m=C["s16.a"], f=C["s16.a"], Qf=C["s16.a"] + 0.2, tau=C["s16.b"], Qq=C["s16.c"]),
                cx=1460, y0=160, y1=920, w=460, inv=True, rot=dict(Qf="600 J", tau="200 J", Qq="?"))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    maquina(c, t, dict(q=C["s18"], m=C["s18"], f=C["s18"], Qf=C["s18"] + 0.2, tau=C["s18"] + 0.4, Qq=C["s18.c"]),
            cx=1460, y0=160, y1=920, w=460, inv=True, rot=dict(Qf="600 J", tau="200 J", Qq="800 J"))
    E.frase(c, t, C["s18.a"], ps("o lado quente é a", "i", 70) + [("soma", "g", 70, COR)], XE, 260, passo=0.1)
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.formula(c, "600 + 200", XE, 420, 90, "g", TINTA, a))
    bola_txt(c, t, C["s18.c"], "800 J", XE + 700, 390, 110, 64)
    E.frase(c, t, C["s18.d"], ps("entropia do universo:", "i", 64) + [("aumenta", "g", 64, COR)], XE, 660, passo=0.1)
    E.foco(c, t, C["s18.e"], 0.4, lambda a: E.formula(c, "dentro ↓   fora ↑↑", XE, 800, 70, "g", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, (("s19.a", [("geladeira:", "g", 64), ("máquina", "i", 64), ("ao", "i", 64), ("contrário", "g", 64, COR)]),
                         ("s19.b", [("gasta", "i", 64), ("trabalho:", "g", 64), ("calor", "i", 64), ("do", "i", 64), ("frio", "g", 64, FRIO), ("para", "i", 64), ("o", "i", 64), ("quente", "g", 64, COR)]),
                         ("s19.c", [("entropia:", "g", 64, COR), ("espalhamento,", "i", 64), ("sempre", "i", 64), ("cresce", "g", 64)])), y0=380, dy=190)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("praticar", "g", 100, COR)] + ps("a trilha de calor", "i", 90), XE, 410, passo=0.12)
    for i, s in enumerate(("panela no fogo", "motor", "geladeira")):
        E.foco(c, t, C["s20.b"] + 0.6 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 230 + i * 400, 600, 54, "g", fundo=E.COR if i == 0 else TINTA, a=a))
    inscreva(c, t, C["s20.c"], C["s20.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, invertida=b_invertida, ciclo=b_ciclo, porta=b_porta, entropia=b_entropia,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
