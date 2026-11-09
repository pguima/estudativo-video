"""Visual — Estudativo · FIS-CIN-001: grandezas físicas e Sistema Internacional. Primeira aula de Física.

LINGUAGEM VISUAL DA FÍSICA (todas as aulas FIS-* copiam daqui; peças em _ferramentas/fisica.py, importado como F):
- Matéria: E.usar("Física", "<Trilha>"). Laranja #FF5A1F, forma-símbolo = órbita (E.simbolo / E.orbita), que aparece na
  promessa do gancho, nas capas e na tira da matéria. Papel claro, tipografia mista, uma cor forte por tela, como na Matemática.
- GRANDEZA: o nome em itálico serifado (TINTA) e o símbolo (letra) em grotesca pesada laranja (COR): "velocidade  v".
- MEDIDA = NÚMERO + UNIDADE, sempre juntos na tela: F.medida / F.medida_em — número pesado em tinta, unidade menor (72%) em
  cinza-tinta (F.UNID). Número sem unidade só aparece para mostrar que "não diz nada" (com "?").
- UNIDADE DO SI: na tabela do SI, o símbolo da unidade vai em laranja ("m", "kg", "s"). Unidade fora do SI que precisa
  ser convertida (h, km/h, g) vai com a pílula vermelha "fora do SI" na primeira vez.
- CONVERSÃO: F.fila de frações com unidade (fatores que valem 1). A unidade que corta é riscada em laranja NO INSTANTE da
  fala; o resultado aparece numa troca embaixo (= ...) e o final vai na esfera laranja (bola_txt). Conta de apoio em cinza.
- FÓRMULA NOVA: F.formula_legenda — fórmula grande em tinta e, embaixo, cada letra em laranja + nome + (unidade do SI).
  CONFERIR FÓRMULA: F.unidades — a unidade de cada letra entre colchetes embaixo dela ([m] = [m/s] · [s]); o que corta é
  riscado; dois lados iguais = verde, diferentes = vermelho.
- VETOR: seta grossa (F.vetor) com a letra-vetor (F.letra_vetor, setinha em cima) e "= módulo" ao lado. Cor pelo tipo:
  força e vetor genérico = laranja (COR); velocidade e deslocamento = petróleo (F.VEL); aceleração = violeta (F.ACEL).
  Componentes mais claras com tracejado até os eixos (F.componentes). Direção = reta tracejada; sentido = a ponta.
  Escalar = pílula em tinta; vetorial = pílula laranja.
- OBJETOS: corpo, carro, esfera de pêndulo em laranja (o assunto); suportes, chão, fios, espelhos e eixos em tinta.
  Carga +, polo norte e quente em laranja; carga −, polo sul e frio em azul (F.NEG). Raio de luz e onda em laranja.
- Certo = verde, errado = vermelho com risco (E.risco), como em todo o canal. Atalho e macete no palco escuro (E.palco),
  com laranja claro (CLARO) e branco. Questão com E.relogio. Texto à esquerda (XE), desenho à direita; mínimo 40 px.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-001_grandezas_fisicas_sistema_internacional.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("grandeza", "si", "vetorial", "formula", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 72 * 1000 == 72000 and 72000 / 3600 == 20 and 720 / 36 == 20 and 60 * 60 == 3600
assert 20 * 10 == 200 and 72 * 10 == 720 and 200 < 720 / 3
assert 18 * 1000 / 3600 == 5 and 180 / 36 == 5 and 5 * 60 == 300


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
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


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def bicicleta(c, x, y, s, a=1.0, cor=None, escuro=False):
    """bicicleta com as rodas tocando y; s = raio da roda"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    cor = cor or E.COR
    R, Fh = (x - 1.15 * s, y - s), (x + 1.15 * s, y - s)
    P, S, Hd = (x - 0.1 * s, y - s), (x - 0.45 * s, y - 2.05 * s), (x + 0.8 * s, y - 2.1 * s)
    for cx in (R, Fh):
        c.drawCircle(*cx, s, M.paint(tinta, a, stroke=max(4, s * 0.09)))
        c.drawCircle(*cx, s * 0.1, M.paint(tinta, a))
    for A, B in ((R, P), (P, S), (S, R), (S, Hd), (Hd, P), (Hd, Fh)):
        M.line(c, *A, *B, cor, a, max(5, s * 0.12))
    M.line(c, S[0] - s * 0.25, S[1] - s * 0.12, S[0] + s * 0.25, S[1] - s * 0.12, tinta, a, max(5, s * 0.13))
    M.line(c, Hd[0], Hd[1], Hd[0] - s * 0.15, Hd[1] - s * 0.35, tinta, a, max(4, s * 0.09))
    M.line(c, Hd[0] - s * 0.15, Hd[1] - s * 0.35, Hd[0] + s * 0.25, Hd[1] - s * 0.4, tinta, a, max(4, s * 0.09))
    c.drawCircle(*P, s * 0.16, M.paint(tinta, a, stroke=4))


def velocimetro(c, cx, cy, r, valor, vmax, texto, a=1.0):
    """mostrador de velocímetro: arco de 240 graus, ponteiro e o valor escrito"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r * 1.08, M.paint("#1B1B20", a))
    E.arco(c, cx, cy, r * 0.86, 150, 240, "#5A5A66", r * 0.06, a)
    E.arco(c, cx, cy, r * 0.86, 150, 240 * valor / vmax, E.COR, r * 0.06, a)
    for k in range(9):
        g = math.radians(150 + 240 * k / 8)
        M.line(c, cx + math.cos(g) * r * 0.66, cy + math.sin(g) * r * 0.66, cx + math.cos(g) * r * 0.76, cy + math.sin(g) * r * 0.76, BR, a * 0.7, 3)
    g = math.radians(150 + 240 * valor / vmax)
    M.line(c, cx, cy, cx + math.cos(g) * r * 0.72, cy + math.sin(g) * r * 0.72, E.COR, a, max(5, r * 0.05))
    c.drawCircle(cx, cy, r * 0.08, M.paint(BR, a))
    v, _, u = texto.partition(" ")
    F.medida(c, v, u, cx, cy + r * 0.62, r * 0.3, BR, a, "center", cor_u=E.CLARO)


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
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


# ---------------- gancho ----------------
def sonda(c, x, y, s, a=1.0, giro=0.0):
    """sonda espacial: corpo e dois painéis solares"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.rotate(giro)
    for d in (-1, 1):
        M.rrect(c, d * s * 0.55 - (s * 1.1 if d < 0 else 0), -s * 0.22, s * 1.1, s * 0.44, 4, "#2F5DA8", a)
        M.line(c, d * s * 0.3, 0, d * s * 0.55, 0, TINTA2, a, 4)
    M.rrect(c, -s * 0.3, -s * 0.34, s * 0.6, s * 0.68, 6, "#C9A227", a)
    c.drawCircle(0, -s * 0.48, s * 0.16, M.paint(TINTA2, a))
    c.restore()


def marte(c, cx, cy, r, a=1.0):
    E.bola(c, cx, cy, r, "#C4512A", a)
    for dx, dy, k in ((-0.3, -0.25, 0.16), (0.25, 0.1, 0.11), (-0.05, 0.38, 0.09), (0.38, -0.35, 0.07)):
        c.drawCircle(cx + dx * r, cy + dy * r, k * r, M.paint("#7A2A12", 0.35 * a))


def b_gancho(c, t, C, b):
    def um():
        cx, cy, r = 1440, 600, 270
        E.foco(c, t, C["s01.a"] + 0.3, 0.7, lambda a: marte(c, cx, cy, r, a), blur=0)
        E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: centro(c, "Marte", cx, cy + r + 90, 60, "i", TINTA2, a))
        # a sonda chega por um arco e, em s01.b, passa reto e some
        p = ease_io(prog(t, C["s01.a"] + 0.4, 2.2))
        if t < C["s01.b"]:
            px, py = lerp(900, 1180, p), lerp(200, 330, p) - 60 * math.sin(p * math.pi)
            E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: sonda(c, px, py, 58, a, 10))
        else:
            q = ease_out(prog(t, C["s01.b"], 1.4))
            px, py = lerp(1180, 1830, q), lerp(330, 150, q)
            sonda(c, px, py, 58 * (1 - 0.5 * q), 1 - q, 10 + 300 * q)
            E.foco(c, t, C["s01.b"] + 0.6, 0.4, lambda a: E.pilula(c, "perdida", 1700, 220, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s01.a"], [("1999", "g", 170, TINTA)], XE, 330)
        E.frase(c, t, C["s01.a"] + 0.8, ps("uma sonda da NASA", "i", 76), XE, 450, passo=0.12)
        E.frase(c, t, C["s01.b"], [("se", "i", 90), ("perdeu", "g", 90, ERRADO)], XE, 570)
        E.frase(c, t, C["s01.c"] - 0.6, [("culpa", "i", 80), ("de", "i", 80), ("uma", "i", 80)], XE, 720)
        E.frase(c, t, C["s01.c"], [("unidade", "g", 130, COR)], XE, 860)
    E.saida(c, t, C["s01.d"] - 0.15, um)
    if C["s01.d"] - 0.15 <= t < C["s02"]:
        def dois():
            for i, (k, l1, l2, l3) in enumerate((("s01.d", "equipe 1", "unidades inglesas", "libra · pé"),
                                                  ("s01.e", "equipe 2", "sistema métrico", "quilograma · metro"))):
                x = 230 + i * 820
                p = ep(t, C[k], 0.5)
                E.caixa_pontilhada(c, x, 330, 640, 420, p, prog_=p)
                E.frase(c, t, C[k] + 0.1, [(l1, "i", 64, TINTA2)], x + 50, 430)
                E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR if i else TINTA)], x + 50, 540)
                E.frase(c, t, C[k] + 0.6, [(l3, "b", 50, TINTA2)], x + 50, 650)
            E.foco(c, t, C["s01.e"] + 0.5, 0.5, lambda a: centro(c, "≠", W / 2 - 5, 590, 170, "g", ERRADO, a))
            E.frase(c, t, C["s01.e"] + 1.2, ps("as contas não conversavam", "i", 66), W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s02"] - 0.1, dois)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.a", "unidade certa", 1.4), ("s02.b", "direção e sentido", 0), ("s02.c", "conferir a fórmula", 0))
        for i, (k, s, dt) in enumerate(itens):
            y = 450 + i * 160
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                            centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 84, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def prefixo(a, x, y):
        E.formula(c, "quilo = 10^3", x - 40, y + 20, 56, "g", TINTA, a, "center")

    def corte(a, x, y):
        F.termo(c, 99, -1, x - 20, y - 12, 56, ("60", "min"), ("1", "h"), cortes=[("c", "u", -1)])
    lembrete2(c, t, C, "s03", (("s03.b", "os prefixos,", "como o quilo"), ("s03.c", "cortar unidades,", "fatores que valem 1")),
              (prefixo, corte))


# ---------------- grandeza física ----------------
def mesa(c, x, y, w, a=1.0):
    """mesa de lado: tampo em y, pernas até y + 260"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, 34, 8, "#8B5E3C", a)
    for lx in (x + 40, x + w - 70):
        M.rrect(c, lx, y + 30, 30, 170, 6, "#6E4A2F", a)


def b_grandeza(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], [("grandeza", "i", 100), ("física", "g", 100, COR)], XE, 250)
        E.frase(c, t, C["s04.a"], ps("tudo o que dá para", "i", 76) + [("medir", "g", 76)], XE, 370, passo=0.12)
        for i, s in enumerate(("comprimento", "massa", "tempo", "velocidade")):
            ti = lerp(C["s04.a"] + 1.4, C["s04.b"] - 0.6, i / 3)
            x = XE + 20 + [0, 380, 640, 880][i]
            E.foco(c, t, ti, 0.4, lambda a, s=s, x=x: E.pilula(c, s, x + (E.larg(s, "g", 44) + 48) / 2, 480, 44, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s04.b"], [("medir", "g", 80), ("=", "g", 80, TINTA2), ("comparar", "i", 84), ("com", "i", 84), ("um", "i", 84),
                                   ("padrão", "g", 80, COR)], XE, 660, passo=0.14)
        # mesa de 2 m: o metro cabe duas vezes
        mx, my, mw = 760, 820, 900
        E.foco(c, t, C["s04.c"] - 1.6, 0.5, lambda a: mesa(c, mx, my, mw, a))
        for k in range(2):
            tk = C["s04.c"] + 0.7 * k
            q = ease_io(prog(t, tk, 0.6))
            if q > 0:
                x0 = mx + k * mw / 2
                yy = lerp(my - 160, my - 60, q)
                M.rrect(c, x0 + 6, yy, mw / 2 - 12, 44, 10, E.COR, q)
                for j in range(1, 10):
                    M.line(c, x0 + 6 + (mw / 2 - 12) * j / 10, yy, x0 + 6 + (mw / 2 - 12) * j / 10, yy + (18 if j != 5 else 28), BR, q, 3)
                F.medida(c, 1, "m", x0 + mw / 4, yy - 22, 56, TINTA, q, "center")
        E.foco(c, t, C["s04.c"] + 1.5, 0.4, lambda a: F.medida(c, 2, "m", mx + mw + 60, my + 40, 90, COR, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], ps("toda medida tem duas partes", "i", 80), W / 2, 210, "center", 0.12)

    def partes():
        y = 470
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.escreve(c, "2", 700, y, 240, "g", TINTA, a))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "m", 900, y, 240 * 0.72, "b", F.UNID, a))
        E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: centro(c, "número", 770, y + 110, 58, "i", TINTA2, a))
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: centro(c, "unidade", 1000, y + 110, 58, "i", TINTA2, a))
    E.saida(c, t, C["s05.c"] - 0.1, partes)
    if t < C["s05.c"]:
        return
    E.foco(c, t, C["s05.c"], 0.5, lambda a: (E.escreve(c, "20", XE + 40, 500, 200, "g", TINTA, a),
                                             E.escreve(c, "?", XE + 300, 500, 200, "g", ERRADO, a)))
    E.frase(c, t, C["s05.c"] + 0.4, ps("só o número", "i", 64) + [("não diz nada", "g", 60, ERRADO)], XE + 20, 620, passo=0.12)
    E.foco(c, t, C["s05.d"], 0.5, lambda a: (F.medida(c, 20, "km/h", 900, 470, 110, TINTA, a), bicicleta(c, 1630, 520, 70, a)))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: (F.medida(c, 20, "m/s", 900, 780, 110, COR, a), F.carrinho(c, 1640, 820, 260, a=a)))
    E.foco(c, t, C["s05.d"] + 0.6, 0.4, lambda a: E.escreve(c, "bicicleta", 900, 545, 50, "i", TINTA2, a))
    E.foco(c, t, C["s05.e"] + 0.6, 0.4, lambda a: E.escreve(c, "carro na estrada", 900, 855, 50, "i", TINTA2, a))


# ---------------- o SI ----------------
def tabela_si(c, t, C, y0, k=1.0):
    """grandeza · unidade · símbolo, uma linha por cue"""
    cols = (XE + 40, 820, 1420)
    cab = ("grandeza", "unidade", "símbolo")
    E.foco(c, t, C["s06.b"] - 0.6, 0.4, lambda a: [E.escreve(c, s, x, y0, 46 * k, "i", TINTA2, a) for s, x in zip(cab, cols)])
    if t >= C["s06.b"] - 0.6:
        M.line(c, XE + 30, y0 + 26, 1700, y0 + 26, TINTA2, ep(t, C["s06.b"] - 0.6, 0.4), 3)
    for i, (k_, g, u, s) in enumerate((("s06.b", "comprimento", "metro", "m"), ("s06.c", "massa", "quilograma", "kg"), ("s06.d", "tempo", "segundo", "s"))):
        y = y0 + (130 + 120 * i) * k
        E.foco(c, t, C[k_], 0.5, lambda a, g=g, u=u, s=s, y=y: (E.escreve(c, g, cols[0], y, 66 * k, "i", TINTA, a),
                                                                E.escreve(c, u, cols[1], y, 66 * k, "g", TINTA, a),
                                                                E.escreve(c, s, cols[2], y, 76 * k, "g", COR, a)))


def b_si(c, t, C, b):
    def s06():
        E.foco(c, t, C["s06.a"], 0.5, lambda a: E.escreve(c, "SI", XE, 300, 200, "g", COR, a))
        E.frase(c, t, C["s06.a"] + 0.3, ps("Sistema Internacional", "g", 70), XE + 300, 220, passo=0.12)
        E.frase(c, t, C["s06.a"] + 0.7, ps("de Unidades", "i", 74), XE + 300, 300, passo=0.12)
        E.frase(c, t, lerp(C["s06.a"], C["s06.b"], 0.45), ps("7 de base;", "i", 54, TINTA2) + ps("para o movimento,", "i", 54, TINTA2) + [("3", "g", 54, COR)],
                XE, 410, passo=0.08)
        tabela_si(c, t, C, 530)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], ps("as outras se", "i", 80) + [("montam", "g", 80, COR)], XE, 230, passo=0.12)
            E.frase(c, t, C["s07.a"], [("área", "i", 80)], XE, 450)
            E.formula_em(c, t, C["s07.a"] + 0.6, "m × m = ", XE + 420, 450, 96, "g", TINTA)
            E.foco(c, t, C["s07.a"] + 1.4, 0.5, lambda a: E.formula(c, "m^2", XE + 420 + E.formula(None, "m × m = ", 0, 0, 96, a=0), 450, 96, "g", COR, a))
            E.frase(c, t, C["s07.b"], [("velocidade", "i", 80)], XE, 700)
            E.formula_em(c, t, C["s07.b"] + 0.8, "f{distância}{tempo} → f{m}{s} = ", XE + 420, 700, 80, "g", TINTA)
            wv = E.formula(None, "f{distância}{tempo} → f{m}{s} = ", 0, 0, 80, a=0)
            E.foco(c, t, C["s07.b"] + 1.8, 0.5, lambda a: E.formula(c, "m/s", XE + 420 + wv, 700, 80, "g", COR, a))
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], ps("duas", "i", 84) + [("pegadinhas", "g", 84, COR)], W / 2, 200, "center")
    x1, x2, w, y, h = 170, 1000, 750, 300, 560
    for x, k in ((x1, "s08.a"), (x2, "s08.b")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    # 1: quilograma, não grama
    E.frase(c, t, C["s08.a"], [("massa", "i", 70)], x1 + 50, y + 110)
    E.foco(c, t, C["s08.a"] + 0.5, 0.5, lambda a: E.escreve(c, "kg", x1 + 60, y + 300, 170, "g", CERTO, a))
    E.foco(c, t, C["s08.a"] + 1.0, 0.5, lambda a: E.escreve(c, "g", x1 + 420, y + 300, 170, "g", ERRADO, a))
    if t >= C["s08.a"] + 1.5:
        E.risco(c, x1 + 410, y + 320, x1 + 530, y + 180, t, C["s08.a"] + 1.5, largura=12)
    E.frase(c, t, lerp(C["s08.a"], C["s08.b"], 0.55), ps("a única com", "i", 56) + [("prefixo", "g", 56, COR)], x1 + 50, y + 460, passo=0.1)
    # 2: hora e km/h
    E.frase(c, t, C["s08.b"], ps("muito usadas", "i", 66), x2 + 50, y + 110, passo=0.12)
    E.foco(c, t, C["s08.b"] + 0.6, 0.5, lambda a: (F.medida(c, "", "h", x2 + 60, y + 290, 150, TINTA, a, cor_u=TINTA),
                                                   F.medida(c, "", "km/h", x2 + 260, y + 290, 150, TINTA, a, cor_u=TINTA)))
    pilula_em(c, t, C["s08.c"], "fora do SI", x2 + w / 2, y + 440, 52, ERRADO)


# ---------------- converter ----------------
def b_converter(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("passe tudo para", "i", 70) + [("m,", "g", 70, COR), ("kg", "g", 70, COR), ("e", "i", 70), ("s", "g", 70, COR)],
            W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (F.medida(c, 72, "km/h", 960 - 40, 320, 96, TINTA, a, "right"),
                                             E.escreve(c, "→", 960 + 10, 320, 90, "g", TINTA2, a),
                                             F.medida(c, "?", "m/s", 960 + 140, 320, 96, COR, a)))
    if t < C["s10"]:
        return
    ta, tb = C["s11.a"], C["s11.b"]
    itens = [dict(t0=C["s10"], cima=("72", "km"), baixo=("1", "h"), cortes=[("c", "u", ta), ("b", "u", tb)]),
             dict(t0=C["s10.a"], cima=("1.000", "m"), baixo=("1", "km"), cortes=[("b", "u", ta + 0.15)]),
             dict(t0=C["s10.b"], cima=("1", "h"), baixo=("3.600", "s"), cortes=[("c", "u", tb + 0.15)])]
    xs, _ = F.fila(c, t, itens, W / 2, 540, 96)
    E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: centro(c, "some o km", xs[1], 740, 46, "i", TINTA2, a))
    E.foco(c, t, C["s10.b"] + 0.6, 0.4, lambda a: centro(c, "some a h", xs[2], 740, 46, "i", TINTA2, a))
    contas = [(lerp(C["s10.b"], C["s11"], 0.55), "1 h = 60 × 60 s = 3.600 s"), (C["s11"], "")]
    troca(c, t, contas, lambda s, a: centro(c, s, W / 2, 900, 60, "b", TINTA2, a) if s else None)
    y = 900

    def r1(a):
        centro(c, "=", 640, y + 20, 100, "g", TINTA2, a)
        F.termo(c, 99, -1, 900, y - 30, 80, ("72.000", "m"), ("3.600", "s"))
        E.escreve(c, "corte dois zeros", 1150, y - 10, 48, "i", TINTA2, a) if t >= C["s11.c"] + 1.4 else None
    if C["s11.c"] <= t:
        E.saida(c, t, C["s11.d"] - 0.1, lambda: E.foco(c, t, C["s11.c"], 0.45, r1))
    if C["s11.d"] <= t:
        E.saida(c, t, C["s11.e"] - 0.1, lambda: E.foco(c, t, C["s11.d"], 0.45, lambda a: centro(c, "= 720 ÷ 36", W / 2, y + 10, 90, "g", TINTA, a)))
    bola_txt(c, t, C["s11.e"], "20 m/s", W / 2, y - 20, 125, 70)


# ---------------- escalar e vetorial ----------------
def b_vetorial(c, t, C, b):
    def s12():
        E.foco(c, t, C["s12.a"], 0.6, lambda a: F.bloco(c, 1400, 430, 360, 260, "60 kg", a=a))
        F.chao(c, 1160, 1640, 560, ep(t, C["s12.a"], 0.5)) if t >= C["s12.a"] else None
        E.frase(c, t, C["s12.a"], [("massa", "i", 80)], XE, 330)
        E.foco(c, t, C["s12.a"] + 0.5, 0.5, lambda a: F.medida(c, 60, "kg", XE + 300, 330, 110, TINTA, a))
        E.frase(c, t, C["s12.b"], ps("número e unidade", "i", 70) + [("dizem", "g", 66), ("tudo", "g", 66, CERTO)], XE, 470, passo=0.12)
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "ESCALAR", XE + 290, 640, 84, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s12.d"], 0.5, lambda a: F.cronometro(c, 1260, 830, 95, 5, a, "5 s"))
        if t >= C["s12.d"] + 0.4:
            F.termometro(c, t, C["s12.d"] + 0.4, 1620, 960, 300, 30, 0, 40, [0, 30], "°C")
        E.frase(c, t, C["s12.d"], [("tempo", "g", 70), ("e", "i", 74), ("temperatura", "g", 70)], XE, 830, passo=0.2)
        E.frase(c, t, C["s12.d"] + 0.8, ps("também são escalares", "i", 64, TINTA2), XE, 930, passo=0.12)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if C["s13"] <= t < C["s14"]:
        def s13():
            O, R = (1250, 560), 300
            E.frase(c, t, C["s13.a"], [("ande", "i", 100), ("3", "g", 100, COR)], XE, 340)
            xm_ = XE + E.larg("ande", "i", 100) + 26 + E.larg("3", "g", 100) + 18
            E.foco(c, t, C["s13.a"] + 0.2, 0.4, lambda a: E.formula(c, "m", xm_, 340, 72, "b", F.UNID, a))
            E.frase(c, t, C["s13.a"] + 1.0, [("para", "i", 100), ("onde?", "g", 100, COR)], XE, 480)
            E.foco(c, t, C["s13.a"] + 0.2, 0.4, lambda a: E.bola(c, *O, 26, TINTA, a), blur=0)
            for i in range(10):
                g = math.radians(90 - 36 * i)
                ti = C["s13.a"] + 1.5 + 0.12 * i
                F.vetor(c, t, ti, O, (O[0] + R * math.cos(g) * 0.93, O[1] - R * math.sin(g) * 0.93), largura=7, cor=F.VEL)
            if t >= C["s13.b"]:
                pt = M.paint(TINTA2, ep(t, C["s13.b"], 0.6), stroke=5)
                pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
                c.drawArc(skia.Rect.MakeXYWH(O[0] - R, O[1] - R, 2 * R, 2 * R), -90, 360 * ease_io(prog(t, C["s13.b"], 0.9)), False, pt)
                E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: E.pilula(c, "3 m para qualquer lado", O[0], O[1] + R + 70, 42, "b", fundo=TINTA2, a=a))
            E.frase(c, t, C["s13.c"], [("falta:", "i", 74), ("direção", "g", 74, COR)], XE, 700)
            E.frase(c, t, C["s13.d"], [("e", "i", 74), ("sentido", "g", 74, COR)], XE + 205, 810)
        E.saida(c, t, C["s14"] - 0.1, s13)
    if C["s14"] <= t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14.a"], [("direção", "g", 84, COR), ("=", "g", 84, TINTA2), ("a", "i", 88), ("linha", "i", 88)], XE, 240, passo=0.12)
            linhas = (("horizontal", (980, 420), (1760, 420)), ("vertical", (1180, 180), (1180, 560)), ("inclinada", (1380, 560), (1700, 220)))
            for i, (s, A, B) in enumerate(linhas):
                ti = C["s14.a"] + 1.0 + 0.6 * i
                q = ease_io(prog(t, ti, 0.5))
                if q > 0:
                    M.line(c, *A, *B, TINTA, 0.8, 5, dash=E.TRACO, progress=q)
                    E.foco(c, t, ti + 0.2, 0.4, lambda a, s=s, A=A, i=i: E.escreve(c, s, (980, 1200, 1500)[i], (470, 200, 600)[i], 44, "i", TINTA2, a))
            E.frase(c, t, C["s14.b"], [("sentido", "g", 84, COR), ("=", "g", 84, TINTA2), ("para", "i", 88), ("que", "i", 88), ("lado", "i", 88)],
                    XE, 760, passo=0.12)
            y = 880
            M.line(c, 760, y, 1700, y, TINTA, 0.8 * ep(t, C["s14.b"], 0.4), 5, dash=E.TRACO) if t >= C["s14.b"] else None
            F.vetor(c, t, C["s14.b"] + 1.2, (1240, y), (1640, y), None, None, F.VEL, 10)
            F.vetor(c, t, C["s14.b"] + 2.2, (1220, y), (820, y), None, None, F.VEL, 10)
            E.foco(c, t, C["s14.b"] + 1.4, 0.4, lambda a: centro(c, "para a direita", 1440, y + 80, 44, "i", TINTA2, a))
            E.foco(c, t, C["s14.b"] + 2.4, 0.4, lambda a: centro(c, "para a esquerda", 1020, y + 80, 44, "i", TINTA2, a))
        E.saida(c, t, C["s14.c"] - 1.7, s14)
        if t >= C["s14.c"] - 1.6:
            E.frase(c, t, C["s14.c"] - 1.6, ps("precisa disso?", "i", 90), W / 2, 380, "center", 0.12)
            E.foco(c, t, C["s14.c"], 0.5, lambda a: E.pilula(c, "VETORIAL", W / 2, 600, 110, "g", fundo=E.COR, a=a))
    if t < C["s15"]:
        return

    # s15: anatomia do vetor
    A, B = (900, 640), (1600, 300)
    E.frase(c, t, C["s15"], ps("desenhada como seta:", "i", 74), XE, 200, passo=0.12)
    E.frase(c, t, C["s15.a"], [("o", "i", 90), ("vetor", "g", 90, COR)], XE + 680, 200)
    if t >= C["s15.c"]:
        ux, uy = E._uni(*A, *B)
        q = ep(t, C["s15.c"], 0.6)
        M.line(c, A[0] - ux * 260, A[1] - uy * 260, B[0] + ux * 220, B[1] + uy * 220, TINTA2, 0.7 * q, 4, dash=E.TRACO)
    F.vetor(c, t, C["s15.a"], A, B, "d", "3 m", E.COR, 12, 0.8, lado=1, size=64)
    def legenda(k, s1, s2, y):
        E.foco(c, t, C[k], 0.5, lambda a: (E.bola(c, XE + 30, y - 22, 26, a=a)))
        E.frase(c, t, C[k] + 0.1, [(s1, "g", 64), (s2, "i", 64, TINTA2)], XE + 80, y, passo=0.12)
    legenda("s15.b", "tamanho", "= módulo", 400)
    legenda("s15.c", "linha", "= direção", 510)
    legenda("s15.d", "ponta", "= sentido", 620)
    if t >= C["s15.b"]:  # o módulo: cota ao lado da seta
        E.segmento(c, t, C["s15.b"], (A[0] + 40, A[1] + 70), (B[0] + 40, B[1] + 70), None, cor=TINTA2, largura=4, pontas=False, d=0.6)
    q = ep(t, C["s15.d"], 0.4) * (1 - ep(t, C["s15.e"], 0.4))
    if q > 0:
        c.drawCircle(*B, 60 + 8 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
    E.frase(c, t, C["s15.e"], [("vetoriais:", "i", 60)], XE, 800)
    for i, (s, cor) in enumerate((("deslocamento", F.VEL), ("velocidade", F.VEL), ("força", E.COR))):
        x = XE + [0, 450, 820][i]
        E.foco(c, t, C["s15.e"] + 0.3 + 0.8 * i, 0.4, lambda a, s=s, x=x, cor=cor: E.pilula(c, s, x + (E.larg(s, "g", 44) + 48) / 2, 900, 44, "g", fundo=cor, a=a))
    E.foco(c, t, C["s15.f"] - 0.3, 0.5, lambda a: velocimetro(c, 1640, 860, 150, 72, 180, "72 km/h", a))
    E.foco(c, t, C["s15.f"] + 0.3, 0.4, lambda a: E.pilula(c, "só o módulo", 1640, 655, 40, "b", fundo=TINTA, a=a))


# ---------------- conferir a fórmula ----------------
def b_formula(c, t, C, b):
    if t < C["s18"]:
        E.frase(c, t, C["s16.a"], ps("conferir uma", "i", 80) + [("fórmula", "g", 80, COR)], W / 2, 180, "center", 0.12)
        E.frase(c, t, C["s16.b"], ps("distância = velocidade × tempo", "i", 62, TINTA2), W / 2, 300, "center", 0.1)

        termos = [("d", "m"), ("=", None), ("v", "m/s"), ("·", None), ("t", "s")]
        cs = F.unidades(c, t, C["s16.c"], termos, W / 2, 520, 150, C["s16.d"])
        yu = 520 + 150 * 0.95
        if t >= C["s17.a"]:  # o segundo de [m/s] corta com o de [s]
            su = 75
            wv, wt = E.formula(None, "[m/s]", 0, 0, su, "b", a=0), E.formula(None, "[s]", 0, 0, su, "b", a=0)
            xs1 = cs[2] + wv / 2 - E.formula(None, "s]", 0, 0, su, "b", a=0)
            xs2 = cs[4] - wt / 2 + E.formula(None, "[", 0, 0, su, "b", a=0)
            for k, x in enumerate((xs1, xs2)):
                M.line(c, x - 6, yu + 8, x + 44, yu - 58, E.COR, 1.0, 7, progress=ep(t, C["s17.a"] + 0.2 * k, 0.35))
            E.foco(c, t, C["s17.b"], 0.5, lambda a: E.pilula(c, "sobra metro", W / 2 + 200, yu + 88, 44, "g", fundo=E.COR, a=a))
            E.foco(c, t, C["s17.c"], 0.5, lambda a: E.selo(c, W / 2 + 560, 470, 70, True, a))
        E.saida(c, t, C["s17.d"] - 0.1, lambda: E.frase(c, t, C["s17.c"], [("m", "g", 66, CERTO), ("=", "g", 66), ("m:", "g", 66, CERTO), ("coerente", "g", 66, CERTO)],
                                                         W / 2, 880, "center", 0.12) if t >= C["s17.c"] else None)
        if t >= C["s17.d"]:
            E.frase(c, t, C["s17.d"], ps("os dois lados do", "i", 64) + [("=", "g", 64, COR)] + ps("têm a", "i", 64) + [("mesma unidade", "g", 60, COR)],
                    W / 2, 880, "center", 0.1)
            E.frase(c, t, C["s17.e"], [("unidade", "i", 50), ("errada", "g", 50, ERRADO), ("→", "g", 50, TINTA2), ("fórmula", "i", 50), ("errada", "g", 50, ERRADO)],
                    W / 2 - 420, 1000, "center", 0.08)
            E.frase(c, t, C["s17.f"], [("unidade", "i", 50), ("certa", "g", 50, CERTO), ("→", "g", 50, TINTA2), ("ainda", "i", 50), ("não", "i", 50), ("prova", "g", 50)],
                    W / 2 + 420, 1000, "center", 0.08)
        return
    # s18: a fórmula lembrada errado
    E.frase(c, t, C["s18"], ps("se alguém lembrar", "i", 76) + [("errado", "g", 76, ERRADO)], W / 2, 180, "center", 0.12)
    E.formula_em(c, t, C["s18.a"], "d = f{v}{t}", W / 2 - 380, 430, 150, "g", ERRADO, "center")
    E.formula_em(c, t, C["s18.b"], "f{m/s}{s}", W / 2 + 120, 430, 96, "b", F.UNID, "center")
    E.formula_em(c, t, C["s18.c"], "= m/s^2", W / 2 + 240, 430, 96, "g", TINTA, "left")
    E.foco(c, t, C["s18.c"] - 0.6, 0.4, lambda a: centro(c, "s duas vezes embaixo", W / 2 + 120, 570, 46, "i", TINTA2, a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "m/s² existe: é a da aceleração (outra aula)", W / 2, 690, 46, "b", fundo=F.ACEL, a=a))
    E.frase(c, t, C["s18.e"], [("m/s²", "g", 84, ERRADO), ("não", "i", 90), ("é", "i", 90), ("metro", "g", 84)], W / 2, 870, "center", 0.12)
    E.foco(c, t, C["s18.e"] + 1.0, 0.5, lambda a: E.selo(c, W / 2 + 470, 840, 60, False, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s19"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s19.a"], ps("misturar unidades", "i", 76), XE + 480, 200, passo=0.12)
    vx = lambda v: 300 + v * 5.2

    def s19():
        F.chao(c, 160, 1760, 520, ep(t, C["s19"] + 2.0, 0.5)) if t >= C["s19"] + 2.0 else None
        E.foco(c, t, C["s19"] + 2.0, 0.5, lambda a: F.carrinho(c, 420, 520, 240, a=a))
        E.foco(c, t, C["s19"] + 2.4, 0.4, lambda a: F.medida(c, 72, "km/h", 420, 330, 70, TINTA, a, "center"))
        E.foco(c, t, C["s19.b"], 0.5, lambda a: F.cronometro(c, 1500, 330, 95, 10, a, "10 s"))
        E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "72 × 10 = 720", W / 2, 720, 110, "g", TINTA, a, "center"))
        E.foco(c, t, C["s19.d"], 0.5, lambda a: E.escreve(c, "720 m?", W / 2 - 180, 900, 120, "g", ERRADO, a))
        if t >= C["s19.d"] + 0.8:
            E.risco(c, W / 2 - 200, 920, W / 2 + 200, 810, t, C["s19.d"] + 0.8, largura=12)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    # nada corta: km/h × s
    itens = [dict(t0=C["s20.a"], cima=("72", "km"), baixo=("1", "h"), cor=TINTA), dict(t0=C["s20.a"] + 0.4, cima=("10", "s"))]
    xs, xd = F.fila(c, t, itens, 620, 420, 96)
    E.foco(c, t, C["s20.a"] + 1.0, 0.4, lambda a: (E.pilula(c, "h embaixo", xs[0], 620, 40, "b", fundo=ERRADO, a=a),
                                                  E.pilula(c, "s em cima", xs[1], 620, 40, "b", fundo=ERRADO, a=a)))
    E.frase(c, t, C["s20.b"], [("nada", "g", 76, ERRADO), ("corta", "g", 76, ERRADO)], 620, 760, "center")
    # no SI
    itens2 = [dict(t0=C["s20.c"], cima=("20", "m"), baixo=("1", "s"), cortes=[("b", "u", C["s20.c"] + 1.4)]),
              dict(t0=C["s20.c"] + 0.5, cima=("10", "s"), cortes=[("c", "u", C["s20.c"] + 1.6)])]
    xs2, xd2 = F.fila(c, t, itens2, 1380, 420, 96)
    if t >= C["s20.c"]:
        M.line(c, 1000, 260, 1000, 820, FIO, ep(t, C["s20.c"], 0.4), 3)
    bola_txt(c, t, C["s20.d"], "200 m", 1380, 700, 130, 74, CERTO)
    E.frase(c, t, C["s20.d"] + 1.0, [("200", "g", 64, CERTO), ("bem", "i", 66), ("menos", "i", 66), ("que", "i", 66), ("720", "g", 64, ERRADO)],
            W / 2, 960, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s21():
        E.frase(c, t, C["s21"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s21.a"], [("decore", "i", 76, CLARO), ("só", "i", 76, CLARO)], W / 2 - 330, 320, "center", 0.12)
        for i, s in enumerate(("m", "kg", "s")):
            E.foco(c, t, C["s21.a"] + 0.6 + 0.3 * i, 0.4, lambda a, i=i, s=s: (E.bola(c, 1000 + 170 * i, 295, 66, a=a), centro(c, s, 1000 + 170 * i, 318, 64, "g", BR, a)))
        E.frase(c, t, C["s21.a"] + 2.0, ps("as outras:", "i", 70, CLARO) + [("tire", "g", 70, BR), ("da", "g", 70, BR), ("fórmula", "g", 70, BR)], W / 2, 460, "center", 0.12)
        E.formula_em(c, t, C["s21.b"], "vazão = f{volume}{tempo}", W / 2 - 120, 650, 84, "g", BR, "right")
        E.formula_em(c, t, C["s21.c"] - 0.5, "→ f{m^3}{s} = ", W / 2 - 60, 650, 84, "g", CLARO, "left")
        wv = E.formula(None, "→ f{m^3}{s} = ", 0, 0, 84, a=0)
        E.foco(c, t, C["s21.c"], 0.5, lambda a: (E.bola(c, W / 2 - 60 + wv + 130, 625, 110, a=a),
                                                 E.formula(c, "m^3/s", W / 2 - 60 + wv + 130, 650, 64, "g", BR, a, "center")))
        E.frase(c, t, C["s21.d"], ps("algumas ganham nome:", "i", 56, CLARO) + [("newton", "g", 56, BR)] + ps("(força, outra aula)", "i", 56, CLARO),
                W / 2, 900, "center", 0.1)
    E.saida(c, t, C["s22"] - 0.1, s21)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22.a"], ps("a unidade faz", "i", 70, CLARO) + [("as mesmas contas", "g", 66, BR)] + ps("que o número", "i", 70, CLARO),
            W / 2, 190, "center", 0.12)
    E.frase(c, t, C["s22.b"], ps("pede uma", "i", 64, CLARO) + [("distância:", "g", 64, BR)], W / 2, 340, "center", 0.12)
    for i, (f_, u, ok) in enumerate((("d = v · t", "m", True), ("d = f{v}{t}", "m/s^2", False))):
        y = 520 + i * 190
        ti = C["s22.b"] + 1.0 + 1.2 * i
        E.foco(c, t, ti, 0.5, lambda a, i=i, f_=f_, y=y: (E.pilula(c, "AB"[i], 560, y - 30, 44, "g", fundo=E.COR, a=a),
                                                         E.formula(c, f_, 660, y, 84, "g", BR, a)))
        E.foco(c, t, ti + 0.6, 0.4, lambda a, u=u, y=y, ok=ok: (E.formula(c, "→ " + u, 1060, y, 72, "b", CLARO, a),
                                                                E.selo(c, 1440, y - 26, 44, ok, a)))
    if t >= C["s22.b"] + 3.2:
        E.risco(c, 640, 740, 960, 650, t, C["s22.b"] + 3.2, largura=10)
    E.frase(c, t, C["s22.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("todas com a mesma unidade", "i", 64, CLARO),
            W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s23"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s23.a"], [("ciclista", "i", 80)], XE, 360)
    E.foco(c, t, C["s23.a"] + 0.3, 0.5, lambda a: F.medida(c, 18, "km/h", XE + 330, 360, 100, COR, a))
    E.frase(c, t, C["s23.b"], ps("quantos", "i", 80) + [("metros", "g", 76)], XE, 520, passo=0.12)
    E.frase(c, t, C["s23.b"] + 0.6, ps("em", "i", 80) + [("1 minuto?", "g", 76, COR)], XE, 630, passo=0.12)
    E.frase(c, t, C["s23.c"], [("escalar", "g", 70), ("ou", "i", 76), ("vetorial?", "g", 70, COR)], XE, 800, passo=0.15)
    if t < C["s24"]:
        E.foco(c, t, C["s23.a"], 0.6, lambda a: bicicleta(c, 1460, 660, 130, a))
        if t >= C["s23.a"]:
            F.chao(c, 1080, 1840, 660, ep(t, C["s23.a"], 0.5))
    else:
        E.relogio(c, t, C["s24.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s25():
        a_, b_, c_ = C["s25.a"], C["s25.b"], C["s25.c"]
        itens = [dict(t0=a_, cima=("18", "km"), baixo=("1", "h"), cortes=[("c", "u", b_ + 0.8), ("b", "u", c_ + 0.9)]),
                 dict(t0=b_, cima=("1.000", "m"), baixo=("1", "km"), cortes=[("b", "u", b_ + 0.95)]),
                 dict(t0=c_, cima=("1", "h"), baixo=("3.600", "s"), cortes=[("c", "u", c_ + 1.05)])]
        F.fila(c, t, itens, W / 2, 330, 96)
        y = 640
        troca(c, t, [(C["s25.d"], "= 18.000 ÷ 3.600"), (lerp(C["s25.d"], C["s25.e"], 0.5), "= 180 ÷ 36")],
              lambda s, a: centro(c, s, W / 2, y, 90, "g", TINTA, a))
        bola_txt(c, t, C["s25.e"], "5 m/s", W / 2, 860, 120, 70)
    E.saida(c, t, C["s26"] - 0.1, s25)
    if t < C["s26"]:
        return
    E.frase(c, t, C["s26.a"], [("1", "g", 80), ("minuto", "i", 84), ("=", "g", 80, TINTA2), ("60", "g", 80, COR), ("s", "b", 70, F.UNID)], XE, 210, passo=0.12)
    itens = [dict(t0=C["s26.b"], cima=("5", "m"), baixo=("1", "s"), cortes=[("b", "u", C["s26.b"] + 1.6)]),
             dict(t0=C["s26.b"] + 0.5, cima=("60", "s"), cortes=[("c", "u", C["s26.b"] + 1.8)])]
    F.fila(c, t, itens, 560, 430, 96)
    bola_txt(c, t, C["s26.c"], "300 m", 560, 720, 130, 74, CERTO)
    # a velocidade é vetorial: a bicicleta com a seta
    E.foco(c, t, C["s26.d"], 0.5, lambda a: bicicleta(c, 1330, 640, 95, a))
    if t >= C["s26.d"]:
        F.chao(c, 1050, 1800, 640, ep(t, C["s26.d"], 0.4))
    F.vetor(c, t, C["s26.d"] + 0.5, (1330, 360), (1720, 360), "v", None, F.VEL, 11, size=64)
    E.foco(c, t, C["s26.d"] + 0.3, 0.5, lambda a: E.pilula(c, "VETORIAL", 1420, 800, 70, "g", fundo=E.COR, a=a))
    E.frase(c, t, lerp(C["s26.d"], C["s26.end"], 0.25), [("18", "g", 56), ("é", "i", 60), ("só", "i", 60), ("o", "i", 60), ("módulo", "g", 56, COR)],
            1420, 950, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s27"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s27.a", [("número", "g", 70), ("+", "g", 70, COR), ("unidade", "g", 70)]),
                 ("s27.b", [("tudo", "i", 70), ("em", "i", 70), ("m,", "g", 70, COR), ("kg", "g", 70, COR), ("e", "i", 70), ("s", "g", 70, COR)]),
                 ("s27.c", [("vetorial:", "g", 70), ("direção", "i", 70), ("e", "i", 70), ("sentido", "i", 70)]),
                 ("s27.d", [("fórmula:", "g", 70), ("mesma", "i", 70), ("unidade", "i", 70), ("dos", "i", 70), ("dois", "i", 70), ("lados", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s28"] - 0.1, resumo)
    if t < C["s28"]:
        return
    E.frase(c, t, C["s28"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s28.a"], [("Somar", "g", 120, COR), ("e", "i", 110), ("subtrair", "g", 120, COR)], XE, 400)
    E.frase(c, t, C["s28.a"] + 0.5, [("vetores", "g", 120, COR)], XE, 540)
    # o barco no rio
    rx, ry, rw, rh = 330, 620, 900, 280
    q = ep(t, C["s28.b"], 0.5)
    if q > 0:
        c.drawRect(skia.Rect.MakeXYWH(rx, ry, rw, rh), M.paint("#7FC8E8", 0.35 * q))
        for yy in (ry, ry + rh):
            M.line(c, rx, yy, rx + rw, yy, "#3B8DB5", q, 5)
    O = (rx + 260, ry + rh - 30)
    F.vetor(c, t, C["s28.b"] + 0.3, O, (O[0], ry + 30), None, None, E.COR, 10)
    F.vetor(c, t, C["s28.b"] + 0.9, O, (O[0] + 300, O[1]), None, None, F.VEL, 10)
    if t >= C["s28.b"] + 1.5:
        M.line(c, *O, O[0] + 300, ry + 30, TINTA, 0.8, 5, dash=E.TRACO, progress=ease_io(prog(t, C["s28.b"] + 1.5, 0.6)))
    E.foco(c, t, C["s28.b"] + 0.3, 0.4, lambda a: E.escreve(c, "barco", O[0] - 190, ry + 140, 44, "i", TINTA, a))
    E.foco(c, t, C["s28.b"] + 0.9, 0.4, lambda a: E.escreve(c, "correnteza", O[0] + 330, O[1] + 10, 44, "i", TINTA, a))
    E.foco(c, t, C["s28.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s28.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s28.c"] + 0.2, 0.4))
    E.frase(c, t, C["s28.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grandeza=b_grandeza, si=b_si, converter=b_converter, vetorial=b_vetorial,
              formula=b_formula, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
