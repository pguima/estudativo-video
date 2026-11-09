"""Visual — Estudativo · FIS-CIN-018: período, frequência e rpm. Primeira aula do módulo Movimento circular.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py (peças em _ferramentas/fisica.py, F).
MOVIMENTO CIRCULAR (vale para FIS-CIN-018 a 021): o que gira é desenhado de cima, como um disco claro com contorno em tinta,
um raio e um ponto laranja na borda (o "ponto que gira"); o rastro da volta é um arco laranja. Período T em laranja (é o
tempo, unidade s), frequência f em violeta (F.ACEL) com a unidade Hz; rpm é unidade fora do SI (pílula vermelha "fora do SI"
na primeira vez). Conversão rpm → Hz com F.fila, como em toda conversão de unidade.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-018_periodo_frequencia_rpm.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("periodo", "frequencia", "inverso", "rpm", "atalho", "questao", "fim"))
BR = "#FFFFFF"
FREQ = F.ACEL  # frequência

# todas as contas da aula
assert 1200 / 60 == 20 and 1 / 20 == 0.05 and 60 / 1200 == 0.05 and 1200 * 60 == 72000
assert 10 / 5 == 2 and 1 / 2 == 0.5 and 1 / 4 == 0.25 and 2 * 60 == 120
assert 3000 / 60 == 50 and 300 / 6 == 50 and 1 / 50 == 0.02 and 60 / 3000 == 0.02


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


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


def promessa(c, t, C, cena, itens, size=76):
    """“até o fim da aula” + itens numerados [(cue, texto)] + a órbita da Física à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    passo_y = 150 if len(itens) <= 3 else 128
    for i, (k, s) in enumerate(itens):
        y = 430 + i * passo_y
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", size, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, num="2", titulo=("coisas",)):
    """você precisa de N coisas: itens = [(cue, linha fina, linha forte, desenho(a, x, y) ou None)]"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 80), XE, 380, passo=0.14)
    t1 = C[itens[0][0]] - 0.6 if num is None else C[cena + ".a"]
    if num:
        E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, num, XE - 8, 700, 320, "g", COR, a))
        E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, titulo[0], XE + 205, 680, 110, "i", TINTA, a))
    else:
        for j, s in enumerate(titulo):
            E.frase(c, t, t1 + 0.2 * j, [(s, "g", 110, COR)], XE, 540 + 130 * j)
    n = len(itens)
    x, w = 820, 1000
    h = 230 if n == 2 else 190
    gap = 290 if n == 2 else 225
    y0 = 230 if n == 2 else 150
    for i, (k, l1, l2, des) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + h * 0.75)
        if des:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, des=des, y=y: des(a, x + w - 170, y + h / 2))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            820, y0 + n * gap + 20, "left", 0.12)


def fim(c, t, C, cr, itens, cp, linhas, desenho, k_insc, k_bons):
    """resumo numerado (cena cr, itens = [(cue, partes)]) e a ponte (cena cp): linhas = [(cue, partes)], desenho(a) à esquerda embaixo"""
    def resumo():
        E.frase(c, t, C[cr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[cp] - 0.1, resumo)
    if t < C[cp]:
        return
    E.frase(c, t, C[cp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    for i, (k, partes) in enumerate(linhas):
        E.frase(c, t, C[k], partes, XE, 400 + 140 * i, passo=0.12)
    desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


# ---------------- peças desta aula ----------------
def disco(c, cx, cy, r, ang, a=1.0, rastro=None, cor=None, escuro=False):
    """disco visto de cima: contorno, raio até o ponto laranja da borda no ângulo ang (graus, anti-horário a partir da direita).
    rastro = ângulo já varrido (graus) desenhado como arco laranja a partir do topo"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF" if not escuro else "#1A1A24", 0.9 * a))
    c.drawCircle(cx, cy, r, M.paint(tinta, a, stroke=5))
    if rastro:
        E.arco(c, cx, cy, r + 22, -90, min(359.9, rastro), cor or E.COR, 8, a)
    g = math.radians(ang)
    px, py = cx + math.cos(g) * r, cy - math.sin(g) * r
    M.line(c, cx, cy, px, py, tinta, a, 4)
    c.drawCircle(cx, cy, 8, M.paint(tinta, a))
    E.bola(c, px, py, max(16, r * 0.1), cor, a)


def ventilador(c, x, y, r, giro, a=1.0, borrado=False):
    if a <= 0:
        return
    c.drawCircle(x, y, r * 1.08, M.paint(TINTA2, a * 0.6, stroke=4))
    for k in range(3):
        c.save(); c.translate(x, y); c.rotate(giro + 120 * k)
        c.drawOval(skia.Rect.MakeXYWH(r * 0.12, -r * 0.2, r * 0.9, r * 0.4), M.paint(E.COR, a * (0.5 if borrado else 1)))
        c.restore()
    if borrado:
        c.drawCircle(x, y, r * 0.95, M.paint(E.COR, 0.18 * a))
    c.drawCircle(x, y, r * 0.16, M.paint(TINTA, a))
    M.rrect(c, x - 14, y + r * 1.08, 28, r * 0.9, 6, TINTA2, a)
    M.rrect(c, x - r * 0.6, y + r * 1.98, r * 1.2, 26, 10, TINTA2, a)


def relogio_parede(c, cx, cy, r, seg, a=1.0):
    """relógio com só o ponteiro dos segundos (seg de 0 a 60)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=8))
    for k in range(12):
        g = math.radians(k * 30)
        M.line(c, cx + math.sin(g) * r * 0.8, cy - math.cos(g) * r * 0.8, cx + math.sin(g) * r * 0.92, cy - math.cos(g) * r * 0.92, TINTA, a, 5)
    g = math.radians(seg * 6)
    M.line(c, cx, cy, cx + math.sin(g) * r * 0.82, cy - math.cos(g) * r * 0.82, E.COR, a, 6)
    c.drawCircle(cx, cy, 10, M.paint(E.COR, a))


def furadeira(c, x, y, s=1.0, a=1.0, giro=0.0):
    """furadeira de lado, broca apontando para a esquerda; (x, y) = ponta da broca"""
    if a <= 0:
        return
    M.rrect(c, x + 120 * s, y - 50 * s, 300 * s, 100 * s, 30 * s, E.COR, a)
    M.rrect(c, x + 300 * s, y + 30 * s, 80 * s, 200 * s, 24 * s, E.mix(E.COR, "#000000", 0.25), a)
    M.rrect(c, x + 80 * s, y - 30 * s, 60 * s, 60 * s, 10 * s, TINTA, a)
    M.rrect(c, x, y - 9 * s, 90 * s, 18 * s, 6, "#9A9AA2", a)
    for k in range(4):
        xx = x + ((k * 22 + giro) % 88) * s
        M.line(c, xx, y - 9 * s, xx + 10 * s, y + 9 * s, TINTA2, a, 3)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: ventilador(c, 1450, 430, 220, t * 2400, a, borrado=True))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: (F.medida(c, "1.200", "", XE, 330, 150, TINTA, a), E.formula(c, "rpm", XE + 470, 330, 80, "b", F.UNID, a)))
        E.frase(c, t, C["s01.a"] + 0.5, ps("rotações por minuto", "i", 60, TINTA2), XE, 420, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("voltas em", "i", 72) + [("1 segundo?", "g", 72, COR)], XE, 590, passo=0.12)
        bola_txt(c, t, C["s01.c"], "20 voltas", XE + 130, 780, 110, 44, FREQ)
        E.frase(c, t, C["s01.d"], ps("cada volta:", "i", 60), XE + 300, 760, passo=0.1)
        E.foco(c, t, C["s01.d"] + 0.6, 0.5, lambda a: F.medida(c, "0,05", "s", XE + 300, 860, 90, COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "o período"), ("s02.c", "a frequência"), ("s02.d", "rpm em hertz")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "tempo:", "1 min = 60 s", None), ("s03.c", "no SI, o tempo é medido em", "segundo (s)", None)))


# ---------------- período ----------------
def b_periodo(c, t, C, b):
    def s04():
        cx, cy, r = 1450, 520, 230
        q = max(0.0, t - C["s04"]) / 3.0  # uma volta a cada 3 s
        E.foco(c, t, C["s04"], 0.5, lambda a: disco(c, cx, cy, r, 90 - 360 * q, a, rastro=(360 * (q % 1)) if t >= C["s04.a"] else None))
        E.frase(c, t, C["s04"], ps("roda, ventilador, relógio:", "i", 60, TINTA2), XE, 240, passo=0.1)
        E.frase(c, t, C["s04.a"], ps("tempo de", "i", 76) + [("1 volta", "g", 76)], XE, 400, passo=0.12)
        E.frase(c, t, C["s04.a"] + 1.0, [("=", "g", 76, TINTA2), ("período", "g", 90, COR)], XE, 520, passo=0.12)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.escreve(c, "T", XE, 760, 220, "g", COR, a))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: (E.escreve(c, "unidade:", XE + 230, 700, 56, "i", TINTA2, a), F.medida(c, "", "segundo (s)", XE + 230, 780, 90, TINTA, a, cor_u=TINTA)))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    seg = max(0.0, t - C["s05.a"]) * 6  # ponteiro acelerado: 6 s por segundo
    E.foco(c, t, C["s05.a"], 0.5, lambda a: relogio_parede(c, 620, 520, 220, seg % 60, a))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.escreve(c, "T =", 400, 900, 90, "g", TINTA, a), F.medida(c, 60, "s", 570, 900, 90, COR, a)))
    q = max(0.0, t - C["s05.c"]) / 4.0
    E.foco(c, t, C["s05.c"], 0.5, lambda a: disco(c, 1400, 520, 220, 90 - 360 * q, a, rastro=360 * (q % 1)))
    E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: centro(c, "carrossel, de cima", 1400, 230, 48, "i", TINTA2, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: (E.escreve(c, "T =", 1180, 900, 90, "g", TINTA, a), F.medida(c, 4, "s", 1350, 900, 90, COR, a)))


# ---------------- frequência ----------------
def b_frequencia(c, t, C, b):
    cx, cy, r = 1450, 500, 210

    def s06():
        E.frase(c, t, C["s06"], ps("a pergunta ao contrário:", "i", 60, TINTA2), XE, 230, passo=0.1)
        E.frase(c, t, C["s06.a"], ps("quantas voltas em", "i", 72) + [("1 s?", "g", 72, FREQ)], XE, 350, passo=0.12)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.escreve(c, "f", XE, 560, 200, "g", FREQ, a))
        E.formula_em(c, t, C["s06.c"], "f = f{voltas}{tempo}", XE + 200, 520, 80, "g", TINTA)
        E.formula_em(c, t, C["s06.d"], "f{10 voltas}{5 s} =", XE, 780, 76, "g", TINTA)
        bola_txt(c, t, C["s06.e"], "2 voltas/s", XE + 680, 750, 120, 40, FREQ)
        # 10 voltas em 5 s
        u = max(0.0, min(5.0, t - C["s06.d"]))
        voltas = 2 * u
        E.foco(c, t, C["s06.d"], 0.5, lambda a: disco(c, cx, cy, r, 90 - 360 * voltas, a, rastro=360 * (voltas % 1)))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: (centro(c, f"{int(voltas)} voltas", cx, cy + r + 110, 60, "g", FREQ, a),
                                                 F.cronometro(c, cx + 330, cy - 200, 70, u, a, E._num(round(u, 1)) + " s")))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], ps("voltas por segundo têm nome:", "i", 66), XE, 260, passo=0.1)
    E.foco(c, t, C["s07.a"], 0.5, lambda a: (E.escreve(c, "hertz", XE, 480, 170, "g", FREQ, a), E.pilula(c, "Hz", XE + 640, 430, 80, "g", fundo=FREQ, a=a)))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "2 voltas/s = 2 Hz", XE, 680, 90, "g", TINTA, a))
    E.frase(c, t, C["s07.c"], ps("homenagem a", "i", 56, TINTA2) + [("Heinrich Hertz", "g", 56)], XE, 880, passo=0.1)


# ---------------- inverso ----------------
def b_inverso(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"], [("período", "g", 72, COR), ("e", "i", 72), ("frequência:", "g", 72, FREQ), ("inversos", "i", 76)], XE, 230, passo=0.12)
        # 1 segundo dividido em 2 voltas
        x0, x1, y = 300, 1300, 420
        if t >= C["s08.b"]:
            q = ep(t, C["s08.b"], 0.5)
            M.rrect(c, x0, y, x1 - x0, 70, 14, FIO, q)
            E.foco(c, t, C["s08.b"] + 0.2, 0.4, lambda a: centro(c, "1 segundo", (x0 + x1) / 2, y - 24, 46, "i", TINTA2, a))
            for k in range(2):
                tk = C["s08.b"] + 0.5 + 0.5 * k
                qq = ep(t, tk, 0.4)
                if qq > 0:
                    M.rrect(c, x0 + k * (x1 - x0) / 2 + 6, y + 6, (x1 - x0) / 2 - 12, 58, 10, E.COR, 0.85 * qq)
                    centro(c, f"volta {k + 1}", x0 + (k + 0.5) * (x1 - x0) / 2, y + 48, 40, "g", BR, qq)
            E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "0,5 s cada", (x0 + x1) / 2, y + 140, 56, "g", COR, a))
        F.formula_legenda(c, t, C["s08.d"], "T = f{1}{f}", [("T", "período", "s"), ("f", "frequência", "Hz")], XE, 720, 110, tl=[C["s08.d"] + 0.6, C["s08.d"] + 1.0])
        E.formula_em(c, t, C["s08.e"], "f = f{1}{T}", 1200, 720, 110, "g", TINTA)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    q = max(0.0, t - C["s09"]) / 4.0
    E.foco(c, t, C["s09"], 0.5, lambda a: disco(c, 1480, 380, 170, 90 - 360 * q, a, rastro=360 * (q % 1)))
    E.foco(c, t, C["s09.a"], 0.5, lambda a: (E.escreve(c, "carrossel: T =", XE, 260, 70, "i", TINTA, a), F.medida(c, 4, "s", XE + E.larg("carrossel: T =", "i", 70) + 24, 260, 80, COR, a)))
    E.formula_em(c, t, C["s09.b"], "f = f{1}{4} =", XE, 440, 84, "g", TINTA)
    E.foco(c, t, C["s09.c"], 0.5, lambda a: F.medida(c, "0,25", "Hz", XE + E.formula(None, "f = f{1}{4} =", 0, 0, 84, a=0) + 30, 440, 84, FREQ, a))
    E.frase(c, t, C["s09.d"], [("mais", "i", 60), ("voltas", "g", 60, FREQ), ("por", "i", 60), ("segundo", "i", 60), ("→", "g", 60), ("menos", "i", 60), ("tempo", "g", 60, COR),
                               ("por", "i", 60), ("volta", "i", 60)], XE, 680, passo=0.1)
    E.formula_em(c, t, C["s09.e"], "f{1}{s} = Hz      f{1}{Hz} = s", XE, 880, 76, "g", TINTA2)


# ---------------- rpm ----------------
def b_rpm(c, t, C, b):
    def s10():
        E.foco(c, t, C["s10.a"], 0.5, lambda a: E.escreve(c, "rpm", XE, 400, 200, "g", TINTA, a))
        E.frase(c, t, C["s10.a"] + 0.6, ps("rotações por minuto", "i", 72), XE, 520, passo=0.12)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.pilula(c, "fora do SI", XE + 590, 330, 56, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s10.c"], ps("antes da conta:", "i", 66) + [("passe", "g", 66), ("para", "i", 66), ("Hz", "g", 66, FREQ)], XE, 720, passo=0.12)
        E.foco(c, t, C["s10"], 0.5, lambda a: ventilador(c, 1520, 420, 200, t * 900, a, borrado=True))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], [("÷ 60", "g", 90, COR)], W - 420, 200)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (F.medida(c, "1.200", "voltas", XE, 260, 84, TINTA, a), E.escreve(c, "em 1 min", XE + 600, 260, 66, "i", TINTA2, a)))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: (E.escreve(c, "=", XE, 380, 84, "g", TINTA2, a), F.medida(c, "1.200", "voltas", XE + 80, 380, 84, TINTA, a),
                                             E.escreve(c, "em 60 s", XE + 680, 380, 66, "i", COR, a)))
    E.frase(c, t, C["s11.d"], ps("em 1 s, cabe", "i", 62) + [("1/60", "g", 62, COR)] + ps("disso", "i", 62), XE, 520, passo=0.1)
    E.formula_em(c, t, C["s11.e"], "f{1200}{60} =", XE, 690, 84, "g", TINTA)
    bola_txt(c, t, C["s11.e"] + 1.4, "20 Hz", XE + 470, 665, 100, 54, FREQ)
    E.formula_em(c, t, C["s11.f"], "T = f{1}{20} = 0,05 s", XE + 800, 690, 76, "g", COR)
    E.frase(c, t, C["s11.g"], ps("de volta:", "i", 62) + [("× 60", "g", 62, COR)], XE, 900, passo=0.1)
    E.foco(c, t, C["s11.g"] + 1.2, 0.5, lambda a: E.formula(c, "2 Hz → 2 · 60 = 120 rpm", XE + 520, 900, 66, "g", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 210)
    E.frase(c, t, C["s12.a"], [("multiplicar", "g", 70, ERRADO)] + ps("por 60 em vez de dividir", "i", 70), XE, 340, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "1.200 · 60 = 72.000 Hz", XE, 520, 96, "g", ERRADO, a))
    if t >= C["s12.c"]:
        E.risco(c, XE - 10, 540, XE + 1150, 440, t, C["s12.c"], largura=12)
    E.frase(c, t, C["s12.c"], [("absurdo:", "g", 64, ERRADO)] + ps("em 1 s cabem", "i", 64) + [("menos", "g", 64)] + ps("voltas que em 1 min", "i", 64), XE, 700, passo=0.1)
    E.frase(c, t, C["s12.d"], [("rpm", "g", 76), ("→", "g", 76, TINTA2), ("Hz:", "g", 76, FREQ), ("o", "i", 76), ("número", "i", 76), ("diminui", "g", 76, CERTO)],
            XE, 880, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("o atalho:", "i", 76, CLARO), W / 2, 170, "center")
        E.foco(c, t, C["s13.a"], 0.5, lambda a: centro(c, "rpm ÷ 60 = Hz", W / 2, 360, 110, "g", BR, a))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: centro(c, "Hz × 60 = rpm", W / 2, 520, 90, "g", CLARO, a))
        E.formula_em(c, t, C["s13.c"], "T = f{60}{rpm}", W / 2 - 300, 760, 110, "g", BR, "center")
        E.formula_em(c, t, C["s13.d"], "f{60}{1200} = 0,05 s", W / 2 + 330, 760, 90, "g", CLARO, "center")
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("as voltas de 1 minuto dividem", "i", 66, CLARO) + [("60 s", "g", 66, BR)] + ps("em partes iguais", "i", 66, CLARO),
            W / 2, 280, "center", 0.1)
    if t >= C["s14.a"] + 1.4:  # 60 s em 6 partes iguais
        x0, x1, y = 360, 1560, 420
        for k in range(6):
            q = ep(t, C["s14.a"] + 1.4 + 0.15 * k, 0.3)
            M.rrect(c, x0 + k * (x1 - x0) / 6 + 4, y, (x1 - x0) / 6 - 8, 60, 10, E.COR, 0.8 * q)
        E.foco(c, t, C["s14.a"] + 2.4, 0.4, lambda a: centro(c, "6 voltas por minuto → cada uma leva 60 ÷ 6 = 10 s", W / 2, y + 140, 50, "b", CLARO, a))
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("já veio em", "i", 66, CLARO) + [("Hz", "g", 66, BR)], W / 2, 800, "center", 0.1)
    E.formula_em(c, t, C["s14.c"], "T = f{1}{f}", W / 2, 960, 90, "g", BR, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("broca de furadeira", "i", 76), XE, 340, passo=0.12)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (F.medida(c, "3.000", "", XE, 490, 130, TINTA, a), E.formula(c, "rpm", XE + 400, 490, 76, "b", F.UNID, a)))
    E.frase(c, t, C["s15.c"], [("frequência", "g", 72), ("em", "i", 72), ("Hz?", "g", 72, FREQ)], XE, 700, passo=0.12)
    E.frase(c, t, C["s15.d"], [("período?", "g", 72, COR)], XE, 820)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: furadeira(c, 1180, 520, 1.3, a, t * 300))
    else:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "f{3000}{60} = f{300}{6} =", XE, 330, 90, "g", TINTA)
    bola_txt(c, t, C["s17.b"], "50 Hz", XE + 900, 305, 110, 58, FREQ)
    E.formula_em(c, t, C["s17.c"], "T = f{1}{50} =", XE, 600, 90, "g", TINTA)
    bola_txt(c, t, C["s17.d"], "0,02 s", XE + 650, 575, 110, 52)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: E.pilula(c, "atalho: 60 ÷ 3000 = 0,02 s", XE + 470, 820, 56, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s18.b"] + 0.8, ps("50 voltas a cada segundo", "i", 60, TINTA2), XE, 960, passo=0.1)
    E.foco(c, t, C["s17"], 0.5, lambda a: furadeira(c, 1300, 640, 1.1, a, t * 300))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s19.a", [("período:", "g", 64, COR), ("tempo", "i", 66), ("de", "i", 66), ("1", "i", 66), ("volta", "i", 66)]),
             ("s19.b", [("frequência:", "g", 64, FREQ), ("voltas", "i", 66), ("por", "i", 66), ("segundo", "i", 66)]),
             ("s19.c", [("T = 1 ÷ f", "g", 64), ("e", "i", 66), ("f = 1 ÷ T", "g", 64)]),
             ("s19.d", [("rpm", "g", 64), ("÷ 60", "g", 64, COR), ("=", "g", 64), ("Hz", "g", 64, FREQ)]))

    def desenho():  # hélice: a ponta anda mais que o meio
        cx, cy, r = 470, 820, 190
        giro = (t - C["s20.a"]) * 90
        E.foco(c, t, C["s20.a"], 0.5, lambda a: disco(c, cx, cy, r, 90 - giro, a))
        g = math.radians(90 - giro)
        for k, (rr, L) in enumerate(((0.45, 70), (1.0, 160))):
            px, py = cx + math.cos(g) * r * rr, cy - math.sin(g) * r * rr
            tx, ty = math.sin(g), math.cos(g)
            if t >= C["s20.b"]:
                F.seta(c, px, py, px - tx * L * -1, py - ty * L * -1, F.VEL, ep(t, C["s20.b"], 0.4), 8)
    fim(c, t, C, "s19", itens, "s20", [("s20.a", [("Velocidade", "g", 100, COR)]), ("s20.b", [("angular", "g", 100, COR), ("e", "i", 100), ("linear", "g", 100, COR)])],
        desenho, "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, periodo=b_periodo, frequencia=b_frequencia, inverso=b_inverso, rpm=b_rpm,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
