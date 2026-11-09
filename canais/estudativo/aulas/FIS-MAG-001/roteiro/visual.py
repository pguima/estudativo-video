"""Visual — Estudativo · FIS-MAG-001: ímãs e campo magnético. Primeira aula da trilha Magnetismo.

LINGUAGEM VISUAL DO MAGNETISMO (as aulas FIS-MAG-* copiam daqui; a base é a da Física, no visual.py da FIS-CIN-001):
- Matéria: E.usar("Física", "Magnetismo"). Laranja, órbita, papel claro, uma cor forte por tela, texto à esquerda (XE).
- POLOS: norte em laranja (E.COR), sul em azul (F.NEG), sempre com a letra N ou S em branco (F.ima). Ímã em barra deitado
  com o norte à direita é a posição padrão; norte à esquerda = o mesmo desenho espelhado (espelho()).
- CAMPO B: linhas de campo em cinza-tinta (TINTA2) com setas, saindo do N e entrando no S por fora (F.linhas_campo);
  por dentro do ímã, tracejadas. O vetor bê é seta em tinta (TINTA) com a letra-vetor B. A letra B nunca é laranja: laranja
  é força. Campo que fura a folha: grade de símbolos em tinta, ponto no círculo = saindo, xis no círculo = entrando
  (folha_campo, aulas 002 em diante).
- BÚSSOLA (bussola): caixa branca com aro em tinta e agulha losango, metade norte laranja e metade sul azul. A agulha gira
  até o sentido do campo calculado de verdade (campo_dip, dois polos), nunca num ângulo chutado.
- CORRENTE (aulas 002 em diante): fio em tinta com as setinhas laranja andando (F.corrente) e a letra i; sentido
  convencional, o mesmo de FIS-ELE. FORÇA: seta grossa laranja com F (F.forca/F.vetor). VELOCIDADE: petróleo (F.VEL).
  Carga + laranja e − azul (F.carga), como no campo elétrico.
- MÃO DIREITA (aulas 002 em diante): desenho simples da mão, em tom de pele claro com contorno em tinta; cada dedo leva a
  pílula da grandeza que aponta (polegar i ou v; dedos B; palma F).
- FLUXO (aulas 005 em diante): a área da espira pintada de laranja claro, com as linhas de campo atravessando.
- USINAS (aulas 009 em diante): cadeia de energia = pílulas em fila ligadas por setas; a última, "elétrica", em laranja.
  Água em azul claro (#7FC8E8), como o rio da FIS-CIN-001.
- Certo = verde, errado = vermelho com risco. Atalho no palco escuro. Questão com E.relogio. Mínimo de 40 px.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-001_imas_e_campo_magnetico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("polos", "linhas", "bussola", "partido", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG

# sem contas nesta aula: os asserts conferem a geometria que a aula afirma
# (a agulha à direita do norte aponta para a direita; o pedaço partido tem S na ponta quebrada)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do magnetismo ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def polos_ima(cx, cy, w, sentido=1):
    """dois polos para o cálculo do campo: N em +sentido"""
    return [(cx + sentido * w * 0.36, cy, 1.0), (cx - sentido * w * 0.36, cy, -1.0)]


def campo_dip(x, y, polos):
    """direção do campo (vetor unitário de tela) num ponto: soma de polos q/r², N = +1, S = −1"""
    bx = by = 0.0
    for px, py, q in polos:
        dx, dy = x - px, y - py
        r = max(8.0, math.hypot(dx, dy))
        bx += q * dx / r ** 3
        by += q * dy / r ** 3
    n = math.hypot(bx, by) or 1.0
    return bx / n, by / n


def ang_tela(ux, uy):
    """vetor de tela → ângulo da Física (graus, 90 = para cima)"""
    return math.degrees(math.atan2(-uy, ux))


# conferência da geometria: à direita do norte, o campo aponta para a direita; perto do sul, aponta para o sul
assert abs(ang_tela(*campo_dip(1300, 540, polos_ima(960, 540, 400)))) < 1
assert abs(abs(ang_tela(*campo_dip(600, 540, polos_ima(960, 540, 400)))) - 0) < 1  # à esquerda do S, o campo entra no S: para a direita


def bussola(c, cx, cy, r, ang, a=1.0, escuro=False):
    """bússola: caixa redonda e agulha; ang = para onde aponta o norte da agulha (graus da Física, 0 = direita)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#1B1B22" if escuro else BR, a))
    c.drawCircle(cx, cy, r, M.paint(BR if escuro else TINTA, a, stroke=max(3, r * 0.08)))
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    nx, ny = -uy, ux
    L, wd = r * 0.8, r * 0.22
    for s, cor in ((1, E.COR), (-1, NEG)):
        p = skia.Path()
        p.moveTo(cx + ux * L * s, cy + uy * L * s)
        p.lineTo(cx + nx * wd, cy + ny * wd)
        p.lineTo(cx - nx * wd, cy - ny * wd)
        p.close()
        c.drawPath(p, M.paint(cor, a))
    c.drawCircle(cx, cy, r * 0.1, M.paint(TINTA if not escuro else BR, a))


def gira(t, t0, de, para, d=0.8):
    """ângulo que gira de `de` para `para` a partir de t0, pelo caminho mais curto"""
    dif = (para - de + 180) % 360 - 180
    return de + dif * ease_io(prog(t, t0, d))


def espelho(c, cx, fn):
    """desenha fn espelhado na vertical x = cx (ímã com o norte à esquerda)"""
    c.save(); c.translate(cx, 0); c.scale(-1, 1); c.translate(-cx, 0)
    fn()
    c.restore()


def mini_ima(c, cx, cy, w, h, a=1.0, letras=False, norte_dir=True):
    """ímã pequeno: metade sul azul e norte laranja (à direita, ou à esquerda com norte_dir=False)"""
    if a <= 0:
        return
    k = 1 if norte_dir else -1
    M.rrect(c, cx - w / 2, cy - h / 2, w / 2, h, 5, NEG if k > 0 else E.COR, a)
    M.rrect(c, cx, cy - h / 2, w / 2, h, 5, E.COR if k > 0 else NEG, a)
    if letras:
        E._meio(c, "S", cx - k * w / 4, cy, h * 0.55, "g", BR, a)
        E._meio(c, "N", cx + k * w / 4, cy, h * 0.55, "g", BR, a)


def barra(c, cx, cy, w=360, h=110, a=1.0, ang=0.0, letras=True):
    """ímã em barra parado com o norte no sentido ang (graus da Física: 0 = direita, 90 = cima); letras sempre em pé"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-ang)
    for lado, cor in ((1, E.COR), (-1, NEG)):
        x0 = 0 if lado > 0 else -w / 2
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, -h / 2), skia.Point(0, h / 2)],
                                                   [M.hexc(E.mix(cor, BR, 0.2), a), M.hexc(E.mix(cor, "#000000", 0.2), a)]))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, -h / 2, w / 2, h), 10, 10), p)
    c.restore()
    if letras:
        ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
        sz = min(h, w / 2) * 0.55
        E._meio(c, "N", cx + ux * w / 4, cy + uy * w / 4, sz, "g", BR, a)
        E._meio(c, "S", cx - ux * w / 4, cy - uy * w / 4, sz, "g", BR, a)


def ima_parado(c, cx, cy, w=360, h=110, a=1.0):
    barra(c, cx, cy, w, h, a)


def ferradura(c, cx, cy, s, a=1.0):
    """ímã de ferradura com as pontas para cima: N à esquerda, S à direita; devolve as pontas (xN, xS, y)"""
    if a > 0:
        larg_, alto = s * 0.34, s * 1.0
        for lado, cor, letra in ((-1, E.COR, "N"), (1, NEG, "S")):
            x0 = cx + lado * s * 0.62 - larg_ / 2
            M.rrect(c, x0, cy - alto, larg_, alto * 0.62, 8, cor, a)
            E._meio(c, letra, x0 + larg_ / 2, cy - alto + alto * 0.24, larg_ * 0.62, "g", BR, a)
        pt = M.paint("#8A8A96", a, stroke=larg_)
        c.drawArc(skia.Rect.MakeXYWH(cx - s * 0.62, cy - alto * 0.62 - s * 0.62 + alto * 0.24, s * 1.24, s * 1.24), 0, 180, False, pt)
        for lado in (-1, 1):
            M.rrect(c, cx + lado * s * 0.62 - larg_ / 2, cy - alto * 0.4, larg_, alto * 0.18, 4, "#8A8A96", a)
    return cx - s * 0.62 + s * 0.17, cx + s * 0.62 - s * 0.17, cy - alto * 0.66 if a > 0 else 0


def terra(c, cx, cy, r, a=1.0):
    """a Terra: esfera azul com continentes, eixo e os nomes dos polos geográficos"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#2F7FC2", a)
    for dx, dy, k in ((-0.3, -0.2, 0.32), (0.3, 0.25, 0.26), (0.05, -0.55, 0.18), (-0.25, 0.5, 0.15)):
        c.drawCircle(cx + dx * r, cy + dy * r, k * r, M.paint("#3FA45B", 0.8 * a))


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas (o mesmo da FIS-CIN-001): itens = [(cue, linha fina, linha forte)]"""
    E.frase(c, t, C[cena] + 0.2, ps("lembre", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        cx, cy, w, h = 1240, 520, 620, 150
        tb = C["s01.b"]
        sep = 90 * ease_out(prog(t, tb, 0.5))
        # o ímã inteiro, depois as duas metades
        if t < tb:
            F.ima(c, t, C["s01.a"], cx, cy, w, h)
        else:
            for lado in (-1, 1):
                x0 = cx + lado * (w / 4 + sep)
                F.ima(c, 99, 0, x0, cy, w / 2, h) if t >= C["s01.d"] else None
                if t < C["s01.d"]:
                    cor = NEG if lado < 0 else E.COR
                    M.rrect(c, x0 - w / 4, cy - h / 2, w / 2, h, 10, cor)
                    E._meio(c, "S" if lado < 0 else "N", x0, cy, h * 0.55, "g", BR)
            # a pergunta: só norte? só sul?
            if t < C["s01.c"] + 0.4:
                for lado, s in ((-1, "só sul?"), (1, "só norte?")):
                    E.foco(c, t, tb + 1.2 + (0.6 if lado < 0 else 0), 0.4,
                           lambda a, lado=lado, s=s: centro(c, s, cx + lado * (w / 4 + 90), cy + h + 40, 52, "i", TINTA2, a))
            E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "dois ímãs inteiros", cx, cy + h + 70, 50, "g", fundo=CERTO, a=a))
        if t >= tb:  # a linha do corte
            M.line(c, cx, cy - h, cx, cy + h, ERRADO, 1 - ep(t, tb + 0.4, 0.4), 6, dash=E.TRACO)
        E.frase(c, t, C["s01.a"], ps("quebre o ímã", "i", 88) + [("ao meio", "g", 88, COR)], XE, 230, passo=0.14)
        E.frase(c, t, C["s01.c"], [("não!", "g", 130, ERRADO)], XE, 860)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.a", "linhas de campo", 1.4), ("s02.b", "a bússola", 0), ("s02.c", "o ímã partido", 0))
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 84, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def linhas(a, x, y):
        for cx, s in ((x - 110, "+"), (x + 70, "−")):
            pass
        k = 0.55
        c.save(); c.translate(x - 30, y); c.scale(k, k)
        F.campo_carga(c, 99, 0, -150, 0, 60, 130, 8, True)
        F.campo_carga(c, 99, 0, 150, 0, 60, 130, 8, False)
        F.carga(c, 99, 0, -150, 0, 46, "+")
        F.carga(c, 99, 0, 150, 0, 46, "−")
        c.restore()

    def juntas(a, x, y):
        for i in range(7):
            yy = y - 95 + i * 22
            M.line(c, x - 150, yy, x - 40, yy, TINTA2, a, 4)
        for i in range(3):
            yy = y - 95 + i * 66
            M.line(c, x + 30, yy, x + 140, yy, TINTA2, a, 4)
        E.escreve(c, "forte", x - 150, y + 90, 40, "b", COR, a)
        E.escreve(c, "fraco", x + 30, y + 90, 40, "b", TINTA2, a)
    lembrete2(c, t, C, "s03", (("s03.b", "linhas de força:", "da + para a −"), ("s03.c", "linhas mais juntas,", "campo mais forte")),
              (linhas, juntas))


# ---------------- polos ----------------
def b_polos(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("todo ímã tem", "i", 84) + [("dois", "g", 84, COR), ("polos", "g", 84, COR)], XE, 220, passo=0.14)
        cx, cy = 960, 420
        if t < C["s04.d"] - 0.2:
            F.ima(c, t, C["s04.a"], cx, cy, 700, 170)
            E.foco(c, t, C["s04.b"], 0.4, lambda a: centro(c, "polo norte", cx + 175, cy + 160, 56, "g", COR, a))
            E.foco(c, t, C["s04.c"], 0.4, lambda a: centro(c, "polo sul", cx - 175, cy + 160, 56, "g", NEG, a))
        # norte com norte: se empurram; norte com sul: se puxam
        for k, y, iguais in (("s04.d", 640, True), ("s04.e", 880, False)):
            if t < C[k]:
                continue
            q = ease_out(prog(t, C[k], 0.9))
            gap = 60 + (160 * q if iguais else -40 * q)
            xa, xb = 960 - gap / 2 - 200, 960 + gap / 2 + 200
            E.foco(c, t, C[k], 0.4, lambda a, xa=xa, y=y: ima_parado(c, xa, y, 400, 110, a))
            if iguais:
                E.foco(c, t, C[k], 0.4, lambda a, xb=xb, y=y: barra(c, xb, y, 400, 110, a, 180))
            else:
                E.foco(c, t, C[k], 0.4, lambda a, xb=xb, y=y: ima_parado(c, xb, y, 400, 110, a))
            rot = "N com N: se empurram" if iguais else "N com S: se puxam"
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, rot=rot, y=y, iguais=iguais: E.escreve(c, rot, XE, y - 80, 48, "b", ERRADO if iguais else CERTO, a))
            for lado in (-1, 1):
                x0 = 960 + lado * (gap / 2 + 420)
                xa_, xb_ = (x0, x0 + lado * 110) if iguais else (x0 + lado * 130, x0 + lado * 20)
                F.seta(c, xa_, y, xb_, y, TINTA, ep(t, C[k] + 0.5, 0.3), 8, p=ep(t, C[k] + 0.5, 0.4))
        return
    E.frase(c, t, C["s05"], ps("a mesma regra das", "i", 80) + [("cargas", "g", 80, COR)], W / 2, 210, "center", 0.12)
    for i, (k, s, cor) in enumerate((("s05.a", "iguais se repelem", ERRADO), ("s05.b", "diferentes se atraem", CERTO))):
        x = 520 + i * 880
        E.foco(c, t, C[k], 0.5, lambda a, x=x, i=i: (F.carga(c, 99, 0, x - 110, 420, 60, "+"), F.carga(c, 99, 0, x + 110, 420, 60, "+" if i == 0 else "−")))
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x, i=i: (mini_ima(c, x - 130, 580, 200, 64, a, True),
                                                           mini_ima(c, x + 130, 580, 200, 64, a, True, i != 0)))
        E.frase(c, t, C[k] + 0.2, [(s, "g", 60, cor)], x, 720, "center")
    E.frase(c, t, C["s05.c"], ps("sem", "i", 76) + [("encostar", "g", 76, COR)], W / 2, 880, "center", 0.12)
    E.frase(c, t, lerp(C["s05.c"], C["s05.end"], 0.55), ps("em volta: um", "i", 64, TINTA2) + [("campo", "g", 64, COR)], W / 2, 980, "center", 0.12)


# ---------------- campo ----------------
def b_campo(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("campo", "i", 110), ("magnético", "g", 110, COR)], XE, 250)
    E.frase(c, t, C["s06.b"], ps("onde outro ímã", "i", 66) + [("sente força", "g", 64)], XE, 370, passo=0.12)
    cx, cy = 1350, 640
    F.ima(c, t, C["s06.a"] + 0.4, cx, cy, 420, 120)
    # um ímã pequeno sente o puxão
    if t >= C["s06.b"]:
        q = math.sin(t * 3) * 6
        mini_ima(c, cx + 330 + q, cy - 200, 160, 52, ep(t, C["s06.b"], 0.4))
        F.seta(c, cx + 230, cy - 200, cx + 160, cy - 200, E.COR, ep(t, C["s06.b"] + 0.4, 0.3), 8)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: F.letra_vetor(c, "B", XE + 90, 640, 200, TINTA, a))
    E.foco(c, t, C["s06.c"] + 0.4, 0.4, lambda a: E.escreve(c, "campo magnético", XE + 240, 600, 50, "i", TINTA2, a))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: (E.escreve(c, "unidade:", XE + 240, 680, 50, "i", TINTA2, a),
                                             E.escreve(c, "tesla (T)", XE + 450, 680, 56, "g", COR, a)))
    E.foco(c, t, C["s06.e"], 0.5, lambda a: E.pilula(c, "VETORIAL", XE + 230, 860, 80, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s06.e"] + 0.4, ps("direção e sentido", "i", 56, TINTA2), XE + 500, 880, passo=0.12)


# ---------------- linhas de campo ----------------
def b_linhas(c, t, C, b):
    cx, cy, w, h = 1240, 600, 400, 120
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("linhas", "i", 96), ("de campo", "g", 96, COR)], XE, 220)
        F.linhas_campo(c, t, C["s07.b"], cx, cy, w, 3, d=lerp(1.4, 2.6, 0.5), h=h)
        F.ima(c, t, C["s07"], cx, cy, w, h)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "saem do N", cx + 330, cy + 250, 46, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "entram no S", cx - 330, cy + 250, 46, "g", fundo=NEG, a=a))
        E.frase(c, t, C["s07.c"], ps("por fora,", "i", 60, TINTA2) + ps("dão a volta", "i", 60), XE, 340, passo=0.12)
        return
    if t < C["s09"]:
        F.linhas_campo(c, 99, 0, cx, cy, w, 3, h=h)
        ima_parado(c, cx, cy, w, h)
        regras = (("s08.a", "B tangente à linha"), ("s08.b", "juntas = mais forte"), ("s08.c", "nunca se cruzam"))
        for i, (k, s) in enumerate(regras):
            y = 230 + i * 110
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 34, y - 24, 32, a=a), centro(c, str(i + 1), XE + 34, y - 5, 40, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 54, COR if i == 0 else TINTA)], XE + 90, y)
        # 1: vetor B tangente num ponto da linha de cima
        if t >= C["s08.a"]:
            px, py = cx, cy - (h / 2 + h * (0.45 + 0.7 * 2))
            E.foco(c, t, C["s08.a"] + 0.4, 0.3, lambda a: c.drawCircle(px, py, 12, M.paint(TINTA, a)))
            F.vetor(c, t, C["s08.a"] + 0.6, (px, py), (px - 170, py), "B", None, TINTA, 9, size=56, lado=1)
        # 2: perto do polo, as linhas se apertam
        q = ep(t, C["s08.b"], 0.4) * (1 - ep(t, C["s08.c"] - 0.2, 0.3))
        if q > 0:
            for x in (cx + w / 2 + 30, cx - w / 2 - 30):
                c.drawCircle(x, cy, 120 + 6 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
        def cruz(a):
            M.line(c, XE + 120, 560, XE + 420, 700, TINTA2, a, 5)
            M.line(c, XE + 120, 700, XE + 420, 560, TINTA2, a, 5)
            E.selo(c, XE + 500, 630, 44, False, a)
        E.foco(c, t, C["s08.c"] + 0.3, 0.4, cruz)
        return
    E.frase(c, t, C["s09"], ps("diferente das linhas de força:", "i", 64, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, C["s09.a"], ps("não", "g", 84, COR) + ps("terminam no polo", "i", 84), XE, 320, passo=0.12)
    F.linhas_campo(c, 99, 0, cx, cy + 60, w, 3, h=h)
    ima_parado(c, cx, cy + 60, w, h, 0.55 if t >= C["s09.b"] else 1)
    if t >= C["s09.b"]:  # por dentro, do S para o N, tracejado
        q = ease_io(prog(t, C["s09.b"], 0.8))
        M.line(c, cx - w / 2 + 20, cy + 60, lerp(cx - w / 2 + 20, cx + w / 2 - 30, q), cy + 60, TINTA, 1.0, 6, dash=E.TRACO)
        if q > 0.8:
            F._cabeca(c, cx + 30, cy + 60, 1, 0, 26, TINTA, 1)
        E.frase(c, t, C["s09.b"] + 0.5, ps("por dentro:", "i", 60) + [("do S para o N", "g", 60)], XE, 620, passo=0.12)
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "linhas fechadas", XE + 230, 460, 50, "g", fundo=E.COR, a=a))


# ---------------- bússola ----------------
def b_bussola(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("a", "i", 100), ("bússola", "g", 100, COR)], XE, 240)
        E.frase(c, t, C["s10.b"], ps("um ímã pequeno que", "i", 60) + [("gira", "g", 60)], XE, 360, passo=0.12)
        cx, cy, w = 1300, 680, 420
        E.foco(c, t, C["s10.c"] - 0.6, 0.5, lambda a: (F.linhas_campo(c, 99, 0, cx, cy, w, 2, h=110), ima_parado(c, cx, cy, w, 110, a)))
        # bússola grande à esquerda da tela; depois, alinhada com a linha de cima
        bx, by = 1300, 330
        alvo = ang_tela(*campo_dip(bx, by, polos_ima(cx, cy, w)))
        ang = gira(t, C["s10.c"], 60 + 25 * math.sin(t * 1.3) if t < C["s10.c"] else 60, alvo, 1.0)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: bussola(c, bx, by, 110, ang, a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "N da agulha = sentido de B", XE + 380, 520, 46, "g", fundo=E.COR, a=a))
        return
    cx, cy, w = 1100, 580, 440
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("um", "i", 76) + [("medidor", "g", 76, COR)] + ps("de campo", "i", 76), XE, 200, passo=0.12)
        F.ima(c, t, C["s11"] + 0.2, cx, cy, w, 120)
        pts = []
        for i in range(14):
            g = 2 * math.pi * i / 14
            pts.append((cx + 400 * math.cos(g), cy + 270 * math.sin(g)))
        for i, (x, y) in enumerate(pts):
            ti = C["s11.a"] + 0.08 * i
            alvo = ang_tela(*campo_dip(x, y, polos_ima(cx, cy, w)))
            ang = gira(t, C["s11.b"] + 0.05 * i, 90, alvo, 0.9)
            E.foco(c, t, ti, 0.4, lambda a, x=x, y=y, ang=ang: bussola(c, x, y, 50, ang, a))
        if t >= C["s11.b"] + 1.2:
            F.linhas_campo(c, t, C["s11.b"] + 1.2, cx, cy, w, 2, d=1.2, h=120)
        return
    # a Terra é um ímã
    tx, ty, r = 1350, 600, 300
    E.frase(c, t, C["s12"], ps("longe dos ímãs: aponta para o", "i", 60) + [("norte", "g", 60)], XE, 200, passo=0.1)
    E.foco(c, t, C["s12.a"], 0.6, lambda a: terra(c, tx, ty, r, a))
    if t >= C["s12.a"] + 0.6:
        barra(c, tx, ty, 380, 90, ep(t, C["s12.a"] + 0.6, 0.5), -90)
    E.foco(c, t, C["s12.a"] + 0.4, 0.4, lambda a: centro(c, "norte geográfico", tx, ty - r - 40, 46, "i", TINTA, a))
    E.foco(c, t, C["s12.a"] + 0.4, 0.4, lambda a: centro(c, "sul geográfico", tx, ty + r + 70, 46, "i", TINTA, a))
    E.frase(c, t, C["s12.a"], ps("a Terra é um", "i", 70) + [("ímã", "g", 70, COR)], XE, 360, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: bussola(c, 620, 640, 110, 90, a))
    E.foco(c, t, C["s12.b"] + 0.4, 0.4, lambda a: E.escreve(c, "N da agulha → S", XE, 860, 54, "g", TINTA, a))
    q = ep(t, C["s12.c"], 0.4)
    if q > 0:
        c.drawCircle(tx, ty - 95, 80 + 6 * math.sin(t * 5), M.paint(NEG, q, stroke=7))
        E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: E.pilula(c, "sul magnético", tx + 330, ty - 230, 46, "g", fundo=NEG, a=a))


# ---------------- ímã partido ----------------
def fila_imas(c, x0, y, n, wm, hm, a, abre=0.0, corte=None, nomes=False, gap=6):
    """fila de n ímãs minúsculos a partir de x0; corte = índice depois do qual a fila se abre `abre` px"""
    for i in range(n):
        x = x0 + i * (wm + gap) + wm / 2 + (abre if corte is not None and i >= corte else 0)
        mini_ima(c, x, y, wm, hm, a)


def b_partido(c, t, C, b):
    n, wm, hm, gap = 8, 150, 70, 8
    x0, y = (W - (n * wm + (n - 1) * gap)) / 2, 560
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("uma fila de", "i", 76) + [("ímãs minúsculos", "g", 76, COR)], XE, 220, passo=0.12)
        for i in range(n):
            E.foco(c, t, C["s13.a"] + 0.1 * i, 0.4, lambda a, i=i: mini_ima(c, x0 + i * (wm + gap) + wm / 2
                                                                         + (90 * ease_out(prog(t, C["s13.b"], 0.5)) if i >= n // 2 else 0), y, wm, hm, a))
        if t >= C["s13.b"]:
            xm = x0 + (n // 2) * (wm + gap) - gap / 2
            M.line(c, xm, y - 140, xm, y + 140, ERRADO, 1 - ep(t, C["s13.b"] + 0.4, 0.4), 6, dash=E.TRACO)
        if t >= C["s13.c"]:
            for k in range(2):
                xa = x0 + k * (n // 2) * (wm + gap) + (90 if k else 0)
                xb = xa + (n // 2) * (wm + gap) - gap
                E.foco(c, t, C["s13.c"] + 0.2 * k, 0.4, lambda a, xa=xa: E.pilula(c, "S", xa + 30, y + 120, 46, "g", fundo=NEG, a=a))
                E.foco(c, t, C["s13.c"] + 0.2 * k + 0.1, 0.4, lambda a, xb=xb: E.pilula(c, "N", xb - 30, y + 120, 46, "g", fundo=E.COR, a=a))
            E.frase(c, t, C["s13.c"] + 0.6, ps("cada metade:", "i", 60, TINTA2) + [("S", "g", 60, NEG), ("...", "g", 60, TINTA2), ("N", "g", 60, COR)], W / 2, 860, "center", 0.12)
        return
    # corta de novo e de novo: quatro pedaços, cada um com N e S
    E.frase(c, t, C["s14"], ps("corte de novo", "i", 70), XE, 200, passo=0.12)
    def pedacos(a):
        k = 4
        tot = 1300
        wp = (tot - (k - 1) * 70) / k
        for j in range(k):
            x = 310 + j * (wp + 70)
            M.rrect(c, x, 330, wp / 2, 100, 10, NEG, a)
            M.rrect(c, x + wp / 2, 330, wp / 2, 100, 10, E.COR, a)
            E._meio(c, "S", x + wp / 4, 380, 54, "g", BR, a)
            E._meio(c, "N", x + 3 * wp / 4, 380, 54, "g", BR, a)
    E.foco(c, t, C["s14"] + 0.6, 0.5, pedacos)
    E.frase(c, t, C["s14.a"], ps("sempre os", "i", 64) + [("dois polos", "g", 64, COR)], W / 2, 540, "center", 0.12)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "não existe polo sozinho", W / 2, 640, 52, "g", fundo=TINTA, a=a))
    # carga x polo
    E.foco(c, t, C["s14.c"] + 1.0, 0.5, lambda a: F.carga(c, 99, 0, 640, 830, 64, "+"))
    E.foco(c, t, C["s14.c"] + 1.4, 0.4, lambda a: E.selo(c, 760, 760, 34, True, a))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: (M.rrect(c, 1180, 790, 110, 90, 10, E.COR, a), E._meio(c, "N", 1235, 835, 54, "g", BR, a)))
    E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: E.selo(c, 1330, 760, 34, False, a))
    E.foco(c, t, C["s14.d"] + 0.1, 0.4, lambda a: (centro(c, "carga sozinha", 640, 960, 44, "i", TINTA2, a), centro(c, "polo sozinho", 1235, 960, 44, "i", TINTA2, a)))
    E.foco(c, t, C["s14.e"], 0.4, lambda a: E.escreve(c, "a origem: outra aula", 1440, 860, 42, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s15.a"], ps("o N da bússola não aponta para um", "i", 60) + [("N", "g", 60, COR)], XE, 320, passo=0.1)
    # N com N: a agulha fugiria
    if t < C["s15.c"]:
        E.foco(c, t, C["s15.b"], 0.5, lambda a: barra(c, 1150, 620, 400, 110, a, 180))
        q = ease_out(prog(t, C["s15.b"] + 0.6, 0.8))
        E.foco(c, t, C["s15.b"] + 0.2, 0.4, lambda a: bussola(c, 700 - 60 * q, 620, 100, 180 * q, a))
        E.foco(c, t, C["s15.b"] + 1.2, 0.4, lambda a: E.pilula(c, "N com N: a agulha fugiria", 900, 830, 50, "g", fundo=ERRADO, a=a))
        return
    tx, ty, r = 1400, 640, 240
    terra(c, tx, ty, r)
    barra(c, tx, ty, 300, 76, 1, -90)
    centro(c, "norte geográfico", tx, ty - r - 30, 44, "i", TINTA)
    E.frase(c, t, C["s15.c"], [("norte", "g", 80), ("geográfico", "i", 84)], XE, 560, passo=0.12)
    E.frase(c, t, C["s15.c"] + 0.6, [("=", "g", 80, TINTA2), ("sul", "g", 80, NEG), ("magnético", "i", 84)], XE, 700, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        E.frase(c, t, C["s16"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        cx, cy, w = 960, 560, 420
        F.linhas_campo(c, t, C["s16.a"], cx, cy, w, 2, d=1.6, h=110, escuro=True)
        F.ima(c, t, C["s16"] + 0.3, cx, cy, w, 110)
        E.foco(c, t, C["s16.a"], 0.4, lambda a: E.pilula(c, "sai do N", cx + 380, cy - 40, 50, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "entra no S", cx - 380, cy - 40, 50, "g", fundo=NEG, a=a))
        E.frase(c, t, C["s16.b"] + 0.9, ps("mão única, por fora", "i", 60, BR), W / 2, 880, "center", 0.12)
        if t >= C["s16.c"]:
            for i, (x, y) in enumerate(((cx + 380, cy + 150), (cx, cy - 300), (cx - 400, cy + 160))):
                ang = ang_tela(*campo_dip(x, y, polos_ima(cx, cy, w)))
                E.foco(c, t, C["s16.c"] + 0.3 * i, 0.4, lambda a, x=x, y=y, ang=ang: bussola(c, x, y, 54, ang, a, True))
            E.frase(c, t, C["s16.c"] + 0.4, ps("a agulha segue a seta", "g", 56, BR), W / 2, 980, "center", 0.12)
        return
    E.frase(c, t, C["s17"], ps("funciona com", "i", 70, CLARO) + [("qualquer ímã", "g", 70, BR)], W / 2, 160, "center", 0.12)
    # barra
    E.foco(c, t, C["s17.a"], 0.5, lambda a: (F.linhas_campo(c, 99, 0, 380, 470, 240, 1, h=70, escuro=True), ima_parado(c, 380, 470, 240, 70, a)))
    # ferradura com as linhas retas entre as pontas
    def fer(a):
        xn, xs, yp = ferradura(c, 960, 590, 230, a)
        for k in range(4):
            yy = yp - 60 - k * 0  # linhas retas entre as pontas
        for k in range(3):
            yy = yp - 20 - 50 * k
            F.seta(c, xn + 50, yy, xs - 50, yy, E.CLARO, a, 4, 18)
    E.foco(c, t, C["s17.b"], 0.5, fer)
    # a Terra
    def ter(a):
        terra(c, 1540, 470, 150, a)
        barra(c, 1540, 470, 190, 50, a, -90)
    E.foco(c, t, lerp(C["s17.b"], C["s17.c"], 0.35), 0.5, ter)
    E.frase(c, t, C["s17.c"], ps("desenhe a linha no ponto e", "i", 54, CLARO) + [("siga a seta", "g", 54, BR)], W / 2, 830, "center", 0.1)
    E.frase(c, t, C["s17.d"], [("perto do N:", "g", 50, CLARO), ("para longe;", "i", 54, BR), ("perto do S:", "g", 50, CLARO), ("para ele", "i", 54, BR)],
            W / 2, 950, "center", 0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s19"]:
        cx, cy, w = 1250, 380, 460
        F.ima(c, t, C["s18.a"], cx, cy, w, 120)
        E.foco(c, t, C["s18.b"], 0.5, lambda a: bussola(c, cx + w / 2 + 170, cy, 80, 90 + 30 * math.sin(t * 2), a))
        E.foco(c, t, C["s18.b"] + 0.4, 0.4, lambda a: E.formula(c, "?", cx + w / 2 + 290, cy + 30, 90, "g", COR, a))
        E.frase(c, t, C["s18.c"], ps("para onde aponta o", "i", 64) + [("N da agulha?", "g", 64, COR)], XE, 680, passo=0.12)
        E.frase(c, t, C["s18.d"], ps("partido ao meio: que polo na", "i", 56) + [("ponta quebrada?", "g", 56, COR)], XE, 820, passo=0.1)
        if t >= C["s18.d"]:
            M.line(c, cx, cy - 110, cx, cy + 110, ERRADO, ep(t, C["s18.d"], 0.4), 6, dash=E.TRACO)
    else:
        E.relogio(c, t, C["s19.a"], cx=1460, cy=500, r=200)
        E.frase(c, t, C["s19"], ps("bússola à direita do", "i", 60) + [("N", "g", 60, COR)], XE, 420, passo=0.1)
        E.frase(c, t, C["s19"] + 0.2, ps("e o polo da", "i", 60) + [("ponta quebrada", "g", 60, COR)], XE, 540, passo=0.1)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cx, cy, w = 900, 420, 460
    if t < C["s21"]:
        F.linhas_campo(c, t, C["s20.a"], cx, cy, w, 2, d=1.2, h=120)
        ima_parado(c, cx, cy, w, 120)
        bx = cx + w / 2 + 230
        ang = gira(t, C["s20.c"], 60, ang_tela(*campo_dip(bx, cy, polos_ima(cx, cy, w))), 0.8)
        bussola(c, bx, cy, 90, ang)
        if t >= C["s20.b"]:
            F.vetor(c, t, C["s20.b"], (bx + 120, cy + 180), (bx + 330, cy + 180), "B", None, TINTA, 9, size=54)
        E.frase(c, t, C["s20.a"], ps("a linha", "i", 64) + [("sai do N", "g", 64, COR)], XE, 760, passo=0.12)
        E.foco(c, t, C["s20.c"] + 0.4, 0.5, lambda a: E.pilula(c, "para a direita", 1500, 860, 60, "g", fundo=CERTO, a=a))
        return
    q = 120 * ease_out(prog(t, C["s21.a"] + 0.3, 0.6))
    for lado in (-1, 1):
        x0 = cx + lado * (w / 4 + q / 2)
        E.foco(c, t, C["s21.a"], 0.4, lambda a, x0=x0, lado=lado: (M.rrect(c, x0 - w / 4, cy - 60, w / 4, 120, 10, NEG, a),
                                                                   M.rrect(c, x0, cy - 60, w / 4, 120, 10, E.COR, a)))
    E.frase(c, t, C["s21.a"], ps("o ímã partido", "i", 70), XE, 220, passo=0.12)
    xd = cx + w / 4 + q / 2
    E.foco(c, t, C["s21.a"] + 0.4, 0.4, lambda a: E._meio(c, "N", xd + w / 8, cy, 64, "g", BR, a))
    E.foco(c, t, C["s21.a"] + 0.4, 0.4, lambda a: E._meio(c, "S", cx - w / 4 - q / 2 - w / 8, cy, 64, "g", BR, a))
    E.foco(c, t, C["s21.b"], 0.4, lambda a: (F.seta(c, xd - w / 8, cy + 230, xd - w / 8, cy + 90, TINTA, a, 7), centro(c, "ponta quebrada", xd - w / 8, cy + 290, 44, "i", TINTA2, a)))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E._meio(c, "S", xd - w / 8, cy, 64, "g", BR, a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "polo sul", 1560, 420, 60, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s21.c"] + 0.1, 0.4, lambda a: E._meio(c, "N", cx - w / 4 - q / 2 + w / 8, cy, 64, "g", BR, a))
    E.frase(c, t, C["s21.d"], ps("cada pedaço:", "i", 64) + [("um ímã inteiro", "g", 64, COR)], XE, 900, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s22.a", [("polos iguais", "g", 70), ("se repelem", "i", 74)]),
                 ("s22.b", [("linha:", "g", 70), ("sai do", "i", 74), ("N,", "g", 70, COR), ("entra no", "i", 74), ("S", "g", 70, NEG)]),
                 ("s22.c", [("bússola:", "g", 70), ("aponta no sentido de", "i", 74), ("B", "g", 70)]),
                 ("s22.d", [("todo ímã:", "g", 70), ("dois polos", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("corrente", "g", 110, COR), ("cria", "i", 110)], XE, 400)
    E.frase(c, t, C["s23.a"] + 0.5, [("campo", "g", 110, COR)], XE, 530)
    # fio com corrente e a bússola que gira
    fx = 700
    if t >= C["s23.a"]:
        bussola(c, fx, 800, 90, gira(t, C["s23.a"] + 0.8, 90, 180, 1.0), ep(t, C["s23.a"] + 0.2, 0.4))  # fio por cima: a agulha fica de lado
        M.line(c, fx, 600, fx, 1000, TINTA, ep(t, C["s23.a"], 0.4), 8)
        F.corrente(c, t, C["s23.a"] + 0.4, [(fx, 1000), (fx, 600)], fecha=False)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.pilula(c, "regra da mão direita", 1060, 800, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, polos=b_polos, campo=b_campo, linhas=b_linhas, bussola=b_bussola,
              partido=b_partido, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
