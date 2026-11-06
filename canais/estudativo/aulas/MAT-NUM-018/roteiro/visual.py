"""Visual — Estudativo · MAT-NUM-018: expressões com inteiros.
Identidade em _ferramentas/editorial.py. Toda expressão que se resolve passa por E.expressao, que confere se as etapas valem o mesmo.
Peças locais: monta (expressão que se escreve por partes) e bloco_em (caixa em volta de um trecho)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-018_expressoes_com_inteiros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sinais", "resolver", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def pal(s, estilo="i", size=84, cor=TINTA):
    """frase em palavras, para entrar uma a uma"""
    return [(p, estilo, size, cor) for p in s.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def xpos(s, i, size):
    """x do caractere i dentro de s, escrito na grotesca pesada"""
    return E.larg(s[:i], "g", size) + (E.APERTO["g"] * size if i else 0)


def monta(c, t, s, mascara, tempos, cx, y, size, tinta=None):
    """expressão que se escreve por partes, cada uma na sua fala (peça local).
    mascara = uma letra por caractere; tempos = {letra: t0 ou (t0, cor)}"""
    assert len(s) == len(mascara), (s, mascara)
    x = cx - E.larg(s, "g", size) / 2
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and mascara[j] == mascara[i]:
            j += 1
        v = tempos[mascara[i]]
        t0, cor = v if isinstance(v, tuple) else (v, tinta or TINTA)
        E.foco(c, t, t0, 0.45, lambda a, i=i, j=j, cor=cor: E.escreve(c, s[i:j], x + xpos(s, i, size), y, size, "g", cor, a))
        i = j


def bloco_em(c, t, t0, s, trecho, cx, y, size, cor=CLARO):
    """caixa pontilhada em volta de um trecho da expressão; devolve o centro do trecho (peça local)"""
    i = s.find(trecho)
    x = cx - E.larg(s, "g", size) / 2 + xpos(s, i, size)
    w = E.larg(trecho, "g", size)
    q = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x - 18, y - size * 0.92, w + 36, size * 1.2, q, cor, prog_=q)
    return x + w / 2


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
        y, s = 400, 150
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "−3 + 2 × (−4)", XE, y, s, "g", TINTA, a))
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "= 4", 1190, y, s, "g", ERRADO, a))
        E.risco(c, 1310, y + 20, 1460, y - 130, t, kc, largura=16)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 1620, y - 50, 84, False, a))
        E.frase(c, t, kd - 0.3, pal("a resposta é", size=110), XE, 760)
        bola_txt(c, t, kd, "−11", 920, 720, 150, 120)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, pal("até o fim desta aula", size=90), XE, 330)
        E.frase(c, t, lerp(ta, tb, 0.35), [("expressões", "g", 124)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.5), pal("com", size=110) + [("negativos", "g", 120, COR)], XE, 640, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.7), pal("sem se perder nos sinais", size=84), XE, 770, passo=0.1)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1490, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka, kb = C["s03.a"], C["s03.b"]
    E.frase(c, t, C["s03"] + 0.1, [("dois", "g", 92, COR)] + pal("lembretes", size=92), W / 2, 190, "center", passo=0.1)
    x, w = 190, 1540
    for y, k, l1, l2 in ((270, ka, "ordem das operações", "parênteses · vezes e dividido · mais e menos"),
                         (590, kb, "regra de sinais", "sinais iguais: mais · sinais diferentes: menos")):
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 270, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "g", 84, COR)], x + 50, y + 110)
        E.frase(c, t, k + 0.4, [(l2, "i", 72)], x + 50, y + 215)


# ---------------- sinais ----------------
def b_sinais(c, t, C, b):
    def papeis():
        ka, kb, kc, kd, ke = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
        E.frase(c, t, C["s04"] + 0.2, pal("o", size=100) + [("menos", "g", 100, COR)] + pal("tem", size=100) + [("dois", "g", 100, COR), ("papéis", "g", 100, COR)], W / 2, 190, "center", passo=0.1)
        x1, x2 = 540, 1380
        E.frase(c, t, kb, [("operação:", "g", 80, COR)] + pal("tirar", size=84), x1, 360, "center", passo=0.1)
        E.frase(c, t, kc, [("sinal", "g", 80, COR), ("colado", "g", 80, COR)] + pal("no número", size=84), x2, 360, "center", passo=0.1)
        y = 660
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "10 − 3", x1, y, 190, "g", TINTA, a))
        E.foco(c, t, ke, 0.5, lambda a: E.centro(c, "−3", x2, y, 190, "g", TINTA, a))
        if t >= kd:
            s = "10 − 3"
            xm = x1 - E.larg(s, "g", 190) / 2 + xpos(s, 3, 190) + E.larg("−", "g", 190) / 2
            q = ep(t, kd + 0.2, 0.4)
            M.arrow(c, xm, 840, xm, 700, COR, q, 7, 22, q)
            E.foco(c, t, kd + 0.2, 0.4, lambda a: E.centro(c, "operação", xm, 900, 70, "i", COR, a))
        if t >= ke:
            xm = x2 - E.larg("−3", "g", 190) / 2 + E.larg("−", "g", 190) / 2
            q = ep(t, ke + 0.2, 0.4)
            M.arrow(c, xm, 840, xm, 700, COR, q, 7, 22, q)
            E.foco(c, t, ke + 0.2, 0.4, lambda a: E.centro(c, "sinal colado", xm + 40, 900, 70, "i", COR, a))
    E.saida(c, t, C["s05"] - 0.1, papeis)

    if t >= C["s05"]:
        ka, kb = C["s05.a"], C["s05.b"]
        s, y, size = "2 × (−4)", 480, 200
        E.frase(c, t, C["s05"] + 0.1, pal("e o parêntese em volta do", size=88) + [("−4?", "g", 92, COR)], W / 2, 200, "center", passo=0.1)
        monta(c, t, s, "aaaabccb", dict(a=ka, b=(ka, COR), c=ka), W / 2, y, size)
        E.frase(c, t, lerp(ka, kb, 0.45), pal("ali dentro não tem conta nenhuma", size=84), W / 2, 700, "center", passo=0.1)
        E.frase(c, t, kb, pal("só", size=88) + [("separa", "g", 88, COR)] + pal("o vezes do menos", size=88), W / 2, 840, "center", passo=0.1)
        E.frase(c, t, lerp(kb, C["s05.end"], 0.5), pal("para os sinais não encostarem", size=80), W / 2, 960, "center", passo=0.1)


# ---------------- resolver ----------------
def b_resolver(c, t, C, b):
    def r1():
        ka, kb, kc, kd, ke = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
        E.frase(c, t, ka, pal("o", size=92) + [("vezes", "g", 92, COR)] + pal("vem antes do", size=92) + [("mais", "g", 92, COR)], W / 2, 180, "center", passo=0.1)
        E.expressao(c, t, [("−3 + 2 × (−4)", "2 × (−4)", kb), ("−3 + (−8)", "−3 + (−8)", kd), ("−11", "−11", ke)], [kc, ke], 700, 370, 130, empilha=180, t0=C["s06"])
        E.frase(c, t, kb + 0.5, pal("sinais diferentes", size=72), 1270, 350, passo=0.08)
        tu = lerp(kd, ke, 0.5)
        E.foco(c, t, tu, 0.5, lambda a: E.divida(c, 1340, 610, 250, 170, "R$ 3", a))
        E.foco(c, t, tu + 0.5, 0.5, lambda a: E.divida(c, 1610, 610, 250, 170, "R$ 8", a))
    E.saida(c, t, C["s07"] - 0.1, r1)

    def r2():
        ka, kb, kc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        fim = C["s07.end"]
        E.frase(c, t, C["s07"] + 0.1, pal("em", size=88) + [("dinheiro", "g", 88, COR)], W / 2, 150, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.divida(c, 400, 410, 320, 190, "R$ 3", a))
        E.frase(c, t, kb, pal("leva", size=76) + [("fiado", "g", 76, COR)], 1090, 280, "center", passo=0.1)
        E.foco(c, t, kb + 0.3, 0.5, lambda a: E.divida(c, 950, 420, 270, 170, "R$ 4", a))
        E.foco(c, t, kb + 0.6, 0.5, lambda a: E.divida(c, 1240, 420, 270, 170, "R$ 4", a))
        E.frase(c, t, kc, [("1º", "g", 76, COR)] + pal("quanto aumentou:", size=76) + [("2 × (−4) = −8", "g", 84)], W / 2, 620, "center", passo=0.1)
        E.frase(c, t, kd, [("2º", "g", 76, COR)] + pal("junta com o que já devia:", size=76) + [("−3 + (−8)", "g", 84)], W / 2, 740, "center", passo=0.1)
        E.frase(c, t, lerp(kd, fim, 0.45), pal("na ordem em que leu,", size=76) + pal("a dívida de 3", "g", 72, ERRADO), W / 2, 860, "center", passo=0.1)
        E.frase(c, t, lerp(kd, fim, 0.68), pal("entraria no vezes sem ter nada a ver com ele", size=72), W / 2, 950, "center", passo=0.08)
    if C["s07"] - 0.1 <= t:
        E.saida(c, t, C["s08"] - 0.1, r2)

    def r3():
        ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
        E.frase(c, t, C["s08"] + 0.1, pal("parêntese", "g", 84, COR) + pal("com conta dentro vem primeiro", size=84), W / 2, 180, "center", passo=0.1)
        E.expressao(c, t, [("(−2 + 7) × (−3)", "(−2 + 7)", lerp(ka, kb, 0.65)), ("5 × (−3)", "5 × (−3)", kc), ("−15", "−15", kd)], [kb, kd], W / 2 - 200, 380, 130, empilha=190, t0=ka)
        E.frase(c, t, kb, pal("deve 2, paga 7:", size=68), 1290, 370, passo=0.08)
        E.frase(c, t, kb + 0.5, pal("sobra", size=68) + [("5", "g", 72, COR)], 1290, 450, passo=0.08)
        E.frase(c, t, lerp(kc, kd, 0.5), pal("sinais diferentes", size=68), 1290, 560, passo=0.08)
    if C["s08"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, r3)

    if t >= C["s09"]:
        ka, kb, kc, kd = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
        fim = C["s09.end"]
        tf = lerp(kd, fim, 0.2)
        E.frase(c, t, ka, pal("vezes e dividido:", size=84) + [("da", "g", 80, COR), ("esquerda", "g", 80, COR), ("para", "g", 80, COR), ("a", "g", 80, COR), ("direita", "g", 80, COR)], W / 2, 180, "center", passo=0.1)
        E.expressao(c, t, [("−12 ÷ 2 × (−3)", "−12 ÷ 2", kc), ("−6 × (−3)", "−6 × (−3)", kd), ("+18", "+18", tf)], [lerp(kc, kd, 0.75), tf], W / 2, 350, 124, empilha=155, t0=kb)
        E.frase(c, t, lerp(kd, fim, 0.38), pal("um passo por linha, e copie o resto igual,", size=76), W / 2, 800, "center", passo=0.08)
        E.frase(c, t, lerp(kd, fim, 0.66), pal("muito erro é só", size=80) + [("sinal", "g", 80, ERRADO), ("que", "g", 80, ERRADO), ("sumiu", "g", 80, ERRADO)] + pal("na cópia", size=80), W / 2, 920, "center", passo=0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s = "10 − (3 − 8)"

    def engano():
        ka, kb, kc, kd = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        E.frase(c, t, ka, [("cuidado", "g", 96, ERRADO)] + pal("com o menos antes de um parêntese", size=88), W / 2, 200, "center", passo=0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, s, W / 2, 470, 170, "g", TINTA, a))
        E.frase(c, t, kc - 0.4, pal("ignora o parêntese:", size=84), 560, 740, "center", passo=0.1)
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "10 − 3 − 8", 1220, 745, 130, "g", TINTA, a))
        E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "= −1", 1090, 910, 130, "g", ERRADO, a))
        tr = lerp(kd, C["s10.end"], 0.45)
        E.foco(c, t, tr, 0.5, lambda a: E.selo(c, 1520, 860, 70, False, a))
    E.saida(c, t, C["s11"] - 0.1, engano)
    if t >= C["s11"]:
        ka, kb, kc = C["s11.a"], C["s11.b"], C["s11.c"]
        fim = C["s11.end"]
        tp = [lerp(ka, kb, 0.75), lerp(kb, kc, 0.8), lerp(kc, fim, 0.7)]
        E.frase(c, t, C["s11"] + 0.1, pal("o", size=88) + [("parêntese", "g", 88, COR)] + pal("vem primeiro", size=88), W / 2, 180, "center", passo=0.1)
        E.expressao(c, t, [(s, "(3 − 8)", ka), ("10 − (−5)", "− (−5)", kb), ("10 + 5", "10 + 5", kc), ("15", "15", tp[2])], tp, 640, 340, 124, empilha=165, t0=C["s11"])
        E.frase(c, t, lerp(kb, kc, 0.3), [("tirar", "g", 76, COR), ("uma", "g", 76, COR), ("dívida", "g", 76, COR)], 1190, 400, passo=0.1)
        E.frase(c, t, lerp(kb, kc, 0.5), pal("é como", size=76) + [("ganhar", "g", 76, CERTO)], 1190, 500, passo=0.1)
        E.foco(c, t, lerp(kb, kc, 0.2), 0.5, lambda a: E.divida(c, 1420, 700, 320, 190, "R$ 5", a, ease_io(prog(t, lerp(kb, kc, 0.6), 0.6))))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s = "−12 ÷ 3 − 2 × (−5)"

    def explica():
        ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
        fim = C["s12.end"]
        E.frase(c, t, C["s12"] + 0.1, pal("agora, o atalho:", size=84, cor=CLARO), W / 2, 200, "center", passo=0.1)
        E.frase(c, t, ka, pal("os", size=150, cor=BR) + [("blocos,", "g", 150, BR)] + pal("com um cuidado", size=110, cor=CLARO), W / 2, 380, "center", passo=0.12)
        E.frase(c, t, kb, pal("separe nos", size=80, cor=CLARO) + [("+", "g", 84, BR), ("e", "i", 80, CLARO), ("−", "g", 84, BR)] + pal("que ligam uma conta na outra", size=80, cor=CLARO), W / 2, 560, "center", passo=0.09)
        E.frase(c, t, kc, [("sinal", "g", 92, BR), ("colado", "g", 92, BR)] + pal("não corta", size=92, cor=CLARO), W / 2, 720, "center", passo=0.1)
        E.frase(c, t, lerp(kc, fim, 0.4), pal("o menos do começo, ou depois de", size=72, cor=CLARO) + [("×", "g", 76, BR), ("ou", "i", 72, CLARO), ("÷,", "g", 76, BR)], W / 2, 850, "center", passo=0.08)
        E.frase(c, t, lerp(kc, fim, 0.75), pal("é do próprio número", size=72, cor=CLARO), W / 2, 950, "center", passo=0.08)
    E.saida(c, t, C["s13"] - 0.1, explica)

    def exemplo():
        ka, kb, kc, kd, ke = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
        cx, y, size = W / 2, 290, 124
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, s, cx, y, size, "g", BR, a))
        y2 = 540
        fins = {kb: lerp(kb, kc, 0.75), kc: lerp(kc, kd, 0.75)}
        xs = []
        for tr, k, res in (("−12 ÷ 3", kb, "−4"), ("2 × (−5)", kc, "−10")):
            if t >= k:
                xr = bloco_em(c, t, k, s, tr, cx, y, size)
                xs.append(xr)
                q = ep(t, k, 0.4)
                M.arrow(c, xr, y + 54, xr, y2 - 120, CLARO, q, 4, 14, q)
                E.foco(c, t, fins[k], 0.45, lambda a, xr=xr, res=res: E.centro(c, res, xr, y2, 120, "g", CLARO, a))
        if len(xs) == 2:
            E.foco(c, t, kd, 0.45, lambda a: E.centro(c, "−", (xs[0] + xs[1]) / 2, y2, 110, "g", BR, a))
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "−4 − (−10)", 720, 800, 120, "g", BR, a))
        E.frase(c, t, lerp(kd, ke, 0.4), pal("tirar uma dívida de 10 é ganhar 10", size=72, cor=CLARO), W / 2, 950, "center", passo=0.08)
        bola_txt(c, t, ke, "+6", 1320, 760, 110, 110)
        E.frase(c, t, lerp(ka, kb, 0.75), pal("corte no menos do meio", size=72, cor=CLARO), W / 2, 130, "center", passo=0.08)
    if C["s13"] - 0.1 <= t:
        E.saida(c, t, C["s14"] - 0.1, exemplo)

    if t >= C["s14"]:
        ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
        fim = C["s14.end"]
        E.frase(c, t, C["s14"] + 0.1, pal("funciona porque", size=84, cor=CLARO), W / 2, 170, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.selo(c, 290, 320, 72, True, a))
        E.frase(c, t, C["s14"] + 0.4, [("×", "g", 76, BR), ("e", "i", 76, CLARO), ("÷", "g", 76, BR)] + pal("vêm antes,", size=76, cor=CLARO), 400, 300, passo=0.1)
        E.frase(c, t, ka, [("grudados", "g", 76, BR)] + pal("no mesmo bloco", size=76, cor=CLARO), 400, 390, passo=0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 290, 560, 72, False, a))
        E.frase(c, t, kb, pal("não serve", size=76, cor=CLARO) + [("dentro", "g", 76, BR)] + pal("de parênteses", size=76, cor=CLARO), 400, 540, passo=0.1)
        E.frase(c, t, lerp(kb, kc, 0.3), pal("lá dentro é um bloco só, e vem primeiro", size=64, cor=CLARO), 400, 625, passo=0.08)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 290, 800, 72, False, a))
        E.frase(c, t, kc, pal("com", size=76, cor=CLARO) + [("uma", "g", 76, BR), ("operação", "g", 76, BR), ("só,", "g", 76, BR)] + pal("não compensa", size=76, cor=CLARO), 400, 780, passo=0.1)
        E.frase(c, t, lerp(kc, fim, 0.6), pal("faça direto", size=64, cor=CLARO), 400, 865, passo=0.08)


# ---------------- questão ----------------
QS = "−5 + 3 × (−2) − (4 − 9)"


def b_questao(c, t, C, b):
    ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"], pal("hora de testar", size=72, cor=COR), XE, 200)
    E.frase(c, t, ka - 0.3, pal("resolva", size=100), XE, 420)
    monta(c, t, QS, "a" * 3 + "b" * 11 + "c" * 9, dict(a=ka, b=kb, c=kc), 680, 600, 92)
    E.relogio(c, t, C["s16.a"], 1520, 400, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def blocos():
        ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
        cx, y, size = W / 2, 320, 112
        E.frase(c, t, C["s17"] + 0.1, pal("em", size=84) + [("blocos", "g", 84, COR)], W / 2, 170, "center", passo=0.1)
        E.foco(c, t, C["s17"] + 0.1, 0.5, lambda a: E.centro(c, QS, cx, y, size, "g", TINTA, a))
        y2 = 620
        for tr, k, f, res, n in (("−5", ka, None, "−5", 1), ("3 × (−2)", kb, 0.75, "−6", 2), ("(4 − 9)", kc, 0.65, "−5", 3)):
            if t < k:
                continue
            xr = bloco_em(c, t, k, QS, tr, cx, y, size, COR)
            q = ep(t, k, 0.4)
            M.arrow(c, xr, y + 54, xr, y2 - 120, COR, q, 4, 14, q)
            ti = k if f is None else lerp(k, kc if n == 2 else C["s17.end"], f)
            E.foco(c, t, ti, 0.45, lambda a, xr=xr, res=res, n=n: (E.centro(c, res, xr, y2, 120, "g", COR, a), E.centro(c, f"bloco {n}", xr, y2 + 90, 62, "i", TINTA, a)))
    E.saida(c, t, C["s18"] - 0.1, blocos)
    if t >= C["s18"]:
        ka, kb, kc, kd = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
        tp = [lerp(ka, kb, 0.3), kc, kd]
        E.expressao(c, t, [("−5 + (−6) − (−5)", "−5 + (−6)", ka), ("−11 − (−5)", "− (−5)", lerp(ka, kb, 0.55)), ("−11 + 5", "−11 + 5", kc), ("−6", "−6", kd)],
                    tp, 620, 290, 116, empilha=165, t0=C["s18"])
        E.frase(c, t, lerp(ka, kb, 0.6), pal("subtrair uma", size=72) + [("dívida", "g", 72, ERRADO)] + pal("de 5", size=72), 1440, 300, "center", passo=0.08)
        E.foco(c, t, lerp(ka, kb, 0.7), 0.5, lambda a: E.divida(c, 1440, 520, 320, 190, "R$ 5", a, ease_io(prog(t, kb, 0.6))))
        E.frase(c, t, kb, pal("tirar essa dívida é", size=72) + [("ganhar", "g", 72, CERTO), ("5", "g", 72, CERTO)], 1440, 760, "center", passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s19.a", "a ordem é a de sempre"), ("s19.b", "o sinal se decide a cada passo"), ("s19.c", "menos antes de parêntese: atenção"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 280, y - 30, 56, a=a), E.centro(c, str(i + 1), 280, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 370, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"] - 0.4, pal("próxima aula: você"), XE, 270)
    E.frase(c, t, C["s20.a"], [("pratica", "g", 130, COR)], XE, 420)
    E.frase(c, t, C["s20.b"], pal("monta e resolve", size=96) + [("expressões", "g", 100)] + pal("com negativos", size=96), XE, 560, passo=0.1)
    E.frase(c, t, C["s20.c"], pal("um saldo que", size=96) + [("entra", "g", 100, ERRADO), ("no", "g", 100, ERRADO), ("vermelho", "g", 100, ERRADO)], XE, 690, passo=0.1)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 800, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(990, 825, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], 700, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sinais=b_sinais, resolver=b_resolver, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
