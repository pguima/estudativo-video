"""Visual — Estudativo · FIS-MOD-001: fóton, a energia em pacotes. Primeira aula da trilha Física Moderna.

LINGUAGEM VISUAL DA FÍSICA MODERNA (todas as FIS-MOD copiam daqui; a da Física inteira está no visual.py da FIS-CIN-001,
a das ondas no da FIS-OND e a da luz no da FIS-OPT-001):
- Matéria: E.usar("Física", "Física Moderna"). Papel claro, uma cor forte por tela (laranja), texto à esquerda (XE) e
  desenho à direita. Atalho no palco escuro, questão com E.relogio, certo = verde e errado = vermelho com risco.
- FÓTON = pacote de onda: um trecho curto de senoide com a ponta em seta, que viaja (foton / pacote). É o raio de luz da
  Óptica (laranja, F.raio) visto de perto: luz genérica é laranja (E.COR). Só quando a COR da luz é o assunto o pacote
  ganha a cor do espectro (cor_luz(nm): vermelho, verde, violeta) ou o violeta do ultravioleta (UV). Comprimento de onda
  e frequência seguem a trilha Ondas: λ e f em grotesca, a onda contínua é F.onda.
- FONTE DE LUZ = esfera âmbar com brilho (LUZ, lampada_fonte / sol), a mesma da Óptica; lâmpada colorida = a cor da luz.
- ELÉTRON = esferinha azul com "−" (eletron, F.NEG); próton e núcleo = laranja com "+" (F.carga). Metal = placa cinza.
- ENERGIA: número + unidade (F.medida), unidade menor e cinza; "eV" e "J" nunca sem número. Constante física (h, c, carga
  do elétron) = cartão pontilhado com o símbolo em laranja e o valor em notação científica (constante).
- NÍVEIS DE ENERGIA (FIS-MOD-003 em diante) = escada de linhas em tinta, com n à esquerda e o valor em eV à direita; o
  salto é uma seta laranja e o fóton sai pelo lado.
- RELATIVIDADE (FIS-MOD-005, 011): quem viaja em petróleo (F.VEL, a nave); quem vê de fora em tinta; γ sempre em laranja.
- CÉU (FIS-MOD-008 a 010): estrelas e galáxias desenhadas dentro de uma janela escura arredondada (ceu), no papel. Não é o
  palco: o palco continua só para atalho.
- Contas: potências de dez com E.formula ("10^{−34}"); letra grega e "=" sempre em grotesca ("g"/"b"), nunca em itálico.
  Resposta final na esfera laranja (bola_txt). Todas as contas da aula ficam em assert no topo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-001_foton_energia_em_pacotes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pacote", "formula", "ev", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
h_, e_ = 6.6e-34, 1.6e-19
assert abs(6.6 * 8 - 52.8) < 1e-9 and -34 + 14 == -20                      # 52,8 × 10⁻²⁰
assert abs(h_ * 8e14 - 5.28e-19) < 1e-30 and abs(5.28 / 1.6 - 3.3) < 1e-9     # 5,28 × 10⁻¹⁹ J = 3,3 eV
assert abs(5.28e-19 * 1.6e-19 - 8.448e-38) < 1e-48                             # o erro: 8,4 × 10⁻³⁸
assert abs(h_ * 4e14 / e_ - 1.65) < 1e-9 and abs(3.3 / 2 - 1.65) < 1e-9        # vermelho: metade, 1,65 eV
assert abs(6.6 * 1.6 - 10.56) < 1e-9 and -34 + 15 == -19 and abs(10.56 / 1.6 - 6.6) < 1e-9   # questão: 6,6 eV
assert 1.6e15 / 4e14 == 4 and abs(4 * 1.65 - 6.6) < 1e-9
assert len("0," + "0" * 33 + "66") - 2 - 2 == 33                               # 6,6 × 10⁻³⁴: 33 zeros antes do 6
assert abs(3e8 / 8e14 - 375e-9) < 1e-15 and abs(3e8 / 4e14 - 750e-9) < 1e-15   # 375 nm (UV) e 750 nm (vermelho)


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
def pele(c, x, y, w, h, queima=0.0, a=1.0):
    """faixa de pele vista de lado; queima (0..1) avermelha"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 18, E.mix("#E8B48A", "#D9483B", queima), a)
    for i in range(6):
        M.line(c, x + 30 + i * (w - 60) / 5, y + 12, x + 30 + i * (w - 60) / 5, y + 26, "#B98057", a * 0.6, 3)


def barra_quente(c, x, y, w, h, k, a=1.0):
    """barra de ferro aquecida: k = 0 vermelho, 0,5 amarelo, 1 branco"""
    if a <= 0:
        return
    cor = E.mix("#C3261B", "#FFC21A", min(1, k * 2)) if k < 0.5 else E.mix("#FFC21A", "#FFF8E8", (k - 0.5) * 2)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(x + w / 2, y + h / 2), w * 0.8, [M.hexc(cor, 0.45 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(x + w / 2, y + h / 2, w * 0.8, p)
    M.rrect(c, x, y, w, h, 14, cor, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14), M.paint(TINTA2, a * 0.6, stroke=3))
    M.line(c, x - 160, y + h / 2, x, y + h / 2, "#55565C", a, 26)  # o cabo da pinça


def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("lâmpada vermelha", "i", 70) + [("fortíssima", "g", 66, VERM)], XE, 210, passo=0.12)
        # lâmpada vermelha → pele sem queimadura
        L1, P1 = (330, 520), (220, 800)
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: lampada_fonte(c, *L1, 70, VERM, a, t))
        E.foco(c, t, C["s01.a"] + 0.6, 0.5, lambda a: pele(c, P1[0], P1[1], 620, 80, 0, a))
        for dx in (-60, 60, 180, 300):
            jorro(c, t, C["s01.a"] + 0.8 + 0.07 * dx / 60, (L1[0] + 40 + dx * 0.3, L1[1] + 70), (L1[0] + dx, P1[1] - 20), VERM, 0.34, 0.8,
                  n=3, amp=14, lam=26, largura=4)
        E.foco(c, t, C["s01.a"] + 2.0, 0.4, lambda a: E.pilula(c, "sem queimadura", P1[0] + 310, P1[1] + 150, 46, "b", fundo=TINTA, a=a))
        # sol → pele queimada
        S, P2 = (1420, 470), (1110, 800)
        E.frase(c, t, C["s01.b"], ps("poucos minutos de", "i", 70) + [("sol", "g", 66, COR)], 1060, 210, passo=0.12)
        E.foco(c, t, C["s01.b"] + 0.3, 0.5, lambda a: sol(c, *S, 90, a, t))
        E.foco(c, t, C["s01.b"] + 0.5, 0.5, lambda a: pele(c, P2[0], P2[1], 620, 80, ep(t, C["s01.b"] + 1.2, 1.2), a))
        for dx in (-140, -20, 100, 220):
            jorro(c, t, C["s01.c"] + 0.07 * (dx + 140) / 60, (S[0] + dx * 0.35, S[1] + 110), (S[0] + dx, P2[1] - 20), UV, 0.42, 0.8,
                  n=3, amp=10, lam=16, largura=4)
        E.foco(c, t, C["s01.b"] + 1.8, 0.4, lambda a: E.pilula(c, "queimadura", P2[0] + 310, P2[1] + 150, 46, "b", fundo=ERRADO, a=a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "ultravioleta", 1700, 300, 46, "g", fundo=UV, a=a))
    E.saida(c, t, C["s01.d"] - 0.15, um)
    if C["s01.d"] - 0.15 <= t < C["s02"]:
        def dois():
            E.frase(c, t, C["s01.d"], ps("a luz chega", "i", 100), W / 2, 420, "center", 0.14)
            E.frase(c, t, C["s01.d"] + 0.5, [("em pacotes", "g", 150, COR)], W / 2, 640, "center")
            for i in range(4):
                foton(c, t, C["s01.d"] + 0.8 + 0.35 * i, (300, 820), (1620, 820), E.COR, 2.2, n=3, amp=26, lam=42, largura=7)
        E.saida(c, t, C["s02"] - 0.1, dois)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a energia de um fóton"), ("s02.b", "joule → elétron-volt"), ("s02.c", "a ideia de Planck")))


def b_lembrete(c, t, C, b):
    def onda(a, x, y):
        F.poli(c, [(x - 110 + i * 3, y + 30 * math.sin(i * 0.18)) for i in range(80)], 1.0, E.COR, a, 6)

    def trabalho(a, x, y):
        M.rrect(c, x - 90, y - 60, 14, 120, 4, F.NEG, a)
        M.rrect(c, x + 80, y - 60, 14, 120, 4, E.COR, a)
        eletron(c, x, y, 22, a)
    lembrete2(c, t, C, "s03", (("s03.b", "a luz é onda, e a velocidade é", "c = λ · f"), ("s03.c", "trabalho da força elétrica", "τ = q · U")),
              (onda, trabalho))


# ---------------- a ideia de Planck ----------------
def rampa_escada(c, t, t0, t1, x, y, a=1.0):
    """à esquerda, rampa com bola em qualquer altura; à direita (t1), escada com bola só nos degraus"""
    E.foco(c, t, t0, 0.5, lambda a: M.line(c, x, y, x + 520, y - 300, TINTA, a, 8))
    if t >= t0 + 0.4:
        u = 0.5 + 0.42 * math.sin((t - t0) * 1.2)
        E.bola(c, x + 520 * u + 18, y - 300 * u - 34, 30, E.COR, ep(t, t0 + 0.4, 0.4))
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: centro(c, "rampa: qualquer altura", x + 260, y + 80, 46, "i", TINTA2, a))
    xs = x + 760
    if t >= t1:
        q = ep(t, t1, 0.5)
        pts = [(xs, y)]
        for k in range(5):
            pts += [(xs + 104 * k, y - 60 * (k + 1)), (xs + 104 * (k + 1), y - 60 * (k + 1))]
        F.poli(c, pts, q, TINTA, 1.0, 8)
        k = int(((t - t1) * 1.1) % 5)
        E.bola(c, xs + 104 * k + 52, y - 60 * (k + 1) - 32, 30, E.COR, ep(t, t1 + 0.4, 0.4))
        E.foco(c, t, t1 + 0.6, 0.4, lambda a: centro(c, "escada: só nos degraus", xs + 260, y + 80, 46, "i", TINTA2, a))


def b_pacote(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 0.2, [("1900", "g", 150, TINTA)], XE, 260)
        E.frase(c, t, C["s04.a"], ps("a luz de um", "i", 76) + [("corpo quente", "g", 72, COR)], XE, 390, passo=0.12)
        k = ep(t, C["s04.b"] + 0.6, 3.0)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: barra_quente(c, 1340, 300, 400, 90, k, a))
        for i, (s, x) in enumerate((("vermelho", 1290), ("amarelo", 1480), ("branco", 1670))):
            E.foco(c, t, C["s04.b"] + 0.8 + 1.0 * i, 0.4, lambda a, s=s, x=x: centro(c, s, x, 470, 44, "i", TINTA2, a))
        E.frase(c, t, C["s04.c"], [("Max", "g", 76), ("Planck", "g", 76, COR)], XE, 560, passo=0.15)
        E.frase(c, t, C["s04.d"], ps("a energia não sai em", "i", 66) + ps("qualquer quantidade", "g", 62), XE, 700, passo=0.1)
        E.frase(c, t, C["s04.e"], ps("sai em", "i", 80) + [("pacotes", "g", 80, COR)], XE, 860, passo=0.14)
        for i in range(3):
            foton(c, t, C["s04.e"] + 0.4 + 0.45 * i, (1000, 820), (1760, 820), E.COR, 1.6, n=3, amp=24, lam=40, largura=7)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return

    def rampa():
        rampa_escada(c, t, C["s05.a"], C["s05.b"], 260, 560)
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "quantização: energia em degraus", W / 2, 760, 56, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s05.d"] - 0.15, rampa)
    if t < C["s05.d"]:
        return
    E.frase(c, t, C["s05.d"], [("1905", "g", 130, TINTA), ("Einstein:", "g", 80, TINTA)], XE, 330, passo=0.3)
    E.frase(c, t, C["s05.d"] + 1.0, ps("a própria luz é feita de pacotes", "i", 76), XE, 470, passo=0.1)
    E.frase(c, t, C["s05.e"] - 1.6, ps("o pacote de luz se chama", "i", 84), XE, 650, passo=0.12)
    E.frase(c, t, C["s05.e"], [("fóton", "g", 170, COR)], XE, 840)
    E.foco(c, t, C["s05.e"] + 0.8, 0.5, lambda a: pacote(c, 1500, 840, 0, E.COR, a, n=3, amp=46, lam=84, largura=10))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06.a"], ps("energia de", "i", 76) + [("um fóton", "g", 72, COR)], XE, 200, passo=0.12)
        F.formula_legenda(c, t, C["s06.b"], "E = h · f", [("f", "frequência", "Hz"), ("E", "energia", "J"), ("h", "constante de Planck", "J·s")],
                          XE, 400, 150, tl=[C["s06.c"], C["s06.d"], C["s06.e"]], size_l=56)
        constante(c, t, C["s06.e"] + 0.8, 1090, 640, "constante de Planck", "h =", "6,6 × 10^{−34} J·s", 66)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return

    def s07a():
        E.frase(c, t, C["s07"], ps("confira pela unidade", "i", 76), XE, 200, passo=0.12)
        cs = F.unidades(c, t, C["s07"] + 0.4, [("E", "J"), ("=", None), ("h", "J·s"), ("·", None), ("f", "1/s")], W / 2, 420, 140, C["s07.a"])
        if t >= C["s07.b"]:
            yu = 420 + 140 * 0.95
            for k, x in enumerate((cs[2] + 50, cs[4] + 40)):
                M.line(c, x - 22, yu + 8, x + 22, yu - 52, E.COR, 1.0, 7, progress=ep(t, C["s07.b"] + 0.2 * k, 0.35))
            E.foco(c, t, C["s07.b"] + 0.6, 0.5, lambda a: E.pilula(c, "sobra joule", W / 2 + 280, 720, 50, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s07.c"] - 0.15, s07a)
    if t < C["s07.c"]:
        return
    E.frase(c, t, C["s07.c"], [("h", "g", 80, COR), ("=", "g", 80, TINTA2)], XE, 300, passo=0.1)
    zeros = "0," + "0" * 33 + "66"
    for i, ch in enumerate(zeros):
        x = XE + 160 + i * 41
        ti = C["s07.c"] + 0.3 + 0.035 * i
        cor = COR if ch == "6" else TINTA
        E.foco(c, t, ti, 0.25, lambda a, ch=ch, x=x, cor=cor: E.escreve(c, ch, x, 300, 64, "g", cor, a), sobe=6, blur=6)
    E.foco(c, t, C["s07.c"] + 1.8, 0.4, lambda a: E.chave(c, XE + 160 + 2 * 41, XE + 160 + 35 * 41 - 6, 330, TINTA2, 1.0, 40))
    E.foco(c, t, C["s07.c"] + 2.0, 0.4, lambda a: centro(c, "33 zeros", XE + 160 + 18.5 * 41, 440, 52, "g", TINTA2, a))
    E.frase(c, t, C["s07.d"], ps("um fóton:", "i", 70) + [("pouquíssima", "g", 66, COR)] + ps("energia", "i", 70), XE, 620, passo=0.12)
    E.foco(c, t, C["s07.e"], 0.5, lambda a: lampada_fonte(c, 330, 860, 70, LUZ, a, t))
    jorro(c, t, C["s07.e"] + 0.3, (420, 860), (1500, 860), E.COR, 0.16, 1.0, n=2, amp=14, lam=26, largura=4)
    for dy in (-60, 60):
        jorro(c, t, C["s07.e"] + 0.38, (420, 860 + dy * 0.3), (1500, 860 + dy), E.COR, 0.19, 1.0, n=2, amp=14, lam=26, largura=4)
    E.foco(c, t, C["s07.e"] + 0.8, 0.5, lambda a: E.pilula(c, "bilhões de bilhões por segundo", 1520, 1000, 44, "b", fundo=TINTA, a=a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    E.frase(c, t, C["s08"], [("ultravioleta", "g", 76, UV)], XE, 200)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (E.escreve(c, "f =", XE + 560, 200, 76, "g", TINTA2, a),
                                             E.formula(c, "8 × 10^{14} Hz", XE + 700, 200, 76, "g", TINTA, a)))
    foton(c, t, C["s08.a"] + 0.4, (1500, 180), (1820, 180), UV, 1.2, n=3, amp=12, lam=18, largura=4, fica=True)
    linhas = [(C["s08.b"], "6,6 × 8 = 52,8"), (C["s08.c"], "10^{−34} · 10^{14} = 10^{−20}"), (C["s08.d"], "E = 52,8 × 10^{−20} J")]
    E.formula_em(c, t, C["s08"] + 1.2, "E = h · f = 6,6 × 10^{−34} · 8 × 10^{14}", XE, 360, 70, "g", TINTA)
    for i, (ti, s) in enumerate(linhas):
        E.formula_em(c, t, ti, s, XE + 80, 500 + 120 * i, 70, "g", TINTA2 if i < 2 else TINTA)
    if t >= C["s08.e"] - 0.3:
        E.foco(c, t, C["s08.e"] - 0.3, 0.4, lambda a: E.pilula(c, "vírgula ← 1 casa, expoente +1", 1380, 740, 40, "b", fundo=TINTA2, a=a))
    bola_txt_f(c, t, C["s08.e"], "5,28 × 10^{−19}", "J", W / 2 + 300, 930, 92, 66)


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


# ---------------- elétron-volt ----------------
def placas(c, t, t0, x, y, h, gap, a_e=True):
    """duas placas: − à esquerda (0 V), + à direita (1 V); o elétron atravessa de uma para a outra"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, x, y, 22, h, 6, F.NEG, q)
    M.rrect(c, x + gap, y, 22, h, 6, E.COR, q)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: (centro(c, "0 V", x + 11, y + h + 70, 48, "b", TINTA2, a), centro(c, "1 V", x + gap + 11, y + h + 70, 48, "b", TINTA2, a)))
    if a_e:
        u = ease_io(prog(t, t0 + 0.8, 1.6))
        eletron(c, lerp(x + 70, x + gap - 50, u), y + h / 2, 30, q)


def b_ev(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09.a"], [("5,28", "g", 76), ("×", "g", 76, TINTA2)], XE, 230, passo=0.08)
        E.foco(c, t, C["s09.a"] + 0.2, 0.4, lambda a: E.formula(c, "10^{−19} J", XE + 290, 230, 76, "g", TINTA, a))
        E.foco(c, t, C["s09.a"] + 0.8, 0.4, lambda a: E.pilula(c, "minúsculo", XE + 900, 205, 46, "b", fundo=TINTA2, a=a))
        E.frase(c, t, C["s09.b"], ps("unidade do átomo:", "i", 70) + [("elétron-volt", "g", 80, COR), ("(eV)", "b", 60, TINTA2)], XE, 370, passo=0.12)
        placas(c, t, C["s09.c"], 1180, 470, 280, 520)
        E.frase(c, t, C["s09.c"] + 0.3, ps("levar a carga de um elétron", "i", 58) , XE, 500, passo=0.08)
        E.frase(c, t, C["s09.c"] + 1.0, ps("por", "i", 58) + [("1 volt", "g", 58, COR)], XE, 580, passo=0.12)
        E.formula_em(c, t, C["s09.d"], "τ = q · U", XE, 720, 76, "g", TINTA)
        E.formula_em(c, t, C["s09.e"], "= 1,6 × 10^{−19} C · 1 V", XE + 330, 720, 76, "g", TINTA2)
        E.foco(c, t, C["s09.f"], 0.5, lambda a: (E.formula(c, "1 eV", XE, 900, 100, "g", COR, a),
                                                 E.formula(c, "= 1,6 × 10^{−19} J", XE + 250, 900, 100, "g", TINTA, a)))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10"], [("J", "g", 80, TINTA), ("→", "g", 80, TINTA2), ("eV:", "g", 80, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s10.a"], [("divida", "g", 76)] + ps("por", "i", 80), XE + 420, 220, passo=0.12)
    E.foco(c, t, C["s10.a"] + 0.4, 0.4, lambda a: E.formula(c, "1,6 × 10^{−19}", XE + 880, 220, 76, "g", COR, a))
    cx, y = 520, 480
    E.formula_em(c, t, C["s10.a"] + 0.8, "f{5,28 × 10^{−19}}{1,6 × 10^{−19}}", cx, y, 110, "g", TINTA, "center")
    if t >= C["s10.b"]:
        for yy in (y - 50, y + 50):
            E.risco(c, cx + 50, yy + 30, cx + 290, yy - 30, t, C["s10.b"] + (0.2 if yy > y else 0), E.COR, 8)
    E.formula_em(c, t, C["s10.c"], "= f{5,28}{1,6}", cx + 360, y, 110, "g", TINTA2, "left")
    bola_txt(c, t, C["s10.d"], "3,3", "eV", 1560, 460, 150, 96)
    E.frase(c, t, C["s10.e"], ps("o fóton ultravioleta tem", "i", 70) + [("3,3 eV", "g", 70, UV)], W / 2, 850, "center", 0.1)


# ---------------- brilho não é energia ----------------
def molecula(c, cx, cy, s, quebra=0.0, a=1.0):
    """molécula da pele: duas bolas ligadas; quebra (0..1) separa as duas"""
    if a <= 0:
        return
    d = s * (0.8 + 1.4 * quebra)
    if quebra < 0.3:
        M.line(c, cx - d / 2, cy, cx + d / 2, cy, TINTA2, a * (1 - quebra * 3), 10)
    E.bola(c, cx - d / 2, cy - 30 * quebra, s * 0.42, "#6C7A89", a)
    E.bola(c, cx + d / 2, cy + 30 * quebra, s * 0.42, "#6C7A89", a)


def b_brilho(c, t, C, b):
    E.frase(c, t, C["s11.a"], ps("luz mais forte =", "i", 76) + [("mais fótons", "g", 76, COR)], XE, 210, passo=0.12)
    E.frase(c, t, C["s11.b"], [("não", "g", 76, ERRADO)] + ps("fótons mais fortes", "i", 76), XE, 330, passo=0.12)
    E.frase(c, t, C["s11.c"], ps("energia de cada fóton: só a", "i", 64) + [("frequência", "g", 64, COR)], XE, 450, passo=0.1)
    # dois quadros: muitos fótons vermelhos não quebram; um ultravioleta quebra
    for i, (x, cor, k, periodo) in enumerate(((180, VERM, 0, 0.18), (1000, UV, 1, 9.0))):
        p = ep(t, C["s11.d"], 0.5)
        E.caixa_pontilhada(c, x, 540, 740, 440, p, prog_=p)
        if t >= C["s11.d"]:
            M_ = (x + 560, 760)
            E.foco(c, t, C["s11.d"] + 0.2, 0.4, lambda a, M_=M_, i=i: molecula(c, *M_, 120, ep(t, C["s11.d"] + 2.2, 0.6) if i else 0, a))
            jorro(c, t, C["s11.d"] + 0.4 + (1.2 if i else 0), (x + 60, 760), (M_[0] - 70, 760), cor, periodo, 1.0,
                  n=3, amp=14 if not i else 10, lam=26 if not i else 16, largura=4)
            E.foco(c, t, C["s11.d"] + 0.3, 0.4, lambda a, x=x, i=i: E.escreve(c, ("muitos fótons fracos" if not i else "um fóton forte"), x + 40, 620, 46, "i", TINTA, a))
    E.foco(c, t, C["s11.d"] + 2.6, 0.4, lambda a: E.selo(c, 1000 + 680, 920, 40, True, a))
    E.foco(c, t, C["s11.e"], 0.4, lambda a: (E.selo(c, 180 + 680, 920, 40, False, a),
                                             E.escreve(c, "não somam", 180 + 40, 940, 50, "g", ERRADO, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("multiplicar na conversão", "i", 76), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "5,28 × 10^{−19} · 1,6 × 10^{−19}", W / 2, 400, 84, "g", TINTA, "center")
    E.formula_em(c, t, C["s12.c"], "= 8,4 × 10^{−38} eV ?", W / 2, 540, 84, "g", ERRADO, "center")
    if t >= C["s12.c"] + 0.9:
        E.risco(c, W / 2 - 400, 560, W / 2 + 400, 470, t, C["s12.c"] + 0.9, largura=12)
    E.frase(c, t, C["s12.d"], [("eV", "g", 70, COR)] + ps("é uma unidade", "i", 70) + [("minúscula", "g", 66)], XE, 720, passo=0.12)
    E.frase(c, t, C["s12.e"], ps("unidade menor", "i", 66) + [("→", "g", 66, TINTA2), ("número maior", "g", 66, CERTO)], XE, 840, passo=0.12)
    E.foco(c, t, C["s12.e"] + 1.4, 0.5, lambda a: (F.medida(c, 1, "m", 1260, 840, 80, TINTA, a), E.escreve(c, "=", 1400, 840, 80, "g", TINTA2, a),
                                                   F.medida(c, 100, "cm", 1470, 840, 80, CERTO, a)))
    E.foco(c, t, C["s12.e"] + 2.0, 0.5, lambda a: (F.medida(c, "5,28 × 10⁻¹⁹", "J", W / 2 - 40, 990, 64, TINTA, a, "right"),
                                                   E.escreve(c, "=", W / 2 + 10, 990, 64, "g", TINTA2, a),
                                                   F.medida(c, "3,3", "eV", W / 2 + 80, 990, 64, CERTO, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], [("E", "g", 90, BR), ("e", "i", 90, CLARO), ("f:", "g", 90, BR)] + ps("diretamente proporcionais", "g", 64, CLARO),
                W / 2, 300, "center", 0.12)
        E.frase(c, t, C["s13.b"], [("2×", "g", 90, E.COR), ("f", "g", 90, BR), ("→", "g", 90, CLARO), ("2×", "g", 90, E.COR), ("E", "g", 90, BR)],
                W / 2, 440, "center", 0.15)
        # barras: frequência e energia do vermelho e do ultravioleta
        for i, (cor, nome, fq, ev, tt) in enumerate(((VERM, "vermelho", "4 × 10^{14} Hz", "1,65 eV", C["s13.c"]),
                                                     (UV, "ultravioleta", "8 × 10^{14} Hz", "3,3 eV", C["s13.c"] - 0.6))):
            y = 820 - i * 170
            q = ease_io(prog(t, tt, 0.7))
            if q > 0:
                M.rrect(c, 560, y - 60, 560 * (0.5 if i == 0 else 1.0) * q, 80, 16, cor, 1.0)
                E.foco(c, t, tt, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, 160, y, 54, "i", CLARO, a))
                E.foco(c, t, tt + 0.5, 0.4, lambda a, fq=fq, y=y: E.formula(c, fq, 580, y - 4, 44, "b", BR, a))
                tv = C["s13.d"] if i == 0 else C["s13.c"]
                E.foco(c, t, tv, 0.4, lambda a, ev=ev, y=y: E.escreve(c, ev, 1240, y, 72, "g", E.COR if i == 0 else BR, a))
        E.foco(c, t, C["s13.d"] + 0.6, 0.4, lambda a: E.pilula(c, "metade", 1620, 795, 48, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], ps("velocidade da luz fixa:", "i", 66, CLARO), W / 2, 180, "center")
    E.frase(c, t, C["s14.a"], [("λ", "g", 84, BR), ("maior", "g", 70, BR), ("→", "g", 84, CLARO), ("f", "g", 84, BR), ("menor", "g", 70, BR),
                               ("→", "g", 84, CLARO), ("fóton", "g", 70, BR), ("mais fraco", "g", 70, E.COR)], W / 2, 320, "center", 0.12)
    # faixa do espectro, do vermelho ao violeta
    q = ease_io(prog(t, C["s14.b"], 0.9))
    x0, x1, y = 300, 1620, 470
    if q > 0:
        n = 120
        for i in range(int(n * q)):
            nm = 750 - (750 - 400) * i / n
            M.rrect(c, x0 + (x1 - x0) * i / n, y, (x1 - x0) / n + 1, 110, 0, cor_luz(nm), 1.0)
        E.foco(c, t, C["s14.b"] + 0.5, 0.4, lambda a: (E.escreve(c, "vermelho", x0, y + 170, 50, "i", CLARO, a),
                                                       E.escreve(c, "violeta", x1 - E.larg("violeta", "i", 50), y + 170, 50, "i", CLARO, a)))
        F.seta(c, x0 + 200, y + 240, x1 - 200, y + 240, BR, ep(t, C["s14.b"] + 0.8, 0.4), 8, None, ease_io(prog(t, C["s14.b"] + 0.8, 0.8)))
        E.foco(c, t, C["s14.b"] + 1.4, 0.4, lambda a: centro(c, "fóton mais forte", W / 2, y + 330, 60, "g", E.COR, a))
    E.frase(c, t, C["s14.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("números sem relação simples:", "i", 60, CLARO) + [("h · f", "g", 60, BR)],
            W / 2, 1000, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("lâmpada", "i", 76) + [("ultravioleta", "g", 70, UV)], XE, 340, passo=0.12)
    E.foco(c, t, C["s15.a"] + 0.6, 0.5, lambda a: (E.escreve(c, "f =", XE, 470, 80, "g", TINTA2, a), E.formula(c, "1,6 × 10^{15} Hz", XE + 150, 470, 80, "g", TINTA, a)))
    E.frase(c, t, C["s15.b"], ps("energia do fóton", "i", 70) + [("em J", "g", 64), ("e", "i", 70), ("em eV?", "g", 64, COR)], XE, 610, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("quantas vezes a do", "i", 64) + [("vermelho", "g", 60, VERM)], XE, 750, passo=0.12)
    E.foco(c, t, C["s15.c"] + 1.2, 0.4, lambda a: (E.escreve(c, "f =", XE, 860, 64, "g", TINTA2, a), E.formula(c, "4 × 10^{14} Hz?", XE + 125, 860, 64, "g", TINTA, a)))
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: lampada_fonte(c, 1460, 460, 110, UV, a, t))
        jorro(c, t, C["s15.a"] + 0.4, (1460, 600), (1460, 960), UV, 0.5, 1.0, n=3, amp=10, lam=16, largura=4)
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.formula_em(c, t, C["s17"] + 0.4, "E = 6,6 × 10^{−34} · 1,6 × 10^{15}", XE, 220, 72, "g", TINTA)
        E.formula_em(c, t, C["s17.a"], "6,6 × 1,6 = 10,56", XE + 80, 360, 70, "g", TINTA2)
        E.formula_em(c, t, C["s17.b"], "10^{−34} · 10^{15} = 10^{−19}", XE + 80, 480, 70, "g", TINTA2)
        bola_txt_f(c, t, C["s17.c"], "10,56 × 10^{−19}", "J", 640, 650, 92, 64)
        E.formula_em(c, t, C["s17.d"], "f{10,56 × 10^{−19}}{1,6 × 10^{−19}}", 1300, 680, 76, "g", TINTA, "center")
        if t >= C["s17.d"] + 0.8:
            for yy in (640, 720):
                E.risco(c, 1310, yy + 20, 1500, yy - 26, t, C["s17.d"] + 0.8 + (0.2 if yy > 650 else 0), E.COR, 7)
        bola_txt(c, t, C["s17.e"], "6,6", "eV", 1300, 900, 120, 76)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], ps("pelo atalho:", "i", 76, COR), XE, 200)
    E.formula_em(c, t, C["s18.b"], "1,6 × 10^{15} = 16 × 10^{14}", XE, 360, 84, "g", TINTA)
    E.formula_em(c, t, C["s18.c"], "16 ÷ 4 = 4", XE, 500, 84, "g", TINTA)
    E.frase(c, t, C["s18.d"], [("4×", "g", 100, COR), ("a", "i", 90), ("frequência", "i", 90)], XE, 680, passo=0.12)
    E.frase(c, t, C["s18.d"] + 0.9, [("4×", "g", 100, COR), ("a", "i", 90), ("energia", "i", 90)], XE, 810, passo=0.12)
    E.formula_em(c, t, C["s18.e"], "4 × 1,65 = 6,6 eV", 1300, 760, 84, "g", CERTO, "center")
    E.foco(c, t, C["s18.e"] + 0.8, 0.4, lambda a: E.selo(c, 1300, 560, 70, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s19", (("s19.a", [("a luz vem em", "i", 70), ("fótons", "g", 70, COR)]),
                                ("s19.b", [("E = h · f", "g", 76)]),
                                ("s19.c", [("J", "g", 70), ("→", "g", 70, TINTA2), ("eV:", "g", 70, COR), ("÷ 1,6 × 10⁻¹⁹", "g", 70)])), y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, tela_resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Efeito", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.4, [("fotoelétrico", "g", 110, COR)], XE, 530)
    placa_metal(c, 330, 800, 640, 90, ep(t, C["s20.a"], 0.5), "metal")
    foton(c, t, C["s20.a"] + 0.6, (360, 620), (620, 790), UV, 0.9, n=3, amp=10, lam=16, largura=4)
    if t >= C["s20.a"] + 1.5:
        u = ease_out(prog(t, C["s20.a"] + 1.5, 1.2))
        eletron(c, lerp(660, 1000, u), lerp(780, 640, u), 26, min(1, u * 4))
    E.frase(c, t, C["s20.b"], ps("a cor importa mais que o", "i", 56) + [("brilho", "g", 56, COR)], XE, 990, passo=0.1)
    inscreva(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pacote=b_pacote, formula=b_formula, exemplo=b_exemplo, ev=b_ev, brilho=b_brilho,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
