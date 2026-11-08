"""Visual — Estudativo · MAT-EST-012: média, mediana e moda numa tabela.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): a tabela (quadro()) entra coluna a coluna, cada
célula no marcador em que a fala diz o número, a coluna da vez na cor da matéria e as prontas em preto; lista de dados =
fichas; conta da vez à direita, resposta na esfera; atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- A TABELA FICA À ESQUERDA e ganha uma coluna por medida: "nota × alunos" (média), "acumulada" (mediana), "(nota − 7) × alunos"
  (atalho). A linha da vez ganha a caixa pontilhada (linha_viva()).
- A LISTA ESCONDIDA NA TABELA = RÉGUA DE 20 CASAS (casas()) pintadas pela nota de cada aluno, em ordem; as casas do meio (10ª e
  11ª) com anel. Mostra que a tabela já é a lista ordenada.
- quadro(escuro=True) desenha a mesma tabela no palco.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-012_media_mediana_e_moda_numa_tabela.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("media", "mediana", "moda", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
NOTAS = [(4, 2), (6, 4), (7, 5), (8, 6), (9, 3)]
FILHOS = [(0, 2), (1, 7), (2, 5), (3, 4), (4, 2)]
LISTA = [n for n, k in NOTAS for _ in range(k)]
assert len(LISTA) == 20 and sum(n * k for n, k in NOTAS) == 142 and 142 / 20 == 7.1
assert LISTA[9] == LISTA[10] == 7 and LISTA[6] == 7 and LISTA[5] == 6 and (20 + 1) / 2 == 10.5
assert sum((n - 7) * k for n, k in NOTAS if n < 7) == -10 and sum((n - 7) * k for n, k in NOTAS if n > 7) == 12 and 7 + 2 / 20 == 7.1
LF = [n for n, k in FILHOS for _ in range(k)]
assert len(LF) == 20 and sum(LF) == 37 and 37 / 20 == 1.85 and LF[9] == LF[10] == 2 and max(FILHOS, key=lambda r: r[1])[0] == 1


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ², ³ ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None, escuro=False):
    """tabela de dados que entra coluna a coluna. colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...];
    total = [(texto, t0[, cor]), ...] depois de um fio grosso; escuro=True para o palco. Devolve o y da linha de base de cada linha"""
    h_lin = h_lin or size * 1.55
    tinta, tinta2 = (BR, CLARO) if escuro else (TINTA, TINTA2)
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, tinta, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.7, "i", tinta2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: centro(c, s, cx, yy, size, "g", cc[0] if cc else tinta, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, tinta, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else tinta, a))
    return bases


def ficha(c, s, cx, cy, size, a=1.0, cor=None, borda=None):
    """um dado da lista: pílula branca com borda fina (cor = fundo aceso)"""
    if a <= 0:
        return
    w = E.larg(s, "b", size) + size * 1.1
    h = size * 1.55
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2)
    c.drawRRect(rr, M.paint(cor or BR, a))
    c.drawRRect(rr, M.paint(borda or (cor or FIO), a, stroke=3))
    centro(c, s, cx, cy + size * 0.36, size, "b", (BR if cor and M.lum(cor) < 0.5 else TINTA), a)


# ---------------- peças desta aula ----------------
TX, TY, SZ, HL = 130, 330, 58, 92     # a tabela: canto, tamanho do número, altura da linha
X = 1450                               # o centro da conta da vez


def tab(c, t, tb, extra=(), tt=None, tot_extra=(), linhas=NOTAS, nomes=("nota", "alunos"), escuro=False, vez=None, x=TX):
    """a tabela-base (nota, alunos) já pronta em tb, mais as colunas extra = [(título, largura, t_tit, [(texto, t[, cor])...])].
    tt = instante do total 20; tot_extra = células do total nas colunas extra; vez = índice da linha da vez (número na cor)"""
    cols = [(nomes[0], 170, tb), (nomes[1], 210, tb)] + [(tit, w, ti) for tit, w, ti, _ in extra]
    lin = []
    for j, (n, k) in enumerate(linhas):
        cor = (CLARO if escuro else COR) if vez == j else (BR if escuro else TINTA)
        lin.append([(str(n), tb + 0.05 * j, cor), (str(k), tb + 0.05 * j + 0.03, cor)] + [cel[j] for _, _, _, cel in extra])
    total = None
    if tt is not None:
        total = [("total", tt), ("20", tt)] + list(tot_extra)
    return quadro(c, t, x, TY, cols, lin, total, size=SZ, h_lin=HL, escuro=escuro)


def linha_viva(c, t, t0, t1, j, w, x=TX, cor=None):
    """caixa pontilhada na linha j da tabela, de t0 até t1"""
    p = ep(t, t0, 0.5) * (1 - ep(t, t1, 0.4)) if t1 is not None else ep(t, t0, 0.5)
    if p > 0:
        y = TY + 20 + HL * j + 6
        E.caixa_pontilhada(c, x - 20, y, w + 40, HL - 8, p, cor, prog_=ep(t, t0, 0.5))


def casas(c, t, t0, lista, cx, y, lado=66, gap=10, cores_t=None, aneis=(), t_anel=None, numeros=True, escuro=False):
    """a lista ordenada em casas numeradas (1 a n). cores_t = (instante, {valor: cor}) pinta cada casa pela nota;
    aneis = casas (1..n) com anel a partir de t_anel. Devolve x(k)"""
    n = len(lista)
    x0 = cx - (n * lado + (n - 1) * gap) / 2
    xk = lambda k: x0 + (k - 1) * (lado + gap) + lado / 2
    tinta = BR if escuro else TINTA
    for k in range(1, n + 1):
        def um(a, k=k):
            v = lista[k - 1]
            fundo = None
            if cores_t:
                for ti, mapa in cores_t:
                    if t >= ti and v in mapa:
                        fundo = mapa[v]
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xk(k) - lado / 2, y - lado / 2, lado, lado), 12, 12)
            c.drawRRect(r, M.paint(fundo or (PAPEL if not escuro else "#07070F"), a))
            c.drawRRect(r, M.paint(tinta, a * 0.6, stroke=3))
            if numeros:
                centro(c, str(k), xk(k), y + lado * 0.2, lado * 0.46, "g", BR if fundo and M.lum(fundo) < 0.5 else tinta, a)
            if k in aneis and t_anel is not None and t >= t_anel:
                q = ease_back(prog(t, t_anel, 0.4))
                rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xk(k) - lado / 2 - 8 * q, y - lado / 2 - 8 * q, lado + 16 * q, lado + 16 * q), 16, 16)
                c.drawRRect(rr, M.paint(E.COR, a, stroke=6))
        E.foco(c, t, t0 + 0.03 * k, 0.4, um, sobe=8)
    return xk


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, a1, ps("20 alunos, 5 notas,", "i", 64) + [("uma tabela", "g", 70, COR)], W / 2, 190, "center", 0.1)
        tab(c, t, a1 + 0.4, tt=a1 + 1.2)
        for i, v in enumerate(LISTA):
            col, lin = i % 5, i // 5
            E.foco(c, t, b1 + 0.12 * i, 0.3, lambda a, v=v, col=col, lin=lin: ficha(c, str(v), 1180 + col * 120, 370 + lin * 110, 46, a), sobe=10)
        if t >= c1:
            E.risco(c, 1110, 340, 1760, 760, t, c1, largura=14)
            E.risco(c, 1110, 760, 1760, 340, t, c1 + 0.2, largura=14)
        E.foco(c, t, c1 + 0.3, 0.4, lambda a: E.pilula(c, "não precisa", 1420, 850, 56, "g", fundo=ERRADO, a=a))
        tq = lerp(c1, C["s01.end"], 0.45)
        E.frase(c, t, tq, ps("a tabela já entrega", "i", 52) + [("as 3 medidas", "g", 56, COR)], 560, 960, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 280, passo=0.14)
        E.frase(c, t, ta + 1.4, [("média, mediana", "g", 96, COR)], XE, 420, passo=0.14)
        E.frase(c, t, ta + 2.2, ps("e", "i", 88) + [("moda", "g", 96, COR)], XE, 540, passo=0.14)
        E.frase(c, t, ta + 3.2, ps("direto da tabela", "i", 88), XE, 670, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "a média ponderada:", "cada valor tem um peso"), ("s03.c", "moda e mediana:", "posição do meio = f{n + 1}{2}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 90, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.6, l2, x + 44, y + 180, 56, "g", COR)
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- média ----------------
def b_media(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5, d5, e5, f5 = (C[f"s05.{k}"] for k in "abcdef")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    E.frase(c, t, C["s04"] + 0.1, [("média", "g", 80, COR)], XE, 180)
    ts = [b5, c5, d5, e5, f5]
    prods = [n * k for n, k in NOTAS]
    vez = lambda j: COR if ts[j] <= t < (ts[j + 1] if j < 4 else a6) else TINTA
    cel = [(str(p), ts[j], vez(j)) for j, p in enumerate(prods)]
    tab(c, t, C["s04"], [("nota × alunos", 290, a5, cel)], tt=C["s04"], tot_extra=[("142", a6, COR if t < C["s07"] else TINTA)])
    linha_viva(c, t, a4, C["s05"] - 0.2, 2, 380)

    def um():
        E.frase(c, t, a4, ps("5 alunos tiraram", "i", 58) + [("7", "g", 64, COR)], X, 330, "center", 0.1)
        for i in range(5):
            E.foco(c, t, a4 + 1.0 + 0.15 * i, 0.4, lambda a, i=i: ficha(c, "7", X - 280 + 140 * i, 460, 56, a, E.COR), sobe=20)
        E.frase(c, t, a4 + 2.0, ps("o 7 aparece 5 vezes na lista", "i", 46, TINTA2), X, 580, "center", 0.06)
        E.frase(c, t, b4, ps("nº de alunos =", "i", 60) + [("peso", "g", 66, COR)], X, 720, "center", 0.1)
        E.foco(c, t, b4 + 1.4, 0.4, lambda a: E.pilula(c, "média ponderada", X, 850, 56, "g", a=a, cor=E.SOBRE))
    fase(c, t, C["s04"], C["s05"] - 0.1, um)

    def dois():
        E.frase(c, t, a5, ps("cada nota × o nº de alunos", "i", 54), X, 300, "center", 0.08)
        for j, ((n, k), ti) in enumerate(zip(NOTAS, ts)):
            fcen(c, t, ti, f"{n} × {k} = {n * k}", X, 420 + 110 * j, 66, vez(j))
    fase(c, t, C["s05"], C["s06"] - 0.1, dois)
    if t < C["s06"] - 0.1:
        return
    fcen(c, t, a6, "8 + 24 + 35 + 48 + 27 = 142", X, 320, 54)
    E.frase(c, t, b6, ps("÷", "g", 60) + [("20 alunos", "g", 60, COR)] + ps("e não ÷ 5 linhas", "i", 56, ERRADO), X, 440, "center", 0.1)
    fcen(c, t, c6, "142 ÷ 20 = 7,1", X - 170, 600, 80)
    bola_txt(c, t, c6 + 0.6, "7,1", X + 270, 575, 90, 70)
    vx = E.reta(c, t, d6, 1040, 1820, 820, 4, 9, [4, 5, 6, 7, 8, 9], size=40)
    E.foco(c, t, d6 + 0.5, 0.4, lambda a: (c.drawCircle(vx(7.1), 820, 17, M.paint(E.COR, a)), centro(c, "7,1", vx(7.1), 770, 46, "g", COR, a)))
    E.frase(c, t, d6 + 0.9, ps("entre a menor e a maior nota", "i", 46, TINTA2), X, 990, "center", 0.06)
    E.foco(c, t, d6 + 1.4, 0.4, lambda a: E.selo(c, 1070, 975, 32, True, a))


# ---------------- mediana ----------------
def b_mediana(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    E.frase(c, t, C["s07"] + 0.1, [("mediana", "g", 80, COR)], XE, 180)
    acum = [("2", a8 + 0.4, TINTA2), ("6", b8, COR if t < c8 else TINTA), ("11", c8, COR), ("", 0), ("", 0)]
    extra = [("acumulada", 250, a8, acum)] if t >= a8 - 0.1 else []
    tab(c, t, C["s07"], extra, tt=C["s07"])
    linha_viva(c, t, d8, None, 2, 630 if extra else 380)
    if t >= c7:   # a tabela já vem em ordem
        p = ep(t, c7, 0.7)
        M.arrow(c, TX - 50, TY + 40, TX - 50, lerp(TY + 40, TY + 20 + 5 * HL, p), E.COR, p, 6, 18, p)
    xk = casas(c, t, b7, LISTA, W / 2, 970, cores_t=[(d8, {7: E.COR})], aneis=(10, 11), t_anel=b7 + 0.8)

    def um():
        fcen(c, t, a7, "f{20 + 1}{2} = 10,5", X, 380, 90)
        E.frase(c, t, b7, ps("a média do", "i", 58) + [("10º e do 11º", "g", 62, COR)], X, 560, "center", 0.1)
        E.frase(c, t, c7, ps("a tabela", "i", 56) + [("já vem em ordem", "g", 60, COR)], X, 700, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, a8, ps("quem diz onde estão:", "i", 52) + [("a acumulada", "g", 56, COR)], X + 40, 330, "center", 0.08)
    E.frase(c, t, b8, ps("até a nota 6:", "i", 54) + [("6 alunos", "g", 58)], X + 40, 440, "center", 0.08)
    E.frase(c, t, c8, ps("até a nota 7:", "i", 54) + [("11 alunos", "g", 58)], X + 40, 530, "center", 0.08)
    E.frase(c, t, d8, ps("do 7º ao 11º:", "i", 54) + [("nota 7", "g", 58, COR)], X + 40, 640, "center", 0.08)
    bola_txt(c, t, e8, "7", X + 340, 760, 80, 80)
    E.foco(c, t, e8 + 0.2, 0.4, lambda a: centro(c, "mediana", X + 120, 785, 52, "i", COR, a))
    E.frase(c, t, f8, ps("meio em linhas diferentes? média das duas notas", "i", 40, TINTA2), X - 20, 870, "center", 0.05)
    if t >= d8:
        q = ep(t, d8, 0.5)
        E.chave(c, xk(7) - 33, xk(11) + 33, 920, E.COR, q, -24, 5)


# ---------------- moda e o erro ----------------
def b_moda(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, C["s09"] + 0.1, [("moda", "g", 80, COR)], XE, 180)
    tab(c, t, C["s09"], tt=C["s09"], vez=3 if t >= b9 else None)
    linha_viva(c, t, b9, None, 3, 380)
    if t >= d9:
        p = ep(t, d9, 0.6)
        y = TY + 20 + HL * 4 - HL * 0.3 - SZ * 0.36
        M.arrow(c, TX + 240, y, TX + 125, y, E.COR, p, 6, 18, p)

    def um():
        E.frase(c, t, a9, ps("a nota que", "i", 58) + [("mais alunos tiraram", "g", 62, COR)], X, 330, "center", 0.1)
        E.frase(c, t, b9, ps("maior frequência:", "i", 56) + [("6 alunos", "g", 60, COR)], X, 460, "center", 0.1)
        bola_txt(c, t, c9, "8", X, 660, 110, 110)
        E.foco(c, t, c9 + 0.2, 0.4, lambda a: centro(c, "moda", X - 220, 680, 60, "i", COR, a))
        E.frase(c, t, d9, ps("o maior nº de alunos →", "i", 46, TINTA2) + [("a nota ao lado", "g", 50)], X, 880, "center", 0.06)
    fase(c, t, C["s09"], C["s10"] - 0.1, um)
    if t < C["s10"] - 0.1:
        return
    E.frase(c, t, C["s10"] + 0.1, [("erro comum", "g", 64, ERRADO)], X, 300, "center")
    E.foco(c, t, a0, 0.4, lambda a: (ficha(c, "moda = 6", X - 60, 450, 64, a, ERRADO), E.selo(c, X + 230, 450, 40, False, a)))
    E.foco(c, t, b0, 0.4, lambda a: (ficha(c, "moda = 8", X - 60, 620, 64, a, CERTO), E.selo(c, X + 230, 620, 40, True, a)))
    E.frase(c, t, b0 + 0.4, ps("um valor dos dados:", "i", 50) + [("a nota", "g", 54, CERTO)], X, 740, "center", 0.08)
    E.frase(c, t, c0, ps("6 =", "i", 50, ERRADO) + ps("quantas vezes ela aparece", "i", 50), X, 850, "center", 0.08)
    for k, (ti, cor, x0, w) in enumerate(((b0, CERTO, TX - 10, 190), (a0, ERRADO, TX + 170, 210))):
        p = ep(t, ti, 0.5)
        if p > 0:
            E.caixa_pontilhada(c, x0, TY - 60, w, HL * 6 + 70, p, cor, prog_=p)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s11"] + 0.1, ps("o atalho da média:", "i", 64, CLARO), XE, 180, passo=0.1)
    desv = [(n - 7) * k for n, k in NOTAS]
    txt = [f"−3 × 2 = −6", "−1 × 4 = −4", "0", "+1 × 6 = +6", "+2 × 3 = +6"]
    cel = [(s, b1 + 0.35 * j, CLARO if d < 0 else BR) for j, (s, d) in enumerate(zip(txt, desv))]
    tab(c, t, C["s11"], [("(nota − 7) × alunos", 430, b1, cel)], tt=C["s11"], tot_extra=[("+2", d1, CLARO)], escuro=True, vez=2 if t >= a1 else None)
    X2 = 1500

    def um():
        E.frase(c, t, a1, ps("base: uma nota do meio,", "i", 52, CLARO) + [("7", "g", 60, BR)], X2, 330, "center", 0.08)
        E.frase(c, t, b1, ps("quanto passa ou falta", "i", 52, CLARO), X2, 450, "center", 0.08)
        E.frase(c, t, b1 + 0.8, ps("× o nº de alunos", "i", 52, CLARO), X2, 520, "center", 0.08)
        fcen(c, t, c1, "abaixo: −6 − 4 = −10", X2, 650, 60, CLARO)
        fcen(c, t, lerp(c1, d1, 0.5), "acima: +6 + 6 = +12", X2, 760, 60, BR)
        fcen(c, t, d1, "−10 + 12 = 2", X2, 900, 76, BR)
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    fcen(c, t, a2, "2 ÷ 20 = 0,1", X2, 340, 76, BR)
    fcen(c, t, b2, "7 + 0,1 = 7,1", X2, 480, 90, BR)
    E.frase(c, t, c2, ps("tirou 7 de todas: tirou 7 da média", "i", 44, CLARO), X2, 610, "center", 0.06)
    E.frase(c, t, c2 + 1.6, ps("no fim,", "i", 48, CLARO) + [("devolve o 7", "g", 52, BR)], X2, 690, "center", 0.06)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "valores pequenos? conta direta", X2, 850, 42, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a3, b3 = C["s13.a"], C["s13.b"]
    E.frase(c, t, C["s13"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    tab(c, t, a3, tt=a3 + 0.5, linhas=FILHOS, nomes=("filhos", "famílias"))
    E.frase(c, t, a3, ps("20 famílias de uma rua", "i", 54), 1000, 360, passo=0.08)
    E.frase(c, t, b3, ps("calcule", "i", 60) + [("média,", "g", 64, COR)], 1000, 480, passo=0.1)
    E.frase(c, t, b3 + 0.6, [("mediana e moda", "g", 64, COR)], 1000, 570, passo=0.1)
    E.frase(c, t, b3 + 1.2, ps("do número de filhos", "i", 54), 1000, 650, passo=0.08)
    E.relogio(c, t, C["s14.a"], 1580, 800, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    prods = [n * k for n, k in FILHOS]
    cel = [(str(p), a5 + 0.3 + 0.25 * j) for j, p in enumerate(prods)]
    extra = [("filhos × famílias", 290, a5, cel)]
    tot = [("37", b5, COR if t < C["s16"] else TINTA)]
    if t >= C["s16"] - 0.1:
        extra.append(("acumulada", 240, C["s16"], [("2", C["s16"] + 0.2, TINTA2), ("9", a6, COR if t < b6 else TINTA), ("14", b6, COR), ("", 0), ("", 0)]))
    tm = lerp(c6, d6, 0.5)
    tab(c, t, C["s15"], extra, tt=C["s15"], tot_extra=tot, linhas=FILHOS, nomes=("filhos", "famílias"), x=90,
        vez=1 if t >= tm else None)
    if t >= c6 - 0.1:
        linha_viva(c, t, c6, tm, 2, 1010, x=90)
    linha_viva(c, t, tm, None, 1, 380, x=90)
    X2 = 1530

    def um():
        E.frase(c, t, a5, [("média", "g", 64, COR)], X2, 330, "center")
        fcen(c, t, b5, "0 + 7 + 10 + 12 + 8 = 37", X2, 470, 52)
        fcen(c, t, c5, "37 ÷ 20 = 1,85", X2, 620, 76, COR)
        E.frase(c, t, c5 + 0.8, ps("filhos por família", "i", 48, TINTA2), X2, 710, "center", 0.06)
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, C["s16"] + 0.1, [("mediana:", "g", 60, COR)] + ps("o 10º e o 11º", "i", 56), X2, 300, "center", 0.08)
    fcen(c, t, b6, "9 + 5 = 14", X2, 420, 66)
    E.foco(c, t, c6, 0.4, lambda a: E.pilula(c, "mediana = 2", X2, 530, 56, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, tm, [("moda:", "g", 60, COR)] + ps("a maior frequência é 7", "i", 52), X2, 680, "center", 0.08)
    E.foco(c, t, d6, 0.4, lambda a: E.pilula(c, "moda = 1 filho", X2, 800, 56, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, d6 + 0.6, 0.4, lambda a: E.escreve(c, "não 7", X2 - 100, 920, 60, "g", ERRADO, a))
    if t >= d6 + 0.9:
        E.risco(c, X2 - 110, 900, X2 + 90, 880, t, d6 + 0.9, largura=8)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s17.a", [("média:", "g", 64, COR)] + ps("valor × frequência, ÷ total", "i", 60)),
                 ("s17.b", [("mediana:", "g", 64, COR)] + ps("pela acumulada", "i", 60)),
                 ("s17.c", [("moda:", "g", 64, COR)] + ps("o valor da linha mais frequente", "i", 60)))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a0, b0, c0, d0 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a0, [("qual medida", "g", 110, COR)] + ps("usar?", "i", 96), XE, 410)
    E.frase(c, t, b0, ps("um salário muito alto", "i", 54) + [("puxa a média", "g", 58, COR)], XE, 560, passo=0.08)
    E.frase(c, t, b0 + 1.6, ps("e quase não mexe na", "i", 54) + [("mediana", "g", 58, COR)], XE, 650, passo=0.08)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, media=b_media, mediana=b_mediana, moda=b_moda, erro=b_moda,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
