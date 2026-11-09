"""Visual — Estudativo · FIS-CAL-014: segunda lei e máquinas térmicas (trilha Calor e Termodinâmica).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001), a da trilha Calor e Termodinâmica (cabeçalho do
visual.py da FIS-CAL-001) e as peças da termodinâmica do cabeçalho do visual.py da FIS-CAL-011. Nesta aula:
- MÁQUINA TÉRMICA (`maquina`): fonte quente (faixa laranja) em cima, a máquina (esfera escura) no meio, fonte fria (faixa
  azul) embaixo. Calor = setas onduladas laranja descendo (Q_q e Q_f); trabalho τ = seta reta em tinta saindo para a direita.
  Q_q e Q_f com índice (`fs`), sempre como quantidades sem sinal.
- BARRA DO CALOR (`barra_calor`): 100 % do calor recebido; a parte útil (trabalho) em laranja, a jogada fora em azul.
- Rendimento η na esfera laranja (bola_txt), em porcentagem.
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
ARQUIVO_FINAL = "estudativo_FIS-CAL-014_segunda_lei_maquinas_termicas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("maquina", "rendimento", "segunda", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FRIO = F.NEG
GELO = "#A9D8F5"
AGUA = "#5BA8E0"

# todas as contas da aula (τ = Qq − Qf; η = τ/Qq = 1 − Qf/Qq)
assert 1000 - 700 == 300 and 300 / 1000 == 0.3 and abs((1 - 700 / 1000) - 0.3) < 1e-12
assert round(300 / 700 * 100) == 43                     # o erro: dividir pelo calor jogado fora
assert 800 - 600 == 200 and 200 / 800 == 0.25 and 600 / 800 == 0.75 and 1 - 0.75 == 0.25
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
def barra_calor(c, t, t0, x, y, w, h, util, tu=None, rot_u=None, rot_f=None, size=48):
    """barra com 100 % do calor recebido: a parte útil (fração util) em laranja, à esquerda; o resto em azul. tu = instante da divisão"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, x, y, w, h, 18, E.mix(E.COR, BR, 0.75), q)
    if tu is not None and t >= tu:
        p = ease_io(prog(t, tu, 0.8))
        wu = w * util
        M.rrect(c, x, y, wu, h, 18, E.COR, q)
        M.rrect(c, x + wu, y, (w - wu) * p, h, 18, FRIO, q * 0.9)
        if rot_u:
            E.foco(c, t, tu + 0.3, 0.4, lambda a: centro(c, rot_u, x + wu / 2, y + h / 2 + size * 0.36, size, "g", BR, a))
        if rot_f:
            E.foco(c, t, tu + 0.7, 0.4, lambda a: centro(c, rot_f, x + wu + (w - wu) / 2, y + h / 2 + size * 0.36, size, "g", BR, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(TINTA, q, stroke=4))


def roda(c, t, cx, cy, r, a=1.0, gira=True):
    """roda-d'água com pás, girando"""
    if a <= 0:
        return
    g0 = t * 40 if gira else 0
    c.drawCircle(cx, cy, r, M.paint("#8B5E3C", a, stroke=14))
    c.drawCircle(cx, cy, r * 0.15, M.paint("#6E4A2F", a))
    for k in range(8):
        g = math.radians(g0 + 45 * k)
        x1, y1 = cx + math.cos(g) * r, cy + math.sin(g) * r
        M.line(c, cx, cy, x1, y1, "#6E4A2F", a, 8)
        M.line(c, x1, y1, x1 + math.cos(g) * 40, y1 + math.sin(g) * 40, "#8B5E3C", a, 22)


def queda(c, t, x, y0, y1, a=1.0, largura=46):
    """filete de água caindo"""
    if a <= 0:
        return
    M.rrect(c, x - largura / 2, y0, largura, y1 - y0, largura / 2, AGUA, a * 0.8)
    for k in range(4):
        yy = y0 + ((t * 300 + k * (y1 - y0) / 4) % (y1 - y0))
        c.drawCircle(x, yy, largura * 0.22, M.paint(BR, a * 0.7))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        E.frase(c, t, C["s01.a"], ps("a gasolina queima:", "i", 76) + [("calor", "g", 76, COR)], XE, 260, passo=0.12)
        barra_calor(c, t, C["s01.a"] + 0.4, XE, 340, 1580, 130, 0.25, C["s01.b"], "1/4: movimento", "escapamento e radiador")
        E.frase(c, t, C["s01.b"], ps("só cerca de", "i", 70) + [("um", "g", 70, COR), ("quarto", "g", 70, COR)] + ps("vira movimento", "i", 70), XE, 600, passo=0.1)
        E.frase(c, t, C["s01.d"], [("defeito", "g", 76), ("do", "i", 80), ("motor?", "g", 76)], XE, 760, passo=0.12)
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.pilula(c, "nem o motor perfeito chega a 100 %", W / 2 + 120, 920, 56, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s01.a"] + 0.6, 0.6, lambda a: F.carrinho(c, 1500, 760, 380, a=a))
        return
    promessa(c, t, C, "s02", (("s02.b", "o rendimento"), ("s02.c", "por que nunca 100 %")))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def rend(a, x, y):
        E.formula(c, "f{útil}{total}", x - 20, y + 20, 56, "g", TINTA, a, "center")

    def ciclo_(a, x, y):
        E.formula(c, "ΔU = 0", x - 40, y + 20, 56, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "rendimento:", "útil ÷ total, em %"), ("s03.c", "num ciclo:", "o que entra, sai")), (rend, ciclo_))


# ---------------- a máquina ----------------
MQ = dict(cx=1400, y0=140, y1=940, w=560)


def b_maquina(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("máquina", "g", 90), ("térmica", "g", 90, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s04.a"], ps("transforma", "i", 70) + [("calor", "g", 70, COR)] + ps("em", "i", 70) + [("trabalho", "g", 70)], XE, 400, passo=0.1)
        E.frase(c, t, C["s04.a"] + 1.4, ps("repetindo um ciclo", "i", 60, TINTA2), XE, 490, passo=0.1)
        for i, s in enumerate(("motor de carro", "usina térmica", "locomotiva a vapor")):
            E.foco(c, t, C["s04.a"] + 3.0 + 0.9 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 280 + i * 500, 640, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s04.b"], ps("toda máquina tem", "i", 76) + [("três partes", "g", 76, COR)], XE, 860, passo=0.12)
        return
    T = dict(q=C["s05.a"], Qq=C["s05.b"], m=C["s05.b"] - 0.2, tau=C["s05.c"], f=C["s05.d"], Qf=C["s05.e"])
    maquina(c, t, T, **MQ)
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("1.", "g", 70, COR), ("fonte", "g", 70), ("quente", "g", 70, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s05.a"] + 1.0, ps("algo queima ou ferve", "i", 56, TINTA2), XE + 70, 340, passo=0.08)
        E.foco(c, t, C["s05.b"], 0.4, lambda a: fs(c, "a máquina recebe Q_q", XE + 70, 440, 60, "g", TINTA, a))
        E.frase(c, t, C["s05.c"], [("2.", "g", 70, COR), ("faz", "i", 74), ("o", "i", 74), ("trabalho", "g", 70), ("τ", "g", 70, COR)], XE, 600, passo=0.12)
        E.frase(c, t, C["s05.d"], [("3.", "g", 70, COR), ("fonte", "g", 70), ("fria", "g", 70, FRIO)], XE, 760, passo=0.12)
        E.frase(c, t, C["s05.d"] + 1.0, ps("o ar ou a água de um rio", "i", 56, TINTA2), XE + 70, 840, passo=0.08)
        E.foco(c, t, C["s05.e"], 0.4, lambda a: fs(c, "recebe o resto: Q_f", XE + 70, 940, 60, "g", TINTA, a))
        return
    E.frase(c, t, C["s06.a"], ps("no ciclo,", "i", 70) + [("ΔU = 0", "g", 70, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s06.b"], ps("tudo o que entra,", "i", 70) + [("sai", "g", 70, COR)], XE, 380, passo=0.12)
    fs_em(c, t, C["s06.c"], "Q_q = τ + Q_f", XE, 560, 110)
    fs_em(c, t, C["s06.d"], "τ = Q_q − Q_f", XE, 740, 110, cor=COR)
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.pilula(c, "quantidades, sem sinal", XE + 330, 900, 50, "g", fundo=TINTA, a=a))


# ---------------- rendimento ----------------
def b_rendimento(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("rendimento:", "i", 76) + [("η", "g", 96, COR)], XE, 240, passo=0.12)
        E.foco(c, t, C["s07.a"] + 0.5, 0.4, lambda a: E.escreve(c, "a letra grega eta", XE + 600, 240, 50, "i", TINTA2, a))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "η = f{útil}{total}", XE, 470, 110, "g", TINTA, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: E.formula(c, "útil = τ", XE + 820, 420, 70, "g", TINTA, a))
        E.foco(c, t, C["s07.d"], 0.4, lambda a: fs(c, "total = Q_q", XE + 820, 540, 70, "g", COR, a))
        if t >= C["s07.e"]:
            fs_em(c, t, C["s07.e"], "η = f{τ}{Q_q}", XE, 800, 150)
            for i, (l, n) in enumerate((("τ", "trabalho (J)"), ("Q_q", "calor da fonte quente (J)"))):
                E.foco(c, t, C["s07.e"] + 0.6 + 0.4 * i, 0.4, lambda a, l=l, n=n, i=i: (fs(c, l, XE + 600, 740 + i * 90, 60, "g", COR, a),
                                                                                       E.escreve(c, n, XE + 720, 740 + i * 90, 54, "i", TINTA, a)))
        return
    T = dict(q=C["s08.a"], m=C["s08.a"], f=C["s08.b"], Qq=C["s08.a"] + 0.2, Qf=C["s08.b"] + 0.2, tau=C["s08.c"])
    maquina(c, t, T, cx=1420, y0=160, y1=920, w=520, rot=dict(Qq="1.000 J", Qf="700 J", tau="300 J"))
    E.frase(c, t, C["s08"], ps("exemplo", "i", 66, TINTA2), XE, 220)
    fs_em(c, t, C["s08.a"], "Q_q = 1.000 J", XE, 360, 70, cor=COR)
    fs_em(c, t, C["s08.b"], "Q_f = 700 J", XE, 470, 70, cor=FRIO)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.formula(c, "τ = 1.000 − 700 = 300 J", XE, 600, 64, "g", TINTA, a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.formula(c, "η = f{300}{1.000} = 0,3", XE, 760, 72, "g", TINTA, a))
    bola_txt(c, t, C["s08.f"], "30 %", 520, 940, 100, 64)


# ---------------- segunda lei ----------------
def b_segunda(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"] + 1.0, [("segunda", "g", 90, COR), ("lei", "g", 90)], XE, 250, passo=0.12)
        E.frase(c, t, C["s09.a"], ps("nenhuma máquina, em ciclo,", "i", 66), XE, 400, passo=0.08)
        E.frase(c, t, C["s09.a"] + 1.4, ps("transforma", "i", 66) + [("todo", "g", 66, ERRADO)] + ps("o calor em trabalho", "i", 66), XE, 490, passo=0.08)
        barra_calor(c, t, C["s09.a"] + 2.4, XE, 620, 1580, 120, 0.6, C["s09.b"], "trabalho", "para a fonte fria")
        E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.pilula(c, "sempre sobra calor para a fonte fria", W / 2, 880, 54, "g", fundo=FRIO, a=a))
        return
    if t < C["s11"]:
        # a roda-d'água
        E.frase(c, t, C["s10.a"], [("roda-d'água", "g", 84, COR)], XE, 230)
        x = 1180
        E.foco(c, t, C["s10.a"], 0.5, lambda a: (M.rrect(c, 960, 200, 360, 70, 12, AGUA, a), centro(c, "água no alto", 1140, 175, 44, "i", TINTA2, a)))
        E.foco(c, t, C["s10.b"], 0.4, lambda a: queda(c, t, x + 100, 270, 930, a))
        E.foco(c, t, C["s10.a"] + 0.3, 0.5, lambda a: roda(c, t, x + 230, 600, 190, a, t >= C["s10.b"]))
        E.foco(c, t, C["s10.c"], 0.5, lambda a: (M.rrect(c, 1000, 930, 520, 70, 12, AGUA, a), centro(c, "chega lá embaixo", 1260, 1040, 44, "i", TINTA2, a)))
        E.frase(c, t, C["s10.b"], ps("gira porque a água", "i", 60) + [("cai", "g", 60, COR)], XE, 360, passo=0.08)
        E.frase(c, t, C["s10.c"], ps("a água", "i", 60) + [("não some", "g", 60)], XE, 460, passo=0.08)
        E.frase(c, t, C["s10.d"], ps("o calor também", "i", 60) + [("desce", "g", 60, COR)] + ps("do quente ao frio", "i", 60), XE, 620, passo=0.08)
        E.frase(c, t, C["s10.e"], ps("a máquina aproveita a passagem", "i", 58), XE, 740, passo=0.08)
        E.frase(c, t, C["s10.f"], ps("mas o calor precisa", "i", 58) + [("chegar", "g", 58, FRIO)], XE, 840, passo=0.08)
        E.frase(c, t, C["s10.f"] + 1.2, [("à", "i", 58), ("fonte", "g", 58, FRIO), ("fria", "g", 58, FRIO)], XE, 920, passo=0.08)
        return
    T = dict(q=C["s11"], m=C["s11"], f=C["s11"], Qq=C["s11"] + 0.3, tau=C["s11"] + 0.5)
    maquina(c, t, T, cx=1420, y0=160, y1=920, w=520)
    if t >= C["s11.a"] + 0.5:
        E.risco(c, 1160, 920, 1680, 780, t, C["s11.a"] + 0.5, largura=12)
    E.frase(c, t, C["s11.a"], ps("sem fonte fria,", "i", 76) + [("sem", "g", 72), ("passagem", "g", 72)], XE, 300, passo=0.1)
    E.frase(c, t, C["s11.b"], ps("a máquina", "i", 80) + [("para", "g", 84, ERRADO)], XE, 440, passo=0.12)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "η < 100 %", XE, 700, 150, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("dividir pelo calor", "i", 76) + [("errado", "g", 76, ERRADO)], XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "f{300}{700} ≈ 43 %", W / 2, 470, 130, "g", ERRADO, a, "center"))
    if t >= C["s12.c"] + 0.8:
        E.risco(c, W / 2 - 360, 500, W / 2 + 360, 360, t, C["s12.c"] + 0.8, largura=12)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "700 J = o que foi jogado fora", W / 2, 680, 56, "g", fundo=FRIO, a=a))
    E.foco(c, t, C["s12.e"], 0.4, lambda a: fs(c, "o total é o que entrou: Q_q = 1.000 J", W / 2, 860, 76, "g", CERTO, a, "center"))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 70, CLARO), W / 2, 160, "center")
    if t < C["s14"]:
        E.foco(c, t, C["s13.a"], 0.5, lambda a: fs(c, "η = 1 − f{Q_f}{Q_q}", W / 2, 420, 150, "g", BR, a, "center"))
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.formula(c, "f{700}{1.000} = 0,7", W / 2, 640, 84, "g", E.CLARO, a, "center"))
        E.foco(c, t, C["s13.c"], 0.4, lambda a: E.formula(c, "1 − 0,7 = 0,3", W / 2, 800, 90, "g", BR, a, "center"))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "30 %, sem calcular o trabalho", W / 2, 930, 56, "g", fundo=E.COR, a=a))
        return
    E.foco(c, t, C["s14.a"], 0.4, lambda a: fs(c, "τ = Q_q − Q_f", W / 2, 340, 90, "g", E.CLARO, a, "center"))
    E.foco(c, t, C["s14.b"], 0.4, lambda a: fs(c, "η = f{Q_q − Q_f}{Q_q} = 1 − f{Q_f}{Q_q}", W / 2, 520, 96, "g", BR, a, "center"))
    if t >= C["s14.c"]:
        q = ep(t, C["s14.c"], 0.5)
        x, y, w, h = 360, 660, 1200, 100
        M.rrect(c, x, y, w * 0.3, h, 16, E.COR, q)
        M.rrect(c, x + w * 0.3, y, w * 0.7 * ease_io(prog(t, C["s14.c"] + 0.3, 0.8)), h, 16, FRIO, q)
        E.foco(c, t, C["s14.c"] + 0.8, 0.4, lambda a: (centro(c, "30 % sobram", x + w * 0.15, y + 66, 46, "g", BR, a),
                                                      centro(c, "70 % jogados fora", x + w * 0.65, y + 66, 46, "g", BR, a)))
    E.frase(c, t, C["s14.d"], [("não", "g", 58, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("a questão já dá o trabalho", "i", 62, CLARO), W / 2, 900, "center", 0.1)
    E.foco(c, t, C["s14.d"] + 2.4, 0.4, lambda a: fs(c, "use f{τ}{Q_q}", W / 2, 1010, 64, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("recebe", "i", 74) + [("800 J", "g", 72, COR)] + ps("da fonte quente", "i", 74), XE, 360, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("joga", "i", 74) + [("600 J", "g", 72, FRIO)] + ps("na fonte fria", "i", 74), XE, 480, passo=0.1)
    E.frase(c, t, C["s15.c"], [("τ", "g", 80, COR), ("=", "g", 80), ("?", "g", 80, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s15.d"], [("η", "g", 80, COR), ("=", "g", 80), ("?", "g", 80, COR)], XE, 800, passo=0.12)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)
    else:
        maquina(c, t, dict(q=C["s15.a"], m=C["s15.a"], Qq=C["s15.a"] + 0.2, f=C["s15.b"], Qf=C["s15.b"] + 0.2, tau=C["s15.c"]),
                cx=1460, y0=160, y1=920, w=480, rot=dict(Qq="800 J", Qf="600 J", tau="?"))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s18"]:
        passos(c, t, [(C["s17.a"], "tudo o que entra, sai", TINTA2), (C["s17.b"], "τ = 800 − 600 = 200 J", TINTA), (C["s17.c"], "η = f{200}{800}", TINTA)], XE, 260, 150, 72)
        E.foco(c, t, C["s17.d"], 0.4, lambda a: E.formula(c, "= f{1}{4}", XE + 330, 560, 72, "g", TINTA, a))
        bola_txt(c, t, C["s17.e"], "25 %", 1300, 560, 160, 90)
        return
    E.frase(c, t, C["s18"], ps("com o atalho", "i", 66, TINTA2), XE, 220)
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.formula(c, "f{600}{800} = f{3}{4} = 75 % jogados fora", XE, 380, 72, "g", FRIO, a))
    barra_calor(c, t, C["s18.a"] + 0.5, XE, 520, 1580, 120, 0.25, C["s18.a"] + 0.9, "25 %", "75 %")
    bola_txt(c, t, C["s18.b"], "25 %", W / 2, 840, 120, 70)
    E.foco(c, t, C["s18.c"], 0.6, lambda a: F.carrinho(c, 1500, 940, 300, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def r():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, s) in enumerate((("s19.a", "recebe Q_q, faz τ, joga Q_f fora"), ("s19.b", "η = f{τ}{Q_q}"), ("s19.c", "segunda lei: η < 100 %"))):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            fs_em(c, t, C[k] + 0.1, s, 360, y, 70, cor=COR if i == 1 else TINTA)
    E.saida(c, t, C["s20"] - 0.1, r)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("o", "i", 90), ("rendimento", "g", 90, COR), ("máximo", "g", 90, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s20.b"], ps("só com as temperaturas das fontes", "i", 60), XE, 530, passo=0.08)
    if t >= C["s20.b"]:
        F.termometro(c, t, C["s20.b"] + 0.2, 500, 960, 300, 85, 0, 100)
        F.termometro(c, t, C["s20.b"] + 0.5, 800, 960, 300, 20, 0, 100, cor=FRIO)
    inscreva(c, t, C["s20.c"], C["s20.d"])


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, maquina=b_maquina, rendimento=b_rendimento, segunda=b_segunda, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
