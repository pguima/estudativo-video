"""Visual — Estudativo · MAT-EST-006: tabelas de dupla entrada, mapas e infográficos.
Mesma linguagem da Estatística definida em MAT-EST-001 (docstring de lá): tabela (quadro()) com cabeçalho em itálico fino,
fio embaixo, linha "total" depois do fio grosso, números na grotesca, célula da vez na cor da matéria; barra de 100%
(barra100()); conta da vez à direita; resposta na esfera; atalho no palco escuro.
Novo nesta aula (para copiar nas próximas):
- DUPLA ENTRADA = quadro() com a coluna "total" à direita e a linha "total" embaixo; a leitura é uma FAIXA CLARA na linha e
  outra na coluna (banda()), com o cursor de dedo, e um ANEL na célula do cruzamento (anel_cel()). Tab guarda a geometria.
  quadro() aceita tinta/tinta2 para o palco escuro.
- MAPA = bairros como polígonos (mapa()), pintados com 3 tons da matéria; LEGENDA em quadrinhos com a faixa de cada cor
  (legenda()), lida antes do mapa. Bairro da vez com contorno grosso.
- INFOGRÁFICO = casa com as pessoas dentro (casa()), o número grande com a unidade e a barra de 100% para a parte.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Estatística")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EST-006_tabelas_mapas_e_infograficos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dupla", "mapa", "info", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PAPEL = E.PAPEL
BANDA = E.mix(E.COR, PAPEL, 0.86)
TONS = [E.mix(E.COR, BR, 0.78), E.mix(E.COR, BR, 0.42), E.COR]     # legenda do mapa: claro, médio, escuro
T = [[120, 80], [100, 50], [140, 210]]                             # manhã, tarde, noite x presencial, a distância
LIN = [sum(r) for r in T]
COLT = [sum(r[k] for r in T) for k in range(2)]
assert LIN == [200, 150, 350] and COLT == [360, 340] and sum(LIN) == 700 == sum(COLT)
assert 210 / 700 == 0.3 and 210 / 350 == 0.6 and 350 - 140 == 210
assert 600 * 40 // 100 == 240 and 240 // 4 == 60
assert 60 + 90 == 150 and 200 - 50 == 150 and 150 / 200 == 0.75 and 150 + 200 == 350


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com %, ² ou → vai na grotesca)"""
    return [(w, "g" if any(ch in w for ch in "%²³→") else est, size * (0.92 if any(ch in w for ch in "%²³→") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def quadro(c, t, x, y, colunas, linhas, total=None, size=58, h_lin=None, cores=None, t_fio=None, tinta=TINTA, tinta2=TINTA2):
    """tabela de dados (MAT-EST-001), com tinta/tinta2 para o palco escuro. colunas = [(título, largura, t0)];
    linhas = [[(texto, t0[, cor]), ...], ...]; total = [(texto, t0[, cor]), ...] depois de um fio grosso"""
    h_lin = h_lin or size * 1.55
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
        E.foco(c, t, ti, 0.45, lambda a, tit=tit, cx=cx: centro(c, tit, cx, y - 6, size * 0.78, "i", tinta2, a))
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
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, yy=yy, cc=cc, k=k: centro(c, s, cx, yy, size, "b" if k == 0 else "g", cc[0] if cc else tinta, a))
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
            cx = xs[k] + colunas[k][1] / 2 + (22 if k == 0 and cores else 0)
            E.foco(c, t, ti, 0.4, lambda a, s=s, cx=cx, cc=cc, k=k: centro(c, s, cx, yy, size, "i" if k == 0 else "g", cc[0] if cc else tinta, a))
    return bases


def barra100(c, t, t0, x, y, w, h, partes, cores=None, rotulos=None, size=46, d=1.0, a=1.0):
    """frequência relativa (MAT-EST-001): barra deitada de 100% dividida nas fatias, com a % (ou o rótulo) dentro"""
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


# ================= peças da tabela de dupla entrada (copiar nas próximas aulas) =================
class Tab:
    """geometria do quadro(): x, y, larguras, número de linhas, size, h_lin; base(j) = linha de base da linha j (j = n: total)"""
    def __init__(self, x, y, ws, n, size, h_lin=None):
        self.x, self.y, self.ws, self.n, self.size = x, y, ws, n, size
        self.h = h_lin or size * 1.55
        self.xs = [x]
        for w in ws:
            self.xs.append(self.xs[-1] + w)

    def base(self, j):
        if j < self.n:
            return self.y + 20 + self.h * (j + 1) - self.h * 0.3
        return self.y + 20 + self.h * self.n + 8 + self.h * 0.72

    def cx(self, k):
        return (self.xs[k] + self.xs[k + 1]) / 2

    def cy(self, j):
        return self.base(j) - self.size * 0.36


def banda(c, t, t0, G, linha=None, coluna=None, cor=BANDA, t1=None):
    """faixa clara atrás de uma linha ou de uma coluna inteira (desenhe antes do quadro)"""
    p = ep(t, t0, 0.4) * (1 - ep(t, t1, 0.4) if t1 is not None else 1)
    if p <= 0:
        return
    if linha is not None:
        y = G.base(linha) - G.size * 0.98
        w = (G.xs[-1] - G.x + 30) * ease_io(prog(t, t0, 0.5))
        M.rrect(c, G.x - 15, y, w, G.size * 1.36, 14, cor, p)
    if coluna is not None:
        y0 = G.y - G.size * 0.78 - 26
        y1 = G.base(G.n) + G.size * 0.42
        hh = (y1 - y0) * ease_io(prog(t, t0, 0.5))
        M.rrect(c, G.xs[coluna] + 8, y0, G.ws[coluna] - 16, hh, 14, cor, p)


def anel_cel(c, t, t0, G, j, k, cor=None, t1=None, lw=7):
    """anel em volta da célula (linha j, coluna k)"""
    q = ease_back(prog(t, t0, 0.45)) * (1 - ep(t, t1, 0.4) if t1 is not None else 1)
    if q <= 0:
        return
    rx, ry = G.ws[k] * 0.36, G.size * 0.72
    cx, cy = G.cx(k), G.cy(j)
    c.drawOval(skia.Rect.MakeLTRB(cx - rx * q, cy - ry * q, cx + rx * q, cy + ry * q), M.paint(cor or E.COR, min(1, q), stroke=lw))


# ---------------- a tabela do curso ----------------
GT = Tab(110, 360, [300, 300, 340, 240], 3, 58, 96)
TURNOS = ["manhã", "tarde", "noite"]


def curso(c, t, tr=None, tc=None, tt=None, cor_cel=None, vazio=None, tinta=TINTA, tinta2=TINTA2, G=GT):
    """a tabela dos inscritos; tr = instante dos turnos, tc = das colunas e células, tt = dos totais.
    cor_cel = {(j, k): cor}; vazio = (j, k) com '?' no lugar do número"""
    tr = -9 if tr is None else tr
    tc = -9 if tc is None else tc
    tt = -9 if tt is None else tt
    cor_cel = cor_cel or {}
    cols = [("", G.ws[0], tr), ("presencial", G.ws[1], tc), ("a distância", G.ws[2], tc + 0.3), ("total", G.ws[3], tt)]
    linhas = []
    for j in range(3):
        lin = [(TURNOS[j], tr + 0.3 * j)]
        for k in range(2):
            s = "?" if vazio == (j, k) else str(T[j][k])
            lin.append((s, tc + 0.3 * k + 0.15 * j, cor_cel.get((j, k), (COR if tinta == TINTA else "#FFD500") if vazio == (j, k) else tinta)))
        lin.append((str(LIN[j]), tt + 0.15 * j, cor_cel.get((j, 2), tinta)))
        linhas.append(lin)
    total = [("total", tt), (str(COLT[0]), tt + 0.2, cor_cel.get((3, 0), tinta)), (str(COLT[1]), tt + 0.3, cor_cel.get((3, 1), tinta)),
             ("700", tt + 0.4, cor_cel.get((3, 2), tinta))]
    return quadro(c, t, G.x, G.y, cols, linhas, total, G.size, G.h, t_fio=tr, tinta=tinta, tinta2=tinta2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a1, ps("dos alunos da", "i", 58) + [("noite,", "g", 62, COR)] + ps("quantos % estudam", "i", 58) + [("a distância?", "g", 62, COR)],
                W / 2, 180, "center", 0.08)
        banda(c, t, c1 - 0.3, GT, linha=2)
        curso(c, t, b1, b1 + 0.4, b1 + 0.8)
        X = 1620
        E.foco(c, t, c1, 0.5, lambda a: E.selo(c, X - 150, 470, 46, False, a))
        E.foco(c, t, c1 + 0.1, 0.5, lambda a: E.escreve(c, "30%?", X - 80, 505, 100, "g", ERRADO, a))
        E.frase(c, t, c1 + 0.8, ps("muita gente responde", "i", 44, TINTA2), X, 580, "center", 0.08)
        bola_txt(c, t, d1, "60%", X, 790, 130, 84)
        E.frase(c, t, d1 + 0.5, [("o certo", "g", 50, CERTO)], X, 970, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 600, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 88), XE, 260, passo=0.14)
        E.frase(c, t, ta + 1.4, ps("cruzar", "i", 80) + [("linha e coluna", "g", 92, COR)], XE, 400, passo=0.14)
        E.frase(c, t, ta + 3.0, ps("a", "i", 80) + [("legenda", "g", 92, COR)] + ps("de um mapa", "i", 80), XE, 530, passo=0.14)
        E.frase(c, t, ta + 5.0, ps("o dado certo do", "i", 80) + [("infográfico", "g", 92, COR)], XE, 660, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 575, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 660, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 980, 820
    itens = (("s03.b", "a tabela de frequência,", "com o total no fim"), ("s03.c", "ler a pergunta antes:", "só os números úteis"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 90, "left", 0.1)
        E.frase(c, t, C[k] + 0.8, [(l2, "g", 52, COR)], x + w - 60, y + 170, "right", 0.1)
    alvo = [240 + i * 280 + 200 for i in range(2)]
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(alvo[0], alvo[1], q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54), x, 900, "left", 0.1)


# ---------------- dupla entrada ----------------
def b_dupla(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    s5, s6 = C["s05"], C["s06"]
    # faixas atrás da tabela
    banda(c, t, d4, GT, linha=3, t1=s5 - 0.2)
    banda(c, t, d4, GT, coluna=3, t1=s5 - 0.2)
    banda(c, t, b5, GT, linha=2, t1=s6)
    banda(c, t, c5, GT, coluna=2, t1=s6)
    banda(c, t, a6, GT, linha=2, t1=b6)
    banda(c, t, b6, GT, coluna=2, t1=c6)
    vez = {}
    if s5 <= t < s6 and t >= d5:
        vez[(2, 1)] = COR
    if a6 <= t < b6:
        vez[(2, 2)] = COR
    if b6 <= t < c6:
        vez[(3, 1)] = COR
    if t >= c6:
        vez[(3, 2)] = COR
    curso(c, t, b4, c4, d4, vez)
    anel_cel(c, t, d5, GT, 2, 2, t1=s6)
    anel_cel(c, t, c6, GT, 3, 3)
    if s5 <= t < s6 + 0.4:   # os dedos
        q1 = ease_io(prog(t, b5, 0.5))
        E.cursor(c, lerp(GT.x - 60, GT.xs[1] - 30, q1), GT.cy(2) + 16, ep(t, b5, 0.4) * (1 - ep(t, s6, 0.3)))
        E.cursor(c, GT.cx(2) + 10, lerp(GT.y - 200, GT.y - 105, ease_io(prog(t, c5, 0.5))), ep(t, c5, 0.4) * (1 - ep(t, s6, 0.3)))
    X = 1600

    def um():
        E.frase(c, t, a4, ps("cada número depende de", "i", 50), X, 260, "center", 0.08)
        E.frase(c, t, a4 + 1.4, [("2 coisas", "g", 66, COR)], X, 350, "center", 0.1)
        E.frase(c, t, b4, ps("linhas:", "i", 54) + [("turnos", "g", 58, COR)], X, 500, "center", 0.1)
        E.frase(c, t, c4, ps("colunas:", "i", 54), X, 600, "center", 0.1)
        E.frase(c, t, c4 + 0.5, [("jeito de estudar", "g", 58, COR)], X, 670, "center", 0.1)
        E.frase(c, t, d4, ps("última linha e coluna:", "i", 50), X, 760, "center", 0.1)
        E.frase(c, t, d4 + 1.0, [("os totais", "g", 60, COR)], X, 840, "center", 0.1)
    fase(c, t, C["s04"], s5 - 0.1, um)

    def dois():
        E.frase(c, t, a5, [("cruze", "g", 66, COR)] + ps("linha e coluna", "i", 60), X, 260, "center", 0.1)
        E.frase(c, t, lerp(a5, b5, 0.5), ps("noite, a distância?", "i", 52, TINTA2), X, 360, "center", 0.1)
        E.frase(c, t, b5, ps("dedo na", "i", 48) + [("linha", "g", 52, COR)] + ps("da noite", "i", 48), X, 500, "center", 0.1)
        E.frase(c, t, c5, ps("dedo na", "i", 48) + [("coluna", "g", 52, COR)] + ps("a distância", "i", 48), X, 600, "center", 0.1)
        bola_txt(c, t, d5, "210", X, 790, 120, 76)
        E.frase(c, t, d5 + 0.5, ps("alunos", "i", 48, TINTA2), X, 960, "center", 0.1)
    fase(c, t, s5, s6 - 0.1, dois)
    if t < s6 - 0.1:
        return
    E.frase(c, t, s6 + 0.1, ps("e os totais?", "i", 60), X, 260, "center", 0.1)
    E.frase(c, t, a6, ps("linha da noite:", "i", 50, TINTA2), X, 400, "center", 0.1)
    fcen(c, t, a6 + 0.5, "140 + 210 = 350", X, 480, 62)
    E.frase(c, t, b6, ps("coluna a distância:", "i", 50, TINTA2), X, 610, "center", 0.1)
    fcen(c, t, b6 + 0.5, "80 + 50 + 210 = 340", X, 690, 54)
    E.frase(c, t, c6, ps("total geral:", "i", 54) + [("700", "g", 62, COR)], X, 860, "center", 0.1)


# ================= peças do mapa (copiar nas próximas aulas) =================
BAIRROS = [   # nome, polígono, tom (0 claro, 1 médio, 2 escuro)
    ("Norte", [(260, 300), (620, 260), (900, 320), (820, 480), (560, 470), (420, 450), (300, 440)], 2),
    ("Oeste", [(300, 440), (420, 450), (440, 640), (380, 800), (230, 760), (210, 560)], 1),
    ("Centro", [(420, 450), (560, 470), (820, 480), (760, 650), (600, 700), (440, 640)], 1),
    ("Leste", [(820, 480), (900, 320), (1010, 450), (1000, 700), (900, 800), (760, 650)], 2),
    ("Sul", [(440, 640), (600, 700), (760, 650), (900, 800), (700, 900), (480, 880), (380, 800)], 0),
]
assert [tom for *_, tom in BAIRROS].count(2) == 2 and [tom for *_, tom in BAIRROS].count(1) == 2


def _poli(pts, dx=0, dy=0, k=1.0, cx=0, cy=0):
    p = skia.Path()
    for i, (x, y) in enumerate(pts):
        x, y = cx + (x - cx) * k + dx, cy + (y - cy) * k + dy
        p.moveTo(x, y) if i == 0 else p.lineTo(x, y)
    p.close()
    return p


def _centro(pts):
    return sum(x for x, _ in pts) / len(pts), sum(y for _, y in pts) / len(pts)


def mapa(c, t, t0, tcor=None, destaque=(), cor_dest=TINTA, nomes=True, a=1.0):
    """os bairros: entram em cinza no t0 e ganham a cor da legenda no tcor; destaque = {índice: t} com contorno grosso"""
    for i, (nome, pts, tom) in enumerate(BAIRROS):
        q = ep(t, t0 + 0.12 * i, 0.4) * a
        if q <= 0:
            continue
        cor = E.mix(E.mix(FIO, PAPEL, 0.3), TONS[tom], ep(t, tcor + 0.1 * i, 0.5)) if tcor is not None else E.mix(FIO, PAPEL, 0.3)
        path = _poli(pts)
        c.drawPath(path, M.paint(cor, q))
        sep = M.paint(PAPEL, q, stroke=8)
        sep.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, sep)
        if nomes:
            cx, cy = _centro(pts)
            tinta = BR if tcor is not None and t >= tcor + 0.1 * i + 0.25 and M.lum(TONS[tom]) < 0.5 else TINTA
            centro(c, nome, cx, cy + 14, 38, "b", tinta, q)
    for i, td in dict(destaque).items():
        q = ep(t, td, 0.4) * a
        if q > 0:
            pt = M.paint(cor_dest, q, stroke=9)
            pt.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(_poli(BAIRROS[i][1]), pt)


LEG = ["de 0 a 40%", "de 40 a 70%", "de 70 a 100%"]


def legenda(c, t, t0, ts, x, y, size=46, vez=None, a=1.0):
    """o quadrinho da legenda: um quadrado de cor e a faixa ao lado, cada linha no seu instante; vez = linha acesa"""
    p = ep(t, t0, 0.5) * a
    if p > 0:
        E.caixa_pontilhada(c, x, y, 560, 330, p, prog_=p)
        E.foco(c, t, t0 + 0.2, 0.4, lambda q: E.escreve(c, "legenda", x + 30, y - 22, 46, "g", COR, q * a))
    for i, ti in enumerate(ts):
        yy = y + 70 + 95 * i
        def fn(q, i=i, yy=yy):
            M.rrect(c, x + 40, yy - 34, 90, 64, 10, TONS[i], q * a)
            E.escreve(c, LEG[i], x + 160, yy + size * 0.36, size, "g" if vez == i else "b", COR if vez == i else TINTA, q * a)
        E.foco(c, t, ti, 0.4, fn)


# ---------------- mapa ----------------
def b_mapa(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    s9 = C["s09"]
    dest = {}
    if a9 <= t < b9:
        dest = {0: a9, 3: a9 + 0.2}
    elif b9 <= t < d9:
        dest = {2: b9}
    mapa(c, t, b7, c7, dest, E.mix(TINTA, E.COR, 0.0))
    E.foco(c, t, a7, 0.4, lambda q: E.escreve(c, "mapa", 230, 220, 64, "g", COR, q))
    X = 1480
    vez = 2 if a9 <= t < b9 else 1 if c9 <= t < d9 else None
    if t >= C["s08"] - 0.1:
        legenda(c, t, a8, [b8, c8, d8], 1180, 370, vez=vez)

    def um():
        E.frase(c, t, b7, ps("os bairros de uma cidade", "i", 54), X, 400, "center", 0.1)
        E.frase(c, t, c7, ps("a cor diz:", "i", 54), X, 540, "center", 0.1)
        E.frase(c, t, c7 + 0.8, [("% das casas", "g", 60, COR)], X, 630, "center", 0.1)
        E.frase(c, t, c7 + 1.6, ps("com rede de esgoto", "i", 54), X, 710, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, um)
    if t < C["s08"] - 0.1:
        return

    def dois():
        E.frase(c, t, a8, ps("o segredo:", "i", 56) + [("a legenda", "g", 60, COR)], X, 220, "center", 0.1)
        E.frase(c, t, e8, ps("cada cor é", "i", 54) + [("uma faixa", "g", 58, COR)], X, 780, "center", 0.1)
        E.frase(c, t, e8 + 1.2, ps("como as classes da tabela", "i", 46, TINTA2), X, 860, "center", 0.08)
    fase(c, t, C["s08"], s9 - 0.1, dois)
    if t < s9 - 0.1:
        return

    def tres():
        E.frase(c, t, s9 + 0.1, ps("70% ou mais?", "i", 56), X, 220, "center", 0.1)
        E.frase(c, t, a9, ps("conte os escuros:", "i", 52), X - 80, 790, "center", 0.1)
        bola_txt(c, t, a9 + 0.5, "2", X + 230, 770, 70, 70)
    fase(c, t, s9, b9 - 0.1, tres)
    if t < b9 - 0.1:
        return
    E.frase(c, t, b9 - 0.6, ps("o Centro: quantos %?", "i", 54), X, 220, "center", 0.1)
    E.frase(c, t, b9, ps("a cor não dá o", "i", 50) + [("número exato", "g", 54, ERRADO)], X, 760, "center", 0.1)
    E.frase(c, t, c9, ps("só a faixa:", "i", 52) + [("de 40 a 70%", "g", 56, COR)], X, 850, "center", 0.1)
    E.foco(c, t, d9, 0.5, lambda q: E.pilula(c, "leia a legenda antes de tudo", X, 970, 46, "g", a=q, cor=E.SOBRE))


# ================= peças do infográfico (copiar nas próximas aulas) =================
def pessoa(c, cx, cy, s, cor, a=1.0):
    """bonequinho: cabeça e corpo arredondado"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.62, s * 0.3, M.paint(cor, a))
    M.rrect(c, cx - s * 0.42, cy - s * 0.25, s * 0.84, s * 0.95, s * 0.36, cor, a)


def casa(c, t, t0, cx, cy, w, h, n=4, cor=None):
    """a casa em traço grosso com n pessoas dentro, que entram uma a uma"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    cor = cor or E.COR
    path = skia.Path()
    path.moveTo(cx - w / 2, cy + h / 2); path.lineTo(cx - w / 2, cy - h * 0.1); path.lineTo(cx, cy - h / 2)
    path.lineTo(cx + w / 2, cy - h * 0.1); path.lineTo(cx + w / 2, cy + h / 2); path.close()
    c.drawPath(path, M.paint(BR, p))
    pt = M.paint(TINTA, p, stroke=8)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pt)
    for i in range(n):
        x = cx - w / 2 + w * (i + 0.5) / n
        E.foco(c, t, t0 + 0.3 + 0.15 * i, 0.4, lambda a, x=x: pessoa(c, x, cy + h * 0.2, w / n * 0.62, cor, a), sobe=10)


def gota(c, cx, cy, r, cor, a=1.0):
    p = skia.Path()
    p.moveTo(cx, cy - r * 1.6)
    p.cubicTo(cx + r * 0.4, cy - r * 0.9, cx + r, cy - r * 0.4, cx + r, cy + r * 0.1)
    p.cubicTo(cx + r, cy + r * 0.7, cx + r * 0.55, cy + r, cx, cy + r)
    p.cubicTo(cx - r * 0.55, cy + r, cx - r, cy + r * 0.7, cx - r, cy + r * 0.1)
    p.cubicTo(cx - r, cy - r * 0.4, cx - r * 0.4, cy - r * 0.9, cx, cy - r * 1.6)
    c.drawPath(p, M.paint(cor, a))


# ---------------- infográfico ----------------
def b_info(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    # o infográfico, à esquerda
    E.foco(c, t, a0, 0.4, lambda q: E.escreve(c, "infográfico", 160, 210, 64, "g", COR, q))
    casa(c, t, b0, 400, 470, 420, 340)
    E.foco(c, t, b0 + 0.8, 0.5, lambda q: (gota(c, 700, 420, 36, E.mix(E.COR, BR, 0.3), q),
                                           E.escreve(c, "600 L", 760, 450, 96, "g", TINTA, q),
                                           E.escreve(c, "por dia", 770, 510, 46, "i", TINTA2, q)))
    p = ep(t, b1, 0.5) * (1 - ep(t, c1, 0.4))
    if p > 0:
        E.caixa_pontilhada(c, 670, 340, 360, 210, p, None, prog_=p)
    barra100(c, t, [c0, c0 + 0.5], 160, 760, 860, 90, [40, 60], [E.COR, E.mix(FIO, PAPEL, 0.3)], ["banho 40%", ""], size=44)
    X = 1480

    def um():
        E.frase(c, t, a0, ps("números, desenhos e texto", "i", 54), X, 300, "center", 0.1)
        E.frase(c, t, b0, ps("casa com", "i", 54) + [("4 pessoas", "g", 58, COR)], X, 460, "center", 0.1)
        E.frase(c, t, b0 + 1.2, [("600 litros", "g", 58, COR)] + ps("por dia", "i", 54), X, 550, "center", 0.1)
        E.frase(c, t, c0, ps("o banho leva", "i", 54) + [("40%", "g", 58, COR)], X, 700, "center", 0.1)
    fase(c, t, C["s10"], C["s11"] - 0.1, um)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, a1, ps("cada pessoa, no banho,", "i", 52), X, 220, "center", 0.1)
    E.frase(c, t, a1 + 1.0, ps("por dia:", "i", 52) + [("quantos litros?", "g", 56, COR)], X, 300, "center", 0.1)
    E.frase(c, t, b1, ps("o dado: número e", "i", 50) + [("unidade", "g", 54, COR)], X, 430, "center", 0.1)
    E.frase(c, t, b1 + 1.6, ps("600 L = a casa toda, num dia", "i", 46, TINTA2), X, 500, "center", 0.08)
    fcen(c, t, c1, "40% de 600 = 240 L", X, 640, 60)
    E.frase(c, t, c1 + 1.4, ps("ainda a casa toda", "i", 46, ERRADO), X, 710, "center", 0.08)
    fcen(c, t, d1, "240 ÷ 4 = 60", X - 150, 880, 66)
    bola_txt(c, t, d1 + 0.6, "60 L", X + 230, 860, 100, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    s3 = C["s13"]
    banda(c, t, a3, GT, linha=2)
    curso(c, t, C["s12"] - 0.4, C["s12"] - 0.2, C["s12"])
    anel_cel(c, t, b2 - 0.6, GT, 2, 2, ERRADO if t < s3 else E.COR)
    anel_cel(c, t, b2, GT, 3, 3, ERRADO, t1=s3)
    anel_cel(c, t, b3, GT, 2, 3, E.COR)
    E.frase(c, t, a2, ps("dos alunos da", "i", 52) + [("noite,", "g", 56, COR)] + ps("quantos % a distância?", "i", 52), W / 2, 200, "center", 0.08)
    X = 1600

    def um():
        E.frase(c, t, C["s12"] + 0.2, [("erro comum:", "g", 62, ERRADO)], X, 360, "center", 0.1)
        fcen(c, t, b2, "210 ÷ 700", X, 520, 72, ERRADO)
        E.frase(c, t, b2 + 1.0, ps("divide pelo total geral", "i", 46, TINTA2), X, 600, "center", 0.08)
        E.foco(c, t, c2, 0.5, lambda q: E.selo(c, X - 130, 750, 50, False, q))
        E.foco(c, t, c2 + 0.1, 0.5, lambda q: E.escreve(c, "30%", X - 50, 790, 100, "g", ERRADO, q))
    fase(c, t, C["s12"], s3 - 0.1, um)
    if t < s3 - 0.1:
        return
    E.frase(c, t, a3, ps("só a", "i", 56) + [("noite:", "g", 60, COR)], X, 360, "center", 0.1)
    E.frase(c, t, b3, ps("total dela =", "i", 52) + [("350", "g", 58, COR)], X, 450, "center", 0.1)
    fcen(c, t, c3, "210 ÷ 350 = 0,6", X, 590, 64)
    bola_txt(c, t, d3, "60%", X, 760, 110, 74)
    E.foco(c, t, e3, 0.5, lambda q: E.pilula(c, "quem é o 100% aqui?", X, 950, 48, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
GP = Tab(110, 380, [300, 300, 340, 240], 3, 58, 96)
BANDA_P = E.mix(E.COR, "#07070F", 0.35)


def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5 = C["s15.a"], C["s15.b"]
    banda(c, t, b4, GP, linha=2, cor=BANDA_P)
    vazio = (2, 1) if c4 <= t < d4 + 0.6 else None
    cor_cel = {(2, 1): BR} if t >= d4 + 0.6 else {}
    curso(c, t, C["s14"], C["s14"] + 0.2, C["s14"] + 0.4, cor_cel, vazio, BR, CLARO, GP)
    if vazio and t >= c4:
        anel_cel(c, t, c4, GP, 2, 2, BR)
    X = 1580

    def um():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 64, CLARO), X, 200, "center", 0.1)
        E.frase(c, t, a4, ps("a tabela se", "i", 56, CLARO), X, 290, "center", 0.1)
        E.frase(c, t, a4 + 0.5, [("confere sozinha", "g", 60, BR)], X, 360, "center", 0.1)
        E.frase(c, t, b4, ps("cada linha soma", "i", 50, CLARO), X, 470, "center", 0.1)
        E.frase(c, t, b4 + 1.0, [("o total da linha", "g", 54, BR)], X, 540, "center", 0.1)
        E.frase(c, t, c4, ps("apagou um número?", "i", 52, CLARO), X, 660, "center", 0.1)
        E.frase(c, t, c4 + 1.0, [("total − as outras", "g", 56, BR)], X, 730, "center", 0.1)
        fcen(c, t, d4, "350 − 140 = 210", X, 860, 70, BR)
    fase(c, t, C["s14"], C["s15"] - 0.1, um)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, a5, ps("o total é só a", "i", 56, CLARO), X, 330, "center", 0.1)
    E.frase(c, t, a5 + 0.7, [("soma das partes", "g", 62, BR)], X, 410, "center", 0.1)
    E.foco(c, t, b5, 0.5, lambda q: E.selo(c, X - 200, 600, 44, False, q))
    E.frase(c, t, b5 + 0.1, ps("sem os totais:", "i", 52, CLARO), X - 130, 622, "left", 0.1)
    E.frase(c, t, b5 + 1.2, ps("não há de onde tirar", "i", 52, CLARO), X, 720, "center", 0.1)


# ---------------- questão ----------------
GQ = Tab(1050, 400, [220, 180, 200, 180], 2, 54, 92)


def leitura(c, t, t0, tm, tn, G=GQ, noite="?", cor_n=None, tinta=TINTA):
    cols = [("", G.ws[0], t0), ("lê", G.ws[1], t0 + 0.2), ("não lê", G.ws[2], t0 + 0.3), ("total", G.ws[3], t0 + 0.4)]
    linhas = [[("manhã", tm), ("60", tm + 0.2), ("90", tm + 0.5), ("150", tm + 1.2)],
              [("noite", tn), (noite, tn + 0.2, cor_n or COR), ("50", tn + 0.8), ("200", tn + 1.2)]]
    return quadro(c, t, G.x, G.y, cols, linhas, None, G.size, G.h, t_fio=t0, tinta=tinta)


def b_questao(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7 = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a6, ps("alunos que", "i", 58) + [("leem por gosto", "g", 62, COR)], XE, 300, passo=0.1)
    E.frase(c, t, a6 + 1.2, ps("em cada turno", "i", 58), XE, 380, passo=0.1)
    E.frase(c, t, a7, [("1)", "g", 58, COR)] + ps("quantos da noite leem?", "i", 56), XE, 600, passo=0.1)
    E.frase(c, t, b7, [("2)", "g", 58, COR)] + ps("entre os da noite,", "i", 56), XE, 710, passo=0.1)
    E.frase(c, t, b7 + 1.0, [("quantos %", "g", 60, COR)] + ps("leem?", "i", 56), XE + 70, 800, passo=0.1)
    E.saida(c, t, C["s18.a"] - 0.1, lambda: leitura(c, t, a6, b6, c6))
    E.relogio(c, t, C["s18.a"], 1440, 540, 200)


# ---------------- resposta ----------------
GR = Tab(110, 380, [240, 200, 220, 200], 2, 60, 110)


def b_resposta(c, t, C, b):
    a9, b9 = C["s19.a"], C["s19.b"]
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    banda(c, t, a0, GR, linha=1)
    leitura(c, t, -9, -9, -9, GR, "150" if t >= b9 else "?", COR)
    anel_cel(c, t, a0 + 0.6, GR, 1, 3)
    X = 1460

    def um():
        E.frase(c, t, C["s19"] + 0.1, [("1)", "g", 60, COR)] + ps("pelo atalho", "i", 56), X, 300, "center", 0.1)
        fcen(c, t, a9, "200 − 50 = 150", X, 470, 76)
        bola_txt(c, t, b9, "150", X, 680, 110, 70)
        E.frase(c, t, b9 + 0.5, ps("alunos da noite leem", "i", 48, TINTA2), X, 850, "center", 0.1)
    fase(c, t, C["s19"], C["s20"] - 0.1, um)
    if t < C["s20"] - 0.1:
        return
    E.frase(c, t, C["s20"] + 0.1, [("2)", "g", 60, COR)] + ps("só a noite:", "i", 56), X, 230, "center", 0.1)
    E.frase(c, t, a0, [("100% = 200", "g", 64, COR)], X, 330, "center", 0.1)
    fcen(c, t, b0, "150 ÷ 200 = 0,75", X, 480, 68)
    bola_txt(c, t, c0, "75%", X, 650, 100, 70)
    E.foco(c, t, d0, 0.5, lambda q: E.selo(c, X - 300, 870, 40, False, q))
    fcen(c, t, d0 + 0.2, "150 ÷ (150 + 200)", X + 30, 890, 50, ERRADO)
    E.frase(c, t, d0 + 1.2, ps("o total da escola: errado", "i", 44, TINTA2), X, 970, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s21.a", ps("cruze", "i", 60) + [("linha e coluna", "g", 66, COR)]),
                 ("s21.b", ps("leia a", "i", 60) + [("legenda", "g", 66, COR)] + ps("antes do mapa", "i", 60)),
                 ("s21.c", ps("confira a", "i", 60) + [("unidade", "g", 66, COR)] + ps("do infográfico", "i", 60)),
                 ("s21.d", ps("ache o", "i", 60) + [("100%", "g", 66, COR)] + ps("antes de dividir", "i", 60)))
        for i, (k, partes) in enumerate(itens):
            y = 370 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 200, y - 25, 50, a=a), centro(c, str(i + 1), 200, y - 4, 58, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 290, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, a2, [("prática", "g", 110, COR)] + ps("de tudo", "i", 90), XE, 410)
    xp = XE
    for i, s in enumerate(("tabelas", "barras", "linhas", "setores", "histogramas")):
        wp = E.larg(s, "g", 40) + 44
        E.foco(c, t, a2 + 1.2 + 0.5 * i, 0.4, lambda q, s=s, cx=xp + wp / 2: E.pilula(c, s, cx, 540, 40, "g", fundo=TINTA, a=q))
        xp += wp + 24
    E.frase(c, t, b2, ps("com", "i", 64) + [("porcentagens e variações", "g", 70, COR)], XE, 690, passo=0.12)
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1550, 300, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1680, p), lerp(620, 325, p), ep(t, c2 + 0.2, 0.4))
    E.frase(c, t, d2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dupla=b_dupla, mapa=b_mapa, info=b_info, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
