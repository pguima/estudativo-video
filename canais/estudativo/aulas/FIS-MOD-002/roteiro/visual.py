"""Visual — Estudativo · FIS-MOD-002: efeito fotoelétrico.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001 (fóton = pacote de onda, elétron
azul com "−", metal = placa cinza, energia = número + unidade). Função trabalho W = degrau/poço em tinta; energia cinética,
o "troco", em verde-certo só na resposta. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-002_efeito_fotoeletrico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("efeito", "trabalho", "conta", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
assert abs(3.3 - 2.3 - 1.0) < 1e-9                       # sódio: 1 eV
assert 1.65 < 2.3                                        # vermelho não arranca do sódio
assert abs(6.6 - 4.3 - 2.3) < 1e-9 and 1.65 < 4.3        # questão: 2,3 eV; vermelho não arranca do zinco
assert abs(5.28e-19 / 1.6e-19 - 3.3) < 1e-9              # 5,28 × 10⁻¹⁹ J = 3,3 eV
assert abs((5.28e-19 - 2.3) - (-2.3)) < 1e-12            # o erro: "praticamente −2,3"
assert 4.3 / 4.14e-15 > 1e15                              # o ultravioleta do gancho tem de passar de ~1 × 10¹⁵ Hz no zinco


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


# ---------------- peças desta aula ----------------
def arranca(c, t, t0, x0, y0, cor, sai=True, n=1, dx=0, vel=1.0):
    """fóton cai na placa (topo em y0) e, se sai, um elétron pula para fora"""
    foton(c, t, t0, (x0 - 220, y0 - 260), (x0, y0 - 20), cor, 0.8, n=3, amp=12 if cor != VERM else 16, lam=18 if cor != VERM else 28, largura=4)
    if sai and t >= t0 + 0.8:
        u = ease_out(prog(t, t0 + 0.8, 1.0 / vel))
        eletron(c, lerp(x0 + 10, x0 + 220 + dx, u), lerp(y0 - 10, y0 - 300, u), 24, min(1, u * 5) * (1 - prog(t, t0 + 2.4, 0.4)))


def arranca_loop(c, t, t0, t1, periodo, x0, y0, cor, sai=True):
    """um fóton (e um elétron) a cada periodo, de t0 até t1"""
    k = max(0, int((t - t0 - 2.8) // periodo))
    while t0 + k * periodo <= min(t, t1):
        arranca(c, t, t0 + k * periodo, x0 + 40 * (k % 3), y0, cor, sai, dx=-40 * (k % 2))
        k += 1


def poco(c, x, y, w, prof, a=1.0):
    """chão com um buraco de profundidade prof: a bola no fundo precisa de energia para sair"""
    if a <= 0:
        return
    pts = [(x, y), (x + w * 0.35, y), (x + w * 0.4, y + prof), (x + w * 0.6, y + prof), (x + w * 0.65, y), (x + w, y)]
    F.poli(c, pts, 1.0, TINTA, a, 7)


def b_gancho(c, t, C, b):
    def um():
        for i, (x, cor, k_t, k_r, nome) in enumerate(((180, VERM, "s01.a", "s01.b", "vermelha fortíssima"), (1000, UV, "s01.c", "s01.d", "ultravioleta fraquinha"))):
            p = ep(t, C[k_t], 0.5)
            E.caixa_pontilhada(c, x, 170, 740, 760, p, prog_=p)
            if t < C[k_t]:
                continue
            E.frase(c, t, C[k_t] + 0.1, ps("luz", "i", 60) + [(nome, "g", 52, cor)], x + 40, 260, passo=0.1)
            placa_metal(c, x + 200, 760, 460, 90, ep(t, C[k_t] + 0.3, 0.4), "zinco")
            E.foco(c, t, C[k_t] + 0.3, 0.5, lambda a, x=x, cor=cor, i=i: lampada_fonte(c, x + 110, 400, 70 if i == 0 else 40, cor, a, t))
            if i == 0:
                jorro(c, t, C[k_t] + 0.6, (x + 160, 450), (x + 380, 740), VERM, 0.22, 0.9, n=3, amp=16, lam=28, largura=4)
                E.foco(c, t, C[k_r], 0.4, lambda a, x=x: E.pilula(c, "nada acontece", x + 370, 900, 46, "b", fundo=TINTA, a=a))
            else:
                for k in range(4):
                    arranca(c, t, C[k_t] + 0.6 + 1.0 * k, x + 380, 760, UV, dx=40 * (k % 2))
                E.foco(c, t, C[k_r], 0.4, lambda a, x=x: E.pilula(c, "elétrons saltam", x + 370, 900, 46, "b", fundo=E.COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a energia do elétron"), ("s02.b", "quem manda: a frequência"), ("s02.c", "não a intensidade")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        pacote(c, x, y, 0, E.COR, a, n=3, amp=26, lam=44, largura=7)

    def f2(a, x, y):
        eletron(c, x, y, 34, a)
    lembrete2(c, t, C, "s03", (("s03.b", "energia de um fóton:", "E = h · f"), ("s03.c", "elétron-volt:", "1 eV = 1,6 × 10⁻¹⁹ J")), (f1, f2))


# ---------------- o efeito ----------------
def b_efeito(c, t, C, b):
    def s04():
        placa_metal(c, 1100, 860, 640, 90, ep(t, C["s04"], 0.5), "metal")
        arranca_loop(c, t, C["s04.a"], C["s05"], 0.9, 1300, 860, E.COR)
        E.frase(c, t, C["s04.a"], ps("a luz arranca", "i", 76) + [("elétrons", "g", 76, F.NEG)], XE, 240, passo=0.12)
        E.frase(c, t, C["s04.b"], [("efeito", "g", 96, COR), ("fotoelétrico", "g", 96, COR)], XE, 380, passo=0.15)
        E.frase(c, t, C["s04.c"], ps("os que saem:", "i", 64) + [("fotoelétrons", "g", 60)], XE, 490, passo=0.12)
        E.frase(c, t, C["s04.d"], [("Einstein,", "g", 70), ("1905", "g", 70, COR)], XE, 680, passo=0.15)
        E.foco(c, t, C["s04.e"], 0.5, lambda a: E.pilula(c, "Nobel por isto, não pela relatividade", XE + 470, 800, 44, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], ps("a regra:", "i", 76, COR), XE, 200)
    E.frase(c, t, C["s05.a"], [("1 fóton", "g", 90), ("→", "g", 90, TINTA2), ("1 elétron", "g", 90, F.NEG)], XE, 340, passo=0.2)
    E.frase(c, t, C["s05.a"] + 1.0, ps("toda a energia de uma vez", "i", 66), XE, 440, passo=0.1)
    # um fóton chega no elétron e some dentro dele
    q = ep(t, C["s05.a"], 0.4)
    eletron(c, 1500, 380, 40, q)
    foton(c, t, C["s05.a"] + 0.4, (1000, 380), (1440, 380), E.COR, 1.0, n=3, amp=30, lam=50, largura=7)
    E.frase(c, t, C["s05.b"], [("não", "g", 70, ERRADO)] + ps("existe meio fóton", "i", 70), XE, 640, passo=0.12)
    E.foco(c, t, C["s05.b"] + 0.5, 0.4, lambda a: (pacote(c, 1300, 620, 0, E.COR, a * 0.5, n=1, amp=26, lam=50, largura=7),
                                                  E.risco(c, 1240, 660, 1380, 580, t, C["s05.b"] + 0.8, largura=9)))
    E.frase(c, t, C["s05.c"], [("não", "g", 70, ERRADO)] + ps("junta vários fótons", "i", 70), XE, 840, passo=0.12)
    if t >= C["s05.c"]:
        eletron(c, 1500, 820, 34, ep(t, C["s05.c"], 0.4))
        for k, dy in enumerate((-60, 0, 60)):
            foton(c, t, C["s05.c"] + 0.3 + 0.15 * k, (1050, 820 + dy), (1300, 820 + dy * 0.4), VERM, 0.9, n=3, amp=12, lam=24, largura=4, fica=True)
        E.foco(c, t, C["s05.c"] + 1.4, 0.4, lambda a: E.selo(c, 1660, 820, 40, False, a))


# ---------------- função trabalho ----------------
def b_trabalho(c, t, C, b):
    def s06():
        y = 560
        E.foco(c, t, C["s06.a"], 0.5, lambda a: poco(c, 980, y, 760, 220, a))
        sobe = ease_io(prog(t, C["s06.b"] + 0.3, 1.0))
        E.foco(c, t, C["s06.a"] + 0.3, 0.4, lambda a: E.bola(c, 1360, y + 220 - 40 - 220 * sobe * 0.0, 38, E.COR, a))
        if t >= C["s06.b"]:
            F.seta(c, 1500, y + 210, 1500, y - 10, TINTA, 1.0, 8, None, ease_io(prog(t, C["s06.b"], 0.6)))
            E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: E.escreve(c, "energia mínima", 1540, y + 110, 46, "i", TINTA2, a))
            E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "W", 1540, y + 190, 80, "g", COR, a))
        E.frase(c, t, C["s06.a"], ps("bola no fundo do", "i", 70) + [("buraco", "g", 70)], XE, 230, passo=0.12)
        E.frase(c, t, C["s06.c"], [("função", "g", 90, COR), ("trabalho", "g", 90, COR)], XE, 400, passo=0.15)
        E.frase(c, t, C["s06.d"], ps("letra", "i", 70) + [("W", "g", 80, COR)], XE, 510, passo=0.12)
        E.frase(c, t, C["s06.e"], ps("cada metal tem a sua", "i", 64), XE, 640, passo=0.1)
        for k, (n, v) in enumerate((("sódio", "2,3"), ("zinco", "4,3"))):
            E.foco(c, t, C["s06." + "fg"[k]], 0.5, lambda a, n=n, v=v, k=k: (E.escreve(c, n, XE, 780 + 120 * k, 60, "i", TINTA, a),
                                                                            F.medida(c, v, "eV", XE + 260, 780 + 120 * k, 76, COR, a)))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    # escada de energia: o fóton pequeno não chega, o grande passa e sobra
    yb, yw = 860, 520
    E.foco(c, t, C["s07"], 0.5, lambda a: (M.line(c, 1000, yw, 1700, yw, TINTA, a, 5, dash=E.TRACO), E.escreve(c, "W", 1730, yw + 22, 64, "g", COR, a),
                                           M.line(c, 1000, yb, 1700, yb, TINTA, a, 5)))
    for i, (x, alto, ok, kk) in enumerate(((1150, 220, False, "s07.a"), (1500, 560, True, "s07.b"))):
        q = ease_io(prog(t, C[kk], 0.7))
        if q > 0:
            M.rrect(c, x, yb - alto * q, 120, alto * q, 10, E.COR if ok else VERM, 0.85)
            E.foco(c, t, C[kk] + 0.6, 0.4, lambda a, x=x, ok=ok: E.selo(c, x + 60, yb + 80, 38, ok, a))
    E.frase(c, t, C["s07.a"], ps("energia do fóton", "i", 64) + [("menor", "g", 60, ERRADO)] + ps("que W:", "i", 64), XE, 260, passo=0.1)
    E.frase(c, t, C["s07.a"] + 1.0, ps("não sai", "g", 70), XE, 360, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("maior que W:", "i", 64) + [("sai", "g", 70, CERTO)], XE, 520, passo=0.12)
    if t >= C["s07.c"]:
        q = ep(t, C["s07.c"], 0.5)
        M.rrect(c, 1500, yb - 560, 120, 560 - (yb - yw), 10, CERTO, q)
        E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: E.escreve(c, "sobra", 1640, yb - 470, 50, "i", CERTO, a))
    E.frase(c, t, C["s07.c"], ps("o que sobra: energia de", "i", 60) + [("movimento", "g", 58)], XE, 680, passo=0.1)
    E.frase(c, t, C["s07.d"], [("energia", "g", 80, CERTO), ("cinética", "g", 80, CERTO)], XE, 820, passo=0.15)
    E.frase(c, t, C["s07.d"] + 1.2, ps("(a fórmula dela é outra aula)", "i", 50, TINTA2), XE, 910, passo=0.08)


# ---------------- a equação ----------------
def b_conta(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"], ps("uma conta de", "i", 76) + [("sobra", "g", 76, COR)], XE, 210, passo=0.12)
        F.formula_legenda(c, t, C["s08.b"], "Ec = h · f − W", [("h · f", "energia que chega com o fóton", None), ("W", "o preço para sair", None),
                                                                ("Ec", "o troco: o máximo que o elétron leva", None)],
                          XE, 430, 150, tl=[C["s08.c"], C["s08.d"], C["s08.e"]], size_l=58, dy=110)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("fóton", "i", 76)], XE, 230)
            E.foco(c, t, C["s09.a"] + 0.3, 0.5, lambda a: F.medida(c, "3,3", "eV", XE + 230, 230, 96, UV, a))
            E.frase(c, t, C["s09.b"], [("sódio", "i", 76)], XE, 380)
            E.foco(c, t, C["s09.b"] + 0.3, 0.5, lambda a: F.medida(c, "2,3", "eV", XE + 230, 380, 96, TINTA, a))
            E.formula_em(c, t, C["s09.c"], "Ec = 3,3 − 2,3", XE, 580, 110, "g", TINTA)
            bola_txt(c, t, C["s09.d"], "1", "eV", 640, 830, 120, 90)
            placa_metal(c, 1100, 760, 600, 90, ep(t, C["s09.b"], 0.5), "sódio")
            arranca_loop(c, t, C["s09.b"] + 0.4, C["s10"], 1.1, 1340, 760, UV)
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("fóton", "i", 76), ("vermelho", "g", 76, VERM)], XE, 230, passo=0.12)
    E.foco(c, t, C["s10.a"] + 0.6, 0.5, lambda a: F.medida(c, "1,65", "eV", XE + 600, 230, 96, VERM, a))
    E.formula_em(c, t, C["s10.b"], "1,65 < 2,3", XE, 400, 110, "g", TINTA)
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "nenhum elétron sai", XE + 330, 530, 50, "g", fundo=TINTA, a=a))
    placa_metal(c, 1200, 600, 560, 90, ep(t, C["s10"], 0.5), "sódio")
    jorro(c, t, C["s10.a"] + 0.3, (1150, 300), (1420, 580), VERM, 0.35, 0.9, n=3, amp=16, lam=28, largura=4)
    E.frase(c, t, C["s10.d"], ps("f em que", "i", 60) + [("h · f = W:", "g", 60)], XE, 720, passo=0.1)
    E.frase(c, t, C["s10.e"], [("frequência", "g", 84, COR), ("de corte", "g", 84, COR)], XE, 860, passo=0.15)
    E.foco(c, t, C["s10.e"] + 1.2, 0.4, lambda a: E.escreve(c, "f₀", XE + 860, 860, 84, "g", TINTA2, a))


# ---------------- intensidade ----------------
def b_brilho(c, t, C, b):
    E.frase(c, t, C["s11.a"], ps("mais intensa =", "i", 70) + [("mais fótons", "g", 70, COR)] + ps("por segundo", "i", 70), XE, 200, passo=0.1)
    for i, (x, cor, kk, nome, sai) in enumerate(((180, E.COR, "s11.b", "acima do corte", True), (1000, VERM, "s11.d", "abaixo do corte", False))):
        p = ep(t, C[kk], 0.5)
        E.caixa_pontilhada(c, x, 280, 740, 560, p, prog_=p)
        if t < C[kk]:
            continue
        E.foco(c, t, C[kk], 0.4, lambda a, x=x, nome=nome: E.escreve(c, nome, x + 40, 350, 54, "g", TINTA, a))
        placa_metal(c, x + 160, 740, 500, 80, ep(t, C[kk] + 0.2, 0.4))
        if sai:
            arranca_loop(c, t, C[kk] + 0.4, 1e9, 0.45, x + 300, 740, cor)
        else:
            for dx in (0, 40, 80):
                jorro(c, t, C[kk] + 0.4 + dx / 100, (x + 80 + dx, 420), (x + 340 + dx, 720), cor, 0.4, 0.8, n=3, amp=16, lam=28, largura=4)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "mesma energia cada um", 550, 900, 42, "b", fundo=E.COR, a=a))
    E.foco(c, t, C["s11.d"] + 2.0, 0.4, lambda a: E.pilula(c, "continua nada", 1370, 900, 42, "b", fundo=TINTA, a=a))
    E.frase(c, t, C["s11.e"], [("frequência:", "g", 60, COR)] + ps("se sai", "i", 64) + [("·", "g", 60, TINTA2), ("intensidade:", "g", 60)] + ps("quantos saem", "i", 64),
            W / 2, 1010, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("misturar unidades", "i", 76), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "Ec = 5,28 × 10^{−19} J − 2,3 eV", W / 2, 400, 84, "g", TINTA, "center")
    E.formula_em(c, t, C["s12.c"], "≈ −2,3 ?", W / 2, 540, 96, "g", ERRADO, "center")
    E.foco(c, t, C["s12.c"] + 1.0, 0.4, lambda a: E.pilula(c, "energia negativa: impossível", W / 2, 640, 46, "b", fundo=ERRADO, a=a))
    if t >= C["s12.c"] + 1.5:
        E.risco(c, W / 2 - 520, 430, W / 2 + 520, 340, t, C["s12.c"] + 1.5, largura=12)
    E.frase(c, t, C["s12.d"], ps("antes de subtrair:", "i", 66) + [("mesma unidade", "g", 66, COR)], XE, 790, passo=0.12)
    E.formula_em(c, t, C["s12.e"], "5,28 × 10^{−19} J = 3,3 eV", W / 2, 940, 84, "g", CERTO, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), XE, 150)
    P = F.grafico(c, t, C["s13.a"], 860, 200, 760, 640, 0, 10, 0, 7, eixo_x="f", eixo_y="Ec", passo=1, marcas_x=[], marcas_y=[], escuro=True)
    E.frase(c, t, C["s13.a"], [("gráfico", "g", 64, BR)] + ps("Ec × f", "g", 64, E.COR), XE, 280, passo=0.12)
    E.curva(c, t, C["s13.b"], P, lambda f: f - 3, 3, 10, 1.0, cor=E.COR, largura=8)
    E.frase(c, t, C["s13.b"], ps("depois do corte:", "i", 56, CLARO) + [("reta", "g", 60, BR)], XE, 420, passo=0.12)
    E.ponto(c, t, C["s13.c"], P, 3, 0, None, cor=BR)
    E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: centro(c, "corte", P.x(3), P.oy + 80, 46, "g", BR, a))
    E.frase(c, t, C["s13.c"], ps("corta o eixo no", "i", 56, CLARO) + [("corte", "g", 56, BR)], XE, 520, passo=0.1)
    if t >= C["s13.d"]:  # triângulo da inclinação
        q = ep(t, C["s13.d"], 0.5)
        x0, y0 = P(6, 3)
        x1, y1 = P(8, 3)
        x2, y2 = P(8, 5)
        M.line(c, x0, y0, x1, y1, BR, q, 4, dash=E.TRACO)
        M.line(c, x1, y1, x2, y2, BR, q, 4, dash=E.TRACO)
        E.foco(c, t, C["s13.d"] + 0.3, 0.4, lambda a: E.escreve(c, "inclinação = h", x1 + 20, (y1 + y2) / 2 + 20, 50, "g", BR, a))
    E.frase(c, t, C["s13.d"], ps("inclinação:", "i", 56, CLARO) + [("h", "g", 64, E.COR)], XE, 620, passo=0.12)
    if t >= C["s14"]:
        E.curva(c, t, C["s14.a"], P, lambda f: f - 5.5, 5.5, 10, 1.0, cor=CLARO, largura=8)
        E.ponto(c, t, C["s14.c"], P, 5.5, 0, None, cor=CLARO)
        E.frase(c, t, C["s14.a"], ps("outro metal:", "i", 56, CLARO) + [("paralela", "g", 60, BR)], XE, 740, passo=0.1)
        E.frase(c, t, C["s14.d"], [("mais à direita", "g", 52, BR)] + ps("= maior W", "g", 52, E.COR), XE, 840, passo=0.1)
        E.foco(c, t, C["s14.d"] + 0.6, 0.4, lambda a: E.pilula(c, "maior W", P.x(5.5), P.oy - 60, 40, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s14.e"], [("sem", "g", 50, ERRADO)] + ps("gráfico? use a equação", "i", 54, CLARO), XE, 960, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("fótons de", "i", 70)], XE, 340)
    E.foco(c, t, C["s15.a"] + 0.4, 0.5, lambda a: F.medida(c, "6,6", "eV", XE + 330, 340, 90, UV, a))
    E.frase(c, t, C["s15.a"] + 1.2, ps("zinco,", "i", 70) + [("W =", "g", 70)], XE, 460, passo=0.12)
    E.foco(c, t, C["s15.a"] + 1.8, 0.5, lambda a: F.medida(c, "4,3", "eV", XE + 360, 460, 90, TINTA, a))
    E.frase(c, t, C["s15.b"], [("Ec", "g", 76, COR)] + ps("de cada elétron?", "i", 70), XE, 620, passo=0.12)
    E.frase(c, t, C["s15.c"], [("2×", "g", 70, COR)] + ps("a intensidade: o que muda?", "i", 64), XE, 760, passo=0.1)
    if t < C["s16"]:
        placa_metal(c, 1200, 760, 520, 90, ep(t, C["s15.a"], 0.5), "zinco")
        arranca_loop(c, t, C["s15.a"] + 0.4, 1e9, 1.2, 1400, 760, UV)
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.formula_em(c, t, C["s17.a"], "6,6 > 4,3", XE, 260, 110, "g", TINTA)
        E.foco(c, t, C["s17.a"] + 0.6, 0.4, lambda a: E.pilula(c, "o elétron sai", XE + 820, 225, 46, "b", fundo=CERTO, a=a))
        E.formula_em(c, t, C["s17.b"], "Ec = 6,6 − 4,3", XE, 480, 110, "g", TINTA)
        bola_txt(c, t, C["s17.c"], "2,3", "eV", 1400, 600, 170, 100)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("2×", "g", 90, COR)] + ps("a intensidade:", "i", 76) + [("2×", "g", 90, COR), ("fótons", "g", 76)], XE, 240, passo=0.12)
    E.frase(c, t, C["s18.b"], [("2×", "g", 90, COR), ("elétrons", "g", 76, F.NEG)], XE, 400, passo=0.12)
    E.frase(c, t, C["s18.c"], ps("cada um com os mesmos", "i", 70), XE, 560, passo=0.1)
    E.foco(c, t, C["s18.c"] + 1.0, 0.5, lambda a: F.medida(c, "2,3", "eV", XE + 770, 560, 90, CERTO, a))
    E.frase(c, t, C["s18.d"], ps("só a", "i", 70) + [("frequência", "g", 70, COR)] + ps("muda a energia", "i", 70), XE, 760, passo=0.12)
    placa_metal(c, 1260, 900, 480, 80, ep(t, C["s18"], 0.5), "zinco")
    arranca_loop(c, t, C["s18.a"] + 0.5, 1e9, 0.5, 1400, 900, UV)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s19", (("s19.a", [("1 fóton", "g", 70), ("→", "g", 70, TINTA2), ("1 elétron", "g", 70, F.NEG)]),
                                ("s19.b", [("Ec = h · f − W", "g", 76)]),
                                ("s19.c", [("frequência:", "g", 64, COR), ("se sai;", "i", 66), ("intensidade:", "g", 64), ("quantos", "i", 66)])), y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, tela_resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Espectros", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.4, [("e níveis", "g", 110, COR)], XE, 530)
    # escada de níveis com um salto e o fóton saindo
    x0, x1 = 330, 900
    for k, y in enumerate((900, 760, 690)):
        q = ep(t, C["s20.a"] + 0.3 + 0.15 * k, 0.4)
        M.line(c, x0, y, x1, y, TINTA, q, 6)
    if t >= C["s20.b"]:
        F.seta(c, 560, 700, 560, 880, E.COR, 1.0, 8, None, ease_io(prog(t, C["s20.b"], 0.5)))
        foton(c, t, C["s20.b"] + 0.5, (600, 800), (1050, 800), VERM, 1.0, n=3, amp=16, lam=28, largura=5, fica=True)
    inscreva(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, efeito=b_efeito, trabalho=b_trabalho, conta=b_conta, brilho=b_brilho,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
