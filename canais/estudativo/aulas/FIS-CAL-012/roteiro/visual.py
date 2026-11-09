"""Visual — Estudativo · FIS-CAL-012: primeira lei da termodinâmica (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001), a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001) e as peças da termodinâmica do cabeçalho do visual.py da FIS-CAL-011 (cilindro, seta reta = trabalho,
seta ondulada = calor). Nesta aula:
- O GÁS como CAIXA (`caixa_gas`): o balanço de energia. Seta que ENTRA na caixa soma (+, laranja); seta que SAI subtrai (−).
- ENERGIA INTERNA U = a agitação das partículas: tremem mais quando U sobe, menos quando U cai; ΔU sempre em laranja.
- Sinais: valor positivo em laranja, negativo em azul (F.NEG); conta errada em vermelho com risco.
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
ARQUIVO_FINAL = "estudativo_FIS-CAL-012_primeira_lei_termodinamica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("interna", "lei", "sinais", "exemplo", "exemplo2", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula (ΔU = Q − τ)
du = lambda Q, tau: Q - tau
assert du(500, 200) == 300
assert du(-100, -300) == 200 and -100 + 300 == 200
assert du(-100, 300) == -400                        # o erro: sinal do trabalho esquecido
assert 300 - 100 == 200                             # o atalho da caixa na bomba
assert du(-400, 100) == -500 and 0 - (400 + 100) == -500
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
def balanco(c, t, x, y, w, h, setas, agit=0.4, a_caixa=1.0, t0=None, escuro=False):
    """o gás como caixa com setas: setas = [(instante, tipo "Q"|"tau", entra?, rótulo, lado "esq"|"dir"|"cima"|"baixo")]"""
    if t0 is not None:
        E.foco(c, t, t0, 0.5, lambda a: caixa_gas(c, x, y, w, h, a * a_caixa, t, agit))
    tinta = BR if escuro else TINTA
    for (ti, tipo, entra, rot, lado) in setas:
        if lado == "esq":
            fora, dentro = (x - 300, y + h / 2), (x - 16, y + h / 2)
        elif lado == "dir":
            fora, dentro = (x + w + 300, y + h / 2), (x + w + 16, y + h / 2)
        elif lado == "cima":
            fora, dentro = (x + w / 2, y - 250), (x + w / 2, y - 16)
        else:
            fora, dentro = (x + w / 2, y + h + 330), (x + w / 2, y + h + 110)
        A, B = (fora, dentro) if entra else (dentro, fora)
        cor = E.COR if tipo == "Q" else tinta
        if tipo == "Q":
            seta_calor(c, t, ti, A, B, None, cor, d=0.6, amp=12, ondas=2.5)
        else:
            seta_reta(c, t, ti, A, B, None, cor, d=0.5)
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        vert = lado in ("cima", "baixo")
        E.foco(c, t, ti + 0.3, 0.4, lambda a, rot=rot, mx=mx, my=my, vert=vert, cor=cor: E.formula(
            c, rot, mx + (30 if vert else 0), my + (20 if vert else -40), 54, "g", cor, a, "left" if vert else "center"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        x, y, w, h = 1240, 360, 400, 520
        fr = lerp(0.4, 0.62, ease_io(prog(t, C["s01.b"], 1.2)))
        ag = 0.25 + 0.6 * ep(t, C["s01.c"], 0.8)
        E.foco(c, t, C["s01.a"], 0.6, lambda a: cilindro(c, t, x, y, w, h, fr, a, agit=ag))
        seta_calor(c, t, C["s01.a"] + 0.3, (x + w / 2, y + h + 190), (x + w / 2, y + h + 20), None, d=0.6, amp=12, ondas=2)
        E.foco(c, t, C["s01.a"] + 0.7, 0.4, lambda a: F.medida(c, 500, "J", x + w / 2 + 50, y + h + 140, 56, COR, a))
        if t >= C["s01.c"]:
            F.termometro(c, t, C["s01.c"], x + w + 150, y + h, 380, 70, 0, 100)
        E.frase(c, t, C["s01.a"], ps("um gás recebe", "i", 80) + [("500 J", "g", 80, COR)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("empurra o êmbolo", "i", 74), XE, 430, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("e", "i", 74) + [("esquenta", "g", 74, COR)], XE, 540, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("para onde foi", "i", 90) + [("cada", "g", 90, COR), ("joule?", "g", 90, COR)], XE, 760, passo=0.12)
        return
    promessa(c, t, C, "s02", (("s02.b", "a conta como extrato"), ("s02.c", "sem errar o sinal")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def calor(a, x, y):
        E.bola(c, x - 130, y, 30, E.COR, a)
        E.bola(c, x + 90, y, 30, FRIO, a)
        F.seta(c, x - 90, y, x + 50, y, E.COR, a, 6)

    def trab(a, x, y):
        E.formula(c, "τ = p · ΔV", x - 40, y + 20, 60, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "calor Q, em joule:", "do quente para o frio"), ("s03.c", "trabalho do gás:", "+ na expansão")), (calor, trab))


# ---------------- energia interna ----------------
def b_interna(c, t, C, b):
    E.frase(c, t, C["s04"], ps("falta um nome", "i", 70, TINTA2), XE, 200)
    E.frase(c, t, C["s04.a"], ps("partículas sempre", "i", 70) + [("se agitando", "g", 68, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s04.b"], [("energia", "g", 84), ("interna", "g", 84, COR)], XE, 480, passo=0.12)
    E.foco(c, t, C["s04.b"] + 0.8, 0.5, lambda a: E.formula(c, "U", XE + 760, 480, 110, "g", COR, a))
    E.frase(c, t, C["s04.c"], ps("gás ideal: só depende da", "i", 60) + [("temperatura", "g", 58, COR)], XE, 620, passo=0.08)
    E.foco(c, t, C["s04.d"], 0.4, lambda a: E.formula(c, "esquentou → U aumenta", XE, 770, 58, "g", COR, a))
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.formula(c, "esfriou → U diminui", XE, 870, 58, "g", FRIO, a))
    ag = 0.4 + 0.5 * ep(t, C["s04.d"], 0.8) - 0.75 * ep(t, C["s04.e"], 0.8)
    cor = E.mix(E.COR, FRIO, ep(t, C["s04.e"], 0.8))
    E.foco(c, t, C["s04.a"], 0.6, lambda a: particulas(c, t, 1220, 300, 520, 440, max(0.05, ag), cor, a, n=(5, 4), r=18))
    if t >= C["s04.c"]:
        nivel = 50 + 30 * ep(t, C["s04.d"], 0.8) - 60 * ep(t, C["s04.e"], 0.8)
        F.termometro(c, t, C["s04.c"], 1480, 990, 190, nivel, 0, 100, (), d=0.01)


# ---------------- a lei ----------------
BX, BY, BW, BH = 860, 430, 340, 250


def b_lei(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("a energia não some nem aparece", "i", 70), W / 2, 200, "center", 0.1)
        balanco(c, t, BX, BY, BW, BH, [(C["s05.b"], "Q", True, "calor", "esq"), (C["s05.c"], "tau", False, "trabalho", "dir")], t0=C["s05.b"] - 0.4,
                agit=0.3 + 0.5 * ep(t, C["s05.d"], 0.8))
        E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "o resto fica: energia interna", BX + BW / 2, BY - 90, 48, "g", fundo=E.COR, a=a))
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("primeira lei da termodinâmica", "i", 70, TINTA2), XE, 200, passo=0.1)
        F.formula_legenda(c, t, C["s06.a"], "Q = τ + ΔU", [("Q", "calor", "J"), ("τ", "trabalho", "J"), ("ΔU", "variação da energia interna", "J")],
                          XE, 400, 160, tl=[C["s06.b"], C["s06.c"], C["s06.d"]], size_l=58)
        pilula_em(c, t, C["s06.e"], "tudo em joule", 1500, 340, 56, E.COR)
        return
    E.frase(c, t, C["s07"], ps("pense num", "i", 80) + [("salário", "g", 80, COR)], W / 2, 200, "center", 0.12)
    linhas = (("s07.a", "calor Q", "o salário que entra", E.COR), ("s07.b", "trabalho τ", "o que você gasta", TINTA), ("s07.c", "ΔU", "o quanto o saldo mudou", E.COR))
    for i, (k, l, r, cor) in enumerate(linhas):
        y = 380 + i * 140
        E.foco(c, t, C[k], 0.4, lambda a, l=l, y=y, cor=cor: E.formula(c, l, 760, y, 70, "g", cor, a, "right"))
        E.frase(c, t, C[k] + 0.2, [("=", "g", 70, TINTA2)] + ps(r, "i", 72), 800, y, passo=0.08)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.formula(c, "ΔU = Q − τ", W / 2, 900, 130, "g", TINTA, a, "center"))
    E.foco(c, t, C["s07.d"] + 1.6, 0.4, lambda a: centro(c, "o que entrou menos o que saiu", W / 2, 1000, 50, "i", TINTA2, a))


# ---------------- sinais ----------------
def b_sinais(c, t, C, b):
    E.frase(c, t, C["s08"], ps("os sinais seguem o", "i", 76) + [("gás", "g", 76, COR)], W / 2, 190, "center", 0.12)
    linhas = (("s08.a", "Q", "recebe calor", "cede calor"), ("s08.b", "τ", "expande", "é comprimido"), ("s08.c", "ΔU", "esquenta", "esfria"))
    E.foco(c, t, C["s08.a"] - 0.4, 0.4, lambda a: (centro(c, "positivo (+)", 900, 330, 54, "g", COR, a), centro(c, "negativo (−)", 1500, 330, 54, "g", FRIO, a)))
    for i, (k, letra, pos, neg) in enumerate(linhas):
        y = 500 + i * 190
        E.foco(c, t, C[k], 0.4, lambda a, letra=letra, y=y: E.formula(c, letra, 420, y, 100, "g", TINTA, a, "center"))
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, pos=pos, y=y: E.pilula(c, pos, 900, y - 30, 54, "g", fundo=E.COR, a=a))
        E.foco(c, t, C[k] + 1.6, 0.4, lambda a, neg=neg, y=y: E.pilula(c, neg, 1500, y - 30, 54, "g", fundo=FRIO, a=a))
        if t >= C[k]:
            M.line(c, 250, y + 70, 1750, y + 70, FIO, ep(t, C[k], 0.4), 3)


# ---------------- exemplo 1 ----------------
def b_exemplo(c, t, C, b):
    E.frase(c, t, C["s09"], ps("voltando ao gancho", "i", 70, TINTA2), XE, 200)
    passos(c, t, [(C["s09.a"], "Q = +500 J", COR), (C["s09.b"], "τ = +200 J", TINTA), (C["s09.c"], "ΔU = 500 − 200", TINTA)], XE, 360, 140, 84)
    bola_txt(c, t, C["s09.d"], "+300 J", 470, 860, 130, 70)
    balanco(c, t, 1240, 470, 300, 220, [(C["s09.a"] + 0.2, "Q", True, "500", "esq"), (C["s09.b"] + 0.2, "tau", False, "200", "dir")],
            t0=C["s09.a"], agit=0.3 + 0.5 * ep(t, C["s09.e"], 0.8))
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "saldo positivo: esquentou", 1390, 860, 50, "g", fundo=E.COR, a=a))


# ---------------- exemplo 2: a bomba ----------------
def bomba(c, t, x, y, w, h, frac, a=1.0):
    """bomba de encher pneu: cilindro com a alça em cima e a mangueira"""
    if a <= 0:
        return
    ye = cilindro(c, t, x, y, w, h, frac, a, agit=0.5)
    M.rrect(c, x - 60, ye - 46 - 170, w + 120, 34, 16, TINTA, a)
    p = skia.Path()
    p.moveTo(x + w, y + h - 40); p.cubicTo(x + w + 160, y + h - 40, x + w + 120, y + h + 60, x + w + 240, y + h + 40)
    c.drawPath(p, M.paint(TINTA, a, stroke=10))


def b_exemplo2(c, t, C, b):
    x, y, w, h = 1350, 380, 260, 480
    fr = lerp(0.75, 0.4, ease_io(prog(t, C["s10.a"], 1.4)))
    E.foco(c, t, C["s10"], 0.6, lambda a: bomba(c, t, x, y, w, h, fr, a))
    if t >= C["s10.a"]:
        seta_reta(c, t, C["s10.a"], (x + w / 2, 120), (x + w / 2, 260), "300 J", TINTA, lado=1)
    seta_calor(c, t, C["s10.b"], (x - 20, y + h - 80), (x - 260, y + h - 80), "100 J", d=0.6, amp=10, ondas=2)
    if t < C["s11"]:
        E.frase(c, t, C["s10"], [("bomba", "g", 80, COR)] + ps("de encher pneu", "i", 80), XE, 220, passo=0.12)
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.formula(c, "compressão: τ = −300 J", XE, 520, 70, "g", FRIO, a))
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.formula(c, "calor saindo: Q = −100 J", XE, 660, 70, "g", FRIO, a))
        return
    passos(c, t, [(C["s11.a"], "ΔU = Q − τ", TINTA2), (C["s11.b"], "ΔU = −100 − (−300)", TINTA), (C["s11.d"], "ΔU = −100 + 300", TINTA)], XE, 280, 140, 76)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "menos com menos dá mais", XE + 330, 650, 44, "b", fundo=TINTA2, a=a))
    bola_txt(c, t, C["s11.e"], "+200 J", 470, 820, 120, 66)
    E.foco(c, t, C["s11.f"], 0.4, lambda a: E.pilula(c, "o ar esquentou", 900, 820, 50, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("o sinal do trabalho", "i", 76) + [("na", "i", 76), ("compressão", "g", 72)], XE + 480, 200, passo=0.1)
    E.foco(c, t, C["s12.a"] + 1.2, 0.4, lambda a: E.formula(c, "τ = +300 ?", W / 2, 400, 90, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "−100 − 300", W / 2, 560, 100, "g", TINTA, a, "center"))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "= −400 J", W / 2, 700, 100, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "esfriou?", W / 2 - 200, 860, 110, "g", ERRADO, a))
    if t >= C["s12.e"]:
        E.risco(c, W / 2 - 220, 880, W / 2 + 230, 780, t, C["s12.e"], largura=12)
        E.foco(c, t, C["s12.e"] + 0.5, 0.4, lambda a: E.pilula(c, "a bomba esquenta na mão", W / 2, 990, 48, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho:", "i", 70, CLARO) + [("a", "i", 70, CLARO), ("caixa", "g", 70, BR)], W / 2, 160, "center")
    x, y, w, h = 810, 470, 300, 210
    if t < C["s14"]:
        balanco(c, t, x, y, w, h, [(C["s13.c"], "Q", True, "+", "esq"), (C["s13.d"], "tau", False, "−", "dir")], t0=C["s13.a"], escuro=True)
        E.foco(c, t, C["s13.c"] + 0.4, 0.4, lambda a: centro(c, "entra: soma", x - 150, y + h + 110, 54, "g", E.CLARO, a))
        E.foco(c, t, C["s13.d"] + 0.4, 0.4, lambda a: centro(c, "sai: subtrai", x + w + 150, y + h + 110, 54, "g", BR, a))
        E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "ΔU = entra − sai", W / 2, 940, 96, "g", BR, a, "center"))
        return
    balanco(c, t, x, y, w, h, [(C["s14.a"], "tau", True, "300", "cima"), (C["s14.b"], "Q", False, "100", "dir")], t0=C["s14"], escuro=True)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "300 − 100 = +200 J", W / 2, 890, 90, "g", BR, a, "center"))
    E.frase(c, t, C["s14.e"], [("não", "g", 56, ERRADO), ("compensa:", "i", 60, CLARO), ("Q", "g", 56, BR), ("e", "i", 60, CLARO), ("τ", "g", 56, BR)] + ps("já com sinal", "i", 60, CLARO), W / 2, 1010, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("o gás", "i", 74) + [("cede", "g", 72), ("400 J", "g", 72, COR)] + ps("de calor", "i", 74), XE, 360, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("e", "i", 74) + [("faz", "g", 72), ("100 J", "g", 72, COR)] + ps("de trabalho", "i", 74), XE, 490, passo=0.1)
    E.frase(c, t, C["s15.c"], [("ΔU", "g", 80, COR), ("=", "g", 80), ("?", "g", 80, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s15.d"], [("sobe", "g", 70), ("ou", "i", 74), ("desce?", "g", 70, COR)], XE, 800, passo=0.12)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)
    else:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: caixa_gas(c, 1310, 420, 300, 220, a, t, 0.4))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x, y, w, h = 1240, 420, 300, 220
    balanco(c, t, x, y, w, h, [(C["s17.a"], "Q", False, "400", "esq"), (C["s17.b"], "tau", False, "100", "dir")], t0=C["s17"],
            agit=0.5 - 0.4 * ep(t, C["s18.d"], 0.8))
    if t < C["s18"]:
        E.frase(c, t, C["s17"], ps("com a caixa", "i", 70, TINTA2), XE, 220)
        E.frase(c, t, C["s17.a"], [("sai", "i", 70), ("400", "g", 70, FRIO)] + ps("de calor", "i", 70), XE, 360, passo=0.1)
        E.frase(c, t, C["s17.b"], [("sai", "i", 70), ("100", "g", 70, FRIO)] + ps("de trabalho", "i", 70), XE, 480, passo=0.1)
        E.foco(c, t, C["s17.c"], 0.4, lambda a: E.formula(c, "0 − 500", XE, 640, 84, "g", TINTA, a))
        bola_txt(c, t, C["s17.d"], "−500 J", 420, 850, 120, 64)
        return
    passos(c, t, [(C["s18.a"], "Q = −400 J   τ = +100 J", TINTA2), (C["s18.b"], "ΔU = −400 − 100 = −500 J", TINTA)], XE, 300, 150, 66)
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.pilula(c, "a energia interna diminuiu", XE + 420, 620, 50, "g", fundo=FRIO, a=a))
    E.frase(c, t, C["s18.d"], ps("a temperatura", "i", 80) + [("desce", "g", 84, FRIO)], XE, 820, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        resumo(c, t, C, (("s19.a", [("Q = τ + ΔU", "g", 70, COR)]),
                         ("s19.b", [("cada", "i", 66), ("termo:", "i", 66), ("+", "g", 66, COR), ("ou", "i", 66), ("−", "g", 66, FRIO)]),
                         ("s19.c", [("caixa:", "g", 66), ("entra", "i", 66), ("soma,", "g", 66, COR), ("sai", "i", 66), ("subtrai", "g", 66, FRIO)])), y0=380, dy=190)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("quando um termo vira", "i", 84) + [("zero", "g", 90, COR)], XE, 410, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "Q = τ + ΔU", 620, 650, 110, "g", TINTA, a, "center"))
    if t >= C["s20.b"] + 0.8:
        E.risco(c, 700, 670, 960, 580, t, C["s20.b"] + 0.8, cor=E.COR, largura=10)
        E.foco(c, t, C["s20.b"] + 1.2, 0.4, lambda a: E.formula(c, "0", 830, 760, 80, "g", COR, a, "center"))
    inscreva(c, t, C["s20.c"], C["s20.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, interna=b_interna, lei=b_lei, sinais=b_sinais, exemplo=b_exemplo,
              exemplo2=b_exemplo2, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
