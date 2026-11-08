"""Visual — Estudativo · MAT-EST-007: praticando dados, tabelas e gráficos (aula de prática, 5 situações).
Mesma linguagem da Estatística de MAT-EST-001 a 006, com as peças copiadas de lá:
- barras com a grade do eixo e a leitura por guia tracejada (guia(), MAT-EST-003);
- linha no tempo com as pílulas de variação, o trecho da maior alta grosso e o anel no ponto mais alto (variacoes(), trecho(),
  anel(), MAT-EST-003);
- pizza com o ângulo do setor no centro (ang_centro(), MAT-EST-004);
- histograma com colunas por instante e a faixa da vez (Hist, eixos_h(), hist_cols(), MAT-EST-005) e classe(20, 30)
  (MAT-EST-002);
- tabela (quadro(), MAT-EST-001) com a faixa clara na linha da vez (banda(), MAT-EST-006).
Cada situação: o gráfico entra à direita com a pergunta à esquerda e o relógio de pausa; na resposta, o gráfico vai para a
esquerda e a conta da vez fica à direita, com a resposta na esfera.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-007_praticando_dados_tabelas_e_graficos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
APAGADO = E.mix(CINZA, PAPEL, 0.55)
CATS = E._paleta(4)
ESPORTE = [("futebol", 20, CATS[0]), ("vôlei", 12, CATS[1]), ("corrida", 10, CATS[2]), ("natação", 8, CATS[3])]
CINE = [("jan", 300), ("fev", 360), ("mar", 320), ("abr", 480), ("mai", 500)]
LIM4, FREQ4 = [0, 10, 20, 30, 40], [18, 15, 12, 5]
assert sum(v for _, v, _ in ESPORTE) == 50 and 6 * 2 == 12 and 12 * 2 == 24
assert [CINE[i + 1][1] - CINE[i][1] for i in range(4)] == [60, -40, 160, 20] and 160 / 320 == 0.5
assert 108 == 3 * 36 and 3000 // 10 == 300 and 300 * 3 == 900 and 108 / 360 == 0.3
assert sum(FREQ4) == 50 and 12 + 5 == 17 and 17 * 2 == 34
assert 45 * 4 == 60 * 3 and 72 / 120 == 0.6 and 45 / 60 == 0.75


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, °, ² ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%°²³→") else est, size * (0.92 if any(ch in w for ch in "%°²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def situacao(c, t, t0, n, x=XE, y=170):
    """a pílula "situação n" no alto"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}", x + (E.larg(f"situação {n}", "g", 50) + 55) / 2, y, 50, "g", a=a, cor=E.SOBRE))


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None):
    """tabela de dados (MAT-EST-001). colunas = [(título, largura, t0)]; linhas = [[(texto, t0[, cor]), ...], ...]"""
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
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", TINTA2, a))
    bases = []
    for j, lin in enumerate(linhas):
        yy = y + 20 + h_lin * (j + 1) - h_lin * 0.3
        bases.append(yy)
        for k, cel in enumerate(lin):
            s, ti, *cc = cel
            if s == "":
                continue
            cx = xs[k] + colunas[k][1] / 2
            if k == 0 and cores:
                E.foco(c, t, ti, 0.4, lambda a, yy=yy, j=j: c.drawCircle(xs[0] + 22, yy - size * 0.34, size * 0.24, M.paint(cores[j], a)))
                cx += 22
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: centro(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else TINTA, a))
    return bases


def classe(ini, fim):
    """rótulo de classe "20 ⊢ 30" (MAT-EST-002), desenhado: a fonte não tem o sinal"""
    def fn(c, cx, y, size, cor, a):
        s1, s2 = str(ini), str(fim)
        w1, w2 = E.larg(s1, "g", size), E.larg(s2, "g", size)
        gap = size * 1.05
        x0 = cx - (w1 + gap + w2) / 2
        E.escreve(c, s1, x0, y, size, "g", cor, a)
        sx, sy = x0 + w1 + size * 0.28, y - size * 0.36
        M.line(c, sx, sy - size * 0.32, sx, sy + size * 0.32, cor, a, max(3, size * 0.09))
        M.line(c, sx, sy, sx + gap - size * 0.56, sy, cor, a, max(3, size * 0.09))
        E.escreve(c, s2, x0 + w1 + gap, y, size, "g", cor, a)
    return fn


# ---------------- gráficos de barras e de linhas (MAT-EST-003) ----------------
class Graf:
    def __init__(self, x, y, w, h, n, vmax, vmin=0):
        self.x, self.y, self.w, self.h, self.n, self.vmax, self.vmin = x, y, w, h, n, vmax, vmin

    def px(self, i):
        return self.x + self.w * (i + 0.5) / self.n

    def py(self, v):
        return self.y + self.h - (v - self.vmin) / (self.vmax - self.vmin) * self.h

    def pt(self, i, v):
        return self.px(i), self.py(v)


def guia(c, t, t0, G, i, v, rotulo=None, cor=None, size=44):
    p = ease_io(prog(t, t0, 0.6))
    if p <= 0:
        return
    k = cor or E.COR
    xs, y = G.px(i), G.py(v)
    M.line(c, xs, y, lerp(xs, G.x, p), y, k, 1, 5, dash=E.TRACO)
    c.drawCircle(xs, y, 9, M.paint(k))
    s = rotulo if rotulo is not None else E._num(v)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.pilula(c, s, G.x - 20 - (E.larg(s, "g", size) + size * 1.1) / 2, y, size, "g", fundo=k, a=a))


def trecho(c, t, t0, G, dados, i, cor=None, largura=13):
    p = ease_io(prog(t, t0, 0.6))
    if p > 0:
        P, Q = G.pt(i, dados[i][1]), G.pt(i + 1, dados[i + 1][1])
        M.line(c, *P, *Q, cor or E.COR, 1, largura, progress=p)


def variacoes(c, t, ts, G, dados, size=38, dy=-56, off=None):
    """a pílula "+30" sobre cada trecho no instante ts[i] (MAT-EST-003); off = {i: (dx, dy)} afasta a pílula de um rótulo"""
    for i, ti in enumerate(ts):
        if ti is None:
            continue
        d = dados[i + 1][1] - dados[i][1]
        P, Q = G.pt(i, dados[i][1]), G.pt(i + 1, dados[i + 1][1])
        s = ("+" if d > 0 else "−") + E._num(abs(d))
        mx = (P[0] + Q[0]) / 2
        if d > 0:
            mx, my = mx - 50, (P[1] + Q[1]) / 2 + dy - 14
        else:
            mx, my = mx - 10, (P[1] + Q[1]) / 2 + 74
        if off and i in off:
            mx, my = mx + off[i][0], my + off[i][1]
        E.foco(c, t, ti, 0.4, lambda a, s=s, mx=mx, my=my, d=d: E.pilula(c, s, mx, my, size, "g", fundo=E.COR if d > 0 else TINTA2, a=a))


def anel(c, t, t0, P, r=30, cor=None):
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or ERRADO, 1, stroke=6))


def eixos_linha(c, t, t0, G, dados, marcas, unidade=None, size=38):
    vy = E._eixo_dados(c, t, t0, G.x, G.y, G.w, G.h, G.vmin, G.vmax, marcas, E._num, size, TINTA)
    for i, (rot, _) in enumerate(dados):
        E.foco(c, t, t0 + 0.2 + 0.05 * i, 0.4, lambda a, i=i, rot=rot: centro(c, rot, G.px(i), G.y + G.h + 18 + size * 1.05, size, "b", TINTA, a))
    if unidade:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, unidade, G.x - 10, G.y - 46, 38, "i", TINTA2, a))
    return vy


# ---------------- setores (MAT-EST-004) ----------------
def _u(g):
    return math.cos(math.radians(g)), math.sin(math.radians(g))


def ang_centro(c, t, t0, cx, cy, ini, varre, rotulo, cor=TINTA, r=70, dist=None, size=50):
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    E.arco(c, cx, cy, r, ini, varre * p, cor, 6)
    ux, uy = _u(ini + varre / 2)
    d = dist or r + 30 + size * 0.9
    E.foco(c, t, t0 + 0.25, 0.4, lambda a: centro(c, rotulo, cx + ux * d, cy + uy * d + size * 0.36, size, "g", cor, a))


# ---------------- histograma (MAT-EST-005) ----------------
class Hist:
    def __init__(self, x, y, w, h, lims, vmax, marcas):
        self.x, self.y, self.w, self.h, self.lims, self.vmax, self.marcas = x, y, w, h, lims, vmax, marcas

    def vx(self, v):
        return self.x + (v - self.lims[0]) / (self.lims[-1] - self.lims[0]) * self.w

    def vy(self, f):
        return self.y + self.h - f / self.vmax * self.h


def eixos_h(c, t, t0, G, size=38, unidade=None, eixo=None):
    E._eixo_dados(c, t, t0, G.x, G.y, G.w, G.h, 0, G.vmax, G.marcas, E._num, size, TINTA)
    for i, v in enumerate(G.lims):
        E.foco(c, t, t0 + 0.2 + i * 0.04, 0.4, lambda a, v=v: (M.line(c, G.vx(v), G.y + G.h, G.vx(v), G.y + G.h + 14, TINTA, a, 4),
                                                               centro(c, E._num(v), G.vx(v), G.y + G.h + 24 + size, size, "b", TINTA, a)), sobe=6)
    if unidade:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, unidade, G.x - 10, G.y - 46, 38, "i", TINTA2, a))
    if eixo:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, eixo, G.x + G.w - E.larg(eixo, "i", 36), G.y + G.h + 24 + size + 46, 36, "i", TINTA2, a))


def hist_cols(c, t, ts, G, freqs, cores=None, valores=True, size=38, d=0.5):
    for i, f in enumerate(freqs):
        q = E.ease_out(prog(t, ts[i], d))
        if q <= 0:
            continue
        x0, x1 = G.vx(G.lims[i]), G.vx(G.lims[i + 1])
        cr = (cores[i] if cores else None) or E.COR
        topo = lerp(G.y + G.h, G.vy(f), q)
        c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, G.y + G.h), M.paint(cr))
        c.drawRect(skia.Rect.MakeLTRB(x0, topo, x1, G.y + G.h), M.paint(PAPEL, 1.0, stroke=4))
        if valores:
            cv = COR if cr == E.COR else TINTA2
            E.foco(c, t, ts[i] + d * 0.8, 0.4, lambda a, f=f, x0=x0, x1=x1, cv=cv: centro(c, E._num(f), (x0 + x1) / 2, G.vy(f) - 22, size * 1.05, "g", cv, a), sobe=6)


def faixa(c, t, t0, G, v0, v1, rotulo, cor=None, dy=120, size=42):
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0:
        return
    y = G.y + G.h + dy
    E.chave(c, G.vx(v0), G.vx(v1), y, cor or E.COR, p, 22, 6)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rotulo, (G.vx(v0) + G.vx(v1)) / 2, y + 30 + size, size, "g", cor or COR, a))


# ---------------- os gráficos das situações ----------------
GQ1 = Graf(1080, 300, 760, 560, 4, 20)       # na pergunta, à direita
GR1 = Graf(260, 280, 860, 600, 4, 20)        # na resposta, à esquerda
MARC1 = list(range(0, 21, 2))
GQ2 = Graf(1080, 320, 760, 520, 5, 600)
GR2 = Graf(230, 280, 960, 600, 5, 600)
MARC2 = [0, 100, 200, 300, 400, 500, 600]
HQ4 = Hist(1080, 320, 760, 520, LIM4, 20, [0, 5, 10, 15, 20])
HR4 = Hist(250, 300, 900, 500, LIM4, 20, [0, 5, 10, 15, 20])


def esporte(c, t, t0, G, size=38):
    E.colunas(c, t, t0, ESPORTE, G.x, G.y, G.w, G.h, vmax=20, eixo_y=True, marcas=MARC1, valores=False, size=size)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: E.escreve(c, "pessoas", G.x - 10, G.y - 46, 38, "i", TINTA2, a))


def cinema(c, t, t0, G, d=1.4, size=38):
    eixos_linha(c, t, t0, G, CINE, MARC2, "público", size)
    E.serie(c, t, t0, CINE, G.x, G.y, G.w, G.h, vmin=0, vmax=600, marcas=MARC2, cor=TINTA, d=d, eixos=False, size=size)


def despesas(c, t, t0, cx, cy, r, d=1.0):
    E.pizza(c, t, t0, [("aluguel", 30), ("", 70)], cx, cy, r, cores=[E.COR, E.mix(FIO, PAPEL, 0.2)], rotulos=False, d=d)
    E.foco(c, t, t0 + d, 0.4, lambda a: centro(c, "aluguel", cx + r * 0.62, cy - r - 30, 46, "b", COR, a))
    E.foco(c, t, t0 + d + 0.2, 0.4, lambda a: centro(c, "outras despesas", cx - r * 0.3, cy + r + 70, 40, "i", TINTA2, a))


def espera(c, t, ts, G, cores=None, size=38, t0=None):
    eixos_h(c, t, ts[0] - 0.4 if t0 is None else t0, G, size, "pessoas", "minutos")
    hist_cols(c, t, ts, G, FREQ4, cores, True, size)


def aprovacao(c, t, t0, tm, tn, x, y, size=58, cor_lin=None):
    cols = [("turno", 260, t0), ("aprovados", 300, t0 + 0.2), ("alunos", 260, t0 + 0.3)]
    cl = cor_lin or {}
    linhas = [[("manhã", tm), ("45", tm + 0.4, cl.get(0, TINTA)), ("60", tm + 0.8, cl.get(0, TINTA))],
              [("noite", tn), ("72", tn + 0.4, cl.get(1, TINTA)), ("120", tn + 0.8, cl.get(1, TINTA))]]
    return quadro(c, t, x, y, cols, linhas, None, size, size * 1.7)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "5", XE - 8, 560, 340, "g", COR, a))
    E.frase(c, t, a1 + 0.2, ps("situações com", "i", 84), XE + 230, 420, passo=0.12)
    E.frase(c, t, a1 + 0.9, [("tabelas e gráficos", "g", 90, COR)], XE + 230, 530, passo=0.12)
    y, w, h, gap = 660, 290, 200, 60
    xs = [XE + (w + gap) * i for i in range(5)]
    t0 = a1 + 1.6
    E.colunas(c, t, t0, [("", 5), ("", 8), ("", 3)], xs[0], y, w, h, vmax=9, valores=False, size=20)
    E.serie(c, t, t0 + 0.3, [("", 2), ("", 4), ("", 3), ("", 6)], xs[1], y, w, h, vmin=0, vmax=7, marcas=[], valores=False, eixos=False, size=20)
    M.line(c, xs[1], y + h, xs[1] + w, y + h, TINTA, ep(t, t0 + 0.3, 0.4), 5)
    E.pizza(c, t, t0 + 0.6, [("", 40), ("", 35), ("", 25)], xs[2] + w / 2, y + h / 2, h / 2, rotulos=False, d=0.8)
    E.histograma(c, t, t0 + 0.9, [0, 1, 2, 3, 4], [2, 5, 4, 1], xs[3], y, w, h, vmax=6, marcas=[], valores=False, size=1)
    for i in range(3):
        for k in range(3):
            E.foco(c, t, t0 + 1.2 + 0.03 * (i + k), 0.3, lambda a, i=i, k=k: M.rrect(c, xs[4] + k * (w / 3) + 6, y + 20 + i * 62, w / 3 - 12, 50, 8,
                                                                                   E.COR if (i, k) == (1, 1) else E.mix(FIO, PAPEL, 0.1), a))
    E.relogio(c, t, b1, 1560, 300, 110)


# ---------------- o que vai usar ----------------
def b_lembrete(c, t, C, b):
    a2, b2, c2, d2, e2 = (C[f"s02.{k}"] for k in "abcde")
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 84), XE, 220, passo=0.12)
    itens = ((a2, "tabela de frequência"), (b2, "barras, linhas e setores"), (c2, "histograma"), (d2, "dupla entrada"))
    for i, (ti, s) in enumerate(itens):
        y = 360 + i * 120
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 22, 40, a=a), centro(c, str(i + 1), XE + 40, y - 3, 46, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, [(s, "g", 62)], XE + 110, y, "left", 0.1)
    x, w = 1180, 620
    p = ep(t, e2, 0.5)
    E.caixa_pontilhada(c, x, 380, w, 300, p, prog_=p)
    E.frase(c, t, e2 + 0.1, ps("em quase todas:", "i", 52), x + 40, 460, "left", 0.1)
    E.frase(c, t, e2 + 0.6, [("porcentagem", "g", 64, COR)], x + 40, 550, "left", 0.1)
    fcen(c, t, e2 + 1.2, "f{parte}{total}", x + w / 2, 640, 62, TINTA2)
    E.frase(c, t, lerp(e2, C["s02.end"], 0.6), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- situação 1: barras ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s03.{k}"] for k in "abcd")
    situacao(c, t, a3, 1)
    E.frase(c, t, b3, ps("esporte preferido de", "i", 56), XE, 320, passo=0.1)
    E.frase(c, t, b3 + 1.0, [("50 pessoas", "g", 62, COR)], XE, 400, passo=0.1)
    E.frase(c, t, c3, ps("cada linha da grade vale", "i", 52) + [("2", "g", 64, COR)], XE, 530, passo=0.1)
    E.frase(c, t, d3, ps("quantas preferem", "i", 56) + [("vôlei?", "g", 60, COR)], XE, 680, passo=0.1)
    E.frase(c, t, d3 + 1.2, [("quantos %?", "g", 60, COR)], XE, 770, passo=0.1)

    def gr():
        esporte(c, t, b3, GQ1)
        if t >= c3:
            for k in (1, 2, 3):
                M.line(c, GQ1.x, GQ1.py(2 * k), GQ1.x + GQ1.w, GQ1.py(2 * k), E.COR, ep(t, c3 + 0.15 * k, 0.4), 4)
    E.saida(c, t, C["s04.a"] - 0.1, gr)
    E.relogio(c, t, C["s04.a"], 1440, 540, 200)


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    G = GR1
    esporte(c, t, -9, G)
    for k in range(1, 7):   # contar as linhas até a do vôlei
        yk = G.py(2 * k)
        E.foco(c, t, a5 + 0.25 * k, 0.3, lambda a, yk=yk, k=k: (c.drawCircle(G.x + G.w / 2, yk, 22, M.paint(E.COR, a)),
                                                               centro(c, str(k), G.x + G.w / 2, yk + 11, 30, "g", BR, a)))
    guia(c, t, b5, G, 1, 12)
    X = 1530

    def um():
        E.frase(c, t, a5, ps("vôlei: na", "i", 56) + [("6ª linha", "g", 60, COR)], X, 260, "center", 0.1)
        E.frase(c, t, lerp(a5, b5, 0.5), ps("6 pessoas?", "i", 52, ERRADO), X, 360, "center", 0.1)
        fcen(c, t, b5, "6 · 2 = 12", X, 500, 84, COR)
    fase(c, t, C["s05"], c5 - 0.1, um)
    if t < c5 - 0.1:
        return
    E.frase(c, t, c5, ps("o atalho:", "i", 52, TINTA2), X, 240, "center", 0.1)
    E.frase(c, t, c5 + 0.6, ps("o total vira", "i", 56) + [("100", "g", 62, COR)], X, 330, "center", 0.1)
    fcen(c, t, c5 + 1.4, "50 · 2 = 100", X, 480, 70)
    fcen(c, t, d5, "12 · 2 = 24", X, 620, 70, COR)
    bola_txt(c, t, e5, "24%", X, 820, 110, 76)


# ---------------- situação 2: linhas ----------------
def b_questao2(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    situacao(c, t, a6, 2)
    E.frase(c, t, b6, ps("o", "i", 56) + [("público", "g", 62, COR)] + ps("de um cinema", "i", 56), XE, 320, passo=0.1)
    E.frase(c, t, b6 + 1.2, ps("de janeiro a maio", "i", 52, TINTA2), XE, 400, passo=0.1)
    E.frase(c, t, d6, ps("a", "i", 56) + [("maior alta?", "g", 60, COR)], XE, 600, passo=0.1)
    E.frase(c, t, d6 + 1.2, ps("de quantos", "i", 56) + [("%?", "g", 60, COR)], XE, 690, passo=0.1)
    E.saida(c, t, C["s07.a"] - 0.1, lambda: cinema(c, t, c6 - 0.6, GQ2, max(1.0, (d6 - c6) * 0.9)))
    E.relogio(c, t, C["s07.a"], 1440, 540, 200)


def b_resposta2(c, t, C, b):
    a8, b8, c8, d8, e8, f8 = (C[f"s08.{k}"] for k in "abcdef")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    G = GR2
    cinema(c, t, -9, G, 1.0, 40)
    variacoes(c, t, [a8, b8, c8, d8], G, CINE, off={1: (-40, 0), 3: (40, 150)})
    trecho(c, t, e8, G, CINE, 2)
    anel(c, t, f8, G.pt(4, 500), 34, TINTA2)
    X = 1570

    def um():
        fcen(c, t, a8, "jan → fev: +60", X, 280, 52)
        fcen(c, t, b8, "fev → mar: desce", X, 380, 52, TINTA2)
        fcen(c, t, c8, "mar → abr: +160", X, 480, 52, COR)
        fcen(c, t, d8, "abr → mai: +20", X, 580, 52)
        E.foco(c, t, e8, 0.5, lambda a: E.pilula(c, "maior alta: mar → abr", X, 720, 48, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, f8, ps("maio: maior público,", "i", 46, TINTA2), X, 850, "center", 0.08)
        E.frase(c, t, f8 + 0.9, ps("não a maior alta", "i", 46, TINTA2), X, 915, "center", 0.08)
    fase(c, t, C["s08"], C["s09"] - 0.1, um)
    if t < C["s09"] - 0.1:
        return
    E.frase(c, t, C["s09"] + 0.1, ps("a alta em", "i", 60) + [("%", "g", 66, COR)], X, 260, "center", 0.1)
    fcen(c, t, a9, "f{diferença}{valor de antes}", X, 420, 68)
    fcen(c, t, b9, "160 ÷ 320 = 0,5", X, 600, 66)
    bola_txt(c, t, c9, "50%", X, 790, 110, 74)
    E.frase(c, t, c9 + 0.6, ps("160 é a metade de 320", "i", 44, TINTA2), X, 970, "center", 0.08)


# ---------------- situação 3: setores ----------------
PQX, PQY, PQR = 1440, 560, 260
PRX, PRY, PRR = 560, 570, 290


def b_questao3(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    situacao(c, t, a0, 3)
    E.frase(c, t, b0, ps("despesas de uma família", "i", 56), XE, 320, passo=0.1)
    E.frase(c, t, b0 + 1.4, [("R$ 3.000", "g", 62, COR)] + ps("por mês", "i", 56), XE, 400, passo=0.1)
    E.frase(c, t, c0, ps("aluguel:", "i", 56) + [("108°", "g", 62, COR)], XE, 560, passo=0.1)
    E.frase(c, t, d0, ps("quantos", "i", 56) + [("reais?", "g", 60, COR)], XE, 700, passo=0.1)

    def pz():
        despesas(c, t, b0, PQX, PQY, PQR)
        ang_centro(c, t, c0, PQX, PQY, -90, 108, "108°", BR, 60, PQR * 0.6, 54)
    E.saida(c, t, C["s11.a"] - 0.1, pz)
    E.relogio(c, t, C["s11.a"], 1440, 540, 200)


def b_resposta3(c, t, C, b):
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    despesas(c, t, -9, PRX, PRY, PRR)
    for k in range(1, 3):   # as 3 fatias de 36° dentro dos 108°
        ux, uy = _u(-90 + 36 * k)
        M.line(c, PRX + ux * PRR * 0.3, PRY + uy * PRR * 0.3, PRX + ux * PRR, PRY + uy * PRR, BR, ep(t, b2 + 0.2 * k, 0.4), 4, dash=E.TRACO)
    ang_centro(c, t, -9, PRX, PRY, -90, 108, "108°", BR, 60, PRR * 0.72, 56)
    X = 1500

    def um():
        E.frase(c, t, a2, ps("atalho:", "i", 56) + [("10% = 36°", "g", 62, COR)], X, 260, "center", 0.1)
        fcen(c, t, b2, "108 = 3 · 36", X, 420, 70)
        E.frase(c, t, b2 + 1.2, ps("→", "i", 56) + [("30%", "g", 66, COR)], X, 510, "center", 0.1)
        fcen(c, t, c2, "10% de 3.000 = 300", X, 650, 58)
        fcen(c, t, d2, "300 · 3 = 900", X - 140, 820, 64)
        bola_txt(c, t, d2 + 0.6, "R$ 900", X + 230, 800, 110, 50)
    fase(c, t, C["s12"], e2 - 0.1, um)
    if t < e2 - 0.1:
        return
    E.frase(c, t, e2, ps("pela conta direta:", "i", 52, TINTA2), X, 400, "center", 0.1)
    fcen(c, t, e2 + 0.6, "108 ÷ 360 = 0,3 = 30%", X, 540, 58)
    bola_txt(c, t, e2 + 1.4, "R$ 900", X, 760, 120, 54)


# ---------------- situação 4: histograma ----------------
def b_questao4(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    situacao(c, t, a3, 4)
    E.frase(c, t, b3, ps("minutos de espera na fila", "i", 54), XE, 320, passo=0.1)
    E.frase(c, t, b3 + 1.4, [("50 pessoas", "g", 62, COR)], XE, 400, passo=0.1)
    E.frase(c, t, d3, ps("20 minutos", "i", 56) + [("ou mais:", "g", 60, COR)], XE, 600, passo=0.1)
    E.frase(c, t, d3 + 1.2, [("quantos %?", "g", 62, COR)], XE, 690, passo=0.1)
    ts = [c3 + (d3 - c3) * k / 4 for k in range(4)]
    E.saida(c, t, C["s14.a"] - 0.1, lambda: espera(c, t, ts, HQ4, t0=b3))
    E.relogio(c, t, C["s14.a"], 1440, 540, 200)


def b_resposta4(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    G = HR4
    cores = [E.mix(E.COR, APAGADO, ep(t, b5, 0.4)) if i < 2 else None for i in range(4)]
    espera(c, t, [-9] * 4, G, cores, 40, -9)
    faixa(c, t, b5, G, 20, 40, "20 minutos ou mais", dy=160)
    X = 1560

    def um():
        E.frase(c, t, C["s15"] + 0.1, ps("na borda, o primeiro entra", "i", 50), X, 260, "center", 0.1)
        E.foco(c, t, a5, 0.5, lambda a: classe(20, 30)(c, X, 420, 100, COR, a))
        E.foco(c, t, a5 + 0.8, 0.4, lambda a: centro(c, "20 entra", X - 110, 510, 44, "g", CERTO, a))
        fcen(c, t, b5, "12 + 5 = 17", X, 680, 76)
        E.frase(c, t, b5 + 1.2, ps("pessoas", "i", 48, TINTA2), X, 760, "center", 0.1)
    fase(c, t, C["s15"], c5 - 0.1, um)
    if t < c5 - 0.1:
        return
    E.frase(c, t, c5, ps("total 50: vira", "i", 56) + [("100", "g", 62, COR)], X, 300, "center", 0.1)
    fcen(c, t, c5 + 0.8, "50 · 2 = 100", X, 440, 66)
    fcen(c, t, d5, "17 · 2 = 34", X, 600, 70, COR)
    bola_txt(c, t, d5 + 0.7, "34%", X, 800, 110, 76)


# ---------------- situação 5: dupla entrada ----------------
def b_questao5(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    situacao(c, t, a6, 5)
    E.frase(c, t, b6, ps("os", "i", 56) + [("aprovados", "g", 62, COR)] + ps("de um curso", "i", 56), XE, 320, passo=0.1)
    E.frase(c, t, e6, ps("qual turno teve a", "i", 56), XE, 640, passo=0.1)
    E.frase(c, t, e6 + 1.2, [("maior porcentagem", "g", 62, COR)] + ps("de aprovação?", "i", 56), XE, 730, passo=0.1)
    E.saida(c, t, C["s17.a"] - 0.1, lambda: aprovacao(c, t, b6, c6, d6, 1060, 380))
    E.relogio(c, t, C["s17.a"], 1440, 540, 200)


def b_resposta5(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    x0, y0, size = 150, 400, 62
    hl = size * 1.7
    for j, ti, t1 in ((0, a8, c8), (1, c8, C["s19"])):
        p = ep(t, ti, 0.4) * (1 - ep(t, t1, 0.4))
        if p > 0:
            yb = y0 + 20 + hl * (j + 1) - hl * 0.3
            M.rrect(c, x0 - 15, yb - size * 0.98, 850, size * 1.36, 14, E.mix(E.COR, PAPEL, 0.86), p)
    aprovacao(c, t, -9, -9, -9, x0, y0, size)
    X = 1440

    def um():
        E.frase(c, t, C["s18"] + 0.1, ps("cada turno tem o seu", "i", 52) + [("100%", "g", 58, COR)], X, 240, "center", 0.1)
        E.frase(c, t, a8, [("manhã:", "g", 60)], 1000, 420, "left", 0.1)
        E.foco(c, t, a8 + 0.3, 0.5, lambda a: E.fracao(c, "45", "60", 1290, 400, 84, TINTA, a))
        E.pontes(c, t, 1360, 1520, 400, 84, "÷ 15", b8 - 0.6, b8 - 0.3, size=34)
        E.foco(c, t, b8, 0.5, lambda a: E.fracao(c, "3", "4", 1580, 400, 84, COR, a))
        E.frase(c, t, b8 + 1.0, [("= 75%", "g", 62, COR)], 1640, 425, "left", 0.1)
        fcen(c, t, c8, "noite: 72 ÷ 120 = 0,6", X, 640, 60)
        E.frase(c, t, d8, [("= 60%", "g", 62, COR)], X, 740, "center", 0.1)
    fase(c, t, C["s18"], C["s19"] - 0.1, um)
    if t < C["s19"] - 0.1:
        return
    bola_txt(c, t, a9, "manhã", X, 330, 120, 50)
    E.frase(c, t, a9 + 0.6, [("75%", "g", 56, COR)] + ps("contra", "i", 50) + [("60%", "g", 56)], X, 520, "center", 0.1)
    E.frase(c, t, b9, ps("a noite tem mais aprovados:", "i", 46, TINTA2), X, 640, "center", 0.08)
    fcen(c, t, b9 + 1.2, "72 > 45", X, 720, 56, TINTA2)
    E.foco(c, t, c9, 0.5, lambda q: E.pilula(c, "pede %: a manhã ganha", X, 860, 50, "g", a=q, cor=E.SOBRE))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", ps("leia", "i", 62) + [("título, eixos e legenda", "g", 66, COR)] + ps("antes", "i", 62)),
                 ("s20.b", ps("ache o", "i", 62) + [("100%", "g", 66, COR)] + ps("de cada pergunta", "i", 62)),
                 ("s20.c", [("quantidade", "g", 66, COR)] + ps("ou", "i", 62) + [("porcentagem?", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 52, a=a), centro(c, str(i + 1), 200, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula, uma parte nova", "i", 76), XE, 250, passo=0.12)
    E.frase(c, t, a1, ps("a", "i", 84) + [("média aritmética", "g", 104, COR)], XE, 420)
    E.frase(c, t, b1, ps("a nota que falta para", "i", 60) + [("média 7", "g", 66, COR)], XE, 580, passo=0.1)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(960, 785, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
