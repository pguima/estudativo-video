"""Short de engajamento (não é aula): "Quantos retângulos tem?" em 3 níveis. Vertical 1080x1920, 30 fps.
Mesmo formato dos Shorts 002 e 003: visual das questões de matemática (_ferramentas/matematica.py) em pé,
cores com função: âmbar = peça sozinha / largura, ciano = 2 peças / altura, menta = certo, coral = erro.
Nível 1: faixa com 4 pedaços → 4 + 3 + 2 + 1 = 10 (C) · o segredo: todo retângulo usa 2 linhas de pé e 2 deitadas
Nível 2: 3 colunas × 2 andares → largura 6 jeitos × altura 3 jeitos = 18 (A)
Chefão: grade 3 × 3 → 6 × 6 = 36 (B) · quadrado também é retângulo (só os quadrados dariam 14, a pegadinha)
As contagens foram conferidas por força bruta em conferir_contagens.py.

Sem a voz: sai final/..._sem_audio.mp4 na linha do tempo do roteiro.md (backup em trabalho/).
Com a voz em audio/voz_original.wav + audio/palavras.json: preencher GAPS/ANCORAS/CORRIGE (como no Short 003) e rodar de
novo: as animações são deformadas para a voz e a legenda usa os tempos reais das palavras.
Uso: python3 render_short.py [--stills t1,t2,...]"""
import json
import os
import subprocess
import sys
from pathlib import Path

os.environ["VIDEO_FORMATO"] = "vertical"          # antes de importar o motor
HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
from matematica import *  # noqa
from motor import W, H, FPS

# ---------------------------------------------------------------- linha do tempo (s) = a do roteiro.md
FALAS = [
    (0.0, 3.0, "Quantos retângulos tem aqui? Parece fácil."),
    (3.0, 7.5, "4, 8, 10 ou 12? Comenta a sua antes de ver!"),
    (7.5, 12.5, "Pausa e conta. Valendo!"),
    (12.5, 15.0, "Quem disse 4 contou só os pedaços."),
    (15.0, 17.5, "Juntando 2 vizinhos: mais 3."),
    (17.5, 19.5, "Juntando 3: mais 2."),
    (19.5, 21.5, "E o inteiro: mais 1."),
    (21.5, 24.5, "4 + 3 + 2 + 1 = 10. Letra C!"),
    (24.5, 30.0, "O segredo: todo retângulo usa 2 linhas de pé e 2 deitadas."),
    (30.0, 33.0, "Nível 2: e com 2 andares?"),
    (33.0, 36.5, "18, 9, 6 ou 12?"),
    (36.5, 39.5, "3 segundos!"),
    (39.5, 42.5, "Na largura, 6 jeitos."),
    (42.5, 45.0, "Na altura, 3 jeitos."),
    (45.0, 48.0, "6 vezes 3: 18! Letra A."),
    (48.0, 50.5, "Nível chefão: grade 3 por 3!"),
    (50.5, 54.0, "14, 36, 9 ou 30?"),
    (54.0, 57.0, "Valendo!"),
    (57.0, 61.5, "Largura: 6 jeitos. Altura: 6 jeitos. 6 vezes 6!"),
    (61.5, 64.5, "36! Letra B. Quadrado também é retângulo!"),
    (64.5, 69.5, "Quantos você acertou: 0, 1, 2 ou 3? Comenta! No próximo: quantos caminhos?"),
]
DUR_ROTEIRO = 69.5
DESTAQUE = {"retângulos": AMB, "fácil.": RED, "4": AMB, "3.": CYA, "2.": MNT, "1.": WHITE, "= 10.": MNT, "+ 3": CYA, "+ 3,": CYA, "+ 2,": MNT, "pedaços.": AMB, "Altura:": CYA, "36!": MNT,
            "+ 2": MNT, "+ 1": WHITE, "C!": MNT, "segredo:": AMB, "pé": AMB, "deitadas.": CYA, "andares?": AMB,
            "largura,": AMB, "altura,": CYA, "Largura:": AMB, "Altura:": CYA, "18!": MNT, "A.": MNT, "chefão:": RED,
            "36!": MNT, "B.": MNT, "Quadrado": CYA, "retângulo!": CYA, "caminhos?": CYA, "Comenta!": CYA}

# ---------------------------------------------------------------- sincronia com a narração gravada (quando chegar)
VOZ = HERE / "audio" / "voz_original.wav"
NARRACAO = HERE / "audio" / "narracao.wav"
# a voz veio sem as pausas: silêncio aberto depois de "Valendo!", de "deitadas." (o segredo respira), de "3 segundos!" e do
# 2º "Valendo!"
GAPS = [(9.60, 3.2), (27.60, 1.0), (34.60, 1.7), (49.50, 2.1)]   # (posição no áudio original, segundos de silêncio)
ANCORAS = [(0.0, 0.0), (3.0, 3.07), (7.5, 7.80), (12.5, 10.06), (15.0, 12.57), (17.5, 14.95), (19.5, 17.15),
           (21.5, 18.94), (22.4, 21.30), (24.5, 23.17), (25.4, 25.36), (26.5, 26.59), (30.0, 27.99), (33.0, 30.52),
           (36.5, 33.39), (39.5, 34.74), (42.5, 36.66), (45.0, 38.43), (46.0, 39.71), (48.0, 41.73), (50.5, 44.91),
           (54.0, 48.50), (57.0, 49.68), (59.1, 51.60), (61.0, 53.04), (62.0, 54.74), (62.9, 55.95), (64.5, 59.03),
           (67.1, 63.23), (69.5, 65.70)]                       # (tempo do roteiro, tempo no áudio original)
CORRIGE = {5.30: "12?", 19.00: "4", 20.74: "1", 7.20: "ver!", 9.02: "Valendo!", 11.84: "pedaços.", 13.34: "vizinhos:",
           17.46: "inteiro:", 21.30: "= 10.", 23.38: "segredo:", 28.28: "2:", 29.36: "2", 29.64: "andares?", 32.82: "12?",
           33.86: "segundos!", 39.74: "18!", 42.32: "chefão:", 44.26: "3!", 47.90: "30?", 48.58: "Valendo!",
           49.80: "Largura:", 51.70: "Altura:", 53.92: "6!", 54.74: "36!", 58.14: "retângulo!", 61.80: "3?",
           62.48: "Comenta!", 63.44: "próximo:", 64.24: "quantos", 64.44: "caminhos?"}  # {início da palavra: texto}
INICIO = {27.30: 28.00}                  # palavra que a transcrição começou cedo (engoliu o silêncio): {início: início real}
SOMA = {19.38, 20.04, 20.58}              # "mais" das contas: vira "+ 3" junto com o número seguinte
COM_VOZ = VOZ.exists() and (HERE / "audio" / "palavras.json").exists() and len(ANCORAS) > 2


def com_gaps(x):
    return x + sum(d for g, d in GAPS if x >= g)


_A = [(r, com_gaps(a)) for r, a in ANCORAS]
DUR = _A[-1][1]


def roteiro_t(t):
    """tempo real do vídeo -> tempo da linha do tempo do roteiro (as animações são escritas nela)"""
    for (r0, a0), (r1, a1) in zip(_A, _A[1:]):
        if t < a1 or (r1, a1) == _A[-1]:
            return r0 + (t - a0) * (r1 - r0) / (a1 - a0)


def _palavras():
    """[(texto, início, fim)] no tempo real. Sem voz: ritmo de Short a partir do início de cada fala."""
    if not COM_VOZ:
        out = []
        for t0, t1, s in FALAS:
            ws = s.split()
            passo = min(0.36, (t1 - t0 - 0.3) / len(ws))
            out += [(w, t0 + 0.1 + passo * k, t0 + 0.1 + passo * (k + 1)) for k, w in enumerate(ws)]
        return out
    ws = json.load(open(HERE / "audio" / "palavras.json", encoding="utf-8"))[0]["words"]
    out = [[CORRIGE.get(w["s"], w["w"]), INICIO.get(w["s"], w["s"]), w["e"]] for w in ws if CORRIGE.get(w["s"], w["w"]) != ""]
    i = 0
    while i < len(out) - 1:
        if out[i][1] in SOMA:
            out[i] = ["+ " + out[i + 1][0].rstrip(","), out[i][1], out[i + 1][2]]
            del out[i + 1]
        i += 1
    return [(w, com_gaps(s), com_gaps(e)) for w, s, e in out]


PALAVRAS = _palavras()

QX0, QX1, QY0, QY1 = 70, W - 70, 965, 1445          # quadro
QCX = W / 2
CAP_Y_V = 1540

# níveis: opções, certa e tempos (gancho, opções, contagem, revelação, total, fim)
N1 = dict(opc=[("A", "4"), ("B", "8"), ("C", "10"), ("D", "12")], certa="C",
          t_hook=0.0, t_opc=3.0, t_conta=7.5, dur_conta=5, t_rev=12.5, t_tot=21.5, t_fim=30.0)
N2 = dict(opc=[("A", "18"), ("B", "9"), ("C", "6"), ("D", "12")], certa="A",
          t_hook=30.0, t_opc=33.0, t_conta=36.5, dur_conta=3, t_rev=39.5, t_tot=46.0, t_fim=48.0)
N3 = dict(opc=[("A", "14"), ("B", "36"), ("C", "9"), ("D", "30")], certa="B",
          t_hook=48.0, t_opc=50.5, t_conta=54.0, dur_conta=3, t_rev=57.0, t_tot=62.0, t_fim=64.5)
T_1, T_2, T_3, T_4 = 12.5, 15.0, 17.5, 19.5          # nível 1: sozinhos, de 2, de 3, inteiro
T_ATALHO, T_CTA = 24.5, 64.5

# ---------------------------------------------------------------- geometria (px): grades de cols × rows casas
G1 = dict(cols=4, rows=1, x0=170.0, y0=445.0, cw=185.0, ch=280.0)      # faixa: casas em pé (não são quadrados)
G2 = dict(cols=3, rows=2, x0=180.0, y0=415.0, cw=240.0, ch=170.0)      # casas deitadas
G3 = dict(cols=3, rows=3, x0=255.0, y0=300.0, cw=190.0, ch=190.0)      # chefão: casas quadradas


def gx(G, i):
    return G["x0"] + i * G["cw"]


def gy(G, j):
    return G["y0"] + j * G["ch"]


def spans(n):
    """intervalos (a, b) de 0..n, os menores primeiro"""
    return [(i, i + d) for d in range(1, n + 1) for i in range(n - d + 1)]


def todos(G):
    """todos os retângulos (i0, i1, j0, j1), dos menores para o maior"""
    rs = [(i0, i1, j0, j1) for i0, i1 in spans(G["cols"]) for j0, j1 in spans(G["rows"])]
    return sorted(rs, key=lambda r: ((r[1] - r[0]) * (r[3] - r[2]), r[2], r[0]))


assert [len(todos(G)) for G in (G1, G2, G3)] == [10, 18, 36]


# ---------------------------------------------------------------- peças no estilo das questões, em pé
def header_v(c, s, a):
    if a > 0:
        text_mid(c, s, W / 2, 175, 40, "black", AMB, a, tracking=2)


def quadro(c, a):
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(QX0, QY0, QX1, QY1), 26, 26)
    c.drawRRect(r, paint(BG2, 0.55 * a))
    c.drawRRect(r, paint(CYA, 0.18 * a, stroke=2))


def neon(c, p, q, col, a, w=8, glow=0.5, u=1.0):
    if a <= 0 or u <= 0:
        return
    x1, y1 = p[0] + (q[0] - p[0]) * u, p[1] + (q[1] - p[1]) * u
    c.drawLine(p[0], p[1], x1, y1, blur_paint(col, glow * a, 10, stroke=w + 4))
    c.drawLine(p[0], p[1], x1, y1, paint(col, a, stroke=w, cap_round=True))


def figura(c, G, t, t0, a):
    """a grade: traço neon ciano com brilho, preenchimento bem leve, desenhada de cima/esquerda"""
    if a <= 0:
        return
    u = ep(t, t0 + 0.15, 0.9)
    x1, y1 = gx(G, G["cols"]), gy(G, G["rows"])
    c.drawRect(skia.Rect.MakeLTRB(G["x0"], G["y0"], x1, y1), paint(CYA, 0.07 * a))
    for i in range(G["cols"] + 1):
        neon(c, (gx(G, i), G["y0"]), (gx(G, i), y1), CYA, a, 8, 0.5, u)
    for j in range(G["rows"] + 1):
        neon(c, (G["x0"], gy(G, j)), (x1, gy(G, j)), CYA, a, 8, 0.5, u)


def ret(c, G, r, col, a, inset=12, width=9, fill=0.16):
    """um retângulo destacado (i0, i1, j0, j1): recuado para dentro, brilho + contorno"""
    if a <= 0:
        return
    i0, i1, j0, j1 = r
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(gx(G, i0) + inset, gy(G, j0) + inset, gx(G, i1) - inset,
                                                  gy(G, j1) - inset), 12, 12)
    c.drawRRect(rr, paint(col, fill * a))
    c.drawRRect(rr, blur_paint(col, 0.55 * a, 14, stroke=width + 6))
    c.drawRRect(rr, paint(col, a, stroke=width))


def regua(c, G, lado, s, col, a, n=None):
    """colchete de fora da grade marcando uma largura (lado "x", em cima) ou altura (lado "y", à esquerda)"""
    if a <= 0:
        return
    if lado == "x":
        p, q, d = (gx(G, s[0]) + 8, G["y0"] - 44), (gx(G, s[1]) - 8, G["y0"] - 44), (0, 18)
    else:
        p, q, d = (G["x0"] - 44, gy(G, s[0]) + 8), (G["x0"] - 44, gy(G, s[1]) - 8), (18, 0)
    neon(c, p, q, col, a, 10, 0.6)
    for e in (p, q):
        neon(c, e, (e[0] + d[0], e[1] + d[1]), col, a, 10, 0.6)
    if n is not None:
        if lado == "x":
            badge(c, str(n), (p[0] + q[0]) / 2, p[1] - 6, a, col, r=26)
        else:
            badge(c, str(n), p[0] - 6, (p[1] + q[1]) / 2, a, col, r=26)


def badge(c, s, cx, cy, a, bg=AMB, fg=None, r=30):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(bg, a))
    text_mid(c, s, cx, cy, r * 1.05, "black", fg or BG0, a)


def _blocos():
    """legenda em blocos de até 4 palavras: quebra na pontuação ou numa pausa da voz"""
    blocos, cur = [], []
    for k, (w_, s0, e0) in enumerate(PALAVRAS):
        cur.append(k)
        prox = PALAVRAS[k + 1][1] if k + 1 < len(PALAVRAS) else DUR
        if k + 1 < len(PALAVRAS) and PALAVRAS[k + 1][0][:1] in "+=":       # a conta fica inteira num bloco
            continue
        if len(cur) >= 4 or (w_[-1] in ":," and len(cur) >= 2) or prox - e0 > 0.45 or w_[-1] in ".!?":
            blocos.append(cur); cur = []
    if cur:
        blocos.append(cur)
    out = []
    for n, b in enumerate(blocos):
        ini = PALAVRAS[b[0]][1] - 0.08
        fim = PALAVRAS[b[-1]][2] + 0.7
        if n + 1 < len(blocos):
            fim = min(fim, PALAVRAS[blocos[n + 1][0]][1] - 0.08)
        out.append((ini, fim, b))
    return out


BLOCOS = _blocos()


def legenda(c, t):
    """faixa escura curta (estilo matematica.CAPTION): a palavra que está sendo dita em âmbar"""
    for s0, e, ch in BLOCOS:
        if s0 <= t < e:
            break
    else:
        return
    size, sp = 54, 15
    ws = [PALAVRAS[k][0] for k in ch]
    tot = sum(text_w(w_, "extrabold", size) for w_ in ws) + sp * (len(ws) - 1)
    k_ = ease_out(clamp((t - s0) / 0.14)) * (1 - prog(t, e - 0.12, 0.12))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(W / 2 - tot / 2 - 28, CAP_Y_V - size * 0.9, tot + 56, size * 1.8), 18, 18)
    c.drawRRect(r, paint(BG0, 0.72 * k_))
    x = W / 2 - tot / 2
    f = font("extrabold", size)
    for k, w_ in zip(ch, ws):
        falando = PALAVRAS[k][1] - 0.05 <= t < PALAVRAS[k][2] + 0.05
        col = AMB if falando else (CYA if w_ in DESTAQUE else WHITE)
        c.drawString(w_, x, CAP_Y_V + size * 0.36, f, paint(col, k_))
        x += text_w(w_, "extrabold", size) + sp


# ---------------------------------------------------------------- blocos comuns aos níveis
def opcoes(c, N, t, y0=1300, t_out=None):
    ok = ep(t, N["t_tot"] + 0.9, 0.4)
    for k, (L, v) in enumerate(N["opc"]):
        a = ep(t, N["t_opc"] + 0.25 * k, 0.3) * (1 - prog(t, (t_out or N["t_fim"]) - 0.3, 0.3))
        if a <= 0:
            continue
        x = QX0 + 120 + (k % 2) * 460
        y = y0 + (k // 2) * 96 + (1 - ease_back(clamp(prog(t, N["t_opc"] + 0.25 * k, 0.4)))) * 20
        certo = L == N["certa"]
        dim = 1 - 0.55 * ok * (not certo)
        if certo and ok > 0:
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 46, y - 42, 340, 84), 18, 18)
            c.drawRRect(r, blur_paint(MNT, 0.3 * ok, 22))
            c.drawRRect(r, paint(BG1, 0.95 * ok))
            c.drawRRect(r, paint(MNT, ok, stroke=4))
        badge(c, L, x, y, a * dim, MNT if (certo and ok > 0.5) else AMB, r=28)
        text(c, v, x + 50, y + 23, 64, "black", MNT if (certo and ok > 0.5) else WHITE, a * dim, align="left")
        if ok > 0 and not certo:
            strike(c, x + 44, x + 50 + text_w(v, "black", 64) + 6, y, a, ok)
        if certo and ok > 0:
            check(c, x + 250, y, 24, ok)


def contagem(c, N, t):
    t0, d = N["t_conta"], N["dur_conta"]
    if not (t0 - 0.1 <= t < t0 + d + 0.3):
        return
    a = ep(t, t0, 0.3) * (1 - prog(t, t0 + d - 0.1, 0.3))
    u = clamp((t - t0) / d)
    n = max(1, d - int(t - t0))
    cx, cy, r = QCX, QY0 + 140, 80
    c.drawCircle(cx, cy, r, paint(INK2, 0.2 * a, stroke=12))
    arc = skia.Path(); arc.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * (1 - u))
    c.drawPath(arc, blur_paint(AMB, 0.5 * a, 10, stroke=16))
    c.drawPath(arc, paint(AMB, a, stroke=12, cap_round=True))
    k = 1 + 0.3 * (1 - ease_out(clamp(((t - t0) % 1.0) / 0.25)))
    text_mid(c, str(n), cx, cy, 80 * k, "black", WHITE, a)


def placar(c, linhas, t, t_out, y0=QY0 + 66, dy=68, x_seta=320):
    """linhas: (rótulo, total, cor, t0, passo) — badge âmbar, rótulo, contador que corre, ✓ ao completar"""
    a_all = 1 - prog(t, t_out, 0.3)
    for k, (nome, tot, col, t0, passo) in enumerate(linhas):
        a = ep(t, t0, 0.25) * a_all
        if a <= 0:
            continue
        y = y0 + k * dy
        badge(c, str(k + 1), QX0 + 90, y, a, r=26)
        text_mid(c, nome, QX0 + 136, y, 46, "black", col, a, align="left")
        n = min(tot, int(max(0.0, t - t0) / passo) + 1)
        text_mid(c, "→", QX0 + x_seta, y, 42, "black", INK2, a)
        text_mid(c, str(n), QX0 + x_seta + 80, y, 54, "black", WHITE if n < tot else col, a)
        if t >= t0 + passo * tot:
            check(c, QX1 - 90, y, 24, ep(t, t0 + passo * tot, 0.3) * a_all)


def gancho(c, N, t, partes, sub=None):
    a = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3))
    if a <= 0:
        return
    eq(c, partes, QY0 + 95, a, size=64, cx=QCX, maxw=880)
    if sub:
        label(c, sub, QCX, QY0 + 175, ep(t, N["t_hook"] + 0.5, 0.3) * (1 - prog(t, N["t_opc"] + 1.0, 0.3)), 34, INK2)


def selo_torto(c, s, t, t0, t_out, x):
    k = pop(t, t0, 0.4) * (1 - prog(t, t_out, 0.3))
    if k > 0:
        c.save(); c.translate(x, QY0 + 2); c.rotate(-5); c.scale(k, k)
        pill(c, s, 0, 0, 30, RED, WHITE, 1)
        c.restore()


def piscando(c, G, rs, t, t0, passo, col, fim, **kw):
    """destaca os retângulos um de cada vez; o último fica até `fim`"""
    for q, r in enumerate(rs):
        tq = t0 + passo * q
        a = ep(t, tq, 0.08) * (1 - prog(t, fim if q == len(rs) - 1 else tq + passo * 0.92, 0.08))
        ret(c, G, r, col, a, **kw)


def larg_alt(c, G, t, t0, passo, t1, passo1, fim):
    """largura: cada intervalo de colunas (faixa âmbar + colchete em cima); depois altura: os de linhas (ciano, à esquerda)"""
    sx, sy = spans(G["cols"]), spans(G["rows"])
    for q, s in enumerate(sx):
        tq = t0 + passo * q
        a = ep(t, tq, 0.08) * (1 - prog(t, (t1 - 0.1) if q == len(sx) - 1 else tq + passo * 0.92, 0.08))
        ret(c, G, (s[0], s[1], 0, G["rows"]), AMB, a, inset=6, width=5, fill=0.13)
        regua(c, G, "x", s, AMB, a, q + 1)
    for q, s in enumerate(sy):
        tq = t1 + passo1 * q
        a = ep(t, tq, 0.08) * (1 - prog(t, fim if q == len(sy) - 1 else tq + passo1 * 0.92, 0.08))
        ret(c, G, (0, G["cols"], s[0], s[1]), CYA, a, inset=6, width=5, fill=0.13)
        regua(c, G, "y", s, CYA, a, q + 1)


# ---------------------------------------------------------------- nível 1 (faixa com 4 pedaços)
def nivel1(c, t):
    N, G = N1, G1
    if t >= N["t_fim"] + 0.3:
        return
    ga = 1 - prog(t, N["t_fim"] - 0.3, 0.3)
    figura(c, G, t, N["t_hook"], ga * (1 - 0.6 * ep(t, T_ATALHO + 0.3, 0.3)))     # no segredo, a grade apaga um pouco
    out = 1 - prog(t, N["t_tot"], 0.4)
    if T_1 <= t < N["t_tot"] + 0.4:            # sozinhos: acendem e ficam, numerados
        for k in range(4):
            a = ep(t, T_1 + 0.3 + 0.5 * k, 0.2) * (1 - 0.7 * prog(t, T_2, 0.3)) * out
            ret(c, G, (k, k + 1, 0, 1), AMB, a, inset=16, width=7)
            if t < T_2 and a > 0:
                text_mid(c, str(k + 1), gx(G, k + 0.5), gy(G, 0.5), 72, "black", AMB, a)
    for blocos, t0, passo, t1, col in (([(0, 2), (1, 3), (2, 4)], T_2, 0.7, T_3, CYA),
                                      ([(0, 3), (1, 4)], T_3, 0.8, T_4, MNT)):
        if t0 <= t < t1:                        # de 2 e de 3 pedaços: um de cada vez
            for k, (i0, i1) in enumerate(blocos):
                tk = t0 + 0.3 + passo * k
                a = ep(t, tk, 0.15) * (1 - prog(t, t1 - 0.2 if k == len(blocos) - 1 else tk + passo - 0.1, 0.15))
                ret(c, G, (i0, i1, 0, 1), col, a, inset=10, width=10, fill=0.14)
                badge(c, str(k + 1), (gx(G, i0) + gx(G, i1)) / 2, gy(G, 0.5), a, col, r=36)
    if T_4 <= t < N["t_tot"]:                   # o inteiro
        a = ep(t, T_4 + 0.3, 0.2) * (1 - prog(t, N["t_tot"] - 0.2, 0.15))
        ret(c, G, (0, 4, 0, 1), WHITE, a, inset=6, width=12, fill=0.08)
        badge(c, "1", W / 2, gy(G, 0.5), a, WHITE, r=38)
    gancho(c, N, t, [("Quantos ", WHITE), ("retângulos", AMB), (" tem?", WHITE)], "conte todos os tamanhos")
    selo_torto(c, "PARECE FÁCIL", t, 1.3, N["t_conta"] - 0.2, QX1 - 160)
    label(c, "comenta a sua antes de ver ↓", QCX, QY0 + 175, ep(t, N["t_opc"] + 1.4, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3)),
          34, CYA, "black")
    contagem(c, N, t)
    placar(c, [("1 pedaço", 4, AMB, T_1 + 0.3, 0.5), ("2 pedaços", 3, CYA, T_2 + 0.3, 0.7), ("3 pedaços", 2, MNT, T_3 + 0.3, 0.8),
               ("inteiro", 1, WHITE, T_4 + 0.3, 0.5)], t, N["t_tot"] - 0.2, y0=QY0 + 58, dy=60, x_seta=440)
    a = ep(t, N["t_tot"], 0.3) * (1 - prog(t, T_ATALHO, 0.3))
    if a > 0:
        eq(c, [("4", AMB), (" + ", WHITE), ("3", CYA), (" + ", WHITE), ("2", MNT), (" + ", WHITE), ("1", WHITE),
               (" = ", WHITE), ("10", MNT)], QY0 + 120, a, size=90, cx=QCX, box=MNT if t > N["t_tot"] + 1.2 else None, maxw=880)
    opcoes(c, N, t, t_out=T_ATALHO)
    # o segredo: cada retângulo = 2 linhas de pé (âmbar) + 2 deitadas (ciano)
    a = ep(t, T_ATALHO, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a <= 0:
        return
    for k, (i0, i1) in enumerate([(1, 3), (0, 4), (2, 3)]):
        tk = T_ATALHO + 0.5 + 1.6 * k
        ak = ep(t, tk, 0.15) * (1 - prog(t, N["t_fim"] - 0.3 if k == 2 else tk + 1.5, 0.15)) * a
        if ak <= 0:
            continue
        ret(c, G, (i0, i1, 0, 1), MNT, ak * 0.8, inset=18, width=5, fill=0.16)
        y0, y1 = G["y0"], gy(G, 1)
        for i in (i0, i1):
            neon(c, (gx(G, i), y0 - 22), (gx(G, i), y1 + 22), AMB, ak, 12, 0.8)
        for y in (y0, y1):
            neon(c, (gx(G, i0) - 22, y), (gx(G, i1) + 22, y), CYA, ak, 12, 0.8)
    label(c, "todo retângulo usa", QCX, QY0 + 62, a, 36, INK2)
    a1 = ep(t, T_ATALHO + 0.9, 0.3) * a
    badge(c, "2", QX0 + 180, QY0 + 165, a1, AMB, r=34)
    text_mid(c, "linhas de pé", QX0 + 235, QY0 + 165, 54, "black", AMB, a1, align="left")
    a2 = ep(t, T_ATALHO + 2.0, 0.3) * a
    badge(c, "2", QX0 + 180, QY0 + 270, a2, CYA, r=34)
    text_mid(c, "linhas deitadas", QX0 + 235, QY0 + 270, 54, "black", CYA, a2, align="left")
    label(c, "escolheu as linhas, achou o retângulo", QCX, QY0 + 385, ep(t, T_ATALHO + 3.2, 0.3) * a, 34, MNT, "black")


# ---------------------------------------------------------------- nível 2 (3 colunas × 2 andares)
def nivel2(c, t):
    N, G = N2, G2
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    figura(c, G, t, N["t_hook"], ga)
    tr = N["t_rev"]
    larg_alt(c, G, t, tr + 0.2, 0.4, tr + 3.2, 0.6, tr + 5.3)
    piscando(c, G, todos(G), t, tr + 5.5, 0.12, MNT, N["t_fim"] - 0.3, inset=10, width=8, fill=0.14)
    gancho(c, N, t, [("E com ", WHITE), ("2 andares", AMB), ("?", WHITE)], "3 colunas · 2 andares")
    contagem(c, N, t)
    placar(c, [("largura", 6, AMB, tr + 0.2, 0.4), ("altura", 3, CYA, tr + 3.2, 0.6), ("6 × 3", 18, MNT, tr + 5.5, 0.12)],
           t, N["t_fim"] - 0.3, y0=QY0 + 75, dy=78, x_seta=400)
    opcoes(c, N, t)


# ---------------------------------------------------------------- chefão (grade 3 × 3)
def nivel3(c, t):
    N, G = N3, G3
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    figura(c, G, t, N["t_hook"], ga)
    tr = N["t_rev"]
    larg_alt(c, G, t, tr + 0.2, 0.3, tr + 2.1, 0.3, tr + 3.85)
    piscando(c, G, todos(G), t, tr + 4.0, 0.06, MNT, N["t_fim"] - 0.3, inset=10, width=8, fill=0.14)
    gancho(c, N, t, [("Grade ", WHITE), ("3 × 3", AMB), ("!", WHITE)], "9 casas")
    selo_torto(c, "NÍVEL DIFÍCIL", t, N["t_hook"] + 0.5, N["t_conta"] - 0.2, QX1 - 150)
    contagem(c, N, t)
    placar(c, [("largura", 6, AMB, tr + 0.2, 0.3), ("altura", 6, CYA, tr + 2.1, 0.3), ("6 × 6", 36, MNT, tr + 4.0, 0.06)],
           t, N["t_fim"] - 0.3, y0=QY0 + 75, dy=78, x_seta=400)
    popill(c, "QUADRADO TAMBÉM É RETÂNGULO", QCX, 930, 30, CYA, BG0, 1 - prog(t, N["t_fim"] - 0.3, 0.3), t, N["t_tot"] + 1.4)
    opcoes(c, N, t)


# ---------------------------------------------------------------- final
def cta(c, t):
    a = ep(t, T_CTA, 0.35)
    if a <= 0:
        return
    eq(c, [("Quantos você ", WHITE), ("acertou", AMB), ("?", WHITE)], QY0 - 520, a, size=72, cx=QCX, maxw=900)
    for k in range(4):                         # placar 0 · 1 · 2 · 3 para comentar
        ak = ep(t, T_CTA + 0.4 + 0.2 * k, 0.3)
        x = QCX + (k - 1.5) * 200
        if ak > 0:
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 80, QY0 - 420, 160, 160), 28, 28)
            col = [RED, AMB, CYA, MNT][k]
            c.drawRRect(r, blur_paint(col, 0.3 * ak, 18))
            c.drawRRect(r, paint(BG1, 0.95 * ak))
            c.drawRRect(r, paint(col, ak, stroke=5))
            text_mid(c, str(k), x, QY0 - 340, 96, "black", col, ak)
    ab = ep(t, T_CTA + 1.4, 0.3)
    if ab > 0:
        y = QY0 + 110
        w1 = text_w("comenta o seu número", "black", 54)
        text_mid(c, "comenta o seu número", QCX - 40, y, 54, "black", WHITE, ab)
        check(c, QCX + w1 / 2 + 10, y, 28, ab, CYA)
    label(c, "largura × altura: o atalho dos retângulos", QCX, QY0 + 210, ep(t, T_CTA + 2.0, 0.3), 30, INK2)
    popill(c, "PRÓXIMO: QUANTOS CAMINHOS?", QCX, QY0 + 340, 34, CYA, BG0, 1.0, t, T_CTA + 2.6)


HEADERS = [(0.0, "DESAFIO"), (7.5, "PAUSE E CONTE"), (T_1, "1 PEDAÇO"), (T_2, "2 PEDAÇOS"), (T_3, "3 PEDAÇOS"),
           (T_4, "O INTEIRO"), (21.5, "TOTAL"), (T_ATALHO, "O SEGREDO"), (N2["t_hook"], "NÍVEL 2"),
           (N2["t_conta"], "NÍVEL 2 · CONTE"), (N2["t_rev"], "NÍVEL 2 · RESPOSTA"), (N3["t_hook"], "NÍVEL CHEFÃO"),
           (N3["t_conta"], "CHEFÃO · CONTE"), (N3["t_rev"], "CHEFÃO · RESPOSTA"), (T_CTA, "E AÍ?")]


def frame(c, t_real):
    t = roteiro_t(t_real)
    BACKGROUND(c, t_real)
    s_ = "QUESTÃO DE MATEMÁTICA · 004"          # selo do canto (o mesmo das questões)
    pill(c, s_, 52 + (text_w(s_, "extrabold", 24) + 29) / 2, 80, 24, AMB, BG0, 0.95, "extrabold")
    for k, (t0, s) in enumerate(HEADERS):
        t1 = HEADERS[k + 1][0] if k + 1 < len(HEADERS) else DUR_ROTEIRO + 1
        if t0 <= t < t1:
            header_v(c, s, ep(t, t0, 0.25) * (1 - prog(t, t1 - 0.2, 0.2)))
    quadro(c, ep(t, 0.1, 0.4))
    nivel1(c, t)
    nivel2(c, t)
    nivel3(c, t)
    cta(c, t)
    legenda(c, t_real)


def narracao():
    """voz gravada + os silêncios de contagem (GAPS), 48 kHz, -14 LUFS, cauda de silêncio até DUR"""
    partes, ini, filt = [], 0.0, []
    for k, (g, d) in enumerate(GAPS + [(None, 0)]):
        fim = f":end={g}" if g is not None else ""
        filt.append(f"[0:a]atrim=start={ini}{fim},asetpts=PTS-STARTPTS[v{k}]")
        partes.append(f"[v{k}]")
        if d:
            filt.append(f"anullsrc=r=24000:cl=mono,atrim=duration={d}[s{k}]")
            partes.append(f"[s{k}]")
        ini = g
    filt.append("".join(partes) + f"concat=n={len(partes)}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11,"
                f"aresample=48000,apad=whole_dur={DUR}[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(VOZ), "-filter_complex", ";".join(filt), "-map", "[a]",
                    "-ac", "1", str(NARRACAO)], check=True)


def render_frame(t):
    surf = skia.Surface(W, H)
    frame(surf.getCanvas(), t)
    return surf


if __name__ == "__main__":
    out = HERE / "final"
    out.mkdir(exist_ok=True)
    if "--stills" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--stills") + 1].split(",")]
        d = HERE / "trabalho" / "stills"; d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.png"):
            f.unlink()
        for t in ts:
            render_frame(t).makeImageSnapshot().save(str(d / f"t{t:06.2f}.png"), skia.kPNG)
        print("ok", d)
        sys.exit()
    mudo = HERE / "trabalho" / "video_mudo.mp4"
    mudo.parent.mkdir(exist_ok=True)
    # Surface.makeImageSnapshot().tobytes() sai em BGRA neste skia (vermelho puro = 0,0,255,255)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mudo)], stdin=subprocess.PIPE)
    for f in range(int(DUR * FPS)):
        ff.stdin.write(render_frame(f / FPS).makeImageSnapshot().tobytes())
    ff.stdin.close(); ff.wait()
    if not COM_VOZ:
        dst = out / "estudativo_short_004_quantos_retangulos_sem_audio.mp4"
        subprocess.run(["cp", str(mudo), str(dst)], check=True)
        print(dst)
        sys.exit()
    narracao()
    dst = out / "estudativo_short_004_quantos_retangulos.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mudo), "-i", str(NARRACAO), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                    str(dst)], check=True)
    print(dst)
