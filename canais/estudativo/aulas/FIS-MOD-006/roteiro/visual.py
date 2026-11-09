"""Visual — Estudativo · FIS-MOD-006: semicondutores e transistores.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Aqui: cristal de silício = rede de
esferas cinza ligadas por pares de elétrons (pontinhos azuis); átomo dopante em laranja; elétron livre = elétron azul
(eletron); LACUNA = círculo tracejado vazio. Tipo n em azul (F.NEG), tipo p em laranja (E.COR). Diodo = seta com barra em
tinta, com os componentes de circuito de fisica.py (F.pilha, F.lampada, F.fio, F.corrente). Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-006_semicondutores_e_transistores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("materiais", "dopagem", "diodo", "transistor", "erro", "atalho", "questao", "fim"))

# todas as contas (e contagens) da aula
VAL = dict(Si=4, P=5, As=5, B=3)
assert VAL["P"] - VAL["Si"] == 1 and VAL["Si"] - VAL["B"] == 1        # fósforo sobra 1 (n); boro falta 1 (p)
assert VAL["As"] - VAL["Si"] == 1                                      # questão: arsênio → tipo n
assert 4 * 1 == 4                                                      # cada Si divide 4 elétrons com 4 vizinhos
assert 1947 + 9 == 1956                                                # transistor (1947); Nobel de 1956
assert 1e10 > 1e9                                                      # mais de dez bilhões de transistores


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha Física Moderna (o mesmo em todas as FIS-MOD; candidatas a fisica.py) ----------------
BR = "#FFFFFF"
LUZ = "#FFB000"   # brilho de fonte de luz (o mesmo da Óptica)
UV = "#8B3CF7"    # ultravioleta
VERM = "#D0202A"  # luz vermelha (não é o vermelho de "errado": vem sempre com a palavra "vermelha")


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cor_luz(nm):
    """cor aproximada de uma luz visível pelo comprimento de onda em nanômetros (380 a 750)"""
    pts = ((380, (0.55, 0.0, 0.9)), (440, (0.25, 0.1, 1.0)), (490, (0.0, 0.65, 1.0)), (510, (0.0, 0.85, 0.35)),
           (580, (1.0, 0.9, 0.0)), (620, (1.0, 0.45, 0.0)), (660, (0.95, 0.1, 0.05)), (750, (0.6, 0.0, 0.0)))
    nm = max(380, min(750, nm))
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        if nm <= b:
            f = (nm - a) / (b - a)
            r, g, bb = (ca[i] + (cb[i] - ca[i]) * f for i in range(3))
            return "#%02X%02X%02X" % (int(r * 255), int(g * 255), int(bb * 255))
    return "#990000"


def pacote(c, x, y, ang, cor, a=1.0, n=3, amp=22, lam=34, largura=5):
    """um fóton parado: n ondas com envelope, centradas em (x, y), andando no ângulo ang (graus, 0 = direita, 90 = cima)"""
    if a <= 0:
        return
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    nx, ny = -uy, ux
    L = n * lam
    path = skia.Path()
    for i in range(61):
        s = -L / 2 + L * i / 60
        env = math.sin(math.pi * i / 60)
        d = amp * env * math.sin(2 * math.pi * s / lam)
        px, py = x + ux * s + nx * d, y + uy * s + ny * d
        path.moveTo(px, py) if i == 0 else path.lineTo(px, py)
    c.drawPath(path, M.paint(cor, a, stroke=largura, cap_round=True))
    F._cabeca(c, x + ux * (L / 2 + 16), y + uy * (L / 2 + 16), ux, uy, 20, cor, a)


def foton(c, t, t0, A, B, cor=None, d=1.0, n=3, amp=22, lam=34, largura=5, fica=False):
    """fóton que viaja de A até B entre t0 e t0 + d; some ao chegar (fica=True: para em B)"""
    if t < t0:
        return
    p = ease_io(prog(t, t0, d))
    if p >= 1 and not fica:
        return
    ang = math.degrees(math.atan2(-(B[1] - A[1]), B[0] - A[0]))
    a = min(1.0, prog(t, t0, 0.2)) * (1.0 if fica else 1 - max(0.0, (p - 0.85) / 0.15))
    pacote(c, lerp(A[0], B[0], p), lerp(A[1], B[1], p), ang, cor or E.COR, a, n, amp, lam, largura)


def jorro(c, t, t0, A, B, cor, periodo=0.5, d=1.1, t1=1e9, **kw):
    """fótons saindo de A para B um atrás do outro, de t0 até t1"""
    if t < t0:
        return
    k0 = int(max(0.0, t - t0 - d) // periodo)
    k = k0
    while t0 + k * periodo <= min(t, t1):
        foton(c, t, t0 + k * periodo, A, B, cor, d, **kw)
        k += 1


def eletron(c, cx, cy, r=26, a=1.0):
    """elétron: esferinha azul com o sinal de menos"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, F.NEG, a)
    M.line(c, cx - r * 0.42, cy, cx + r * 0.42, cy, BR, a, max(3, r * 0.2))


def lampada_fonte(c, cx, cy, r, cor=LUZ, a=1.0, t=0.0):
    """fonte de luz: esfera com brilho pulsando (a mesma linguagem da Óptica)"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    k = r * (2.3 + 0.12 * math.sin(t * 4))
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), k, [M.hexc(cor, 0.55 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, k, p)
    E.bola(c, cx, cy, r, cor, a)


def sol(c, cx, cy, r, a=1.0, t=0.0):
    """o Sol: fonte âmbar com raios em volta"""
    if a <= 0:
        return
    for i in range(12):
        g = math.radians(i * 30 + t * 8)
        M.line(c, cx + math.cos(g) * r * 1.25, cy + math.sin(g) * r * 1.25, cx + math.cos(g) * r * 1.6, cy + math.sin(g) * r * 1.6, LUZ, a, 8)
    lampada_fonte(c, cx, cy, r, LUZ, a, t)


def constante(c, t, t0, x, y, nome, simbolo, valor, size=64, w=None):
    """cartão de constante física: nome em itálico, símbolo laranja e valor em notação científica"""
    w = w or max(620, E.formula(None, valor, 0, 0, size, "g", a=0) + size * 2.4)
    hh = size * 3.1
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.escreve(c, nome, x + 34, y + size * 1.0, size * 0.62, "i", TINTA2, a))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.formula(c, simbolo, x + 34, y + size * 2.3, size, "g", COR, a),
                                            E.formula(c, valor, x + 34 + E.formula(None, simbolo + " ", 0, 0, size, "g", a=0), y + size * 2.3, size, "g", TINTA, a)))


def bola_txt(c, t, t0, v, u, cx, cy, r, size, cor=None):
    """resposta na esfera: número pesado e unidade menor"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def promessa(c, t, C, cena, itens):
    """tela do "até o fim da aula": órbita à direita e três itens numerados. itens = [(cue, texto)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.4 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


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
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, y0=350, dy=170):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


def inscreva(c, t, C, cena):
    """inscreva-se com o cursor e "bons estudos!" (as duas últimas marcas da cena final)"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def placa_metal(c, x, y, w, h, a=1.0, rotulo=None):
    """placa de metal vista de lado: retângulo cinza com reflexo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 10, "#9AA0A8", a)
    M.rrect(c, x + 8, y + 8, w - 16, h * 0.18, 6, "#C9CED4", a)
    if rotulo:
        centro(c, rotulo, x + w / 2, y + h - 22, min(48, h * 0.4), "b", TINTA, a)


def bola_txt_f(c, t, t0, v, u, cx, cy, h, size, cor=None):
    """resultado com potência de dez numa pílula larga laranja (a esfera não cabe a notação científica)"""
    w = E.formula(None, v + " " + u, 0, 0, size, "g", a=0) + size * 1.4

    def d(a):
        q = ease_back(prog(t, t0, 0.5))
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w * q / 2, cy - h / 2, w * q, h), h / 2, h / 2)
        c.drawRRect(rr, M.paint(cor or E.COR, a))
        wv = E.formula(None, v + " ", 0, 0, size, "g", a=0)
        x0 = cx - (wv + E.formula(None, u, 0, 0, size * 0.75, "b", a=0)) / 2
        E.formula(c, v, x0, cy + size * 0.36, size, "g", E.SOBRE, a)
        E.formula(c, u, x0 + wv, cy + size * 0.36, size * 0.75, "b", E.SOBRE, a)
    E.foco(c, t, t0, 0.5, d)


# ---------------- peças desta aula ----------------
def cristal(c, t, t0, x0, y0, n, m, passo, dop=None, tipo=None, t_dop=None, a=1.0):
    """rede de silício n × m; dop = (i, j) do átomo dopante; tipo "n" (elétron sobrando) ou "p" (lacuna)"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    r = passo * 0.24
    for i in range(n):
        for j in range(m):
            x, y = x0 + i * passo, y0 + j * passo
            if i < n - 1:
                M.line(c, x + r, y, x + passo - r, y, TINTA2, q * 0.5, 4)
                falta = dop == (i, j) and tipo == "p" and t_dop is not None and t >= t_dop
                for k, dy in enumerate((-7, 7)):
                    if not (falta and k == 1):
                        c.drawCircle(x + passo / 2, y + dy, 6, M.paint(F.NEG, q))
                if falta:
                    pt = M.paint(E.COR, q * ep(t, t_dop, 0.4), stroke=3)
                    pt.setPathEffect(skia.DashPathEffect.Make([5, 4], 0))
                    c.drawCircle(x + passo / 2, y + 7, 12, pt)
            if j < m - 1:
                M.line(c, x, y + r, x, y + passo - r, TINTA2, q * 0.5, 4)
                for dx in (-7, 7):
                    c.drawCircle(x + dx, y + passo / 2, 6, M.paint(F.NEG, q))
    for i in range(n):
        for j in range(m):
            x, y = x0 + i * passo, y0 + j * passo
            e_dop = dop == (i, j) and t_dop is not None and t >= t_dop
            cor = E.COR if e_dop else "#8C96A3"
            E.bola(c, x, y, r, cor, q)
            s = ("P" if tipo == "n" else "B") if e_dop else "Si"
            centro(c, s, x, y + r * 0.35, r * 0.9, "g", BR, q)
    if dop and tipo == "n" and t_dop is not None and t >= t_dop + 0.6:
        x, y = x0 + dop[0] * passo, y0 + dop[1] * passo
        u = (t - t_dop - 0.6) * 0.8
        eletron(c, x + passo * 0.4 + 30 * math.sin(u * 2), y - passo * 0.4 + 18 * math.cos(u * 3), 18, ep(t, t_dop + 0.6, 0.4))


def diodo(c, A, B, a=1.0, cor=TINTA, k=36):
    """símbolo do diodo: seta (triângulo) de A para B com a barra do lado de B"""
    if a <= 0:
        return
    ux, uy = (B[0] - A[0]), (B[1] - A[1])
    L = math.hypot(ux, uy); ux, uy = ux / L, uy / L
    nx, ny = -uy, ux
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    M.line(c, A[0], A[1], mx - ux * k, my - uy * k, cor, a, 6)
    M.line(c, mx + ux * k, my + uy * k, B[0], B[1], cor, a, 6)
    p = skia.Path()
    p.moveTo(mx - ux * k + nx * k, my - uy * k + ny * k); p.lineTo(mx - ux * k - nx * k, my - uy * k - ny * k); p.lineTo(mx + ux * k, my + uy * k); p.close()
    c.drawPath(p, M.paint(cor, a))
    M.line(c, mx + ux * k + nx * k, my + uy * k + ny * k, mx + ux * k - nx * k, my + uy * k - ny * k, cor, a, 7)


def bloco_pn(c, x, y, w, h, camadas, a=1.0, size=60):
    """faixa de semicondutor dividida em camadas, como ("p", "n") ou ("n", "p", "n")"""
    if a <= 0:
        return
    ww = w / len(camadas)
    for i, s in enumerate(camadas):
        cor = E.mix(E.COR, "#FFFFFF", 0.35) if s == "p" else E.mix(F.NEG, "#FFFFFF", 0.35)
        M.rrect(c, x + i * ww, y, ww, h, 10, cor, a)
        centro(c, s, x + i * ww + ww / 2, y + h / 2 + size * 0.36, size, "g", BR, a)


def circuito(c, t, t0, x, y, w, h, direto=True, ta=None):
    """pilha à esquerda, diodo em cima, lâmpada à direita; direto=True: lado p no positivo, a lâmpada acende em ta"""
    A, B, Cc, D = (x, y + h), (x, y), (x + w, y), (x + w, y + h)
    F.fio(c, t, t0, [A, B, Cc, D, A], d=0.8)
    # direto: o + da pilha em cima, ligado ao lado p (a base da seta); invertido: o + embaixo
    F.pilha(c, t, t0 + 0.2, (x, y + h * 0.7), (x, y + h * 0.3)) if direto else F.pilha(c, t, t0 + 0.2, (x, y + h * 0.3), (x, y + h * 0.7))
    if t >= t0 + 0.4:
        diodo(c, (x + w * 0.3, y), (x + w * 0.7, y), ep(t, t0 + 0.4, 0.4))
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: (centro(c, "p", x + w * 0.38, y - 50, 40, "g", COR, a), centro(c, "n", x + w * 0.62, y - 50, 40, "g", F.NEG, a)))
    F.lampada(c, t, t0 + 0.5, (x + w, y + h * 0.25), (x + w, y + h * 0.75), acesa=ta)
    if direto and ta is not None and t >= ta:
        F.corrente(c, t, ta, [A, B, Cc, D, A], E.COR, vel=140, fecha=True)


def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("o processador do celular:", "i", 66), XE, 240, passo=0.1)
        E.frase(c, t, C["s01.a"] + 1.2, [("+ de 10 bilhões", "g", 90, COR)] + ps("de chaves", "i", 76), XE, 380, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("ligando e desligando", "i", 60) + [("bilhões de vezes por segundo", "g", 56)], XE, 520, passo=0.08)
        # chip com chavinhas piscando
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: M.rrect(c, 1180, 620, 520, 380, 30, "#2A2A30", a))
        if t >= C["s01.a"] + 0.6:
            for i in range(10):
                for j in range(6):
                    on = (math.sin(t * 9 + i * 1.7 + j * 2.3) > 0) if t >= C["s01.b"] else False
                    M.rrect(c, 1215 + i * 47, 650 + j * 55, 30, 30, 6, E.COR if on else "#4A4A55", ep(t, C["s01.a"] + 0.6, 0.4))
        E.frase(c, t, C["s01.c"], ps("feitas de", "i", 70) + [("silício", "g", 76, COR)], XE, 720, passo=0.12)
        E.frase(c, t, C["s01.c"] + 1.2, ps("o elemento que está na areia", "i", 56, TINTA2), XE, 820, passo=0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a dopagem"), ("s02.b", "o diodo, mão única"), ("s02.c", "o transistor, a chave")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        E.formula(c, "R = ρ · f{L}{A}", x - 30, y + 20, 56, "g", TINTA, a, "center")

    def f2(a, x, y):
        E.bola(c, x - 20, y, 26, "#8C96A3", a)
        for k in range(4):
            g = math.radians(45 + 90 * k)
            c.drawCircle(x - 20 + math.cos(g) * 60, y + math.sin(g) * 60, 9, M.paint(F.NEG, a))
        c.drawCircle(x - 20, y, 60, M.paint(TINTA2, a * 0.5, stroke=2))
    lembrete2(c, t, C, "s03", (("s03.b", "a resistividade:", "o quanto atrapalha"), ("s03.c", "camada de valência:", "a última camada do átomo")), (f1, f2))


# ---------------- condutor, isolante, semicondutor ----------------
def b_materiais(c, t, C, b):
    def s04():
        for i, (k, nome, desc, cor, kk) in enumerate((("s04.a", "condutor", "metal: ρ baixa", CERTO, "s04.b"), ("s04.c", "isolante", "borracha: ρ enorme", ERRADO, "s04.d"),
                                                      ("s04.e", "semicondutor", "no meio do caminho", E.COR, "s04.f"))):
            x = 180 + 540 * i
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, x, 300, 480, 520, p, prog_=p)
            if t < C[k]:
                continue
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, x=x, desc=desc: centro(c, desc, x + 240, 400, 42, "b", TINTA, a))
            E.foco(c, t, C[kk], 0.5, lambda a, x=x, nome=nome, cor=cor: E.pilula(c, nome, x + 240, 750, 50, "g", fundo=cor, a=a))
            n_e = (10, 0, 2)[i]
            for e in range(n_e):
                u = (t * (0.35 + 0.05 * e) + e * 0.37) % 1
                eletron(c, x + 40 + 400 * u, 480 + 40 * (e % 5) + 10 * math.sin(t * 3 + e), 14, ep(t, C[k] + 0.4, 0.4))
            if i == 1:
                E.foco(c, t, C[k] + 0.4, 0.4, lambda a, x=x: [eletron(c, x + 80 + 80 * e, 560, 14, a * 0.5) for e in range(5)])
        E.frase(c, t, C["s04.f"], ps("o mais usado:", "i", 66) + [("silício", "g", 72, COR)], W / 2, 960, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    cristal(c, t, C["s05.a"], 1000, 300, 4, 4, 190)
    E.frase(c, t, C["s05.a"], [("silício:", "g", 70), ("4", "g", 90, COR)] + ps("elétrons na valência", "i", 64), XE, 260, passo=0.12)
    E.frase(c, t, C["s05.b"], ps("divide com", "i", 64) + [("4 vizinhos", "g", 64)], XE, 400, passo=0.12)
    E.frase(c, t, C["s05.c"], ps("todo mundo", "i", 64) + [("preso", "g", 64)] + ps("nas ligações", "i", 64), XE, 540, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("pouquíssimos elétrons livres", "i", 60), XE, 680, passo=0.08)
    E.foco(c, t, C["s05.d"] + 1.2, 0.4, lambda a: E.pilula(c, "silício puro conduz mal", XE + 330, 820, 48, "g", fundo=TINTA, a=a))


# ---------------- dopagem ----------------
def b_dopagem(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], [("dopagem", "g", 90, COR)], XE, 220)
        E.frase(c, t, C["s06.b"], ps("pouquíssimos átomos:", "i", 60) + [("1 em 1 milhão", "g", 60)], XE, 330, passo=0.1)
        cristal(c, t, C["s06"], 1150, 330, 4, 4, 170, dop=(1, 1), tipo="n", t_dop=C["s06.c"])
        E.frase(c, t, C["s06.c"], [("5", "g", 90, COR)] + ps("elétrons, como o", "i", 60) + [("fósforo", "g", 60, COR)], XE, 500, passo=0.12)
        E.frase(c, t, C["s06.d"], [("4", "g", 70)] + ps("nas ligações", "i", 60), XE, 610, passo=0.12)
        E.frase(c, t, C["s06.e"], [("1", "g", 70, F.NEG)] + ps("sobra livre", "i", 60), XE, 710, passo=0.12)
        E.frase(c, t, C["s06.f"], ps("sobra elétron, negativo:", "i", 56), XE, 840, passo=0.1)
        E.foco(c, t, C["s06.g"], 0.5, lambda a: E.pilula(c, "tipo n", XE + 160, 940, 64, "g", fundo=F.NEG, a=a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    cristal(c, t, C["s07"], 1150, 330, 4, 4, 170, dop=(1, 1), tipo="p", t_dop=C["s07.a"])
    E.frase(c, t, C["s07.a"], [("3", "g", 90, COR)] + ps("elétrons, como o", "i", 60) + [("boro", "g", 60, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("falta", "i", 64) + [("1", "g", 70, COR)] + ps("para fechar", "i", 64), XE, 380, passo=0.12)
    E.frase(c, t, C["s07.c"], ps("o buraco:", "i", 64) + [("lacuna", "g", 70, COR)], XE, 510, passo=0.12)
    if t >= C["s07.d"]:  # um elétron vizinho pula para a lacuna: a lacuna anda para o outro lado
        u = ease_io(prog(t, C["s07.d"], 1.2))
        x0, y0 = 1150 + 170 * 1.5, 330 + 170 * 1 + 7
        eletron(c, lerp(x0 + 170, x0, u), y0, 12, 1.0)
        F.seta(c, x0 + 160, y0 + 60, x0 + 20, y0 + 60, F.NEG, ep(t, C["s07.d"], 0.3), 5, None, u)
        F.seta(c, x0 + 20, y0 - 60, x0 + 160, y0 - 60, E.COR, ep(t, C["s07.d"] + 0.6, 0.3), 5, None, ease_io(prog(t, C["s07.d"] + 0.6, 0.8)))
    E.frase(c, t, C["s07.d"], ps("a lacuna anda ao contrário do elétron", "i", 52), XE, 640, passo=0.07)
    E.frase(c, t, C["s07.e"], ps("como uma", "i", 60) + [("carga positiva", "g", 60, COR)], XE, 750, passo=0.1)
    E.foco(c, t, C["s07.f"], 0.5, lambda a: E.pilula(c, "tipo p", XE + 160, 900, 64, "g", fundo=E.COR, a=a))


# ---------------- diodo ----------------
def b_diodo(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], [("p", "g", 80, COR), ("+", "g", 80, TINTA2), ("n", "g", 80, F.NEG), ("=", "g", 80, TINTA2)], XE, 220, passo=0.12)
        E.frase(c, t, C["s08.a"], [("diodo", "g", 90, COR)], XE + 420, 220)
        E.foco(c, t, C["s08.a"], 0.5, lambda a: bloco_pn(c, 1150, 140, 520, 120, ("p", "n"), a))
        E.frase(c, t, C["s08.b"], [("p", "g", 64, COR)] + ps("no positivo:", "i", 60), XE, 420, passo=0.12)
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "a corrente passa", XE + 220, 520, 48, "g", fundo=CERTO, a=a))
        circuito(c, t, C["s08.b"], 1050, 360, 520, 260, True, C["s08.c"])
        E.frase(c, t, C["s08.d"], ps("inverta a pilha:", "i", 60), XE, 720, passo=0.12)
        E.foco(c, t, C["s08.e"], 0.5, lambda a: E.pilula(c, "a corrente para", XE + 220, 820, 48, "g", fundo=ERRADO, a=a))
        circuito(c, t, C["s08.d"], 1050, 720, 520, 260, False, None)
        E.foco(c, t, C["s08.f"], 0.5, lambda a: E.pilula(c, "rua de mão única", 1310, 1030, 46, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], ps("no circuito:", "i", 70) + [("seta com barra", "g", 70)], XE, 230, passo=0.12)
    E.foco(c, t, C["s09.a"] + 0.6, 0.5, lambda a: diodo(c, (700, 520), (1220, 520), a, TINTA, 90))
    if t >= C["s09.b"]:
        F.seta(c, 760, 680, 1160, 680, E.COR, 1.0, 9, None, ease_io(prog(t, C["s09.b"], 0.6)))
        E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: centro(c, "sentido da corrente", 960, 760, 48, "i", TINTA, a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: (centro(c, "lado n", 1055, 400, 50, "g", F.NEG, a), centro(c, "lado p", 870, 400, 50, "g", COR, a)))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: lampada_fonte(c, 1600, 560, 60, E.COR, a, t))
    E.frase(c, t, C["s09.d"], [("LED", "g", 70, COR)] + ps("é um diodo que solta luz", "i", 60), XE, 900, passo=0.1)


# ---------------- transistor ----------------
def b_transistor(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10.a"], ps("três camadas:", "i", 66) + [("n p n", "g", 70)], XE, 230, passo=0.12)
        E.frase(c, t, C["s10.b"], [("transistor", "g", 90, COR)], XE, 360)
        x, y, w, h = 1000, 360, 660, 140
        E.foco(c, t, C["s10.a"] + 0.3, 0.5, lambda a: bloco_pn(c, x, y, w, h, ("n", "p", "n"), a))
        base_on = t >= C["s10.f"]
        if t >= C["s10.c"]:
            F.fio(c, t, C["s10.c"], [(x - 120, y + h / 2), (x, y + h / 2)], d=0.4)
            F.fio(c, t, C["s10.c"], [(x + w, y + h / 2), (x + w + 120, y + h / 2)], d=0.4)
        if t >= C["s10.d"]:
            F.fio(c, t, C["s10.d"], [(x + w / 2, y + h), (x + w / 2, y + h + 200)], d=0.4)
            E.foco(c, t, C["s10.d"] + 0.3, 0.4, lambda a: E.escreve(c, "base", x + w / 2 + 30, y + h + 160, 50, "g", TINTA, a))
        if base_on:
            F.corrente(c, t, C["s10.f"], [(x + w / 2, y + h + 200), (x + w / 2, y + h)], E.COR, vel=60, fecha=False)
            F.corrente(c, t, C["s10.f"] + 0.3, [(x - 120, y + h / 2), (x + w + 120, y + h / 2)], E.COR, vel=180, fecha=False)
        E.frase(c, t, C["s10.c"], ps("a corrente principal só passa se", "i", 54), XE, 520, passo=0.07)
        E.frase(c, t, C["s10.d"], ps("chegar", "i", 60) + [("corrente na base", "g", 60, COR)], XE, 620, passo=0.1)
        E.frase(c, t, C["s10.e"], [("sem:", "g", 60, ERRADO)] + ps("chave aberta, nada passa", "i", 60), XE, 780, passo=0.1)
        E.frase(c, t, C["s10.f"], [("com:", "g", 60, CERTO)] + ps("a chave fecha", "i", 60), XE, 890, passo=0.1)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], ps("corrente pequena controla", "i", 62) + [("corrente grande", "g", 62, COR)], XE, 220, passo=0.1)
    E.frase(c, t, C["s11.b"], [("amplifica,", "g", 64)] + ps("como no rádio", "i", 64), XE, 330, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("chave aberta e fechada:", "i", 62), XE, 480, passo=0.1)
    E.foco(c, t, C["s11.c"] + 1.0, 0.5, lambda a: (E.bola(c, XE + 760, 460, 54, TINTA, a), centro(c, "0", XE + 760, 484, 64, "g", BR, a),
                                                  E.bola(c, XE + 900, 460, 54, E.COR, a), centro(c, "1", XE + 900, 484, 64, "g", BR, a)))
    E.frase(c, t, C["s11.d"], [("1947,", "g", 80, COR)] + ps("nos Estados Unidos", "i", 64), XE, 680, passo=0.12)
    E.frase(c, t, C["s11.e"], ps("hoje:", "i", 62) + [("bilhões num chip", "g", 62)] + ps("do tamanho de uma unha", "i", 62), XE, 830, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], [("tipo p", "g", 70, COR)] + ps("tem carga positiva?", "i", 70), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.selo(c, 1680, 190, 60, False, a))
    E.frase(c, t, C["s12.c"], ps("cada átomo de boro é", "i", 64) + [("neutro", "g", 64)], XE, 380, passo=0.1)
    E.frase(c, t, C["s12.c"] + 1.4, ps("tantos elétrons quanto prótons", "i", 54, TINTA2), XE, 470, passo=0.08)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.pilula(c, "o cristal continua neutro", XE + 330, 580, 50, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s12.e"], ps("p e n dizem", "i", 64) + [("quem carrega a corrente", "g", 60, COR)], XE, 740, passo=0.1)
    E.foco(c, t, C["s12.f"], 0.5, lambda a: (E.pilula(c, "p: a lacuna", XE + 160, 870, 50, "g", fundo=E.COR, a=a)))
    E.foco(c, t, C["s12.g"], 0.5, lambda a: (E.pilula(c, "n: o elétron livre", XE + 620, 870, 50, "g", fundo=F.NEG, a=a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("compare com os", "i", 66, CLARO) + [("4", "g", 90, BR)] + ps("do silício", "i", 66, CLARO), W / 2, 320, "center", 0.12)
        for i, (k, n, tipo, cor, txt) in enumerate((("s13.b", "5", "tipo n", F.NEG, "um a mais: sobra elétron"), ("s13.c", "3", "tipo p", E.COR, "um a menos: falta elétron"))):
            y = 520 + 200 * i
            E.foco(c, t, C[k], 0.5, lambda a, n=n, y=y: (E.bola(c, 420, y - 30, 70, a=a), centro(c, n, 420, y, 80, "g", BR, a)))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, txt=txt, y=y: E.escreve(c, txt, 540, y, 60, "i", CLARO, a))
            E.foco(c, t, C[k] + 0.8, 0.4, lambda a, tipo=tipo, cor=cor, y=y: E.pilula(c, tipo, 1550, y - 20, 60, "g", fundo=cor, a=a))
        E.frase(c, t, C["s13.d"], ps("vale para qualquer elemento", "i", 60, CLARO), W / 2, 960, "center", 0.1)
        return
    E.frase(c, t, C["s14.a"], ps("no diodo,", "i", 66, CLARO) + [("siga a seta", "g", 66, BR)], W / 2, 300, "center", 0.12)
    E.foco(c, t, C["s14.a"] + 0.5, 0.5, lambda a: diodo(c, (620, 520), (1300, 520), a, BR, 80))
    if t >= C["s14.b"]:
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "+", 520, 540, 80, "g", E.COR, a))
        F.seta(c, 560, 640, 1260, 640, CERTO, 1.0, 9, None, ease_io(prog(t, C["s14.b"] + 0.5, 0.8)))
        E.foco(c, t, C["s14.b"] + 1.0, 0.4, lambda a: centro(c, "chegou pela base da seta: passa", 910, 720, 50, "g", BR, a))
        E.foco(c, t, C["s14.b"] + 2.4, 0.4, lambda a: centro(c, "chegou pela barra: para", 910, 800, 50, "g", ERRADO, a))
    E.frase(c, t, C["s14.c"], [("vários diodos?", "g", 56, ERRADO)] + ps("siga o caminho um por um", "i", 58, CLARO), W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("arsênio:", "g", 70), ("5", "g", 84, COR)] + ps("elétrons na valência", "i", 62), XE, 330, passo=0.12)
    E.frase(c, t, C["s15.b"], ps("silício com arsênio:", "i", 62) + [("tipo p", "g", 62, COR), ("ou", "i", 62), ("tipo n?", "g", 62, F.NEG)], XE, 450, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("pilha, diodo e lâmpada:", "i", 60), XE, 620, passo=0.1)
    E.frase(c, t, C["s15.d"], [("p", "g", 64, COR)] + ps("ligado ao", "i", 60) + [("negativo", "g", 60, F.NEG)], XE, 720, passo=0.1)
    E.frase(c, t, C["s15.e"], ps("a lâmpada", "i", 70) + [("acende?", "g", 70, COR)], XE, 860, passo=0.12)
    if t < C["s16"]:
        circuito(c, t, C["s15.c"], 1150, 500, 520, 300, False, None)
    else:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17.a"], [("5", "g", 90, COR)] + ps("elétrons: um a mais que o silício", "i", 62), XE, 230, passo=0.1)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.pilula(c, "sobra elétron: tipo n", XE + 300, 350, 56, "g", fundo=F.NEG, a=a))
    if t < C["s18"]:
        cristal(c, t, C["s17.a"] + 0.3, 1150, 520, 3, 3, 170, dop=(1, 1), tipo="n", t_dop=C["s17.a"] + 0.6)
        return
    E.frase(c, t, C["s18.a"], ps("o diodo só conduz com o", "i", 60) + [("p no positivo", "g", 60, COR)], XE, 520, passo=0.1)
    E.frase(c, t, C["s18.b"], ps("aqui, o p está no", "i", 60) + [("negativo", "g", 60, F.NEG)], XE, 630, passo=0.1)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "a corrente para", XE + 220, 750, 50, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "lâmpada apagada", XE + 680, 750, 50, "g", fundo=TINTA, a=a))
    if t < C["s18.e"]:
        circuito(c, t, C["s18"], 1150, 500, 520, 300, False, None)
    else:
        circuito(c, t, C["s18.e"], 1150, 500, 520, 300, True, C["s18.e"] + 0.8)
        E.frase(c, t, C["s18.e"], ps("vire a pilha:", "i", 60) + [("acende", "g", 60, CERTO)], XE, 900, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s19", (("s19.a", [("5", "g", 70, F.NEG), ("→ tipo n;", "g", 66, F.NEG), ("3", "g", 70, COR), ("→ tipo p", "g", 66, COR)]),
                                ("s19.b", [("diodo:", "g", 66), ("só do", "i", 70), ("p", "g", 70, COR), ("para o", "i", 70), ("n", "g", 70, F.NEG)]),
                                ("s19.c", [("transistor:", "g", 66), ("a base liga e desliga", "i", 70)])), y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, tela_resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Praticando:", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.4, [("física moderna", "g", 100, COR)], XE, 520)
    for i, s in enumerate(("fóton", "fotoelétrico", "espectros", "relatividade")):
        E.foco(c, t, C["s20.b"] + 0.4 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s, XE + 160 + 330 * (i % 2), 700 + 110 * (i // 2), 48, "g", fundo=TINTA, a=a))
    inscreva(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, materiais=b_materiais, dopagem=b_dopagem, diodo=b_diodo, transistor=b_transistor,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
