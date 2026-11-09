"""Visual — Estudativo · FIS-MOD-007: praticando física moderna.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Prática: cada questão abre com o
número numa esfera, o enunciado à esquerda e um desenho à direita; no "pause e tente" o desenho dá lugar ao relógio; a
resolução usa as mesmas peças das aulas (fóton, placa de metal, escada de níveis, nave). Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-007_praticando_fisica_moderna.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))

# todas as contas da aula
h_, c_, e_ = 6.6e-34, 3e8, 1.6e-19
assert abs(c_ / 6e-7 - 5e14) < 1 and abs(h_ * 5e14 - 3.3e-19) < 1e-31 and 6.6 * 5 == 33        # Q1
assert abs(4.8e-19 / e_ - 3) < 1e-12 and abs(3 - 2.3 - 0.7) < 1e-12                               # Q2
assert abs(13.6 - 3.4 - 10.2) < 1e-12 and abs(13.6 - 1.51 - 12.09) < 1e-12 and 10.2 < 11 < 12.09  # Q3
assert abs(1 / math.sqrt(1 - 0.36) - 1.25) < 1e-12 and abs(2 * 1.25 - 2.5) < 1e-12                # Q4: 2,5 μs
assert abs(0.6 * c_ - 1.8e8) < 1e-3 and abs(1.8e8 * 2.5e-6 - 450) < 1e-6                          # Q4: 450 m
assert abs(600e-9 - 6e-7) < 1e-20                                                                  # 600 nm


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
def numero_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 190, 50, a=a), centro(c, str(n), XE + 50, 214, 64, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, ps("questão", "i", 72, COR), XE + 130, 214)


def pausa(c, t, t0, desenho):
    """desenho à direita até a pausa; depois, o relógio"""
    if t < t0:
        desenho()
    else:
        E.relogio(c, t, t0, cx=1500, cy=470, r=190)


def niveis_h(c, t, t0, x, w, size=44):
    for i, (n, v, y) in enumerate(((1, "−13,6", 880), (2, "−3,4", 520), (3, "−1,51", 400))):
        q = ep(t, t0 + 0.2 * i, 0.4)
        if q <= 0:
            continue
        M.line(c, x, y, x + w * q, y, TINTA, 1.0, 6)
        E.foco(c, t, t0 + 0.2 * i, 0.4, lambda a, n=n, v=v, y=y: (E.escreve(c, f"n = {n}", x - 140, y + 14, size, "g", TINTA2, a),
                                                                F.medida(c, v, "eV", x + w + 20, y + 14, size, COR, a)))


def nave(c, x, y, L, a=1.0, cor=None):
    if a <= 0:
        return
    cor = cor or F.VEL
    h = min(0.28 * L, 120)
    p = skia.Path()
    p.moveTo(x, y - h / 2); p.lineTo(x + L * 0.75, y - h / 2); p.quadTo(x + L, y, x + L * 0.75, y + h / 2); p.lineTo(x, y + h / 2); p.close()
    c.drawPath(p, M.paint(cor, a))
    c.drawCircle(x + L * 0.62, y, h * 0.18, M.paint("#DDF4F6", a))


def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("Física Moderna", "g", 90, COR)] + ps("assusta pelo nome", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, C["s01.b"], ps("mas a prova cobra", "i", 70) + [("poucas fórmulas", "g", 70)], XE, 400, passo=0.12)
    E.frase(c, t, C["s01.c"], ps("até o fim da aula:", "i", 66) + [("5 questões", "g", 70, COR)], XE, 580, passo=0.12)
    for i, s in enumerate(("fóton", "fotoelétrico", "espectros", "dualidade", "relatividade")):
        E.foco(c, t, C["s01.c"] + 1.2 + 0.35 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s, XE + 150 + 330 * (i % 3), 720 + 120 * (i // 3), 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1550, 330, 220 * ease_back(prog(t, C["s01.a"] + 0.4, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as constantes", "i", 80, COR), XE, 220)
    constante(c, t, C["s02.a"], XE, 300, "constante de Planck", "h =", "6,6 × 10^{−34} J·s", 66)
    constante(c, t, C["s02.b"], XE, 540, "velocidade da luz", "c =", "3 × 10^8 m/s", 66)
    constante(c, t, C["s02.c"], XE, 780, "elétron-volt", "1 eV =", "1,6 × 10^{−19} J", 66)
    E.frase(c, t, lerp(C["s02.c"], C["s02.end"], 0.6), ps("faltou alguma aula?", "i", 56, COR) + ps("procure no canal", "i", 56), 1060, 960, "left", 0.12)


def b_metodo(c, t, C, b):
    def s03():
        E.frase(c, t, C["s03.a"], ps("a palavra da questão", "i", 76) + [("escolhe a fórmula", "g", 72, COR)], XE, 220, passo=0.12)
        linhas = (("s03.b", "frequência, cor", "E = h · f"), ("s03.c", "arrancar elétron", "Ec = h · f − W"), ("s03.d", "nível, salto", "diferença dos níveis"))
        for i, (k, pal, f) in enumerate(linhas):
            y = 420 + 190 * i
            E.foco(c, t, C[k], 0.5, lambda a, pal=pal, y=y: E.pilula(c, pal, XE + 260, y - 22, 52, "g", fundo=TINTA, a=a))
            E.foco(c, t, C[k] + 0.4, 0.5, lambda a, y=y: E.escreve(c, "→", XE + 560, y, 70, "g", TINTA2, a))
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, f=f, y=y: E.formula(c, f, XE + 680, y, 80, "g", COR, a))
    E.saida(c, t, C["s04"] - 0.1, s03)
    if t < C["s04"]:
        return
    linhas = (("s04.a", "onda de partícula", "λ = h ÷ Q"), ("s04.b", "perto da luz", "γ: × tempo, ÷ comprimento"))
    for i, (k, pal, f) in enumerate(linhas):
        y = 300 + 190 * i
        E.foco(c, t, C[k], 0.5, lambda a, pal=pal, y=y: E.pilula(c, pal, XE + 260, y - 22, 52, "g", fundo=TINTA, a=a))
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, y=y: E.escreve(c, "→", XE + 560, y, 70, "g", TINTA2, a))
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, f=f, y=y: E.escreve(c, f, XE + 680, y, 72, "g", COR, a))
    E.frase(c, t, C["s04.c"], ps("antes da conta:", "i", 70) + [("unidades combinando", "g", 70, CERTO)], XE, 740, passo=0.12)
    E.frase(c, t, C["s04.c"] + 1.4, [("J", "g", 70), ("com", "i", 70), ("J,", "g", 70), ("eV", "g", 70), ("com", "i", 70), ("eV", "g", 70)], XE, 860, passo=0.12)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    if t < C["s06"]:
        numero_q(c, t, C["s05"], 1)
        E.frase(c, t, C["s05.a"], ps("luz", "i", 70) + [("laranja", "g", 70, cor_luz(600))] + ps("de", "i", 70) + [("600 nm", "g", 70)], XE, 360, passo=0.12)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "λ = 6 × 10^{−7} m", XE, 480, 70, "g", TINTA2, a))
        E.frase(c, t, C["s05.c"], ps("energia de cada fóton,", "i", 66) + [("em J?", "g", 66, COR)], XE, 640, passo=0.12)
        pausa(c, t, C["s05.d"], lambda: (lampada_fonte(c, 1250, 500, 70, cor_luz(600), ep(t, C["s05.a"], 0.5), t),
                                         jorro(c, t, C["s05.a"] + 0.3, (1330, 500), (1800, 500), cor_luz(600), 0.6, 1.2, n=3, amp=18, lam=30, largura=5)))
        return
    E.formula_em(c, t, C["s06.a"], "c = λ · f", XE, 240, 90, "g", TINTA)
    E.formula_em(c, t, C["s06.b"], "f = f{3 × 10^8}{6 × 10^{−7}}", XE, 420, 90, "g", TINTA)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "= 5 × 10^{14} Hz", XE + 640, 420, 80, "g", TINTA2, a))
    E.formula_em(c, t, C["s06.d"], "E = 6,6 × 10^{−34} · 5 × 10^{14} = 33 × 10^{−20}", XE, 640, 72, "g", TINTA)
    bola_txt_f(c, t, C["s06.e"], "3,3 × 10^{−19}", "J", W / 2, 850, 110, 76)


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    if t < C["s08"]:
        numero_q(c, t, C["s07"], 2)
        E.frase(c, t, C["s07.a"], ps("fótons de", "i", 66), XE, 340)
        E.foco(c, t, C["s07.a"] + 0.4, 0.5, lambda a: E.formula(c, "4,8 × 10^{−19} J", XE + 290, 340, 72, "g", UV, a))
        E.frase(c, t, C["s07.b"], ps("sódio:", "i", 66) + [("W = 2,3 eV", "g", 66)], XE, 460, passo=0.12)
        E.frase(c, t, C["s07.c"], [("Ec", "g", 70, COR)] + ps("dos elétrons?", "i", 66), XE, 610, passo=0.12)
        E.frase(c, t, C["s07.d"], ps("e com o", "i", 66) + [("triplo", "g", 66, COR)] + ps("da intensidade?", "i", 66), XE, 730, passo=0.12)

        def des():
            placa_metal(c, 1200, 700, 520, 90, ep(t, C["s07.a"], 0.5), "sódio")
            k = int(max(0, t - C["s07.a"]) // 1.0)
            for j in range(max(0, k - 2), k + 1):
                t0 = C["s07.a"] + 1.0 * j
                foton(c, t, t0, (1150, 420), (1400 + 40 * (j % 3), 690), UV, 0.8, n=3, amp=12, lam=18, largura=4)
                if t >= t0 + 0.8:
                    u = ease_out(prog(t, t0 + 0.8, 1.0))
                    eletron(c, lerp(1410 + 40 * (j % 3), 1660, u), lerp(690, 420, u), 22, min(1, u * 5) * (1 - prog(t, t0 + 2.2, 0.4)))
        pausa(c, t, C["s07.e"], des)
        return
    E.frase(c, t, C["s08.a"], ps("unidades diferentes:", "i", 66) + [("fóton em eV", "g", 66, COR)], XE, 220, passo=0.12)
    E.formula_em(c, t, C["s08.b"], "f{4,8 × 10^{−19}}{1,6 × 10^{−19}} = 3 eV", XE, 400, 84, "g", TINTA)
    E.formula_em(c, t, C["s08.c"], "Ec = 3 − 2,3", XE, 580, 90, "g", TINTA)
    bola_txt(c, t, C["s08.d"], "0,7", "eV", 1450, 560, 140, 90)
    E.frase(c, t, C["s08.e"], [("3×", "g", 80, COR)] + ps("intensidade:", "i", 66) + [("3×", "g", 80, COR), ("elétrons", "g", 66, F.NEG)], XE, 820, passo=0.12)
    E.frase(c, t, C["s08.f"], ps("cada um com os mesmos", "i", 60) + [("0,7 eV", "g", 64, CERTO)], XE, 940, passo=0.1)


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    if t < C["s10"]:
        numero_q(c, t, C["s09"], 3)
        E.frase(c, t, C["s09.a"], [("hidrogênio", "g", 66)] + ps("no primeiro nível", "i", 66), XE, 340, passo=0.12)
        E.frase(c, t, C["s09.c"], ps("absorve um fóton de", "i", 66) + [("10,2 eV?", "g", 66, COR)], XE, 520, passo=0.12)
        E.frase(c, t, C["s09.d"], ps("e um de", "i", 66) + [("11 eV?", "g", 66, COR)], XE, 640, passo=0.12)
        pausa(c, t, C["s09.e"], lambda: niveis_h(c, t, C["s09.a"], 1250, 360))
        if t < C["s09.e"] and t >= C["s09.a"]:
            eletron(c, 1430, 880 - 24, 20, ep(t, C["s09.a"], 0.4))
        return
    niveis_h(c, t, C["s10"], 1150, 360)
    E.formula_em(c, t, C["s10.a"], "1 → 2: 13,6 − 3,4 = 10,2", XE, 260, 72, "g", TINTA)
    if t >= C["s10.b"]:
        foton(c, t, C["s10.b"], (900, 700), (1270, 700), UV, 0.8, n=3, amp=12, lam=18, largura=4)
        F.seta(c, 1300, 870, 1300, 530, CERTO, 1.0, 8, None, ease_io(prog(t, C["s10.b"] + 0.8, 0.6)))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "10,2 eV: absorvido", XE + 300, 400, 52, "g", fundo=CERTO, a=a))
    E.formula_em(c, t, C["s10.d"], "1 → 3: 12,09", XE, 560, 72, "g", TINTA)
    if t >= C["s10.e"]:
        F.seta(c, 1420, 870, 1420, 620, ERRADO, 1.0, 8, None, ease_io(prog(t, C["s10.e"], 0.6)))
        E.foco(c, t, C["s10.e"] + 0.5, 0.4, lambda a: E.escreve(c, "11 eV: fica no meio", 1460, 680, 44, "b", ERRADO, a))
    E.frase(c, t, C["s10.e"], ps("11 não paga nenhum salto certinho", "i", 56), XE, 720, passo=0.08)
    E.foco(c, t, C["s10.f"], 0.5, lambda a: E.pilula(c, "11 eV: passa direto", XE + 300, 850, 52, "g", fundo=ERRADO, a=a))


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    if t < C["s12"]:
        numero_q(c, t, C["s11"], 4)
        E.frase(c, t, C["s11.a"], ps("partícula instável:", "i", 64) + [("2 μs", "g", 70)] + ps("parada", "i", 64), XE, 340, passo=0.12)
        E.frase(c, t, C["s11.b"], ps("no acelerador:", "i", 64) + [("0,6c", "g", 70, F.VEL)], XE, 460, passo=0.12)
        E.frase(c, t, C["s11.c"], ps("quanto vive no", "i", 64) + [("laboratório?", "g", 64, COR)], XE, 610, passo=0.12)
        E.frase(c, t, C["s11.d"], [("quantos metros", "g", 64, COR)] + ps("anda?", "i", 64), XE, 730, passo=0.12)

        def des():
            if t >= C["s11.b"]:
                u = ((t - C["s11.b"]) / 1.6) % 1
                E.bola(c, lerp(1150, 1800, u), 520, 30, E.COR, ep(t, C["s11.b"], 0.3))
                M.line(c, 1100, 580, 1840, 580, TINTA2, 0.5, 4, dash=E.TRACO)
        pausa(c, t, C["s11.e"], des)
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: (E.escreve(c, "0,6c →", XE, 230, 76, "g", TINTA, a), E.escreve(c, "γ = 1,25", XE + 300, 230, 76, "g", COR, a)))
    E.frase(c, t, C["s12.b"], ps("laboratório vê de fora:", "i", 60) + [("tempo maior", "g", 60, COR)], XE, 360, passo=0.1)
    E.formula_em(c, t, C["s12.c"], "2 × 1,25 = 2,5 μs", XE, 500, 84, "g", TINTA)
    E.formula_em(c, t, C["s12.d"], "v = 0,6 · 3 × 10^8 = 1,8 × 10^8 m/s", XE, 660, 70, "g", TINTA2)
    E.formula_em(c, t, C["s12.e"], "d = 1,8 × 10^8 · 2,5 × 10^{−6}", XE, 800, 70, "g", TINTA2)
    bola_txt(c, t, C["s12.f"], "450", "m", 1500, 500, 150, 90)


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    if t < C["s14"]:
        numero_q(c, t, C["s13"], 5)
        E.frase(c, t, C["s13.a"], [("elétron", "g", 66, F.NEG), ("e", "i", 66), ("próton", "g", 66, COR)] + ps("com a", "i", 66) + [("mesma Q", "g", 66)], XE, 360, passo=0.12)
        E.frase(c, t, C["s13.b"], ps("quem tem o maior", "i", 66) + [("λ?", "g", 70, COR)], XE, 500, passo=0.12)
        pausa(c, t, C["s13.c"], lambda: (eletron(c, 1250, 500, 30, ep(t, C["s13.a"], 0.4)),
                                         (E.bola(c, 1550, 500, 70, E.COR, ep(t, C["s13.a"], 0.4)), centro(c, "+", 1550, 530, 70, "g", BR, ep(t, C["s13.a"], 0.4)))))
        return
    E.frase(c, t, C["s14.a"], ps("a pegadinha está na", "i", 70) + [("massa", "g", 70, ERRADO)], XE, 220, passo=0.12)
    E.formula_em(c, t, C["s14.b"], "λ = f{h}{Q}", XE, 420, 120, "g", TINTA)
    E.frase(c, t, C["s14.c"], [("mesma Q", "g", 70), ("→", "g", 70, TINTA2), ("mesmo λ", "g", 70, COR)], XE + 520, 400, passo=0.12)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "os comprimentos de onda são iguais", W / 2, 600, 56, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s14.e"], ps("massa só importa com a", "i", 60) + [("mesma velocidade", "g", 60)], XE, 780, passo=0.1)
    E.frase(c, t, C["s14.f"], [("elétron:", "g", 60, F.NEG)] + ps("Q menor,", "i", 60), XE, 900, passo=0.1)
    E.frase(c, t, C["s14.g"], [("λ maior", "g", 60, COR)], XE + 470, 900)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s15", (("s15.a", [("a palavra", "i", 70), ("escolhe a fórmula", "g", 66, COR)]),
                                ("s15.b", [("unidades", "g", 66), ("acertadas antes da conta", "i", 70)])), y0=420, dy=220)
    E.saida(c, t, C["s15.c"] - 0.6, tela_resumo)
    if t < C["s15.c"] - 0.6:
        return
    E.frase(c, t, C["s15.c"] - 0.5, [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s15.d"], [("Vida das estrelas", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s15.d"] + 0.4, [("e buracos negros", "g", 100, COR)], XE, 520)
    E.foco(c, t, C["s15.d"] + 0.6, 0.5, lambda a: (M.rrect(c, 300, 640, 640, 340, 30, "#0E0E18", a),
                                                  [c.drawCircle(320 + 600 * ((k * 0.6180339) % 1), 660 + 300 * ((k * 0.4142135 + 0.3 * (k % 3)) % 1), 3, M.paint(BR, a * 0.8)) for k in range(30)],
                                                  E.bola(c, 620, 810, 70, "#FFB000", a)))
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s15.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s15.e"] + 0.2, 0.4))
    E.frase(c, t, C["s15.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
