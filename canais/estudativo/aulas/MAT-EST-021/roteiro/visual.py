"""Visual — Estudativo · MAT-EST-021: praticando análise crítica de dados (5 conclusões). Fecha a trilha de Estatística.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá) e da análise crítica de MAT-EST-019/020:
colunas com eixo cortado (colunas_eixo(), circula(), pedaco()), manchete (manchete()), terceiro fator (tres()),
pessoas = bolinhas (pessoas()), barra de 100% (barra100()), pizza = E.pizza, dispersão = E.plano + E.ponto.
Novo nesta aula: cada situação termina com a CONCLUSÃO numa caixa pontilhada (conclusao()) e cada resposta abre com o
VEREDITO (veredito()): selo e pílula verde "se sustenta" ou vermelha "não se sustenta".
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-021_praticando_analise_critica_de_dados.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
APAGADO = E.mix(CINZA, PAPEL, 0.6)
CATS = E._paleta(3)
assert 1000 - 980 == 20 and 1050 - 980 == 70 and 70 / 20 == 3.5 and 1050 - 1000 == 50 and 50 / 1000 == 0.05
assert 60 + 45 + 30 == 135 and 500 / 2000 == 0.25 and 12 - 10 == 2 and 2 / 10 == 0.2
MIL = lambda v: f"{v:,}".replace(",", ".")


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


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados que entra coluna a coluna (de MAT-EST-001)"""
    h_lin = h_lin or size * 1.55
    xs = [x]
    for _, w, _ in colunas:
        xs.append(xs[-1] + w)
    larg = xs[-1] - x
    t_cab = min(ti for _, _, ti in colunas)
    p = ease_io(prog(t, t_fio if t_fio is not None else t_cab, 0.6))
    if p > 0:
        M.line(c, x, y + 20, x + larg * p, y + 20, TINTA, 1, 3)
    for k, (tit, w, ti) in enumerate(colunas):
        cx = xs[k] + w / 2
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: E.formula(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a, "center"))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc: centro(c, s, cx, yy, size, "g", cc[0] if cc else TINTA, a))
    if total:
        yf = y + 20 + h_lin * len(linhas) + 8
        tt = min(cel[1] for cel in total if cel[0] != "")
        q = ease_io(prog(t, tt, 0.5))
        if q > 0:
            M.line(c, x, yf, x + larg * q, yf, TINTA, 1, 6)
        yy = yf + h_lin * 0.72
        bases.append(yy)
        for k, cel in enumerate(total):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 and not s[0].isdigit() else "g", cc[0] if cc else TINTA, a))
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


def fichas(c, t, t0, itens, x, y, w, size=44, gap=22, passo=0.06):
    """lista de dados em grade de fichas, da esquerda para a direita. itens = [texto]"""
    cx, cy = x, y
    h = size * 1.55
    for i, s in enumerate(itens):
        wi = E.larg(s, "b", size) + size * 1.1
        if cx + wi > x + w:
            cx, cy = x, cy + h + gap
        px = cx + wi / 2
        E.foco(c, t, t0 + passo * i, 0.4, lambda a, s=s, px=px, cy=cy: ficha(c, s, px, cy, size, a), sobe=8)
        cx += wi + gap




def colunas_eixo(c, t, t0, dados, x, y, w, h, vmin, vmax, marcas, tv=None, quebra=None, size=46, cores=None, fmt=str, rot_t=None):
    """colunas com o eixo do lado começando em vmin (cortado se vmin > 0). dados = [(rótulo, valor)].
    tv = instante dos valores no topo (None: sem valores); quebra = instante do zigue-zague do corte. Devolve (vy, centros)"""
    cores = cores or CATS
    vy = lambda v: y + h - (v - vmin) / (vmax - vmin) * h
    p = ep(t, t0, 0.5)
    if p <= 0:
        return vy, []
    for v in marcas:
        if v != vmin:
            M.line(c, x, vy(v), x + w, vy(v), FIO, p, 2)
    M.line(c, x, y + h, x, y - 20, TINTA, 1, 4, progress=p)
    M.line(c, x - 10, y + h, x + w, y + h, TINTA, 1, 5, progress=p)
    for i, v in enumerate(marcas):
        E.foco(c, t, t0 + 0.15 + 0.04 * i, 0.4, lambda a, v=v: E.escreve(c, fmt(v), x - 20 - E.larg(fmt(v), "b", size), vy(v) + size * 0.36, size, "b", TINTA2, a), sobe=6)
    n = len(dados)
    slot = w / n
    bw = slot * 0.56
    cs = []
    for i, (rot, v) in enumerate(dados):
        cx = x + slot * (i + 0.5)
        q = ease_io(prog(t, t0 + 0.3 + 0.15 * i, 0.6))
        if q > 0:
            topo = lerp(y + h, vy(v), q)
            M.rrect(c, cx - bw / 2, topo, bw, y + h - topo, 10, cores[i], 1.0)
            c.drawRect(skia.Rect.MakeXYWH(cx - bw / 2, y + h - 12, bw, 12 * q), M.paint(cores[i]))
        E.foco(c, t, rot_t if rot_t is not None else t0 + 0.3, 0.4, lambda a, rot=rot, cx=cx: centro(c, rot, cx, y + h + 20 + size, size * 1.1, "g", TINTA, a), sobe=6)
        if tv is not None:
            E.foco(c, t, tv + 0.2 * i, 0.4, lambda a, v=v, cx=cx, i=i: centro(c, fmt(v), cx, vy(v) - 22, size * 1.15, "g", COR if i else TINTA, a), sobe=6)
        cs.append(cx)
    if quebra is not None:
        k = ep(t, quebra, 0.4)
        if k > 0:
            zy = y + h - 34
            pth = skia.Path(); pth.moveTo(x - 22, zy + 16)
            for j, dx in enumerate((-8, 8, -8, 8)):
                pth.lineTo(x + dx, zy - j * 12)
            c.drawRect(skia.Rect.MakeXYWH(x - 26, zy - 46, 52, 70), M.paint(PAPEL, k))
            M.line(c, x - 24, zy + 16, x + 24, zy + 4, ERRADO, k, 5)
            M.line(c, x - 24, zy - 6, x + 24, zy - 18, ERRADO, k, 5)
    return vy, cs


def circula(c, t, t0, cx, cy, r, cor=ERRADO):
    p = ep(t, t0, 0.5)
    if p > 0:
        E.arco(c, cx, cy, r, -90, 360 * p, cor, 6)


def pedaco(c, t, t0, x, y0, y1, rot, cor=ERRADO, size=48, lado=1):
    """chave vertical ao lado da coluna, de y0 (baixo) a y1 (cima), com o rótulo"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    ym = lerp(y0, y1, p)
    M.line(c, x, y0, x, ym, cor, 1, 5)
    M.line(c, x - 12 * lado, y0, x, y0, cor, 1, 5)
    if p > 0.95:
        M.line(c, x - 12 * lado, y1, x, y1, cor, 1, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.escreve(c, rot, x + 16, (y0 + y1) / 2 + size * 0.36, size, "g", cor, a) if lado > 0
                                          else E.escreve(c, rot, x - 16 - E.larg(rot, "g", size), (y0 + y1) / 2 + size * 0.36, size, "g", cor, a)), sobe=4)


def pessoas(c, t, t0, x, y, cols, lins, passo, r, estado=None, d=0.9):
    """a população em bolinhas (de MAT-EST-001). estado(i, j) -> (cor, anel)"""
    for j in range(lins):
        for i in range(cols):
            cx, cy = x + i * passo, y + j * passo
            k = ease_back(prog(t, t0 + d * (i / max(1, cols - 1)) * 0.8 + 0.02 * j, 0.35))
            cor, anel = (estado(i, j) if estado else (None, False))
            if k > 0:
                c.drawCircle(cx, cy, r * k, M.paint(cor or E.COR))
                if anel:
                    c.drawCircle(cx, cy, (r + 7) * k, M.paint(TINTA, 1, stroke=4))


def manchete(c, t, t0, cx, cy, w, linhas, size=64, rot="MANCHETE"):
    """o número de jornal: cartão branco com faixa preta e a frase em grotesca"""
    def fn(a):
        h = 110 + len(linhas) * size * 1.25
        x, y = cx - w / 2, cy - h / 2
        sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
        sh.setImageFilter(skia.ImageFilters.Blur(18, 18))
        c.drawRect(skia.Rect.MakeXYWH(x + 10, y + 16, w, h), sh)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(BR, a))
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, 56), M.paint(TINTA, a))
        E.escreve(c, rot, x + 30, y + 40, 32, "b", BR, a)
        for i, s in enumerate(linhas):
            centro(c, s, cx, y + 56 + size * 1.2 * (i + 1), size, "g", TINTA, a)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=3))
    E.foco(c, t, t0, 0.5, fn)


def no(c, s, cx, cy, size=52, cor=None, a=1.0):
    w = E.larg(s, "g", size) + size * 1.2
    E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, a=a)
    return w


def tres(c, t, tc, t1, t2, tx, causa, ef1, ef2, cx, cy, dx=420, dy=170, size=54):
    """o terceiro fator: causa em cima, efeitos embaixo; setas da causa (t1, t2) e a seta riscada entre os efeitos (tx)"""
    A, B1, B2 = (cx, cy - dy), (cx - dx, cy + dy), (cx + dx, cy + dy)
    for (P, ti) in ((B1, t1), (B2, t2)):
        p = ep(t, ti, 0.5)
        if p > 0:
            ux, uy = P[0] - A[0], P[1] - A[1]
            L = math.hypot(ux, uy)
            M.arrow(c, A[0] + ux / L * 70, A[1] + uy / L * 70, P[0] - ux / L * 70, P[1] - uy / L * 70, TINTA, 1, 6, 22, p)
    if tx is not None:
        p = ep(t, tx, 0.5)
        if p > 0:
            pt = M.paint(TINTA2, p, stroke=5)
            pt.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
            c.drawLine(B1[0] + 220, B1[1], B2[0] - 220, B2[1], pt)
            M.line(c, B2[0] - 240, B2[1] - 14, B2[0] - 220, B2[1], TINTA2, p, 5)
            M.line(c, B2[0] - 240, B2[1] + 14, B2[0] - 220, B2[1], TINTA2, p, 5)
            k = ep(t, tx + 0.4, 0.4)
            if k > 0:
                M.line(c, cx - 36 * k, B1[1] - 36 * k, cx + 36 * k, B1[1] + 36 * k, ERRADO, 1, 10)
                M.line(c, cx - 36 * k, B1[1] + 36 * k, cx + 36 * k, B1[1] - 36 * k, ERRADO, 1, 10)
    E.foco(c, t, tc, 0.5, lambda a: no(c, causa, *A, size, a=a))
    E.foco(c, t, min(t1, tx if tx is not None else t1), 0.5, lambda a: no(c, ef1, *B1, size, TINTA2, a))
    E.foco(c, t, min(t2, tx if tx is not None else t2), 0.5, lambda a: no(c, ef2, *B2, size, TINTA2, a))


def barra100(c, t, t0, x, y, w, h, partes, cores=None, rotulos=None, size=46, d=1.0, a=1.0):
    """frequência relativa: barra deitada de 100% dividida nas fatias das categorias (partes em %), cada fatia entra no seu
    tempo (t0 número = em fila; lista = um instante por fatia) e ganha a % (ou o rótulo) dentro"""
    cores = cores or E._paleta(len(partes))
    tot = float(sum(partes))
    ts = t0 if isinstance(t0, (list, tuple)) else [t0 + d * i / len(partes) for i in range(len(partes))]
    xa = x
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    if t >= min(ts):
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(E.mix(FIO, PAPEL, 0.5), a))
        for i, v in enumerate(partes):
            wi = w * v / tot
            q = ease_io(prog(t, ts[i], 0.5))
            if q > 0:
                c.drawRect(skia.Rect.MakeXYWH(xa, y, wi * q, h), M.paint(cores[i], a))
            xa += wi
        c.restore()
        xa = x
        for i, v in enumerate(partes):
            wi = w * v / tot
            if i:
                M.line(c, xa, y, xa, y + h, PAPEL, a * ep(t, ts[i], 0.4), 5)
            s = rotulos[i] if rotulos else E._num(v) + "%"
            cor_t = BR if M.lum(cores[i]) < 0.5 else TINTA
            E.foco(c, t, ts[i] + 0.3, 0.4, lambda q, s=s, xa=xa, wi=wi, cor_t=cor_t: centro(c, s, xa + wi / 2, y + h / 2 + size * 0.36, size, "g", cor_t, q * a))
            xa += wi
        c.drawRRect(r, M.paint(TINTA, a * ep(t, min(ts), 0.4), stroke=3))


def veredito(c, t, t0, ok, texto, cx=W / 2, cy=200, size=60):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, texto, cx, cy, size, "g", fundo=CERTO if ok else ERRADO, a=a))
    w = E.larg(texto, "g", size) + size * 1.2
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: E.selo(c, cx - w / 2 - 60, cy - size * 0.3, 40, ok, a))


def conclusao(c, t, t0, linhas, x, y, w, size=54):
    h = 90 + len(linhas) * size * 1.25
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.escreve(c, "conclusão:", x + 36, y + 62, 46, "i", TINTA2, a))
    for i, s in enumerate(linhas):
        E.frase(c, t, t0 + 0.3 + 0.3 * i, [(s, "g", size, COR)], x + 36, y + 62 + size * 1.25 * (i + 1), "left")


def situacao(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, f"situação {n}" if n != 5 else "última situação", XE + 180, 140, 54, "g", a=a, cor=E.SOBRE))


def relogio(c, t, t0):
    E.relogio(c, t, t0, cx=1660, cy=800, r=110)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")
    E.frase(c, t, a1, [("5", "g", 160, COR)] + ps("conclusões", "i", 110), XE, 340, passo=0.14)
    E.frase(c, t, b1, ps("ela", "i", 72) + [("se sustenta nos dados?", "g", 78, COR)], XE, 490, passo=0.1)
    E.relogio(c, t, c1, cx=1500, cy=740, r=150)
    E.foco(c, t, d1, 0.5, lambda a: E.selo(c, XE + 40, 760, 44, True, a))
    E.foco(c, t, d1 + 0.3, 0.5, lambda a: E.selo(c, XE + 150, 760, 44, False, a))
    E.frase(c, t, d1 + 0.5, ps("nem toda conclusão", "i", 56) + [("está errada", "g", 60, CERTO)], XE, 880, passo=0.08)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s02.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02.a"] + 0.15, 0.5, lambda a: E.escreve(c, "kits", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 860, 960
    itens = (("s02.a", "os 3 olhares do gráfico", ["eixo no zero", "escala com passo igual", "figura proporcional"]),
             ("s02.b", "as 3 perguntas da pesquisa", ["quem foi ouvido?", "por cento de quanto?", "o que mais mudou junto?"]))
    for i, (k, tit, linhas) in enumerate(itens):
        y = 180 + i * 380
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 340, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(tit, "g", 58, COR)], x + 40, y + 80, "left")
        for j, s in enumerate(linhas):
            E.frase(c, t, C[k] + 0.8 + 0.9 * j, [(f"{j + 1}.", "g", 48, TINTA2)] + ps(s, "i", 50), x + 60, y + 160 + 64 * j, "left", 0.06)
    E.frase(c, t, lerp(C["s02.b"], C["s02.end"], 0.7), ps("travou?", "i", 48, COR) + ps("procure a aula no canal", "i", 48), x, 1000, "left", 0.1)


# ---------------- situação 1: eixo cortado ----------------
AX, AY, AW, AH = 300, 330, 560, 470


def aluguel(c, t, t0, tv=None):
    return colunas_eixo(c, t, t0, [("bairro A", 1000), ("bairro B", 1050)], AX, AY, AW, AH, 980, 1060, [980, 1000, 1020, 1040, 1060],
                        tv=tv, size=40, fmt=MIL)


def b_questao1(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s03.{k}"] for k in "abcde")
    situacao(c, t, a3, 1)
    E.frase(c, t, b3, ps("aluguel médio em dois bairros", "i", 52) + [("(R$)", "g", 50)], XE, 240, passo=0.08)
    vy, cs = aluguel(c, t, b3 + 0.4, d3)
    circula(c, t, c3, AX - 60, vy(980) - 14, 56)
    E.frase(c, t, c3, ps("o eixo começa em", "i", 48, TINTA2) + [("R$ 980", "g", 52, ERRADO)], AX, 960, passo=0.08)
    conclusao(c, t, e3, ["o aluguel em B é mais de", "3 vezes o de A"], 1000, 300, 820)
    relogio(c, t, C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    veredito(c, t, a5, False, "não se sustenta", 1420, 180)
    vy, cs = aluguel(c, t, C["s05"], C["s05"])
    bw = AW / 2 * 0.56
    pedaco(c, t, b5, cs[0] + bw / 2 + 20, vy(980), vy(1000), "20", ERRADO)
    pedaco(c, t, b5 + 2.6, cs[1] + bw / 2 + 20, vy(980), vy(1050), "70", ERRADO)
    X = 1420

    def um():
        fcen(c, t, b5, "1.000 − 980 = 20", X, 360, 62)
        fcen(c, t, b5 + 2.6, "1.050 − 980 = 70", X, 470, 62)
        fcen(c, t, c5, "70 ÷ 20 = 3,5", X, 610, 70, ERRADO)
        E.frase(c, t, c5 + 0.6, ps("daí a impressão", "i", 48, ERRADO), X, 680, "center", 0.06)
    fase(c, t, C["s05"], C["s06"] - 0.1, um)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("com os valores:", "i", 54), X, 330, "center", 0.08)
    fcen(c, t, a6, "1.050 − 1.000 = 50", X, 450, 64)
    fcen(c, t, b6, "50 ÷ 1.000 = 0,05", X, 570, 64)
    bola_txt(c, t, c6, "5%", X, 760, 110, 84)
    E.frase(c, t, c6 + 0.4, ps("B é só 5% maior", "i", 48, TINTA2), X, 940, "center", 0.06)


# ---------------- situação 2: pizza acima de 100% ----------------
APPS = [("app X · 60%", 60), ("app Y · 45%", 45), ("app Z · 30%", 30)]


def b_questao2(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    situacao(c, t, a7, 2)
    E.frase(c, t, b7, ps("pergunta:", "i", 52, TINTA2) + [("quais aplicativos de transporte você usa?", "g", 54)], XE, 250, passo=0.06)
    E.pizza(c, t, c7, APPS, 440, 650, 220, pct=False, size=44)
    conclusao(c, t, d7, ["o gráfico mostra bem como", "os usuários se dividem", "entre os aplicativos"], 1080, 360, 780, 50)
    relogio(c, t, C["s08.a"])


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    veredito(c, t, a9, False, "não se sustenta", 1420, 180)
    E.pizza(c, t, C["s09"] - 1.2, APPS, 520, 620, 240, pct=False, size=44)
    X = 1400

    def um():
        fcen(c, t, b9, "60 + 45 + 30 = 135%", X, 380, 74, ERRADO)
        E.frase(c, t, c9, ps("a pizza inteira é", "i", 54) + [("100%", "g", 60, COR)], X, 520, "center", 0.08)
        E.frase(c, t, d9, ps("aceitava", "i", 52) + [("mais de uma resposta", "g", 56, ERRADO)], X, 650, "center", 0.08)
        E.frase(c, t, d9 + 1.2, ps("quem usa 2 apps foi contado 2 vezes", "i", 46, TINTA2), X, 730, "center", 0.06)
    fase(c, t, C["s09"], e9 - 0.1, um)
    if t >= e9 - 0.1:
        E.frase(c, t, e9, ps("o certo:", "i", 54) + [("gráfico de colunas", "g", 58, CERTO)], X, 330, "center", 0.08)
        E.colunas(c, t, e9 + 0.3, [("X", 60, CATS[0]), ("Y", 45, CATS[1]), ("Z", 30, CATS[2])], 1080, 430, 640, 450, vmax=70,
                  fmt=lambda v: f"{v}%", size=46)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.2, ps("o atalho:", "i", 60, CLARO), XE, 180, passo=0.1)
    E.frase(c, t, a0, [("some as fatias", "g", 76, BR)], XE, 300, passo=0.1)
    E.frase(c, t, a0 + 1.0, ps("antes de ler qualquer pizza", "i", 60, CLARO), XE, 380, passo=0.1)
    E.frase(c, t, b0, ps("cada pessoa:", "i", 56, CLARO) + [("uma fatia só", "g", 60, BR)], XE, 520, passo=0.08)
    E.frase(c, t, b0 + 2.2, ps("passou de 100%:", "i", 56, CLARO) + [("contou 2 vezes", "g", 60, BR)], XE, 610, passo=0.08)
    E.foco(c, t, c0, 0.5, lambda a: E.selo(c, XE + 40, 760, 40, False, a))
    E.frase(c, t, c0 + 0.1, ps("não compensa: brigar por 1 ponto", "i", 54, CLARO), XE + 110, 780, passo=0.08)
    E.frase(c, t, d0, [("99% ou 101%", "g", 60, BR)] + ps("= arredondamento", "i", 56, CLARO), XE + 110, 870, passo=0.08)
    cx, cy, r = 1500, 560, 210
    p = ease_io(prog(t, a0, 1.2))
    ang = -90.0
    for v, cor in ((50, E.COR), (30, CLARO), (20, E.mix(CLARO, BR, 0.5))):
        varre = 360 * v / 100
        fim = min(ang + varre, -90 + 360 * p)
        if fim > ang:
            pth = skia.Path()
            pth.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ang, fim - ang, True)
            pth.arcTo(skia.Rect.MakeXYWH(cx - r * 0.55, cy - r * 0.55, 2 * r * 0.55, 2 * r * 0.55), fim, ang - fim, False)
            pth.close()
            c.drawPath(pth, M.paint(cor))
            c.drawPath(pth, M.paint("#07070F", 1, stroke=5))
        ang += varre
    E.foco(c, t, a0 + 1.2, 0.4, lambda a: centro(c, "100%", cx, cy + 26, 74, "g", BR, a))


# ---------------- situação 3: amostra boa ----------------
SORTEIO = lambda i, j: (i * 5 + j * 3) % 4 == 0      # um quarto, espalhado


def grade_escola(c, t, t0, ts, x=160, y=420):
    def est(i, j):
        if t < ts:
            return None, False
        dentro = SORTEIO(i, j)
        q = ep(t, ts, 0.5)
        return (E.COR if dentro else E.mix(E.COR, APAGADO, q)), dentro and q > 0.5
    pessoas(c, t, t0, x, y, 12, 7, 66, 22, est)


def b_questao3(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    situacao(c, t, a1, 3)

    def g():
        grade_escola(c, t, b1, c1)
        E.frase(c, t, b1, ps("escola:", "i", 52) + [("2.000 alunos", "g", 56, COR)], XE, 280, passo=0.08)
    fase(c, t, C["s11"], C["s12.a"] - 0.1, g)
    X = 1400
    E.frase(c, t, c1, ps("sorteou", "i", 52) + [("500,", "g", 56, COR)] + ps("proporcional ao turno", "i", 52), X, 300, "center", 0.08)
    E.frase(c, t, c1 + 1.6, ps("quer reforço aos sábados?", "i", 50, TINTA2), X, 380, "center", 0.08)
    E.frase(c, t, d1, [("60%", "g", 80, COR)] + ps("disseram sim", "i", 56), X, 510, "center", 0.08)
    conclusao(c, t, e1, ["a maioria dos alunos", "da escola quer o reforço"], 1000, 600, 820, 50)
    E.relogio(c, t, C["s12.a"], cx=520, cy=560, r=170)


def b_resposta3(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, ps("quem foi ouvido?", "i", 60), W / 2, 190, "center", 0.08)
    grade_escola(c, t, C["s13"], C["s13"], y=380)
    X = 1400
    E.frase(c, t, a3, ps("sorteados", "i", 52) + [("entre todos,", "g", 56, COR)], X, 330, "center", 0.08)
    E.frase(c, t, a3 + 1.2, ps("cada turno no seu peso", "i", 50), X, 400, "center", 0.08)
    E.frase(c, t, a3 + 2.6, [("a panela mexida", "g", 54, CERTO)], X, 480, "center", 0.08)
    fcen(c, t, b3, "500 ÷ 2.000 = 0,25 = f{1}{4}", X, 620, 62)
    barra100(c, t, [c3, c3 + 0.4], 300, 880, 1320, 90, [60, 40], [E.COR, E.mix(FIO, PAPEL, 0.2)], ["sim: 60%", ""], size=44)
    if t >= c3:
        xm = 300 + 1320 * 0.5
        M.line(c, xm, 850, xm, 1000, ERRADO, ep(t, c3 + 0.6, 0.4), 5, dash=E.TRACO)
        E.foco(c, t, c3 + 0.8, 0.4, lambda a: centro(c, "metade", xm, 1040, 42, "b", ERRADO, a))
    veredito(c, t, d3, True, "se sustenta", 1400, 760, 56)


# ---------------- situação 4: ponto percentual ----------------
def b_questao4(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    situacao(c, t, a4, 4)
    E.frase(c, t, a4 + 0.6, ps("taxa de desemprego da cidade", "i", 56), XE, 260, passo=0.08)
    fcen(c, t, b4, "10%", 480, 480, 150)
    E.foco(c, t, c4 - 0.3, 0.4, lambda a: M.arrow(c, 680, 430, 900, 430, TINTA2, a, 7, 24))
    fcen(c, t, c4, "12%", 1100, 480, 150, COR)
    manchete(c, t, d4, 760, 760, 1100, ["Desemprego sobe 2%"], 76)
    relogio(c, t, C["s15.a"])


def b_resposta4(c, t, C, b):
    a6, b6, c6, d6, e6, f6 = (C[f"s16.{k}"] for k in "abcdef")

    def um():
        veredito(c, t, a6, False, "não se sustenta como está escrita", W / 2, 170, 54)
        fcen(c, t, b6, "12% − 10% = 2 pontos percentuais", W / 2, 360, 66)
        fcen(c, t, c6, "2 ÷ 10 = 0,2", 700, 520, 72)
        fcen(c, t, d6, "= 20%", 1200, 520, 72, COR)
        E.frase(c, t, d6 + 0.5, ps("variação percentual", "i", 46, TINTA2), 960, 600, "center", 0.06)
        manchete(c, t, e6, W / 2, 780, 1500, ["Desemprego sobe 2 pontos percentuais, ou 20%"], 58, "A MANCHETE CERTA")
        E.frase(c, t, f6, ps("o erro deixou a notícia", "i", 50) + [("menos grave", "g", 54, ERRADO)], W / 2, 1010, "center", 0.08)
    um()


# ---------------- situação 5: correlação ----------------
FOGO = [(1, 1.2), (2, 2.0), (2.5, 3.1), (3.5, 3.4), (4, 4.6), (5, 4.9), (6, 6.2), (7, 6.8)]


def b_questao5(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    situacao(c, t, a7, 5)
    E.frase(c, t, b7, ps("levantamento de incêndios", "i", 54), XE, 250, passo=0.08)
    P = E.plano(c, t, b7 + 0.3, 260, 360, 640, 480, 0, 8, 0, 8, passo=2, nomes=("bombeiros", "prejuízo"), rotulos=False)
    for i, (x, y) in enumerate(FOGO):
        E.ponto(c, t, c7 + 0.12 * i, P, x, y, r=14)
    conclusao(c, t, d7, ["mandar mais bombeiros", "aumenta o prejuízo"], 1060, 330, 760, 52)
    relogio(c, t, C["s18.a"])


def b_resposta5(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    veredito(c, t, a9, False, "não se sustenta", W / 2, 180)
    E.frase(c, t, a9 + 1.0, ps("o que mais mudou junto?", "i", 56), W / 2, 320, "center", 0.08)
    tres(c, t, b9, c9, d9, e9 - 0.4, "tamanho do incêndio", "mais bombeiros", "mais prejuízo", W / 2, 620, dx=460)
    E.frase(c, t, e9, ps("os dados mostram", "i", 56) + [("correlação, não causa", "g", 60, COR)], W / 2, 1000, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s20.a", ps("olhe", "i", 58) + [("o eixo, a escala e a figura", "g", 62, COR)]),
                 ("s20.b", [("some a pizza", "g", 62, COR)]),
                 ("s20.c", ps("quem foi ouvido,", "i", 54) + ps("por cento de quanto,", "i", 54) + ps("o que mudou junto", "i", 54)),
                 ("s20.d", ps("tudo passou?", "i", 58) + [("a conclusão fica de pé", "g", 62, CERTO)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 50, a=a), centro(c, str(i + 1), 200, y - 4, 58, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, a1, ps("trilha de", "i", 70) + [("estatística: completa", "g", 76, CERTO)], XE, 250, passo=0.1)
    E.frase(c, t, b1, ps("na próxima aula:", "i", 60) + [("contagem", "g", 100, COR)], XE, 420, passo=0.1)
    E.frase(c, t, c1, ps("3 camisas e 4 calças:", "i", 54) + [("quantas roupas?", "g", 58, COR)], XE, 560, passo=0.08)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(700, 405, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
