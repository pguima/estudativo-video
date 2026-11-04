"""Short de engajamento (não é aula): "Quantos caminhos?" em 3 níveis. Vertical 1080x1920, 30 fps.
Mesmo formato dos Shorts 002–004: visual das questões de matemática (_ferramentas/matematica.py) em pé.
Uma grade de ruas; de A até B, só vale andar para a direita ou para baixo (os caminhos mais curtos).
Cores com função: âmbar = caminho / vem da esquerda, ciano = ruas / vem de cima, menta = certo, coral = erro.
Nível 1: 2 × 2 quarteirões → os 6 caminhos desenhados um por um (B) · o segredo: cada esquina = a de cima + a da esquerda
Nível 2: 3 × 2 → soma esquina por esquina = 10 (D)
Chefão: 3 × 3 → 20 (C) · os números das esquinas formam o triângulo de Pascal (diagonal 1 3 3 1)
As contagens foram conferidas por força bruta em conferir_contagens.py.

Sem a voz: sai final/..._sem_audio.mp4 na linha do tempo do roteiro.md.
Com a voz em audio/voz_original.wav + audio/palavras.json: preencher GAPS/ANCORAS/CORRIGE (como no Short 004) e rodar de
novo: as animações são deformadas para a voz e a legenda usa os tempos reais das palavras.
Uso: python3 render_short.py [--stills t1,t2,...]"""
import json
import os
import subprocess
import sys
from math import comb, sin
from pathlib import Path

os.environ["VIDEO_FORMATO"] = "vertical"          # antes de importar o motor
HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
from matematica import *  # noqa
from motor import W, H, FPS

# ---------------------------------------------------------------- linha do tempo (s) = a do roteiro.md
FALAS = [
    (0.0, 3.0, "Quantos caminhos vão de A até B?"),
    (3.0, 6.0, "Só vale andar pra direita ou pra baixo."),
    (6.0, 9.5, "4, 6, 8 ou 12? Comenta antes de ver!"),
    (9.5, 14.5, "Pausa e conta. Valendo!"),
    (14.5, 21.5, "Um por um: 1, 2, 3, 4, 5, 6!"),
    (21.5, 24.0, "6 caminhos. Letra B!"),
    (24.0, 28.5, "O segredo: cada esquina soma a de cima com a da esquerda."),
    (28.5, 33.0, "Na borda, 1. Depois 2, 3, 3... e 3 mais 3: 6!"),
    (33.0, 36.0, "Nível 2: e com 3 de largura?"),
    (36.0, 39.5, "8, 12, 6 ou 10?"),
    (39.5, 42.5, "3 segundos!"),
    (42.5, 47.5, "Soma esquina por esquina: 2, 3, 4... 3, 6, 10!"),
    (47.5, 50.0, "Dá 10! Letra D."),
    (50.0, 52.5, "Nível chefão: grade 3 por 3!"),
    (52.5, 56.0, "9, 12, 20 ou 27?"),
    (56.0, 59.0, "Valendo!"),
    (59.0, 64.0, "Mesma soma, esquina por esquina... e 10 mais 10: 20!"),
    (64.0, 66.5, "Letra C! E olha: é o triângulo de Pascal!"),
    (66.5, 71.5, "Quantos você acertou: 0, 1, 2 ou 3? Comenta! No próximo: quantos apertos de mão?"),
]
DUR_ROTEIRO = 71.5
DESTAQUE = {"caminhos": AMB, "A": AMB, "B?": AMB, "direita": AMB, "baixo.": AMB, "B!": MNT, "6!": MNT, "segredo:": AMB,
            "cima": CYA, "esquerda.": AMB, "largura?": AMB, "10!": MNT, "D.": MNT, "chefão:": RED, "20!": MNT, "C!": MNT,
            "Pascal!": CYA, "Comenta!": CYA, "mão?": CYA}

# ---------------------------------------------------------------- sincronia com a narração gravada (quando chegar)
VOZ = HERE / "audio" / "voz_original.wav"
NARRACAO = HERE / "audio" / "narracao.wav"
# a voz veio no ritmo de Short: silêncio aberto depois de "Valendo!", entre os números de "1, 2, 3, 4, 5, 6" (cada caminho tem
# tempo de ser desenhado), depois do "6!" do segredo, de "3 segundos!", do 2º "Valendo!" e antes de "e 10 mais 10"
GAPS = [(10.00, 3.2), (11.24, 0.35), (11.64, 0.35), (12.04, 0.35), (12.40, 0.35), (12.91, 0.35), (24.90, 0.8),
        (31.40, 1.7), (44.50, 2.1), (46.49, 1.0)]   # (posição no áudio original, segundos de silêncio)
ANCORAS = [(0.0, 0.0), (3.0, 2.54), (6.0, 5.24), (9.5, 8.56), (14.5, 10.20), (15.5, 10.94), (16.4, 11.28), (17.3, 11.68),
           (18.2, 12.12), (19.1, 12.48), (20.0, 12.94), (21.5, 13.70), (22.4, 14.64), (24.0, 15.64), (28.5, 19.14),
           (29.7, 20.58), (30.3, 21.46), (30.9, 22.20), (31.9, 23.26), (33.0, 25.33), (36.0, 27.80), (39.5, 30.32),
           (42.5, 31.76), (43.6, 33.10), (44.25, 33.54), (44.9, 34.06), (45.55, 34.66), (46.2, 35.28), (46.85, 35.78),
           (47.5, 36.46), (48.4, 37.16), (50.0, 38.16), (52.5, 41.02), (56.0, 43.80), (59.0, 44.75), (63.2, 46.70),
           (64.0, 47.72), (64.9, 48.40), (65.0, 49.44), (65.3, 50.16), (66.5, 51.78), (69.1, 55.88), (71.5, 58.90)]
CORRIGE = {2.68: "vale", 6.54: "12?", 7.92: "ver!", 9.54: "Valendo!", 12.92: "6!", 14.96: "B!", 15.84: "segredo:",
           19.26: "borda,", 22.20: "3...", 24.28: "= 6!", 25.54: "2:", 26.90: "largura?", 29.78: "10?", 30.68: "segundos!",
           32.52: "esquina:", 36.46: "Dá", 36.66: "10!", 38.52: "chefão:", 40.32: "3!", 43.08: "27?", 43.80: "Valendo!",
           45.94: "esquina...", 35.78: "10!", 47.72: "= 20!", 48.76: "C!", 49.58: "olha:", 50.84: "Pascal!", 54.62: "3?",
           54.90: "Comenta!", 56.06: "próximo:", 56.66: "quantos", 57.16: "apertos", 57.76: "mão?"}  # {início da palavra: texto}
INICIO = {25.16: 25.33, 27.28: 27.80, 31.60: 31.76, 11.04: 10.94, 11.22: 11.28, 11.64: 11.68, 12.02: 12.12,
          12.68: 12.48, 12.92: 12.94, 46.38: 46.58}  # palavra que a transcrição começou fora do lugar: {início: início real}
SOMA = {23.54, 47.06}                      # "mais" das contas: vira "+ 3" junto com o número seguinte
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
N1 = dict(opc=[("A", "4"), ("B", "6"), ("C", "8"), ("D", "12")], certa="B",
          t_hook=0.0, t_opc=6.0, t_conta=9.5, dur_conta=5, t_rev=14.5, t_tot=21.5, t_fim=33.0)
N2 = dict(opc=[("A", "8"), ("B", "12"), ("C", "6"), ("D", "10")], certa="D",
          t_hook=33.0, t_opc=36.0, t_conta=39.5, dur_conta=3, t_rev=42.5, t_tot=47.5, t_fim=50.0)
N3 = dict(opc=[("A", "9"), ("B", "12"), ("C", "20"), ("D", "27")], certa="C",
          t_hook=50.0, t_opc=52.5, t_conta=56.0, dur_conta=3, t_rev=59.0, t_tot=64.0, t_fim=66.5)
T_REGRA, T_CAM0, P_CAM = 3.0, 15.5, 0.9                # nível 1: a regra, o 1º caminho, um caminho a cada 0,9 s
T_SEG, T_PASCAL, T_CTA = 24.0, 65.0, 66.5
# soma das esquinas (borda, 1ª de dentro, passo) — no nível 1, as de dentro casam com "2, 3, 3... 3 mais 3: 6"
SOMA_N1 = (28.6, [29.7, 30.3, 30.9, 31.9])
SOMA_N2 = (42.7, 43.6, 0.65)
SOMA_N3 = (59.2, 59.6, 0.45)

# ---------------------------------------------------------------- geometria (px): grades de ruas, cols × rows quarteirões
G1 = dict(cols=2, rows=2, x0=310.0, y0=380.0, s=230.0, r=40)
G2 = dict(cols=3, rows=2, x0=225.0, y0=420.0, s=210.0, r=37)
G3 = dict(cols=3, rows=3, x0=285.0, y0=330.0, s=170.0, r=33)


def px(G, i):
    return G["x0"] + i * G["s"]


def py(G, j):
    return G["y0"] + j * G["s"]


def val(i, j):
    """caminhos de A até a esquina (i, j)"""
    return comb(i + j, i)


def caminhos(G):
    """todos os caminhos (sequências de "R"/"D"), em ordem"""
    from itertools import product
    return ["".join(m) for m in product("RD", repeat=G["cols"] + G["rows"]) if m.count("R") == G["cols"]]


def internas(G):
    """esquinas de dentro (as que somam), linha por linha"""
    return [(i, j) for j in range(1, G["rows"] + 1) for i in range(1, G["cols"] + 1)]


assert [len(caminhos(G)) for G in (G1, G2, G3)] == [6, 10, 20]
assert [val(G["cols"], G["rows"]) for G in (G1, G2, G3)] == [6, 10, 20]
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


def ruas(c, G, t, t0, a):
    """a grade de ruas: quarteirões bem leves + traço neon ciano, desenhada de cima/esquerda"""
    if a <= 0:
        return
    u = ep(t, t0 + 0.15, 0.9)
    s = G["s"]
    for i in range(G["cols"]):
        for j in range(G["rows"]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(px(G, i) + 22, py(G, j) + 22, s - 44, s - 44), 16, 16)
            c.drawRRect(r, paint(CYA, 0.07 * a * u))
    x1, y1 = px(G, G["cols"]), py(G, G["rows"])
    for i in range(G["cols"] + 1):
        neon(c, (px(G, i), G["y0"]), (px(G, i), y1), CYA, a * 0.8, 7, 0.4, u)
    for j in range(G["rows"] + 1):
        neon(c, (G["x0"], py(G, j)), (x1, py(G, j)), CYA, a * 0.8, 7, 0.4, u)


def ponto(c, s, cx, cy, a, col):
    """A e B: bolinha com brilho, ao lado da esquina"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, 40, blur_paint(col, 0.5 * a, 16))
    c.drawCircle(cx, cy, 34, paint(col, a))
    text_mid(c, s, cx, cy, 40, "black", BG0, a)


def pontos(c, G, a):
    ponto(c, "A", G["x0"] - G["r"] - 46, G["y0"], a, AMB)
    ponto(c, "B", px(G, G["cols"]) + G["r"] + 46, py(G, G["rows"]), a, MNT)
    c.drawCircle(G["x0"], G["y0"], 11, paint(AMB, a))
    c.drawCircle(px(G, G["cols"]), py(G, G["rows"]), 11, paint(MNT, a))


def seta(c, p, q, col, a, w=10):
    if a <= 0:
        return
    neon(c, p, q, col, a, w, 0.7)
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / n, dy / n
    for sg in (1, -1):
        neon(c, q, (q[0] - 26 * ux + sg * 18 * uy, q[1] - 26 * uy - sg * 18 * ux), col, a, w, 0.7)


def caminho(c, G, m, col, a, u=1.0, w=12, glow=0.7):
    """um caminho ("RRDD"...) desenhado até a fração u do comprimento"""
    if a <= 0 or u <= 0:
        return
    i = j = 0
    n = len(m)
    for k, d in enumerate(m):
        f = clamp(u * n - k)
        if f <= 0:
            break
        i1, j1 = (i + 1, j) if d == "R" else (i, j + 1)
        neon(c, (px(G, i), py(G, j)), (px(G, i1), py(G, j1)), col, a, w, glow, f)
        i, j = i1, j1


def esquina(c, G, i, j, a, col, k=1.0):
    """número da esquina (caminhos até ela)"""
    if a <= 0:
        return
    r = G["r"] * k
    x, y = px(G, i), py(G, j)
    c.drawCircle(x, y, r + 6, blur_paint(col, 0.35 * a, 12))
    c.drawCircle(x, y, r, paint(BG1, a))
    c.drawCircle(x, y, r, paint(col, a, stroke=5))
    v = str(val(i, j))
    text_mid(c, v, x, y, r * (1.05 if len(v) == 1 else 0.9), "black", WHITE if col != MNT else MNT, a)


def somas(c, G, t, t_borda, tempos, fim, a_all=1.0):
    """borda = 1 (ciano); as de dentro acendem uma a uma (âmbar; a última, B, em menta) com as duas ruas que chegam
    nela piscando: de cima (ciano) e da esquerda (âmbar). Devolve a esquina sendo somada agora (ou None)."""
    out = 1 - prog(t, fim - 0.3, 0.3)
    ativa = None
    ints = internas(G)
    for k, (i, j) in enumerate(ints):                # as duas ruas que chegam: por baixo dos números
        tk, prox = tempos[k], tempos[k + 1] if k + 1 < len(ints) else fim
        if tk - 0.05 <= t < prox:
            ativa = (i, j)
            a = ep(t, tk - 0.05, 0.1) * (1 - prog(t, prox - 0.1, 0.1)) * a_all
            neon(c, (px(G, i), py(G, j - 1)), (px(G, i), py(G, j)), CYA, a, 12, 0.9)
            neon(c, (px(G, i - 1), py(G, j)), (px(G, i), py(G, j)), AMB, a, 12, 0.9)
    for i in range(G["cols"] + 1):
        for j in range(G["rows"] + 1):
            if i == 0 or j == 0:
                esquina(c, G, i, j, ep(t, t_borda + 0.06 * (i + j), 0.2) * out * a_all, CYA, pop(t, t_borda + 0.06 * (i + j), 0.3))
    for k, (i, j) in enumerate(ints):
        tk = tempos[k]
        if t < tk - 0.05:
            continue
        ult = k == len(ints) - 1
        esquina(c, G, i, j, ep(t, tk, 0.15) * out * a_all, MNT if ult else AMB, pop(t, tk, 0.35))
    return ativa


def conta_esquina(c, ij, y, a, size=90, box=False):
    """no quadro: de cima + da esquerda = valor"""
    if ij is None or a <= 0:
        return
    i, j = ij
    eq(c, [(str(val(i, j - 1)), CYA), (" + ", WHITE), (str(val(i - 1, j)), AMB), (" = ", WHITE), (str(val(i, j)), MNT if box else AMB)],
       y, a, size=size, cx=QCX, box=MNT if box else None, maxw=880)


def regra_quadro(c, y, a):
    """de cima (ciano) + da esquerda (âmbar)"""
    eq(c, [("de cima", CYA), (" + ", WHITE), ("da esquerda", AMB)], y, a, size=56, cx=QCX, maxw=880)


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


# ---------------------------------------------------------------- nível 1 (2 × 2 quarteirões)
def nivel1(c, t):
    N, G = N1, G1
    if t >= N["t_fim"] + 0.3:
        return
    ga = 1 - prog(t, N["t_fim"] - 0.3, 0.3)
    ruas(c, G, t, N["t_hook"], ga)
    pontos(c, G, ga * ep(t, 0.3, 0.3))
    # a regra: setinhas saindo do A, pra direita e pra baixo
    ar = ep(t, T_REGRA + 0.2, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3)) * (0.75 + 0.25 * sin(6 * t))
    seta(c, (G["x0"] + 20, G["y0"]), (G["x0"] + 0.62 * G["s"], G["y0"]), AMB, ar)
    seta(c, (G["x0"], G["y0"] + 20), (G["x0"], G["y0"] + 0.62 * G["s"]), AMB, ar)
    # um por um: o atual em âmbar, os anteriores ficam em menta fraco
    cams = caminhos(G)
    if N["t_rev"] <= t < T_SEG:
        fade = 1 - prog(t, T_SEG - 0.4, 0.4)
        for k, m in enumerate(cams):
            tk = T_CAM0 + P_CAM * k
            if t < tk:
                break
            atual = t < tk + P_CAM and k < len(cams) - 1 or (k == len(cams) - 1 and t < N["t_tot"])
            if atual:
                caminho(c, G, m, AMB, fade, ep(t, tk, 0.55), 13, 0.8)
            else:
                caminho(c, G, m, MNT, 0.32 * fade + 0.45 * fade * (t >= N["t_tot"]) * (1 - prog(t, N["t_tot"] + 0.3, 0.6)), 1.0, 7, 0.3)
    gancho(c, N, t, [("Quantos ", WHITE), ("caminhos", AMB), (" de A até B?", WHITE)])
    a = ep(t, T_REGRA, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3))
    eq(c, [("só vale ", INK2), ("→", AMB), (" ou ", INK2), ("↓", AMB)], QY0 + 190, a, size=56, cx=QCX, maxw=880)
    selo_torto(c, "PARECE FÁCIL", t, 1.3, N["t_conta"] - 0.2, QX1 - 160)
    label(c, "comenta antes de ver ↓", QCX, QY0 + 265, ep(t, N["t_opc"] + 1.4, 0.3) * (1 - prog(t, N["t_conta"] - 0.2, 0.3)),
          34, CYA, "black")
    contagem(c, N, t)
    # contador dos caminhos
    n = sum(1 for k in range(len(cams)) if t >= T_CAM0 + P_CAM * k)
    a = ep(t, T_CAM0, 0.3) * (1 - prog(t, T_SEG, 0.3))
    if a > 0 and n > 0:
        k_ = 1 + 0.25 * (1 - ease_out(clamp((t - T_CAM0 - P_CAM * (n - 1)) / 0.25)))
        eq(c, [(str(n), AMB if t < N["t_tot"] else MNT), (" caminho" + ("s" if n > 1 else ""), WHITE)], QY0 + 120, a,
           size=int(90 * k_), cx=QCX, box=MNT if t > N["t_tot"] + 0.2 else None, maxw=880)
    opcoes(c, N, t, t_out=T_SEG)
    # o segredo: cada esquina = a de cima + a da esquerda
    a = ep(t, T_SEG, 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a <= 0:
        return
    ativa = somas(c, G, t, SOMA_N1[0], SOMA_N1[1], N["t_fim"])
    label(c, "cada esquina =", QCX, QY0 + 62, a, 36, INK2)
    regra_quadro(c, QY0 + 150, ep(t, T_SEG + 0.8, 0.3) * a)
    conta_esquina(c, ativa, QY0 + 300, a, 84, box=ativa == (2, 2))
    if ativa is None and t >= SOMA_N1[0]:
        label(c, "na borda, só 1 jeito", QCX, QY0 + 300, ep(t, SOMA_N1[0], 0.3) * a, 40, CYA, "black")


# ---------------------------------------------------------------- nível 2 (3 × 2 quarteirões)
def nivel(c, t, N, G, t_borda, tempos, hook, sub, selo=None):
    if not (N["t_hook"] - 0.1 <= t < N["t_fim"] + 0.3):
        return None
    ga = ep(t, N["t_hook"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    ruas(c, G, t, N["t_hook"], ga)
    pontos(c, G, ga * ep(t, N["t_hook"] + 0.3, 0.3))
    ativa = somas(c, G, t, t_borda, tempos, N["t_fim"]) if t >= N["t_rev"] else None
    gancho(c, N, t, hook, sub)
    if selo:
        selo_torto(c, selo, t, N["t_hook"] + 0.5, N["t_conta"] - 0.2, QX1 - 150)
    contagem(c, N, t)
    a = ep(t, N["t_rev"], 0.3) * (1 - prog(t, N["t_fim"] - 0.3, 0.3))
    if a > 0:
        regra_quadro(c, QY0 + 62, a * 0.85)
        fim = (G["cols"], G["rows"])
        if ativa is None and t < tempos[0]:
            label(c, "na borda, só 1 jeito", QCX, QY0 + 160, ep(t, t_borda, 0.3) * a, 40, CYA, "black")
        conta_esquina(c, ativa if ativa else (fim if t >= tempos[-1] else None), QY0 + 170, a, 88,
                      box=(ativa or fim) == fim and t >= tempos[-1])
    opcoes(c, N, t)
    return ga


def nivel2(c, t):
    b, i0, p = SOMA_N2
    nivel(c, t, N2, G2, b, [i0 + p * k for k in range(len(internas(G2)))],
          [("E com ", WHITE), ("3 de largura", AMB), ("?", WHITE)], "3 quarteirões × 2")


def nivel3(c, t):
    b, i0, p = SOMA_N3
    G = G3
    ga = nivel(c, t, N3, G, b, [i0 + p * k for k in range(len(internas(G)))],
               [("Grade ", WHITE), ("3 × 3", AMB), ("!", WHITE)], "mesma regra: só → ou ↓", "NÍVEL DIFÍCIL")
    if not ga:
        return
    # o triângulo de Pascal: a diagonal 1 3 3 1
    a = ep(t, T_PASCAL, 0.3) * (1 - prog(t, N3["t_fim"] - 0.3, 0.3))
    if a > 0:
        pts = [(px(G, 3 - j), py(G, j)) for j in range(4)]
        neon(c, (pts[0][0] + 40, pts[0][1] - 40), (pts[-1][0] - 40, pts[-1][1] + 40), MNT, a * 0.7, 8, 0.6,
             ep(t, T_PASCAL, 0.5))
        for j in range(4):
            esquina(c, G, 3 - j, j, a, MNT)
    popill(c, "É O TRIÂNGULO DE PASCAL", QCX, 930, 30, CYA, BG0, 1 - prog(t, N3["t_fim"] - 0.3, 0.3), t, T_PASCAL + 0.3)


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
    label(c, "cada esquina = a de cima + a da esquerda", QCX, QY0 + 210, ep(t, T_CTA + 2.0, 0.3), 30, INK2)
    popill(c, "PRÓXIMO: QUANTOS APERTOS DE MÃO?", QCX, QY0 + 340, 34, CYA, BG0, 1.0, t, T_CTA + 2.6)


HEADERS = [(0.0, "DESAFIO"), (N1["t_conta"], "PAUSE E CONTE"), (N1["t_rev"], "UM POR UM"), (N1["t_tot"], "TOTAL"),
           (T_SEG, "O SEGREDO"), (N2["t_hook"], "NÍVEL 2"), (N2["t_conta"], "NÍVEL 2 · CONTE"),
           (N2["t_rev"], "NÍVEL 2 · RESPOSTA"), (N3["t_hook"], "NÍVEL CHEFÃO"), (N3["t_conta"], "CHEFÃO · CONTE"),
           (N3["t_rev"], "CHEFÃO · RESPOSTA"), (T_CTA, "E AÍ?")]


def frame(c, t_real):
    t = roteiro_t(t_real)
    BACKGROUND(c, t_real)
    s_ = "QUESTÃO DE MATEMÁTICA · 005"          # selo do canto (o mesmo das questões)
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
        dst = out / "estudativo_short_005_quantos_caminhos_sem_audio.mp4"
        subprocess.run(["cp", str(mudo), str(dst)], check=True)
        print(dst)
        sys.exit()
    narracao()
    dst = out / "estudativo_short_005_quantos_caminhos.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mudo), "-i", str(NARRACAO), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                    str(dst)], check=True)
    print(dst)
