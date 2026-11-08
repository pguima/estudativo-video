"""Visual — Estudativo · MAT-TOP-004: princípio da casa dos pombos.
Mesma linguagem do módulo (MAT-TOP-001): resposta na esfera, erro em vermelho, certo em verde, atalho no palco escuro.
Peças desta aula: pombo() (corpo cinza, bico âmbar), casinha() (contorno com telhado), meses() (grade de 12 meses, 6 x 2,
com bolinhas = pessoas), meia() (meia preta, branca ou azul). A pessoa "que sobra" e a casinha que repete ficam na cor da matéria.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-004_principio_da_casa_dos_pombos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pombos", "meses", "dias", "meias", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
BICO = "#E8A33C"
PRETA, AZUL = "#22222A", "#3B6FD8"
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
assert divmod(13, 12) == (1, 1) and 12 * 2 + 1 == 25 and 12 * 3 == 36 and 3 * 1 + 1 == 4
assert 3 * 2 + 1 == 7 and 5 + 5 + 2 == 12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


# ---------------- peças desta aula ----------------
def pombo(c, x, y, s, a=1.0, cor="#8C8C9C"):
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(x - s * 0.5, y - s * 0.3, s, s * 0.6), M.paint(cor, a))
    path = skia.Path()  # asa
    path.moveTo(x - s * 0.35, y - s * 0.05); path.quadTo(x - s * 0.05, y - s * 0.35, x + s * 0.2, y - s * 0.02); path.close()
    c.drawPath(path, M.paint(E.mix(cor, "#000000", 0.25), a))
    c.drawCircle(x + s * 0.42, y - s * 0.28, s * 0.2, M.paint(cor, a))
    bico = skia.Path()
    bico.moveTo(x + s * 0.58, y - s * 0.32); bico.lineTo(x + s * 0.76, y - s * 0.26); bico.lineTo(x + s * 0.58, y - s * 0.2); bico.close()
    c.drawPath(bico, M.paint(BICO, a))
    c.drawCircle(x + s * 0.47, y - s * 0.32, s * 0.04, M.paint(TINTA, a))


def casinha(c, x, y, w, h, a=1.0, cor=None, cheia=0.0):
    """casinha com telhado; (x, y) = centro da base; cheia = fundo na cor"""
    cor = cor or TINTA
    if a <= 0:
        return
    r = skia.Rect.MakeXYWH(x - w / 2, y - h, w, h)
    if cheia > 0:
        c.drawRect(r, M.paint(cor, 0.15 * cheia * a))
    c.drawRect(r, M.paint(cor, a, stroke=6))
    p = skia.Path()
    p.moveTo(x - w / 2 - 20, y - h); p.lineTo(x, y - h - w * 0.45); p.lineTo(x + w / 2 + 20, y - h); p.close()
    c.drawPath(p, M.paint(cor, a, stroke=6))


def voa(t, t0, A, B, d=0.7):
    """posição de quem voa de A até B, com um arco"""
    p = ease_io(prog(t, t0, d))
    x, y = lerp(A[0], B[0], p), lerp(A[1], B[1], p)
    return x, y - 120 * 4 * p * (1 - p)


# grade de meses
MX, MY, MW, MH, MGX, MGY = 175, 215, 240, 165, 270, 200


def caixa_mes(i):
    col, lin = i % 6, i // 6
    return MX + col * MGX, MY + lin * MGY


def meses(c, t, t0, destaque=None, cor_d=None):
    for i, m in enumerate(MESES):
        x, y = caixa_mes(i)
        q = ep(t, t0 + i * 0.05, 0.4)
        if q <= 0:
            continue
        on = destaque is not None and i == destaque
        M.rrect(c, x, y, MW, MH, 18, (cor_d or COR) if on else BR, q * (0.14 if on else 0.9))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, MW, MH), 18, 18), M.paint((cor_d or COR) if on else FIO, q, stroke=4))
        centro(c, m, x + MW / 2, y + 48, 40, "b", TINTA2, q)


def gente_mes(c, t, i, k, t0, cor=TINTA, r=20):
    """k-ésima pessoa (0, 1, 2) no mês i"""
    x, y = caixa_mes(i)
    cx = x + MW / 2 + (k - 1) * 56 if k < 3 else x + MW / 2
    cy = y + 112
    s = ease_back(prog(t, t0, 0.4))
    if s > 0:
        c.drawCircle(cx, cy, r * s, M.paint(cor))


def meia(c, x, y, s, cor, a=1.0, escuro=False):
    """meia em pé: (x, y) = topo do cano; s = altura"""
    if a <= 0:
        return
    w = s * 0.36
    p = skia.Path()
    p.moveTo(x - w / 2, y)
    p.lineTo(x + w / 2, y)
    p.lineTo(x + w / 2, y + s * 0.62)
    p.quadTo(x + w / 2 + s * 0.04, y + s * 0.74, x + w / 2 + s * 0.34, y + s * 0.76)
    p.quadTo(x + w / 2 + s * 0.46, y + s * 0.88, x + w / 2 + s * 0.32, y + s)
    p.lineTo(x - w / 2 + s * 0.12, y + s)
    p.quadTo(x - w / 2 - s * 0.04, y + s, x - w / 2, y + s * 0.8)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    c.drawPath(p, M.paint(CLARO if escuro else TINTA, a, stroke=4))
    M.line(c, x - w / 2, y + s * 0.12, x + w / 2, y + s * 0.12, CLARO if escuro else TINTA, a * 0.6, 3)


def meia_em(c, t, t0, x, y, s, cor, escuro=False):
    E.foco(c, t, t0, 0.4, lambda a: meia(c, x, y, s, cor, a, escuro))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.escreve(c, "13", XE, 560, 320, "g", COR, a))
        E.frase(c, t, C["s01.a"] + 0.3, ps("pessoas", "i", 110), XE, 700)
        for i in range(12):
            col, lin = i % 4, i // 4
            x, y = 900 + col * 230, 260 + lin * 180
            q = ep(t, C["s01.a"] + 0.4 + i * 0.05, 0.4)
            on = i == 4 and t >= C["s01.b"]
            M.rrect(c, x, y, 200, 140, 16, COR if on else BR, q * (0.16 if on else 0.9))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 200, 140), 16, 16), M.paint(COR if on else FIO, q, stroke=4))
            centro(c, MESES[i], x + 100, y + 42, 36, "b", TINTA2, q)
            if on:
                for k in range(2):
                    s = ease_back(prog(t, C["s01.b"] + 0.3 + k * 0.3, 0.4))
                    if s > 0:
                        c.drawCircle(x + 70 + k * 60, y + 95, 22 * s, M.paint(COR))
        E.frase(c, t, C["s01.b"] + 0.4, ps("2 no mesmo mês", "g", 66, COR), 900, 860)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "certeza", 1500, 930, 70, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("quantos", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.4, [("garantem", "g", 120)], XE, 630)
        E.frase(c, t, C["s02.a"] + 2.0, [("uma", "i", 110), ("repetição", "g", 120, COR)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só vai precisar de", "i", 84), XE, 300)
    E.frase(c, t, C["s03.a"], [("divisão", "g", 130, COR), ("com", "i", 120), ("resto", "g", 130)], XE, 480)
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, XE, 580, 1200, 300, p, prog_=p)
    E.foco(c, t, C["s03.b"] + 0.2, 0.5, lambda a: E.escreve(c, "13 ÷ 12 = 1", XE + 60, 760, 120, "g", TINTA, a))
    E.foco(c, t, C["s03.b"] + 1.2, 0.5, lambda a: E.escreve(c, "sobra 1", XE + 760, 760, 110, "g", COR, a))


# ---------------- pombos e casinhas ----------------
CAS = [(560, 760), (960, 760), (1360, 760)]
POMBOS0 = [(560, 330), (860, 330), (1160, 330), (1460, 330)]


def b_pombos(c, t, C, b):
    def cena():
        E.frase(c, t, C["s04.a"], [("pombos", "g", 80, COR), ("e", "i", 84), ("casinhas", "g", 80)], W / 2, 170, "center")
        for i, (x, y) in enumerate(CAS):
            on = t >= C["s04.e"] + 0.6 and i == 1
            E.foco(c, t, C["s04.c"] + i * 0.15, 0.5, lambda a, x=x, y=y, on=on: casinha(c, x, y, 230, 200, a, COR if on else TINTA, 1.0 if on else 0))
        destinos = [(560, 690), (905, 690), (1360, 690), (1015, 690)]
        for i, A in enumerate(POMBOS0):
            t_vai = C["s04.d"] - 0.9 + i * 0.3 if i < 3 else C["s04.e"]
            x, y = voa(t, t_vai, A, destinos[i])
            cor = COR if i == 3 and t >= C["s04.d"] else "#8C8C9C"
            E.foco(c, t, C["s04.b"] + i * 0.15, 0.4, lambda a, x=x, y=y, cor=cor: pombo(c, x, y, 110 if t < t_vai else 90, a, cor))
        if C["s04.d"] <= t < C["s04.e"]:
            E.foco(c, t, C["s04.d"] + 0.2, 0.4, lambda a: E.escreve(c, "sobra 1", 1560, 340, 60, "g", COR, a))
        E.foco(c, t, C["s04.e"] + 0.6, 0.4, lambda a: E.pilula(c, "2 na mesma casinha", 960, 900, 56, "g", fundo=COR, a=a))
    E.saida(c, t, C["s05"] - 0.1, cena)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], [("princípio", "i", 90), ("da", "i", 90), ("casa", "g", 90, COR), ("dos", "i", 90), ("pombos", "g", 90, COR)], W / 2, 220, "center")
    E.frase(c, t, C["s05.b"], [("mais", "i", 76), ("pombos", "g", 72), ("que", "i", 76), ("casinhas", "g", 72)], W / 2, 420, "center")
    E.foco(c, t, C["s05.c"] - 0.2, 0.4, lambda a: M.arrow(c, W / 2, 460, W / 2, 540, COR, a, 6, 20, a))
    E.frase(c, t, C["s05.c"], [("alguma", "i", 76), ("casinha", "i", 76), ("com", "i", 76), ("2", "g", 76, COR), ("ou", "i", 76), ("mais", "g", 72, COR)], W / 2, 640, "center")
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.escreve(c, "não diz qual", 380, 860, 70, "i", TINTA2, a))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: E.escreve(c, "garante que existe", 1000, 860, 70, "g", CERTO, a))


# ---------------- meses ----------------
def b_meses(c, t, C, b):
    destaque = 2 if t >= C["s06.e"] + 0.5 else None
    meses(c, t, C["s06.a"], destaque)
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.escreve(c, "12 casinhas", MX, 160, 52, "i", TINTA2, a))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "pessoas = pombos", 1180, 160, 52, "i", COR, a))

    def pior():
        E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "pior caso", 400, 700, 60, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s06.d"], ps("12 pessoas, cada uma num mês", "i", 60), 620, 715)
    if t < C["s07"]:
        E.saida(c, t, C["s07"] - 0.1, pior)
    for i in range(12):
        gente_mes(c, t, i, 0, C["s06.d"] + i * 0.12)
    if t >= C["s06.e"]:
        gente_mes(c, t, 2, 2, C["s06.e"], COR)
        E.foco(c, t, C["s06.e"], 0.3, lambda a: E.escreve(c, "13ª", caixa_mes(2)[0] + MW - 70, caixa_mes(2)[1] + 50, 36, "g", COR, a))
    if t >= C["s07"]:
        E.frase(c, t, C["s07.a"], [("12", "g", 70), ("não", "g", 70, ERRADO), ("garantem", "i", 70)], XE, 760)
        E.frase(c, t, C["s07.b"], [("13", "g", 70, COR), ("garantem", "g", 70, CERTO)], 1000, 760)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.escreve(c, "13 ÷ 12 = 1, sobra 1", XE, 920, 80, "g", TINTA, a))
        E.foco(c, t, C["s07.d"], 0.5, lambda a: E.escreve(c, "→ algum mês com 2", 1060, 920, 70, "g", COR, a))


def b_tres(c, t, C, b):
    destaque = 7 if t >= C["s08.e"] else None
    meses(c, t, C["s08"], destaque)
    E.frase(c, t, C["s08.a"], [("3", "g", 64, COR), ("no", "i", 64), ("mesmo", "i", 64), ("mês?", "i", 64)], MX, 160)
    for k in range(2):
        for i in range(12):
            gente_mes(c, t, i, k, C["s08.b"] + k * 1.2 + i * 0.07)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "pior caso: 2 em cada mês", 1300, 140, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.escreve(c, "12 × 2 = 24", XE, 800, 100, "g", TINTA, a))
    E.foco(c, t, C["s08.c"] + 0.6, 0.5, lambda a: E.escreve(c, "nenhum trio", XE, 900, 60, "i", TINTA2, a))
    if t >= C["s08.d"]:
        x, y = caixa_mes(7)
        s = ease_back(prog(t, C["s08.d"], 0.4))
        c.drawCircle(x + MW / 2 + 84, y + 112, 20 * s, M.paint(COR))
    E.foco(c, t, C["s08.e"], 0.4, lambda a: E.escreve(c, "24 + 1", 760, 800, 100, "g", COR, a))
    bola_txt(c, t, C["s08.e"] + 0.3, "25", 1240, 770, 110, 110)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.escreve(c, "25 ÷ 12 = 2, sobra 1", 760, 960, 70, "g", TINTA, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.escreve(c, "→ um trio", 1480, 960, 64, "g", COR, a))


def b_dias(c, t, C, b):
    E.frase(c, t, C["s10"], ps("com os dias do ano", "i", 84), XE, 220)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.escreve(c, "366", XE, 480, 220, "g", TINTA, a))
    E.frase(c, t, C["s10.a"] + 0.5, ps("dias possíveis", "i", 70), XE + 470, 470)
    E.foco(c, t, C["s10.a"] + 0.8, 0.4, lambda a: E.pilula(c, "contando 29 de fevereiro", 1460, 400, 46, "b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.escreve(c, "367", XE, 740, 160, "g", CERTO, a))
    E.frase(c, t, C["s10.b"] + 0.4, [("pessoas:", "i", 66), ("garantem", "g", 64, CERTO), ("2", "g", 64, CERTO), ("no", "i", 66), ("mesmo", "i", 66), ("dia", "i", 66)], XE + 380, 730)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.escreve(c, "366", XE, 940, 160, "g", ERRADO, a))
    E.frase(c, t, C["s10.c"] + 0.4, [("pessoas:", "i", 66), ("pode", "i", 66), ("não", "g", 64, ERRADO), ("repetir", "i", 66)], XE + 380, 930)


# ---------------- meias ----------------
def b_meias(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("a", "i", 84), ("gaveta", "g", 80, COR), ("de", "i", 84), ("meias", "i", 84)], XE, 190)
    # gaveta
    gx, gy, gw, gh = XE, 300, 640, 380
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (M.rrect(c, gx, gy, gw, gh, 24, "#2A2A33", a),))
    if t >= C["s11.b"]:
        cores = [PRETA, BR, AZUL] * 3
        for i, cor in enumerate(cores):
            x, y = gx + 90 + (i % 5) * 115, gy + 60 + (i // 5) * 160
            meia_em(c, t, C["s11.b"] + 0.3 + i * 0.06, x, y, 130, cor, True)
    E.frase(c, t, C["s11.c"], [("garantir", "i", 66), ("um", "i", 66), ("par", "g", 64, COR)], 900, 330)
    for i, cor in enumerate((PRETA, BR, AZUL)):
        meia_em(c, t, C["s11.d"] + i * 0.3, 980 + i * 190, 440, 190, cor)
    E.foco(c, t, C["s11.d"] + 0.9, 0.4, lambda a: E.escreve(c, "uma de cada: 3", 900, 760, 56, "i", TINTA2, a))
    meia_em(c, t, C["s11.e"], 1550, 440, 190, AZUL)
    if t >= C["s11.e"]:
        q = ep(t, C["s11.e"] + 0.4, 0.4)
        E.caixa_pontilhada(c, 1320, 410, 400, 260, q, CERTO, prog_=q)
    bola_txt(c, t, C["s11.e"] + 0.6, "4", 1500, 880, 90, 110)
    E.foco(c, t, C["s11.e"] + 0.8, 0.4, lambda a: E.escreve(c, "meias", 1610, 910, 64, "i", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("multiplicar direto", "i", 72, ERRADO), 1050, 200)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.escreve(c, "12 × 3 = 36", XE, 440, 140, "g", ERRADO, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "o MENOR que garante?", 1400, 400, 60, "g", fundo=TINTA, a=a))
    if t >= C["s12.d"]:
        E.risco(c, XE - 10, 460, 1000, 330, t, C["s12.d"] - 0.2, largura=14)
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.escreve(c, "12 × 2 + 1 = 25", XE, 700, 140, "g", CERTO, a))
    E.frase(c, t, C["s12.e"], ps("encha cada mês só até quase transbordar", "i", 66), W / 2, 920, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s13"], [("atalho", "g", 80, BR)], W / 2, 180, "center")
        E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "casinhas × (quero − 1)", W / 2, 400, 100, "g", BR, a, "center"))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "+ 1", W / 2 + 610, 400, 100, "g", CLARO, a, "center"))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.escreve(c, "3 no mesmo mês:", 260, 640, 64, "i", CLARO, a),
                                                E.escreve(c, "12 × 2 + 1 = 25", 900, 640, 84, "g", BR, a)))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: (E.escreve(c, "par de meias:", 260, 820, 64, "i", CLARO, a),
                                                E.escreve(c, "3 × 1 + 1 = 4", 900, 820, 84, "g", BR, a)))
    E.saida(c, t, C["s14"] - 0.1, parte1)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("a multiplicação é o", "i", 70, CLARO) + [("pior", "g", 66, BR), ("caso", "g", 66, BR)], W / 2, 220, "center")
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "a pergunta escolhe a casinha? não vale", W / 2, 380, 60, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s14.c"], [("2", "g", 66, BR), ("pretas:", "i", 70, CLARO)], 260, 560)
    for i in range(10):
        cor = BR if i < 5 else AZUL
        meia_em(c, t, C["s14.d"] + i * 0.1, 220 + i * 120, 640, 150, cor, True)
    for i in range(2):
        meia_em(c, t, C["s14.d"] + 1.3 + i * 0.2, 1480 + i * 140, 640, 150, PRETA, True)
    E.foco(c, t, C["s14.d"] + 1.0, 0.4, lambda a: E.escreve(c, "as outras cores primeiro", 220, 900, 56, "i", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    for j, (cor, nome) in enumerate(((BR, "brancas"), (PRETA, "pretas"), (AZUL, "azuis"))):
        y = 290 + j * 150
        for i in range(5):
            meia_em(c, t, C["s15.a"] + j * 0.5 + i * 0.05, XE + 40 + i * 80, y, 110, cor)
        E.foco(c, t, C["s15.a"] + j * 0.5, 0.4, lambda a, y=y, nome=nome: E.escreve(c, f"5 {nome}", XE + 470, y + 80, 60, "i", TINTA, a))
    E.frase(c, t, C["s15.b"], [("garantir", "i", 72), ("3", "g", 72, COR), ("da", "i", 72), ("mesma", "i", 72), ("cor?", "i", 72)], XE, 820)
    E.frase(c, t, C["s15.c"], [("garantir", "i", 72), ("2", "g", 72, COR), ("pretas?", "g", 72, COR)], XE, 950)
    E.relogio(c, t, C["s16.a"], 1500, 450, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s17"], [("3", "g", 72, COR), ("da", "i", 72), ("mesma", "i", 72), ("cor", "i", 72)], XE, 190)
        E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "casinhas = 3 cores", 900, 190, 60, "i", TINTA2, a))
        for j, cor in enumerate((BR, PRETA, AZUL)):
            for k in range(2):
                meia_em(c, t, C["s17.b"] + j * 0.3 + k * 0.12, 260 + j * 330 + k * 120, 320, 170, cor)
        E.foco(c, t, C["s17.b"] + 1.0, 0.4, lambda a: E.escreve(c, "3 × 2 = 6", 260, 640, 90, "g", TINTA, a))
        meia_em(c, t, C["s17.c"], 1340, 320, 170, PRETA)
        bola_txt(c, t, C["s17.c"] + 0.3, "7", 1600, 420, 100, 120, CERTO)
        E.foco(c, t, C["s17.c"] + 0.5, 0.4, lambda a: E.escreve(c, "3 × 2 + 1 = 7", 900, 640, 90, "g", CERTO, a))
    E.saida(c, t, C["s18"] - 0.1, parte1)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("2", "g", 72, COR), ("pretas:", "i", 72), ("escolhe", "i", 72), ("a", "i", 72), ("cor", "g", 72, COR)], XE, 190)
    for i in range(10):
        meia_em(c, t, C["s18.b"] + i * 0.1, 220 + i * 120, 330, 160, BR if i < 5 else AZUL)
    E.foco(c, t, C["s18.b"] + 1.0, 0.4, lambda a: E.escreve(c, "5 + 5 = 10", 220, 640, 84, "g", TINTA, a))
    for i in range(2):
        meia_em(c, t, C["s18.c"] + i * 0.2, 1480 + i * 140, 330, 160, PRETA)
    E.foco(c, t, C["s18.c"] + 0.4, 0.4, lambda a: E.escreve(c, "+ 2", 1480, 640, 84, "g", TINTA, a))
    bola_txt(c, t, C["s18.d"], "12", 1500, 870, 110, 110, CERTO)
    E.foco(c, t, C["s18.d"] + 0.3, 0.4, lambda a: E.escreve(c, "meias", 1630, 900, 64, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        for i, (k, s) in enumerate((("s19.a", "imagine o pior caso"), ("s19.b", "some um"))):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 480, y - 30, 56, a=a), centro(c, str(i + 1), 480, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 110)], 580, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20.a"], [("Inclusão", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s20.a"] + 0.3, [("e", "i", 120), ("exclusão", "g", 130, COR)], XE, 620)
    E.frase(c, t, C["s20.a"] + 0.8, ps("múltiplos de 2 ou de 3", "i", 70), XE, 770)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pombos=b_pombos, meses=b_meses, tres=b_tres, dias=b_dias, meias=b_meias, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
